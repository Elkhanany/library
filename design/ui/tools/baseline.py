#!/usr/bin/env python3
"""Wave-0 baselines: every 'was N' the later waves are measured against (W0-HARNESS, C2-baselines).

    python3 baseline.py [contrast tables eq cpl spy weather verify]   # default: all; locked.sh

Writes scratchpad/ui/baselines/:
  contrast.json   measured, failing, unparsed (and the worst groups) per page x {390,1280} x
                  {light,dark}, from architect/contrast.js through prodshot --eval, so a later run of
                  `prodshot --eval "$(cat contrast.js)"` measures under the same conditions
  bar.json        .topnav height, brand x, Library x and each destination's x, per page x width
  tables.json     BC-900 at 390 and 1280: total evidence-table height and median row height; each
                  table's scrollWidth/clientWidth at 390, 1280, 1680 and 1920
  eq-wide.json    every physics display wider than 665px (35em at 19px) at 1280, with page and id
  eqnum.json      .eq, .eqnum and displays per physics page after load
  cpl.json        median characters per line of body text at 1280: BC-900, ch1-2, the Through-Line
                  and registry rows (trials.html)
  spy.json        sidebar spy accuracy on ch1-1 (shots/navigation/spy2.py)
  weather/        hub tiles hovered, one PNG per book and theme, plus the hub at rest
  verify.json     make.py + verify.py 'needing attention' per book, figcheck, from baselines/logs/
  shots/          the viewport screenshots the contrast census was taken on
The probes live in architect/probes/*.js and architect/contrast.js; reuse them for 'after'."""
import asyncio, functools, http.server, json, os, re, socketserver, statistics, subprocess, sys, threading

ROOT = '/home/user/library'
ARCH = os.path.dirname(os.path.abspath(__file__))
UI = os.path.dirname(ARCH)
B = os.path.join(UI, 'baselines')
PROBES = os.path.join(ARCH, 'probes')
PY = sys.executable
REF = open(os.path.join(B, 'REF')).read().strip() if os.path.exists(os.path.join(B, 'REF')) else None

CONTRAST_PAGES = [
    'index.html', 'newton-to-mtheory/index.html', 'breast-cancer/index.html',
    'newton-to-mtheory/contents.html', 'breast-cancer/contents.html',
    'breast-cancer/BC-900.html', 'breast-cancer/BC-500.html', 'breast-cancer/BC-870.html',
    'breast-cancer/BC-490.html', 'newton-to-mtheory/ch1-1.html', 'newton-to-mtheory/ch1-2.html',
    'newton-to-mtheory/ch3-5.html', 'newton-to-mtheory/ch4-6.html', 'breast-cancer/stories.html',
    'breast-cancer/trials.html', 'newton-to-mtheory/ledger.html', 'newton-to-mtheory/throughline.html',
    'the-ages-of-thought/index.html',     # the atlas
    'the-long-argument/index.html',       # the timeline
]
CPL_PAGES = ['breast-cancer/BC-900.html', 'newton-to-mtheory/ch1-2.html',
             'newton-to-mtheory/throughline.html', 'breast-cancer/trials.html']


def read(name):
    return open(os.path.join(PROBES, name)).read().strip() if name != 'contrast.js' \
        else open(os.path.join(ARCH, 'contrast.js')).read().strip()


def about(what):
    return {'what': what, 'ref': REF, 'engine': 'chromium (HeadlessChrome 141, Playwright 1.56)',
            'served': 'docs/ under /library/ by prodshot.py, service workers blocked'}


def save(name, obj):
    with open(os.path.join(B, name), 'w') as fh:
        json.dump(obj, fh, indent=1, sort_keys=False)
        fh.write('\n')
    print('  wrote baselines/%s' % name, flush=True)


def prodshot(out, paths, widths, themes, ev, extra=()):
    cmd = [PY, os.path.join(ARCH, 'prodshot.py'), out] + list(paths) + \
          ['--widths', ','.join(map(str, widths)), '--themes', ','.join(themes), '--eval', ev] + list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True)
    rows = []
    for line in r.stdout.splitlines():
        if not line.startswith('{'):
            continue
        d = json.loads(line)
        if 'failed' in d:
            print('  !! prodshot failed:', d, flush=True)
            continue
        name = os.path.basename(d['shot'])[:-4]
        parts = name.split('.')
        if parts[-1] == 'touch':
            parts = parts[:-1]
        theme, width = parts[-1], int(parts[-2])
        page = '.'.join(parts[:-2]).replace('__', '/')
        rows.append((page, width, theme, d.get('eval')))
    if r.returncode != 0:
        print('  !! prodshot exit %d: %s' % (r.returncode, r.stderr[-400:]), flush=True)
    return rows


def contrast():
    ev = '() => ({c: (%s)(), b: (%s)()})' % (read('contrast.js'), read('bar.js'))
    rows = prodshot(os.path.join(B, 'shots'), CONTRAST_PAGES, (390, 1280), ('light', 'dark'), ev)
    con, bar = {}, {}
    for page, w, theme, e in rows:
        c = e['c']
        con.setdefault(page, {}).setdefault(str(w), {})[theme] = {
            'measured': c['measured'], 'failing': c['failing'], 'unparsed': c['unparsed'],
            'groups': c['groups'][:6]}
        if theme == 'light':
            bar.setdefault(page, {})[str(w)] = e['b']
    missing = [(p, w, t) for p in CONTRAST_PAGES for w in ('390', '1280') for t in ('light', 'dark')
               if t not in con.get(p, {}).get(w, {})]
    if missing:
        print('  !! contrast runs missing:', missing, flush=True)
    tot = {k: sum(v[w][t][k] for v in con.values() for w in v for t in v[w])
           for k in ('measured', 'failing', 'unparsed')}
    save('contrast.json', {'_about': dict(about(
        'text-contrast census (architect/contrast.js). Pass later = failing 0, unparsed 0 and '
        'measured >= this page\'s value'), totals=tot, runs=len(rows)), 'pages': con})
    save('bar.json', {'_about': about('the library bar (architect/probes/bar.js), light theme; x in CSS px '
                                      'from the viewport left; {"bar": false} where a page has no .topnav '
                                      '(the hub, before wave 1)'), 'pages': bar})
    print('  contrast: %d runs, measured %d, failing %d, unparsed %d' % (len(rows), tot['measured'],
          tot['failing'], tot['unparsed']), flush=True)


def tables():
    rows = prodshot(os.path.join(B, 'shots', 'tables'), ['breast-cancer/BC-900.html'],
                    (390, 1280, 1680, 1920), ('light',), read('tables.js'))
    out = {'_about': about('BC-900 evidence tables (architect/probes/tables.js), light theme')}
    for _p, w, _t, e in rows:
        allrows = [h for t in e for h in t.get('rows', [])]
        out[str(w)] = {
            'tables': len(e),
            'totalHeight': sum(t.get('h', 0) for t in e),
            'medianRowHeight': statistics.median(allrows) if allrows else None,
            'rows': len(allrows),
            'scroll': [{'i': t['i'], 'cols': t.get('cols'), 'scrollWidth': t.get('sw'), 'clientWidth': t.get('cw'),
                        'ratio': round(t['sw'] / t['cw'], 3) if t.get('cw') else None,
                        'scroller': t.get('scroller'), 'height': t.get('h')} for t in e],
        }
    save('tables.json', out)


def eq():
    d = os.path.join(ROOT, 'docs', 'newton-to-mtheory')
    pages = ['newton-to-mtheory/' + f for f in sorted(os.listdir(d)) if f.endswith('.html')]
    rows = prodshot(os.path.join(B, 'shots', 'eq'), pages, (1280,), ('light',), read('eqwide.js'))
    wide, nums = [], {}
    for page, _w, _t, e in rows:
        nums[page] = {k: e[k] for k in ('eq', 'eqnum', 'eqWithOneNum', 'displays')}
        for x in e['wide']:
            wide.append({'page': page, 'id': x['id'], 'section': x.get('section'), 'display': x['i'],
                         'width': x['w'], 'box': x['box']})
    wide.sort(key=lambda x: -x['width'])
    save('eq-wide.json', {'_about': about('physics displays wider than 665px (35em at 19px) at 1280, light '
                                          '(architect/probes/eqwide.js); width is the rendered maths, box '
                                          'the display box'),
                          'count': len(wide), 'pages': sorted({x['page'] for x in wide}), 'displays': wide})
    save('eqnum.json', {'_about': about('.eq, .eqnum and .katex-display counts per physics page after load, '
                                        '1280 light (architect/probes/eqwide.js)'),
                        'totals': {k: sum(v[k] for v in nums.values()) for k in ('eq', 'eqnum', 'eqWithOneNum', 'displays')},
                        'pages': nums})
    print('  eq: %d pages, %d displays wider than 665px' % (len(rows), len(wide)), flush=True)


def cpl():
    rows = prodshot(os.path.join(B, 'shots', 'cpl'), CPL_PAGES, (1280,), ('light',), read('cpl.js'))
    save('cpl.json', {'_about': about('median characters per line of body text at 1280, light '
                                      '(architect/probes/cpl.js); trials.html = registry row text'),
                      'pages': {p: e for p, _w, _t, e in rows}})
    for p, _w, _t, e in rows:
        print('  cpl %-36s median %s (%d lines, %s px %s)' % (p, e['median'], e['lines'], e['fontPx'], e['family']),
              flush=True)


def spy():
    r = subprocess.run([PY, os.path.join(UI, 'shots', 'navigation', 'spy2.py')], capture_output=True, text=True)
    out = {'_about': about('sidebar spy on newton-to-mtheory/ch1-1.html at 1280: scroll in 300px steps down '
                           'to 60% and back up; at each step compare the TOC entry marked active with the last '
                           'h2/h3 above 120px (scratchpad/ui/shots/navigation/spy2.py)')}
    for line in r.stdout.splitlines():
        m = re.match(r'(down|up): samples (\d+) none (\d+) mismatch (\d+)', line.strip())
        if m:
            s, n, x = int(m.group(2)), int(m.group(3)), int(m.group(4))
            out[m.group(1)] = {'samples': s, 'none': n, 'mismatch': x,
                               'accuracy': round((s - n - x) / s, 3) if s else None}
    save('spy.json', out)
    print('  spy:', {k: v for k, v in out.items() if k != '_about'}, flush=True)


def weather():
    out = os.path.join(B, 'weather')
    os.makedirs(out, exist_ok=True)

    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def translate_path(self, path):
            if path.startswith('/library/'): path = path[len('/library'):]
            elif path == '/library': path = '/'
            return super().translate_path(path)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(H, directory=os.path.join(ROOT, 'docs')))
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = 'http://127.0.0.1:%d/library/' % httpd.server_address[1]
    made = []

    async def run():
        from playwright.async_api import async_playwright
        async with async_playwright() as pw:
            br = await pw.chromium.launch()
            for theme in ('light', 'dark'):
                ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block',
                                           color_scheme=theme, device_scale_factor=1)
                await ctx.add_init_script(
                    "try{var s=JSON.parse(localStorage.getItem('library:v1')||'{}');s.look='%s';"
                    "localStorage.setItem('library:v1',JSON.stringify(s));localStorage.setItem('nmt-theme','%s')}catch(e){}"
                    % (theme, theme))
                pg = await ctx.new_page()
                await pg.goto(base + 'index.html', wait_until='networkidle')
                await pg.wait_for_timeout(500)
                f = os.path.join(out, 'hub-rest-%s.png' % theme)
                await pg.screenshot(path=f); made.append(f)
                slugs = await pg.eval_on_selector_all('.book[data-slug]', 'els => els.map(e => e.dataset.slug)')
                for slug in slugs:
                    await pg.hover('.book[data-slug="%s"]' % slug)
                    await pg.wait_for_timeout(900)
                    f = os.path.join(out, 'hub-hover-%s-%s.png' % (slug, theme))
                    await pg.screenshot(path=f); made.append(f)
                    await pg.mouse.move(2, 890)
                    await pg.wait_for_timeout(400)
                await ctx.close()
            await br.close()
    try:
        asyncio.run(run())
    finally:
        httpd.shutdown()
    print('  weather: %d screenshots in baselines/weather/' % len(made), flush=True)


def verify():
    L = os.path.join(B, 'logs')
    out = {'_about': dict(about('make.py + verify.py per book and figcheck on newton-to-mtheory/ch*, run on the '
                                'wave-0 tree (logs in baselines/logs/)'), served='file:// (build/<slug>/)')}
    for slug in ('breast-cancer', 'newton-to-mtheory'):
        v = open(os.path.join(L, 'verify-%s.log' % slug)).read()
        mk = open(os.path.join(L, 'make-%s.log' % slug)).read()
        m = re.search(r'(\d+) pages · (\d+) typeset expressions · zero external requests · needing attention: (\d+)', v)
        b = re.search(r'built (\d+) chapters.*?\((\d+) MB', mk)
        out[slug] = {'pages': int(m.group(1)), 'typeset': int(m.group(2)), 'needingAttention': int(m.group(3)),
                     'flagged': [l.split()[0] for l in v.splitlines() if '<-- CHECK' in l],
                     'makeChapters': int(b.group(1)) if b else None, 'buildMB': int(b.group(2)) if b else None,
                     'makeExit': int(re.search(r'exit=(\d+)', mk).group(1)),
                     'verifyExit': int(re.search(r'exit=(\d+)', v).group(1))}
    fc = open(os.path.join(L, 'figcheck.log')).read()
    m = re.search(r'figcheck: (\d+) chapters.*?(\d+) failures', fc)
    out['figcheck'] = {'chapters': int(m.group(1)), 'failures': int(m.group(2))} if m else {'raw': fc[-300:]}
    save('verify.json', out)


STEPS = {'contrast': contrast, 'tables': tables, 'eq': eq, 'cpl': cpl, 'spy': spy, 'weather': weather,
         'verify': verify}
want = [a for a in sys.argv[1:] if a in STEPS] or list(STEPS)
for s in want:
    print('baseline: %s' % s, flush=True)
    STEPS[s]()
