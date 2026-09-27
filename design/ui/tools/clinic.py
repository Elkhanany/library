#!/usr/bin/env python3
"""The clinical apparatus, asserted (W3-CLINIC; W4-MATH folds these into navcheck).

    python3 probes/clinic.py            # docs/ (served under /library/) and build/breast-cancer
    python3 probes/clinic.py --static   # the markup checks only, no browser
    python3 probes/clinic.py --nobuild  # skip the Dropbox build (build/ is only as fresh as make.py)

Reads docs/ and build/, so run it through architect/locked.sh. CLINIC_PORT picks the port
(default: any free one). Exit 1 on any failure.

Markup (every docs/breast-cancer/BC-*.html, as saved by the build):
  - no id is used twice (NAV-20: there were 93 across 24 chapters);
  - every evidence block has p.ev-title (and any p.ev-note) before its table; every th and td
    carries a c-* column class, every td a data-label; no p.ct-cap is left;
  - story wrappers are story-<question id>; every .trial in the column has data-trial; chips
    are saved as span.trial.chip (the build runs under file:, where they stay spans);
  - no mark keeps a title (the build moved it to data-facts), and no state is saved: no .more,
    no aria-expanded, no open reference list;
  - h2#references is followed by details.refs-list whose summary counts its entries.

Behaviour (Chromium, docs served under /library/ as on GitHub Pages):
  - BC-900 at 1280: evidence tables total <= 7,000px, median row <= 200px, every ev-title
    above its table, the cue on every table with hidden columns and on no other;
    at 1680 and 1920 every table fits (scrollWidth == clientWidth);
  - BC-900 at 390: total <= 6,500px, every visible non-first td shows its label line;
  - BC-900 cited paragraphs: baseline-to-baseline gaps vary by <= 1px (390 and 1280);
  - touch at 390: a tap on the first trial mark opens the sheet with the facts and a link to
    trials.html#t-<key>; following it opens that registry row; no mark has a title;
  - keyboard at 1280: tab stops added by marks <= distinct keys per h2 section; Tab reaches
    the first mark of a section, Enter opens its card, Escape closes it;
  - Enter then Tab / Shift+Tab on every mark of BC-900 and BC-870 (.col [data-trial][tabindex=0],
    .col .gloss[tabindex=0]) at 390 and 1280: Enter puts focus in the card; the key takes it out;
    the focused element's rect intersects the viewport; focus is on the mark or within 1 screen
    of it; scrollY moves by less than 1 screen; Shift+Tab returns to the mark;
  - BC-870 at 390: the next-chapter card is <= 1.5 screens below the end of the prose;
    #r-<12th entry> opens the list, and the entry is in view and highlighted;
  - page.pdf() of BC-900 holds the last reference, every evidence-table head, no cue text;
    under print media every evidence th and td computes to 8pt;
  - story sizes: .st-title > .sq-ask > story dd >= callout text, at 390 and 1280.

The Dropbox build (build/breast-cancer, file://):
  - chips stay spans, and the trial card has no registry link."""
import asyncio, collections, functools, glob, html.parser, http.server, json, os, re, socketserver
import statistics, sys, threading, zlib

ROOT = '/home/user/library'
DOCS = os.path.join(ROOT, 'docs')
BOOK = os.path.join(DOCS, 'breast-cancer')
BUILD = os.path.join(ROOT, 'build', 'breast-cancer')
FAILS = []


def check(ok, what, detail=''):
    print('  %s  %s%s' % ('ok  ' if ok else 'FAIL', what, ('  (%s)' % detail) if detail else ''))
    if not ok:
        FAILS.append(what)


# ------------------------------------------------------------------ markup
class Tags(html.parser.HTMLParser):
    """A flat list of (tag, attrs, depth, text-so-far index) with the text between them."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags, self.stack, self.text = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a, tuple(t for t, _ in self.stack)))
        if tag not in ('br', 'img', 'input', 'meta', 'link', 'hr', 'wbr', 'source', 'col'):
            self.stack.append((tag, a))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break


def markup():
    print('markup: docs/breast-cancer/BC-*.html')
    files = sorted(glob.glob(os.path.join(BOOK, 'BC-*.html')))
    dup, dupch = 0, 0
    bad = collections.defaultdict(list)
    for f in files:
        name = os.path.basename(f)
        s = open(f, encoding='utf-8').read()
        s = re.sub(r'<script\b.*?</script>', '', s, flags=re.S)
        ids = collections.Counter(re.findall(r'(?<![-\w])id="([^"]*)"', s))
        d = sum(v - 1 for v in ids.values() if v > 1)
        dup += d
        dupch += d > 0
        col = s[s.find('<div class="col'):]
        if 'class="ct-cap"' in col:
            bad['ct-cap left'].append(name)
        for ev in re.findall(r'<div class="evidence[^"]*">(.*?)</table></div></div>', col, re.S):
            # a caption, when the block has one, is p.ev-title (then any p.ev-note), all of it
            # before the table; a captionless block starts with the scroller
            head, rest = ev.split('<div class="ev-scroll', 1) if '<div class="ev-scroll' in ev else ('', ev)
            if (head and not re.fullmatch(r'<p class="ev-title">.*?</p>(<p class="ev-note">.*?</p>)?', head, re.S)) \
                    or 'ev-title' in rest or 'ev-note' in rest or not rest.startswith('"><table'):
                bad['ev-title not before the table'].append(name)
            if re.search(r'<t[hd](?=[\s>])(?![^>]*class="c-)', ev):
                bad['a th or td without a c-* class'].append(name)
            if re.search(r'<td(?=[\s>])(?![^>]*data-label=)', ev):
                bad['a td without data-label'].append(name)
        for sid in re.findall(r'<div class="story" id="([^"]*)"', col):
            if not sid.startswith('story-SQ-'):
                bad['story wrapper id'].append('%s:%s' % (name, sid))
        for m in re.finditer(r'<(\w+)([^>]*\bclass="(?:[^"]*\s)?(?:trial|gloss)(?:\s[^"]*)?"[^>]*)>', col):
            tag, attrs = m.group(1), m.group(2)
            if 'data-trial=' not in attrs and 'gloss' not in attrs:
                bad['a .trial without data-trial'].append(name)
            if re.search(r'\stitle="', attrs):
                bad['a mark keeps its title'].append(name)
            if 'chip' in attrs.split('class="')[1].split('"')[0] and tag != 'span':
                bad['a chip saved as a link'].append(name)
        if re.search(r'class="evidence[^"]*\bmore\b', col) or 'aria-expanded' in col:
            bad['state saved in the page'].append(name)
        if '<h2 class="refs-head" id="references">' in col:
            m = re.search(r'<details class="refs-list"( open)?><summary>All (\d+) references?</summary>'
                          r'\s*<ol class="refs">(.*?)</ol>\s*</details>', col, re.S)
            if not m:
                bad['references not in details.refs-list'].append(name)
            else:
                if m.group(1):
                    bad['reference list saved open'].append(name)
                if int(m.group(2)) != len(re.findall(r'<li id="r-', m.group(3))):
                    bad['summary miscounts the references'].append(name)
    check(dup == 0, 'no duplicate ids', '%d in %d of %d chapters' % (dup, dupch, len(files)))
    for k in ('ct-cap left', 'ev-title not before the table', 'a th or td without a c-* class',
              'a td without data-label', 'story wrapper id', 'a .trial without data-trial',
              'a mark keeps its title', 'a chip saved as a link', 'state saved in the page',
              'references not in details.refs-list', 'reference list saved open',
              'summary miscounts the references'):
        v = bad.get(k, [])
        check(not v, 'markup: ' + k if v else 'markup: no ' + k.replace('a ', '', 1), ', '.join(v[:4]))


# ------------------------------------------------------------------ pdf text
def pdf_text(b):
    """The text of a Chromium page.pdf(), through each font's ToUnicode map. Enough to ask
    whether a string was printed; spacing is not reproduced, so compare without spaces."""
    objs = {int(n): o for n, o in re.findall(rb'(\d+) 0 obj(.*?)endobj', b, re.S)}

    def stream(o):
        m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', o, re.S)
        if not m:
            return b''
        d = m.group(1)
        if b'/FlateDecode' in o[:m.start()]:
            d = zlib.decompressobj().decompress(d)
        return d

    def ref(o, key):
        m = re.search(rb'/' + key + rb'\s+(\d+) 0 R', o)
        return int(m.group(1)) if m else None

    cache = {}

    def cmap(n):
        if n not in cache:
            c, s = {}, stream(objs.get(n, b'')).decode('latin-1')
            for blk in re.findall(r'beginbfchar(.*?)endbfchar', s, re.S):
                for a, u in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
                    c[int(a, 16)] = bytes.fromhex(u).decode('utf-16-be', 'replace')
            for blk in re.findall(r'beginbfrange(.*?)endbfrange', s, re.S):
                for lo, hi, u in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
                    for i, g in enumerate(range(int(lo, 16), int(hi, 16) + 1)):
                        c[g] = chr(int(u, 16) + i)
            cache[n] = c
        return cache[n]

    out = []
    for n, o in sorted(objs.items()):
        if not re.search(rb'/Type\s*/Page\b', o):
            continue
        res = objs.get(ref(o, b'Resources'), o) if ref(o, b'Resources') else o
        fm = re.search(rb'/Font\s*<<(.*?)>>', res, re.S)
        fd = fm.group(1) if fm else objs.get(ref(res, b'Font'), b'')
        fonts = {}
        for name, fn in re.findall(rb'/(\w+)\s+(\d+) 0 R', fd):
            tu = ref(objs.get(int(fn), b''), b'ToUnicode')
            fonts[name.decode()] = cmap(tu) if tu else {}
        cm = re.search(rb'/Contents\s*\[(.*?)\]', o, re.S)
        ids = [int(x) for x in re.findall(rb'(\d+) 0 R', cm.group(1))] if cm else [ref(o, b'Contents')]
        content = '\n'.join(stream(objs.get(c, b'')).decode('latin-1') for c in ids if c)
        font = {}
        for t in re.finditer(r'/(\w+)\s+[-\d.]+\s+Tf|\[((?:[^\]\\]|\\.)*)\]\s*TJ|<([0-9A-Fa-f]*)>\s*Tj|\bET\b',
                             content):
            if t.group(1):
                font = fonts.get(t.group(1), {})
                continue
            if t.group(2) is None and t.group(3) is None:
                out.append('\n')
                continue
            for h in (re.findall(r'<([0-9A-Fa-f]*)>', t.group(2)) if t.group(2) is not None else [t.group(3)]):
                out.append(''.join(font.get(int(h[i:i + 4], 16), '') for i in range(0, len(h), 4)))
    return ''.join(out)


# ------------------------------------------------------------------ browser
TABLES_JS = r"""() => {
  const out = [...document.querySelectorAll('.main .evidence')].map(ev => {
    const t = ev.querySelector('table'), sc = ev.querySelector('.ev-scroll') || ev;
    const tt = ev.querySelector('.ev-title');
    const cue = ev.classList.contains('more') && getComputedStyle(ev, '::after').content.includes('more columns');
    const tds = [...t.querySelectorAll('tbody td:not(:first-child)')].filter(td => td.getClientRects().length);
    const lab = tds.filter(td => { const b = getComputedStyle(td, '::before');
      return b.display === 'block' && /^"|attr/.test(b.content) && b.content !== '""'; }).length;
    return {h: t.getBoundingClientRect().height,
            rows: [...t.querySelectorAll('tbody tr')].map(r => r.getBoundingClientRect().height),
            sw: sc.scrollWidth, cw: sc.clientWidth, cue: cue,
            above: !tt || tt.getBoundingClientRect().bottom <= t.getBoundingClientRect().top,
            tds: tds.length, labels: lab};
  });
  return out;
}"""

GAPS_JS = r"""() => {
  const gaps = [];
  document.querySelectorAll('.main .col > p').forEach(p => {
    if (!p.querySelector('.cite')) return;
    const b = new Set();
    const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) {
      const t = w.currentNode;
      if (!t.nodeValue.trim() || t.parentElement.closest('sup, code, .katex')) continue;
      const r = document.createRange(); r.selectNodeContents(t);
      for (const rc of r.getClientRects()) if (rc.width > 0) b.add(rc.bottom + scrollY);
    }
    const lines = [];
    [...b].sort((x, y) => x - y).forEach(v => { if (!lines.length || v - lines[lines.length - 1] > 3) lines.push(v); });
    for (let i = 1; i < lines.length; i++) gaps.push(lines[i] - lines[i - 1]);
  });
  return gaps;
}"""

SIZES_JS = r"""() => {
  const px = s => { const e = document.querySelector(s); return e ? parseFloat(getComputedStyle(e).fontSize) : null; };
  return {title: px('.col .story .st-title'), ask: px('.col .story .sq-ask'), dd: px('.col .story .sq-moves dd'),
          callout: px('.col .callout p')};
}"""

STOPS_JS = r"""() => {
  const col = document.querySelector('.main .col');
  let per = [], seen = new Set();
  col.querySelectorAll('h2, .trial[data-trial], .gloss').forEach(el => {
    if (el.tagName === 'H2') { per.push(seen.size); seen = new Set(); return; }
    seen.add(el.dataset.trial ? 't:' + el.dataset.trial : 'g:' + el.textContent.trim().toLowerCase());
  });
  per.push(seen.size);
  const stops = [...col.querySelectorAll('.trial[data-trial], .gloss')].filter(el =>
    el.tabIndex >= 0 && el.getAttribute('tabindex') !== '-1' && (el.tagName === 'A' || el.hasAttribute('tabindex')));
  return {stops: stops.length, keys: per.reduce((a, b) => a + b, 0)};
}"""


def serve():
    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def translate_path(self, path):
            if path.startswith('/library/'):
                path = path[len('/library'):]
            return super().translate_path(path)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(('127.0.0.1', int(os.environ.get('CLINIC_PORT', '0'))),
                                   functools.partial(H, directory=DOCS))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, 'http://127.0.0.1:%d/library/breast-cancer/' % httpd.server_address[1]


async def browser(base, build):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        br = await pw.chromium.launch()

        async def page(w, url, touch=False, theme='light'):
            ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                       service_workers='block', color_scheme=theme,
                                       has_touch=touch, is_mobile=touch, device_scale_factor=1)
            pg = await ctx.new_page()
            await pg.goto(url, wait_until='networkidle' if url.startswith('http') else 'load', timeout=60000)
            await pg.wait_for_timeout(700)
            return ctx, pg

        print('evidence tables: BC-900')
        for w in (1280, 390, 1680, 1920):
            ctx, pg = await page(w, base + 'BC-900.html')
            t = await pg.evaluate(TABLES_JS)
            await ctx.close()
            total = round(sum(x['h'] for x in t))
            rows = [r for x in t for r in x['rows']]
            if w == 1280:
                check(total <= 7000, '1280: total table height <= 7,000px', '%dpx, baseline 13,311' % total)
                med = statistics.median(rows)
                check(med <= 200, '1280: median row <= 200px', '%.1fpx, was 373' % med)
                check(all(x['above'] for x in t), '1280: every ev-title above its table')
                wrong = [i for i, x in enumerate(t) if x['cue'] != (x['sw'] > x['cw'])]
                check(not wrong, '1280: the cue shows exactly while columns are hidden',
                      '%d of %d tables hide columns' % (sum(x['sw'] > x['cw'] for x in t), len(t)))
            elif w == 390:
                check(total <= 6500, '390: total table height <= 6,500px', '%dpx, baseline 11,916' % total)
                check(all(x['labels'] == x['tds'] for x in t), '390: every visible non-first td has its label line',
                      '%d of %d' % (sum(x['labels'] for x in t), sum(x['tds'] for x in t)))
            else:
                check(all(x['sw'] == x['cw'] for x in t), '%d: every table fits (scrollWidth == clientWidth)' % w,
                      str([(x['sw'], x['cw']) for x in t]))

        print('citations: line spacing in cited paragraphs')
        for w in (390, 1280):
            ctx, pg = await page(w, base + 'BC-900.html')
            g = await pg.evaluate(GAPS_JS)
            await ctx.close()
            check(bool(g) and max(g) - min(g) <= 1, '%d: baseline gaps vary by <= 1px' % w,
                  '%d gaps, %.1f to %.1f' % (len(g), min(g), max(g)) if g else 'none measured')

        print('cards: touch at 390')
        ctx, pg = await page(390, base + 'BC-900.html', touch=True)
        await pg.click('.col .trial[data-trial]', timeout=5000)
        await pg.wait_for_timeout(500)
        s = await pg.evaluate("""() => { const c = document.querySelector('.refcard.sheet.on');
            const m = document.querySelector('.col .trial[data-trial][aria-expanded="true"]');
            const go = c && c.querySelector('a.rc-go');
            return {sheet: !!c, facts: !!(c && c.querySelector('.rc-f') && c.querySelector('.rc-f').textContent.trim()),
                    href: go && go.getAttribute('href'), key: m && m.dataset.trial,
                    titles: document.querySelectorAll('.col .trial[title], .col .gloss[title]').length}; }""")
        check(s['sheet'] and s['facts'], 'the tap opens the sheet with the facts')
        check(bool(s['key']) and s['href'] == 'trials.html#t-' + s['key'],
              'the sheet links to trials.html#t-<key>', str(s['href']))
        check(s['titles'] == 0, 'no hydrated mark keeps a title', '%d do' % s['titles'])
        if s['href']:
            await pg.click('.refcard.sheet.on a.rc-go')
            await pg.wait_for_load_state('networkidle')
            await pg.wait_for_timeout(1200)
            o = await pg.evaluate("(k) => { const d = document.getElementById('t-' + k); "
                                  "return {url: location.pathname + location.hash, open: !!(d && d.open)}; }", s['key'])
            check(o['open'], 'following the link opens that registry row', o['url'])
        await ctx.close()

        print('cards: keyboard at 1280')
        ctx, pg = await page(1280, base + 'BC-900.html')
        k = await pg.evaluate(STOPS_JS)
        check(k['stops'] <= k['keys'], 'mark tab stops <= distinct keys per section',
              '%d stops, %d keys' % (k['stops'], k['keys']))
        # focus whatever comes just before the first span mark that is a tab stop, then Tab
        ok = await pg.evaluate("""() => {
            const m = document.querySelector('.col span.trial[data-trial][tabindex="0"], .col .gloss[tabindex="0"]');
            if (!m) return false;
            const all = [...document.querySelectorAll('a[href], button, input, [tabindex]')].filter(e =>
              e.tabIndex >= 0 && e.getClientRects().length && !e.closest('[hidden]'));
            const i = all.indexOf(m);
            if (i < 1) return false;
            m.setAttribute('data-probe', '1');
            m.scrollIntoView({block: 'center', behavior: 'instant'});
            all[i - 1].focus({preventScroll: true}); return true; }""")
        if ok:
            await pg.keyboard.press('Tab')
            await pg.wait_for_timeout(200)
            on = await pg.evaluate("() => document.activeElement && document.activeElement.getAttribute('data-probe') === '1'")
            check(on, 'Tab reaches the first mark of a key in its section')
            await pg.keyboard.press('Enter')
            await pg.wait_for_timeout(400)
            opened = await pg.evaluate("() => !!document.querySelector('.refcard.on') && "
                                       "document.querySelector('[data-probe]').getAttribute('aria-expanded') === 'true'")
            check(opened, 'Enter opens its card')
            await pg.keyboard.press('Escape')
            await pg.wait_for_timeout(300)
            closed = await pg.evaluate("() => !document.querySelector('.refcard.on')")
            check(closed, 'Escape closes it')
        else:
            check(False, 'a span mark to Tab to')
        await ctx.close()

        # Enter on a prose mark puts focus on the card's registry link; the card sits at the
        # end of <body>, so Tab and Shift+Tab must close it and keep the reader's place. Every
        # mark on BC-900 and BC-870, at 390 and 1280: after the key, focus is out of the card,
        # visible (its rect intersects the viewport), on the mark or within 1 screen of it,
        # scrollY moved < 1 screen, and Shift+Tab lands on the mark.
        MARKS = '.col [data-trial][tabindex="0"], .col .gloss[tabindex="0"]'
        for ch in ('BC-900', 'BC-870'):
            for w in (390, 1280):
                print('cards: Enter then Tab / Shift+Tab on every mark, %s at %d' % (ch, w))
                ctx, pg = await page(w, base + ch + '.html')
                n = await pg.evaluate("(s) => document.querySelectorAll(s).length", MARKS)
                check(n > 0, '%s %d: marks to test' % (ch, w), '%d' % n)
                bad = collections.defaultdict(list)
                for i in range(n):
                    for key in ('Tab', 'Shift+Tab'):
                        await pg.keyboard.press('Escape')
                        await pg.evaluate("""([s, i]) => {
                            document.querySelectorAll('[data-kprobe]').forEach(e => e.removeAttribute('data-kprobe'));
                            const m = document.querySelectorAll(s)[i];
                            m.setAttribute('data-kprobe', '1');
                            m.scrollIntoView({block: 'center', behavior: 'instant'});
                            m.focus({preventScroll: true}); }""", [MARKS, i])
                        await pg.wait_for_timeout(120)
                        await pg.keyboard.press('Enter')
                        await pg.wait_for_timeout(200)
                        y0 = await pg.evaluate("() => scrollY")
                        incard = await pg.evaluate("() => !!document.activeElement.closest('.refcard')")
                        await pg.keyboard.press(key)
                        await pg.wait_for_timeout(250)
                        r = await pg.evaluate("""(y0) => { const a = document.activeElement, m = document.querySelector('[data-kprobe]');
                            const ra = a.getBoundingClientRect(), rm = m.getBoundingClientRect();
                            return {mark: a === m, tag: a.tagName + (a.className ? '.' + String(a.className).split(' ')[0] : '') +
                                    ' ' + (a.textContent || '').trim().slice(0, 30), mtxt: m.textContent.trim().slice(0, 20),
                                    dist: Math.round(Math.abs(ra.top - rm.top)), dy: Math.round(Math.abs(scrollY - y0)),
                                    vis: ra.bottom > 0 && ra.top < innerHeight, vh: innerHeight,
                                    incard: !!a.closest('.refcard')}; }""", y0)
                        desc = '#%d %s -> %s, %dpx from the mark, scrollY moved %dpx' % (
                            i, r['mtxt'], r['tag'], r['dist'], r['dy'])
                        if not incard:
                            bad['Enter puts focus in the card'].append(desc)
                        if r['incard']:
                            bad['%s leaves the card' % key].append(desc)
                        if not r['vis']:
                            bad['%s: the focused element intersects the viewport' % key].append(desc)
                        if not (r['mark'] or r['dist'] <= r['vh']):
                            bad['%s: focus on the mark or within 1 screen of it' % key].append(desc)
                        if r['dy'] >= r['vh']:
                            bad['%s: scroll moves < 1 screen' % key].append(desc)
                        if key == 'Shift+Tab' and not r['mark']:
                            bad['Shift+Tab: focus returns to the mark'].append(desc)
                await ctx.close()
                names = ['Enter puts focus in the card', 'Tab leaves the card', 'Shift+Tab leaves the card',
                         'Tab: the focused element intersects the viewport',
                         'Shift+Tab: the focused element intersects the viewport',
                         'Tab: focus on the mark or within 1 screen of it',
                         'Shift+Tab: focus on the mark or within 1 screen of it',
                         'Tab: scroll moves < 1 screen', 'Shift+Tab: scroll moves < 1 screen',
                         'Shift+Tab: focus returns to the mark']
                for nm in names:
                    f = bad.get(nm, [])
                    check(not f, '%s %d, %d marks: %s' % (ch, w, n, nm),
                          '%d bad: %s' % (len(f), '; '.join(f[:3])) if f else '')

        print('references: BC-870')
        ctx, pg = await page(390, base + 'BC-870.html')
        d = await pg.evaluate("""() => {
            const h = document.getElementById('references'), n = document.querySelector('.chapnav a.next');
            let e = h.previousElementSibling; while (e && !e.getClientRects().length) e = e.previousElementSibling;
            return {end: e.getBoundingClientRect().bottom + scrollY, next: n.getBoundingClientRect().top + scrollY,
                    vh: innerHeight, twelfth: (document.querySelectorAll('ol.refs li')[11] || {}).id}; }""")
        gap = (d['next'] - d['end']) / d['vh']
        check(gap <= 1.5, '390: the next-chapter card is <= 1.5 screens below the prose', '%.2f screens, was about 10' % gap)
        await ctx.close()
        ctx, pg = await page(390, base + 'BC-870.html#' + d['twelfth'])
        await pg.wait_for_timeout(600)
        r = await pg.evaluate("""(id) => { const li = document.getElementById(id), rc = li.getBoundingClientRect();
            const bg = getComputedStyle(li).backgroundColor;
            return {open: document.querySelector('details.refs-list').open, inview: rc.top >= 0 && rc.top < innerHeight,
                    lit: bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent'}; }""", d['twelfth'])
        check(r['open'] and r['inview'] and r['lit'], '#%s opens the list, lands on the entry and highlights it' % d['twelfth'],
              json.dumps(r))
        await ctx.close()

        print('print: page.pdf() of BC-900')
        ctx, pg = await page(1280, base + 'BC-900.html')
        info = await pg.evaluate("""() => ({heads: [...new Set([...document.querySelectorAll('.evidence th')].map(t => t.textContent.trim()))],
            last: [...document.querySelectorAll('ol.refs li')].pop().textContent.trim()})""")
        pdf = await pg.pdf()
        await ctx.close()
        txt = re.sub(r'\s+', '', pdf_text(pdf))
        last = re.sub(r'\s+', '', info['last'])
        check(last[:80] in txt, 'the PDF holds the last reference', info['last'][:60])
        miss = [h for h in info['heads'] if re.sub(r'\s+', '', h) not in txt]
        check(not miss, 'the PDF holds every evidence-table head', 'missing %s' % miss if miss else ', '.join(info['heads']))
        check('morecolumns' not in txt, 'the PDF has no cue text')
        ctx, pg = await page(1280, base + 'BC-900.html')
        await pg.emulate_media(media='print')
        await pg.wait_for_timeout(200)
        fs = await pg.evaluate("""() => { const sz = s => [...new Set([...document.querySelectorAll(s)].map(e =>
                getComputedStyle(e).fontSize))];
            return {th: sz('.evidence table.trials th'), td: sz('.evidence table.trials td')}; }""")
        await ctx.close()
        check(len(fs['th']) == 1 and fs['th'] == fs['td'] and abs(float(fs['td'][0][:-2]) - 32 / 3) < 0.05,
              'print media: evidence th and td compute to the same size, 8pt', json.dumps(fs))

        print('stories: sizes')
        for w in (390, 1280):
            ctx, pg = await page(w, base + 'BC-900.html')
            z = await pg.evaluate(SIZES_JS)
            await ctx.close()
            check(z['title'] > z['ask'] > z['dd'] >= z['callout'],
                  '%d: .st-title > .sq-ask > story dd >= callout text' % w,
                  '%(title).2f > %(ask).2f > %(dd).2f >= %(callout).2f' % z)

        if build:
            print('Dropbox build: build/breast-cancer (file://)')
            f = os.path.join(BUILD, 'BC-900.html')
            if not os.path.exists(f):
                check(False, 'build/breast-cancer/BC-900.html exists (run make.py)')
            else:
                ctx, pg = await page(1280, 'file://' + f)
                b = await pg.evaluate("() => ({links: document.querySelectorAll('.col a.trial.chip').length, "
                                      "spans: document.querySelectorAll('.col span.trial.chip').length})")
                check(b['links'] == 0 and b['spans'] > 0, 'chips stay spans', json.dumps(b))
                await pg.hover('.col p .trial[data-trial], .col td .trial[data-trial]')
                await pg.wait_for_timeout(500)
                c = await pg.evaluate("() => { const c = document.querySelector('.refcard.on'); "
                                      "return {card: !!c, link: !!(c && c.querySelector('a.rc-go'))}; }")
                check(c['card'] and not c['link'], 'the trial card has no registry link', json.dumps(c))
                await ctx.close()
        await br.close()


def main():
    args = sys.argv[1:]
    markup()
    if '--static' not in args:
        httpd, base = serve()
        try:
            asyncio.run(browser(base, '--nobuild' not in args))
        finally:
            httpd.shutdown()
    if FAILS:
        print('clinic: FAIL, %d check(s): %s' % (len(FAILS), '; '.join(FAILS)))
        return 1
    print('clinic: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
