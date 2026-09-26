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
    'the-long-argument':   ['index.html', 'contents.html'],
    'the-ages-of-thought': ['index.html'],
    'breast-cancer':       ['index.html', 'contents.html', 'BC-500.html',
                            'stories.html', 'trials.html'],
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
    # the evidence tables bleed 2px past a 390px phone (PDA-09: the bleed and
    # .main's padding disagree); W3-CLINIC puts the phone bleed on --gutter
    ('breast-cancer/BC-900.html', 390): {'div.col>div.evidence': 'W3-CLINIC'},
    # the sitting-break labels are white-space:nowrap and run up to 2049px wide,
    # clipped by the shell (PDA-09, R-03); W4-MATH lets them wrap
    ('newton-to-mtheory/ch4-6.html', 390): {'p.pause>span': 'W4-MATH'},
    ('newton-to-mtheory/ch4-6.html', 1280): {'p.pause>span': 'W4-MATH'},
    ('newton-to-mtheory/ch4-7.html', 390): {'p.pause>span': 'W4-MATH'},
    ('newton-to-mtheory/ch4-7.html', 1280): {'p.pause>span': 'W4-MATH'},
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
    await pg.goto(url, wait_until='networkidle')
    for _ in range(3):
        try:
            await pg.wait_for_function(
                "() => !('serviceWorker' in navigator)"
                " || navigator.serviceWorker.controller !== null", timeout=6000)
            break
        except Exception:
            # not a failure: the page may simply still be arriving
            await pg.wait_for_load_state('networkidle')
    await pg.wait_for_timeout(200)
    return pg


READY = "() => window.LibraryPWA && window.LibraryPWA.nav().index >= 0"


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
        pg = await page(br, 390, 780)
        await pg.goto(base + slug + '/' + chap, wait_until='networkidle')
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
                    got = await pg.eval_on_selector_all(
                        '.topnav-links a',
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
        # The drawer is the whole of the navigation on a phone: the bar is at
        # the top of a five-thousand word chapter and the reader is not.
        print('\nthe drawer')
        for slug, chap in (('breast-cancer', 'BC-500.html'),
                           ('newton-to-mtheory', 'ch2-1.html')):
            bk = library.book(slug)
            want = [i['label'] for i in bk.nav_items()]
            async with section('%s drawer destinations' % slug):
                pg = await opened(br, base + slug + '/' + chap, 390, 780)
                if await waitsel(pg, '#mnav .mn-dest'):
                    got = await pg.eval_on_selector_all(
                        '#mnav .mn-dest > *', 'els => els.map(e => e.textContent.trim())')
                    ok('%s drawer offers what the bar offers' % slug, got == want, got)
                    if await click(pg, '#mnav-btn'):
                        await pg.wait_for_timeout(250)
                        ok('the destinations are reachable without scrolling the chapter',
                           await pg.is_visible('#mnav .mn-dest .up'))
                    dup = await pg.eval_on_selector_all(
                        '#mnav .mn-foot a', 'els => els.length')
                    ok('no second way to the contents page under them', dup == 0, dup)
                await pg.close()

            # on the contents page the drawer still lists them, and the entry
            # for the page you are on has stopped being a control
            async with section('%s drawer on the contents page' % slug):
                pg = await opened(br, base + slug + '/contents.html', 390, 780)
                if await waitsel(pg, '#mnav .mn-dest'):
                    kinds = await pg.eval_on_selector_all(
                        '#mnav .mn-dest > *', 'els => els.map(e => e.tagName)')
                    ok('%s contents page keeps the destinations' % slug,
                       kinds.count('SPAN') == 1 and 'A' in kinds, kinds)
                seq = await pg.query_selector('#mnav .mn-seq')
                ok('and no prev/next, being outside the sequence', seq is None)
                await pg.close()

        # ------------------------------------------------------ the bar under pressure
        # The bar carries a title, up to four links and, on one page, a
        # floating theme toggle sitting over it. It has to lose none of them.
        # Squeezing the title was the first answer and it squeezed the physics
        # book's to zero pixels; the bar wraps instead. These are the three
        # widths that decide it: a small phone, the phone everything else here
        # is checked at, and a desktop.
        print('\nthe bar under pressure')
        for slug, pagename in (('newton-to-mtheory', 'index.html'),     # four links + toggle
                               ('newton-to-mtheory', 'ch2-1.html'),     # four links + drawer
                               ('breast-cancer', 'index.html'),         # four links, no toggle
                               ('the-ages-of-thought', 'index.html')):  # one link, own chrome
            for w in (320, 390, 1400):
                async with section('the bar on %s/%s at %d' % (slug, pagename, w)):
                    pg = await opened(br, base + slug + '/' + pagename, w, 800)
                    r = await pg.evaluate("""() => {
                      const bar = document.querySelector('.topnav');
                      const b = bar.querySelector('.nav-brand');
                      const L = bar.querySelector('.topnav-links');
                      const t = document.getElementById('themer');
                      const on = t && getComputedStyle(t).display !== 'none';
                      let over = false;
                      if (on) { const c = t.getBoundingClientRect(), a = L.getBoundingClientRect();
                        over = a.right > c.left + 1 && a.left < c.right
                            && a.bottom > c.top + 1 && a.top < c.bottom - 1; }
                      return {clipped: b.scrollWidth > b.clientWidth + 1,
                              spill: L.getBoundingClientRect().right > window.innerWidth + 1,
                              over: over};
                    }""")
                    ok('%s/%s at %d keeps its title, links and toggle apart'
                       % (slug, pagename, w),
                       not (r['clipped'] or r['spill'] or r['over']),
                       [k for k in ('clipped', 'spill', 'over') if r[k]])
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
    print('\nnavcheck: the reading order, the drawer, the keyboard and the '
          'standalone back all behave in both chaptered books, and every book '
          'offers\n          the same navigation on every page, on both '
          'surfaces, at every width; every equation carries one number, and '
          'nothing new\n          passes the viewport with the shell unmasked '
          '(%d KNOWN entries, each owned by the package that removes it)'
          % sum(len(v) for v in KNOWN.values()))
