#!/usr/bin/env python3
"""Prove that a restyle of the clinical chapters changed no words (W0-HARNESS, C2-textdiff).

    python3 textdiff.py snapshot [--force]    # docs/breast-cancer/BC-*.html -> baselines/bc-text/
    python3 textdiff.py                        # compare docs/ now against the snapshot
    python3 textdiff.py compare [--new DIR] [--only BC-900,BC-500] [--max N]

Both reads touch docs/, so run them through architect/locked.sh.

The snapshot keeps each chapter's built HTML (gzipped) plus a manifest of hashes, so the rules
below run on the same extraction old and new, and can be refined later against the same
snapshot. Everything is compared inside the chapter body (.main .col); the sidebar, the bar and
<head> are presentation.

THE RULES (DESIGN.md section 6, W3-CLINIC)
 (i)   Every p, li, h1-h4, dt and dd outside .story, .evidence, .refs, .chapnav (and outside the
       new caption lines p.ev-title / p.ev-note and details.refs-list) has the same text, in the
       same order.
 (ii)  Per evidence table (table.trials, in order):
       - the multiset of body-cell texts is equal. Each span[data-col] counts as its own cell,
         and so does each citation group (sup) wherever it sits, because the Ref column's
         citation moves beside the trial name. What is left of a cell is one more cell, with the
         ' · ' joiners of the meta line removed. Empty cells are dropped (a folded column leaves
         none behind);
       - header texts may only be folded away, never added or renamed (new heads are a
         sub-multiset of the old);
       - the caption survives: p.ev-title + ' ' + p.ev-note equals the old p.ct-cap.
 (iii) Stories (div.story, in order): every question (p.sq-ask), every move (dl.sq-moves dt and
       dd) and the trial line (p.sq-trials) are identical. A where, title or premise line
       (p.st-where, p.st-title, p.st-premise) may disappear only if the same text appeared in an
       earlier story of that chapter; it may never change. A story may gain one line, the
       '<title>, continued' kicker, naming its own title.
 (iv)  Reference entries (ol.refs li) are identical, in order. An 'All N references' summary
       must count them.
 (v)   The only new visible strings are 'All N references' and '<title>, continued'. A text node
       counts as new when its text appears nowhere in the old chapter body (a caption split in
       two, or a cell moved, is not new).

Prints PASS, or the differences per chapter, and exits 1 on any difference."""
import collections, difflib, gzip, hashlib, html.parser, json, os, re, sys

ROOT = '/home/user/library'
UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(UI, 'baselines', 'bc-text')
DOCS_BOOK = os.path.join(ROOT, 'docs', 'breast-cancer')

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param',
        'source', 'track', 'wbr'}


class Node:
    __slots__ = ('tag', 'attrs', 'kids', 'parent')

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.kids, self.parent = tag, attrs, [], parent

    @property
    def cls(self):
        return set((self.attrs.get('class') or '').split())

    def iter(self):
        yield self
        for k in self.kids:
            if isinstance(k, Node):
                yield from k.iter()

    def ancestors(self):
        a = self.parent
        while a is not None:
            yield a
            a = a.parent

    def text(self, skip=None):
        out = []
        def walk(n):
            for k in n.kids:
                if isinstance(k, str):
                    out.append(k)
                elif k.tag not in ('script', 'style') and not (skip and skip(k)):
                    walk(k)
        walk(self)
        return norm(''.join(out))


class Tree(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root', {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs), self.cur)
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, dict(attrs), self.cur))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def norm(s):
    return ' '.join(s.split())


def parse(text):
    t = Tree()
    t.feed(text)
    t.close()
    return t.root


def column(root):
    for n in root.iter():
        if n.tag == 'main' and 'main' in n.cls:
            for c in n.iter():
                if c.tag == 'div' and 'col' in c.cls:
                    return c
    raise ValueError('no .main .col')


def inside(n, classes, tags=()):
    for a in [n] + list(n.ancestors()):
        if a.cls & classes or a.tag in tags:
            return True
    return False


BLOCKS = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'dt', 'dd'}
FENCED = {'story', 'evidence', 'refs', 'chapnav', 'refs-list', 'ev-title', 'ev-note'}
JOINER = re.compile(r'(^|\s)·(?=\s|$)')


def _cut(k):
    return k.tag == 'sup' or 'data-col' in k.attrs


def split_cell(td):
    """A body cell as the multiset rule sees it: each span[data-col] and each citation group
    (sup) is its own cell; the rest of the cell, without the meta line's ' · ' joiners, is one
    more."""
    parts = []
    def walk(n):
        for k in n.kids:
            if isinstance(k, Node):
                if _cut(k):
                    parts.append(k.text())
                else:
                    walk(k)
    walk(td)
    parts.append(norm(JOINER.sub(' ', td.text(skip=_cut))))
    return parts


def model(text):
    col = column(parse(text))
    m = {}
    # (i) blocks outside the apparatus
    m['blocks'] = [n.text() for n in col.iter() if n.tag in BLOCKS and not inside(n, FENCED)]
    # (ii) evidence tables
    tables = []
    for t in col.iter():
        if t.tag != 'table' or 'trials' not in t.cls:
            continue
        ev = next((a for a in t.ancestors() if 'evidence' in a.cls), None)
        cells, heads = [], []
        for c in t.iter():
            if c.tag == 'th':
                heads.append(c.text())
            elif c.tag == 'td':
                cells.extend(split_cell(c))
        cap = None
        # the caption lives inside this evidence block, or (new markup) as p.ev-title and
        # p.ev-note directly before it; never inside a neighbouring block
        box = ev if ev is not None else t
        within = list(box.iter())
        before = []
        if box.parent is not None:
            sibs = [k for k in box.parent.kids if isinstance(k, Node)]
            i = sibs.index(box)
            while i > 0 and sibs[i - 1].cls & {'ev-title', 'ev-note'}:
                i -= 1
                before.insert(0, sibs[i])
        old = [n for n in within if 'ct-cap' in n.cls]
        ttl = [n for n in before + within if 'ev-title' in n.cls]
        note = [n for n in before + within if 'ev-note' in n.cls]
        if old:
            cap = old[0].text()
        elif ttl:
            cap = norm(ttl[-1].text() + ' ' + (note[-1].text() if note else ''))
        tables.append({'cells': [x for x in cells if x], 'heads': heads, 'cap': cap})
    m['tables'] = tables
    # (iii) stories
    stories = []
    for s in col.iter():
        if s.tag != 'div' or 'story' not in s.cls:
            continue
        head = {}
        for c in ('st-where', 'st-title', 'st-premise'):
            x = next((n for n in s.iter() if c in n.cls), None)
            if x is not None:
                head[c] = x.text()
        stories.append({
            'head': head,
            'asks': [n.text() for n in s.iter() if 'sq-ask' in n.cls],
            'moves': [n.text() for n in s.iter() if n.tag in ('dt', 'dd')
                      and any('sq-moves' in a.cls for a in n.ancestors())],
            'trials': [n.text() for n in s.iter() if 'sq-trials' in n.cls],
            'lines': [n.text() for n in s.iter() if n.tag == 'p'],
        })
    m['stories'] = stories
    # (iv) references
    m['refs'] = [n.text() for n in col.iter() if n.tag == 'li'
                 and any(a.tag == 'ol' and 'refs' in a.cls for a in n.ancestors())]
    m['summaries'] = [n.text() for n in col.iter() if n.tag == 'summary'
                      and any('refs-list' in a.cls for a in n.ancestors())]
    # (v) every visible text node, and the whole body as one string
    nodes = []
    def walk(n):
        for k in n.kids:
            if isinstance(k, str):
                t = norm(k)
                if t:
                    nodes.append(t)
            elif k.tag not in ('script', 'style', 'template'):
                walk(k)
    walk(col)
    m['nodes'] = nodes
    m['all'] = ' '.join(nodes)
    return m


def compare(old, new):
    """A list of human-readable differences; empty means PASS."""
    d = []
    def seqdiff(label, a, b, cap=6):
        if a == b:
            return
        out = []
        lines = [l for l in difflib.unified_diff(a, b, 'old', 'new', n=0, lineterm='')
                 if not l.startswith(('---', '+++', '@@'))]
        for j, line in enumerate(lines):
            # centre a changed line on its first differing character, so a one-word edit in
            # a long paragraph is visible
            pair = lines[j + 1] if line[:1] == '-' and j + 1 < len(lines) and lines[j + 1][:1] == '+' \
                else lines[j - 1] if line[:1] == '+' and j > 0 and lines[j - 1][:1] == '-' else None
            start = 0
            if pair is not None:
                p = 0
                while p < min(len(line), len(pair)) - 1 and line[p + 1] == pair[p + 1]:
                    p += 1
                start = max(0, p - 70)
            out.append('      ' + line[:1] + ('...' if start else '') + line[1 + start:1 + start + 170])
        d.append('%s differ (%d old, %d new):\n%s' % (label, len(a), len(b),
                 '\n'.join(out[:cap]) + ('\n      ...' if len(out) > cap else '')))
    # (i)
    seqdiff('(i) blocks outside the apparatus', old['blocks'], new['blocks'])
    # (ii)
    if len(old['tables']) != len(new['tables']):
        d.append('(ii) evidence tables: %d old, %d new' % (len(old['tables']), len(new['tables'])))
    for i, (a, b) in enumerate(zip(old['tables'], new['tables'])):
        ca, cb = collections.Counter(a['cells']), collections.Counter(b['cells'])
        if ca != cb:
            lost, gained = list((ca - cb).elements()), list((cb - ca).elements())
            d.append('(ii) table %d cells differ: lost %s; gained %s' % (
                i + 1, [x[:60] for x in lost[:4]], [x[:60] for x in gained[:4]]))
        extra = collections.Counter(b['heads']) - collections.Counter(a['heads'])
        if extra:
            d.append('(ii) table %d gained header text %s' % (i + 1, list(extra.elements())))
        if a['cap'] != b['cap']:
            d.append('(ii) table %d caption differs:\n      old %r\n      new %r'
                     % (i + 1, (a['cap'] or '')[:160], (b['cap'] or '')[:160]))
    # (iii)
    so, sn = old['stories'], new['stories']
    if len(so) != len(sn):
        d.append('(iii) stories: %d old, %d new' % (len(so), len(sn)))
    seen = collections.defaultdict(set)      # header texts shown so far, in the new chapter
    for i, (a, b) in enumerate(zip(so, sn)):
        for k in ('asks', 'moves', 'trials'):
            seqdiff('(iii) story %d %s' % (i + 1, k), a[k], b[k])
        for c, t in a['head'].items():
            if c in b['head']:
                if b['head'][c] != t:
                    d.append('(iii) story %d %s changed: %r -> %r' % (i + 1, c, t[:80], b['head'][c][:80]))
            elif t not in seen[c]:
                d.append('(iii) story %d dropped its %s %r, which no earlier story showed'
                         % (i + 1, c, t[:80]))
        for c, t in b['head'].items():
            if c not in a['head']:
                d.append('(iii) story %d gained a %s %r' % (i + 1, c, t[:80]))
            seen[c].add(t)
        allowed = set(a['lines'])
        if 'st-title' in a['head']:
            allowed.add(a['head']['st-title'] + ', continued')
        for t in b['lines']:
            if t not in allowed:
                d.append('(iii) story %d gained a line %r' % (i + 1, t[:100]))
    # (iv)
    seqdiff('(iv) references', old['refs'], new['refs'])
    for s in new['summaries']:
        m = re.fullmatch(r'All (\d+) references?', s)
        if not m or int(m.group(1)) != len(new['refs']):
            d.append('(iv) the references summary %r does not count the %d entries'
                     % (s, len(new['refs'])))
    # (v)
    titles = {s['head'].get('st-title') for s in so} - {None}
    newbits = []
    for t in new['nodes']:
        if t in old['all']:
            continue
        m = re.fullmatch(r'All (\d+) references?', t)
        if m and int(m.group(1)) == len(new['refs']):
            continue
        if t.endswith(', continued') and t[:-len(', continued')] in titles:
            continue
        newbits.append(t)
    if newbits:
        c = collections.Counter(newbits)
        d.append('(v) new visible strings: %s' % ', '.join(
            '%r x%d' % (k[:60], v) for k, v in c.most_common(8)))
    return d


def chapters(folder):
    return sorted(f for f in os.listdir(folder) if re.fullmatch(r'BC-.*\.html', f))


def snapshot(force):
    if os.path.isdir(SNAP) and os.listdir(SNAP) and not force:
        raise SystemExit('textdiff: %s exists; it is the baseline. Pass --force to replace it.' % SNAP)
    os.makedirs(SNAP, exist_ok=True)
    man = {}
    for f in chapters(DOCS_BOOK):
        raw = open(os.path.join(DOCS_BOOK, f), 'rb').read()
        with gzip.open(os.path.join(SNAP, f + '.gz'), 'wb', compresslevel=9) as fh:
            fh.write(raw)
        m = model(raw.decode('utf-8'))
        man[f] = {'sha256': hashlib.sha256(raw).hexdigest(), 'blocks': len(m['blocks']),
                  'tables': len(m['tables']), 'stories': len(m['stories']), 'refs': len(m['refs'])}
    ref = open(os.path.join(UI, 'baselines', 'REF')).read().strip() \
        if os.path.exists(os.path.join(UI, 'baselines', 'REF')) else None
    json.dump({'ref': ref, 'chapters': man}, open(os.path.join(SNAP, 'MANIFEST.json'), 'w'),
              indent=1, sort_keys=True)
    t = collections.Counter()
    for v in man.values():
        for k in ('blocks', 'tables', 'stories', 'refs'):
            t[k] += v[k]
    print('textdiff: snapshot of %d chapters -> %s  (%s)' % (len(man), SNAP, dict(t)))


def main():
    args = sys.argv[1:]
    if args[:1] == ['snapshot']:
        return snapshot('--force' in args)
    new_dir = DOCS_BOOK
    if '--new' in args:
        new_dir = os.path.abspath(args[args.index('--new') + 1])
    only = None
    if '--only' in args:
        only = {x if x.endswith('.html') else x + '.html'
                for x in args[args.index('--only') + 1].split(',')}
    cap = int(args[args.index('--max') + 1]) if '--max' in args else 12
    if not os.path.isdir(SNAP):
        raise SystemExit('textdiff: no snapshot at %s; run `textdiff.py snapshot` first' % SNAP)
    old_set = {f[:-3] for f in os.listdir(SNAP) if f.endswith('.html.gz')}
    new_set = set(chapters(new_dir))
    if only:
        old_set &= only
        new_set &= only
    bad = 0
    for f in sorted(old_set ^ new_set):
        print('  %s: %s' % (f, 'missing now' if f in old_set else 'new chapter, not in the snapshot'))
        bad += 1
    checked = 0
    for f in sorted(old_set & new_set):
        with gzip.open(os.path.join(SNAP, f + '.gz'), 'rb') as fh:
            old = model(fh.read().decode('utf-8'))
        new = model(open(os.path.join(new_dir, f), encoding='utf-8').read())
        diffs = compare(old, new)
        checked += 1
        if diffs:
            bad += 1
            if bad <= cap:
                print('  %s' % f)
                for x in diffs:
                    print('    ' + x)
    if bad > cap:
        print('  ... %d more chapter(s) differ' % (bad - cap))
    if bad:
        print('textdiff: FAIL, %d of %d chapter(s) differ from the snapshot' % (bad, checked))
        return 1
    print('textdiff: PASS (%d chapters: the prose, the evidence cells and captions, the stories '
          'and the references all match the snapshot)' % checked)
    return 0


if __name__ == '__main__':
    sys.exit(main() or 0)
