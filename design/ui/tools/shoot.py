#!/usr/bin/env python3
"""Screenshot built pages of the library, served over HTTP under /library/ as GitHub Pages serves them.

    python3 shoot.py OUTDIR PATH [PATH ...] [--widths 390,1280] [--themes light,dark] [--full]

PATH is relative to the site root, e.g. index.html, breast-cancer/index.html,
breast-cancer/BC-900.html, newton-to-mtheory/contents.html. Files are named
<path-with-slashes-as-__>.<width>.<theme>.png. Viewport height is 900 (844 on phones);
--full captures the whole scrolling page. Service workers are blocked so every shot is of
the files on disk now."""
import os, sys, asyncio, threading, socketserver, http.server, functools
ROOT = '/home/user/library'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
opts = {a.split('=')[0]: (a.split('=')[1] if '=' in a else True) for a in sys.argv[1:] if a.startswith('--')}
for i, a in enumerate(sys.argv):
    if a in ('--widths', '--themes') and i + 1 < len(sys.argv):
        opts[a] = sys.argv[i + 1]; args = [x for x in args if x != sys.argv[i + 1]]
out, paths = args[0], args[1:]
widths = [int(w) for w in str(opts.get('--widths', '390,1280')).split(',')]
themes = str(opts.get('--themes', 'light,dark')).split(',')
full = bool(opts.get('--full'))
os.makedirs(out, exist_ok=True)
class H(http.server.SimpleHTTPRequestHandler):
    # Served under /library/ exactly as GitHub Pages serves it, so pwa.js recognises
    # the book and the drawer, positions and folio behave as they do for readers.
    def translate_path(self, path):
        if path.startswith('/library/'):
            path = path[len('/library'):]
        elif path == '/library':
            path = '/'
        return super().translate_path(path)
    def log_message(self, *a): pass
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(H, directory=os.path.join(ROOT, 'docs')))
port = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for theme in themes:
            for w in widths:
                ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                           service_workers='block', color_scheme=theme,
                                           device_scale_factor=1)
                await ctx.add_init_script("try{localStorage.setItem('nmt-theme','%s')}catch(e){}" % theme)
                for p in paths:
                    pg = await ctx.new_page()
                    try:
                        await pg.goto('http://127.0.0.1:%d/library/%s' % (port, p), wait_until='networkidle', timeout=30000)
                        await pg.wait_for_timeout(500)
                        f = os.path.join(out, '%s.%d.%s.png' % (p.replace('/', '__'), w, theme))
                        await pg.screenshot(path=f, full_page=full)
                        print(f)
                    except Exception as e:
                        print('FAILED', p, w, theme, e)
                    await pg.close()
                await ctx.close()
        await br.close()
asyncio.run(main())
httpd.shutdown()
