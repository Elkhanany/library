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
import html
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

# The library-level pages written whole by emit_pages(). Each is self-contained
# (see PAGE), so none takes the injected head or nav.py's bar, and two of them
# are served at addresses that are not their own.
STATIC = ("offline.html", "continue.html", "404.html")

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
#
# THE THEME (DESIGN.md section 4). This is the one place a page's theme is
# decided, before first paint, in this order:
#   1. library:v1.look -- written only when the reader presses the bar's theme
#      button (pwa.js) or the fallback toggle (book.js);
#   2. nmt-theme -- the older key, which was also only ever written by a press;
#   3. the OS setting.
# library:v1.theme is never read. pwa.js used to write it passively on every
# page load, so the first light page an OS-dark reader opened pinned the whole
# library to light for good (NAV-02, PDA-01).
#
# It also adds "js" to <html>, which nav.css keys on to reserve the slots of the
# bar's two buttons before pwa.js un-hides them, so nothing in the bar moves
# when the script arrives.
THEME_JS = (
    "var t='';"
    "try{t=JSON.parse(localStorage.getItem('library:v1')||'{}').look||"
    "localStorage.getItem('nmt-theme')||''}catch(e){}"
    "if(t!=='dark'&&t!=='light')"
    "t=window.matchMedia&&matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';"
    "d.setAttribute('data-theme',t);")

BOOT = (
    "<script>(function(){var d=document.documentElement;"
    + THEME_JS +
    "d.classList.add('js');"
    "if(navigator.standalone===true||matchMedia('(display-mode:standalone)').matches)"
    "d.classList.add('standalone');"
    "})();</script>")


def head(bk, depth):
    """The exact block injected into one page.

    depth 0 is the hub at docs/index.html; depth 1 is any page inside a book's
    directory. docs/ nests no deeper than that, so one relative prefix is right
    for a chapter, the contents page, the ledger and the book's landing page
    alike. Both callers -- this injector and webbuild's SHELL -- use this same
    return value, so the two paths cannot disagree."""
    up = "../" * depth
    if bk is None:
        # The pair is right before any script runs. Once the reader has chosen
        # a theme that is not the OS's, pwa.js rewrites both to the resolved
        # --bg, so the browser chrome follows the page rather than the OS.
        theme = ('<meta name="theme-color" content="#f4f3f0" media="(prefers-color-scheme:light)">\n'
                 '<meta name="theme-color" content="#101216" media="(prefers-color-scheme:dark)">')
        title, icons = "Library", "icons/"
    else:
        # The paper colour, until pwa.js sets it to the page's resolved --bg on
        # load and after every theme change (PDA-14).
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


def nav_json(bk):
    """docs/<slug>/nav.json -- the book in reading order.

    The two chaptered books had navigation that looked standard and was not: a
    top bar, a section sidebar and a prev/next pair at the foot of each chapter,
    each built by the same producer but each answering a different question.
    None of them answered the one a reader on a phone asks most, which is "next
    chapter", without scrolling past five thousand words to reach it.

    This is the list that makes one answer possible in both books at once. It is
    derived from the curriculum rather than from the built pages, so a chapter's
    number and title here are the same strings the contents page shows, and it
    holds only chapters that exist on disk, so the navigation never offers a
    page that would 404.

    A book with fewer than two written chapters gets no file, and the client
    then does nothing: the two single-page books are not chaptered and have
    nothing to page through.

    It also carries the book's destinations, which are the same list the top
    bar is built from. The drawer is the whole of the navigation on a phone,
    and it used to offer one link out of the chapter -- back to the contents
    page -- while the bar three centimetres above it offered four. Carrying
    them here rather than reading them off the bar is what makes them work
    offline and inside a home-screen app, where the bar may be scrolled away
    and there is no browser chrome to fall back on."""
    rows = [{"href": slug + ".html", "num": num, "title": library.plain(title),
             "part": library.plain(part)}
            for num, slug, title, part, _math in bk.written()]
    if len(rows) < 2:
        return None
    out = {"slug": bk.slug, "brand": library.plain(bk.brand),
           "contents": "contents.html", "count": len(rows),
           "links": bk.nav_items(), "chapters": rows}
    # How the front door treats a returning reader (DESIGN.md section 6, Front
    # matter): a "sequential" book's primary becomes "Continue reading" at
    # their place, and a "reference" book keeps Contents as its primary and
    # offers "Continue at ..." beside it. pwa.js reads it here because the
    # front door is not the place to decide it: one book.json key, one reader.
    reading = bk.cfg.get("reading")
    if reading:
        if reading not in ("sequential", "reference"):
            raise SystemExit('%s: book.json "reading" is %r; it is "sequential" or '
                             '"reference"' % (bk.slug, reading))
        out["reading"] = reading
    return out


def shell_files():
    """Library-level files only: the hub, the manifest, the client, the icons,
    the two static pages. Deliberately O(1) in the number of books -- putting
    every book's landing page and stylesheet in here would make the install cost
    grow with the shelf, and charge a reader for twenty books to open one.

    404.html is not one of them. The host serves it online only, with a 404
    status the worker passes through and never stores, and offline a missing
    page gets offline.html; precaching it would charge every install for a page
    no offline reader can reach."""
    out = ["index.html", "manifest.webmanifest", "offline.html",
           "continue.html", "catalog.json", "assets/pwa.js", "assets/pwa.css",
           "assets/nav.css"]
    icons = os.path.join(DOCS, "icons")
    if os.path.isdir(icons):
        out += ["icons/" + f for f in sorted(os.listdir(icons))]
    return [p for p in out if os.path.exists(os.path.join(DOCS, p))]


# --------------------------------------------------------------- static pages

# All three are deliberately dependency-free: no stylesheet, no script, no font
# that has to be fetched. offline.html is what a reader sees when the network is
# gone and the page they asked for was never stored, so it must render from its
# own bytes alone -- a fallback that needs a fetch to look right is not a
# fallback. 404.html is served at whatever address went missing, at any depth,
# so a relative stylesheet link in it would resolve against that address and
# not against docs/.
#
# The theme is resolved inline, in <head>, by the same three steps as BOOT
# (THEME_JS), and both [data-theme] values are styled, so a reader who chose
# dark on a light OS is not flashed a light page here. The media query is kept
# only for a page no script has stamped.

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
%(viewport)s
<title>%(title)s</title>
<script>(function(){var d=document.documentElement;%(theme)s})();</script>
<style>
:root{color-scheme:light;--ink:#16181d;--soft:#565b66;--paper:#f4f3f0;--rule:#dcdfe5}
:root[data-theme="dark"]{color-scheme:dark;--ink:#e6e6e2;--soft:#a9adb6;--paper:#101216;--rule:#31353d}
@media (prefers-color-scheme:dark){
  :root:not([data-theme]){color-scheme:dark;--ink:#e6e6e2;--soft:#a9adb6;--paper:#101216;--rule:#31353d}}
html,body{margin:0;height:100%%}
body{background:var(--paper);color:var(--ink);display:grid;place-items:center;
  padding:max(24px,env(safe-area-inset-top)) 24px max(24px,env(safe-area-inset-bottom));
  font-family:"Iowan Old Style",Charter,"Bitstream Charter",Palatino,Georgia,serif;
  -webkit-text-size-adjust:100%%}
main{max-width:26rem;text-align:center}
h1{font-size:1.5rem;font-weight:400;margin:0 0 .6rem}
h2{font:700 11px/1.3 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;letter-spacing:.1em;
  text-transform:uppercase;color:var(--soft);margin:2rem 0 .5rem;text-align:left}
p{color:var(--soft);line-height:1.6;margin:0 0 1.4rem;
  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:14px}
.acts{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
a,button{display:inline-flex;align-items:center;justify-content:center;font:inherit;font-size:14px;
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-weight:600;
  padding:11px 16px;min-height:44px;box-sizing:border-box;border:1px solid var(--rule);
  border-radius:6px;background:none;color:inherit;text-decoration:none;cursor:pointer}
a:focus-visible,button:focus-visible{outline:2px solid currentColor;outline-offset:2px}
[hidden]{display:none!important}
ul{list-style:none;padding:0;margin:0;text-align:left}
li{border-top:1px solid var(--rule)}
li:last-child{border-bottom:1px solid var(--rule)}
li a{display:flex;justify-content:flex-start;border:0;border-radius:0;padding:12px 2px;font-weight:400;
  font-family:inherit;font-size:1rem}
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


# offline.html's own script. It is served in place of whatever page was asked
# for, at that page's address, so every address in it is absolute from
# library.SITE rather than relative to wherever it happens to be standing
# (NAV-16: its "./" link used to go to the book's folder, which was just as
# likely not to be stored). A book is listed as downloaded only when its
# lib:book:<slug> cache holds a __resident__ record with complete:true, the
# test pwa.js resident() uses (DESIGN.md section 8): a cache holding only the
# pages a reader happened to visit is not a downloaded book. caches.keys()
# is read first because caches.open() would create a missing cache.
OFFLINE_JS = r"""<script>
(function(){
  var S=%(site)s, P='lib:book:';
  var back=document.getElementById('back');
  if(history.length>1){back.hidden=false;back.addEventListener('click',function(){history.back()})}
  if(!('caches' in window))return;
  function complete(k){
    return caches.open(k).then(function(c){return c.keys().then(function(rs){
      var r=rs.filter(function(q){return /\/__resident__$/.test(q.url)})[0];
      return r?c.match(r).then(function(x){return x.json()}):null;
    })}).then(function(j){return j&&j.complete===true?k.slice(P.length):null})
      .catch(function(){return null});
  }
  caches.keys().then(function(ks){
    return Promise.all(ks.filter(function(k){return k.indexOf(P)===0}).map(complete));
  }).then(function(got){
    got=got.filter(Boolean);
    if(!got.length)return;
    var names={};
    return fetch(S+'catalog.json').then(function(r){return r.json()}).then(function(c){
      (c.books||[]).forEach(function(b){names[b.slug]=b.name});
    }).catch(function(){}).then(function(){
      var ul=document.getElementById('dl-list');
      got.sort().forEach(function(s){
        var li=document.createElement('li'),a=document.createElement('a');
        a.setAttribute('href',S+s+'/index.html');a.textContent=names[s]||s;
        li.appendChild(a);ul.appendChild(li);
      });
      document.getElementById('dl').hidden=false;
    });
  }).catch(function(){});
})();
</script>"""


# continue.html's script. With ?b=<slug> (a book's own home-screen
# shortcut) it goes to that book's place: library:v1.lastBy[slug], which
# pwa.js records on every chapter, and failing that the most recent page of
# the book in library:v1.pos, which is all a reader who read before lastBy
# existed has. With no b (the library's shortcut) it goes to the most recent
# place in any book. It used to follow only library:v1.last, the single last
# page of the whole library, so a physics reader's shortcut said "Nothing
# recorded yet" whenever they had since opened the clinical book (NAV-01).
CONTINUE_JS = r"""<script>
(function(){
  var want=new URLSearchParams(location.search).get('b');
  var s={};try{s=JSON.parse(localStorage.getItem('library:v1')||'{}')||{}}catch(e){}
  var by=s.lastBy||{}, go=null, k;
  function newer(a,b){return !a||(b&&(b.at||0)>(a.at||0))?b:a}
  if(want){
    if(by[want]&&by[want].url)go=by[want];
    else{
      // pos keys are paths; a book's front door and contents are not a place
      var pos=s.pos||{},best=null,at=-1,i=0;
      for(k in pos){i++;
        if(k.indexOf('/'+want+'/')<0||/\/(index|contents)\.html$|\/$/.test(k))continue;
        var t=(pos[k]&&pos[k].at)||i;
        if(t>=at){at=t;best=k}
      }
      if(best)go={url:best};
    }
  }else{
    for(k in by)if(by[k]&&by[k].url)go=newer(go,by[k]);
    if(!go&&s.last&&s.last.url)go=s.last;
  }
  if(go&&go.url){location.replace(go.url);return}
  // Nothing recorded, or nothing for this book: offer the shelf rather than
  // dead-ending on a shortcut the reader deliberately tapped.
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
</script>"""


# 404.html's script: the same Go back as offline.html, and nothing else. The
# shelf below it is written at build time, so the page needs no fetch.
NOTFOUND_JS = r"""<script>
(function(){
  var back=document.getElementById('back');
  if(history.length>1){back.hidden=false;back.addEventListener('click',function(){history.back()})}
})();
</script>"""


def emit_pages(bks):
    library.write(os.path.join(DOCS, "offline.html"), PAGE % {
        "viewport": VP_NEW,
        "theme": THEME_JS,
        "title": "Offline — A Library",
        "body": ("<h1>Not stored on this device</h1>"
                 "<p>You are offline, and this page was never downloaded. "
                 "Books you have downloaded are still readable in full.</p>"
                 '<div class="acts"><button type="button" id="back" hidden>Go back</button>'
                 '<a href="%s">The library</a></div>'
                 '<section id="dl" hidden><h2>Downloaded on this device</h2>'
                 '<ul id="dl-list"></ul></section>' % library.SITE),
        "script": OFFLINE_JS % {"site": json.dumps(library.SITE)}})

    # continue.html is the target of the home-screen shortcuts: the library
    # icon's "Continue reading" and each book icon's "Continue", which adds
    # ?b=<slug>. It reads the place pwa.js records and redirects, so a shortcut
    # is a real "carry on where I was" rather than a second copy of the shelf.
    # The hub's Continue strip and the front doors link to the chapter itself
    # and do not come through here.
    library.write(os.path.join(DOCS, "continue.html"), PAGE % {
        "viewport": VP_NEW,
        "theme": THEME_JS,
        "title": "Continue reading",
        "body": ('<h1>Continue reading</h1>'
                 '<p id="m">Looking for where you left off\u2026</p>'
                 '<ul id="l"></ul>'),
        "script": CONTINUE_JS})

    # 404.html is what Cloudflare Pages serves, with status 404, for any
    # address that has no file. Without it Pages assumes a single-page app and
    # answers every missing address with the hub and status 200, which the
    # worker and the book download then store as if it were the chapter asked
    # for. Like offline.html it stands at the address that was asked for, so
    # every link is absolute from library.SITE. It is the site's page rather
    # than the app's -- never precached, never served by the worker -- so it
    # keeps the plain viewport webbuild writes, which the app layer's
    # viewport-fit=cover replaces only on the pages it injects.
    shelf = "".join('<li><a href="%s%s/index.html">%s</a></li>'
                    % (library.SITE, b.slug, html.escape(b.app_name)) for b in bks)
    library.write(os.path.join(DOCS, "404.html"), PAGE % {
        "viewport": VP_OLD,
        "theme": THEME_JS,
        "title": "Not found — A Library",
        "body": ("<h1>Nothing at this address</h1>"
                 "<p>There is no page here. The link may be mistyped, or the "
                 "page may have moved.</p>"
                 '<div class="acts"><button type="button" id="back" hidden>Go back</button>'
                 '<a href="%s">The library</a></div>'
                 '<section><h2>The books</h2><ul>%s</ul></section>'
                 % (library.SITE, shelf)),
        "script": NOTFOUND_JS})


# ------------------------------------------------------------ the host's rules
#
# Cloudflare Pages answers every *.html address with a permanent 308 to the
# same address without the extension. Two things here break on that. The
# worker stores the response it is handed, which is then a redirected one, and
# a browser refuses a redirected response as the answer to a navigation, so a
# stored chapter would not open offline. And pwa.js finds a chapter in
# nav.json, and keys the reader's place, by the .html file name the address no
# longer carries.
#
# A 200 rule is a rewrite, and Pages applies _redirects before its own .html
# handling, so each line serves the file at the address that was asked for,
# with no redirect. The destinations stay extensionless: one ending in .html
# would be redirected in turn. They are root-relative rather than built from
# library.SITE because Pages always serves the output directory at the root.
REDIRECTS = ("/index.html / 200\n"
             "/*/index.html /:splat/ 200\n"
             "/*.html /:splat 200\n")


def emit_redirects():
    library.write(os.path.join(DOCS, "_redirects"), REDIRECTS)


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

    # 2. the three static pages and the host's rules, then manifests and the
    #    catalogue
    emit_pages(bks)
    emit_redirects()
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

    # 2b. the reading order, for the books that have one. Written before the
    #     offline manifest in step 4 so it is hashed with the rest of the book
    #     and downloads with it: navigation that only works online is not
    #     navigation an installed app can rely on.
    for b in bks:
        nav = nav_json(b)
        p = os.path.join(DOCS, b.slug, "nav.json")
        if nav:
            write_json(p, nav)
        elif os.path.exists(p):
            os.remove(p)

    # 3. inject the head block into every built page
    pages = 0
    for dp, _, fs in os.walk(DOCS):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
            if rel in STATIC:
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
            if rel in STATIC:
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
        # A chaptered book without its reading order still renders; it silently
        # loses prev/next everywhere, which is exactly the kind of quiet
        # regression the rest of this function exists to catch.
        want = nav_json(b)
        p = os.path.join(DOCS, b.slug, "nav.json")
        if want and not os.path.exists(p):
            bad.append("%s/nav.json (missing)" % b.slug)
        elif want and json.loads(library.read(p)) != want:
            bad.append("%s/nav.json (stale)" % b.slug)
        elif not want and os.path.exists(p):
            bad.append("%s/nav.json (should not exist: fewer than two chapters)" % b.slug)
    # The generated files themselves, not only their presence. offline.html,
    # continue.html, 404.html, _redirects, every manifest (its shortcuts and
    # theme_color follow the books' labels and colours), every nav.json and the
    # two shell assets are regenerated in memory, through the very writers
    # emit_all() uses, and compared byte for byte with docs/. library.write is
    # captured for the duration, so nothing is written. A label change in PAGE
    # or book.json that was never pushed through pwa.py used to pass here
    # because the file existed. A missing 404.html or _redirects fails here like
    # any other file: the site still serves without either, and quietly stores
    # the wrong pages.
    made = {}
    real_write = library.write

    def capture(path, text):
        made[os.path.relpath(path, DOCS).replace(os.sep, "/")] = text

    library.write = capture
    try:
        emit_pages(bks)
        emit_redirects()
        write_json(os.path.join(DOCS, "manifest.webmanifest"), library_manifest())
        for b in bks:
            write_json(os.path.join(DOCS, b.slug, "manifest.webmanifest"),
                       b.manifest(icon_entries()))
            nav = nav_json(b)
            if nav:
                write_json(os.path.join(DOCS, b.slug, "nav.json"), nav)
        for name in ("pwa.js", "pwa.css"):
            src = os.path.join(library.ASSETS, name)
            if os.path.exists(src):
                capture(os.path.join(DOCS, "assets", name), library.read(src))
    finally:
        library.write = real_write
    for rel, text in sorted(made.items()):
        p = os.path.join(DOCS, rel)
        if not os.path.exists(p):
            if rel + " (missing)" not in bad:
                bad.append(rel + " (missing)")
            continue
        with io.open(p, "rb") as fh:
            disk = fh.read()
        if disk != text.encode("utf-8") and not any(x.startswith(rel + " (") for x in bad):
            bad.append(rel + " (differs from what pwa.py would emit)")
    if bad:
        print("pwa: %d file(s) do not match what pwa.py would emit:" % len(bad))
        for r in bad[:60]:
            print("   ", r)
        print("    run: python3 tools/pwa.py")
        return 1
    print("pwa: every built page carries the current app-layer head; "
          "manifests, worker and icons all present; offline.html, continue.html, "
          "404.html, _redirects, %d manifests, %d nav.json and the shell assets "
          "are what pwa.py would emit"
          % (1 + len(bks), sum(1 for r in made if r.endswith("nav.json"))))
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        raise SystemExit(check())
    n = emit_all()
    print("pwa: %d pages injected, %d books, shell of %d files"
          % (n, len(library.books()), len(shell_files())))
