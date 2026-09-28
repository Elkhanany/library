#!/usr/bin/env python3
"""
navcheck.py -- drive the built site and prove the chapter navigation works.

    python3 tools/navcheck.py

The navigation the two chaptered books share is built at read time out of
docs/<slug>/nav.json, so nothing about it is visible in the built HTML and
sitecheck.py cannot see it at all. This opens the pages in the Chromium that
verify.py already uses and checks the behaviour instead: that the drawer
carries the right neighbours, that the arrow keys move a chapter, that the
first chapter keeps the shape of the control, that a standalone launch gets a
back button, and that the two books with no reading order are untouched.

It also checks the thing sitecheck can only half see. nav.py --check proves
every page carries the bar its book.json describes, which is a claim about
bytes. The claims here are about surfaces: that the drawer on a phone offers
the same destinations as the bar above it, that the page you are on is marked
rather than linked on both, that a landing page has a back control in a
home-screen app -- the atlas had no bar at all and so had none -- and that a
book whose whole interface fills the window still fits in it with the bar
there.

TWO THINGS IT HAS TO REPRODUCE, OR IT TESTS NOTHING

pwa.js returns immediately on file://, so docs/ is served over http. And it
reads the book slug out of the path, expecting the project prefix that GitHub
Pages puts there, so docs/ is served under /library/ rather than at the root.
Serving it at the root makes every book page look like the hub, which switches
the whole app layer off silently: the first version of this file did exactly
that and reported seven failures that were all its own.

A MISSING ELEMENT IS A FAILURE, NOT A CRASH

Every wait goes through waitfn()/waitsel(), which record a FAIL naming the page
and what was waited for and let the run carry on; every block of tests runs
inside a section() that turns an unexpected exception into one FAIL for that
block. A redesign that renames one selector therefore reports every test it
breaks, not the first one followed by a traceback.

WHERE THE READER IS, AND THE PHONE'S CHROME

Below 1000px the sidebar's jobs move to the folio bar and the drawer
(DESIGN.md section 6), and both are built by book.js from the page itself: the
folio's arrows carry the neighbours' numbers and go where the chapter foot
goes, the foot ends above the folio, the drawer's first row is the way up to
the chapter's part in the contents (checked against the contents page's own
part ids), and headroom takes the bar and the folio away on reading down and
brings them back on a deliberate scroll up but not on a 20px nudge. On a
desktop the sidebar's active entry is checked after a jump and after scrolling
up, the two cases the old observer got wrong. On the clinical contents page,
"Find a chapter" filters to the rows that match and Escape restores every row.

THE MATHEMATICS (DESIGN.md section 6, Equations and figures; Callouts,
preambles and sitting breaks)

Every sitting break in the physics book has its kicker (.k, at most 40
characters) and a non-empty line (.t), which on ch4-6 and ch4-7 wraps inside
the column with its first letter capitalised. Inline maths is 1.045 times the
text on a phone. Every display on ch3-5 at 390 fits its box or carries its
edge shades, and at 1280 none of the widest displays in the book overflows
its box. No equation number overlaps its display at 390, 1000 or 1280; at
1280 every number sits right of the column, and (1.2.11) keeps its line at
390. With a 20px default text size, on ch1-2 at 1200 and 1280 (where the
margin track is too narrow to hang a number) and at 1400 (where it hangs),
every number stays inside .main's content box and over no display, with no
page overflow. Hovering the first equation reference on ch1-2 at 1280 shows a
card holding the equation and its number, whose "Go to equation" jumps there; a
tap at 390 on a touch screen shows the sheet instead.

THE CLINICAL APPARATUS (folded in from the W3-CLINIC probe)

No id is used twice on any chapter page of either book, or on the ledger,
the Through-Line, the registry or the stories page. A tap on BC-900's first
trial mark at 390 opens the sheet with the trial's facts and a link to its
registry row, and following it opens that row. BC-870 opened at its twelfth
reference opens the list and lands on the entry, highlighted.

TWO CHECKS THE RESTYLE DEPENDS ON

- Equation numbers. The build numbers every .eq and runtime_js() switches the
  runtime numbering off (DESIGN.md section 8, the boot shape). If that contract
  breaks, every equation carries two numbers; ch1-1 is checked for exactly one.
- The masked-overflow sweep. overflow clipping on html, body, .wrap, .main and
  .col hides anything that pokes past the viewport, so "nothing scrolls
  sideways" can pass over text nobody can see. The sweep lifts that mask and
  fails on any element whose right edge passes the viewport by more than 1px,
  except the ones listed in KNOWN, each tagged with the package that removes
  it. A KNOWN entry that no longer reproduces also fails, so the list can only
  shrink: delete the entry when its package lands.
"""
import asyncio, http.server, os, socketserver, sys, threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

# One page of each kind per book: the front door, the contents page, a chapter,
# and anything the book declared for itself. These are the four ways a page got
# into docs/, and before this they were four different bars.
BAR_PAGES = {
    'newton-to-mtheory':   ['index.html', 'contents.html', 'ch2-1.html',
                            'ledger.html', 'throughline.html'],
    # no contents page: a book with nothing written builds none (NAV-04)
    'the-long-argument':   ['index.html'],
    'the-ages-of-thought': ['index.html'],
    'breast-cancer':       ['index.html', 'contents.html', 'BC-500.html',
                            'stories.html', 'trials.html'],
    # 9A carries the most figures, one of them placed twice
    'the-other-end-of-the-trade': ['index.html', 'contents.html', '9a.html'],
}

# The masked-overflow sweep: the hub, the four front doors, both contents pages,
# the clinical chapter with the most evidence tables and one without, the two
# appendices, the physics chapters with the widest sitting-break labels, the
# ledger and the through-line, and the atlas and the timeline each with their
# reading surface open (a dossier, a study). (label, path, action) -- the action
# is a script run after load that opens that surface, or None.
OPEN_STUDY = ("() => { if (typeof openStudy !== 'function' || typeof MONO === 'undefined')"
              " return false; const ids = Object.keys(MONO);"
              " openStudy(ids.includes('spinoza') ? 'spinoza' : ids[0]); return true; }")
SWEEP_PAGES = [
    ('index.html', 'index.html', None),
    ('newton-to-mtheory/index.html', 'newton-to-mtheory/index.html', None),
    ('breast-cancer/index.html', 'breast-cancer/index.html', None),
    ('the-long-argument/index.html', 'the-long-argument/index.html', None),
    ('the-ages-of-thought/index.html', 'the-ages-of-thought/index.html', None),
    ('newton-to-mtheory/contents.html', 'newton-to-mtheory/contents.html', None),
    ('breast-cancer/contents.html', 'breast-cancer/contents.html', None),
    ('breast-cancer/BC-900.html', 'breast-cancer/BC-900.html', None),
    ('breast-cancer/BC-500.html', 'breast-cancer/BC-500.html', None),
    ('breast-cancer/trials.html', 'breast-cancer/trials.html', None),
    ('breast-cancer/stories.html', 'breast-cancer/stories.html', None),
    ('newton-to-mtheory/ch1-2.html', 'newton-to-mtheory/ch1-2.html', None),
    ('newton-to-mtheory/ch4-6.html', 'newton-to-mtheory/ch4-6.html', None),
    ('newton-to-mtheory/ch4-7.html', 'newton-to-mtheory/ch4-7.html', None),
    ('newton-to-mtheory/ledger.html', 'newton-to-mtheory/ledger.html', None),
    ('newton-to-mtheory/throughline.html', 'newton-to-mtheory/throughline.html', None),
    # the trading book: its front door, its contents, the chapter with the widest
    # table (eight columns), and the one with the most figures
    ('the-other-end-of-the-trade/index.html', 'the-other-end-of-the-trade/index.html', None),
    ('the-other-end-of-the-trade/contents.html', 'the-other-end-of-the-trade/contents.html', None),
    ('the-other-end-of-the-trade/3a.html', 'the-other-end-of-the-trade/3a.html', None),
    ('the-other-end-of-the-trade/9a.html', 'the-other-end-of-the-trade/9a.html', None),
    ('the atlas, a dossier open', 'the-ages-of-thought/index.html#who=spinoza', None),
    ('the timeline, a study open', 'the-long-argument/index.html', OPEN_STUDY),
]
SWEEP_WIDTHS = (390, 1280)

# Today's offenders, measured on the tree wave 0 started from, each with the
# package that removes it. (sweep label, width) -> {offender: package}. An
# offender is "parent>element", tag#id.class with at most two classes, as
# SWEEP_JS describes it. New offenders fail; so does an entry here that no
# longer reproduces. The list only shrinks.
KNOWN = {
    # (the evidence tables' 2px bleed past a 390px phone, PDA-09, went when
    # W2-FRAME put .main's phone padding on --gutter, which the bleed uses;
    # the sitting-break labels, nowrap and up to 2049px wide, went when W4-MATH
    # split them into a kicker and a wrapping line)
}

# The sweep itself. The shell is forced to overflow:visible, so a clip on the
# shell cannot hide anything. An element inside its own scroller (overflow-x
# auto or scroll), inside a component that clips on purpose (hidden or clip
# below the shell), inside position:fixed chrome, or not visible, is not an
# offender; nor is KaTeX's hidden MathML copy. Only the topmost offender of a
# subtree is reported. A copy lives in scratchpad/ui/architect/sweep.js.
SWEEP_JS = r"""() => {
  const vw = document.documentElement.clientWidth || innerWidth;
  const st = document.createElement('style');
  st.textContent = 'html,body,.wrap,.main,.col{overflow:visible!important}';
  document.head.appendChild(st);
  const natural = document.documentElement.scrollWidth;
  const SHELL = new Set([document.documentElement, document.body,
                         ...document.querySelectorAll('.wrap,.main,.col')]);
  const one = e => { let s = e.tagName.toLowerCase(); if (e.id) s += '#' + e.id;
    const c = typeof e.className === 'string' ? e.className.trim() : '';
    if (c) s += '.' + c.split(/\s+/).slice(0, 2).join('.'); return s; };
  const desc = el => (el.parentElement ? one(el.parentElement) + '>' : '') + one(el);
  const offend = new Set(), out = [];
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect();
    if (r.width === 0 || r.right <= vw + 1) continue;
    const cs = getComputedStyle(e);
    if (cs.position === 'fixed' || cs.visibility !== 'visible' || cs.display === 'none') continue;
    if (e.closest('.katex-mathml')) continue;
    let skip = false;
    for (let a = e.parentElement; a; a = a.parentElement) {
      const acs = getComputedStyle(a);
      if (acs.position === 'fixed') { skip = true; break; }
      const ox = acs.overflowX;
      if (ox === 'auto' || ox === 'scroll') { skip = true; break; }
      if ((ox === 'hidden' || ox === 'clip') && !SHELL.has(a)) { skip = true; break; }
    }
    if (skip) continue;
    offend.add(e);
    if (e.parentElement && offend.has(e.parentElement)) continue;
    out.push({sel: desc(e), right: Math.round(r.right),
              text: (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50)});
  }
  st.remove();
  return {vw: vw, natural: natural, offenders: out};
}"""

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
PORT = int(os.environ.get("NAVCHECK_PORT", "8931"))
TIMEOUT = 10000         # ms; no single step may hang the run for Playwright's 30s
fails = []


class Handler(http.server.SimpleHTTPRequestHandler):
    """docs/ under a /library/ prefix, which is where GitHub Pages puts it."""

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DOCS, **kw)

    def translate_path(self, path):
        if path.startswith('/library/'):
            path = path[len('/library'):]
        elif path == '/library':
            path = '/'
        return super().translate_path(path)

    def log_message(self, *a):
        pass


def serve():
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(('127.0.0.1', PORT), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def json_of(path):
    import json
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def ok(name, cond, detail=''):
    print(('  PASS  ' if cond else '  FAIL  ') + name + (('  ' + str(detail)) if detail else ''))
    if not cond:
        fails.append(name)


def _why(e):
    s = str(e).strip().splitlines()
    return (type(e).__name__ + ': ' + (s[0] if s else ''))[:160]


def _short(js):
    js = ' '.join(js.split())
    return js if len(js) <= 90 else js[:87] + '...'


def where(pg):
    """The page, as a reader would name it: the path under /library/."""
    try:
        return pg.url.split('/library/', 1)[-1] or 'index.html'
    except Exception:
        return '?'


async def waitfn(pg, js, timeout=5000, what=None):
    """wait_for_function that never aborts the run: on timeout it records a FAIL
    naming the page and what it waited for, and returns False."""
    try:
        await pg.wait_for_function(js, timeout=timeout)
        return True
    except Exception as e:
        ok('%s: waited for %s' % (where(pg), what or _short(js)), False, _why(e))
        return False


async def waitsel(pg, sel, timeout=5000, state='attached'):
    """wait_for_selector that never aborts the run: a FAIL with page and selector."""
    try:
        await pg.wait_for_selector(sel, timeout=timeout, state=state)
        return True
    except Exception as e:
        ok('%s: waited for %s' % (where(pg), sel), False, _why(e))
        return False


async def text(pg, sel):
    """The element's text, or a FAIL naming page and selector and ''."""
    el = await pg.query_selector(sel)
    if el is None:
        ok('%s: found %s' % (where(pg), sel), False, 'no such element')
        return ''
    return (await el.text_content()) or ''


async def click(pg, sel):
    """Click, or a FAIL naming page and selector. Returns whether it clicked."""
    try:
        await pg.click(sel, timeout=5000)
        return True
    except Exception as e:
        ok('%s: clicked %s' % (where(pg), sel), False, _why(e))
        return False


class section:
    """One block of tests. An exception inside it becomes one FAIL for the block,
    and the run moves on to the next block."""

    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        return self

    async def __aexit__(self, et, ev, tb):
        if et is None:
            return False
        ok('%s ran to the end' % self.name, False, _why(ev))
        return True


async def page(br, width=1400, height=900):
    pg = await br.new_page(viewport={'width': width, 'height': height})
    pg.set_default_timeout(TIMEOUT)
    return pg


async def opened(br, url, width=1400, height=900):
    """A page, once it has stopped moving.

    Every Playwright context starts with an empty cache, so the service worker
    installs, takes control, and pwa.js reloads once to hand the page over to
    it. That reload destroys the execution context underneath any evaluate()
    that started before it, and the error reads like a broken page rather than
    a page that was still arriving. Waiting for the controller is waiting for
    the exact thing that causes it."""
    pg = await page(br, width, height)
    # Whether this document was controlled from its start. One that was not
    # is the one pwa.js reloads when the worker takes control, and a
    # controller alone does not say which document is running: the old one
    # has it too for the moment before its reload begins. So the wait is for
    # a document that started under control, loaded.
    await pg.add_init_script(
        "window.__ncControlled = !('serviceWorker' in navigator)"
        " || !!navigator.serviceWorker.controller;")
    await pg.goto(url, wait_until='networkidle')
    for _ in range(3):
        try:
            await pg.wait_for_function(
                "() => window.__ncControlled === true && document.readyState === 'complete'",
                timeout=6000)
            break
        except Exception:
            # not a failure: the page may simply still be arriving
            try:
                await pg.wait_for_load_state('networkidle')
            except Exception:
                pass
    await pg.wait_for_timeout(200)
    return pg


READY = "() => window.LibraryPWA && window.LibraryPWA.nav().index >= 0"

# The folio bar below 1000px (DESIGN.md section 6): where it is, what its
# arrows say and where they go, and where the chapter foot ends.
FOLIO = """() => {
  const f = document.querySelector('.folio');
  if (!f) return null;
  const r = f.getBoundingClientRect();
  const p = f.querySelector('.folio-prev'), n = f.querySelector('.folio-next');
  const nav = document.querySelector('.chapnav');
  return {top: Math.round(r.top), shown: r.top < innerHeight - 10 && r.height > 0,
          prev: p ? p.textContent.trim() : '', next: n ? n.textContent.trim() : '',
          nextHref: n ? n.getAttribute('href') : null,
          chapnavBottom: nav ? Math.round(nav.getBoundingClientRect().bottom) : null};
}"""
TO_END = ("() => window.scrollTo({top: document.documentElement.scrollHeight - innerHeight,"
          " behavior: 'instant'})")
# Where the bar and the folio are: headroom moves them by transform.
CHROME = """() => {
  const b = document.querySelector('.topnav').getBoundingClientRect();
  const f = document.querySelector('.folio').getBoundingClientRect();
  return {barOut: b.bottom <= 0.5, folioOut: f.top >= innerHeight - 0.5,
          barIn: b.top >= -0.5, folioIn: f.bottom <= innerHeight + 0.5, y: Math.round(scrollY)};
}"""


async def chaptered(br, base, slug, chap):
    # The neighbours and the count come from the book's own reading
    # order rather than from constants here. Hard-coding them made this
    # file report four failures the first time the clinical book was
    # reorganised, when the navigation was working perfectly and only
    # the fixtures were stale.
    pg = await page(br)
    order = (await (await pg.goto(base + slug + '/nav.json')).json())
    await pg.close()
    ids = [c['href'] for c in order['chapters']]
    at = ids.index(chap)
    prev_num = order['chapters'][at - 1]['num']
    next_num = order['chapters'][at + 1]['num']
    total = order['count']
    print('\n%s  %s  (%d of %d)' % (slug, chap, at + 1, total))

    # ---- phone width: the drawer is the surface
    async with section('%s: the drawer at 390' % slug):
        pg = await opened(br, base + slug + '/' + chap, 390, 780)
        await waitfn(pg, READY, what='the reading order (LibraryPWA.nav().index >= 0)')
        await pg.wait_for_timeout(120)

        seq = await pg.query_selector('#mnav .mn-seq')
        ok('drawer carries a prev/next row', seq is not None)
        if seq:
            prev = await text(pg, '#mnav .mn-seq .prev .mn-ch')
            nxt = await text(pg, '#mnav .mn-seq .next .mn-ch')
            ok('prev is the previous chapter', prev.startswith(prev_num), repr(prev[:44]))
            ok('next is the next chapter', nxt.startswith(next_num), repr(nxt[:44]))
            kick = await text(pg, '#mnav .mn-kicker')
            ok('kicker shows the position', ' of %d' % total in kick, repr(kick))
            sb = await text(pg, '.sidebar .sb-title')
            ok('the sidebar says the same', ' of %d' % total in sb, repr(sb))
            # written once, at build: pwa.js no longer appends a second copy
            ok('the position appears exactly once', sb.count(' of ') == 1 and kick == sb.strip(),
               repr(sb))
            # the row must be reachable without scrolling the chapter
            if await click(pg, '#mnav-btn'):
                await pg.wait_for_timeout(250)
                vis = await pg.is_visible('#mnav .mn-seq .next')
                ok('next is visible once the drawer opens', vis)
                href = await pg.get_attribute('#mnav .mn-seq .next', 'href')
                if await click(pg, '#mnav .mn-seq .next'):
                    await pg.wait_for_load_state('load')
                    ok('tapping next goes there', bool(href) and pg.url.endswith(href),
                       pg.url.split('/')[-1])
        await pg.close()

    # ---- desktop: the keyboard is the surface
    async with section('%s: the arrow keys' % slug):
        pg = await page(br, 1400, 900)
        await pg.goto(base + slug + '/' + chap, wait_until='networkidle')
        await pg.wait_for_timeout(300)

        async def press(key):
            # the arrow keys are live only once the reading order has
            # arrived; wait for that rather than for a fixed delay
            await waitfn(pg, READY, what='the reading order (LibraryPWA.nav().index >= 0)')
            try:
                async with pg.expect_navigation(timeout=4000):
                    await pg.keyboard.press(key)
            except Exception:
                pass
            return pg.url.split('/')[-1]
        got = await press('ArrowRight')
        ok('ArrowRight is the next chapter', got != chap, got)
        got = await press('ArrowLeft')
        ok('ArrowLeft comes back', got == chap, got)
        await pg.close()

    # ---- the first and last chapters keep the shape
    async with section('%s: the first chapter' % slug):
        first = ids[0]
        pg = await page(br, 390, 780)
        await pg.goto(base + slug + '/' + first, wait_until='networkidle')
        await pg.wait_for_timeout(300)
        kind = await pg.eval_on_selector_all(
            '#mnav .mn-seq > *', 'els => els.map(e => e.tagName)')
        ok('first chapter has a disabled prev, not a missing one',
           kind == ['SPAN', 'A'], kind)
        await pg.close()


async def sweep(br, base):
    """The masked-overflow sweep (PDA-09). See KNOWN and SWEEP_JS."""
    print('\nnothing passes the viewport with the shell unmasked')
    seen = set()
    for w in SWEEP_WIDTHS:
        ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                   service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        for label, path, action in SWEEP_PAGES:
            async with section('sweep %s at %d' % (label, w)):
                pg = await ctx.new_page()
                try:
                    await pg.goto(base + path, wait_until='load', timeout=45000)
                    await pg.evaluate('() => document.fonts.ready.then(() => true)')
                    await pg.wait_for_timeout(500)
                    if action:
                        did = await pg.evaluate(action)
                        if not did:
                            print('  NOTE  %s: the surface could not be opened; swept the '
                                  'page as it loads' % label)
                        await pg.wait_for_timeout(800)
                    r = await pg.evaluate(SWEEP_JS)
                finally:
                    await pg.close()
                known = KNOWN.get((label, w), {})
                got = {}
                for o in r['offenders']:
                    got.setdefault(o['sel'], []).append(o)
                new = {s: v for s, v in got.items() if s not in known}
                for s in got:
                    if s in known:
                        seen.add((label, w, s))
                ok('%s at %d: nothing new passes the viewport' % (label, w), not new,
                   '; '.join('%s x%d to %dpx %r' % (s, len(v), max(o['right'] for o in v),
                                                    v[0]['text'][:30])
                             for s, v in new.items())
                   or ('known: ' + ', '.join('%s x%d [%s]' % (s, len(got[s]), known[s])
                                             for s in got if s in known) if got else ''))
        await ctx.close()
    # the list only shrinks: an entry that no longer reproduces must be deleted
    for (label, w), entries in sorted(KNOWN.items()):
        for s, pkg in sorted(entries.items()):
            ok('KNOWN %s at %d %s [%s] still reproduces' % (label, w, s, pkg),
               (label, w, s) in seen,
               '' if (label, w, s) in seen else
               'fixed: delete this entry from KNOWN in tools/navcheck.py')


LASTBY = "(slug) => ((JSON.parse(localStorage.getItem('library:v1') || '{}') || {}).lastBy || {})[slug] || null"


async def returning_reader(br, base):
    phys = json_of(os.path.join(DOCS, 'newton-to-mtheory', 'nav.json'))
    clin = json_of(os.path.join(DOCS, 'breast-cancer', 'nav.json'))
    c11 = next(c for c in phys['chapters'] if c['href'] == 'ch1-1.html')
    c500 = next(c for c in clin['chapters'] if c['href'] == 'BC-500.html')
    ok('nav.json carries how each book is read',
       (phys.get('reading'), clin.get('reading')) == ('sequential', 'reference'),
       (phys.get('reading'), clin.get('reading')))
    ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block')
    ctx.set_default_timeout(TIMEOUT)
    pg = await ctx.new_page()
    try:
        await pg.goto(base + 'newton-to-mtheory/ch1-1.html', wait_until='load')
        if await waitfn(pg, READY, what='the reading order on ch1-1'):
            await pg.evaluate("() => window.scrollTo({top: (document.documentElement.scrollHeight"
                              " - innerHeight) * .4, behavior: 'instant'})")
            await pg.wait_for_timeout(1000)
        got = await pg.evaluate(LASTBY, 'newton-to-mtheory')
        ok('reading ch1-1 to 40%% records lastBy with its number and title (%s)' % c11['num'],
           bool(got) and got['url'].endswith('/newton-to-mtheory/ch1-1.html')
           and got['num'] == c11['num'] and got['title'] == c11['title']
           and 30 <= got['pct'] <= 50 and got['at'] > 0, got)

        await pg.goto(base + 'breast-cancer/BC-500.html', wait_until='load')
        await waitfn(pg, READY, what='the reading order on BC-500')
        await pg.wait_for_timeout(300)
        got = await pg.evaluate(LASTBY, 'breast-cancer')
        ok('opening BC-500 records it (%s)' % c500['num'],
           bool(got) and got['url'].endswith('/breast-cancer/BC-500.html')
           and got['num'] == c500['num'], got)

        # a front door and a contents page are not a place in the book
        for where_ in ('breast-cancer/index.html', 'breast-cancer/contents.html'):
            await pg.goto(base + where_, wait_until='load')
            await waitfn(pg, "() => window.LibraryPWA && window.LibraryPWA.nav().ready",
                         what='the reading order on ' + where_)
            await pg.evaluate("() => window.scrollTo({top: 600, behavior: 'instant'})")
            await pg.wait_for_timeout(900)
            got = await pg.evaluate(LASTBY, 'breast-cancer')
            ok('%s records nothing: lastBy is still BC-500' % where_,
               bool(got) and got['url'].endswith('/BC-500.html'), got and got['url'])

        # the clinical front door keeps Contents and offers the place beside it
        await pg.goto(base + 'breast-cancer/index.html', wait_until='load')
        if await waitfn(pg, "() => { const g = document.querySelector('.cta > .go');"
                            " return !!g && g.textContent.trim().startsWith('Continue at'); }",
                        what='a first .go "Continue at ..." on the clinical front door'):
            await pg.wait_for_timeout(300)
            r = await pg.evaluate("""() => { const b = document.querySelector('.cta > .btn');
              const g = document.querySelector('.cta > .go');
              return {main: b.querySelector('.btn-main') ? b.querySelector('.btn-main').textContent.trim() : b.textContent.trim(),
                      go: g.textContent.trim(), href: g.getAttribute('href'),
                      gos: document.querySelectorAll('.cta > .btn').length}; }""")
            want = 'Continue at %s \u00b7 %s' % (c500['num'], c500['title'])
            ok('the reference front door keeps Contents as its primary', r['main'] == 'Contents'
               and r['gos'] == 1, r)
            ok('and its first text link is "%s"' % want[:40], r['go'] == want
               and r['href'].endswith('/BC-500.html'), r)

        # the physics front door: Continue reading, with Begin kept
        await pg.goto(base + 'newton-to-mtheory/index.html', wait_until='load')
        if await waitsel(pg, '.cta > .btn[data-resumed]'):
            r = await pg.evaluate("""() => { const b = document.querySelector('.cta > .btn');
              const g = document.querySelector('.cta > .go');
              return {main: b.querySelector('.btn-main').textContent.trim(),
                      sub: b.querySelector('.btn-sub').textContent.trim(),
                      href: b.getAttribute('href'), aria: b.getAttribute('aria-label'),
                      go: g.textContent.trim(), goHref: g.getAttribute('href')}; }""")
            sub = '%s \u00b7 %s' % (c11['num'], c11['title'])
            ok('the sequential front door\'s primary reads Continue reading over %s' % c11['num'],
               r['main'] == 'Continue reading' and r['sub'] == sub
               and r['href'].endswith('/ch1-1.html') and sub in (r['aria'] or ''), r)
            first = phys['chapters'][0]['href']
            ok('and Begin is its first text link, to %s' % first,
               r['go'] == 'Begin' and r['goHref'] == first, r)

        # the physics contents marks the row and offers the way back
        await pg.goto(base + 'newton-to-mtheory/contents.html', wait_until='load')
        if await waitsel(pg, '.clist li[data-last]'):
            r = await pg.evaluate("""() => { const li = [...document.querySelectorAll('.clist li[data-last]')];
              const j = document.querySelector('.pwa-jump a');
              const part = document.querySelector('h2.part-head');
              return {n: li.length, href: li[0].querySelector('a').getAttribute('href'),
                      tag: (li[0].querySelector('.tag.last') || {}).textContent || null,
                      jump: j ? j.textContent.trim() : null, jumpHref: j ? j.getAttribute('href') : null,
                      above: !!j && !!part && !!(j.compareDocumentPosition(part) & Node.DOCUMENT_POSITION_FOLLOWING)}; }""")
            ok('the physics contents marks %s "Last read", once' % c11['num'],
               r['n'] == 1 and r['href'] == 'ch1-1.html' and r['tag'] == 'Last read', r)
            ok('with "Jump to where you were" above the first part',
               r['jump'] == 'Jump to where you were' and r['above']
               and (r['jumpHref'] or '').endswith('/ch1-1.html'), r)

        # continue.html?b= lands on the book's place, not the library's last page
        await pg.goto(base + 'continue.html?b=newton-to-mtheory', wait_until='load')
        try:
            await pg.wait_for_url('**/newton-to-mtheory/ch1-1.html', timeout=5000)
        except Exception:
            pass
        ok('continue.html?b=newton-to-mtheory lands on ch1-1', pg.url.endswith('/ch1-1.html'),
           pg.url.split('/library/')[-1])
        await pg.goto(base + 'continue.html', wait_until='load')
        try:
            await pg.wait_for_url('**/breast-cancer/BC-500.html', timeout=5000)
        except Exception:
            pass
        ok('continue.html lands on the most recent place, BC-500', pg.url.endswith('/BC-500.html'),
           pg.url.split('/library/')[-1])

        # the hub's strip, most recent first, one tap to the chapter
        await pg.goto(base + 'index.html', wait_until='load')
        if await waitsel(pg, 'section[data-continue]:not([hidden]) li', state='visible'):
            r = await pg.evaluate("""() => [...document.querySelectorAll('section[data-continue] li a')]
              .map(a => [a.dataset.book, a.getAttribute('href'),
                         a.querySelector('.c-ch').textContent.trim()])""")
            ok('the hub\'s Continue strip lists BC-500, then ch1-1',
               [x[0] for x in r] == ['breast-cancer', 'newton-to-mtheory']
               and r[0][1].endswith('/BC-500.html') and r[1][1].endswith('/ch1-1.html')
               and r[0][2].startswith(c500['num'] + ' \u00b7 '), r)
            await pg.click('section[data-continue] li a')
            await pg.wait_for_load_state('load')
            ok('one tap on its first row opens BC-500', pg.url.endswith('/breast-cancer/BC-500.html'),
               pg.url.split('/library/')[-1])
    finally:
        await ctx.close()


async def hub_tiles(br, base):
    """Four tiles, each a status line in its own unit and an offline chip; no
    second list of the same books; and Tab onto each tile brings its weather
    (body[data-focus]) and its ring in the tile's accent (C2-tile-focus)."""
    ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block')
    ctx.set_default_timeout(TIMEOUT)
    pg = await ctx.new_page()
    try:
        await pg.goto(base + 'index.html', wait_until='load')
        n = len(library.books())
        await waitfn(pg, "() => [...document.querySelectorAll('.book button[data-offline]')]"
                         ".every(b => !b.hidden && b.textContent.trim())",
                     timeout=8000, what='every tile\'s offline chip')
        r = await pg.evaluate("""() => ({
          tiles: [...document.querySelectorAll('article.book')].map(t => ({
            slug: t.dataset.slug,
            count: (t.querySelector('.count') || {}).textContent || '',
            chip: (t.querySelector('button[data-offline]') || {}).textContent || ''})),
          lists: document.querySelectorAll('.pwa-shelf, .pwa-row').length,
          store: !!document.querySelector('p[data-store]:not([hidden]) button')})""")
        bad = [t for t in r['tiles'] if not t['count'].strip() or not t['chip'].strip()
               or 'planned' in t['count'] or t['count'].startswith('0 ')]
        ok('%d tiles, each with a status line in its own unit and an offline chip' % n,
           len(r['tiles']) == n and not bad, bad or [t['count'] for t in r['tiles']])
        ok('no separate "Read offline" list; one storage line with Reset',
           r['lists'] == 0 and r['store'], r)

        seen = {}
        await pg.evaluate("() => document.activeElement && document.activeElement.blur()")
        for _ in range(40):
            await pg.keyboard.press('Tab')
            s = await pg.evaluate("""() => {
              const a = document.activeElement, t = a && a.closest && a.closest('article.book');
              if (!t || a.tagName !== 'A') return null;
              const cs = getComputedStyle(t);
              const probe = document.createElement('i');
              probe.style.color = 'var(--bk-hue)'; t.appendChild(probe);
              const hue = getComputedStyle(probe).color; probe.remove();
              return {slug: t.dataset.slug, focus: document.body.getAttribute('data-focus'),
                      style: cs.outlineStyle, width: parseFloat(cs.outlineWidth),
                      color: cs.outlineColor, hue: hue}; }""")
            if s and s['slug'] not in seen:
                seen[s['slug']] = s
            if len(seen) == n:
                break
        for bk in library.books():
            s = seen.get(bk.slug)
            ok('Tab onto the %s tile sets body[data-focus] and draws its accent ring' % bk.slug,
               bool(s) and s['focus'] == bk.slug and s['style'] == 'solid' and s['width'] >= 2
               and s['color'] == s['hue'], s)
    finally:
        await ctx.close()


# ------------------------------------------------------------ the mathematics
# What the physics pages' maths and sitting breaks look like to a reader, after
# book.js has fitted the displays (on load and when the fonts arrive).
MATH_EXTENT = """(d) => { let L = Infinity, R = -Infinity;
    d.querySelectorAll('.katex-html > .base').forEach(b => { const r = b.getBoundingClientRect();
      if (r.width) { L = Math.min(L, r.left); R = Math.max(R, r.right); } });
    return R > L ? {L: L, R: R} : null; }"""

PAUSES = """() => [...document.querySelectorAll('.main .pause')].map(p => {
    const k = p.querySelectorAll('.k'), t = p.querySelectorAll('.t');
    const col = document.querySelector('.main .col').getBoundingClientRect();
    const tr = t.length ? t[0].getBoundingClientRect() : null;
    const cs = t.length ? getComputedStyle(t[0]) : null;
    return {k: k.length === 1 ? k[0].textContent.trim() : null, nk: k.length, nt: t.length,
            t: t.length ? t[0].textContent.trim().slice(0, 40) : '',
            inside: !!tr && tr.width > 0 && tr.left >= col.left - 0.5 && tr.right <= col.right + 0.5,
            wraps: !!cs && cs.whiteSpace !== 'nowrap' && t[0].scrollWidth <= t[0].clientWidth + 1,
            cap: !!t.length && getComputedStyle(t[0], '::first-letter').textTransform === 'uppercase'};
  })"""

DISPLAYS = """() => { const ext = """ + MATH_EXTENT + """;
    const out = {n: 0, bad: []};
    document.querySelectorAll('.main .katex-display').forEach((d, i) => {
      if (!d.getClientRects().length) return;
      out.n++;
      const x = ext(d), b = d.getBoundingClientRect();
      const over = d.scrollWidth > d.clientWidth + 1 || (x && (x.R > b.right + 1 || x.L < b.left - 1));
      if (over) out.bad.push({i: i, cue: d.classList.contains('scrolls'),
                              w: x ? Math.round(x.R - x.L) : 0, box: Math.round(b.width)});
    });
    return out; }"""

NUMBERS = """() => { const ext = """ + MATH_EXTENT + """;
    const col = document.querySelector('.main .col').getBoundingClientRect();
    return [...document.querySelectorAll('.main .eq')].map(e => {
      const n = [...e.children].find(c => c.classList.contains('eqnum'));
      const d = e.querySelector('.katex-display');
      if (!n || !d) return null;
      const nr = n.getBoundingClientRect(), b = d.getBoundingClientRect(), x = ext(d);
      if (!nr.width || !x) return null;
      const L = Math.max(x.L, b.left), R = Math.min(x.R, b.right);
      return {num: n.textContent.trim(), drop: e.classList.contains('eq-drop'),
              hit: nr.left < R && nr.right > L && nr.top < b.bottom && nr.bottom > b.top,
              right: nr.left >= col.right - 0.5};
    }).filter(Boolean); }"""


LARGE_TEXT = """() => { const main = document.querySelector('.main'), cs = getComputedStyle(main);
    const R = main.getBoundingClientRect().right - parseFloat(cs.paddingRight);
    const col = document.querySelector('.main .col').getBoundingClientRect();
    const ns = [...document.querySelectorAll('.main .eq > .eqnum')].map(n => n.getBoundingClientRect())
      .filter(r => r.width);
    return {root: getComputedStyle(document.documentElement).fontSize,
            breakout: cs.getPropertyValue('--breakout').trim(),
            past: ns.length ? Math.round(Math.max(...ns.map(r => r.right - R)) * 10) / 10 : 0,
            hung: ns.filter(r => r.left >= col.right - 0.5).length,
            pageOver: document.documentElement.scrollWidth - innerWidth}; }"""

async def fitted_page(ctx, url):
    """A page whose displays book.js has fitted: after load, the fonts and a
    beat for the refit they start."""
    pg = await ctx.new_page()
    await pg.goto(url, wait_until='load', timeout=45000)
    await pg.evaluate('() => document.fonts.ready.then(() => true)')
    await pg.wait_for_timeout(600)
    return pg


async def mathematics(br, base):
    phys = base + 'newton-to-mtheory/'
    import glob as _glob
    with_breaks = sorted(os.path.basename(f) for f in
                         _glob.glob(os.path.join(DOCS, 'newton-to-mtheory', 'ch*.html'))
                         if 'class="pause"' in open(f, encoding='utf-8').read())

    print('\nthe mathematics: sitting breaks')
    async with section('sitting breaks'):
        ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        bad, n = [], 0
        for ch in with_breaks:
            pg = await fitted_page(ctx, phys + ch)
            for i, p in enumerate(await pg.evaluate(PAUSES)):
                n += 1
                if not (p['nk'] == 1 and p['nt'] == 1 and p['k'] and len(p['k']) <= 40 and p['t']):
                    bad.append('%s #%d %r' % (ch, i, p))
            await pg.close()
        await ctx.close()
        ok('every sitting break (%d, on %d chapters) has one .k of at most 40 characters and a '
           'non-empty .t' % (n, len(with_breaks)), n > 0 and not bad, bad[:3] or '')
        for w in (390, 1280):
            ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                       service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            for ch in ('ch4-6.html', 'ch4-7.html'):
                pg = await fitted_page(ctx, phys + ch)
                ps = await pg.evaluate(PAUSES)
                await pg.close()
                off = [p['t'] for p in ps if not (p['inside'] and p['wraps'] and p['cap'])]
                ok('%s at %d: every .t (%d) wraps inside the column, first letter capitalised'
                   % (ch, w, len(ps)), ps and not off, off[:2] or '')
            await ctx.close()

    print('\nthe mathematics: displays, numbers and inline maths')
    async with section('displays and numbers'):
        for w in (390, 1000, 1280):
            ctx = await br.new_context(viewport={'width': w, 'height': 844 if w < 700 else 900},
                                       service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            for ch in ('ch1-2.html', 'ch3-5.html'):
                pg = await fitted_page(ctx, phys + ch)
                nums = await pg.evaluate(NUMBERS)
                hit = [x['num'] for x in nums if x['hit']]
                ok('%s at %d: no equation number (%d) overlaps its display' % (ch, w, len(nums)),
                   nums and not hit, hit[:5] or '%d dropped below' % sum(x['drop'] for x in nums))
                if w == 1280:
                    left = [x['num'] for x in nums if not x['right']]
                    ok('%s at 1280: every number sits right of the column' % ch, not left, left[:5])
                if w == 390 and ch == 'ch1-2.html':
                    e = [x for x in nums if x['num'] == '(1.2.11)']
                    ok('ch1-2 at 390: (1.2.11) keeps its number on its line',
                       len(e) == 1 and not e[0]['drop'], e)
                if w == 390 and ch == 'ch3-5.html':
                    d = await pg.evaluate(DISPLAYS)
                    nocue = [x for x in d['bad'] if not x['cue']]
                    ok('ch3-5 at 390: every display (%d) fits or shows its edge shades' % d['n'],
                       d['n'] > 0 and not nocue, nocue[:3] or '%d scroll' % len(d['bad']))
                    r = await pg.evaluate("""() => { const p = [...document.querySelectorAll('.main .col > p')]
                        .find(p => !p.closest('.callout, .tools, .pause') && !p.className && p.querySelector('.katex'));
                      return p ? {body: parseFloat(getComputedStyle(p).fontSize),
                                  math: parseFloat(getComputedStyle(p.querySelector('.katex')).fontSize)} : null; }""")
                    ok('ch3-5 at 390: inline maths is 1.045 times the text (+-0.5px)',
                       bool(r) and abs(r['math'] - 1.045 * r['body']) <= 0.5, r)
                await pg.close()
            await ctx.close()
        # the widest displays in the book, at 1280: fitted, or hung into the margin
        ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        for ch in ('ch3-1.html', 'ch3-2.html', 'ch3-7.html', 'ch3-9.html', 'ch4-2.html', 'ch4-7.html'):
            pg = await fitted_page(ctx, phys + ch)
            d = await pg.evaluate(DISPLAYS)
            await pg.close()
            ok('%s at 1280: no display (%d) overflows its box' % (ch, d['n']), d['n'] > 0 and not d['bad'],
               d['bad'][:3] or '')
        await ctx.close()
        # A reader whose default text size is 20px (125%): every rem grows, so
        # the margin track narrows (0 at 1200, 23.75px at 1280) and cannot hold
        # a hanging number. Each number then keeps its line or drops, inside
        # .main's content box, as below 1200. At 1400 the track holds it again.
        for w in (1200, 1280, 1400):
            ctx = await br.new_context(viewport={'width': w, 'height': 900}, service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            cdp = await ctx.new_cdp_session(pg)
            await cdp.send('Page.setFontSizes', {'fontSizes': {'standard': 20, 'fixed': 16}})
            await pg.goto(phys + 'ch1-2.html', wait_until='load', timeout=45000)
            await pg.evaluate('() => document.fonts.ready.then(() => true)')
            await pg.wait_for_timeout(600)
            nums = await pg.evaluate(NUMBERS)
            r = await pg.evaluate(LARGE_TEXT)
            await pg.close()
            await ctx.close()
            hit = [x['num'] for x in nums if x['hit']]
            ok('ch1-2 at %d, 20px default text (root %s, track %s): every number (%d) inside '
               '.main, none over its display, no page overflow'
               % (w, r['root'], r['breakout'], len(nums)),
               r['root'] == '20px' and nums and not hit and r['past'] <= 0.5 and r['pageOver'] <= 0,
               'furthest number edge %+.1fpx from .main, %d hung, %d dropped, overlaps %s, '
               'page overflow %dpx' % (r['past'], r['hung'], sum(x['drop'] for x in nums),
                                       hit[:3] or 0, r['pageOver']))

    print('\nthe mathematics: equation cards')
    async with section('the equation card on ch1-2'):
        ctx = await br.new_context(viewport={'width': 1280, 'height': 900}, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        pg = await fitted_page(ctx, phys + 'ch1-2.html')
        href = await pg.get_attribute('.main a.eqref', 'href')
        await pg.evaluate("() => document.querySelector('.main a.eqref').scrollIntoView({block: 'center', behavior: 'instant'})")
        await pg.wait_for_timeout(200)
        await pg.hover('.main a.eqref')
        if await waitsel(pg, '.refcard.on .katex-display', state='visible'):
            c = await pg.evaluate("""() => { const c = document.querySelector('.refcard.on');
              const go = c.querySelector('a.rc-go');
              return {num: (c.querySelector('.eqnum') || {}).textContent || '',
                      go: go ? go.textContent.trim() : '', href: go ? go.getAttribute('href') : '',
                      ref: document.querySelector('.main a.eqref').textContent.trim()}; }""")
            ok('hovering the first a.eqref at 1280 shows a card with the equation and its number',
               c['num'] == c['ref'] and c['go'] == 'Go to equation' and c['href'] == href, c)
            await pg.hover('.refcard.on a.rc-go')
            await pg.click('.refcard.on a.rc-go')
            await pg.wait_for_timeout(900)
            j = await pg.evaluate("""(h) => { const t = document.getElementById(h.slice(1));
              const r = t.getBoundingClientRect();
              return {hash: location.hash, inview: r.top >= 0 && r.top < innerHeight,
                      open: !!document.querySelector('.refcard.on')}; }""", href)
            ok('its "Go to equation" jumps to %s and closes the card' % href,
               j['hash'] == href and j['inview'] and not j['open'], j)
        await ctx.close()
        ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                   is_mobile=True, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        pg = await fitted_page(ctx, phys + 'ch1-2.html')
        y0 = await pg.evaluate("() => { document.querySelector('.main a.eqref').scrollIntoView({block: 'center', behavior: 'instant'}); return scrollY; }")
        await pg.tap('.main a.eqref')
        if await waitsel(pg, '.refcard.sheet.on .katex-display', state='visible'):
            await pg.wait_for_timeout(300)
            y1 = await pg.evaluate('() => scrollY')
            ok('a tap on it at 390 (touch) opens the sheet and does not jump', abs(y1 - y0) < 2,
               'scrollY %d -> %d' % (y0, y1))
        await ctx.close()


# ------------------------------------------------------ the clinical apparatus
# Folded in from W3-CLINIC's probe: ids, the trial sheet and its registry link,
# and a reference address opening the collapsed list.
async def apparatus(br, base):
    import collections as _c, glob as _glob, re as _re
    print('\nthe clinical apparatus')
    pages = []
    for pat in ('breast-cancer/BC-*.html', 'breast-cancer/trials.html', 'breast-cancer/stories.html',
                'newton-to-mtheory/ch*.html', 'newton-to-mtheory/ledger.html',
                'newton-to-mtheory/throughline.html', 'the-other-end-of-the-trade/*.html'):
        pages += sorted(_glob.glob(os.path.join(DOCS, pat)))
    dup = []
    for f in pages:
        s = _re.sub(r'<script\b.*?</script>', '', open(f, encoding='utf-8').read(), flags=_re.S)
        ids = _c.Counter(_re.findall(r'(?<![-\w])id="([^"]*)"', s))
        dup += ['%s#%s' % (os.path.relpath(f, DOCS), k) for k, v in ids.items() if v > 1]
    ok('no id is used twice on %d chapter and appendix pages' % len(pages), pages and not dup, dup[:4])

    async with section('the trial sheet on BC-900'):
        ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                   is_mobile=True, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        pg = await ctx.new_page()
        await pg.goto(base + 'breast-cancer/BC-900.html', wait_until='load')
        await pg.wait_for_timeout(500)
        await pg.tap('.col .trial[data-trial]')
        if await waitsel(pg, '.refcard.sheet.on', state='visible'):
            s = await pg.evaluate("""() => { const c = document.querySelector('.refcard.sheet.on');
              const m = document.querySelector('.col .trial[data-trial][aria-expanded="true"]');
              const go = c.querySelector('a.rc-go'), f = c.querySelector('.rc-f');
              return {facts: !!(f && f.textContent.trim()), href: go && go.getAttribute('href'),
                      key: m && m.dataset.trial}; }""")
            ok('BC-900 at 390: a tap on the first trial mark opens the sheet with its facts and '
               'a link to trials.html#t-<key>', s['facts'] and bool(s['key'])
               and s['href'] == 'trials.html#t-' + s['key'], s)
            if s['href']:
                await pg.tap('.refcard.sheet.on a.rc-go')
                await pg.wait_for_load_state('load')
                await pg.wait_for_timeout(1000)
                o = await pg.evaluate("(k) => { const d = document.getElementById('t-' + k);"
                                      " return {url: location.pathname + location.hash, open: !!(d && d.open)}; }",
                                      s['key'])
                ok('and following it opens that registry row', o['open'], o)
        await ctx.close()

    async with section('a reference address on BC-870'):
        src = open(os.path.join(DOCS, 'breast-cancer', 'BC-870.html'), encoding='utf-8').read()
        rid = (_re.findall(r'<li id="(r-[^"]+)"', src)[11:12] or [None])[0]
        ok('BC-870 has a twelfth reference', bool(rid), rid)
        if rid:
            ctx = await br.new_context(viewport={'width': 390, 'height': 844}, service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            await pg.goto(base + 'breast-cancer/BC-870.html#' + rid, wait_until='load')
            await pg.wait_for_timeout(900)
            r = await pg.evaluate("""(id) => { const li = document.getElementById(id), rc = li.getBoundingClientRect();
              const bg = getComputedStyle(li).backgroundColor;
              return {open: document.querySelector('details.refs-list').open,
                      inview: rc.top >= 0 && rc.top < innerHeight,
                      lit: bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent'}; }""", rid)
            ok('BC-870 at 390: #%s opens the list, lands on the entry and highlights it' % rid,
               r['open'] and r['inview'] and r['lit'], r)
            await ctx.close()


async def main():
    from playwright.async_api import async_playwright
    base = 'http://127.0.0.1:%d/library/' % PORT
    async with async_playwright() as pw:
        br = await pw.chromium.launch()

        for slug, chap in (('breast-cancer', 'BC-500.html'),
                           ('newton-to-mtheory', 'ch2-1.html')):
            async with section('%s reading order' % slug):
                await chaptered(br, base, slug, chap)

        # ---- standalone: the back control
        print('\nstandalone')
        async with section('standalone back'):
            ctx = await br.new_context(viewport={'width': 390, 'height': 780})
            ctx.set_default_timeout(TIMEOUT)
            await ctx.add_init_script(
                "Object.defineProperty(navigator,'standalone',{get:()=>true});")
            pg = await ctx.new_page()
            await pg.goto(base + 'breast-cancer/contents.html', wait_until='networkidle')
            if await click(pg, '.main a[href$=".html"]'):      # go one page deep
                await pg.wait_for_load_state('load')
                await pg.wait_for_timeout(400)
                ok('back control appears once there is history',
                   await pg.query_selector('.topnav .pwa-back') is not None)
                if await pg.query_selector('.topnav .pwa-back'):
                    if await click(pg, '.topnav .pwa-back'):
                        await pg.wait_for_load_state('load')
                        ok('it goes back', pg.url.endswith('contents.html'),
                           pg.url.split('/')[-1])
            await ctx.close()

        # ---- a page in the book but not in the sequence keeps its keyboard
        async with section('off-sequence keys'):
            pg = await page(br, 1400, 900)
            await pg.goto(base + 'breast-cancer/trials.html', wait_until='networkidle')
            await pg.wait_for_timeout(300)
            before = pg.url
            await pg.keyboard.press('ArrowRight')
            await pg.wait_for_timeout(250)
            ok('arrow keys do nothing off-sequence', pg.url == before, pg.url.split('/')[-1])
            await pg.close()

        # ---- a book with no reading order is untouched
        async with section('single-page book'):
            pg = await page(br, 390, 780)
            await pg.goto(base + 'the-long-argument/index.html', wait_until='networkidle')
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.wait_for_timeout(400)
            ok('single-page book raises nothing', not errs, errs[:1])
            await pg.close()

        # ------------------------------------------------------ the folio bar
        # Below 1000px: numbered arrows read from the chapter foot, the next
        # one going to the next chapter (C1-folio-arrows), with the chapter
        # foot ending above it at the end of the page (NAV-06). Then headroom:
        # reading down takes the bar and the folio out of view, a deliberate
        # scroll up (48px or more) brings them back, and a nudge up to re-read
        # a line does not (C1-headroom-handles).
        print('\nthe folio bar and headroom at 390')
        for slug, chap in (('breast-cancer', 'BC-500.html'),
                           ('newton-to-mtheory', 'ch2-1.html')):
            async with section('%s folio and headroom' % slug):
                order = json_of(os.path.join(DOCS, slug, 'nav.json'))
                hrefs = [c['href'] for c in order['chapters']]
                prev_c, next_c = (order['chapters'][hrefs.index(chap) + d] for d in (-1, 1))
                ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                           is_mobile=True, service_workers='block')
                ctx.set_default_timeout(TIMEOUT)
                pg = await ctx.new_page()
                await pg.goto(base + slug + '/' + chap, wait_until='load')
                if await waitsel(pg, '.folio'):
                    await pg.wait_for_timeout(300)
                    f = await pg.evaluate(FOLIO)
                    ok('%s: the folio bar is there at 390' % chap, f['shown'], f)
                    ok('%s: its \u203a names the next chapter (%s)' % (chap, next_c['num']),
                       next_c['num'] in f['next'], repr(f['next']))
                    ok('%s: and goes to it' % chap, f['nextHref'] == next_c['href'], f['nextHref'])
                    ok('%s: its \u2039 names the previous chapter (%s)' % (chap, prev_c['num']),
                       prev_c['num'] in f['prev'], repr(f['prev']))
                    await pg.evaluate(TO_END)
                    await pg.wait_for_timeout(450)
                    f = await pg.evaluate(FOLIO)
                    ok('%s: at the end, the folio is shown and the chapter foot ends above it'
                       % chap, f['shown'] and f['chapnavBottom'] is not None
                       and f['chapnavBottom'] <= f['top'] + 0.5, f)
                    await pg.evaluate("() => window.scrollTo({top: 0, behavior: 'instant'})")
                    await pg.wait_for_timeout(300)
                    async def at_y(y):
                        await pg.evaluate("(y) => window.scrollTo({top: y, behavior: 'instant'})", y)
                        await pg.wait_for_timeout(450)
                        return await pg.evaluate(CHROME)
                    c = await at_y(1500)
                    ok('%s: 1500px down takes the bar and the folio out of view' % chap,
                       c['barOut'] and c['folioOut'], c)
                    c = await at_y(1480)
                    ok('%s: a 20px nudge up leaves them out' % chap, c['barOut'] and c['folioOut'], c)
                    await at_y(1580)
                    c = await at_y(1380)
                    ok('%s: 200px up brings both back' % chap, c['barIn'] and c['folioIn'], c)
                await ctx.close()

        # ------------------------------------------------------ the spy
        # The active sidebar entry is the heading above the bar's bottom edge
        # plus 24px, after a jump and after scrolling up, where the old
        # observer marked nothing or the section below (NAV-08).
        print('\nthe sidebar spy')
        async with section('the spy on ch1-1'):
            ctx = await br.new_context(viewport={'width': 1280, 'height': 900},
                                       service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            await pg.goto(base + 'newton-to-mtheory/ch1-1.html', wait_until='load')
            await pg.wait_for_timeout(500)
            SPY = """() => {
              const bar = document.querySelector('.topnav').getBoundingClientRect();
              const edge = Math.max(0, bar.top) + bar.height + 24;
              const hs = [...document.querySelectorAll('.main h2[id], .main h3[id]')];
              const links = new Set([...document.querySelectorAll('#sb-toc a')].map(a => a.getAttribute('href')));
              let at = -1;
              hs.forEach((h, i) => { const r = h.getBoundingClientRect(); if ((r.width || r.height) && r.top < edge) at = i; });
              let want = null;
              for (let i = at; i >= 0 && !want; i--) if (links.has('#' + hs[i].id)) want = '#' + hs[i].id;
              const a = document.querySelector('#sb-toc a.active');
              return {active: a ? a.getAttribute('href') : null, want: want,
                      n: document.querySelectorAll('#sb-toc a.active').length};
            }"""
            await pg.evaluate("() => window.scrollTo({top: (document.documentElement.scrollHeight"
                              " - innerHeight) * .4, behavior: 'instant'})")
            await pg.wait_for_timeout(300)
            r = await pg.evaluate(SPY)
            ok('after scrollTo(40%) the active entry is the section being read',
               r['active'] is not None and r['active'] == r['want'] and r['n'] == 1, r)
            await pg.evaluate("() => window.scrollBy({top: -600, behavior: 'instant'})")
            await pg.wait_for_timeout(300)
            r = await pg.evaluate(SPY)
            ok('and after scrolling up 600px', r['active'] is not None and r['active'] == r['want']
               and r['n'] == 1, r)
            await ctx.close()

        # ------------------------------------------------------ the way up on a phone
        # The drawer's first row is the sidebar's up-link: the chapter's part in
        # the contents (C1-phone-up). The part's id is read from the contents
        # page itself, so this checks the link lands on a real heading.
        print('\nthe way up on a phone')
        async with section('the drawer up-link on BC-500'):
            import re as _re
            order = json_of(os.path.join(DOCS, 'breast-cancer', 'nav.json'))
            part = next(c['part'] for c in order['chapters'] if c['href'] == 'BC-500.html')
            src = open(os.path.join(DOCS, 'breast-cancer', 'contents.html'), encoding='utf-8').read()
            ids = {' '.join(_re.sub(r'<[^>]+>', '', t).split()): i for i, t in
                   _re.findall(r'<h2 class="part-head" id="(sec-\d+)">(.*?)</h2>', src, _re.S)}
            want = 'contents.html#' + ids.get(part, '?')
            ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                       is_mobile=True, service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            await pg.goto(base + 'breast-cancer/BC-500.html', wait_until='load')
            if await waitsel(pg, '#mnav-btn'):
                await pg.tap('#mnav-btn')
                await pg.wait_for_timeout(450)
                up = await pg.query_selector('#mnav a.mn-up')
                href = up and await up.get_attribute('href')
                ok('BC-500 at 390: the open drawer\'s up-row goes to %s' % want, href == want, href)
                ok('and is visible, first in the sheet, at least 48px tall',
                   bool(up) and await up.is_visible() and await pg.evaluate("""() => {
                     const u = document.querySelector('#mnav a.mn-up');
                     const first = [...document.querySelectorAll('#mnav > *')].find(e => e.textContent.trim());
                     return first === u && u.getBoundingClientRect().height >= 48; }"""))
            await ctx.close()

        # ------------------------------------------------------ find a chapter
        # The contents page's search box filters the rows by number and title,
        # hides the parts with nothing left, and Escape puts every row back
        # (C1-lookup).
        print('\nfind a chapter')
        async with section('find a chapter on breast-cancer/contents.html'):
            total = json_of(os.path.join(DOCS, 'breast-cancer', 'nav.json'))['count']
            ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                       is_mobile=True, service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            await pg.goto(base + 'breast-cancer/contents.html', wait_until='load')
            ROWS = """() => { const vis = e => e.getClientRects().length > 0;
              const rows = [...document.querySelectorAll('.clist li')];
              return {n: document.querySelectorAll('input.toc-find').length, rows: rows.length,
                      shown: rows.filter(vis).map(r => r.textContent.replace(/\\s+/g, ' ').trim()),
                      parts: [...document.querySelectorAll('h2.part-head')].filter(vis).length}; }"""
            if await waitsel(pg, 'input.toc-find'):
                r = await pg.evaluate(ROWS)
                ok('one Find a chapter box', r['n'] == 1, r['n'])
                await pg.fill('input.toc-find', 'HER2')
                await pg.wait_for_timeout(150)
                r = await pg.evaluate(ROWS)
                ok('typing HER2 leaves only the rows that match',
                   r['shown'] and all('her2' in t.lower() for t in r['shown']),
                   '%d rows: %s' % (len(r['shown']), r['shown'][:3]))
                await pg.press('input.toc-find', 'Escape')
                await pg.wait_for_timeout(150)
                r = await pg.evaluate(ROWS)
                ok('Escape restores all %d' % total, len(r['shown']) == total == r['rows'],
                   '%d of %d' % (len(r['shown']), r['rows']))
            await ctx.close()

        # ---------------------------------------------------------------- the bar
        # The same destinations on every page of a book, and the same ones the
        # book declares. Expected from book.json rather than written out here:
        # a fixture would have to be edited every time a book gains a page,
        # which is the failure this whole change is about.
        print('\nthe bar')
        for bk in library.books():
            want = [(i['href'], i['label']) for i in bk.nav_items()]
            for pagename in BAR_PAGES[bk.slug]:
                async with section('the bar on %s/%s' % (bk.slug, pagename)):
                    pg = await opened(br, base + bk.slug + '/' + pagename)
                    # the book's destinations, then Library, which sits outside
                    # the group so that it never folds under Menu on a phone
                    got = await pg.eval_on_selector_all(
                        '.topnav-links a, .topnav .up',
                        'els => els.map(e => [e.getAttribute("href"), e.textContent.trim()])')
                    got = [tuple(x) for x in got]
                    ok('%s/%s offers what book.json declares' % (bk.slug, pagename),
                       got == want, got if got != want else '')
                    # the page you are on is named, and not offered as a link to itself
                    cur = await pg.eval_on_selector_all(
                        '.topnav [aria-current="page"]',
                        'els => els.map(e => e.getAttribute("href"))')
                    here = [h for h, _l in want if h == pagename] or (
                        ['index.html'] if pagename == 'index.html' else [])
                    ok('%s/%s marks where you are' % (bk.slug, pagename), cur == here, cur)
                    await pg.close()

        # ---- the window still fits, on the two books that fill it
        # Both draw their own full-height interface. The bar is above it now,
        # and a page that scrolls by exactly the height of the bar is the way
        # that goes wrong.
        for slug in ('the-long-argument', 'the-ages-of-thought'):
            async with section('%s fits the window' % slug):
                pg = await opened(br, base + slug + '/index.html')
                over = await pg.evaluate(
                    '() => document.documentElement.scrollHeight - window.innerHeight')
                ok('%s fits the window with the bar' % slug, over <= 1, over)
                vis = await pg.is_visible('.topnav .up')
                ok('%s keeps the way back visible' % slug, vis)
                await pg.close()

        # ------------------------------------------------------ the phone drawer
        # The drawer holds the chapter's sections and its neighbours, and
        # nothing the bar already offers: the destinations are under the bar's
        # Menu on a phone, and the theme control is the bar's (NAV-07). The
        # rows pwa.js and book.js used to add for them must stay gone.
        print('\nthe drawer')
        GONE = ('() => ({dest: document.querySelectorAll("#mnav .mn-dest").length,'
                ' foot: document.querySelectorAll("#mnav .mn-foot").length,'
                ' theme: document.querySelectorAll("#mn-theme").length})')
        for slug, chap in (('breast-cancer', 'BC-500.html'),
                           ('newton-to-mtheory', 'ch2-1.html')):
            async with section('%s drawer' % slug):
                pg = await opened(br, base + slug + '/' + chap, 390, 780)
                if await waitsel(pg, '#mnav .mn-seq'):
                    if await click(pg, '#mnav-btn'):
                        await pg.wait_for_timeout(250)
                        ok('%s drawer opens with its prev/next row in view' % slug,
                           await pg.is_visible('#mnav .mn-seq .next'))
                    g = await pg.evaluate(GONE)
                    ok('%s drawer carries no destinations, footer or theme button' % slug,
                       g == {'dest': 0, 'foot': 0, 'theme': 0}, g)
                await pg.close()

            # the contents page builds a drawer too; outside the sequence it
            # has no prev/next row, and it carries nothing the bar has
            async with section('%s drawer on the contents page' % slug):
                pg = await opened(br, base + slug + '/contents.html', 390, 780)
                if await waitsel(pg, '#mnav'):
                    await waitfn(pg, "() => window.LibraryPWA && window.LibraryPWA.nav().ready",
                                 what='the reading order (LibraryPWA.nav().ready)')
                    await pg.wait_for_timeout(150)
                    g = await pg.evaluate(GONE)
                    ok('%s contents drawer carries no destinations, footer or theme button'
                       % slug, g == {'dest': 0, 'foot': 0, 'theme': 0}, g)
                seq = await pg.query_selector('#mnav .mn-seq')
                ok('and no prev/next, being outside the sequence', seq is None)
                await pg.close()

        # ------------------------------------------------------ the bar under pressure
        # One row at every width, with the theme button last and inside it.
        # The bar used to wrap to two rows and hold a gutter open for a toggle
        # that floated over its last link (NAV-03). These are the widths that
        # decide it: a small phone, the phone everything else here is checked
        # at, and a desktop. At the two phone widths the destinations are
        # folded under Menu, so only what is on screen is tested for overlap.
        print('\nthe bar under pressure')
        BAR_FIT = """() => {
          const bar = document.querySelector('.topnav');
          const vis = e => { const cs = getComputedStyle(e), r = e.getBoundingClientRect();
            return cs.display !== 'none' && cs.visibility === 'visible' && r.width > 0 && r.height > 0; };
          const b = bar.querySelector('.nav-brand');
          const t = bar.querySelector('.nav-theme');
          const items = [...bar.querySelectorAll('.nav-brand, .nav-menu, .topnav-links a, .up')]
            .filter(vis);
          const tr = t ? t.getBoundingClientRect() : null;
          const hit = (a, c) => a.right > c.left + 1 && a.left < c.right - 1
                             && a.bottom > c.top + 1 && a.top < c.bottom - 1;
          const over = tr ? items.filter(e => hit(e.getBoundingClientRect(), tr))
                                 .map(e => e.textContent.trim()) : [];
          const br = bar.getBoundingClientRect();
          const kids = [...bar.children].filter(vis);
          return {clipped: b.scrollWidth > b.clientWidth + 1 || b.scrollHeight > b.clientHeight + 1,
                  spill: kids.some(e => e.getBoundingClientRect().right > innerWidth + 1),
                  theme: !!t && vis(t) && bar.contains(t),
                  inside: !!tr && tr.left >= br.left - 1 && tr.right <= br.right + 1
                          && tr.top >= br.top - 1 && tr.bottom <= br.bottom + 1,
                  last: kids.length > 0 && kids[kids.length - 1] === t,
                  over: over, h: Math.round(br.height * 10) / 10};
        }"""
        for slug, pagename in (('newton-to-mtheory', 'index.html'),     # three links + Library
                               ('newton-to-mtheory', 'ch2-1.html'),     # the same, and a drawer
                               ('breast-cancer', 'index.html'),         # three links + Library
                               ('the-ages-of-thought', 'index.html'),   # Library only, own chrome
                               ('', 'index.html')):                     # the hub: brand and theme
            for w in (320, 390, 1400):
                where_ = (slug + '/' if slug else '') + pagename
                async with section('the bar on %s at %d' % (where_, w)):
                    pg = await opened(br, base + where_, w, 800)
                    r = await pg.evaluate(BAR_FIT)
                    bad = [k for k in ('clipped', 'spill') if r[k]]
                    bad += [k for k in ('theme', 'inside', 'last') if not r[k]]
                    if r['over']:
                        bad.append('theme button over %s' % r['over'])
                    ok('%s at %d: one row, title, links and theme button apart, the theme '
                       'button last and inside the bar' % (where_, w), not bad,
                       bad or 'bar %spx' % r['h'])
                    await pg.close()

        # ---- the bar is at most 48px on a phone, on every page that has one
        print('\nthe bar on a phone')
        ctx = await br.new_context(viewport={'width': 390, 'height': 844}, has_touch=True,
                                   is_mobile=True, service_workers='block')
        ctx.set_default_timeout(TIMEOUT)
        for where_ in ['index.html'] + ['%s/%s' % (bk.slug, p) for bk in library.books()
                                        for p in BAR_PAGES[bk.slug]]:
            async with section('the bar height on %s' % where_):
                pg = await ctx.new_page()
                await pg.goto(base + where_, wait_until='load')
                await pg.wait_for_timeout(250)
                h = await pg.evaluate(
                    "() => document.querySelector('.topnav').getBoundingClientRect().height")
                ok('%s: the bar is one row at 390 touch (<=48px)' % where_, h <= 48, h)
                await pg.close()
        await ctx.close()

        # ---- Menu, at 390: exactly the book's destinations, in 48px rows,
        # with Library and the theme button still in the bar
        print('\nthe menu')
        for bk in library.books():
            dests = [i['label'] for i in bk.nav_items() if i['key'] != 'library']
            # the front door, then the sample pages that are chapters: named by
            # whatever scheme the book uses (ch2-1, BC-500, 9a), so asked of it
            chapters = {f[1] + '.html' for f in bk.written()}
            for pagename in BAR_PAGES[bk.slug][:1] + [p for p in BAR_PAGES[bk.slug][1:]
                                                     if p in chapters]:
                where_ = '%s/%s' % (bk.slug, pagename)
                async with section('the menu on %s' % where_):
                    ctx = await br.new_context(viewport={'width': 390, 'height': 844},
                                               has_touch=True, is_mobile=True,
                                               service_workers='block')
                    ctx.set_default_timeout(TIMEOUT)
                    pg = await ctx.new_page()
                    await pg.goto(base + where_, wait_until='load')
                    await pg.wait_for_timeout(250)
                    menu = await pg.query_selector('.topnav .nav-menu')
                    if not dests:
                        ok('%s: no Menu, having nothing to fold' % where_, menu is None)
                        await ctx.close()
                        continue
                    ok('%s: the Menu is shown and wired' % where_,
                       menu is not None and await menu.is_visible())
                    if menu is not None and await menu.is_visible():
                        await menu.tap()
                        await pg.wait_for_timeout(200)
                        r = await pg.evaluate("""() => {
                          const vis = e => { const cs = getComputedStyle(e), r = e.getBoundingClientRect();
                            return cs.display !== 'none' && cs.visibility === 'visible' && r.height > 0; };
                          const rows = [...document.querySelectorAll('#nav-dest a')].filter(vis);
                          const up = document.querySelector('.topnav .up');
                          const th = document.querySelector('.topnav .nav-theme');
                          const bar = document.querySelector('.topnav').getBoundingClientRect();
                          const inbar = e => { const r = e.getBoundingClientRect();
                            return vis(e) && r.top >= bar.top - 1 && r.bottom <= bar.bottom + 1; };
                          return {rows: rows.map(e => e.textContent.trim()),
                                  minh: Math.min(...rows.map(e => e.getBoundingClientRect().height)),
                                  expanded: document.querySelector('.nav-menu').getAttribute('aria-expanded'),
                                  up: !!up && inbar(up), theme: !!th && inbar(th)};
                        }""")
                        ok('%s: Menu lists exactly the destinations' % where_,
                           r['rows'] == dests and r['expanded'] == 'true', r['rows'])
                        ok('%s: each row is at least 48px' % where_, r['minh'] >= 48, r['minh'])
                        ok('%s: Library and the theme button stay in the bar' % where_,
                           r['up'] and r['theme'], r)
                        await pg.keyboard.press('Escape')
                        await pg.wait_for_timeout(150)
                        shut = await pg.evaluate("""() => ({
                          open: document.querySelector('.topnav').classList.contains('menu-open'),
                          focus: document.activeElement === document.querySelector('.nav-menu')})""")
                        ok('%s: Escape closes it and returns focus to Menu' % where_,
                           not shut['open'] and shut['focus'], shut)
                    await ctx.close()

        # ---- the brand sits at the bar's inset, at the same x on every page
        print('\nthe brand does not move')
        for w in (1280, 1680):
            ctx = await br.new_context(viewport={'width': w, 'height': 900},
                                       service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            xs = {}
            for where_ in ['index.html'] + ['%s/%s' % (bk.slug, p) for bk in library.books()
                                            for p in BAR_PAGES[bk.slug]]:
                async with section('the brand on %s at %d' % (where_, w)):
                    pg = await ctx.new_page()
                    await pg.goto(base + where_, wait_until='load')
                    await pg.wait_for_timeout(200)
                    xs[where_] = await pg.evaluate("""() => {
                      const bar = document.querySelector('.topnav');
                      return {x: bar.querySelector('.nav-brand').getBoundingClientRect().left,
                              inset: parseFloat(getComputedStyle(bar).paddingLeft),
                              up: (bar.querySelector('.up') || {getBoundingClientRect: () => ({left: null})})
                                    .getBoundingClientRect().left};
                    }""")
                    await pg.close()
            await ctx.close()
            got = sorted(set(round(v['x'], 1) for v in xs.values()))
            ok('at %d the brand has one x on every barred page, at the inset' % w,
               got and got[-1] - got[0] <= 1 and all(abs(v['x'] - v['inset']) <= 1
                                                      for v in xs.values()),
               {k: round(v['x'], 1) for k, v in xs.items()} if len(got) > 1 else got)
            for bk in library.books():
                ups = sorted(set(round(xs[k]['up'], 1) for k in xs
                                 if k.startswith(bk.slug + '/') and xs[k]['up'] is not None))
                if ups:
                    ok('at %d %s keeps Library at one x on every page type' % (w, bk.slug),
                       ups[-1] - ups[0] <= 1, ups)

        # ---- one theme, decided once, and a press that sticks
        # A reader whose OS is dark, arriving with nothing stored, gets dark on
        # every page, and nothing is written until they press the button. The
        # library used to switch them to light at the first chapter and then
        # remember light as their choice (NAV-02, PDA-01).
        print('\nthe theme')
        async with section('the theme journey'):
            ctx = await br.new_context(viewport={'width': 1280, 'height': 900},
                                       color_scheme='dark', service_workers='block')
            ctx.set_default_timeout(TIMEOUT)
            pg = await ctx.new_page()
            seen = []
            for where_ in ('index.html', 'breast-cancer/index.html',
                           'breast-cancer/contents.html', 'breast-cancer/BC-500.html',
                           'breast-cancer/trials.html', 'newton-to-mtheory/index.html'):
                await pg.goto(base + where_, wait_until='load')
                await pg.wait_for_timeout(250)
                seen.append((where_, await pg.evaluate(
                    "() => document.documentElement.getAttribute('data-theme')")))
            ok('an OS-dark first visit is dark on every page', all(t == 'dark' for _w, t in seen),
               [x for x in seen if x[1] != 'dark'] or '%d pages' % len(seen))
            stored = await pg.evaluate("() => localStorage.getItem('library:v1')")
            ok('and nothing about the theme is stored until the reader chooses',
               not stored or ('"look"' not in stored and '"theme"' not in stored), stored)
            await pg.goto(base + 'breast-cancer/BC-500.html', wait_until='load')
            await pg.wait_for_timeout(250)
            ok('BC-500 has the bar\'s theme button, wired',
               await pg.evaluate("() => { const b = document.querySelector('.topnav .nav-theme');"
                                 " return !!b && !b.hidden &&"
                                 " document.documentElement.classList.contains('theme-wired'); }"))
            if await click(pg, '.topnav .nav-theme'):
                await pg.wait_for_timeout(200)
                now = await pg.evaluate("""() => ({t: document.documentElement.getAttribute('data-theme'),
                  pressed: document.querySelector('.topnav .nav-theme').getAttribute('aria-pressed'),
                  look: (JSON.parse(localStorage.getItem('library:v1') || '{}') || {}).look})""")
                ok('pressing it on BC-500 turns the page light and records the choice',
                   now == {'t': 'light', 'pressed': 'false', 'look': 'light'}, now)
                await pg.goto(base + 'breast-cancer/contents.html', wait_until='load')
                await pg.wait_for_timeout(200)
                t = await pg.evaluate("() => document.documentElement.getAttribute('data-theme')")
                ok('and the next page opens light, the OS still dark', t == 'light', t)
            await ctx.close()

        # ---- the hub has the same bar, with the theme button
        async with section('the hub bar'):
            pg = await opened(br, base + 'index.html', 1280, 900)
            r = await pg.evaluate("""() => {
              const bar = document.querySelector('.topnav');
              const b = bar && bar.querySelector('.nav-theme');
              return {bar: !!bar, theme: !!b && !b.hidden,
                      brand: bar ? bar.querySelector('.nav-brand').textContent.trim() : null,
                      current: bar ? bar.querySelector('.nav-brand').getAttribute('aria-current') : null};
            }""")
            ok('the hub carries the bar, named and marked current, with the theme button',
               r == {'bar': True, 'theme': True, 'brand': 'A Library', 'current': 'page'}, r)
            await pg.close()

        # ---------------------------------------------------- nothing scrolls sideways
        # A page that scrolls sideways on a phone puts part of itself where a
        # reader will not find it, and the reader is given no reason to look.
        # book.css has guards for the two things that are wide -- a table and an
        # interactive figure both scroll inside their own box -- and the Math
        # Ledger escaped both: KaTeX's hidden MathML copy is position:absolute,
        # nothing between a table cell and the page was positioned, so its
        # containing block was the body and the table's scroller did not hold
        # it. The page was 68px wide of the window at 390px with nothing visible
        # to explain it.
        #
        # Six pages rather than a hundred and forty-seven, because each costs a
        # page load: the two that carry most of the mathematics, the two widest
        # tables in the library, and the two books that draw their own interface.
        print('\nnothing scrolls sideways')
        for pagename in ('newton-to-mtheory/ledger.html',
                         'newton-to-mtheory/throughline.html',
                         'newton-to-mtheory/ch2-1.html',
                         'breast-cancer/trials.html',
                         'the-long-argument/index.html',
                         'the-ages-of-thought/index.html'):
            for w in (320, 390):
                async with section('%s sideways at %d' % (pagename, w)):
                    pg = await opened(br, base + pagename, w, 800)
                    over = await pg.evaluate(
                        '() => document.documentElement.scrollWidth - window.innerWidth')
                    ok('%s does not scroll sideways at %d' % (pagename, w), over <= 1, over)
                    await pg.close()

        # ------------------------------------------------- standalone, everywhere
        # The back control is injected into the bar. A page without one had no
        # back control, and in a home-screen app there is no browser chrome to
        # supply another: the atlas was a dead end on an iPhone.
        print('\nstandalone, on a landing page')
        for slug in ('the-ages-of-thought', 'newton-to-mtheory'):
            async with section('%s standalone landing' % slug):
                ctx = await br.new_context(viewport={'width': 390, 'height': 780})
                ctx.set_default_timeout(TIMEOUT)
                await ctx.add_init_script(
                    "Object.defineProperty(navigator,'standalone',{get:()=>true});")
                pg = await ctx.new_page()
                await pg.goto(base + 'index.html', wait_until='networkidle')
                await pg.goto(base + slug + '/index.html', wait_until='networkidle')
                await pg.wait_for_timeout(400)
                ok('%s landing page has a back control' % slug,
                   await pg.query_selector('.topnav .pwa-back') is not None)
                await ctx.close()

        # ------------------------------------------------- one number per equation
        # The build numbers every .eq; runtime_js() switches the runtime numbering
        # off. If the boot-shape contract breaks (DESIGN.md section 8), the page
        # numbers them again and every equation shows two numbers.
        print('\nequation numbers')
        async with section('equation numbers on ch1-1'):
            pg = await opened(br, base + 'newton-to-mtheory/ch1-1.html', 1280, 900)
            await pg.wait_for_timeout(600)
            r = await pg.evaluate("""() => {
              const eqs = [...document.querySelectorAll('.main .eq')];
              const off = eqs.filter(e => e.querySelectorAll('.eqnum').length !== 1);
              return {n: eqs.length, off: off.length,
                      ids: off.slice(0, 5).map(e => (e.id || '?') + ':' +
                                                    e.querySelectorAll('.eqnum').length)};
            }""")
            ok('ch1-1 has numbered equations to check', r['n'] > 0, r['n'])
            ok('every .eq on ch1-1 has exactly one .eqnum after load', r['off'] == 0,
               '%d of %d wrong: %s' % (r['off'], r['n'], r['ids']) if r['off']
               else '%d equations' % r['n'])
            await pg.close()

        # ------------------------------------------------- the returning reader
        # Where a reader was, offered back to them wherever they arrive
        # (DESIGN.md sections 6 to 8; NAV-01, NAV-14, FD-19, C1-clinical-resume).
        # One reader, one browser: ch1-1 read to 40%, then BC-500. pwa.js
        # records lastBy on a chapter and nowhere else; the hub's Continue
        # strip lists the two books most recent first; continue.html?b= lands
        # on the book's place; the physics contents marks the row; the
        # sequential front door's primary becomes "Continue reading" with
        # Begin kept as the first text link, and the reference front door
        # keeps Contents and gains "Continue at ...".
        print('\nthe returning reader')
        async with section('the returning reader'):
            await returning_reader(br, base)

        # --------------------------------------------------- the hub's tiles
        async with section('the hub tiles'):
            await hub_tiles(br, base)

        # ------------------------------------ the mathematics and the apparatus
        async with section('the mathematics'):
            await mathematics(br, base)
        async with section('the clinical apparatus'):
            await apparatus(br, base)

        # --------------------------------------------------- the masked sweep
        async with section('the masked-overflow sweep'):
            await sweep(br, base)

        await br.close()


if __name__ == '__main__':
    if not os.path.isdir(DOCS):
        raise SystemExit('navcheck: no docs/ to drive. Run tools/webbuild.py first.')
    httpd = serve()
    try:
        asyncio.run(main())
    finally:
        httpd.shutdown()
    if fails:
        print('\nnavcheck: %d failure(s): %s' % (len(fails), ', '.join(fails)))
        raise SystemExit(1)
    print('\nnavcheck: the reading order, the drawer, the folio bar, headroom, the '
          'keyboard and the standalone back all behave in both chaptered books;\n'
          '          the sidebar marks the section being read; Find a chapter filters '
          'the contents; every page, the hub\n'
          '          included, carries one bar in one row with the theme button last, the '
          'brand at one x and the book\'s destinations under '
          'Menu\n          on a phone; an OS-dark reader stays dark and a press '
          'sticks; a returning reader is offered their place on the hub, the front doors, the\n'
          '          contents and continue.html?b=; Tab onto a hub tile brings its weather and ring; '
          'every equation carries one number, clear of its display;\n'
          '          every sitting break has its kicker and line, the displays fit or say they '
          'scroll, an equation reference has its card;\n'
          '          no id repeats, the trial sheet reaches the registry, a reference address '
          'opens the list; and nothing new\n'
          '          passes the viewport with the shell unmasked '
          '(%d KNOWN entries, each owned by the package that removes it)'
          % sum(len(v) for v in KNOWN.values()))
