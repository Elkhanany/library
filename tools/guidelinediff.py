#!/usr/bin/env python3
"""What a guideline cites that the book does not.

Takes a guideline's reference list, already parsed to CSV with one row per
numbered reference, and reports which of its PubMed identifiers are absent from
`references.yaml`. The point is not the count. It is the claim column: a missing
identifier arrives with the sentence the guideline attached to it, so a gap can
be read as a clinical assertion the book does not source rather than as a
citation it happens not to carry.

Required CSV columns are `pmid` and `citation`. Everything else is optional and
improves the report where present: `topic` and `section` bucket the gaps,
`subtopic` and `claim` say what each one was supporting, `year` sorts them, and
`doi` and `url` carry the references that have no identifier at all.

Those identifier-free rows are reported separately and are not a gap in the
same sense. A meeting abstract or a DOI-only entry cannot be matched against a
PubMed identifier, so the book may well cite the same work under a different
handle. They are listed because that is where the newest readouts sit.

Once those rows have been read, the resolution is written down in a YAML file
with one entry per row: the keys that carry it and the basis for saying so.
`--resolved` checks that file against the store and the chapters, so a
resolution that names a key nobody cites is reported rather than trusted.

  python3 tools/guidelinediff.py nccn.csv                    # the gap report
  python3 tools/guidelinediff.py nccn.csv --topic systemic   # one bucket
  python3 tools/guidelinediff.py nccn.csv --covered          # what we do carry
  python3 tools/guidelinediff.py nccn.csv --json out.json    # for a later pass
  python3 tools/guidelinediff.py nccn.csv --resolved map.yaml
"""
import argparse, collections, csv, json, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, 'books', 'breast-cancer')


def book_pmids(book=BOOK):
    """Every PubMed identifier the book can cite, and the key that carries it.

    Read from the reference store rather than from the chapters, because a
    reference present in the store but not yet cited is still not a gap: the
    work has been read and keyed, and citing it is an editing decision."""
    refs = yaml.safe_load(open(os.path.join(book, 'references.yaml'), encoding='utf-8'))['refs']
    out = {}
    for key, rec in refs.items():
        pmid = str(rec.get('pmid') or '').strip()
        if pmid:
            out.setdefault(pmid, []).append(key)
    return out, refs


def cited_keys(book=BOOK):
    """The keys that actually appear in a chapter, so the report can separate
    'we have never read this' from 'we have it on file and do not cite it'."""
    ch = os.path.join(book, 'chapters')
    used = set()
    for fn in sorted(os.listdir(ch)):
        if not fn.endswith('.md'):
            continue
        for m in re.findall(r'\[@([^\]]+)\]', open(os.path.join(ch, fn), encoding='utf-8').read()):
            for k in m.split(';'):
                used.add(k.strip().lstrip('@'))
    return used


def load(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8-sig')))
    if not rows:
        sys.exit('%s: no rows' % path)
    for need in ('pmid', 'citation'):
        if need not in rows[0]:
            sys.exit('%s: no %s column' % (path, need))
    return rows


def classify(rows, have, used, keyof):
    """Three buckets, and the middle one is the interesting one.

    `missing`  the book has no reference with this identifier at all.
    `onfile`   the store carries it but no chapter cites it.
    `cited`    a chapter cites it."""
    out = {'missing': [], 'onfile': [], 'cited': [], 'nopmid': []}
    seen = set()
    for r in rows:
        pmid = (r.get('pmid') or '').strip()
        if not pmid:
            out['nopmid'].append(r)
            continue
        if pmid in seen:       # NCCN's own list repeats a few
            continue
        seen.add(pmid)
        keys = keyof.get(pmid)
        if not keys:
            out['missing'].append(r)
        elif any(k in used for k in keys):
            r = dict(r, _keys=','.join(keys))
            out['cited'].append(r)
        else:
            r = dict(r, _keys=','.join(keys))
            out['onfile'].append(r)
    return out


def shorten(s, n):
    s = ' '.join((s or '').split())
    return s if len(s) <= n else s[:n - 1] + '…'


def report(buckets, rows, topic_filter=None, show_covered=False, width=100):
    tot = len({(r.get('pmid') or '').strip() for r in rows if (r.get('pmid') or '').strip()})
    miss, onfile, cited = buckets['missing'], buckets['onfile'], buckets['cited']
    print('guideline: %d rows, %d unique identifiers, %d rows carrying none'
          % (len(rows), tot, len(buckets['nopmid'])))
    print('  in the book and cited   : %4d' % len(cited))
    print('  in the store, not cited : %4d' % len(onfile))
    print('  absent from the book    : %4d' % len(miss))

    def bucket_of(r):
        return (r.get('topic') or 'untagged').strip()

    print('\nabsent, by the guideline\'s own heading tree')
    per = collections.Counter(bucket_of(r) for r in miss)
    allper = collections.Counter(bucket_of(r) for r in miss + onfile + cited)
    for t, n in sorted(per.items(), key=lambda kv: -kv[1]):
        print('  %-38s %4d of %4d  (%d%%)' % (t, n, allper[t], round(100 * n / allper[t])))

    groups = collections.defaultdict(list)
    for r in miss:
        groups[bucket_of(r)].append(r)
    for t in sorted(groups, key=lambda k: -len(groups[k])):
        if topic_filter and topic_filter.lower() not in t.lower():
            continue
        print('\n' + '=' * width)
        print('%s  (%d absent)' % (t.upper(), len(groups[t])))
        print('=' * width)
        for r in sorted(groups[t], key=lambda r: (r.get('section') or '', -int(r.get('year') or 0))):
            sec = shorten(r.get('section') or '', 34)
            sub = shorten(r.get('subtopic') or '', 40)
            print('\n  %-8s %-4s %s' % (r.get('pmid'), r.get('year') or '', sec + (' · ' + sub if sub else '')))
            print('    %s' % shorten(r.get('citation'), width - 6))
            if r.get('claim'):
                print('    claim: %s' % shorten(r.get('claim'), width - 13))

    if show_covered:
        print('\n' + '=' * width)
        print('IN THE STORE BUT NO CHAPTER CITES IT  (%d)' % len(onfile))
        print('=' * width)
        for r in sorted(onfile, key=lambda r: bucket_of(r)):
            print('  %-8s %-30s %-18s %s'
                  % (r.get('pmid'), shorten(bucket_of(r), 30), r.get('_keys', ''),
                     shorten(r.get('citation'), width - 62)))


def resolved(path, rows, refs, used, width=100):
    """How the book carries each row that has no identifier, checked rather than trusted.

    Title matching cannot settle these rows. A meeting abstract and the paper
    that followed it share a trial and rarely a title, so the resolution is
    recorded once, with its basis, and every key it names must still exist in
    the store and still be cited in a chapter. A row the file marks not
    citable has no PubMed record, and it has to say why."""
    doc = yaml.safe_load(open(path, encoding='utf-8')) or {}
    by = {str(e['ref']): e for e in doc.get('rows') or []}
    nop = [r for r in rows if not (r.get('pmid') or '').strip()]
    tally, bad, notcit = collections.Counter(), [], []
    for r in nop:
        n = str(r.get('ref_no') or '').strip()
        e = by.get(n)
        if not e:
            bad.append('%s: no resolution recorded' % n)
            continue
        keys, basis = e.get('keys') or [], e.get('basis') or ''
        if basis == 'not-citable':
            if keys:
                bad.append('%s: marked not citable but names %s' % (n, ', '.join(keys)))
            if not e.get('note'):
                bad.append('%s: marked not citable with no reason' % n)
            notcit.append((n, e))
        elif not keys:
            bad.append('%s: basis %s names no key' % (n, basis))
        for k in keys:
            if k not in refs:
                bad.append('%s: %s is not in references.yaml' % (n, k))
            elif k not in used:
                bad.append('%s: %s is in the store and no chapter cites it' % (n, k))
        tally[basis] += 1
    stale = sorted(set(by) - {str(r.get('ref_no') or '').strip() for r in nop}, key=int)
    for n in stale:
        bad.append('%s: resolution recorded for a row that now has an identifier or does not exist' % n)

    print('\n' + '=' * width)
    print('ROWS WITH NO IDENTIFIER, AS RESOLVED IN %s' % os.path.basename(path))
    print('=' * width)
    for basis, n in tally.most_common():
        print('  %-20s %4d' % (basis, n))
    print('  %-20s %4d' % ('total', sum(tally.values())))
    if notcit:
        print('\n  not citable, and why')
        for n, e in notcit:
            print('    #%-4s %s' % (n, shorten(e.get('citation'), width - 12)))
            print('          %s' % shorten(e.get('note'), width - 10))
    if bad:
        print('\n  problems')
        for b in bad:
            print('    ' + b)
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('csv')
    ap.add_argument('--book', default=BOOK)
    ap.add_argument('--topic', help='limit the detail to one heading')
    ap.add_argument('--covered', action='store_true',
                    help='also list what the store has and no chapter cites')
    ap.add_argument('--json', metavar='PATH', help='write the buckets for a later pass')
    ap.add_argument('--resolved', metavar='YAML',
                    help='check the recorded resolution of the rows that carry no identifier')
    a = ap.parse_args(argv)

    rows = load(a.csv)
    keyof, refs = book_pmids(a.book)
    used = cited_keys(a.book)
    have = set(keyof)
    buckets = classify(rows, have, used, keyof)
    report(buckets, rows, a.topic, a.covered)
    bad = resolved(a.resolved, rows, refs, used) if a.resolved else []
    if a.json:
        json.dump(buckets, open(a.json, 'w'), indent=1)
        print('\nwrote %s' % a.json)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
