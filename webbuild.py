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

ROOT = os.path.dirname(os.path.abspath(__file__))
STAGE = os.path.join(ROOT, ".webstage")
DOCS = os.path.join(ROOT, "docs")
VEND = os.path.join(ROOT, "vendor", "katex")

spec = importlib.util.spec_from_file_location("bp", os.path.join(ROOT, "build.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

NAV = """<nav class="topnav">
  <a class="brand" href="index.html">Newton&nbsp;→&nbsp;M-Theory</a>
  <div class="topnav-links">
    <a href="contents.html">Chapters</a>
    <a href="throughline.html">In Plain Terms</a>
    <a href="ledger.html">Math Ledger</a>
  </div>
</nav>"""

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — From Newton to M-Theory</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/katex.min.css">
<link rel="stylesheet" href="assets/book.css">
</head>
<body>
{nav}
<div class="wrap">
<nav class="sidebar">
  <a class="sb-home" href="contents.html">← All chapters</a>
  <p class="sb-title">{sbhead}</p>
  <div id="sb-toc">{toc}</div>
</nav>
<main class="main">
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
    js = open(os.path.join(ROOT, "assets", "book.js")).read()
    js = js.replace("numberEquations();", "/* numbered at build time */")
    js = re.sub(r"if \(window\.katex\) \{ typeset\(\); \}.*?\n  \}\);", "});", js, flags=re.S)
    return js


ARC = [
    ("Part 0",   "The Toolkit",
     "Numbers describe a thing only relative to a choice. The useful description is the one "
     "in which a hard problem falls apart into independent pieces."),
    ("Part I",   "The Action Principle",
     "Forces are the wrong primitive. Attach one number to each possible history, and nature "
     "selects the history where that number stops changing."),
    ("Part II",  "Special Relativity",
     "The speed limit is built into the geometry, not the materials. Magnetism turns out to be "
     "electricity, seen from a moving frame."),
    ("Part III", "General Relativity",
     "Gravity is not a force but the shape of the arena. Free fall is the straightest available "
     "motion."),
    ("Part IV",  "Quantum Mechanics",
     "\u201cWhat state is this in\u201d stops having a single answer. The mathematics was already "
     "built in Part\u00a00."),
    ("Part V",   "Quantum Field Theory",
     "Particles stop being fundamental. The field is; particles are its excitations, the way "
     "notes are excitations of a string."),
    ("Part VI",  "Gauge Theory",
     "Demand a symmetry hold locally rather than globally, and a force appears to enforce it. "
     "Every force is that one demand."),
    ("Part VII", "Strings and M-Theory",
     "Gravity refuses the treatment that worked for everything else \u2014 followed by an honest "
     "account of what is known and what is conjecture."),
]


def landing_page(stats):
    """docs/index.html, generated so the counts and the arc can never go stale."""
    tpl = open(os.path.join(ROOT, "src", "_landing.html")).read()

    built = {}          # part index -> (chapters written, chapters planned)
    for i, (_pt, _blurb, chs) in enumerate(bp.PARTS):
        done = sum(1 for c in chs
                   if os.path.exists(os.path.join(ROOT, "src", c[1] + ".html")))
        built[i] = (done, len(chs))

    rows = []
    for i, (k, title, blurb) in enumerate(ARC):
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
    open(os.path.join(DOCS, "index.html"), "w").write(tpl)
    return len(rows)


async def main():
    shutil.rmtree(STAGE, ignore_errors=True)
    bp.OUT = STAGE
    bp.build()

    shutil.rmtree(DOCS, ignore_errors=True)
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)

    # shared assets, fonts kept as separate cacheable files
    css = open(os.path.join(VEND, "katex.min.css")).read()
    css = re.sub(r'url\(fonts/', 'url(fonts/', css)
    open(os.path.join(DOCS, "assets", "katex.min.css"), "w").write(css)
    shutil.copytree(os.path.join(VEND, "fonts"), os.path.join(DOCS, "assets", "fonts"))
    shutil.copy(os.path.join(ROOT, "assets", "book.css"), os.path.join(DOCS, "assets"))
    open(os.path.join(DOCS, "assets", "book.js"), "w").write(runtime_js())
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")

    n = 0
    stats = {"words": 0, "eq": 0, "boxes": 0, "planned": len(bp.FLAT)}
    async with async_playwright() as pw:
        b = await pw.chromium.launch()

        async def render(src, title, desc, sbhead, wide, extra, dest,
                         count_into_stats=False):
            pg = await b.new_page(viewport={"width": 1280, "height": 1000})
            await pg.goto("file://" + src)
            await pg.wait_for_timeout(2400)
            body = await pg.evaluate("document.querySelector('.main .col').innerHTML")
            # prose word count: the maths is stripped, so a \(\gamma\) counts once, not
            # once per KaTeX span plus its MathML shadow
            words = await pg.evaluate("""() => {
                const d = document.querySelector('.main .col').cloneNode(true);
                d.querySelectorAll('.katex, script, style').forEach(e => e.remove());
                return (d.textContent.match(/[A-Za-z0-9\u2019'-]+/g) || []).length; }""")
            toc = await pg.evaluate("document.getElementById('sb-toc').innerHTML")
            await pg.close()
            body = body.replace('href="chapters/', 'href="')
            if count_into_stats:
                stats["words"] += words
                stats["eq"] += len(re.findall(r'class="katex"', body))
                stats["boxes"] += len(re.findall(r'class="callout plain"', body))
            open(dest, "w").write(SHELL.format(title=title, desc=html.escape(desc), nav=NAV,
                                               sbhead=sbhead, toc=toc, body=body,
                                               wide=wide, extra=extra))

        for num, slug, title, part, _m in bp.FLAT:
            src = os.path.join(STAGE, "chapters", slug + ".html")
            if not os.path.exists(src):
                continue
            raw = open(os.path.join(ROOT, "src", slug + ".html")).read()
            m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
            extra = "<script>\n" + m.group(1) + "\n</script>" if m else ""
            await render(src, f"{num} {title}",
                         f"Chapter {num} of From Newton to M-Theory: {title}.",
                         f"Ch {num}", "", extra, os.path.join(DOCS, slug + ".html"),
                         count_into_stats=True)
            n += 1

        for name, out, sbhead, desc in (
            ("index", "contents", "Parts", "Every chapter of From Newton to M-Theory."),
            ("ledger", "ledger", "Ledger",
             "Every mathematical object in the book: where it was defined, what for, and where it is spent."),
            ("throughline", "throughline", "Through-Line",
             "The whole book in plain language, with no mathematics.")):
            src = os.path.join(STAGE, name + ".html")
            if os.path.exists(src):
                t = {"index": "Chapters", "ledger": "Math Ledger",
                     "throughline": "In Plain Terms"}[name]
                await render(src, t, desc, sbhead, " wide", "",
                             os.path.join(DOCS, out + ".html"))
        await b.close()

    def human(x):
        return f"{x/1000:.0f}k" if x >= 10000 else f"{x:,}"
    landing_page({"CH": f"{n} / {stats['planned']}", "WORDS": human(stats["words"]),
                  "EQ": human(stats["eq"]), "BOXES": str(stats["boxes"])})

    shutil.rmtree(STAGE, ignore_errors=True)
    tot = sum(os.path.getsize(os.path.join(dp, f))
              for dp, _, fs in os.walk(DOCS) for f in fs)
    print(f"docs/: landing + {n} chapters + contents + ledger + through-line "
          f"({tot/1e6:.1f} MB)")
    print(f"       {stats['words']:,} words · {stats['eq']:,} expressions · "
          f"{stats['boxes']} plain-terms boxes")

asyncio.run(main())
