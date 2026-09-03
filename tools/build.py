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


def shell(title, body, chapter=None, sidebar_head="Contents", home="index.html",
          extra_js="", wide=False, base=""):
    """base: relative prefix to reach build/ root, e.g. '' or '../'"""
    css = library.read(os.path.join(ASSETS, "book.css"))
    js = library.read(os.path.join(ASSETS, "book.js"))
    k = base + "vendor/katex"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
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
<nav class="sidebar">
  <a class="sb-home" href="{home}">← Newton to M-Theory</a>
  <p class="sb-title">{sidebar_head}</p>
  <div id="sb-toc"></div>
</nav>
<main class="main">
<div class="col{' wide' if wide else ''}">
{body}
</div>
</main>
</div>
{extra_js}
</body>
</html>
"""


def chapnav(i):
    prev_ = FLAT[i - 1] if i > 0 else None
    next_ = FLAT[i + 1] if i < len(FLAT) - 1 else None
    parts = ['<nav class="chapnav">']
    if prev_ and os.path.exists(os.path.join(SRC, prev_[1] + ".html")):
        parts.append(f'<a class="prev" href="{prev_[1]}.html"><span>Previous</span>'
                     f'{prev_[0]} · {html.escape(prev_[2])}</a>')
    else:
        parts.append('<span class="dead"></span>')
    if next_ and os.path.exists(os.path.join(SRC, next_[1] + ".html")):
        parts.append(f'<a class="next" href="{next_[1]}.html"><span>Next</span>'
                     f'{next_[0]} · {html.escape(next_[2])}</a>')
    else:
        parts.append('<span class="dead"></span>')
    parts.append('</nav>')
    return "\n".join(parts)


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
        body = raw + "\n" + chapnav(i)
        out = shell(f"{num} {title}", body, chapter=num,
                    sidebar_head=f"Ch {num}", home="../index.html", extra_js=extra,
                    base="../")
        library.write(os.path.join(OUT, "chapters", slug + ".html"), out)
        built.add(slug)

    # ---- index hub ----
    total = len(FLAT)
    done = len(built)

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
    for label, sub, chs in PARTS:
        rows.append('<section class="part">')
        rows.append(f'<h2 class="part-head">{html.escape(label)}</h2>')
        rows.append(f'<p class="part-sub">{html.escape(sub)}</p>')
        rows.append('<ul class="clist">')
        for num, slug, title, ismath in chs:
            tag = '<span class="tag">math</span>' if ismath else ''
            # The plain-language tag is read out of the chapter file rather than
            # kept in a list here, so it can only ever say what is actually true.
            # It is also suppressed once it stops distinguishing anything: a badge
            # on every written row is decoration, not information.
            if show_clear and slug in clear:
                tag += '<span class="tag clear">clear</span>'
            if slug in built:
                rows.append(f'<li><span class="cnum">{num}</span>'
                            f'<span><a href="chapters/{slug}.html">{html.escape(title)}</a>'
                            f'{tag} <span class="tag ready">ready</span></span></li>')
            else:
                rows.append(f'<li><span class="cnum">{num}</span>'
                            f'<span class="pending">{html.escape(title)}{tag}</span></li>')
        rows.append('</ul></section>')

    nmath = sum(1 for f in FLAT if f[4])
    mathnote = (f' &nbsp;·&nbsp; {nmath} of them dedicated math chapters' if nmath else '')
    ledgerlink = (' &nbsp;·&nbsp; <a href="ledger.html">Math Ledger</a>' if BOOK.has("ledger") else '')
    body = f"""
<div class="hero">
<p class="eyebrow">{html.escape(BOOK.eyebrow)}</p>
<h1>{html.escape(TITLE)}</h1>
<p class="subtitle">{html.escape(BOOK.tagline)}</p>
<p>{BOOK.cfg.get("blurb","")}</p>
<p style="color:var(--ink-soft);font-size:.95rem">
<b>{done} of {total}</b> chapters built{mathnote}{ledgerlink}</p>
</div>
{''.join(rows)}
"""
    library.write(os.path.join(OUT, "index.html"),
        shell("Contents", body, sidebar_head="Parts", home="index.html", wide=True))

    # ---- through-line ----
    tl = os.path.join(SRC, "_throughline.html")
    if BOOK.has("throughline") and os.path.exists(tl):
        library.write(os.path.join(OUT, "throughline.html"),
            shell("The Through-Line", library.read(tl), sidebar_head="Through-Line",
                  home="index.html", wide=True))

    # ---- math ledger ---- (only for a book that keeps one)
    if BOOK.has("ledger"):
        led = os.path.join(SRC, "_ledger.html")
        ledger_body = library.read(led) if os.path.exists(led) else "<h1>Math Ledger</h1><p>Coming with the next batch.</p>"
        library.write(os.path.join(OUT, "ledger.html"),
            shell("Math Ledger", ledger_body, sidebar_head="Ledger", home="index.html", wide=True))

    print(f"built {done}/{total} chapters → {OUT}")


if __name__ == "__main__":
    build()
