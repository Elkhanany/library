#!/usr/bin/env python3
"""Extract every forward reference naming a given chapter, with its context.

The point of `GAPS.md` §7: 393 references to unwritten chapters were each
written in good faith by an author who knew what the later chapter was going
to say. The risk is not that they are wrong — it is that the agent writing
that chapter does not know eight earlier chapters have already told the reader
what it will do. Run this and paste the output into the writing brief, and 393
hopes become 393 requirements.

    python3 debts.py 4.3          one chapter
    python3 debts.py 4            a whole part
    python3 debts.py --census     how many debts each unwritten chapter carries
"""
import re, sys, glob, os, collections, html

def strip(s):
    s = re.sub(r"<[^>]+>", "", s)
    return " ".join(html.unescape(s).split())

def sentences_naming(path, pat):
    """Return (line number, the whole sentence) for each mention."""
    raw = open(path, encoding="utf-8").read()
    txt = strip(raw)
    out = []
    for m in re.finditer(pat, txt):
        a = txt.rfind(". ", 0, max(0, m.start() - 1))
        a = 0 if a < 0 else a + 2
        b = txt.find(". ", m.end())
        b = len(txt) if b < 0 else b + 1
        # locate the line in the source, for editing
        needle = txt[m.start():m.end()]
        ln = raw[:raw.find(needle)].count("\n") + 1 if needle in raw else 0
        out.append((ln, txt[a:b].strip()))
    return out

def census():
    import importlib.util
    spec = importlib.util.spec_from_file_location("bp", "build.py")
    bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
    written = {n for n, slug, *_ in bp.FLAT if os.path.exists("src/" + slug + ".html")}
    planned = [n for n, *_ in bp.FLAT]
    c = collections.Counter()
    for p in glob.glob("src/ch*.html"):
        for m in re.findall(r"Chapter (\d\.\d+)", strip(open(p, encoding="utf-8").read())):
            c[m] += 1
    print(f"{sum(v for k, v in c.items() if k not in written)} forward references "
          f"to unwritten chapters\n")
    unknown = [k for k in c if k not in planned]
    for n in planned:
        if n not in written and c[n]:
            print(f"  {n:5s} {c[n]:3d}")
    if unknown:
        print("\n  !! naming chapters that do not exist in the curriculum: "
              + ", ".join(sorted(unknown)))

def report(target):
    whole_part = "." not in target
    pat = (r"Chapter %s\.\d+" % re.escape(target)) if whole_part \
          else (r"Chapter %s(?!\d)" % re.escape(target))
    total = 0
    for p in sorted(glob.glob("src/ch*.html")):
        hits = sentences_naming(p, pat)
        if not hits:
            continue
        print(f"\n### {os.path.basename(p)[:-5]} — {len(hits)}")
        for ln, s in hits:
            print(f"  · {s}")
            total += 1
    print(f"\n{total} promises name Chapter {target}. Every one is a requirement.")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--census":
        census()
    else:
        report(sys.argv[1])
