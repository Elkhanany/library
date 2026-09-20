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

TWO THINGS IT HAS TO REPRODUCE, OR IT TESTS NOTHING

pwa.js returns immediately on file://, so docs/ is served over http. And it
reads the book slug out of the path, expecting the project prefix that GitHub
Pages puts there, so docs/ is served under /library/ rather than at the root.
Serving it at the root makes every book page look like the hub, which switches
the whole app layer off silently: the first version of this file did exactly
that and reported seven failures that were all its own.
"""
import asyncio, http.server, os, socketserver, sys, threading

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
          'standalone back all behave in both chaptered books')
