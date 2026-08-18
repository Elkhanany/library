#!/usr/bin/env python3
"""
Build src/_throughline.html by extracting every "In plain terms" box, in book order.

The Through-Line is never authored directly — it is assembled from the chapters, so it
cannot drift out of sync. Edit a box in a chapter and it changes here on the next build.
Bridging passages between parts live in BRIDGES below and are the only prose written here.
"""
import os, re, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")

spec = importlib.util.spec_from_file_location("bp", os.path.join(ROOT, "build.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

BOX_RE = re.compile(
    r'<div class="callout plain">\s*<span class="ct">.*?<span class="pnum">([\d.]+)</span>'
    r'\s*</span>\s*(.*?)\s*</div>', re.S)

BRIDGES = {
"Part 0 · The Toolkit": """
<p>What follows is the whole book, with the mathematics taken out.</p>
<p>Each passage below was written to close a section of a chapter, in the reader's own language
rather than the chapter's. Read in place, they are pauses for breath. Read here, one after another,
they are something else: a continuous account of how physics arrived at its present picture of the
world, from the definition of a derivative to what string theory is actually claiming, with no
equation anywhere in it.</p>
<p>One idea runs underneath all of it. <b>Ask what stays the same when you change your point of
view. Whatever survives is real; whatever does not was a fact about where you were standing.</b>
Everything that follows is that sentence, applied to progressively larger questions.</p>
<p>Part 0 builds tools rather than physics. But the tools are not neutral, and the choices made in
building them decide what can be said later.</p>""",

"Part I · The Action Principle": """
<p>The toolkit is finished. What follows stops describing instruments and starts describing nature —
and the first thing it does is throw away the idea most people think physics is made of.</p>""",

"Part II · Special Relativity": """
<p>Mechanics has been rebuilt on a principle rather than a force law, and the rebuild bought
something specific: equations that keep their shape when you change your description. That property
is about to be tested against a contradiction that broke the nineteenth century.</p>""",

"Part III · General Relativity": """
<p>Space and time have become one fabric with a speed limit built into its geometry. But one force
was left behind, still acting instantly across empty space, and the geometry just made that
impossible.</p>""",

"Part IV · Quantum Mechanics": """
<p>Everything so far has assumed that a thing has a definite state and that measuring it is a matter
of care. At small enough scales both assumptions fail, and the mathematics that replaces them was
built four parts ago for entirely different reasons.</p>""",

"Part V · Quantum Field Theory": """
<p>Relativity and quantum mechanics are each secure and are not compatible. Forcing them together
costs the particle its status as the fundamental object.</p>""",

"Part VI · Gauge Theory and the Standard Model": """
<p>Fields can be quantised and the results computed. What has not yet been explained is why there
are the particular forces there are — and the answer turns out to be a single demand, made four
times.</p>""",

"Part VII · Strings and M-Theory": """
<p>One force has refused every method that worked for the others. What follows is the most developed
proposal for what to do about that, followed by an honest account of how much of it is known.</p>""",
}


def extract():
    parts = []
    for label, sub, chs in bp.PARTS:
        entries = []
        for num, slug, title, _m in chs:
            f = os.path.join(SRC, slug + ".html")
            if not os.path.exists(f):
                continue
            boxes = BOX_RE.findall(open(f).read())
            if boxes:
                entries.append((num, title, slug, boxes))
        if entries:
            parts.append((label, sub, entries))
    return parts


def build():
    parts = extract()
    total = sum(len(b) for _, _, e in parts for *_, b in [e[0]] for _ in [0]) if parts else 0
    total = sum(len(bx) for _, _, entries in parts for *_, bx in entries)
    words = 0
    out = ['<p class="eyebrow">Reference</p>',
           '<h1>The Through-Line</h1>',
           '<p class="subtitle">The whole book in plain language, assembled from every '
           '&ldquo;In plain terms&rdquo; passage in order. No mathematics.</p>']

    for label, sub, entries in parts:
        out.append('<div class="callout plain bridge">%s</div>' % BRIDGES.get(label, ""))
        out.append('<h2>%s</h2>' % html.escape(label))
        out.append('<p class="part-sub">%s</p>' % html.escape(sub))
        for num, title, slug, boxes in entries:
            out.append('<h3><a href="%s.html">%s &nbsp;%s</a></h3>' %
                       (slug, num, html.escape(title)))
            for pnum, body in boxes:
                words += len(re.sub(r"<[^>]+>", " ", body).split())
                out.append('<div class="tl-item"><span class="tl-num">%s</span>\n%s\n</div>'
                           % (pnum, body.strip()))

    hdr = ('<p style="color:var(--ink-soft);font-size:.95rem">'
           '<b>%d passages</b> &nbsp;·&nbsp; about %s words &nbsp;·&nbsp; '
           'reads start to finish as one essay &nbsp;·&nbsp; '
           '<a href="ledger.html">Math Ledger</a></p>' % (total, f"{words:,}"))
    out.insert(3, hdr)
    open(os.path.join(SRC, "_throughline.html"), "w").write("\n\n".join(out))
    print(f"through-line: {total} passages, {words:,} words")


if __name__ == "__main__":
    build()
