#!/usr/bin/env python3
"""
Emit the progressive-web-app layer over an already-built docs/.

This is a sibling of webbuild.py, not a flag on it, and the separation is the
point. webbuild.py imports Playwright at module scope and build_book() renders
every chapter through Chromium at 2.4 seconds a page: a full run is a quarter of
an hour, and it rewrites figure SVG coordinates whenever the Chromium version
moves, so a rebuild churns forty megabytes of diff that has nothing to do with
the change. Adding a meta tag must not cost that. Everything here is a pure-text
pass over the bytes already in docs/ -- it opens no chapter body, only the few
hundred bytes inside <head> -- so it runs in about a second with nothing but the
standard library:

    python3 tools/pwa.py

webbuild.py calls emit_all() at the end of a full build, so both paths produce
the same bytes from one producer. verify.py re-derives every head block and
diffs it against what is on disk, which is what stops the two paths drifting.

Nothing here may import webbuild, build, playwright or asyncio.
"""
import io
import json
import os
import re
import struct
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

DOCS = library.DOCS

# The injected block is delimited so it can be found and replaced whole. Every
# emitted page carries exactly one.
OPEN, CLOSE = "<!--PWA-->", "<!--/PWA-->"

# The anchor. Both spellings are accepted so the injector works on a tree built
# before viewport-fit was added and on one built after.
VP_OLD = '<meta name="viewport" content="width=device-width,initial-scale=1">'
VP_NEW = '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'

# Icon sizes. 180 is the only one iOS actually reads for the home screen; 192
# and 512 are the manifest's, and the maskable variant carries extra inset for
# Android's circular mask. 32 is the browser tab, library-level only.
SIZES = [180, 192, 512]


# ---------------------------------------------------------------- writing bytes

def write_bytes(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "wb") as fh:
        fh.write(data)


def write_json(path, obj):
    """Sorted and indented, so two machines building the same source produce
    identical bytes and docs/ does not churn. Same reasoning as library.write."""
    library.write(path, json.dumps(obj, indent=2, sort_keys=True,
                                   ensure_ascii=False) + "\n")


# ------------------------------------------------------------------------ icons
#
# There is no Pillow, no cairosvg and no ImageMagick in the build environment,
# and the Chromium that Playwright expects is not reliably present either. A PNG
# is not hard to write by hand, though: a header, one zlib stream of filtered
# scanlines, and a CRC per chunk. That is the whole format for our purposes, and
# doing it arithmetically means the bytes are identical on every machine, which
# a browser screenshot would not be.
#
# No font rasteriser comes with that, so the mark is geometric rather than a
# monogram. That is the right answer anyway: iOS composites home-screen icons
# through its own mask and, on recent versions, through tinted and dark
# appearances, and a flat high-contrast shape survives all of it where thin
# lettering does not.


def _chunk(tag, data):
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))


def png(path, size, pixel):
    """Colour type 2: 8-bit truecolour, no alpha channel at all.

    Deliberate. iOS composites a transparent pixel in a home-screen icon against
    black, so an icon with alpha gets a black fringe or a black ground on the
    one surface that matters most. Every pixel here is opaque."""
    rows = bytearray()
    for y in range(size):
        rows.append(0)                      # filter type 0, once per scanline
        for x in range(size):
            r, g, b = pixel(x, y)
            rows += bytes((r, g, b))
    data = (b"\x89PNG\r\n\x1a\n"
            + _chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
            + _chunk(b"IDAT", zlib.compress(bytes(rows), 9))
            + _chunk(b"IEND", b""))
    write_bytes(path, data)


def _rgb(hexcolour, default=(0, 0, 0)):
    h = (hexcolour or "").lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return default
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return default


def _mark(slug, bg, fg, inset, size, ss=3):
    """Three stacked bars on a solid ground -- a shelf seen end-on.

    The bar widths are permuted from a hash of the slug, so every book's mark is
    recognisably from the same family and still distinguishable at 60 pixels on
    a home screen. Supersampled ss times per axis and averaged, which is how the
    edges get antialiased without a rasteriser."""
    widths = [1.0, 0.72, 0.88]
    k = sum(ord(c) for c in slug) % 3
    widths = widths[k:] + widths[:k]

    pad = inset * size
    inner = size - 2 * pad
    gap = inner * 0.14
    bar = (inner - 2 * gap) / 3.0

    bands = []
    for i, w in enumerate(widths):
        top = pad + i * (bar + gap)
        bands.append((top, top + bar, pad, pad + inner * w))

    def pixel(x, y):
        hit = 0
        for sy in range(ss):
            fy = y + (sy + 0.5) / ss
            for sx in range(ss):
                fx = x + (sx + 0.5) / ss
                for t, b, l, r in bands:
                    if t <= fy < b and l <= fx < r:
                        hit += 1
                        break
        if hit == 0:
            return bg
        if hit == ss * ss:
            return fg
        a = hit / float(ss * ss)
        return tuple(int(round(bg[i] + (fg[i] - bg[i]) * a)) for i in range(3))

    return pixel


def icon_entries():
    """The manifest's icons array. At least one entry carries no purpose: a set
    that is entirely maskable can leave a browser with nothing it considers
    usable."""
    return ([{"src": "icons/icon-%d.png" % s, "sizes": "%dx%d" % (s, s),
              "type": "image/png"} for s in (192, 512)]
            + [{"src": "icons/icon-512-maskable.png", "sizes": "512x512",
                "type": "image/png", "purpose": "maskable"}])


def emit_icons(outdir, slug, bg, fg):
    bg, fg = _rgb(bg, (40, 40, 40)), _rgb(fg, (255, 255, 255))
    for s in SIZES:
        png(os.path.join(outdir, "icon-%d.png" % s), s,
            _mark(slug, bg, fg, 0.20, s))
    png(os.path.join(outdir, "icon-512-maskable.png"), 512,
        _mark(slug, bg, fg, 0.28, 512))


# ------------------------------------------------------------------- the <head>

# apple-mobile-web-app-capable is what iOS reads, and what Safari falls back to
# when a manifest fails to load. mobile-web-app-capable is the standard spelling
# and exists here only to stop linters flagging the Apple one as deprecated.
# Both are needed. Deleting the Apple tag to satisfy a linter is a known way to
# break installation on iOS -- do not "clean this up".
CAPABLE = ('<meta name="apple-mobile-web-app-capable" content="yes">\n'
           '<meta name="mobile-web-app-capable" content="yes">')

# black-translucent is not used. It is deprecated in WebKit, reported broken on
# recent iOS, and its whole purpose was to let content run under the status bar
# -- which every header here would have to be rebuilt around. With "default",
# iOS reserves the strip, env(safe-area-inset-top) reports what it reserved, and
# the layout is correct whichever way iOS decides to behave.
STATUSBAR = '<meta name="apple-mobile-web-app-status-bar-style" content="default">'

# Runs before first paint, blocking, and deliberately tiny. book.js is loaded at
# the end of the body, so a dark-mode reader gets a white flash on every single
# page before the theme is stamped. Chrome-less and launched from a dark
# background that flash is the ugliest thing in the app, and it is most of what
# a splash screen would have been hiding.
#
# Standalone is detected in JS rather than with @media (display-mode:standalone),
# which is unreliable on iOS; navigator.standalone is the signal that works, so
# every standalone-only rule keys off html.standalone.
BOOT = (
    "<script>"
    "try{var s=JSON.parse(localStorage.getItem('library:v1')||'{}');"
    "var t=s.theme||localStorage.getItem('nmt-theme')||'';}catch(e){var t='';}"
    "if(!t)t=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';"
    "document.documentElement.setAttribute('data-theme',t);"
    "if(navigator.standalone===true||matchMedia('(display-mode:standalone)').matches)"
    "document.documentElement.classList.add('standalone');"
    "</script>")


def head(bk, depth):
    """The exact block injected into one page.

    depth 0 is the hub at docs/index.html; depth 1 is any page inside a book's
    directory. docs/ nests no deeper than that, so one relative prefix is right
    for a chapter, the contents page, the ledger and the book's landing page
    alike. Both callers -- this injector and webbuild's SHELL -- use this same
    return value, so the two paths cannot disagree."""
    up = "../" * depth
    if bk is None:
        # The hub has no theme toggle: its dark mode is purely a media query, so
        # the browser picks the bar colour with the media attribute rather than
        # anything JavaScript has to keep in sync.
        theme = ('<meta name="theme-color" content="#f4f3f0" media="(prefers-color-scheme:light)">\n'
                 '<meta name="theme-color" content="#101216" media="(prefers-color-scheme:dark)">')
        title, icons = "Library", "icons/"
    else:
        theme = '<meta name="theme-color" content="%s">' % bk.theme_color
        title, icons = bk.short_name, "icons/"

    return "\n".join([
        '<link rel="manifest" href="manifest.webmanifest">',
        '<link rel="stylesheet" href="%sassets/pwa.css">' % up,
        '<link rel="apple-touch-icon" href="%sicon-180.png">' % icons,
        '<link rel="icon" type="image/png" sizes="32x32" href="%sicons/icon-32.png">' % up,
        CAPABLE,
        STATUSBAR,
        '<meta name="apple-mobile-web-app-title" content="%s">' % title,
        theme,
        BOOT,
        '<script src="%sassets/pwa.js" defer></script>' % up,
    ])


def inject(text, block):
    """Idempotent, anchored on the viewport meta, and loud when it cannot find it.

    The raise is not decoration. If anyone reformats that meta string in any of
    the emitters, a silent injector would patch zero files and the whole layer
    would quietly stop existing -- much the likeliest silent failure here."""
    text = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE) + r"\n?", "",
                  text, flags=re.S)
    n = text.count(VP_OLD) + text.count(VP_NEW)
    if n != 1:
        raise SystemExit("pwa: viewport anchor found %d times, expected exactly 1" % n)
    anchor = VP_OLD if VP_OLD in text else VP_NEW
    return text.replace(anchor, VP_NEW + "\n" + OPEN + "\n" + block + "\n" + CLOSE, 1)


def strip(text):
    """The inverse, for verify.py."""
    return re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE) + r"\n?", "",
                  text, flags=re.S)


# ----------------------------------------------------------------- the manifest

def library_manifest():
    return {
        "id": library.SITE,
        "name": "A Library",
        "short_name": "Library",
        "description": "Books built from first principles.",
        "lang": "en", "dir": "ltr",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "display_override": ["standalone"],
        "theme_color": "#f4f3f0",
        "background_color": "#f4f3f0",
        "categories": ["education", "books"],
        "icons": icon_entries(),
        "shortcuts": ([{"name": "Continue reading", "url": "continue.html"}]
                      + [{"name": b.app_name, "url": b.slug + "/index.html"}
                         for b in library.books()]),
    }


# ------------------------------------------------------- what a book is made of

# The layer's own outputs are excluded from a book's file list. Without this the
# digest chases its own tail: writing offline.json changes the book's bytes,
# which changes the digest, which changes offline.json. The icons and the
# manifest are shell-cached anyway.
SELF = ("manifest.webmanifest", "offline.json")


def book_files(slug):
    """Every file a reader needs for this book, DOCS-relative, sorted.

    Derived by walking docs/ rather than accumulated during a build, so the
    full-build path and the standalone path cannot disagree about what a book
    contains -- and so the layer stays correct for a book whose chapters were
    rendered in some earlier run and are only sitting in git, which at fifteen
    minutes a rebuild is the normal case."""
    root = os.path.join(DOCS, slug)
    out = []
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if os.path.basename(rel) in SELF:
                continue
            if "/icons/" in rel:
                continue
            out.append(rel)
    return sorted(out)


def filehash(path):
    import hashlib
    h = hashlib.sha256()
    with io.open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()[:8]


def digest(rels):
    """One short hash over a set of files, by path and content both, so a rename
    counts as a change."""
    import hashlib
    h = hashlib.sha256()
    for rel in sorted(rels):
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(filehash(os.path.join(DOCS, rel)).encode("ascii"))
        h.update(b"\0")
    return h.hexdigest()[:12]


def offline_json(bk):
    """Per-file revisions, not one hash for the book.

    A book's cache is named for the book and never for its contents. Hash-naming
    the cache would mean a one-word typo fix in one chapter orphans and deletes
    a reader's entire sixty-five megabyte download; with per-file revisions the
    same fix costs one two-megabyte fetch. At two books that is a nicety. At
    twenty, with something changing most weeks, it is the difference between a
    feature people keep switched on and one they turn off."""
    import gzip
    rels = book_files(bk.slug)
    files = {}
    total = 0
    wire = 0
    for rel in rels:
        p = os.path.join(DOCS, rel)
        files[rel] = filehash(p)
        total += os.path.getsize(p)
        # What it costs to fetch, as opposed to what it costs to keep. These
        # differ by more than tenfold here -- the chapters are pre-rendered
        # markup and compress to about 8% -- and a reader deciding whether to
        # download a book on a phone deserves to be told both rather than
        # whichever number flatters the feature.
        with io.open(p, "rb") as fh:
            wire += len(gzip.compress(fh.read(), 6))
    return {"slug": bk.slug, "digest": digest(rels), "bytes": total,
            "wire": wire, "count": len(rels), "files": files}


def shell_files():
    """Library-level files only: the hub, the manifest, the client, the icons,
    the two static pages. Deliberately O(1) in the number of books -- putting
    every book's landing page and stylesheet in here would make the install cost
    grow with the shelf, and charge a reader for twenty books to open one."""
    out = ["index.html", "manifest.webmanifest", "offline.html",
           "continue.html", "catalog.json", "assets/pwa.js", "assets/pwa.css"]
    icons = os.path.join(DOCS, "icons")
    if os.path.isdir(icons):
        out += ["icons/" + f for f in sorted(os.listdir(icons))]
    return [p for p in out if os.path.exists(os.path.join(DOCS, p))]


# --------------------------------------------------------------- static pages

# Both are deliberately dependency-free: no stylesheet, no script, no font that
# has to be fetched. offline.html is what a reader sees when the network is gone
# and the page they asked for was never stored, so it must render from its own
# bytes alone -- a fallback that needs a fetch to look right is not a fallback.

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s</title>
<style>
:root{color-scheme:light dark;--ink:#16181d;--soft:#565b66;--paper:#f4f3f0;--rule:#dcdfe5}
@media (prefers-color-scheme:dark){
  :root{--ink:#e6e6e2;--soft:#a9adb6;--paper:#101216;--rule:#31353d}}
html,body{margin:0;height:100%%}
body{background:var(--paper);color:var(--ink);display:grid;place-items:center;
  padding:max(24px,env(safe-area-inset-top)) 24px max(24px,env(safe-area-inset-bottom));
  font-family:"Iowan Old Style",Palatino,Georgia,serif;-webkit-text-size-adjust:100%%}
main{max-width:26rem;text-align:center}
h1{font-size:1.5rem;font-weight:600;margin:0 0 .6rem}
p{color:var(--soft);line-height:1.6;margin:0 0 1.4rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:14px}
a,button{display:inline-block;font:inherit;font-size:14px;font-family:-apple-system,sans-serif;
  padding:11px 16px;min-height:44px;box-sizing:border-box;border:1px solid var(--rule);
  border-radius:9px;background:none;color:inherit;text-decoration:none;cursor:pointer}
ul{list-style:none;padding:0;margin:0;text-align:left}
li{border-top:1px solid var(--rule)}
li a{display:block;border:0;border-radius:0;padding:14px 2px}
</style>
</head>
<body>
<main>
%(body)s
</main>
%(script)s
</body>
</html>
"""


def emit_pages(bks):
    library.write(os.path.join(DOCS, "offline.html"), PAGE % {
        "title": "Offline — A Library",
        "body": ("<h1>Not stored on this device</h1>"
                 "<p>You are offline, and this page was never downloaded. "
                 "Books you have downloaded are still readable in full.</p>"
                 '<a href="./">The library</a>'),
        "script": ""})

    # continue.html is the target of the manifest shortcut and of the hub's
    # Continue button. It reads the position the client runtime records and
    # redirects, so the shortcut is a real "carry on where I was" rather than a
    # second copy of the shelf.
    library.write(os.path.join(DOCS, "continue.html"), PAGE % {
        "title": "Continue reading",
        "body": ('<h1>Continue reading</h1>'
                 '<p id="m">Looking for where you left off\u2026</p>'
                 '<ul id="l"></ul>'),
        "script": """<script>
(function(){
  var want=new URLSearchParams(location.search).get('b');
  var s={};try{s=JSON.parse(localStorage.getItem('library:v1')||'{}')}catch(e){}
  var last=s.last;
  if(last&&last.url&&(!want||last.slug===want)){location.replace(last.url);return}
  // Nothing recorded, or recorded for a different book: offer the shelf rather
  // than dead-ending on a shortcut the reader deliberately tapped.
  document.getElementById('m').textContent=
    'Nothing recorded yet. Pick up a book and this will remember your place.';
  // Built with DOM calls rather than by concatenating markup: a book title is
  // author-supplied text, and an href assembled in a string is also something
  // sitecheck would try to resolve as a real link.
  fetch('catalog.json').then(function(r){return r.json()}).then(function(c){
    var ul=document.getElementById('l');
    (c.books||[]).forEach(function(b){
      var li=document.createElement('li'), a=document.createElement('a');
      a.setAttribute('href',b.start); a.textContent=b.name;
      li.appendChild(a); ul.appendChild(li);
    });
  }).catch(function(){});
})();
</script>"""})


# ------------------------------------------------------------------ the emitter

def owning_book(rel, by_slug):
    head_dir = rel.split("/")[0]
    return by_slug.get(head_dir)


def emit_all(books=None):
    bks = books if books is not None else library.books()
    by_slug = {b.slug: b for b in bks}

    # 1. assets and icons, before anything hashes them
    for name in ("pwa.js", "pwa.css"):
        src = os.path.join(library.ASSETS, name)
        if os.path.exists(src):
            library.write(os.path.join(DOCS, "assets", name), library.read(src))
    emit_icons(os.path.join(DOCS, "icons"), "library", "#1b1b1d", "#f4f3f0")
    png(os.path.join(DOCS, "icons", "icon-32.png"), 32,
        _mark("library", _rgb("#1b1b1d"), _rgb("#f4f3f0"), 0.16, 32))
    for b in bks:
        emit_icons(os.path.join(DOCS, b.slug, "icons"), b.slug,
                   b.icon_spec["bg"], b.icon_spec["fg"])

    # 2. the two static pages, then manifests and the catalogue
    emit_pages(bks)
    # 2. manifests and the catalogue
    write_json(os.path.join(DOCS, "manifest.webmanifest"), library_manifest())
    for b in bks:
        write_json(os.path.join(DOCS, b.slug, "manifest.webmanifest"),
                   b.manifest(icon_entries()))
    write_json(os.path.join(DOCS, "catalog.json"), {
        "site": library.SITE,
        "books": [{"slug": b.slug, "name": b.app_name, "short_name": b.short_name,
                   "accent": b.theme.get("accent"), "theme_color": b.theme_color,
                   "start": b.slug + "/index.html"} for b in bks]})

    # 3. inject the head block into every built page
    pages = 0
    for dp, _, fs in os.walk(DOCS):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if rel in ("offline.html", "continue.html"):
                continue
            depth = rel.count("/")
            bk = owning_book(rel, by_slug) if depth else None
            library.write(p, inject(library.read(p), head(bk, depth)))
            pages += 1

    # 4. per-book manifests of what to download -- after step 3, so the recorded
    #    hashes describe the files as injected rather than as they were before
    for b in bks:
        write_json(os.path.join(DOCS, b.slug, "offline.json"), offline_json(b))

    # 5. the worker last of all, since it carries the shell's digest
    emit_sw(bks)
    return pages


def emit_sw(bks):
    src = os.path.join(library.ASSETS, "sw.js")
    if not os.path.exists(src):
        return
    shell = shell_files()
    # How many casually-visited pages of a book to keep when the reader has not
    # deliberately downloaded it. A book that is one file cannot be trimmed to
    # fewer than one, so it is marked 0, meaning never trim.
    casual = {}
    for b in bks:
        pages = [f for f in book_files(b.slug) if f.endswith(".html")]
        casual[b.slug] = 12 if len(pages) > 20 else 0
    hdr = ("/* Generated by tools/pwa.py from shared/assets/sw.js.\n"
           "   Do not edit docs/sw.js by hand -- the next build overwrites it.\n"
           "   BUILD is a content digest of the shell file set, so a deploy that\n"
           "   changes nothing produces the same worker and no reader is asked to\n"
           "   reload for a build that would give them identical bytes. */\n"
           "const BUILD  = %s;\n"
           "const FILES  = %s;\n"
           "const SLUGS  = %s;\n"
           "const CASUAL = %s;\n\n" % (
               json.dumps(digest(shell)),
               json.dumps(shell, indent=2),
               json.dumps([b.slug for b in bks]),
               json.dumps(casual, sort_keys=True)))
    library.write(os.path.join(DOCS, "sw.js"), hdr + library.read(src))


def check():
    """Assert that what is on disk is what this module would emit now.

    The whole layer rests on one string match. If anyone reformats the viewport
    meta in any emitter, or a page is written by a path that does not run the
    injector, the failure is silent -- the tags simply stop being there and the
    site quietly stops being installable. This is what makes that loud, so it
    belongs in CI and in verify.py rather than in a comment asking people to
    remember."""
    bks = library.books()
    by_slug = {b.slug: b for b in bks}
    bad = []
    for dp, _, fs in os.walk(DOCS):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if rel in ("offline.html", "continue.html"):
                continue
            text = library.read(p)
            depth = rel.count("/")
            want = inject(strip(text), head(owning_book(rel, by_slug) if depth else None,
                                            depth))
            if want != text:
                bad.append(rel)
    for rel in ("manifest.webmanifest", "catalog.json", "sw.js",
                "assets/pwa.js", "assets/pwa.css"):
        if not os.path.exists(os.path.join(DOCS, rel)):
            bad.append(rel + " (missing)")
    for b in bks:
        for rel in ("%s/manifest.webmanifest" % b.slug, "%s/offline.json" % b.slug,
                    "%s/icons/icon-180.png" % b.slug):
            if not os.path.exists(os.path.join(DOCS, rel)):
                bad.append(rel + " (missing)")
    if bad:
        print("pwa: %d page(s) do not match what pwa.py would emit:" % len(bad))
        for r in bad[:12]:
            print("   ", r)
        print("    run: python3 tools/pwa.py")
        return 1
    print("pwa: every built page carries the current app-layer head; "
          "manifests, worker and icons all present")
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        raise SystemExit(check())
    n = emit_all()
    print("pwa: %d pages injected, %d books, shell of %d files"
          % (n, len(library.books()), len(shell_files())))
