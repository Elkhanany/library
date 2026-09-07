#!/usr/bin/env python3
"""
Measure the sentence architecture of a book's prose against the house style.

The one rule in .claude/skills/house-style is that independent clauses should
not be chained, and the number that came out of the comparison was a mean of
15-18 words a sentence with nothing much over 35. This reports those numbers
for any book so the rule can be checked rather than remembered.

    python3 tools/prosecheck.py                    # every book with prose data
    python3 tools/prosecheck.py the-long-argument  # one

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


def report(slug):
    d = os.path.join(library.BOOKS, slug, "src", "data")
    if not os.path.isdir(d):
        return False
    allsent, worst, chains = [], [], 0
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json"):
            continue
        data = json.loads(library.read(os.path.join(d, f)))
        for path, text in walk(data, f[:-5]):
            for s in sentences(text):
                n = len(words(s))
                allsent.append(n)
                c = chained(s)
                chains += c
                if n >= 34 or c:
                    worst.append((n, c, path, s))
    if not allsent:
        return False
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
    slugs = args or library.slugs()
    if not any(report(s) for s in slugs):
        print("no book in %s ships prose data under src/data/" % ", ".join(slugs))
