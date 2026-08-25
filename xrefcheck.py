#!/usr/bin/env python3
"""
Every "Chapter N.M" in the prose is a promise about a specific chapter. This checks the half of that
promise a machine can check — that N.M exists — and prints the rest for a human to scan.

Five of the fifteen errors found while converting Part 0 were cross-references that pointed at a real
chapter about the wrong subject (the propagator attributed to The Path Integral, contour integration
attributed to Vector Spaces and Linear Maps). A dangling reference is a build error; a reference to
the wrong real chapter is not, so it needs eyes. What this does is put every one of them on a single
page beside the title it actually resolves to, so scanning is a minute's work instead of an evening's.

    python3 xrefcheck.py            # dangling refs only; exit 1 if any
    python3 xrefcheck.py --all      # every reference with its target title
    python3 xrefcheck.py --self     # only refs a chapter makes to itself (usually a mistake)
"""
import os, re, sys, html, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(ROOT, "src")

LEDGER_CELL = re.compile(r'<td[^>]*>(.*?)</td>', re.S)


def ledger_refs(path):
    """Every bare N.M inside a ledger table cell, with the line it sits on."""
    if not os.path.exists(path):
        return []
    t = open(path, encoding='utf-8').read()
    out = []
    for m in LEDGER_CELL.finditer(t):
        cell = re.sub(r'\$[^$]*\$', ' ', m.group(1))     # a chapter number is never inside maths
        cell = html.unescape(re.sub(r'<[^>]+>', ' ', cell))
        line = t[:m.start()].count('\n') + 1
        # A chapter number here is a bare N.M with N a part (0-7) and M not
        # zero-padded — which keeps measured values like 2.04 out — and is never
        # preceded by a section sign, since "4.3 §8.4" is one chapter and one
        # section, not two chapters.
        for num in sorted(set(re.findall(r'(?<![\d.$§])(?<!§ )([0-7]\.[1-9]\d?)(?![\d.])', cell))):
            out.append((line, num, re.sub(r'\s+', ' ', cell).strip()))
    return out


def curriculum():
    import build as bp
    t = {}
    for label, sub, chs in bp.PARTS:
        for num, slug, title, ismath in chs:
            t[num] = (slug, title)
    return t

def prose(t):
    """Everything a reader reads. Scripts and display maths carry no chapter references, and the
    eyebrow line names the chapter you are already in, which is not a reference to anywhere."""
    t = re.sub(r'<p class="eyebrow">.*?</p>', ' ', t, flags=re.S)
    t = re.sub(r'<!--SCRIPT-->.*?<!--/SCRIPT-->', ' ', t, flags=re.S)
    t = re.sub(r'<div class="eq".*?</div>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(t)

def refs(text):
    """Yield (number, surrounding sentence) for every chapter reference."""
    # "Chapters 4.5 to 4.7" is one reference to each end, not one reference to the
    # first — the separator list has to carry "to" and "through" or the second
    # number is invisible to the census.
    for m in re.finditer(r'\bChapters?\s+((?:\d+\.\d+)(?:\s*(?:,\s*|\s+and\s+|\s+to\s+|\s+through\s+|\s*[–-]\s*)\d+\.\d+)*)', text):
        lo = text.rfind('.', 0, m.start())
        hi = text.find('.', m.end())
        sent = re.sub(r'\s+', ' ', text[lo+1 if lo >= 0 else 0 : hi if hi >= 0 else len(text)]).strip()
        for num in re.findall(r'\d+\.\d+', m.group(1)):
            yield num, sent

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    table = curriculum()
    files = sorted(f for f in os.listdir(SRC) if re.match(r'ch\d+-\d+\.html$', f))
    dangling, rows, selfref = [], [], []
    counts = collections.Counter()

    for f in files:
        own = re.match(r'ch(\d+)-(\d+)', f)
        own = f"{own.group(1)}.{own.group(2)}"
        text = prose(open(os.path.join(SRC, f), encoding='utf-8').read())
        for num, sent in refs(text):
            counts[num] += 1
            if num not in table:
                dangling.append((own, num, sent))
            elif num == own:
                selfref.append((own, num, sent))
            else:
                rows.append((own, num, table[num][1], sent))

    if mode == '--all':
        # One line per distinct (source, target) pair. 2,800 references collapse to a few hundred,
        # which is a page you can actually read.
        seen = {}
        for own, num, title, sent in rows:
            seen.setdefault((own, num, title), []).append(sent)
        for (own, num, title), sents in sorted(seen.items(), key=lambda k: (k[0][0], k[0][1])):
            longest = max(sents, key=len)
            print(f"\n{own} → {num}  ({title})   [{len(sents)}×]\n    …{longest[:320]}")
    elif mode == '--self':
        for own, num, sent in selfref:
            print(f"\n{own} → itself\n    …{sent[:300]}")

    print(f"\nxrefcheck: {len(files)} chapters, {sum(counts.values())} chapter references, "
          f"{len(set(counts))} distinct targets")
    if selfref:
        print(f"  {len(selfref)} self-reference(s) — run --self")
    # The ledger, by its own bare-number convention. It writes "4.5", never
    # "Chapter 4.5", and lives outside the ch*-*.html glob — so neither half of
    # this checker could see it. It missed the Part IV–VII renumbering entirely
    # and carried about 170 references to a curriculum that no longer existed,
    # through four commits, unnoticed.
    led = os.path.join(SRC, "_ledger.html")
    lrefs = ledger_refs(led)
    lbad = [(ln, num, cell) for ln, num, cell in lrefs if num not in table]

    if dangling:
        print(f"\n  {len(dangling)} DANGLING:")
        for own, num, sent in dangling:
            print(f"    {own} cites Chapter {num}, which is not in the curriculum")
            print(f"        …{sent[:220]}")
    else:
        print("  no dangling references")

    if lbad:
        print(f"\n  {len(lbad)} DANGLING in _ledger.html:")
        for ln, num, cell in lbad[:20]:
            print(f"    line {ln} cites {num}, which is not in the curriculum")
            print(f"        …{cell[:180]}")
    else:
        print(f"  _ledger.html: {len(lrefs)} bare references, all in the curriculum")

    return 1 if (dangling or lbad) else 0

if __name__ == '__main__':
    sys.exit(main())
