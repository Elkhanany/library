#!/usr/bin/env python3
"""
One navigation bar, on every page of the site, from one producer.

    python3 tools/nav.py            # harmonise docs/
    python3 tools/nav.py --check    # assert docs/ already is

WHAT WAS WRONG

webbuild.py built a top bar for the pages it rendered through Chromium, and
every other page in the library carried whatever its author had written by
hand. There were five bars:

  * the generated one, on chapters, contents, the ledger and the through-line
  * a hand-written copy on the clinical book's landing page, which had gone
    stale -- Stories had been added to the book and never to that copy
  * a second hand-written copy on each of that book's two appendices, correct
    by luck rather than by construction
  * a bespoke strip on the timeline, and a logo inside the atlas's own header
  * nothing at all on the physics book's landing page

So a reader could reach In Plain Terms from the physics book's contents page
and not from its front door, and the trial registry from three pages of the
clinical book and not from the fourth. That is the complaint this file answers:
the same links, on every page, in the same place.

WHY A TEXT PASS

The same reason pwa.py is one. A full webbuild renders every chapter through
headless Chromium at 2.4 seconds a page and rewrites figure coordinates when
Chromium moves, so it costs a quarter of an hour and forty megabytes of diff.
Changing a label in a navigation bar must not cost that. Nothing here opens a
chapter body: it reads the few hundred bytes around <body> and around </head>,
and it runs in about a second on the standard library alone.

Nothing here may import webbuild, build, playwright or asyncio.

THE TWO ANCHORS

The bar goes immediately after <body>, and the stylesheet link immediately
before </head>. Both are deliberately not the anchor pwa.py uses: the two
injectors then commute, and running either one twice, or both in either order,
gives the same bytes. Each raises rather than patching nothing if its anchor is
ever missing, which is the likeliest silent failure here -- a bar that quietly
stops being emitted looks exactly like a build that has not run yet.
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

DOCS = library.DOCS

# The injected blocks, delimited so each can be found and replaced whole.
OPEN, CLOSE = "<!--NAV-->", "<!--/NAV-->"
CSS_OPEN, CSS_CLOSE = "<!--NAVCSS-->", "<!--/NAVCSS-->"

BODY = "<body>"
HEAD_END = "</head>"

# Library-level pages that carry no bar, and why.
#
# offline.html and continue.html are deliberately dependency-free -- no
# stylesheet, no script, no font to fetch. offline.html is what a reader sees
# when the network is gone and the page they asked for was never stored, so it
# has to render from its own bytes. A bar that needs a stylesheet would be the
# one piece of it that did not. Both already carry their own way back.
#
# The hub is barred. It used to be left out as the page the bar points back to,
# which also left it the one page in the library with no theme control (NAV-02):
# its bar is the brand "A Library", marked as the current page, and the theme
# button.
UNBARRED = ("offline.html", "continue.html")

# The theme button's glyph: a circle half-filled with currentColor, the same
# everywhere (DESIGN.md section 4). Decorative; the button carries the label.
THEME_ICON = ('<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" '
              'focusable="false"><circle cx="10" cy="10" r="7.25" fill="none" '
              'stroke="currentColor" stroke-width="1.5"/><path d="M10 2.75a7.25 '
              '7.25 0 0 1 0 14.5z" fill="currentColor"/></svg>')


# ------------------------------------------------------------------- the bar

def bar(bk, here=None, target=False):
    """The library bar for one page, with the entry for `here` marked as the
    current page (DESIGN.md section 6, "The library bar").

    `bk` is the book the page belongs to, or None for the hub. `here` is a file
    name inside the book -- "contents.html", "BC-500.html" -- or the hub's
    "index.html". A chapter matches nothing and simply gets no mark.

    The skip link comes first, so it is the first Tab stop on every page. Then
    the brand; the Menu button, which folds the book's destinations under one
    control at 640px and below, and only exists where there are destinations
    to fold; the destinations; Library, the way out, outside the fold so it
    never costs a tap; and the theme button, last on every page.

    Both buttons ship hidden. pwa.js wires them and removes the attribute, and
    nav.css reserves their slots meanwhile under html.js, so nothing moves when
    the script arrives. A page whose shell predates this file never shows a
    dead button, because the browser hides [hidden] on its own.

    `target` adds the skip link's target just after the bar, for a page whose
    own markup does not yet name its text with id="text". Without it the link
    would point at nothing on every such page, with scripts or without. pwa.js
    moves the id onto the page's own main, .main, .app or .hero when there is
    one, so on a chapter the skip also passes the sidebar.
    """
    def current(href):
        return ' aria-current="page"' if here and href == here else ""

    theme = ('  <button class="nav-theme" type="button" aria-pressed="false" '
             'aria-label="Dark theme" title="Switch to dark" hidden>%s</button>\n'
             % THEME_ICON)
    skip = '<a class="skip" href="#text">Skip to text</a>\n'
    after = ('\n<span class="skip-target" id="text" tabindex="-1"></span>'
             if target else '')

    if bk is None:
        return (skip + '<nav class="topnav" aria-label="Library">\n'
                '  <a class="nav-brand" href="index.html"%s>A Library</a>\n'
                '%s</nav>%s' % (current("index.html"), theme, after))

    dest, up = [], None
    for item in bk.nav_items():
        if item["key"] == "library":
            up = '  <a class="up" href="%s">%s</a>\n' % (item["href"],
                                                        html.escape(item["label"]))
            continue
        dest.append('<a href="%s"%s>%s</a>'
                    % (item["href"], current(item["href"]), html.escape(item["label"])))
    cls, name = brand(bk)
    out = [skip,
           '<nav class="topnav" aria-label="Library" data-book="%s">\n' % bk.slug,
           '  <a class="%s" href="index.html"%s>%s</a>\n' % (cls, current("index.html"), name)]
    # No destinations besides Library -- the atlas and the timeline -- means no
    # Menu and no empty group: an empty .topnav-links drew the divider before
    # Library with nothing on its other side (NAV-10, FD-15).
    if dest:
        out.append('  <button class="nav-menu" type="button" aria-expanded="false" '
                   'aria-controls="nav-dest" hidden>Menu</button>\n')
        out.append('  <div class="topnav-links" id="nav-dest">\n    %s\n  </div>\n'
                   % "\n    ".join(dest))
    out.append(up or "")
    out.append(theme)
    out.append('</nav>')
    out.append(after)
    return "".join(out)


def brand(bk):
    """The book's name at the head of the bar, as (class, markup).

    A book already declares a short name for the home screen, where iOS elides
    at about twelve characters. A 390px bar carrying four links has about the
    same room, so the bar uses that string rather than cutting the long one:
    "Newton -> M-Theory" becomes "Newton->M" and not "Newton ->...". A book
    whose name is already short gets one span and no rule, which is most of
    them.
    """
    short = bk.short_name
    if library.plain(bk.brand) == library.plain(short):
        return "nav-brand", bk.brand
    return ("nav-brand two",
            '<span class="nav-full">%s</span><span class="nav-short">%s</span>'
            % (bk.brand, html.escape(short)))


def stylesheet(depth):
    """depth 1 is a page inside a book's directory; docs/ nests no deeper."""
    return '<link rel="stylesheet" href="%sassets/nav.css">' % ("../" * depth)


# --------------------------------------------------------------- the injector

# The bars this replaces. A page built before this file existed carries its bar
# raw, and the hand-written pages carried theirs in the source; both have to go,
# or harmonising the site would mean two bars on half of it. Kept rather than
# retired once the sources are clean: it is what makes the pass idempotent over
# a docs/ built by any earlier version of the build.
LEGACY = (re.compile(r'<nav class="topnav"[^>]*>.*?</nav>\s*', re.S),
          re.compile(r'<nav class="libbar"[^>]*>.*?</nav>\s*', re.S))


def strip(text):
    """The inverse of inject(), for --check and for re-deriving a page."""
    text = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE) + r"\n?", "",
                  text, flags=re.S)
    text = re.sub(re.escape(CSS_OPEN) + r".*?" + re.escape(CSS_CLOSE) + r"\n?", "",
                  text, flags=re.S)
    for pat in LEGACY:            # only ever outside the block, stripped above
        text = pat.sub("", text)
    return text


def inject(text, bk, here, depth):
    for anchor, n in ((BODY, text.count(BODY)), (HEAD_END, text.count(HEAD_END))):
        if n != 1:
            raise SystemExit("nav: anchor %s found %d times, expected exactly 1"
                             % (anchor, n))
    # The page names its own text once its shell does (<main id="text">);
    # until then the bar brings a target of its own.
    target = not re.search(r'(?<![\w-])id="text"', text)
    text = text.replace(HEAD_END,
                        CSS_OPEN + "\n" + stylesheet(depth) + "\n" + CSS_CLOSE
                        + "\n" + HEAD_END, 1)
    return text.replace(BODY,
                        BODY + "\n" + OPEN + "\n" + bar(bk, here, target) + "\n" + CLOSE, 1)


def pages(by_slug):
    """Every page that gets a bar, with the book it belongs to.

    Yields (path, rel, book, here, depth). A page in docs/<slug>/ belongs to
    that book, and the hub, docs/index.html, gets the library's own bar with
    book None. Nothing else in the tree is a page a reader lands on.
    """
    for dp, _dirs, fs in os.walk(DOCS):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if rel in UNBARRED:
                continue
            if rel == "index.html":
                yield p, rel, None, "index.html", 0
                continue
            head, _, name = rel.rpartition("/")
            bk = by_slug.get(head)
            if bk is None:
                continue
            yield p, rel, bk, name, rel.count("/")


def emit_all(books=None):
    bks = books if books is not None else library.books()
    by_slug = {b.slug: b for b in bks}

    src = os.path.join(library.ASSETS, "nav.css")
    library.write(os.path.join(DOCS, "assets", "nav.css"), library.read(src))

    n = 0
    for p, _rel, bk, here, depth in pages(by_slug):
        library.write(p, inject(strip(library.read(p)), bk, here, depth))
        n += 1
    return n


def check():
    """Assert that what is on disk is what this module would emit now.

    A stale bar is silent. It goes on linking pages that still exist and simply
    fails to offer the one that was added, which is how the clinical book's
    landing page came to be missing Stories for as long as it did. Nothing about
    the page looks wrong; there is only something absent. So this belongs in CI
    rather than in a note asking people to remember.
    """
    bks = library.books()
    by_slug = {b.slug: b for b in bks}
    bad = []
    for p, rel, bk, here, depth in pages(by_slug):
        text = library.read(p)
        if inject(strip(text), bk, here, depth) != text:
            bad.append(rel)
    css = os.path.join(DOCS, "assets", "nav.css")
    if not os.path.exists(css):
        bad.append("assets/nav.css (missing)")
    elif library.read(css) != library.read(os.path.join(library.ASSETS, "nav.css")):
        bad.append("assets/nav.css (stale)")
    if bad:
        print("nav: %d page(s) do not match what nav.py would emit:" % len(bad))
        for rel in bad[:12]:
            print("   ", rel)
        print("    run: python3 tools/nav.py")
        return 1
    n = sum(1 for _ in pages(by_slug))
    print("nav: %d pages, one bar each, from %d books' book.json"
          % (n, len(bks)))
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        raise SystemExit(check())
    if not os.path.isdir(DOCS):
        raise SystemExit("nav: no docs/ to harmonise. Run tools/webbuild.py first.")
    n = emit_all()
    for b in library.books():
        print("  %-20s %s" % (b.slug,
                              " · ".join(i["label"] for i in b.nav_items())))
    print("nav: %d pages carry the same bar" % n)
