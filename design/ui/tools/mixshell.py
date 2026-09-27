#!/usr/bin/env python3
"""Mixed-version smoke test (W0-HARNESS, C2-mixed-smoke). An installed reader's copy can hold new
pages on an old shell, or old pages on a new shell, until they accept the update. Both must keep a
working theme control and a working drawer.

    python3 mixshell.py [--ref REF] [--mode A|B|AB] [--shots DIR]      # reads docs/: locked.sh

docs/ is served under /library/, as GitHub Pages serves it, in two modes:
  A  the current pages, with docs/assets/{pwa.js,pwa.css,nav.css} (the shell) from `git show REF:`
  B  every book directory (pages, book.css, book.js, nav.json, ...) from `git show REF:`, with the
     current shell (docs/index.html, docs/assets/*, docs/sw.js, ...)
REF defaults to scratchpad/ui/baselines/REF (the commit wave 0 started from); pass the previous
wave's gate commit to test a wave. A file that did not exist at REF is a 404, as it would be for a
reader holding only the old copy.

On breast-cancer/BC-500.html and newton-to-mtheory/ch1-1.html, at 390 (touch) and 1280:
  - at 390, #mnav-btn opens the drawer: #mnav becomes visible inside the viewport;
  - some visible theme control flips html[data-theme] when pressed. The controls are the bar's
    button.nav-theme (DESIGN section 8), the floating #themer and the drawer's #mn-theme. One
    visible with the drawer closed is used first; failing that, the drawer is opened and the
    one inside it is used, which is where a phone keeps it today.
Service workers are blocked, so every request is answered by the mix above. Exits 1 on failure."""
import asyncio, functools, http.server, mimetypes, os, socketserver, subprocess, sys, threading

ROOT = '/home/user/library'
UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
argv = sys.argv[1:]
def opt(name, default=None):
    if name in argv:
        i = argv.index(name); v = argv[i + 1]; del argv[i:i + 2]; return v
    return default
REF = opt('--ref') or open(os.path.join(UI, 'baselines', 'REF')).read().strip()
MODES = opt('--mode', 'AB')
SHOTS = opt('--shots')
SHELL = {'assets/pwa.js', 'assets/pwa.css', 'assets/nav.css'}
SLUGS = sorted(d for d in os.listdir(DOCS) if os.path.isfile(os.path.join(DOCS, d, 'index.html')))
PAGES = ['breast-cancer/BC-500.html', 'newton-to-mtheory/ch1-1.html']
REF = subprocess.run(['git', 'rev-parse', REF], cwd=ROOT, capture_output=True, text=True,
                     check=True).stdout.strip()

_cache = {}
SERVED = {}          # mode -> docs-relative paths answered from REF
def at_ref(rel):
    if rel not in _cache:
        r = subprocess.run(['git', 'show', '%s:docs/%s' % (REF, rel)], cwd=ROOT, capture_output=True)
        _cache[rel] = r.stdout if r.returncode == 0 else None
    return _cache[rel]

def from_ref(mode, rel):
    if mode == 'A':
        return rel in SHELL
    return rel.split('/', 1)[0] in SLUGS and '/' in rel


class H(http.server.SimpleHTTPRequestHandler):
    mode = 'A'
    def log_message(self, *a): pass
    def rel(self):
        p = self.path.split('?', 1)[0].split('#', 1)[0]
        if p.startswith('/library/'):
            p = p[len('/library/'):]
        elif p == '/library':
            p = ''
        else:
            return None
        if p == '' or p.endswith('/'):
            p += 'index.html'
        return p
    def do_GET(self):
        rel = self.rel()
        if rel is not None and from_ref(self.mode, rel):
            data = at_ref(rel)
            SERVED.setdefault(self.mode, set()).add(rel)
            if data is None:
                self.send_error(404, 'not at REF')
                return
            self.send_response(200)
            self.send_header('Content-Type', mimetypes.guess_type(rel)[0] or 'application/octet-stream')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(data)
            return
        return super().do_GET()
    def translate_path(self, path):
        if path.startswith('/library/'): path = path[len('/library'):]
        elif path == '/library': path = '/'
        return super().translate_path(path)


fails, passes = [], 0
def ok(name, cond, detail=''):
    global passes
    print(('  PASS  ' if cond else '  FAIL  ') + name + (('  ' + str(detail)) if detail else ''), flush=True)
    if cond:
        passes += 1
    else:
        fails.append(name)

CTRL = "button.nav-theme, #themer, #mn-theme"
VISIBLE = """() => {
  const CTRL = "button.nav-theme, #themer, #mn-theme";
  const out = [];
  document.querySelectorAll(CTRL).forEach((b, i) => {
    const r = b.getBoundingClientRect(), cs = getComputedStyle(b);
    const vis = !b.hidden && cs.display !== 'none' && cs.visibility === 'visible' && +cs.opacity > 0.05
      && r.width > 4 && r.height > 4 && r.right > 0 && r.left < innerWidth && r.bottom > 0 && r.top < innerHeight;
    out.push({i: i, sel: b.id ? '#' + b.id : 'button.nav-theme', vis: vis, text: (b.textContent || b.getAttribute('aria-label') || '').trim().slice(0, 20)});
  });
  return out;
}"""


async def run_mode(mode, br, base):
    print('\nmode %s: %s' % (mode, 'current pages, shell (pwa.js, pwa.css, nav.css) from REF' if mode == 'A'
                            else 'book pages and book assets from REF, current shell'), flush=True)
    for page in PAGES:
        for w, touch in ((390, True), (1280, False)):
            tag = '%s %s at %d%s' % (mode, page, w, ' touch' if touch else '')
            ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                       service_workers='block', has_touch=touch, is_mobile=touch,
                                       color_scheme='light', device_scale_factor=1)
            ctx.set_default_timeout(8000)
            pg = await ctx.new_page()
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)[:120]))
            try:
                await pg.goto(base + page, wait_until='networkidle', timeout=45000)
                await pg.wait_for_timeout(700)
                drawer = None
                async def open_drawer():
                    btn = await pg.query_selector('#mnav-btn')
                    ok('%s: the drawer button is there' % tag, btn is not None)
                    if not btn:
                        return None
                    if touch:
                        await pg.tap('#mnav-btn')
                    else:
                        await pg.click('#mnav-btn')
                    await pg.wait_for_timeout(450)
                    st = await pg.evaluate("""() => { const p = document.getElementById('mnav');
                      if (!p) return null; const r = p.getBoundingClientRect(), cs = getComputedStyle(p);
                      return {open: p.classList.contains('open') || p.getAttribute('aria-hidden') === 'false',
                              inview: r.width > 40 && r.height > 40 && r.left < innerWidth - 20 && r.right > 20
                                      && r.top < innerHeight && r.bottom > 0,
                              shown: cs.visibility === 'visible' && cs.display !== 'none'}; }""")
                    good = bool(st) and st['open'] and st['inview'] and st['shown']
                    ok('%s: #mnav-btn opens the drawer' % tag, good, st)
                    if SHOTS:
                        os.makedirs(SHOTS, exist_ok=True)
                        await pg.screenshot(path=os.path.join(SHOTS, 'mix%s.%s.%d.drawer.png'
                                                              % (mode, page.replace('/', '__'), w)))
                    return good
                ctrls = await pg.evaluate(VISIBLE)
                vis = [c for c in ctrls if c['vis']]
                where = 'on the page'
                if not vis and w < 700:
                    drawer = await open_drawer()
                    ctrls = await pg.evaluate(VISIBLE)
                    vis = [c for c in ctrls if c['vis']]
                    where = 'in the open drawer'
                ok('%s: a visible theme control %s' % (tag, where), bool(vis),
                   ', '.join('%s%s' % (c['sel'], '' if c['vis'] else ' (hidden)') for c in ctrls) or 'none in the page')
                if vis:
                    c = vis[0]
                    loc = pg.locator(CTRL).nth(c['i'])
                    before = await pg.evaluate("document.documentElement.getAttribute('data-theme')")
                    if touch:
                        await loc.tap()
                    else:
                        await loc.click()
                    await pg.wait_for_timeout(350)
                    after = await pg.evaluate("document.documentElement.getAttribute('data-theme')")
                    ok('%s: pressing %s flips data-theme' % (tag, c['sel']),
                       before != after and after in ('light', 'dark'), '%s -> %s' % (before, after))
                if w < 700 and drawer is None:
                    await open_drawer()
                ok('%s: no page errors' % tag, not errs, errs[:2])
            except Exception as e:
                ok('%s ran to the end' % tag, False, str(e).splitlines()[0][:200])
            await ctx.close()


async def main():
    from playwright.async_api import async_playwright
    socketserver.TCPServer.allow_reuse_address = True
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for mode in MODES:
            handler = type('H' + mode, (H,), {'mode': mode})
            httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(handler, directory=DOCS))
            httpd.daemon_threads = True
            threading.Thread(target=httpd.serve_forever, daemon=True).start()
            try:
                await run_mode(mode, br, 'http://127.0.0.1:%d/library/' % httpd.server_address[1])
            finally:
                httpd.shutdown()
            got = sorted(SERVED.get(mode, ()))
            print('  (mode %s answered %d path(s) from REF: %s)' % (mode, len(got), ', '.join(got[:8])
                  + (' ...' if len(got) > 8 else '')), flush=True)
        await br.close()

print('mixshell: REF %s, modes %s' % (REF[:12], MODES))
asyncio.run(main())
print('\nmixshell: %s (%d passed)' % ('PASS' if not fails else '%d failure(s)' % len(fails), passes))
sys.exit(1 if fails else 0)
