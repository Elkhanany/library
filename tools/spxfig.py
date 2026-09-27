#!/usr/bin/env python3
"""
Try one of The Other End of the Trade's figures on its own, in seconds.

figcheck.py holds the finished book to account, but it needs make.py first,
which renders every chapter. This builds a page holding only the figures named,
in the book's own stylesheet and theme, and puts them through what the build
and figcheck will: at 1280px light and at 390px dark it checks that the page
throws nothing, that every canvas paints, that every control survives being
used and that the figure fits its column; and it loads the page twice and
compares the column, because the build saves the column after the scripts
have run and two builds of one source must be byte for byte the same.

    python3 tools/spxfig.py skew-simulator ev-bet-builder
    python3 tools/spxfig.py --all
    python3 tools/spxfig.py --shots DIR skew-simulator   also save screenshots

A figure's source is books/the-other-end-of-the-trade/figures/<id>.html.
"""
import argparse
import asyncio
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
import spx

BOOK = library.book(spx.SLUG)

PAINTED = """(c)=>{ if (!c.width || !c.height) return 'EMPTY';
  const x=c.getContext('2d'); const d=x.getImageData(0,0,c.width,c.height).data;
  let n=0; for(let i=3;i<d.length;i+=2000) if(d[i]>0) n++;
  return n>8 ? 'painted' : 'BLANK'; }"""

EXERCISE = """(root)=>{
  const f = document.getElementById(root);
  f.querySelectorAll('input[type=range]').forEach(r=>{
    const lo=+r.min, hi=+r.max;
    [lo, lo+(hi-lo)*0.37, hi, +r.defaultValue].forEach(v=>{
      r.value=v; r.dispatchEvent(new Event('input',{bubbles:true}));
      r.dispatchEvent(new Event('change',{bubbles:true}));});});
  f.querySelectorAll('input[type=checkbox],input[type=radio]').forEach(b=>{ b.click(); b.click(); });
  f.querySelectorAll('button').forEach(b=>b.click());
  f.querySelectorAll('input[type=number]').forEach(r=>{
    r.value = r.min || 0; r.dispatchEvent(new Event('input',{bubbles:true}));
    r.value = r.max || 100; r.dispatchEvent(new Event('input',{bubbles:true}));});
}"""

# The rules DESIGN.md section 8 puts on anything the build captures.
STATIC = [
    (re.compile(r"\b(innerHTML|outerHTML|insertAdjacentHTML|appendChild|insertBefore|"
                r"createElement|removeChild|replaceChildren)\b"),
     "builds or removes markup; the figure's markup must be static"),
    (re.compile(r"\bMath\.random\b"), "Math.random: seed it with DL.rng so two builds agree"),
    (re.compile(r"\bDate\.now\b|new Date\("), "reads the clock; the first state must be fixed"),
    (re.compile(r"\bsetInterval\b"), "setInterval: animate on request with requestAnimationFrame"),
]


def page(ids, draft=False):
    figs = spx.Figures()
    parts, scripts, errs = [], [], []
    for fid in ids:
        f = figs.get(fid)
        if f is None:
            errs.append("%s: no figures/%s.html" % (fid, fid))
            continue
        u = fid
        markup = f["markup"].replace("{{uid}}", u)
        if 'id="fig-%s"' % u not in markup:
            errs.append("%s: the figure must carry id=\"fig-{{uid}}\"" % fid)
        for rx, why in STATIC:
            if rx.search(f["script"]):
                errs.append("%s: %s" % (fid, why))
        if re.search(r"\brequestAnimationFrame\b", f["script"]) and "DL.still" not in f["script"]:
            errs.append("%s: animates without checking DL.still() for reduced motion" % fid)
        for m in re.finditer(r'<label for="([^"]+)"', markup):
            if 'id="%s"' % m.group(1) not in markup:
                errs.append("%s: <label for=\"%s\"> names no element" % (fid, m.group(1)))
        for m in re.finditer(r'<input\b[^>]*\bid="([^"]+)"', markup):
            if 'for="%s"' % m.group(1) not in markup and "aria-label" not in m.group(0):
                errs.append("%s: input #%s has no <label for> and no aria-label" % (fid, m.group(1)))
        for m in re.finditer(r"<button\b[^>]*>", markup):
            if 'type="button"' not in m.group(0):
                errs.append("%s: a button without type=\"button\"" % fid)
        parts.append('<h2 id="h-%s">%s</h2>\n<p>A paragraph of prose before the figure.</p>\n%s'
                     % (u, fid, markup))
        scripts.append(f["script"].replace("{{uid}}", u))
    css = library.read(os.path.join(library.ASSETS, "book.css")) + library.themecss(BOOK)
    nav = library.read(os.path.join(library.ASSETS, "nav.css"))
    js = library.read(os.path.join(library.ASSETS, "book.js"))
    doc = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>figures</title>
<style>%s</style><style>%s
:root{--lib-bar-h:0px}</style>
<script>%s</script>
</head><body>
<div class="wrap"><nav class="sidebar" aria-label="Chapter sections"><div id="sb-toc"></div></nav>
<main class="main" id="text"><div class="col">
<h1>Figures</h1>
%s
</div></main></div>
<script>
%s

%s
</script>
</body></html>""" % (css, nav, js, "\n".join(parts), figs.library_js(), "\n\n".join(scripts))
    return doc, errs


async def check(ids, shots):
    from playwright.async_api import async_playwright
    doc, errs = page(ids)
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(doc)
    tmp.close()
    url = "file://" + tmp.name
    bad = {fid: [e for e in errs if e.startswith(fid + ":")] for fid in ids}
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        snaps = []
        for width, theme in ((1280, "light"), (390, "dark"), (1280, "light")):
            ctx = await br.new_context(viewport={"width": width, "height": 900},
                                       is_mobile=width < 600, has_touch=width < 600,
                                       color_scheme=theme)
            pg = await ctx.new_page()
            errors = []
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            await pg.goto(url)
            await pg.evaluate("t => document.documentElement.setAttribute('data-theme', t)", theme)
            await pg.wait_for_timeout(700)
            if len(snaps) < 2 and width == 1280:
                await pg.evaluate("() => { if (window.NMT && NMT.resetForSnapshot) NMT.resetForSnapshot(); }")
                await pg.wait_for_timeout(60)
                snaps.append(await pg.evaluate("document.querySelector('.main .col').innerHTML"))
                if len(snaps) == 2:
                    await ctx.close()
                    continue
            for fid in ids:
                sel = "#fig-" + fid
                if not await pg.query_selector(sel):
                    continue
                cans = await pg.query_selector_all(sel + " canvas")
                states = [await pg.evaluate(PAINTED, c) for c in cans]
                fit = await pg.evaluate("""(s) => { const f = document.querySelector(s);
                    return f.scrollWidth <= f.clientWidth + 1; }""", sel)
                await pg.evaluate(EXERCISE, "fig-" + fid)
                await pg.wait_for_timeout(250)
                after = [await pg.evaluate(PAINTED, c) for c in cans]
                if any(s != "painted" for s in states + after):
                    bad[fid].append("%dpx %s: canvases %s then %s" % (width, theme, states, after))
                if not fit:
                    bad[fid].append("%dpx %s: wider than its column (it scrolls sideways)" % (width, theme))
                if shots:
                    os.makedirs(shots, exist_ok=True)
                    el = await pg.query_selector(sel)
                    await el.scroll_into_view_if_needed()
                    await el.screenshot(path=os.path.join(shots, "%s-%d-%s.png" % (fid, width, theme)))
            for fid in ids:
                for e in errors:
                    bad[fid].append("%dpx %s: %s" % (width, theme, e[:200]))
            await ctx.close()
        await br.close()
    if len(snaps) == 2 and snaps[0] != snaps[1]:
        a, b = snaps
        k = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        for fid in ids:
            bad[fid].append("two loads saved different columns, near: %r / %r"
                            % (a[max(0, k - 60):k + 60], b[max(0, k - 60):k + 60]))
    os.unlink(tmp.name)
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--all", action="store_true", help="every figure in figures/")
    ap.add_argument("--shots", metavar="DIR", help="save each figure's screenshots here")
    args = ap.parse_args()
    ids = args.ids
    if args.all:
        ids = sorted(f[:-5] for f in os.listdir(spx.FIGS) if f.endswith(".html"))
    if not ids:
        ap.error("name a figure, or --all")
    bad = asyncio.run(check(ids, args.shots))
    n = 0
    for fid in ids:
        if bad[fid]:
            n += 1
            print("  FAIL  %s" % fid)
            for e in bad[fid]:
                print("        " + e)
        else:
            print("  ok    %s" % fid)
    print("spxfig: %d figure%s, %d failing" % (len(ids), "s" * (len(ids) != 1), n))
    sys.exit(1 if n else 0)


if __name__ == "__main__":
    main()
