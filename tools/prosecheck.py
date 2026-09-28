#!/usr/bin/env python3
"""
Measure the sentence architecture of a book's prose against the house style.

The one rule in .claude/skills/house-style is that independent clauses should
not be chained, and the number that came out of the comparison was a mean of
15-18 words a sentence with nothing much over 35. This reports those numbers
for any book so the rule can be checked rather than remembered.

    python3 tools/prosecheck.py                    # every book with prose data
    python3 tools/prosecheck.py the-long-argument  # one
    python3 tools/prosecheck.py the-other-end-of-the-trade 1a 1b
                                                   # chapters of a book written in markdown

SCOPE. The 15-18 target was measured on narrative prose about people. It does
not apply to the formal layer, whose `claim` fields state one proposition each
and are meant to be single sentences however long, and whose prose carries line
references that must not be separated from what they refer to. This tool counts
those as chains and will overstate the work in formal.json; the house-style
skill explains why they are correct as they stand.

Lists are deliberately NOT flagged. A colon introducing a series, and
semicolons separating items that carry their own commas, are doing work a full
stop cannot; the rule is about clauses that could stand alone. So a sentence is
only reported when it joins independent clauses -- a semicolon or an " and "
with a subject and a finite verb on both sides -- which is an approximation, and
the point is to rank paragraphs for a human to look at, not to gate a build.
"""
import io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library


def sentences(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"&[a-z]+;|&#\d+;", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', t) if p.strip()]


def words(t):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", t)


def chained(s):
    """A rough count of independent clauses joined inside one sentence."""
    n = 0
    for part in re.split(r";", s)[1:]:
        # a semicolon followed by something with its own subject and verb
        if len(words(part)) > 3:
            n += 1
    for m in re.finditer(r",\s+(and|but)\s+(?=[a-z])", s):
        tail = s[m.end():]
        if len(words(tail)) > 5:
            n += 1
    return n


def walk(obj, path=""):
    """Every prose string in a book's data, with a path to find it again."""
    if isinstance(obj, str):
        if len(obj) > 60:
            yield path, obj
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, "%s[%d]" % (path, i))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, "%s.%s" % (path, k) if path else k)


def markdown_prose(text):
    """The running prose of a markdown chapter, one paragraph a string. Tables,
    code, maths, figure markers and the lines that open and close a callout are
    not sentences, and a list item is measured as its own sentence."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    # a capital, so that a sentence opening with maths is split from the one before it
    text = re.sub(r"\\\((.+?)\\\)", "X", text, flags=re.S)
    out = []
    for para in re.split(r"\n\s*\n", text):
        lines = [l for l in para.split("\n")
                 if l.strip() and not re.match(r"\s*(\||:::|\[FIGURE|\{#eq:)", l)]
        if not lines or re.match(r"\s*#", lines[0]):
            continue
        # A list item (or a check's question or answer) is a piece of its own, with the
        # lines that continue it, so it never runs on into the item before it.
        pieces = []
        for l in lines:
            if re.match(r"\s*([-*]|\d+\.|\?\?|!!)\s+", l) or not pieces:
                pieces.append([])
            pieces[-1].append(re.sub(r"^\s*(#+|[-*]|\d+\.|\?\?|!!|>)\s+", "", l))
        for piece in pieces:
            joined = " ".join(piece)
            # A bold run-in label ("**Step 2: each line.**") is a heading, not a sentence.
            joined = re.sub(r"^\s*\*\*[^*]{1,60}?[.:]\*\*\s+", "", joined)
            joined = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", joined)
            joined = re.sub(r"[*`]", "", joined)
            if joined.strip():
                out.append(joined)
    return out


def report(slug, only=None):
    d = os.path.join(library.BOOKS, slug, "src", "data")
    md = os.path.join(library.BOOKS, slug, "chapters")
    items = []
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith(".json"):
                items += list(walk(json.loads(library.read(os.path.join(d, f))), f[:-5]))
    elif os.path.isdir(md):
        for f in sorted(os.listdir(md)):
            if f.endswith(".md") and (not only or f[:-3] in only):
                items += [(f[:-3], p) for p in markdown_prose(library.read(os.path.join(md, f)))]
    else:
        return False
    allsent, worst, chains = [], [], 0
    per = {}
    for path, text in items:
        for s in sentences(text):
            n = len(words(s))
            allsent.append(n)
            per.setdefault(path.split(".")[0], []).append(n)
            c = chained(s)
            chains += c
            if n >= 34 or c:
                worst.append((n, c, path, s))
    if not allsent:
        return False
    if os.path.isdir(md) and not os.path.isdir(d):
        for name, ns in per.items():
            print("   %-8s %4d sentences, mean %4.1f words, longest %d"
                  % (name, len(ns), sum(ns) / float(len(ns)), max(ns)))
    allsent.sort()
    mean = sum(allsent) / float(len(allsent))
    p95 = allsent[int(.95 * len(allsent))]
    print("%s: %d sentences, mean %.1f words, 95th %d, longest %d"
          % (slug, len(allsent), mean, p95, allsent[-1]))
    inband = "yes" if 15 <= mean <= 18 else "NO -- house style asks 15-18"
    print("   mean within the house target: %s" % inband)
    print("   %d sentences chain independent clauses" % chains)
    worst.sort(key=lambda x: (-x[1], -x[0]))
    for n, c, path, s in worst[:12]:
        print("   %3dw %s %s" % (n, ("chains %d" % c) if c else "        ", path))
        print("        %s" % (s[:150] + ("..." if len(s) > 150 else "")))
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    # prosecheck.py BOOK CHAPTER...: only those chapters of a markdown book
    slugs = args[:1] if len(args) > 1 else (args or library.slugs())
    only = set(args[1:]) or None
    if not any(report(s, only) for s in slugs):
        print("no book in %s ships prose data under src/data/ or chapters/" % ", ".join(slugs))
