#!/usr/bin/env python3
"""
The library build — one book at a time.

Chapter content lives as HTML fragments in src/<slug>.html.
This wraps each in the shared shell (CSS + JS inlined so every chapter
is standalone), builds the index hub and the Math Ledger.

    python3 build.py
"""
import json, os, re, shutil, html, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

CDN = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9"

# ---------------------------------------------------------------- the book
# One build system, several books, so nothing here may assume the physics one.
# use(book) points the module at a book; the module-level names it sets are the
# ones make.py and webbuild.py already read, so their call sites are unchanged.
BOOK = None
PARTS = []          # [(part label, part subtitle, [(num, slug, title, is_math)])]
FLAT = []           # [(num, slug, title, part label, is_math)]
SRC = ASSETS = VENDOR = OUT = None
TITLE = ""


def use(bk):
    """Point the builder at one book of the library."""
    global BOOK, PARTS, FLAT, SRC, ASSETS, VENDOR, OUT, TITLE
    BOOK = bk
    TITLE = bk.title
    SRC = bk.src
    ASSETS = library.ASSETS
    VENDOR = library.VENDOR
    OUT = os.path.join(library.ROOT, ".staging", bk.slug)
    PARTS = [(p["label"], p["subtitle"],
              [(c["num"], c["slug"], c["title"], bool(c.get("math"))) for c in p["chapters"]])
             for p in bk.parts]
    FLAT = [(num, slug, title, part[0], m)
            for part in PARTS for (num, slug, title, m) in part[2]]
    return bk


use(library.book("newton-to-mtheory"))


def shell(title, body, side="", toc="", chapter=None, extra_js="", wide=False, base=""):
    """A staged page. base: relative prefix to reach build/ root, e.g. '' or '../'.
    side is the sidebar's head (sidebar_head()); toc pre-fills #sb-toc, which
    book.js otherwise fills from the page's headings. chapter goes on <body> as
    data-chapter, which book.js numbers the equations from; only staged pages
    carry it, and the shells that ship keep <body> bare.

    Only .main .col and #sb-toc of a staged page are kept: webbuild.py and
    make.py capture them and write their own shells around them. The markup
    here follows theirs (DESIGN.md section 8) so a staged page renders the way
    the finished one will."""
    css = library.read(os.path.join(ASSETS, "book.css"))
    js = library.read(os.path.join(ASSETS, "book.js"))
    k = base + "vendor/katex"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)} — {html.escape(TITLE)}</title>
<link rel="stylesheet" href="{k}/katex.min.css"
      onerror="this.onerror=null;this.href='{CDN}/katex.min.css'">
<style>
{css}
</style>
<script>
{js}
</script>
<script defer src="{k}/katex.min.js"
        onerror="this.onerror=null;var s=document.createElement('script');s.src='{CDN}/katex.min.js';document.head.appendChild(s)"></script>
<script defer src="{k}/auto-render.min.js"
        onerror="this.onerror=null;var s=document.createElement('script');s.src='{CDN}/contrib/auto-render.min.js';document.head.appendChild(s)"></script>
</head>
<body{f' data-chapter="{chapter}"' if chapter else ''}>
<div class="wrap">
<nav class="sidebar" aria-label="Chapter sections">
{side}
  <div id="sb-toc">{toc}</div>
</nav>
<main class="main" id="text">
<div class="col{' wide' if wide else ''}">
{body}
</div>
</main>
</div>
{extra_js}
</body>
</html>
"""


# ---------------------------------------------------------------- the frame
# The sidebar's head and the chapter foot are facts about the book, so they are
# written here, once, from the curriculum, and webbuild.py and make.py both call
# these rather than each composing its own (DESIGN.md sections 6 and 8). A
# chapter's neighbours are the written chapters either side of it: the same
# reading order nav.json gives pwa.js for the arrow keys, so the sidebar's
# arrows, the keys, the chapter foot and the phone's folio bar agree.

def split_label(label):
    """'Part XII · HER2-positive disease' -> ('Part XII', 'HER2-positive disease').
    The numeral is set as a label and the rest as the serif title."""
    head, sep, rest = label.partition(" · ")
    return (head, rest) if sep else ("", label)


def written():
    """The chapters whose source exists, in reading order (FLAT's shape)."""
    return [f for f in FLAT if os.path.exists(os.path.join(SRC, f[1] + ".html"))]


def part_index(label):
    """The part's position in the curriculum: contents.html#sec-<i>."""
    for i, p in enumerate(PARTS):
        if p[0] == label:
            return i
    raise KeyError(label)


def neighbours(slug):
    """(previous, next) written chapter around slug, each a FLAT row or None."""
    w = written()
    at = [f[1] for f in w].index(slug)
    return (w[at - 1] if at > 0 else None,
            w[at + 1] if at < len(w) - 1 else None)


def position(slug):
    """The sidebar's position line, written at build (pwa.js no longer adds one).

    'Chapter 68 of 98' when every chapter is written and the number is the
    ordinal, as in the clinical book. Otherwise the number and the place among
    the chapters there are: 'Chapter 1.1 · 10 of 37 written', in two unbreakable
    halves, so that a narrow sidebar wraps it after the dot and nowhere else.
    The text is the same either way; only the break is steered."""
    w = written()
    at = [f[1] for f in w].index(slug)
    num = w[at][0]
    if len(w) == len(FLAT):
        if str(num) == str(at + 1):
            return f"Chapter {num} of {len(FLAT)}"
        return (f'<span class="sb-at">Chapter {num} ·</span> '
                f'<span class="sb-at">{at + 1} of {len(FLAT)}</span>')
    return (f'<span class="sb-at">Chapter {num} ·</span> '
            f'<span class="sb-at">{at + 1} of {len(w)} written</span>')


PAGE_NAMES = {"contents": "Parts", "ledger": "Math Ledger", "throughline": "In Plain Terms"}


def sidebar_head(page, slug=None, contents="contents.html", keys=True, prefix=""):
    """The sidebar's up-link (.sb-home) and folio row (.sb-folio).

    page is "chapter" (with slug) or one of PAGE_NAMES. A chapter goes up to its
    part in the contents: contents.html#sec-<i> on the site, index.html#sec-<i>
    in the Dropbox build, where the contents page is index.html. Everything
    else goes up to the book. keys says whether the arrow keys work (pwa.js,
    the site only), so a link title never promises a key that does nothing.
    prefix reaches a chapter from the page (staged chapters sit one folder
    down)."""
    esc = html.escape
    if page != "chapter":
        return (f'  <a class="sb-home" href="{prefix}index.html">\u2190 {esc(TITLE)}</a>\n'
                f'  <div class="sb-folio"><p class="sb-title">{PAGE_NAMES[page]}</p></div>')
    row = next(f for f in FLAT if f[1] == slug)
    part = row[3]
    long_ = f' title="{esc(part)}"' if len(part) > 52 else ""
    up = (f'  <a class="sb-home" href="{prefix}{contents}#sec-{part_index(part)}"{long_}>'
          f'\u2190 {esc(part)}</a>')
    prev_, next_ = neighbours(slug)

    def arrow(cls, f, word, key, text):
        if not f:
            # the slot stays, so the position line never moves between pages
            return f'<span class="{cls}" aria-hidden="true"></span>'
        name = f"{word} chapter: {f[0]} · {esc(f[2])}"
        hint = f" ({key})" if keys else ""
        return (f'<a class="{cls}" href="{f[1]}.html" aria-label="{name}" '
                f'title="{name}{hint}">{text}</a>')
    folio = ('  <div class="sb-folio">'
             + arrow("sb-prev", prev_, "Previous", "\u2190", f"\u2039 {prev_[0]}" if prev_ else "")
             + f'<p class="sb-title">{position(slug)}</p>'
             + arrow("sb-next", next_, "Next", "\u2192", f"{next_[0]} \u203a" if next_ else "")
             + '</div>')
    return up + "\n" + folio


def chapnav(slug):
    """The chapter foot: two cards, or a .dead span where there is no neighbour.

    Each card is the direction (a label), then the number and title, then the
    neighbour's part when it is not this chapter's. The part is data-part,
    drawn by book.css, so the card's own text stays "Previous" + "67 · Title",
    the shape the folio bar and the drawer read (DESIGN.md section 8)."""
    here = next(f for f in FLAT if f[1] == slug)[3]
    prev_, next_ = neighbours(slug)
    out = ['<nav class="chapnav" aria-label="Previous and next chapter">']
    for cls, f, word in (("prev", prev_, "Previous"), ("next", next_, "Next")):
        if f:
            dp = f' data-part="{html.escape(f[3])}"' if f[3] != here else ""
            out.append(f'<a class="{cls}" href="{f[1]}.html" rel="{cls}"{dp}><span>{word}</span>'
                       f'{f[0]} · {html.escape(f[2])}</a>')
        else:
            out.append('<span class="dead"></span>')
    out.append('</nav>')
    return "\n".join(out)


def build():
    os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
    v_src, v_dst = VENDOR, os.path.join(OUT, "vendor")
    if os.path.isdir(v_src):
        shutil.rmtree(v_dst, ignore_errors=True)
        shutil.copytree(v_src, v_dst)
    built = set()

    for i, (num, slug, title, partlabel, _m) in enumerate(FLAT):
        f = os.path.join(SRC, slug + ".html")
        if not os.path.exists(f):
            continue
        raw = library.read(f)
        extra = ""
        m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
        if m:
            extra = "<script>\n" + m.group(1) + "\n</script>"
            raw = raw.replace(m.group(0), "")
        body = raw + "\n" + chapnav(slug)
        out = shell(f"{num} {title}", body,
                    side=sidebar_head("chapter", slug, contents="index.html", prefix="../"),
                    chapter=num, extra_js=extra, base="../")
        library.write(os.path.join(OUT, "chapters", slug + ".html"), out)
        built.add(slug)

    # ---- the contents page ----
    # A head, then the parts (FD-10, NAV-05, FD-16). The book's blurb, tagline
    # and ledger link belong to its front door, which the reader has just come
    # through; here they put chapter 1 below the fold on a phone.
    total = len(FLAT)
    done = len(built)
    esc = html.escape

    # Which written chapters are in the plain-language register. While the
    # conversion is partial the tag tells the reader something; once every
    # written chapter carries it, it tells them nothing, so it goes away by
    # itself rather than by anyone remembering to remove it.
    clear = set()
    for _l, _s, _chs in PARTS:
        for _n, _slug, _t, _m in _chs:
            _f = os.path.join(SRC, _slug + ".html")
            if os.path.exists(_f) and "<!--REGISTER:clear-->" in library.read(_f)[:1000]:
                clear.add(_slug)
    show_clear = bool(clear) and not clear >= built
    rows = []
    for i, (label, sub, chs) in enumerate(PARTS):
        # The id is emitted here rather than left to book.js, so a link to
        # contents.html#sec-<i> (the front door's arc rows, a chapter's up-link)
        # names an id the file carries. The value is the one book.js assigned
        # by position, since the part heads are the page's only h2s.
        # The heading's text stays the curriculum label ("Part IX · Title"):
        # the separator is hidden, and the count is drawn by book.css from
        # data-count, so every reader of the heading's text (the sidebar, the
        # drawer, Find a chapter) gets the same words as before.
        k, t = split_label(label)
        n = sum(1 for c in chs if c[1] in built)
        dc = f' data-count="{n} of {len(chs)} written"' if n < len(chs) else ""
        rows.append('<section class="part">')
        rows.append(f'<h2 class="part-head" id="sec-{i}">'
                    + (f'<span class="part-k"{dc}>{esc(k)}<span class="part-sep"> · </span></span>'
                       if k else "")
                    + f'<span class="part-t">{esc(t)}</span></h2>')
        rows.append(f'<p class="part-sub">{esc(sub)}</p>')
        rows.append('<ul class="clist">')
        for num, slug, title, ismath in chs:
            if slug in built:
                tag = '<span class="tag math">Math</span>' if ismath else ''
                # The plain-language tag is read out of the chapter file rather
                # than kept in a list here, so it can only ever say what is
                # actually true. It is also suppressed once it stops
                # distinguishing anything: a badge on every written row is
                # decoration, not information. So is "ready": a written
                # chapter is the one with a link.
                if show_clear and slug in clear:
                    tag += '<span class="tag clear">Clear</span>'
                rows.append(f'<li><span class="cnum">{num}</span>'
                            f'<a href="chapters/{slug}.html">{esc(title)}</a>{tag}</li>')
            else:
                # planned: the title in italic, no link and no label; the
                # legend under the count line says what italic means
                rows.append(f'<li class="planned"><span class="cnum">{num}</span>'
                            f'<span class="pending">{esc(title)}</span></li>')
        rows.append('</ul></section>')

    if done == total:
        count = f"{total} chapters in {len(PARTS)} parts"
    else:
        count = f"{done} of {total} chapters written, in {len(PARTS)} parts"
    legend = ("" if done == total
              else '\n<p class="toc-legend">Titles in italic are planned.</p>')
    body = f"""
<header class="toc-head">
<p class="eyebrow">{esc(TITLE)}</p>
<h1>Contents</h1>
<p class="label toc-count">{count}</p>{legend}
</header>
{''.join(rows)}
"""
    toc = "".join(f'<a href="#sec-{i}">{esc(p[0])}</a>' for i, p in enumerate(PARTS))
    library.write(os.path.join(OUT, "index.html"),
        shell("Contents", body, side=sidebar_head("contents"), toc=toc, wide=True))

    # ---- through-line ---- (the plain column: it is continuous prose)
    tl = os.path.join(SRC, "_throughline.html")
    if BOOK.has("throughline") and os.path.exists(tl):
        library.write(os.path.join(OUT, "throughline.html"),
            shell("In Plain Terms", library.read(tl), side=sidebar_head("throughline")))

    # ---- math ledger ---- (only for a book that keeps one)
    if BOOK.has("ledger"):
        led = os.path.join(SRC, "_ledger.html")
        ledger_body = library.read(led) if os.path.exists(led) else "<h1>Math Ledger</h1><p>Coming with the next batch.</p>"
        library.write(os.path.join(OUT, "ledger.html"),
            shell("Math Ledger", ledger_body, side=sidebar_head("ledger"), wide=True))

    print(f"built {done}/{total} chapters → {OUT}")


if __name__ == "__main__":
    build()
