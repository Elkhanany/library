#!/usr/bin/env python3
"""
Insert (or replace) numbered "In plain terms" boxes in a chapter fragment.

A box goes immediately BEFORE the <h2> that starts the next section, so it closes
the section it belongs to. Numbering is chapter.section — box 2.4.3 closes §3 of
Chapter 2.4 — which makes every box addressable from the Through-Line ledger.

Idempotent: existing .callout.plain blocks are stripped before inserting, so the
script can be re-run after an edit without duplicating anything.
"""
import re, os

BOX = ('<div class="callout plain">\n'
       '  <span class="ct">In plain terms <span class="pnum">{num}</span></span>\n'
       '{body}\n</div>\n')

PLAIN_RE = re.compile(r'\n*<div class="callout plain">.*?\n</div>\n', re.S)


def strip_existing(text):
    return PLAIN_RE.sub("\n", text)


def inject(path, chapter, blocks):
    """chapter: e.g. '2.4'. blocks: list of (section_no, anchor_regex, [paragraphs]).
    anchor_regex matches the line the box is inserted BEFORE; use 'END' for
    end-of-file (i.e. the box closing the final section)."""
    text = strip_existing(open(path).read())
    lines = text.split("\n")
    hits = []
    for sec, anchor, paras in blocks:
        if anchor == "END":
            hits.append((len(lines), sec, paras)); continue
        idx = [i for i, l in enumerate(lines) if re.search(anchor, l)]
        if not idx:
            print(f"   !! {os.path.basename(path)}: anchor not found -> {anchor}")
            continue
        hits.append((idx[0], sec, paras))
    for i, sec, paras in sorted(hits, key=lambda t: t[0], reverse=True):
        body = "\n".join("  <p>%s</p>" % p for p in paras)
        lines.insert(i, BOX.format(num=f"{chapter}.{sec}", body=body))
    open(path, "w").write("\n".join(lines))
    print(f"   {os.path.basename(path)}: {len(hits)} boxes")
    return len(hits)
