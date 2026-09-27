#!/usr/bin/env python3
"""
Emit docs/ — the GitHub Pages site.

Differs from build/ in one way that matters: the website shares one stylesheet and
one set of maths fonts across every page instead of inlining them into each file.
That is wrong for Dropbox (where each file is previewed in isolation and relative
paths do not resolve) and right for a web server (where the browser caches them
once). Same source, two targets, no duplicated content.
"""
import os, re, shutil, html, importlib.util, asyncio
from playwright.async_api import async_playwright

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
import nav
import pwa

ROOT = library.ROOT
STAGE = os.path.join(ROOT, ".webstage")
DOCS = library.DOCS
VEND = os.path.join(library.VENDOR, "katex")
BOOK = None                 # set per book by build_book()

spec = importlib.util.spec_from_file_location("bp", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

def mathcss(bk):
    """A book with no equations ships no KaTeX, so it must not ask for it."""
    return ('<link rel="stylesheet" href="assets/katex.min.css">'
            if bk.has("math") else "")


# The book's own colours: library.themecss(), shared with make.py so the
# Dropbox build carries the same palette as docs/. Imported under this name
# because helpers outside tools/ call webbuild.themecss(bk).
themecss = library.themecss


# The top bar is emitted by tools/nav.py over the finished tree, for the same
# reason the app layer is: it belongs on every page of the site, and most of
# those pages are not rendered here. The landing pages are copied through
# verbatim, the atlas and the timeline are whole documents of their own, and a
# bar this function stamped into SHELL would reach none of them. It used to
# reach only what SHELL wrote, which is how four books came to have five
# different bars between them.


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} — {book}</title>
<meta name="description" content="{desc}">
{mathcss}
<link rel="stylesheet" href="assets/book.css">
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
<script src="assets/book.js"></script>
{extra}
</body>
</html>
"""


def runtime_js():
    """book.js as docs/ ships it: the equations are numbered and the maths typeset
    at build time, so the runtime must do neither again.

    THE BOOT-SHAPE CONTRACT (DESIGN.md section 8, "book.js boot shape"). This
    function makes two text substitutions in shared/assets/book.js, and each must
    happen exactly once:
      1. the literal `numberEquations();` becomes a comment. It is the first
         statement of the DOMContentLoaded boot handler. If it is missing, every
         page numbers its equations a second time over the numbers already baked
         in at build time; if it appears twice, some other call is being disabled.
      2. everything from `if (window.katex) { typeset(); }` up to the handler's
         closing `\\n  });` is deleted. The katex if/else block must therefore be
         the LAST thing in the handler: a boot call placed after it is silently
         removed from docs/ and from the Dropbox build while still working on
         the staged page.
    New boot calls go after `numberEquations();` and before `if (window.katex)`.
    Anything that needs rendered KaTeX or layout registers its own load, resize
    or scroll listener outside the handler. make.py's runtime_js() is a copy of
    this function; change the two together. The contract comment above the
    handler in book.js is dropped here too, so docs/ stays byte-identical."""
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


# A book's landing page names its parts in longer, reader-facing copy than the
# curriculum's subtitles. That copy is the book's, not the builder's, so it lives
# in book.json under "arc" as [kicker, title, blurb] triples.
def arc(bk):
    return [tuple(row) for row in (bk.cfg.get("arc") or [])]


WORDCOUNT_JS = """() => {
                const d = document.querySelector('.main .col').cloneNode(true);
                d.querySelectorAll('.katex, script, style').forEach(e => e.remove());
                return (d.textContent.match(/[A-Za-z0-9\u2019'-]+/g) || []).length; }"""


# The sidebar's section list as the page left it, minus the spy's state: the
# active entry depends on where the build's browser happened to be scrolled,
# and no state class may be saved into a file (DESIGN.md section 8).
TOC_JS = """() => {
                const t = document.getElementById('sb-toc').cloneNode(true);
                t.querySelectorAll('.active, [aria-current]').forEach(a => {
                  a.classList.remove('active'); a.removeAttribute('aria-current');
                  if (!a.className) a.removeAttribute('class'); });
                return t.innerHTML; }"""


def start_stats(bk):
    """Where the book starts, for a front door's primary (DESIGN.md section 6,
    Front matter): {{START_HREF}}, {{START_NUM}} and {{START_TITLE}}, from the
    first written chapter. Facts are built, not typed: the label moves by itself
    the day an earlier chapter is written. A book with nothing written starts
    at its front door."""
    w = bk.written()
    if not w:
        return {"START_HREF": "index.html", "START_NUM": "", "START_TITLE": ""}
    num, slug, title = w[0][0], w[0][1], w[0][2]
    return {"START_HREF": slug + ".html", "START_NUM": html.escape(str(num)),
            "START_TITLE": html.escape(title)}


def extra_pages(bk, stats):
    """Standalone pages a book declares for itself, beyond the built-in ones.

    webbuild has always known exactly two extra pages, the Math Ledger and the
    Through-Line, because for a long time there was one book and it wanted both.
    A book that needs a third -- the clinical book's trial appendix -- had
    nowhere to put it. So a book names its own in book.json:

        "pages": [{"src": "_trials.html", "out": "trials.html"}]

    The file is copied through with the same stat substitution the landing page
    gets, so a page can show live counts without the builder knowing what it is.
    """
    for spec in bk.cfg.get("pages") or []:
        src = os.path.join(bk.src, spec["src"])
        if not os.path.exists(src):
            raise SystemExit("%s: book.json declares pages[%s] which does not exist"
                             % (bk.slug, spec["src"]))
        tpl = library.read(src)
        for key, val in stats.items():
            tpl = tpl.replace("{{%s}}" % key, val)
        library.write(os.path.join(bk.out, spec["out"]), tpl)
    return len(bk.cfg.get("pages") or [])


def landing_page(bk, stats):
    """docs/<slug>/index.html — the book's own front door, generated so its
    counts can never go stale. A book supplies src/_landing.html; without one
    it gets a plain cover built from book.json."""
    tplf = os.path.join(bk.src, "_landing.html")
    if not os.path.exists(tplf):
        library.write(os.path.join(bk.out, "index.html"),
            SHELL.format(mathcss=mathcss(bk), title="Contents", desc=html.escape(bk.tagline),
                         side=bp.sidebar_head("contents"), toc="", wide=" wide", extra="",
                         book=html.escape(bk.title),
                         body=f'<p class="eyebrow">{html.escape(bk.eyebrow)}</p>'
                              f'<h1>{html.escape(bk.title)}</h1>'
                              f'<p class="subtitle">{html.escape(bk.tagline)}</p>'
                              f'<p>{bk.cfg.get("blurb", "")}</p>'
                              f'<p><a href="contents.html">Contents &rarr;</a></p>'))
        return 0

    tpl = library.read(tplf)

    # A book may ship datasets beside its landing page rather than inside it.
    # The philosophy book's studies and formalised arguments are a megabyte
    # between them and are needed only when a reader opens one, so they are
    # fetched at runtime instead of parsed on every visit. Copied verbatim:
    # they are already minified ASCII JSON and the build has no opinion on
    # their contents.
    # A dataset may also be something a reader takes away rather than something
    # the page fetches. The trial workbook is a binary, so it is copied as bytes
    # rather than through library.write, which normalises line endings.
    datadir = os.path.join(bk.src, "data")
    if os.path.isdir(datadir):
        for f in sorted(os.listdir(datadir)):
            if f.endswith(".json"):
                library.write(os.path.join(bk.out, "data", f),
                              library.read(os.path.join(datadir, f)))
            elif f.endswith((".xlsx", ".csv", ".zip")):
                dst = os.path.join(bk.out, "data", f)
                d = os.path.dirname(dst)
                if not os.path.isdir(d):
                    os.makedirs(d)
                shutil.copyfile(os.path.join(datadir, f), dst)

    built = {}          # part index -> (chapters written, chapters planned)
    for i, (_pt, _blurb, chs) in enumerate(bp.PARTS):
        done = sum(1 for c in chs if os.path.exists(bk.chapter_path(c[1])))
        built[i] = (done, len(chs))

    rows = []
    for i, (k, title, blurb) in enumerate(arc(bk)):
        done, total = built.get(i, (0, 0))
        live = done > 0
        tag = "a" if live else "div"
        href = ' href="contents.html#sec-%d"' % i if live else ""
        cls = "arc-row" if live else "arc-row pending"
        count = ("%d of %d chapters" % (done, total)) if live else ("%d chapters" % total)
        rows.append(
            '<{t} class="{c}"{h}><div class="arc-k">{k}</div>'
            '<div class="arc-b"><div class="arc-t">{ti}</div><p>{b}</p></div>'
            '<div class="arc-n">{n}</div></{t}>'.format(
                t=tag, c=cls, h=href, k=k, ti=title, b=blurb, n=count))

    for key, val in stats.items():
        tpl = tpl.replace("{{%s}}" % key, val)
    tpl = tpl.replace("{{ARC}}", "\n".join(rows))
    library.write(os.path.join(bk.out, "index.html"), tpl)
    return len(rows)


HUB_CSS = """
*{box-sizing:border-box}
/* The same role names every book page uses (DESIGN.md section 3), in both
   themes, so the library bar, the offline shelf in pwa.css and anything else
   that reads --bg, --paper or --ink finds the hub's own colours rather than a
   literal fallback. --ink-faint is the palest ink a word may use: 4.96:1 on
   the ground and 5.36:1 on a tile in light, 5.78:1 and 5.48:1 in dark. */
:root{
  --serif:var(--lib-serif,"Iowan Old Style",Charter,"Bitstream Charter","Palatino Linotype",
    "Sitka Text",Palatino,"Source Serif 4","Noto Serif",Georgia,Cambria,serif);
  --sans:var(--lib-sans,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,
    "Helvetica Neue",Arial,sans-serif);
  --bg:#f4f3f0; --paper:#ffffff;
  --ink:#16181d; --ink-soft:#565b66; --ink-faint:#646975; --rule:#dcdfe5;
  --accent-ink:var(--ink);
  color-scheme:light;
}
html,body{margin:0;height:100%}
body{
  font-family:var(--serif); color:var(--ink); background:var(--bg);
  -webkit-font-smoothing:antialiased; position:relative; overflow-x:hidden;
  -webkit-text-size-adjust:100%; text-size-adjust:100%;
}

/* ---------- the field ----------
   One layer per book, all stacked, all transparent until that book is asked
   for. Hovering a tile does not swap an image; it fades one layer up and the
   others down, so the whole page takes on the book's weather.

   Every layer is translucent and mixed from the book's own accent, so the
   wash tints whatever the page is already standing on. That is what makes it
   survive dark mode: an opaque near-white gradient here would flash the whole
   page white the moment a pointer crossed a tile. Nothing is opaque, so
   nothing can. --w1..--wg are the alphas, lifted in dark mode because a tint
   has to work harder against a dark ground to be seen at all. */
:root{--w1:.30;--w2:.20;--w3:.075;--wg:.07;--wt:.11}
.field{position:fixed;inset:0;z-index:0;opacity:0;transition:opacity .55s ease;pointer-events:none;
  --fg:var(--a-rgb); --fg2:var(--a2-rgb)}
.field.base{opacity:1;background-image:radial-gradient(120% 80% at 50% -10%,rgba(90,96,110,.05) 0%,transparent 60%)}
body[data-focus] .field.base{opacity:0}

/* the three weathers a book can ask for, drawn from its own accent */
.field[data-style="lightcone"]{
  background-image:
    radial-gradient(125% 95% at 50% 108%, rgba(var(--fg),var(--w1)) 0%, rgba(var(--fg),calc(var(--w1)*.28)) 40%, transparent 68%),
    radial-gradient(120% 90% at 50% -8%, rgba(var(--fg2),var(--w2)) 0%, transparent 62%),
    linear-gradient(90deg, rgba(var(--fg),var(--w3)) 1px, transparent 1px),
    linear-gradient(rgba(var(--fg),var(--w3)) 1px, transparent 1px),
    linear-gradient(180deg, rgba(var(--fg),var(--wg)), rgba(var(--fg2),calc(var(--wg)*1.6)));
  background-size:auto,auto,46px 46px,46px 46px,auto}
.field[data-style="marginalia"]{
  background-image:
    linear-gradient(90deg,transparent 0 7.3%,rgba(var(--fg),var(--wt)) 7.3% 7.75%,transparent 7.75%),
    repeating-linear-gradient(180deg,transparent 0 33px,rgba(var(--fg2),var(--w3)) 33px 34px),
    radial-gradient(95% 75% at 82% -4%, rgba(var(--fg),var(--w1)) 0%, transparent 62%),
    radial-gradient(85% 65% at 8% 104%, rgba(var(--fg2),var(--w2)) 0%, transparent 60%),
    linear-gradient(180deg, rgba(var(--fg),var(--wg)), rgba(var(--fg2),calc(var(--wg)*1.6)))}
.field[data-style="plain"]{
  background-image:
    radial-gradient(95% 75% at 70% -4%, rgba(var(--fg),var(--w1)) 0%, transparent 62%),
    linear-gradient(180deg, rgba(var(--fg),var(--wg)), rgba(var(--fg2),calc(var(--wg)*1.6)))}
BOOKFIELDS

.wrap{position:relative;z-index:1;max-width:64rem;margin:0 auto;padding:clamp(2.5rem,7vh,5rem) 1.4rem 4rem}

header.lede{max-width:38rem;margin:0 0 clamp(2rem,5vh,3.4rem)}
.eyebrow{font-family:var(--sans);font-size:.7rem;font-weight:700;letter-spacing:.22em;
  text-transform:uppercase;color:var(--ink-faint);margin:0 0 .9rem}
h1{font-size:clamp(2.1rem,5.2vw,3.3rem);line-height:1.04;letter-spacing:-.025em;
  font-weight:600;margin:0 0 1rem}
/* not the eyebrow, which is also a <p> in the lede and lost to this rule: it
   rendered at 18px bold with 4px tracking, louder than anything but the h1
   (FD-05) */
.lede > p:not(.eyebrow){font-size:clamp(1rem,2vw,1.14rem);line-height:1.6;color:var(--ink-soft);margin:0;max-width:34rem}

/* ---------- the shelf ---------- */
.shelf{display:grid;grid-template-columns:repeat(2,1fr);gap:1.15rem}
@media (max-width:760px){.shelf{grid-template-columns:1fr}}

.book{
  position:relative;display:flex;flex-direction:column;justify-content:space-between;
  min-height:19rem;padding:1.6rem 1.5rem 1.35rem;
  text-decoration:none;color:inherit;
  background:rgba(255,255,255,.72);
  border:1px solid var(--rule);border-radius:10px;
  -webkit-backdrop-filter:saturate(140%) blur(6px);
  backdrop-filter:saturate(140%) blur(6px);
  transition:transform .3s ease,box-shadow .3s ease,opacity .4s ease,
             border-color .3s ease,background .4s ease;
}
/* --bk-hue is the tile's accent in the active theme: --bk-accent on paper,
   --bk-accent-2 (the book's accent_dark) on the dark ground, where the light
   accents measured 2.0 to 3.4:1 (FD-03, NAV-12, PDA-04). Both are stamped on
   the tile by hub(); the swap is below, keyed on data-theme. */
.book{--bk-hue:var(--bk-accent)}
.book:hover,.book:focus-visible{
  transform:translateY(-3px);
  border-color:var(--bk-hue);
  box-shadow:0 14px 40px rgba(20,22,28,.14);
}
.book:hover{outline:none}
/* a real ring in the tile's own colour: the focused tile used to differ from
   its neighbours only by a 1px border at 2:1 (PDA-04) */
.book:focus-visible{outline:2px solid var(--bk-hue);outline-offset:3px}
/* the other books recede rather than disappear — still readable, plainly not the subject */
body[data-focus] .book{opacity:.34;filter:saturate(.5)}
body[data-focus] .book[data-live="1"]:hover,
body[data-focus] .book[data-live="1"]:focus-visible{opacity:1;filter:none}

.book .rule{width:2.4rem;height:3px;border-radius:2px;background:var(--bk-hue);margin:0 0 1.1rem}
.book .kicker{font-family:var(--sans);font-size:.66rem;font-weight:700;letter-spacing:.18em;
  text-transform:uppercase;color:var(--bk-hue);margin:0 0 .6rem}
.book h2{font-size:clamp(1.5rem,3.1vw,2rem);line-height:1.08;letter-spacing:-.02em;
  font-weight:600;margin:0 0 .7rem}
.book p{font-size:.95rem;line-height:1.55;color:var(--ink-soft);margin:0}
.book .foot{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;
  margin-top:1.5rem;font-family:var(--sans);font-size:.78rem;color:var(--ink-faint)}
.book .count{font-weight:650;color:var(--ink-soft)}
.book .go{color:var(--bk-hue);font-weight:650}
.book[data-live="0"]{cursor:default}
.book[data-live="0"] .go{color:var(--ink-faint)}

footer{margin-top:3rem;font-family:var(--sans);font-size:.76rem;color:var(--ink-faint)}
footer a{color:inherit}

@media (prefers-reduced-motion:reduce){
  .field,.book{transition:none}
  .book:hover,.book:focus-visible{transform:none}
}
/* A phone cannot hover, so the wash never fires there and the tiles have to
   carry their own colour. Apple's 44pt minimum and the home indicator are the
   other two things a desktop layout forgets. */
@media (pointer:coarse){
  .book{min-height:16rem}
  .book:active{transform:scale(.995)}
  footer a{display:inline-flex;align-items:center;min-height:44px}
  .wrap{padding-left:max(1.4rem,env(safe-area-inset-left));
        padding-right:max(1.4rem,env(safe-area-inset-right));
        padding-bottom:calc(4rem + env(safe-area-inset-bottom))}
}
@media (max-width:520px){
  .shelf{gap:.9rem}
  .book{min-height:14rem;padding:1.3rem 1.2rem 1.15rem}
}
/* ---------- dark ----------
   Keyed on data-theme, which the boot script in <head> stamps before first
   paint from the reader's choice or, failing one, from the OS. The hub used
   to read only the media query, so it ignored the theme a reader had chosen
   and sat dark under html[data-theme=light] (NAV-02, FD-02). The media query
   is kept only as the fallback for a page no script has stamped. HUBDARK is
   filled in by hub() from HUB_DARK, once for each of the two selectors. */
HUBDARK
"""

# The dark theme, as (selector suffix, declarations). hub() writes it twice:
# under :root[data-theme="dark"], and under :root:not([data-theme]) inside the
# prefers-color-scheme media query, so the two can never drift apart.
HUB_DARK = (
    ("", "--bg:#101216;--paper:#181b20;--ink:#e6e6e2;--ink-soft:#a9adb6;"
         "--ink-faint:#8a8f99;--rule:#31353d;color-scheme:dark;"
         "--w1:.40;--w2:.30;--w3:.11;--wg:.13;--wt:.17"),
    # the accents were chosen against paper; on a dark ground the book's
    # lighter variant is the one that reads, so the two swap roles, in the
    # weather and on the tile alike
    (" .book", "background:rgba(24,27,32,.66);--bk-hue:var(--bk-accent-2)"),
    (" .field", "--fg:var(--a2-rgb);--fg2:var(--a-rgb)"),
    (" .field.base", "background-image:radial-gradient(120% 80% at 50% -10%,"
                     "rgba(150,160,180,.06) 0%,transparent 60%)"),
)


def hub_dark():
    def block(scope):
        return "\n".join("%s%s{%s}" % (scope, sel, decl) for sel, decl in HUB_DARK)
    return (block(':root[data-theme="dark"]')
            + "\n@media (prefers-color-scheme:dark){\n"
            + block(":root:not([data-theme])") + "\n}")

HUB_JS = """
(function () {
  var body = document.body;
  function focusBook(slug) {
    if (slug) body.setAttribute('data-focus', slug);
    else body.removeAttribute('data-focus');
  }
  document.querySelectorAll('.book').forEach(function (el) {
    var slug = el.getAttribute('data-slug');
    el.addEventListener('mouseenter', function () { focusBook(slug); });
    el.addEventListener('focus', function () { focusBook(slug); });
    el.addEventListener('mouseleave', function () { focusBook(null); });
    el.addEventListener('blur', function () { focusBook(null); });
  });
  document.querySelector('.shelf').addEventListener('mouseleave', function () { focusBook(null); });
})();
"""


def _rgb(hexcolour):
    """"#a3232b" -> "163,35,43", so a stylesheet can vary the alpha on it."""
    h = hexcolour.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "%d,%d,%d" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _luminance(hexcolour):
    def lin(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(x) for x in _rgb(hexcolour).split(","))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def _contrast(a, b):
    x, y = _luminance(a), _luminance(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


# The tile grounds the kicker and "Read" sit on: rgba(255,255,255,.72) over the
# light hub, rgba(24,27,32,.66) over the dark one (HUB_CSS, HUB_DARK).
TILE_LIGHT, TILE_DARK = "#fcfcfb", "#15181d"


def _legible(accent, ground, floor=4.5):
    """The book's accent, or the nearest mix of it toward white (on a dark
    ground) or black (on a light one) that reads at `floor` on `ground`.

    A book chooses its accents against its own paper. On the hub they are also
    text -- the tile's kicker and "Read" -- on a ground the book never saw, and
    an accent_dark that is fine as a rule can be 3.8:1 as a word. Derived here
    rather than typed into book.json, so a book whose colours already pass is
    emitted unchanged."""
    if _contrast(accent, ground) >= floor:
        return accent
    to = "#ffffff" if _luminance(ground) < 0.2 else "#000000"
    a = [int(x) for x in _rgb(accent).split(",")]
    b = [int(x) for x in _rgb(to).split(",")]
    for step in range(1, 21):
        t = step / 20.0
        c = "#" + "".join("%02x" % round(p + (q - p) * t) for p, q in zip(a, b))
        if _contrast(c, ground) >= floor:
            return c
    return to


def _field_css(bk):
    """A background for one book, mixed from its own accent.

    Only the two colours are emitted here; the gradients themselves live in
    HUB_CSS, keyed off data-style. That split is what lets the dark-mode block
    restyle every book's weather at once instead of once per book, and it is
    why the wash is a tint of the page rather than a sheet laid over it."""
    t = bk.theme
    a = t.get("accent", "#333333")
    a2 = t.get("accent_dark", a)
    return (f'.field[data-book="{bk.slug}"]{{--a-rgb:{_rgb(a)};--a2-rgb:{_rgb(a2)}}}\n'
            f'body[data-focus="{bk.slug}"] .field[data-book="{bk.slug}"]{{opacity:1}}\n'
            f'body[data-focus="{bk.slug}"] .book[data-slug="{bk.slug}"]'
            f'{{opacity:1;filter:none;border-color:var(--bk-hue);'
            f'box-shadow:0 14px 44px -14px rgba(var(--a-rgb),.55)}}\n')


def hub(results):
    """docs/index.html — the library's front door.

    Two tiles per row, each carrying its own colour. Hovering or tabbing to one
    changes the whole page's background to that book's and lets the others
    recede, so the shelf answers "what kind of book is this" before you click.
    """
    fields, tiles = [], []
    for bk, n, stats in results:
        fields.append(_field_css(bk))
        total = len(bk.flat)
        # A book is readable when it has a front door, not when it has chapters:
        # The Long Argument is an interactive index and would otherwise be
        # unclickable on the shelf that exists to open it.
        live = os.path.exists(os.path.join(bk.out, "index.html"))
        href = f"{bk.slug}/index.html" if live else None
        count = (f"{n} of {total} chapters" if n else f"{total} chapters planned")
        go = "Read &rarr;" if live else "Not yet written"
        tag = "a" if live else "div"
        attrs = f' href="{href}"' if live else ""
        tiles.append(
            f'<{tag} class="book" data-slug="{bk.slug}" data-live="{1 if live else 0}"{attrs}'
            f' style="--bk-accent:{_legible(bk.theme.get("accent", "#333333"), TILE_LIGHT)};'
            f'--bk-accent-2:{_legible(bk.theme.get("accent_dark") or bk.theme.get("accent", "#999999"), TILE_DARK)}">'
            f'<div><div class="rule"></div>'
            f'<p class="kicker">{html.escape(bk.eyebrow)}</p>'
            f'<h2>{html.escape(bk.title)}</h2>'
            f'<p>{html.escape(bk.tagline)}</p></div>'
            f'<div class="foot"><span class="count">{count}</span>'
            f'<span class="go">{go}</span></div>'
            f'</{tag}>')

    field_divs = "".join(
        f'<div class="field" data-book="{bk.slug}" '
        f'data-style="{bk.theme.get("field", "plain")}"></div>' for bk, _n, _s in results)
    css = HUB_CSS.replace("BOOKFIELDS", "".join(fields)).replace("HUBDARK", hub_dark())

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>A Library</title>
<meta name="description" content="Books built from first principles: {', '.join(html.escape(b.title) for b, _n, _s in results)}.">
<style>{css}</style>
</head>
<body>
<div class="field base"></div>
{field_divs}
<div class="wrap">
<header class="lede">
  <p class="eyebrow">Built from first principles</p>
  <h1>A library of books that show their working.</h1>
  <p>Each one begins at the beginning and derives what it uses. Where something is taken on
  trust it is marked as such, so you always know what you are standing on.</p>
</header>
<main class="shelf">
{"".join(tiles)}
</main>
<footer>Every page works with the network switched off. <a href="https://github.com/Elkhanany">Source</a>.</footer>
</div>
<script>{HUB_JS}</script>
</body>
</html>
"""
    library.write(os.path.join(DOCS, "index.html"), page)
    return len(tiles)


async def build_book(bk, browser):
    """Render one book into docs/<slug>/."""
    global BOOK
    BOOK = bk
    bp.use(bk)

    shutil.rmtree(STAGE, ignore_errors=True)
    bp.OUT = STAGE
    bp.build()

    out = bk.out
    # Only this book's output is cleared. Wiping all of docs/ would delete the
    # other books, which is exactly the kind of thing a library must not do.
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)

    if bk.has("math"):
        library.write(os.path.join(out, "assets", "katex.min.css"),
                      library.read(os.path.join(VEND, "katex.min.css")))
        shutil.copytree(os.path.join(VEND, "fonts"), os.path.join(out, "assets", "fonts"))
    library.write(os.path.join(out, "assets", "book.css"),
                  library.read(os.path.join(library.ASSETS, "book.css")) + themecss(bk))
    library.write(os.path.join(out, "assets", "book.js"), runtime_js())
    # The front door's stylesheet, for the books that have a hand-written one.
    # Copied per book exactly as book.css is, rather than shared at the library
    # level, so a book's offline download carries everything that book's pages
    # ask for and no book pays for a stylesheet it never loads.
    # Asked for, not merely possible: the atlas and the timeline have landing
    # pages too and are whole self-contained documents that load neither this
    # stylesheet nor book.css. Keying off the file's own <link> means a book
    # gets the stylesheet exactly when it uses it, and stops carrying it the
    # day it stops.
    lp = os.path.join(bk.src, "_landing.html")
    if os.path.exists(lp) and "assets/landing.css" in library.read(lp):
        library.write(os.path.join(out, "assets", "landing.css"),
                      library.read(os.path.join(library.ASSETS, "landing.css")))

    n = 0
    stats = {"words": 0, "eq": 0, "boxes": 0, "planned": len(bp.FLAT)}

    async def render(src, title, desc, side, wide, extra, dest,
                     count_into_stats=False):
        pg = await browser.new_page(viewport={"width": 1280, "height": 1000})
        await pg.goto("file://" + src)
        await pg.wait_for_timeout(2400)
        # Rewind any animated figure before the DOM is saved, so two builds of
        # identical source produce identical files.
        await pg.evaluate("() => { if (window.NMT && NMT.resetForSnapshot) NMT.resetForSnapshot(); }")
        await pg.wait_for_timeout(60)
        body = await pg.evaluate("document.querySelector('.main .col').innerHTML")
        words = await pg.evaluate(WORDCOUNT_JS)
        toc = await pg.evaluate(TOC_JS)
        await pg.close()
        body = body.replace('href="chapters/', 'href="')
        if count_into_stats:
            stats["words"] += words
            stats["eq"] += len(re.findall(r'class="katex"', body))
            stats["boxes"] += len(re.findall(r'class="callout plain"', body))
        library.write(dest, SHELL.format(mathcss=mathcss(bk), title=title, desc=html.escape(desc),
                                         side=side, toc=toc, body=body,
                                         wide=wide, extra=extra,
                                         book=html.escape(bk.title)))

    for num, slug, title, part, _m in bp.FLAT:
        src = os.path.join(STAGE, "chapters", slug + ".html")
        if not os.path.exists(src):
            continue
        raw = library.read(bk.chapter_path(slug))
        m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
        extra = "<script>\n" + m.group(1) + "\n</script>" if m else ""
        await render(src, f"{num} {title}",
                     f"Chapter {num} of {bk.title}: {title}.",
                     bp.sidebar_head("chapter", slug), "", extra,
                     os.path.join(out, slug + ".html"), count_into_stats=True)
        n += 1

    # No contents page for a book with nothing written (NAV-04, FD-15): it was
    # a heading over planned titles, or over nothing at all, and nav_items()
    # no longer offers it. One name per destination (NAV-09): the <title> and
    # the sidebar say what the bar says. Only the contents page and the ledger,
    # whose lines are short rows and tables, take the wide column; the
    # Through-Line is continuous prose and keeps the reading measure.
    pages = ([("index", "contents", "contents", " wide", f"Every chapter of {bk.title}.")]
             if bk.written() else [])
    if bk.has("ledger"):
        pages.append(("ledger", "ledger", "ledger", " wide",
                      "Every mathematical object in the book: where it was defined, "
                      "what for, and where it is spent."))
    if bk.has("throughline"):
        pages.append(("throughline", "throughline", "throughline", "",
                      "The whole book in plain language, with no mathematics."))
    for name, outname, page, wide, desc in pages:
        src = os.path.join(STAGE, name + ".html")
        if os.path.exists(src):
            t = {"contents": "Contents", "ledger": "Math Ledger",
                 "throughline": "In Plain Terms"}[page]
            await render(src, t, desc, bp.sidebar_head(page), wide, "",
                         os.path.join(out, outname + ".html"))

    def human(x):
        return f"{x/1000:.0f}k" if x >= 10000 else f"{x:,}"
    # One dict, passed to both. It was written out twice, identically, and a
    # stat added to one copy would have appeared on the appendices and not on
    # the front door. PARTS is here because a landing page that names a number
    # of parts in its prose goes stale the first time a part is added: the
    # clinical book's said sixteen while the curriculum held seventeen.
    page_stats = {"CH": f"{n} / {stats['planned']}", "WORDS": human(stats["words"]),
                  "EQ": human(stats["eq"]), "BOXES": str(stats["boxes"]),
                  "PARTS": str(len(bp.PARTS))}
    page_stats.update(start_stats(bk))
    extra_pages(bk, page_stats)
    landing_page(bk, page_stats)
    return n, stats


async def main():
    os.makedirs(DOCS, exist_ok=True)
    library.write(os.path.join(DOCS, ".nojekyll"), "")

    results = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        for bk in library.books():
            n, stats = await build_book(bk, browser)
            results.append((bk, n, stats))
            print(f"  {bk.slug}: {n}/{stats['planned']} chapters, "
                  f"{stats['words']:,} words, {stats['eq']:,} expressions")
        await browser.close()
    shutil.rmtree(STAGE, ignore_errors=True)

    hub(results)

    # The app layer goes on last, over the finished tree. It is a text pass and
    # costs about five seconds on a build that takes a quarter of an hour.
    #
    # Emitting it here rather than interpolating the head into SHELL is
    # deliberate: pwa.py is then the single producer of that block, and the
    # full-build path and the standalone `python3 tools/pwa.py` path cannot
    # drift apart because they are the same code. The injector is idempotent
    # and anchored on the viewport meta, and raises rather than silently
    # patching nothing if that anchor ever moves.
    # The bar, then the app layer, both over the finished tree and both pure
    # text. They anchor on different strings -- the bar on <body>, the app layer
    # on the viewport meta -- so neither disturbs the other and the order here
    # is only the order they read best in.
    barred = nav.emit_all([bk for bk, _n, _s in results])
    pages = pwa.emit_all([bk for bk, _n, _s in results])
    print(f"  navigation: {barred} pages carry the library bar")
    print(f"  app layer: {pages} pages, {len(results)} manifests")

    tot = sum(os.path.getsize(os.path.join(dp, f))
              for dp, _, fs in os.walk(DOCS) for f in fs)
    built = sum(n for _b, n, _s in results)
    print(f"docs/: library hub + {len(results)} books, {built} chapters ({tot/1e6:.1f} MB)")


if __name__ == "__main__":
    asyncio.run(main())
