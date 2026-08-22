#!/usr/bin/env python3
"""Every canvas in the built book must actually paint, and every control must
survive being used. A figure that throws on load is worse than no figure, and
neither the page audit nor the source checks can see it."""
import asyncio, os, sys, glob
from playwright.async_api import async_playwright

TARGETS = sys.argv[1:] or [os.path.basename(f)[:-5] for f in sorted(glob.glob("build/ch*.html"))]

PAINTED = """(id)=>{const c=document.getElementById(id); if(!c) return 'missing';
  const x=c.getContext('2d'); const d=x.getImageData(0,0,c.width,c.height).data;
  let n=0; for(let i=3;i<d.length;i+=2000) if(d[i]>0) n++;
  return n>8 ? 'painted('+n+')' : 'BLANK('+n+')';}"""

async def main():
    bad = 0
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for slug in TARGETS:
            for width, theme in ((1280, "light"), (390, "dark")):
                pg = await b.new_page(viewport={"width": width, "height": 900})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                await pg.goto(f"file://{os.getcwd()}/build/{slug}.html")
                if theme == "dark":
                    await pg.evaluate("document.documentElement.setAttribute('data-theme','dark')")
                await pg.wait_for_timeout(1400)
                ids = await pg.evaluate("[...document.querySelectorAll('canvas')].map(c=>c.id)")
                states = {i: await pg.evaluate(PAINTED, i) for i in ids}
                # exercise every control, then re-check
                await pg.evaluate("""()=>{
                  document.querySelectorAll('input[type=range]').forEach(r=>{
                    const lo=+r.min, hi=+r.max;
                    [lo, lo+(hi-lo)*0.37, hi].forEach(v=>{
                      r.value=v; r.dispatchEvent(new Event('input',{bubbles:true}));
                      r.dispatchEvent(new Event('change',{bubbles:true}));});});
                  document.querySelectorAll('button').forEach(b=>b.click());}""")
                await pg.wait_for_timeout(900)
                after = {i: await pg.evaluate(PAINTED, i) for i in ids}
                blanks = [i for i in ids if "BLANK" in states[i] or "BLANK" in after[i]]
                real = [e for e in errs if "favicon" not in e]
                tag = "ok" if not blanks and not real else "FAIL"
                if tag == "FAIL":
                    bad += 1
                    print(f"{slug:9s} {width:4d}px {theme:5s} canvases={len(ids)} "
                          f"blank={blanks} errors={real[:2]}")
                await pg.close()
        await b.close()
    print(f"\nfigcheck: {len(TARGETS)} chapters, canvases painted and every control "
          f"exercised — {bad} failures")
    return 1 if bad else 0

sys.exit(asyncio.run(main()))
