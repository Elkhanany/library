#!/usr/bin/env python3
"""Prove that a register rewrite changed the prose and nothing else.

The plain-language rewrite rebuilds connective prose. It must not touch a
single equation, id, heading, plain-terms box, or line of figure script — and
"must not" is worth checking rather than trusting, because a rewrite that
quietly drops a hypothesis or renumbers a section is far worse than dry prose.

    python3 registercheck.py <original.html> <rewritten.html>

Exit 0 if every invariant holds.
"""
import re, sys, difflib, statistics

def eqs(t):      return re.findall(r'<div class="eq" id="([^"]+)">\s*(.*?)\s*</div>', t, re.S)
def heads(t):    return [(l, " ".join(re.sub(r'<[^>]+>','',s).split()))
                         for l, s in re.findall(r'<h([2-4])>(.*?)</h\1>', t, re.S)]
def plains(t):   return [" ".join(re.sub(r'<[^>]+>',' ',b).split())
                         for b in re.findall(r'<div class="callout plain">(.*?)</div>', t, re.S)]
def script(t):
    m = re.search(r'<!--SCRIPT-->(.*?)<!--/SCRIPT-->', t, re.S)
    return m.group(1) if m else ""
def flags(t):    return t.count("⚑")
def figs(t):     return re.findall(r'<canvas[^>]*id="([^"]+)"', t)
def refs(t):     return sorted(set(re.findall(r'href="#(e-[^"]+)"', t)))

def transitions(t):
    """Consecutive display equations with no bridging prose between them.

    Handing the reader a second equation straight after the first, with nothing
    said in between, is the commonest way a derivation stops being followable —
    the algebra is all present and the thread is not. Grind boxes are exempt:
    they hold algebra deliberately.
    """
    t = re.sub(r'<!--SCRIPT-->.*?<!--/SCRIPT-->', ' ', t, flags=re.S)
    t = re.sub(r'<details.*?</details>', ' GRIND ', t, flags=re.S)
    tot = abrupt = 0
    for m in re.finditer(r'</div>\s*(.*?)\s*<div class="eq"', t, re.S):
        seg = m.group(1)
        if '<div class="eq"' in seg or 'GRIND' in seg:
            continue
        before = t[:m.start()]
        if not before.rstrip().endswith("$$") and 'class="eq"' not in before[-400:]:
            continue
        tot += 1
        if len(re.sub(r'<[^>]+>', ' ', seg).split()) <= 8:
            abrupt += 1
    return abrupt, tot

def prose(t):
    t = re.sub(r'<!--SCRIPT-->.*?<!--/SCRIPT-->', ' ', t, flags=re.S)
    t = re.sub(r'<div class="callout plain">.*?</div>', ' ', t, flags=re.S)
    # Headings, callout titles and figure-control labels are not prose: a dash in
    # a title is a separator, not an interruption, and counting them makes the
    # budget unwinnable for reasons that have nothing to do with readability.
    t = re.sub(r'<h[1-4]>.*?</h[1-4]>', ' ', t, flags=re.S)
    t = re.sub(r'<span class="ct">.*?</span>', ' ', t, flags=re.S)
    t = re.sub(r'<summary>.*?</summary>', ' ', t, flags=re.S)
    t = re.sub(r'<label.*?</label>', ' ', t, flags=re.S)
    t = re.sub(r'\$\$.*?\$\$', ' EQ ', t, flags=re.S)
    t = re.sub(r'\$[^$]*\$', ' x ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t)

def metrics(t, label):
    p = prose(t)
    s = [x for x in re.split(r'(?<=[.!?])\s+', p) if len(x.split()) > 2]
    L = [len(x.split()) for x in s]; w = sum(L)
    print(f"  {label:<12} {w:>6,}w  mean {statistics.mean(L):5.1f}  "
          f">35w {100*sum(1 for x in L if x>35)/len(s):5.1f}%  "
          f"em-dash {1000*p.count('—')/w:5.2f}/kw  "
          f"semicolon {1000*p.count(';')/w:5.2f}/kw")
    return {"emdash": 1000*p.count('—')/w, "semi": 1000*p.count(';')/w,
            "long": 100*sum(1 for x in L if x>35)/len(s), "words": w}

def main(a, b):
    A = open(a, encoding="utf-8").read(); B = open(b, encoding="utf-8").read()
    bad = 0

    def check(name, x, y, show=True):
        nonlocal bad
        if x == y:
            print(f"  ok    {name}")
            return
        bad += 1
        print(f"  FAIL  {name}")
        if show:
            for line in list(difflib.unified_diff(
                    [str(i) for i in (x if isinstance(x, list) else [x])],
                    [str(i) for i in (y if isinstance(y, list) else [y])],
                    lineterm="", n=0))[:14]:
                print("          " + line[:150])

    print(f"\nINVARIANTS  ({a}  →  {b})")
    check(f"equations ({len(eqs(A))})",            eqs(A),    eqs(B))
    check(f"headings ({len(heads(A))})",           heads(A),  heads(B))
    check(f"plain-terms boxes ({len(plains(A))})", plains(A), plains(B))
    check("figure script",                          script(A), script(B), show=False)
    check(f"canvases ({len(figs(A))})",            figs(A),   figs(B))
    check(f"equation references ({len(refs(A))})", refs(A),   refs(B))
    check(f"⚑ marks ({flags(A)})",                 flags(A),  flags(B))

    print("\nPROSE")
    m0 = metrics(A, "before"); m1 = metrics(B, "after")

    a0, n0 = transitions(A); a1, n1 = transitions(B)
    pct0 = 100*a0/n0 if n0 else 0
    pct1 = 100*a1/n1 if n1 else 0
    print(f"  {'equation bridges':<12} {a1} of {n1} transitions carry 8 words or fewer "
          f"({pct1:.0f}%, was {pct0:.0f}%)")

    print("\nTARGETS  (the plain-terms boxes' own numbers, since those read well)")
    m1["abrupt"] = pct1; m0["abrupt"] = pct0
    for key, lim, name in (("emdash", 1.0, "em-dashes/kw"), ("semi", 2.5, "semicolons/kw"),
                           ("long", 14.0, "sentences >35w"),
                           ("abrupt", 3.0, "abrupt eq bridges %")):
        got = m1[key]
        ok = got <= lim
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'MISS'}  {name:<16} {got:6.2f}  (limit {lim}, was {m0[key]:.2f})")

    keep = 100 * m1["words"] / m0["words"]
    print(f"\n  length {keep:.0f}% of the original "
          f"({'ok' if 85 <= keep <= 140 else 'CHECK — a rewrite should not change size much'})")
    print(f"\n{'PASS' if not bad else f'{bad} PROBLEM(S)'}\n")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
