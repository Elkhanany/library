#!/usr/bin/env python3
"""
The offline build — one book at a time.

Two stages, one output.

  stage 1  build.py assembles each src/ fragment into a working page in .staging/,
           with KaTeX loaded from vendor/. Nothing ships from here.
  stage 2  each staged page is opened in headless Chromium so KaTeX renders, the
           equations are numbered and the cross-references resolved; the finished
           DOM is then written into build/ with the stylesheet and the maths fonts
           inlined.

The result is one flat folder of completely self-contained files. No relative
asset paths, no network, no JS needed to see an equation — so a chapter renders
identically opened from disk, from Dropbox on a phone, or as a mail attachment.
Pages also paint faster than the staged versions, which had to typeset a thousand
expressions on load.

    python3 make.py
"""
import os, re, base64, asyncio, shutil, importlib.util
from playwright.async_api import async_playwright

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
BOOK = library.book(os.environ.get("NMT_BOOK", "newton-to-mtheory"))
ROOT = library.ROOT
STAGE = os.path.join(ROOT, ".staging", BOOK.slug)
OUT = os.path.join(ROOT, "build", BOOK.slug)
VEND = os.path.join(library.VENDOR, "katex")

spec = importlib.util.spec_from_file_location("bp", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)


def katex_css_inlined():
    """KaTeX's stylesheet with every woff2 we still ship embedded as a data URI.
    @font-face blocks whose file has been pruned are dropped entirely."""
    css = library.read(os.path.join(VEND, "katex.min.css"))
    have, cache = set(os.listdir(os.path.join(VEND, "fonts"))), {}

    def repl(m):
        fn = os.path.basename(m.group(1))
        if not fn.endswith(".woff2"):
            return m.group(0)
        if fn not in have:
            return "url(about:blank)"
        if fn not in cache:
            cache[fn] = base64.b64encode(
                open(os.path.join(VEND, "fonts", fn), "rb").read()).decode()
        return "url(data:font/woff2;base64,%s)" % cache[fn]

    css = re.sub(r"url\(([^)]+)\)", repl, css)
    css = re.sub(r',\s*url\(fonts/[^)]+\)\s*format\("(woff|truetype)"\)', "", css)
    css = re.sub(r"@font-face\{[^}]*url\(about:blank\)[^}]*\}", "", css)
    return css


def runtime_js():
    """book.js minus the KaTeX pass — the maths is already rendered. Keeps the
    theme toggle, the sidebar TOC and the figure/plotting code.

    THE BOOT-SHAPE CONTRACT (DESIGN.md section 8, "book.js boot shape"). Two text
    substitutions in shared/assets/book.js, each of which must happen exactly once:
      1. the literal `numberEquations();`, the boot handler's first statement,
         becomes a comment. Missing, the Dropbox pages number every equation a
         second time over the numbers baked in here.
      2. everything from `if (window.katex) { typeset(); }` to the handler's
         closing `\\n  });` is deleted, so the katex if/else block must be the
         LAST thing in the handler. A boot call placed after it vanishes from
         every page this script writes.
    New boot calls go after `numberEquations();` and before `if (window.katex)`.
    This is a copy of webbuild.runtime_js(); change the two together. The
    contract comment above the handler in book.js is dropped here too."""
    js = library.read(os.path.join(library.ASSETS, "book.js"))
    law = ("runtime_js(): shared/assets/book.js breaks the boot-shape contract "
           "(DESIGN.md section 8, 'book.js boot shape'): ")
    js, n = re.subn(r"\n  /\* ---------- boot contract .*?\*/", "", js, flags=re.S)
    if n > 1:
        raise RuntimeError(law + "the boot-contract comment appears %d times" % n)
    n = js.count("numberEquations();")
    if n != 1:
        raise RuntimeError(law + "expected exactly one 'numberEquations();' (the boot "
                           "handler's first statement), found %d" % n)
    js = js.replace("numberEquations();", "/* numbered at build time */")
    js, n = re.subn(r"if \(window\.katex\) \{ typeset\(\); \}.*?\n  \}\);", "});", js, flags=re.S)
    if n != 1:
        raise RuntimeError(law + "expected the boot handler to end with exactly one "
                           "'if (window.katex) { typeset(); } else {...}' block closed by "
                           "'\\n  });', found %d" % n)
    return js


# The sidebar's section list without the spy's state (webbuild.TOC_JS).
TOC_JS = """() => {
                const t = document.getElementById('sb-toc').cloneNode(true);
                t.querySelectorAll('.active, [aria-current]').forEach(a => {
                  a.classList.remove('active'); a.removeAttribute('aria-current');
                  if (!a.className) a.removeAttribute('class'); });
                return t.innerHTML; }"""


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} — {book}</title>
<style>
{katexcss}
</style>
<style>
{bookcss}{themecss}
</style>
<style>
{navcss}
:root{{--lib-bar-h:0px}}
</style>
</head>
<body>
<div class="wrap">
<nav class="sidebar" aria-label="Chapter sections">
{side}
  <div id="sb-toc">{toc}</div>
</nav>
<main class="main" id="text">
<div class="col{wide}">
{body}
</div>
</main>
</div>
<script>
{runtime}
</script>
{extra}
</body>
</html>
"""


async def main():
    # Only for a book that asked for one. Run unconditionally, this writes an
    # empty _throughline.html into the src/ of every book in the library, and a
    # book with no plain-language layer should not acquire an empty one by
    # being built.
    if BOOK.has("throughline"):
        print("stage 0 — extracting the through-line")
        tspec = importlib.util.spec_from_file_location("tl", os.path.join(os.path.dirname(os.path.abspath(__file__)), "throughline.py"))
        tl = importlib.util.module_from_spec(tspec); tspec.loader.exec_module(tl)
        tl.build()

    print("stage 1 — assembling fragments")
    shutil.rmtree(STAGE, ignore_errors=True)
    # build.py points itself at the physics book when it loads, which was right
    # when there was one. Without this, NMT_BOOK selects the staging directory
    # and the output directory but not the source, so asking for any other book
    # quietly assembles the physics one into a folder named for the book you
    # asked for. webbuild.py has always done this; make.py never did.
    bp.use(BOOK)
    bp.OUT = STAGE
    bp.build()

    print("stage 2 — rendering maths and inlining assets")
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)
    kcss, bcss, rt = katex_css_inlined(), library.read(os.path.join(library.ASSETS, "book.css")), runtime_js()
    # The book's own palette, as docs/ appends it to book.css, so a Dropbox copy
    # of the clinical book is not printed in the physics book's blue. Then
    # nav.css, which carries the library's type stacks, the drawer and the
    # theme-toggle fallback (#themer), and then the bar height at 0: there is
    # no bar in these files, and scroll padding, the sidebar's top and
    # anything else sized from --lib-bar-h must not leave room for one.
    tcss = library.themecss(BOOK)
    ncss = library.read(os.path.join(library.ASSETS, "nav.css"))
    n = 0

    async with async_playwright() as pw:
        b = await pw.chromium.launch()

        async def render(src, title, side, wide, extra, dest):
            pg = await b.new_page(viewport={"width": 1280, "height": 1000})
            await pg.goto("file://" + src)
            await pg.wait_for_timeout(2400)
            # Rewind any animated figure before the DOM is saved, so two builds of
            # identical source produce identical files.
            await pg.evaluate("() => { if (window.NMT && NMT.resetForSnapshot) NMT.resetForSnapshot(); }")
            await pg.wait_for_timeout(60)
            body = await pg.evaluate("document.querySelector('.main .col').innerHTML")
            toc = await pg.evaluate(TOC_JS)
            left = await pg.evaluate(
                "(document.body.innerText.match(/\\\\[a-zA-Z]+\\{/g)||[]).length")
            bad = await pg.evaluate("document.querySelectorAll('.katex-error').length")
            await pg.close()
            if left or bad:
                print(f"   !! {os.path.basename(dest)}: {left} unrendered, {bad} katex errors")
            body = body.replace('href="chapters/', 'href="')
            library.write(dest, SHELL.format(
                title=title, book=BOOK.title, katexcss=kcss, bookcss=bcss, side=side,
                themecss=tcss, navcss=ncss,
                toc=toc, body=body, wide=wide, runtime=rt, extra=extra))

        for num, slug, title, part, _m in bp.FLAT:
            src = os.path.join(STAGE, "chapters", slug + ".html")
            if not os.path.exists(src):
                continue
            raw = library.read(BOOK.chapter_path(slug))
            m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
            extra = "<script>\n" + m.group(1) + "\n</script>" if m else ""
            # Here the contents page is index.html, so a chapter's up-link goes
            # to index.html#sec-<i>; and there is no pwa.js, so the arrows'
            # titles name no arrow keys.
            await render(src, f"{num} {title}",
                         bp.sidebar_head("chapter", slug, contents="index.html", keys=False),
                         "", extra, os.path.join(OUT, slug + ".html"))
            n += 1

        # One name per destination, as on the site (webbuild.py). Only the
        # contents page and the ledger take the wide column.
        for name, page, title, wide in (("index", "contents", "Contents", " wide"),
                                        ("ledger", "ledger", "Math Ledger", " wide"),
                                        ("throughline", "throughline", "In Plain Terms", "")):
            src = os.path.join(STAGE, name + ".html")
            if os.path.exists(src):
                await render(src, title, bp.sidebar_head(page), wide, "",
                             os.path.join(OUT, name + ".html"))
        await b.close()

    for f in ("PLAN.md", "MATHPLAN-2.5-2.6.md"):
        if os.path.exists(os.path.join(ROOT, f)):
            shutil.copy(os.path.join(ROOT, f), OUT)
    shutil.rmtree(STAGE, ignore_errors=True)

    tot = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)
              if os.path.isfile(os.path.join(OUT, f)))
    print(f"\nbuilt {n} chapters + index + ledger -> build/  ({tot/1e6:.0f} MB, self-contained)")


asyncio.run(main())
