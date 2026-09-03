#!/usr/bin/env python3
"""Verify the shipped build at desktop and phone widths, with all network blocked."""
import asyncio, sys, os, glob, importlib.util
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
BOOK = library.book(os.environ.get("NMT_BOOK", "newton-to-mtheory"))

from playwright.async_api import async_playwright

# Source-level check first: it is cheap, and it catches a class of fault the
# rendered-page audit cannot see, because the browser has already eaten the text
# by the time we measure the page.
_spec = importlib.util.spec_from_file_location("tagcheck", os.path.join(os.path.dirname(os.path.abspath(__file__)), "tagcheck.py"))
_tc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_tc)
_TAGFAIL = _tc.main(sorted(glob.glob(os.path.join(BOOK.src, "ch*.html"))))
print()

BUILD = os.path.join(library.ROOT, "build", BOOK.slug)
F=[f[:-5] for f in sorted(os.listdir(BUILD)) if f.endswith(".html")]
OVF="""(()=>{let bad=0;document.querySelectorAll('.eq').forEach(eq=>{const box=eq.getBoundingClientRect().width;
 let w=eq.scrollWidth;eq.querySelectorAll('.katex-html').forEach(k=>{w=Math.max(w,k.scrollWidth,k.getBoundingClientRect().width)});
 if(w>box+4)bad++});return bad})()"""
async def run(b,f,W,mobile):
    ctx=await b.new_context(viewport={"width":W,"height":900},is_mobile=mobile,has_touch=mobile)
    ext=[]
    await ctx.route("**/*", lambda r: (ext.append(r.request.url), asyncio.ensure_future(r.abort()))
        if not r.request.url.startswith("file://") else asyncio.ensure_future(r.continue_()))
    pg=await ctx.new_page(); errs=[]
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
    await pg.goto("file://" + os.path.join(BUILD, f + ".html").replace(os.sep, "/"))
    await pg.wait_for_timeout(1800)
    await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
    await pg.wait_for_timeout(400)
    r=await pg.evaluate("""(()=>{window.scrollTo(500,0);const sx=window.scrollX;window.scrollTo(0,0);
      return {kx:document.querySelectorAll('.katex').length,
        err:document.querySelectorAll('.katex-error').length,
        raw:(document.body.innerText.match(/\\\\[a-zA-Z]+\\{/g)||[]).length,
        ref:[...document.querySelectorAll('.eqref')].filter(a=>!a.textContent.trim()||a.textContent==='(?)').length,
        canv:[...document.querySelectorAll('canvas')].filter(c=>c.width>0).length,
        hscroll:sx}})()""")
    r["ovf"]=await pg.evaluate(OVF); r["ext"]=len(ext); r["errs"]=errs[:1]
    await ctx.close(); return r
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); kx=0; bad=0
        for f in F:
            d=await run(b,f,1280,False); m=await run(b,f,390,True)
            kx+=d["kx"]
            problem = (d["err"] or d["raw"] or d["ref"] or d["ovf"] or d["ext"] or d["errs"]
                       or m["err"] or m["raw"] or m["hscroll"] or m["ext"] or m["errs"])
            if problem: bad+=1
            print(f"{f:9s} desktop katex={d['kx']:4d} ovf={d['ovf']} canvas={d['canv']} | "
                  f"phone hscroll={m['hscroll']} | external={d['ext']+m['ext']} "
                  f"{'ok' if not problem else '<-- CHECK '+str(d['errs']+m['errs'])}")
        print(f"\n{len(F)} pages · {kx} typeset expressions · zero external requests · needing attention: {bad + _TAGFAIL}")
        await b.close()
asyncio.run(main())
