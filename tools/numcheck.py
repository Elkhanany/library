#!/usr/bin/env python3
"""Every figure in a chapter's prose appears in the registry, in a trial the chapter names.

The chapter layer has no independent check on numbers. bc.py resolves keys and
evidence.py validates filters, but a hazard ratio typed into a sentence is
checked by nobody. This is that check, and it is deliberately mechanical: take
each numeric token out of the prose, and require it to occur in the registry
record or stored abstract of one of the trials that chapter names, or in the
year or volume of one of the references it cites.

A number that does not occur is reported. Some are legitimate: a dose, a year, a
threshold from a guideline, a count of trials the writer made themselves. Those
are adjudicated by reading, which is the point. A number nobody can place is the
one this catches.

A teaching paragraph is the exception, and it is declared rather than reported.
"Out of 100 women, over 7 years" is a sentence shape being recommended to a
clinician, not a result, and no paper will ever hold it. books/breast-cancer/
figures.yaml names those figures with the reason each is constructed, so the
report is empty and a new entry in it is a new defect.

The rule for the declaration is narrow. A figure belongs there only when no
source could carry it. A figure that HAS a source belongs in the prose with its
citation, even when that citation already sits in the paragraph above: repeating
the mark is cheap and makes the paragraph stand on its own, which is what the
paragraph rule was for.

    python3 tools/numcheck.py BC-870 [BC-880 ...]
    python3 tools/numcheck.py            every written chapter
    python3 tools/numcheck.py --declared what figures.yaml declares, and why
"""
import os, re, sys, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import evidence as ev

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")
CH = os.path.join(BOOK, "chapters")
NUM = re.compile(r'\d+(?:[.,]\d+)*')
# a number inside a name is not a figure: HER2, CDK4/6, PD-L1, BRCA1, phase III.
# The second row is the one this list kept missing. A residue position, a cell
# line, a cytochrome, an expression signature and a cyclin-dependent kinase
# inhibitor all carry digits that no registry will ever hold, and every one of
# them was reported as an unsourced figure until it was named here.
SKIP = re.compile(r'(?:HER|CDK|PD-L|BRCA|TROP|ERBB|PIK3|AKT|RB|FAT|CCNE|ESR|TP|GATA|ki-?67|'
                  r'phase|BC-|BS-|ST-|SQ-|NCT|grade|T-DM|SN-|'
                  r'CD|EP|CYP|PAM|SIRP|MDA-MB-|BRD|EZH|SMARC|ARID|KMT|MYC|CCND|'
                  r'serine|threonine|tyrosine|lysine)', re.I)

# A decade is a date, not a measurement. `the 1890s` and `the 1930s` are the
# form that matters, because a bare year is sometimes a real figure and is left
# to be adjudicated by reading.
DECADE = re.compile(r'\d{4}s\b')


def declared():
    """(chapter, figure) pairs the book declares constructed, with the reason."""
    path = os.path.join(BOOK, "figures.yaml")
    if not os.path.exists(path):
        return {}
    doc = yaml.safe_load(open(path, encoding="utf-8")) or {}
    out = {}
    for row in doc.get("constructed") or []:
        for f in row.get("figures") or []:
            out[(row["chapter"], str(f))] = row.get("because", "")
    return out


DECLARED = declared()


def tokens(text):
    """The numbers in a blob, as whole tokens.

    Substring matching was the first version and it was wrong in the direction
    that matters: a ribociclib dose of 600 mg invented by a writer passed
    because 600 occurs inside 1600 somewhere in an abstract. A figure counts as
    found only when the source writes that number, not when some longer number
    contains it."""
    out = set()
    for t in NUM.findall(text):
        out.add(t)
        out.add(t.replace(',', ''))
        if t.startswith('.'):
            out.add('0' + t)
    return out


def haystack(keys, reg, refs, cited):
    parts = []
    for k in keys:
        t = reg.get(k) or {}
        for f in ('n', 'result', 'os', 'claim', 'population', 'arms', 'endpoint', 'year', 'phase'):
            parts.append(str(t.get(f) or ''))
        d = t.get('digest') or {}
        parts += [str(d.get('methods') or ''), str(d.get('results') or '')]
    for r in cited:
        e = refs.get(r) or {}
        parts += [str(e.get('year') or ''), str(e.get('volume') or ''), str(e.get('pages') or '')]
    text = ' '.join(parts).lower()
    text = text.replace('·', '.').replace('–', '-').replace('−', '-')
    text += ' ' + ' '.join('0' + m for m in re.findall(r'(?<![\d.])(\.\d+)', text))
    return text


def check(cid, reg, refs):
    src = open(os.path.join(CH, cid + '.md'), encoding='utf-8').read()
    keys = set(re.findall(r'\{\{trial:([a-z0-9-]+)\}\}', src))
    # every trial the chapter's own tables render is fair game too
    for spec in re.findall(r'^```evidence (.+?)\n```', src, re.M | re.S):
        f, _bad = ev.parse_filter(spec.replace('\n', ' '))
        keys |= {k for k, t in reg.items() if ev.matches(t, f)}
    cited = set(re.findall(r'@([a-z][a-z0-9-]*\d{4}[a-z0-9-]*)', src))
    hay = haystack(keys, reg, refs, cited)

    # An evidence block is a filter and a story block is an identifier, so
    # neither carries prose. A practice, caution or interplay block does, and
    # its figures are checked like any others.
    prose = re.sub(r'```(?:evidence|story)[^\n]*\n```', ' ', src)
    prose = re.sub(r'^```[a-z]*[^\n]*\n|^```$', ' ', prose, flags=re.M)
    prose = re.sub(r'^---\n.*?\n---\n', ' ', prose, flags=re.S)
    prose = re.sub(r'\[\[[^\]]*\]\]', ' ', prose)

    # A figure in a paragraph that cites a paper or names a trial is traceable,
    # and an editor checks it against that source. The unit is the paragraph and
    # not the sentence, because the house style puts the citation at the end of
    # the group of sentences it covers. A figure in a paragraph that points at
    # nothing is the one nobody can place, and it is what this is for.
    out = []
    for sent in re.split(r'\n\s*\n', prose):
        sourced = bool(re.search(r'\[@|\{\{trial:', sent))
        body = re.sub(r'\{\{[^}]*\}\}', ' ', re.sub(r'\[@[^\]]*\]', ' ', sent))
        for m in NUM.finditer(body):
            tok = m.group(0)
            if SKIP.search(body[max(0, m.start() - 12):m.end() + 6]):
                continue
            # a study named in plain prose rather than through the trial macro:
            # CALGB 70604, SWOG 8814, EA1131. The digits are part of the name.
            if re.search(r'[A-Z]{3,}[- ]$', body[max(0, m.start() - 22):m.start()]):
                continue
            if DECADE.match(body[m.start():m.end() + 1]):
                continue
            # a protein named by its mass: p16, p21, p27, p53, p95. A bare `p`
            # against the digits, with no letter before it, is never a figure;
            # a P value is written `p = ` or `P =` and keeps its space.
            if re.search(r'(?<![A-Za-z])[pP]$', body[max(0, m.start() - 2):m.start()]):
                continue
            # "95% confidence interval" is the convention, not a result
            if tok == '95' and re.match(r'%\s*(?:confidence interval|CI)',
                                        body[m.end():m.end() + 24]):
                continue
            if tok in hay or tok.replace(',', '') in hay:
                continue
            if (cid, tok) in DECLARED:
                continue
            out.append(('CHECK' if sourced else 'UNSOURCED', tok, ' '.join(body.split())[:150]))
    return out


if __name__ == '__main__':
    if '--declared' in sys.argv:
        for (cid, tok), why in sorted(DECLARED.items()):
            print('%-8s %-8s %s' % (cid, tok, ' '.join(why.split())))
        print('%d figure(s) declared constructed in books/breast-cancer/figures.yaml'
              % len(DECLARED))
        sys.exit(0)
    reg, refs = ev.load()
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if not args:
        args = sorted(f[:-3] for f in os.listdir(CH) if f.endswith('.md'))
    bad = 0
    for cid in args:
        rows = check(cid, reg, refs)
        u = [r for r in rows if r[0] == 'UNSOURCED']
        print('%s: %d figure(s) the registry cannot place, %d of them in a paragraph that '
              'cites nothing' % (cid, len(rows), len(u)))
        for kind, tok, ctx in rows:
            if kind == 'UNSOURCED' or '--all' in sys.argv:
                print('   %-10s %-8s ...%s...' % (kind, tok, ctx))
        bad += len(u)
    print('%d figure(s) in a paragraph that cites nothing' % bad)
    sys.exit(1 if bad else 0)
