#!/usr/bin/env python3
"""
Emit docs/ — the published site, which Cloudflare Pages serves at the root of its domain.

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
   themes, so the library bar and anything else that reads --bg, --paper or
   --ink finds the hub's own colours rather than a literal fallback.
   --ink-faint is the palest ink a word may use: 4.96:1 on the ground and
   5.36:1 on a tile in light, 5.78:1 and 5.48:1 in dark. */
:root{
  --serif:var(--lib-serif,"Iowan Old Style",Charter,"Bitstream Charter","Palatino Linotype",
    "Sitka Text",Palatino,"Source Serif 4","Noto Serif",Georgia,Cambria,serif);
  --sans:var(--lib-sans,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,
    "Helvetica Neue",Arial,sans-serif);
  --bg:#f4f3f0; --paper:#ffffff;
  --ink:#16181d; --ink-soft:#565b66; --ink-faint:#646975; --rule:#dcdfe5;
  --accent-ink:var(--ink);
  --tile:rgba(255,255,255,.72);
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

/* The frame's inner gutter is the bar's inset (DESIGN.md section 5), so the
   lede starts under the brand's letters on a phone. */
.wrap{position:relative;z-index:1;max-width:64rem;margin:0 auto;
  padding:clamp(2.5rem,7vh,5rem) var(--lib-inset,1.25rem) 4rem}
main{display:block}

/* ---------- the lede: a label, the serif title, the lede ---------- */
header.lede{max-width:38rem;margin:0 0 clamp(2rem,5vh,3.4rem)}
.eyebrow,.continue h2{font:700 .7rem/1.3 var(--sans);letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-faint);margin:0 0 .9rem}
h1{font-size:clamp(2.1rem,5.2vw,3.3rem);line-height:1.06;letter-spacing:-.02em;
  font-weight:400;margin:0 0 1rem;text-wrap:balance}
/* not the eyebrow, which is also a <p> in the lede and lost to this rule: it
   rendered at 18px bold with 4px tracking, louder than anything but the h1
   (FD-05) */
.lede > p:not(.eyebrow){font-size:clamp(1rem,2vw,1.14rem);line-height:1.6;color:var(--ink-soft);margin:0;max-width:34rem}

/* ---------- continue reading ----------
   Filled by pwa.js from library:v1.lastBy, one row per book the reader has
   opened a chapter of, most recent first (DESIGN.md section 6, Hub). Hidden
   until there is something in it, so a first visit shows nothing here. The
   book's name is in its own accent, the dark-safe one in the dark theme,
   which is the same swap the tiles make. */
.continue{margin:0 0 clamp(2rem,5vh,2.8rem);max-width:44rem}
.continue[hidden]{display:none}
.continue ol{list-style:none;margin:0;padding:0}
.continue li{margin:0}
/* Each row stands on its own progress rule: the hairline is the track, the
   book's accent the part read, so the rows need no other divider. */
.continue a{--bk-hue:var(--bk-accent);display:grid;grid-template-columns:minmax(0,13rem) minmax(0,1fr);
  align-items:baseline;gap:.15rem 1.2rem;padding:.65rem 0 0;min-height:44px;
  text-decoration:none;color:var(--ink)}
.continue .c-book{font:600 .8125rem/1.3 var(--sans);color:var(--bk-hue);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.continue .c-ch{font-size:1.02rem;line-height:1.35;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.continue .c-rule{grid-column:1/-1;height:2px;margin-top:.55rem;background:var(--rule);position:relative}
.continue .c-rule i{position:absolute;left:0;top:0;bottom:0;background:var(--bk-hue)}
.continue a:hover .c-ch,.continue a:focus-visible .c-ch{color:var(--bk-hue)}
.continue a:focus-visible{outline:2px solid var(--bk-hue);outline-offset:2px}
@media (max-width:639.98px){
  .continue a{grid-template-columns:minmax(0,1fr)}
}

/* ---------- the shelf ----------
   Tiles in the house register (FD-11): a hairline, radius 6px, the page's
   raised surface let through a little, and nothing that lifts, shadows,
   blurs or holds a tile open to a fixed height. The title's link is
   stretched over the whole tile, so the tile is one target; only the offline
   chip sits above it. */
.shelf{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.15rem}
@media (max-width:639.98px){.shelf{grid-template-columns:minmax(0,1fr);gap:.9rem}}

.book{
  position:relative;display:flex;flex-direction:column;
  padding:1.5rem 1.5rem 1.2rem;
  color:inherit;background:var(--tile);
  border:1px solid var(--rule);border-radius:6px;
  transition:opacity .4s ease,border-color .3s ease,background .4s ease;
}
/* --bk-hue is the tile's accent in the active theme: --bk-accent on paper,
   --bk-accent-2 (the book's accent_dark) on the dark ground, where the light
   accents measured 2.0 to 3.4:1 (FD-03, NAV-12, PDA-04). Both are stamped on
   the tile by hub(); the swap is below, keyed on data-theme. */
.book{--bk-hue:var(--bk-accent)}
.book:hover{border-color:var(--bk-hue)}
/* Keyboard focus lands on the title's link, which is stretched over the tile,
   so the ring goes round the tile in the book's own colour (C2-tile-focus),
   not round the title's words. */
.book h2 a:focus-visible{outline:none}
.book:has(h2 a:focus-visible){outline:2px solid var(--bk-hue);outline-offset:2px;border-color:var(--bk-hue)}
@supports not selector(:has(a)){
  .book:focus-within{outline:2px solid var(--bk-hue);outline-offset:2px}
}
/* the other books recede rather than disappear: still readable, plainly not the subject */
body[data-focus] .book{opacity:.34;filter:saturate(.5)}

.book .rule{width:2.4rem;height:3px;border-radius:2px;background:var(--bk-hue);margin:0 0 1.1rem}
.book .kicker{font:700 .7rem/1.3 var(--sans);letter-spacing:.12em;
  text-transform:uppercase;color:var(--bk-hue);margin:0 0 .6rem}
.book h2{font-size:clamp(1.5rem,3.1vw,2rem);line-height:1.1;letter-spacing:-.015em;
  font-weight:400;margin:0 0 .6rem}
.book h2 a{color:inherit;text-decoration:none}
.book h2 a::after{content:"";position:absolute;inset:0;z-index:1;border-radius:inherit}
.book .tagline{font-size:.98rem;line-height:1.55;color:var(--ink-soft);margin:0}
.book .foot{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;
  gap:.6rem 1rem;margin-top:auto;padding-top:1.3rem;font:.8125rem/1.35 var(--sans)}
.book .count{font-weight:600;color:var(--ink-soft)}
.book .go{color:var(--bk-hue);font-weight:600;white-space:nowrap}
.book .off{grid-column:1/-1;justify-self:start}
.book[data-live="0"] .go{color:var(--ink-faint)}

/* The offline chip: a button, above the stretched link, in the page's own
   inks. pwa.js un-hides it once it knows what is stored; with no script,
   or no Cache Storage, it never shows. */
.book button.off{position:relative;z-index:2;font:600 .75rem/1.2 var(--sans);
  color:var(--ink-soft);background:var(--tile);border:1px solid var(--rule);
  border-radius:999px;padding:.35rem .8rem;min-height:32px;cursor:pointer}
.book button.off:hover{border-color:currentColor;color:var(--ink)}
.book button.off:focus-visible{outline:2px solid var(--bk-hue);outline-offset:2px}
.book button.off[disabled]{cursor:default}
.book button.off[hidden]{display:none}

/* ---------- below the grid: one quiet line ---------- */
.store{margin:1.6rem 0 0;font:.8125rem/1.5 var(--sans);color:var(--ink-faint)}
.store[hidden]{display:none}
.store button{font:inherit;color:inherit;background:none;border:0;padding:0;margin:0;
  text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.store button:hover{color:var(--ink)}
.store button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}

footer{margin-top:2.4rem;font:.8125rem/1.5 var(--sans);color:var(--ink-faint)}
footer a{color:inherit}

@media (prefers-reduced-motion:reduce){
  .field,.book{transition:none}
}
/* A phone cannot hover, so the wash never fires there and the tiles have to
   carry their own colour. Apple's 44pt minimum and the home indicator are the
   other two things a desktop layout forgets. */
@media (pointer:coarse){
  .book button.off{min-height:44px;padding:.5rem 1rem}
  .store button,footer a{display:inline-flex;align-items:center;min-height:44px}
  .wrap{padding-left:max(var(--lib-inset,1rem),env(safe-area-inset-left));
        padding-right:max(var(--lib-inset,1rem),env(safe-area-inset-right));
        padding-bottom:calc(4rem + env(safe-area-inset-bottom))}
}
@media (max-width:520px){
  .book{padding:1.3rem 1.2rem 1.1rem}
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
         "--tile:rgba(24,27,32,.66);"
         "--w1:.40;--w2:.30;--w3:.11;--wg:.13;--wt:.17"),
    # the accents were chosen against paper; on a dark ground the book's
    # lighter variant is the one that reads, so the two swap roles, in the
    # weather, on the tile and in the Continue strip alike
    (" .book", "--bk-hue:var(--bk-accent-2)"),
    (" .continue a", "--bk-hue:var(--bk-accent-2)"),
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

# The weather follows the reader's attention: a pointer over a tile, or
# keyboard focus anywhere inside one. focus and blur do not bubble, so they
# were bound to a tile that is no longer the thing that takes focus (its
# title's link and its offline chip do); focusin and focusout do, and a move
# between the link and the chip inside one tile keeps that tile's weather.
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
    el.addEventListener('mouseleave', function () {
      if (!el.contains(document.activeElement)) focusBook(null);
    });
    el.addEventListener('focusin', function () { focusBook(slug); });
    el.addEventListener('focusout', function (e) {
      if (!e.relatedTarget || !el.contains(e.relatedTarget)) focusBook(null);
    });
  });
  document.querySelector('.shelf').addEventListener('mouseleave', function () {
    if (!document.activeElement || !document.activeElement.closest ||
        !document.activeElement.closest('.book')) focusBook(null);
  });
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


# The grounds a book's accent is set on as text: the tile's kicker and "Read"
# on rgba(255,255,255,.72) or rgba(24,27,32,.66) over the hub (HUB_CSS,
# HUB_DARK), and the Continue strip's book name on the hub's own ground. Each
# accent has to read on both of its theme's grounds.
TILE_LIGHT, TILE_DARK = "#fcfcfb", "#15181d"
GROUND_LIGHT, GROUND_DARK = "#f4f3f0", "#101216"


def _legible(accent, grounds, floor=4.5):
    """The book's accent, or the nearest mix of it toward white (on a dark
    ground) or black (on a light one) that reads at `floor` on every one of
    `grounds`.

    A book chooses its accents against its own paper. On the hub they are also
    text -- the tile's kicker and "Read", the Continue strip's book name -- on
    grounds the book never saw, and an accent_dark that is fine as a rule can
    be 3.8:1 as a word. Derived here rather than typed into book.json, so a
    book whose colours already pass is emitted unchanged."""
    if isinstance(grounds, str):
        grounds = [grounds]
    if all(_contrast(accent, g) >= floor for g in grounds):
        return accent
    to = "#ffffff" if _luminance(grounds[0]) < 0.2 else "#000000"
    a = [int(x) for x in _rgb(accent).split(",")]
    b = [int(x) for x in _rgb(to).split(",")]
    for step in range(1, 21):
        t = step / 20.0
        c = "#" + "".join("%02x" % round(p + (q - p) * t) for p, q in zip(a, b))
        if all(_contrast(c, g) >= floor for g in grounds):
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
            f'{{opacity:1;filter:none;border-color:var(--bk-hue)}}\n')


_WORDS = ("zero one two three four five six seven eight nine ten eleven twelve").split()


def _data_count(bk, ref):
    """len() of a book's data file, or of one key in it: "atlas.json#people"."""
    name, _, key = ref.partition("#")
    path = os.path.join(bk.src, "data", name)
    if not os.path.exists(path):
        raise SystemExit("%s: book.json shelf counts %s, which is not in src/data/"
                         % (bk.slug, name))
    import json
    obj = json.loads(library.read(path))
    if key:
        if key not in obj:
            raise SystemExit("%s: book.json shelf counts %s, which has no %r"
                             % (bk.slug, name, key))
        obj = obj[key]
    return len(obj)


def shelf_status(bk, written):
    """The tile's status line, in the book's own unit, from book.json "shelf"
    and computed here, never typed (DESIGN.md section 1, principle 9).

      {"unit": "chapters"}                      "98 chapters", or
                                                "37 of 76 chapters written"
      {"count": "studies.json", "unit": ...}    "133 thinkers, each with a study"
      {"count": "atlas.json#people", "unit": "thinkers",
       "across": "atlas.json#epochs", "across_unit": "ages"}
                                                "133 thinkers across ten ages"

    A chaptered book says how much of it is written; "chapters planned" and
    "0 chapters" (NAV-13) cannot be produced. A book with nothing to count gets
    no status line rather than a zero."""
    spec = bk.cfg.get("shelf") or {"unit": "chapters"}
    unit = spec.get("unit", "chapters")
    if "count" not in spec:
        total = len(bk.flat)
        if not written:
            return ""
        return ("%d %s" % (total, unit) if written >= total
                else "%d of %d %s written" % (written, total, unit))
    n = _data_count(bk, spec["count"])
    if not n:
        return ""
    out = "%d %s" % (n, unit)
    if spec.get("across"):
        m = _data_count(bk, spec["across"])
        out += " across %s %s" % (_WORDS[m] if m < len(_WORDS) else m,
                                  spec.get("across_unit", ""))
    return out.strip()


def hub(results):
    """docs/index.html -- the library's front door.

    The bar, the lede, the reader's Continue strip (filled by pwa.js), then
    two tiles per row, each carrying its own colour. Hovering or tabbing to
    one changes the whole page's background to that book's and lets the
    others recede, so the shelf answers "what kind of book is this" before you
    click. Then one quiet line about storage, and the footer.
    """
    fields, tiles = [], []
    for bk, n, stats in results:
        fields.append(_field_css(bk))
        # A book is readable when it has a front door, not when it has chapters:
        # The Long Argument is an interactive index and would otherwise be
        # unclickable on the shelf that exists to open it.
        live = os.path.exists(os.path.join(bk.out, "index.html"))
        href = f"{bk.slug}/index.html"
        status = shelf_status(bk, n)
        title = html.escape(bk.title)
        heading = (f'<h2><a href="{href}">{title}</a></h2>' if live
                   else f'<h2>{title}</h2>')
        go = ('<span class="go" aria-hidden="true">Read &rarr;</span>' if live
              else '<span class="go">Not yet written</span>')
        # The chip is emitted hidden and empty: what it says depends on what
        # this device has stored, which only the page can know.
        chip = (f'<button class="off" type="button" data-offline="{bk.slug}" hidden></button>'
                if live else "")
        tiles.append(
            f'<article class="book" data-slug="{bk.slug}" data-live="{1 if live else 0}"'
            f' style="--bk-accent:{_legible(bk.theme.get("accent", "#333333"), [TILE_LIGHT, GROUND_LIGHT])};'
            f'--bk-accent-2:{_legible(bk.theme.get("accent_dark") or bk.theme.get("accent", "#999999"), [TILE_DARK, GROUND_DARK])}">'
            f'<div class="rule"></div>'
            f'<p class="kicker">{html.escape(bk.eyebrow)}</p>'
            f'{heading}'
            f'<p class="tagline">{html.escape(bk.tagline)}</p>'
            f'<div class="foot">'
            + (f'<span class="count">{html.escape(status)}</span>' if status else '<span></span>')
            + f'{go}{chip}</div>'
            f'</article>')

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
<main>
<header class="lede">
  <p class="eyebrow">Built from first principles</p>
  <h1>A library of books that show their working.</h1>
  <p>Each one begins at the beginning and derives what it uses. Where something is taken on
  trust it is marked as such, so you always know what you are standing on.</p>
</header>
<section class="continue" data-continue hidden aria-labelledby="continue-h">
  <h2 id="continue-h">Continue reading</h2>
  <ol></ol>
</section>
<div class="shelf">
{"".join(tiles)}
</div>
<p class="store" data-store hidden></p>
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
