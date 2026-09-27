#!/usr/bin/env python3
"""Production-mode screenshots and measurements: docs/ served under /library/, exactly as
GitHub Pages serves it, so pwa.js sees the book (drawer prev/next, positions, arrow keys,
standalone back all present). shoot.py serves at the root and misses all of that.

    python3 prodshot.py OUTDIR PATH [PATH ...] [options]

  --widths 390,1280     viewport widths (height 844 below 700px, else 900)
  --themes light,dark   colour scheme; the theme is also stored as a reader's choice
                        (library:v1.look and nmt-theme) unless --nostore
  --nostore             store nothing: the OS preference alone decides (first-visit reader)
  --touch               has_touch + is_mobile (pointer:coarse), as on a phone
  --standalone          pretend to be the installed app (navigator.standalone = true)
  --scroll Y            before the shot: a pixel offset, 'mid', 'end', or a fraction like 0.4
                        (an instant jump: the page's smooth scrolling would be caught mid-way)
  --click SELECTOR      click this after scrolling (e.g. '#mnav-btn', '.nav-menu')
  --wait MS             extra settle time after load/click (default 500)
  --full                whole scrolling page
  --eval JS             evaluate this expression (a function body returning JSON-able data)
                        on every page after the shot; printed as one JSON line per shot
  --prefix NAME         filename prefix (default none)
  --overlay DIR         serve the files in DIR over docs/ at the same paths: a request for
                        /library/X is answered from DIR/X when that exists, else docs/X.
                        This is how proof pages (proof.py) and scratch assets are shot
                        without writing anything into docs/
  --engine NAME         chromium (default) or webkit. WebKit is not installed here (see
                        scratchpad/ui/baselines/ENGINES); asking for it exits with a message

Files are OUTDIR/<prefix.><path with / as __>.<width>.<theme>[.touch].png. Service
workers are blocked so every shot is of the files on disk now. Writes nothing in the repo.

Useful --eval snippets (see DESIGN.md "Measuring"):
  "() => ({bar: document.querySelector('.topnav').getBoundingClientRect().height})"
  "() => getComputedStyle(document.querySelector('h1')).fontSize"
"""
import os, sys, json, asyncio, threading, socketserver, http.server, functools
ROOT = '/home/user/library'
argv = sys.argv[1:]
def opt(name, default=None, flag=False):
    if name in argv:
        i = argv.index(name)
        if flag:
            argv.pop(i); return True
        v = argv[i + 1]; del argv[i:i + 2]; return v
    return default
widths = [int(w) for w in opt('--widths', '390,1280').split(',')]
themes = opt('--themes', 'light,dark').split(',')
nostore = opt('--nostore', flag=True)
touch = opt('--touch', flag=True)
standalone = opt('--standalone', flag=True)
scroll = opt('--scroll')
click = opt('--click')
wait = int(opt('--wait', '500'))
full = opt('--full', flag=True)
ev = opt('--eval')
prefix = opt('--prefix', '')
overlay = opt('--overlay')
engine = opt('--engine', 'chromium')
if engine not in ('chromium', 'webkit'):
    raise SystemExit('prodshot: --engine is chromium or webkit, not %r' % engine)
if overlay is not None:
    overlay = os.path.abspath(overlay)
    if not os.path.isdir(overlay):
        raise SystemExit('prodshot: --overlay %s is not a directory' % overlay)
out, paths = argv[0], argv[1:]
os.makedirs(out, exist_ok=True)

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def translate_path(self, path):
        if path.startswith('/library/'): path = path[len('/library'):]
        elif path == '/library': path = '/'
        real = super().translate_path(path)
        if overlay:
            # the same path under the overlay wins when it exists
            rel = os.path.relpath(real, os.path.join(ROOT, 'docs'))
            if not rel.startswith('..'):
                o = os.path.join(overlay, rel)
                if os.path.isfile(o) or (os.path.isdir(o) and os.path.isfile(os.path.join(o, 'index.html'))):
                    return o
        return real
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(H, directory=os.path.join(ROOT, 'docs')))
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
BASE = 'http://127.0.0.1:%d/library/' % PORT

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        try:
            br = await getattr(pw, engine).launch()
        except Exception as e:
            print(json.dumps({'failed': 'launch', 'engine': engine, 'error': str(e)[:300]}))
            raise SystemExit('prodshot: cannot launch %s (see baselines/ENGINES)' % engine)
        for theme in themes:
            for w in widths:
                ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                           service_workers='block', color_scheme=theme,
                                           device_scale_factor=1, has_touch=touch, is_mobile=touch)
                init = ""
                if not nostore:
                    init += ("try{var s=JSON.parse(localStorage.getItem('library:v1')||'{}');s.look='%s';"
                             "localStorage.setItem('library:v1',JSON.stringify(s));"
                             "localStorage.setItem('nmt-theme','%s')}catch(e){}" % (theme, theme))
                if standalone:
                    init += "Object.defineProperty(navigator,'standalone',{get:()=>true});"
                if init:
                    await ctx.add_init_script(init)
                for p in paths:
                    pg = await ctx.new_page()
                    try:
                        await pg.goto(BASE + p, wait_until='networkidle', timeout=45000)
                        await pg.wait_for_timeout(wait)
                        if scroll is not None:
                            await pg.evaluate("""(s) => { const h = document.documentElement.scrollHeight - innerHeight;
                                const y = s === 'end' ? h : s === 'mid' ? h / 2 : (s.includes('.') ? h * parseFloat(s) : parseFloat(s));
                                window.scrollTo({top: y, left: 0, behavior: 'instant'}); }""", scroll)
                            await pg.wait_for_timeout(400)
                        if click:
                            await pg.click(click, timeout=5000)
                            await pg.wait_for_timeout(wait)
                        name = '%s%s.%d.%s%s%s.png' % (prefix + '.' if prefix else '', p.replace('/', '__'),
                                                   w, theme, '.touch' if touch else '',
                                                   '.' + engine if engine != 'chromium' else '')
                        f = os.path.join(out, name)
                        await pg.screenshot(path=f, full_page=full)
                        line = {'shot': f}
                        if ev:
                            line['eval'] = await pg.evaluate(ev)
                        print(json.dumps(line))
                    except Exception as e:
                        print(json.dumps({'failed': p, 'width': w, 'theme': theme, 'error': str(e)[:300]}))
                    await pg.close()
                await ctx.close()
        await br.close()
asyncio.run(main())
httpd.shutdown()
