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
    theme toggle, the sidebar TOC and the figure/plotting code."""
    js = library.read(os.path.join(library.ASSETS, "book.js"))
    js = js.replace("numberEquations();", "/* numbered at build time */")
    js = re.sub(r"if \(window\.katex\) \{ typeset\(\); \}.*?\n  \}\);", "});", js, flags=re.S)
    return js


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — {book}</title>
<style>
{katexcss}
</style>
<style>
{bookcss}
</style>
</head>
<body>
<div class="wrap">
<nav class="sidebar">
  <a class="sb-home" href="index.html">← Newton to M-Theory</a>
  <p class="sb-title">{sbhead}</p>
  <div id="sb-toc">{toc}</div>
</nav>
<main class="main">
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
    print("stage 0 — extracting the through-line")
    tspec = importlib.util.spec_from_file_location("tl", os.path.join(os.path.dirname(os.path.abspath(__file__)), "throughline.py"))
    tl = importlib.util.module_from_spec(tspec); tspec.loader.exec_module(tl)
    tl.build()

    print("stage 1 — assembling fragments")
    shutil.rmtree(STAGE, ignore_errors=True)
    bp.build()

    print("stage 2 — rendering maths and inlining assets")
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)
    kcss, bcss, rt = katex_css_inlined(), library.read(os.path.join(library.ASSETS, "book.css")), runtime_js()
    n = 0

    async with async_playwright() as pw:
        b = await pw.chromium.launch()

        async def render(src, title, sbhead, wide, extra, dest):
            pg = await b.new_page(viewport={"width": 1280, "height": 1000})
            await pg.goto("file://" + src)
            await pg.wait_for_timeout(2400)
            # Rewind any animated figure before the DOM is saved, so two builds of
            # identical source produce identical files.
            await pg.evaluate("() => { if (window.NMT && NMT.resetForSnapshot) NMT.resetForSnapshot(); }")
            await pg.wait_for_timeout(60)
            body = await pg.evaluate("document.querySelector('.main .col').innerHTML")
            toc = await pg.evaluate("document.getElementById('sb-toc').innerHTML")
            left = await pg.evaluate(
                "(document.body.innerText.match(/\\\\[a-zA-Z]+\\{/g)||[]).length")
            bad = await pg.evaluate("document.querySelectorAll('.katex-error').length")
            await pg.close()
            if left or bad:
                print(f"   !! {os.path.basename(dest)}: {left} unrendered, {bad} katex errors")
            body = body.replace('href="chapters/', 'href="')
            library.write(dest, SHELL.format(
                title=title, book=BOOK.title, katexcss=kcss, bookcss=bcss, sbhead=sbhead,
                toc=toc, body=body, wide=wide, runtime=rt, extra=extra))

        for num, slug, title, part, _m in bp.FLAT:
            src = os.path.join(STAGE, "chapters", slug + ".html")
            if not os.path.exists(src):
                continue
            raw = library.read(BOOK.chapter_path(slug))
            m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
            extra = "<script>\n" + m.group(1) + "\n</script>" if m else ""
            await render(src, f"{num} {title}", f"Ch {num}", "", extra,
                         os.path.join(OUT, slug + ".html"))
            n += 1

        TITLES = {"index": "Contents", "ledger": "Math Ledger",
                  "throughline": "The Through-Line"}
        for name, sbhead in (("index", "Parts"), ("ledger", "Ledger"),
                             ("throughline", "Through-Line")):
            src = os.path.join(STAGE, name + ".html")
            if os.path.exists(src):
                await render(src, TITLES[name], sbhead, " wide", "",
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
