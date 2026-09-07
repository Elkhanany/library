#!/usr/bin/env python3
"""
Check a rewritten copy of a book's studies against the original.

Written because a rewrite pass can report success and still have lost something,
and because reading 117 studies by hand is not a check anyone actually performs.
What it can prove mechanically:

  structure   same keys, same array lengths, nothing added or dropped
  encoding    still pure ASCII, entities not turned into literal characters
  markup      every <em> that went in comes out
  facts       every date, number, proper name and work title survives
  hedging     every epistemic marker survives
  shape       how far the sentence length actually moved

What it cannot prove, and nobody should claim it does: whether a sentence was
invented, whether a causal link was asserted that the original only implied, or
whether the new prose is better. Those need a reader.

    python3 tools/rewritecheck.py <original.json> <dir-of-rewrites>
"""
import glob
import io
import json
import os
import re
import sys

# Phrases that mark how a claim is known. Losing one is the failure this whole
# exercise was most at risk of, because it is the failure that reads as an
# improvement.
HEDGES = [
    "disputed", "traditionally", "attributed", "reported", "reportedly",
    "may be", "may have", "is said", "said to", "legend", "conventional",
    "later convention", "alone", "only", "on balance", "generally",
    "most scholars", "the sources disagree", "if genuine", "doubt",
    "uncertain", "conjectur", "apocryph", "ascrib", "purported",
    "credits", "claims", "argued", "held", "contested", "open question",
]


def walk(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, "%s[%d]" % (path, i))
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, "%s.%s" % (path, k) if path else k)


def shape(o):
    """A structural fingerprint: keys and lengths, no content."""
    if isinstance(o, dict):
        return {k: shape(v) for k, v in sorted(o.items())}
    if isinstance(o, list):
        return [shape(v) for v in o]
    return type(o).__name__


def text(study):
    return " ".join(v for _, v in walk(study) if isinstance(v, str))


def sentences(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"&[#a-zA-Z0-9]+;", " ", t)
    return [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', t) if p.strip()]


def wordcount(t):
    return len(re.findall(r"[A-Za-z][A-Za-z'-]*", re.sub(r"<[^>]+>", "", t)))


def main(origpath, rwdir):
    orig = json.loads(io.open(origpath, encoding="utf-8").read())
    new = {}
    for f in sorted(glob.glob(os.path.join(rwdir, "batch-*.json"))):
        new.update(json.loads(io.open(f, encoding="utf-8").read()))

    fail = 0
    report = []
    sb = sw = nb = nw = 0

    for slug in sorted(orig):
        if slug not in new:
            report.append((slug, "MISSING", "not in any batch")); fail += 1
            continue
        a, b = orig[slug], new[slug]

        if shape(a) != shape(b):
            report.append((slug, "STRUCTURE", "keys or array lengths differ")); fail += 1

        ta, tb = text(a), text(b)

        try:
            json.dumps(b, ensure_ascii=False).encode("ascii")
        except UnicodeEncodeError as e:
            report.append((slug, "ENCODING", "non-ASCII: %s" % str(e)[:60])); fail += 1

        na, nbb = ta.count("<em>"), tb.count("<em>")
        if na != nbb:
            report.append((slug, "MARKUP", "<em> %d -> %d" % (na, nbb))); fail += 1

        # facts: every number and every capitalised token must survive
        numa = set(re.findall(r"\b\d[\d,]*\b", ta))
        numb = set(re.findall(r"\b\d[\d,]*\b", tb))
        if numa - numb:
            report.append((slug, "NUMBERS", "lost %s" % sorted(numa - numb)[:8])); fail += 1

        capa = set(re.findall(r"\b[A-Z][a-z]{2,}\b", ta))
        capb = set(re.findall(r"\b[A-Z][a-z]{2,}\b", tb))
        # a word that was only ever sentence-initial can legitimately vanish when
        # sentences are re-cut, so only flag names that appear mid-sentence
        mid = set(re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", ta))
        lost = (capa - capb) & mid
        if lost:
            report.append((slug, "NAMES", "lost %s" % sorted(lost)[:8])); fail += 1

        la, lb = ta.lower(), tb.lower()
        gone = [h for h in HEDGES if la.count(h) > lb.count(h)]
        if gone:
            report.append((slug, "HEDGING", "weakened: %s" % gone[:6])); fail += 1

        wa, wb = wordcount(ta), wordcount(tb)
        if wa and abs(wb - wa) / float(wa) > 0.15:
            report.append((slug, "LENGTH", "words %d -> %d (%+.0f%%)"
                           % (wa, wb, 100.0 * (wb - wa) / wa))); fail += 1

        for s in sentences(ta):
            sb += 1; sw += len(s.split())
        for s in sentences(tb):
            nb += 1; nw += len(s.split())

    print("%d studies compared" % len(orig))
    print("  sentences  %d -> %d  (%+.0f%%)" % (sb, nb, 100.0 * (nb - sb) / sb))
    print("  words      %d -> %d  (%+.1f%%)" % (sw, nw, 100.0 * (nw - sw) / sw))
    print("  mean       %.1f -> %.1f words a sentence" % (sw / float(sb), nw / float(nb)))
    print()
    if report:
        print("%d problems:" % len(report))
        for slug, kind, msg in report:
            print("  %-18s %-10s %s" % (slug, kind, msg))
    else:
        print("structure, encoding, markup, numbers, names and hedging: all intact.")
    print()
    print("NOT checked here: invented sentences, asserted causation the original")
    print("only implied, and whether the prose is better. Those need a reader.")
    return 1 if fail else 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
