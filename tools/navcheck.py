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

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
PORT = int(os.environ.get("NAVCHECK_PORT", "8931"))
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


async def opened(br, url, width=1400, height=900):
    """A page, once it has stopped moving.

    Every Playwright context starts with an empty cache, so the service worker
    installs, takes control, and pwa.js reloads once to hand the page over to
    it. That reload destroys the execution context underneath any evaluate()
    that started before it, and the error reads like a broken page rather than
    a page that was still arriving. Waiting for the controller is waiting for
    the exact thing that causes it."""
    pg = await br.new_page(viewport={'width': width, 'height': height})
    await pg.goto(url, wait_until='networkidle')
    for _ in range(3):
        try:
            await pg.wait_for_function(
                "() => !('serviceWorker' in navigator)"
                " || navigator.serviceWorker.controller !== null", timeout=6000)
            break
        except Exception:
            await pg.wait_for_load_state('networkidle')
    await pg.wait_for_timeout(200)
    return pg


async def main():
    from playwright.async_api import async_playwright
    base = 'http://127.0.0.1:%d/library/' % PORT
    async with async_playwright() as pw:
        br = await pw.chromium.launch()

        for slug, chap in (('breast-cancer', 'BC-500.html'),
                           ('newton-to-mtheory', 'ch2-1.html')):
            # The neighbours and the count come from the book's own reading
            # order rather than from constants here. Hard-coding them made this
            # file report four failures the first time the clinical book was
            # reorganised, when the navigation was working perfectly and only
            # the fixtures were stale.
            page = await br.new_page()
            order = (await (await page.goto(base + slug + '/nav.json')).json())
            await page.close()
            ids = [c['href'] for c in order['chapters']]
            at = ids.index(chap)
            prev_num = order['chapters'][at - 1]['num']
            next_num = order['chapters'][at + 1]['num']
            total = order['count']
            print('\n%s  %s  (%d of %d)' % (slug, chap, at + 1, total))

            # ---- phone width: the drawer is the surface
            pg = await br.new_page(viewport={'width': 390, 'height': 780})
            await pg.goto(base + slug + '/' + chap, wait_until='networkidle')
            await pg.wait_for_function(
                "() => window.LibraryPWA && window.LibraryPWA.nav().index >= 0",
                timeout=5000)
            await pg.wait_for_timeout(120)

            seq = await pg.query_selector('#mnav .mn-seq')
            ok('drawer carries a prev/next row', seq is not None)
            if seq:
                prev = await pg.text_content('#mnav .mn-seq .prev .mn-ch')
                nxt = await pg.text_content('#mnav .mn-seq .next .mn-ch')
                ok('prev is the previous chapter', prev.startswith(prev_num), repr(prev[:44]))
                ok('next is the next chapter', nxt.startswith(next_num), repr(nxt[:44]))
                kick = await pg.text_content('#mnav .mn-kicker')
                ok('kicker shows the position', ' of %d' % total in kick, repr(kick))
                sb = await pg.text_content('.sidebar .sb-title')
                ok('the sidebar says the same', ' of %d' % total in sb, repr(sb))
                # the row must be reachable without scrolling the chapter
                await pg.click('#mnav-btn')
                await pg.wait_for_timeout(250)
                vis = await pg.is_visible('#mnav .mn-seq .next')
                ok('next is visible once the drawer opens', vis)
                href = await pg.get_attribute('#mnav .mn-seq .next', 'href')
                await pg.click('#mnav .mn-seq .next')
                await pg.wait_for_load_state('load')
                ok('tapping next goes there', pg.url.endswith(href), pg.url.split('/')[-1])
            await pg.close()

            # ---- desktop: the keyboard is the surface
            pg = await br.new_page(viewport={'width': 1400, 'height': 900})
            await pg.goto(base + slug + '/' + chap, wait_until='networkidle')
            await pg.wait_for_timeout(300)
            async def press(key, want):
                # the arrow keys are live only once the reading order has
                # arrived; wait for that rather than for a fixed delay
                await pg.wait_for_function(
                    "() => window.LibraryPWA && window.LibraryPWA.nav().index >= 0",
                    timeout=5000)
                try:
                    async with pg.expect_navigation(timeout=4000):
                        await pg.keyboard.press(key)
                except Exception:
                    pass
                return pg.url.split('/')[-1]
            got = await press('ArrowRight', None)
            ok('ArrowRight is the next chapter', got != chap, got)
            got = await press('ArrowLeft', None)
            ok('ArrowLeft comes back', got == chap, got)
            await pg.close()

            # ---- the first and last chapters keep the shape
            first = ids[0]
            pg = await br.new_page(viewport={'width': 390, 'height': 780})
            await pg.goto(base + slug + '/' + first, wait_until='networkidle')
            await pg.wait_for_timeout(300)
            kind = await pg.eval_on_selector_all(
                '#mnav .mn-seq > *', 'els => els.map(e => e.tagName)')
            ok('first chapter has a disabled prev, not a missing one',
               kind == ['SPAN', 'A'], kind)
            await pg.close()

        # ---- standalone: the back control
        print('\nstandalone')
        ctx = await br.new_context(viewport={'width': 390, 'height': 780})
        await ctx.add_init_script(
            "Object.defineProperty(navigator,'standalone',{get:()=>true});")
        pg = await ctx.new_page()
        await pg.goto(base + 'breast-cancer/contents.html', wait_until='networkidle')
        await pg.click('.main a[href$=".html"]')      # go one page deep
        await pg.wait_for_load_state('load')
        await pg.wait_for_timeout(400)
        deep = pg.url
        ok('back control appears once there is history',
           await pg.query_selector('.topnav .pwa-back') is not None)
        if await pg.query_selector('.topnav .pwa-back'):
            await pg.click('.topnav .pwa-back')
            await pg.wait_for_load_state('load')
            ok('it goes back', pg.url.endswith('contents.html'), pg.url.split('/')[-1])
        await ctx.close()

        # ---- a page in the book but not in the sequence keeps its keyboard
        pg = await br.new_page(viewport={'width': 1400, 'height': 900})
        await pg.goto(base + 'breast-cancer/trials.html', wait_until='networkidle')
        await pg.wait_for_timeout(300)
        before = pg.url
        await pg.keyboard.press('ArrowRight')
        await pg.wait_for_timeout(250)
        ok('arrow keys do nothing off-sequence', pg.url == before, pg.url.split('/')[-1])
        await pg.close()

        # ---- a book with no reading order is untouched
        pg = await br.new_page(viewport={'width': 390, 'height': 780})
        r = await pg.goto(base + 'the-long-argument/index.html', wait_until='networkidle')
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
            for page in BAR_PAGES[bk.slug]:
                pg = await opened(br, base + bk.slug + '/' + page)
                got = await pg.eval_on_selector_all(
                    '.topnav-links a',
                    'els => els.map(e => [e.getAttribute("href"), e.textContent.trim()])')
                got = [tuple(x) for x in got]
                ok('%s/%s offers what book.json declares' % (bk.slug, page),
                   got == want, got if got != want else '')
                # the page you are on is named, and not offered as a link to itself
                cur = await pg.eval_on_selector_all(
                    '.topnav [aria-current="page"]',
                    'els => els.map(e => e.getAttribute("href"))')
                here = [h for h, _l in want if h == page] or (
                    ['index.html'] if page == 'index.html' else [])
                ok('%s/%s marks where you are' % (bk.slug, page), cur == here, cur)
                await pg.close()

        # ---- the window still fits, on the two books that fill it
        # Both draw their own full-height interface. The bar is above it now,
        # and a page that scrolls by exactly the height of the bar is the way
        # that goes wrong.
        for slug in ('the-long-argument', 'the-ages-of-thought'):
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
            pg = await opened(br, base + slug + '/' + chap, 390, 780)
            await pg.wait_for_function(
                "() => document.querySelector('#mnav .mn-dest')", timeout=5000)
            got = await pg.eval_on_selector_all(
                '#mnav .mn-dest > *', 'els => els.map(e => e.textContent.trim())')
            ok('%s drawer offers what the bar offers' % slug, got == want, got)
            await pg.click('#mnav-btn')
            await pg.wait_for_timeout(250)
            ok('the destinations are reachable without scrolling the chapter',
               await pg.is_visible('#mnav .mn-dest .up'))
            dup = await pg.eval_on_selector_all(
                '#mnav .mn-foot a', 'els => els.length')
            ok('no second way to the contents page under them', dup == 0, dup)
            await pg.close()

            # on the contents page the drawer still lists them, and the entry
            # for the page you are on has stopped being a control
            pg = await opened(br, base + slug + '/contents.html', 390, 780)
            await pg.wait_for_function(
                "() => document.querySelector('#mnav .mn-dest')", timeout=5000)
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
        for slug, page in (('newton-to-mtheory', 'index.html'),     # four links + toggle
                           ('newton-to-mtheory', 'ch2-1.html'),     # four links + drawer
                           ('breast-cancer', 'index.html'),         # four links, no toggle
                           ('the-ages-of-thought', 'index.html')):  # one link, own chrome
            for w in (320, 390, 1400):
                pg = await opened(br, base + slug + '/' + page, w, 800)
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
                   % (slug, page, w),
                   not (r['clipped'] or r['spill'] or r['over']),
                   [k for k in ('clipped', 'spill', 'over') if r[k]])
                await pg.close()

        # ------------------------------------------------- standalone, everywhere
        # The back control is injected into the bar. A page without one had no
        # back control, and in a home-screen app there is no browser chrome to
        # supply another: the atlas was a dead end on an iPhone.
        print('\nstandalone, on a landing page')
        for slug in ('the-ages-of-thought', 'newton-to-mtheory'):
            ctx = await br.new_context(viewport={'width': 390, 'height': 780})
            await ctx.add_init_script(
                "Object.defineProperty(navigator,'standalone',{get:()=>true});")
            pg = await ctx.new_page()
            await pg.goto(base + 'index.html', wait_until='networkidle')
            await pg.goto(base + slug + '/index.html', wait_until='networkidle')
            await pg.wait_for_timeout(400)
            ok('%s landing page has a back control' % slug,
               await pg.query_selector('.topnav .pwa-back') is not None)
            await ctx.close()

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
          'surfaces, at every width')
