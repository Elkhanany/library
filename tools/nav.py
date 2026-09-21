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
# index.html is the hub. It is the place the bar points back to, it is the
# start_url of the installed app, and it has no book to name; a bar there would
# be a link to itself.
#
# offline.html and continue.html are deliberately dependency-free -- no
# stylesheet, no script, no font to fetch. offline.html is what a reader sees
# when the network is gone and the page they asked for was never stored, so it
# has to render from its own bytes. A bar that needs a stylesheet would be the
# one piece of it that did not. Both already carry their own way back.
UNBARRED = ("index.html", "offline.html", "continue.html")


# ------------------------------------------------------------------- the bar

def bar(bk, here=None):
    """The book's bar, with the entry for `here` marked as the current page.

    `here` is a file name inside the book -- "contents.html", "BC-500.html" --
    or None on a page that is not in the book's directory. A chapter matches
    nothing and simply gets no mark.
    """
    def current(href):
        return ' aria-current="page"' if here and href == here else ""

    links = []
    for item in bk.nav_items():
        cls = ' class="up"' if item["key"] == "library" else ""
        links.append('<a%s href="%s"%s>%s</a>'
                     % (cls, item["href"], current(item["href"]),
                        html.escape(item["label"])))
    cls, name = brand(bk)
    return ('<nav class="topnav" aria-label="Site">\n'
            '  <a class="%s" href="index.html"%s>%s</a>\n'
            '  <div class="topnav-links">\n'
            '    %s\n'
            '  </div>\n'
            '</nav>' % (cls, current("index.html"), name, "\n    ".join(links)))


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
    text = text.replace(HEAD_END,
                        CSS_OPEN + "\n" + stylesheet(depth) + "\n" + CSS_CLOSE
                        + "\n" + HEAD_END, 1)
    return text.replace(BODY,
                        BODY + "\n" + OPEN + "\n" + bar(bk, here) + "\n" + CLOSE, 1)


def pages(by_slug):
    """Every page that gets a bar, with the book it belongs to.

    Yields (path, rel, book, here, depth). A page in docs/<slug>/ belongs to
    that book; nothing else in the tree does, which is why the hub and the two
    static pages fall out here rather than needing a rule of their own.
    """
    for dp, _dirs, fs in os.walk(DOCS):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if rel in UNBARRED:
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
