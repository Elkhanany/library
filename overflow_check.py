import asyncio, sys
from playwright.async_api import async_playwright
F=["ch0-%d"%i for i in range(1,10)]+["ch1-%d"%i for i in range(1,5)]+["ch2-1","ch2-4"]
JS = """(()=>{
  const bad=[];
  document.querySelectorAll('.eq').forEach((eq,i)=>{
    const box = eq.getBoundingClientRect().width;
    let w = 0;
    eq.querySelectorAll('.katex-html').forEach(k=>{ w = Math.max(w, k.scrollWidth, k.getBoundingClientRect().width); });
    // also catch the .eq container itself scrolling
    const sc = eq.scrollWidth;
    if (w > box + 4 || sc > box + 4) bad.push({id:eq.id||('#'+i), need:Math.round(Math.max(w,sc)), have:Math.round(box)});
  });
  return bad;
})()"""
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); total=0
        for f in F:
            for W in (1280, 900):
                pg=await b.new_page(viewport={"width":W,"height":1000})
                await pg.goto("file:///home/claude/physics-book/build/chapters/%s.html"%f)
                await pg.wait_for_timeout(2200)
                await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
                await pg.wait_for_timeout(500)
                bad=await pg.evaluate(JS)
                if bad:
                    total+=len(bad)
                    print(f"{f} @{W}px: {len(bad)} overflow")
                    for x in bad[:12]: print("    ", x)
                await pg.close()
        print("\nTOTAL real overflows:", total)
        await b.close()
asyncio.run(main())
