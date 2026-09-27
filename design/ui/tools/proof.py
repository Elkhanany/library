#!/usr/bin/env python3
"""Proof pages: one chapter-shaped page per chaptered book holding one of every component, cut
from the built docs/ on every run so it tracks the markup (W0-HARNESS, C1-proof-page).

    python3 proof.py                   # reads docs/: run through locked.sh
    python3 prodshot.py OUT breast-cancer/_proof.html newton-to-mtheory/_proof.html \\
        --overlay scratchpad/ui/proof --widths 390,1280 --themes light,dark --full

Writes scratchpad/ui/proof/<slug>/_proof.html and _proof.json (what was taken from where). It is
never written into docs/: prodshot --overlay serves it at /library/<slug>/_proof.html, and its
assets resolve relatively (assets/book.css, ../assets/nav.css ...) against docs/, like a chapter.

The page is a real chapter (the template) with its .main .col replaced and #sb-toc emptied (book.js
rebuilds the list from the headings). Components, each copied verbatim from a built page:
  both:      eyebrow, h1, subtitle; an h2, h3 and h4 each with the paragraph after it; one of every
             callout type; the chapter foot
  clinical:  a story and its second appearance in the same chapter (the 'continued' case); the
             widest evidence table with its caption; that chapter's references
  physics:   the preambles ('Where we are', 'Tools you'll need'); a long and a short numbered
             equation; a figure with its chapter's script; the longest sitting break; a worked
             example and a grind block
A small monospace label before each component names it and its source page."""
import html, html.parser, json, os, re, sys

ROOT = '/home/user/library'
UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(UI, 'proof')
DOCS = os.path.join(ROOT, 'docs')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param',
        'source', 'track', 'wbr'}


class El:
    __slots__ = ('tag', 'attrs', 'start', 'end', 'kids', 'parent')

    def __init__(self, tag, attrs, start, parent):
        self.tag, self.attrs, self.start, self.end, self.kids, self.parent = tag, attrs, start, None, [], parent

    @property
    def cls(self):
        return set((self.attrs.get('class') or '').split())

    def iter(self):
        yield self
        for k in self.kids:
            yield from k.iter()


class Spans(html.parser.HTMLParser):
    """Elements with their [start, end) offsets in the source, for verbatim copying."""

    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.src = src
        self.lines = [0]
        for m in re.finditer('\n', src):
            self.lines.append(m.end())
        self.root = El('#root', {}, 0, None)
        self.cur = self.root
        self.feed(src)
        self.close()

    def at(self):
        ln, col = self.getpos()
        return self.lines[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        s = self.at()
        e = El(tag, dict(attrs), s, self.cur)
        self.cur.kids.append(e)
        if tag in VOID:
            e.end = s + len(self.get_starttag_text() or '')
        else:
            self.cur = e

    def handle_startendtag(self, tag, attrs):
        s = self.at()
        e = El(tag, dict(attrs), s, self.cur)
        e.end = s + len(self.get_starttag_text() or '')
        self.cur.kids.append(e)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is None:
            return
        s = self.at()
        close = self.src.find('>', s)
        # anything opened inside n and never closed ends where n ends
        m = self.cur
        while m is not n:
            m.end = s
            m = m.parent
        n.end = close + 1
        self.cur = n.parent


def text(src, e):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', src[e.start:e.end])).split())


class Page:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.src = open(path, encoding='utf-8').read()
        self.tree = Spans(self.src).root
        self.col = next(e for e in self.tree.iter() if e.tag == 'div' and 'col' in e.cls
                        and e.parent is not None and e.parent.tag == 'main')

    def frag(self, e):
        return self.src[e.start:e.end]

    def find(self, pred, within=None):
        return [e for e in (within or self.col).iter() if pred(e)]

    def after(self, e):
        """The element right after e among its siblings (for 'a heading and its paragraph')."""
        sibs = e.parent.kids
        i = sibs.index(e)
        return sibs[i + 1] if i + 1 < len(sibs) else None


def label(what, src):
    return ('<p class="proof-label" style="font:11px/1.4 ui-monospace,Menlo,Consolas,monospace;'
            'letter-spacing:0;text-transform:none;color:inherit;opacity:1;margin:2.4em 0 .5em;'
            'padding-top:.35em;border-top:1px dashed currentColor">proof &middot; %s &middot; %s</p>\n'
            % (html.escape(what), html.escape(src)))


def pages(slug, pat):
    d = os.path.join(DOCS, slug)
    return [Page(os.path.join(d, f)) for f in sorted(os.listdir(d)) if re.fullmatch(pat, f)]


def pick_callouts(chs, out, took):
    kinds = {}
    for p in chs:
        for e in p.find(lambda e: e.tag == 'div' and 'callout' in e.cls):
            k = ' '.join(sorted(e.cls - {'callout'})) or 'plain'
            if k == 'where':
                continue            # shown with the preambles
            n = len(text(p.src, e))
            best = kinds.get(k)
            score = abs(n - 600)            # a representative length, not the shortest
            if best is None or score < best[0]:
                kinds[k] = (score, p, e)
    for k in sorted(kinds):
        _s, p, e = kinds[k]
        out.append(label('callout ' + k, p.name) + p.frag(e))
        took.append({'component': 'callout ' + k, 'from': p.name})


def headings(chs, out, took, template):
    for lvl in ('h2', 'h3', 'h4'):
        for p in [template] + [c for c in chs if c is not template]:
            hs = p.find(lambda e: e.tag == lvl and 'refs-head' not in e.cls)
            got = None
            for h in hs:
                nx = p.after(h)
                if nx is not None and nx.tag == 'p' and 100 < len(text(p.src, nx)) < 900:
                    got = (h, nx)
                    break
            if got:
                h, nx = got
                out.append(label(lvl + ' and the paragraph after it', p.name) + p.frag(h) + '\n\n' + p.frag(nx))
                took.append({'component': lvl, 'from': p.name})
                break
        else:
            took.append({'component': lvl, 'from': None, 'note': 'no %s in this book\'s chapters' % lvl})


def build(slug, template_name, chapter_pat):
    chs = pages(slug, chapter_pat)
    by = {p.name: p for p in chs}
    tpl = by[template_name]
    out, took = [], []
    # the chapter head, from the template
    head = []
    for e in tpl.col.kids:
        if e.tag == 'h1' or e.cls & {'eyebrow', 'subtitle'}:
            head.append(tpl.frag(e))
        if e.tag == 'h1':
            nx = tpl.after(e)
            if nx is not None and 'subtitle' in nx.cls:
                head.append(tpl.frag(nx))
            break
    out.append('\n'.join(dict.fromkeys(head)))
    took.append({'component': 'eyebrow, h1, subtitle', 'from': tpl.name})

    if slug == 'newton-to-mtheory':
        # the preambles
        for p in chs:
            w = p.find(lambda e: e.tag == 'div' and {'callout', 'where'} <= e.cls)
            t = p.find(lambda e: 'tools' in e.cls)
            if w and t:
                out.append(label('preamble: where we are', p.name) + p.frag(w[0]))
                out.append(label("preamble: tools you'll need", p.name) + p.frag(t[0]))
                took.append({'component': 'preambles', 'from': p.name})
                break
    headings(chs, out, took, tpl)
    pick_callouts(chs + ([Page(os.path.join(DOCS, slug, 'throughline.html'))]
                         if os.path.exists(os.path.join(DOCS, slug, 'throughline.html')) else []),
                  out, took)

    scripts = []
    if slug == 'breast-cancer':
        # a story and its second appearance in one chapter
        for p in chs:
            st = p.find(lambda e: e.tag == 'div' and 'story' in e.cls)
            seen = {}
            pair = None
            for s in st:
                t = next((text(p.src, e) for e in s.iter() if 'st-title' in e.cls), None)
                if t is None:
                    t = next((text(p.src, e).rsplit(', continued', 1)[0] for e in s.iter()
                              if 'continued' in text(p.src, e)[-12:]), None)
                if t in seen:
                    pair = (seen[t], s)
                    break
                seen[t] = s
            if pair:
                out.append(label('story, first appearance', p.name) + p.frag(pair[0]))
                out.append(label('the same story, second appearance', p.name) + p.frag(pair[1]))
                took.append({'component': 'story with a continuation', 'from': p.name})
                break
        # the widest evidence table, its caption, and that chapter's references
        best = None
        for p in chs:
            for ev in p.find(lambda e: e.tag == 'div' and 'evidence' in e.cls):
                cols = len([e for e in ev.iter() if e.tag == 'th'])
                size = len(text(p.src, ev))
                if best is None or (cols, size) > best[0]:
                    best = ((cols, size), p, ev)
        (_k, p, ev) = best
        pre = ''
        sibs = ev.parent.kids
        i = sibs.index(ev)
        while i > 0 and sibs[i - 1].cls & {'ev-title', 'ev-note'}:
            i -= 1
            pre = p.frag(sibs[i]) + '\n' + pre
        out.append(label('the widest evidence table (%d columns)' % _k[0], p.name) + pre + p.frag(ev))
        took.append({'component': 'widest evidence table', 'from': p.name, 'columns': _k[0]})
        rh = p.find(lambda e: e.attrs.get('id') == 'references')
        if rh:
            nx = p.after(rh[0])
            out.append(label('the references', p.name) + p.frag(rh[0]) + '\n\n' + (p.frag(nx) if nx else ''))
            took.append({'component': 'references', 'from': p.name})
    else:
        # a long and a short numbered equation
        eqs = []
        for p in chs:
            for e in p.find(lambda e: e.tag == 'div' and 'eq' in e.cls):
                tex = ' '.join(re.findall(r'<annotation encoding="application/x-tex">(.*?)</annotation>',
                                          p.frag(e), re.S))
                eqs.append((len(tex), p, e))
        eqs.sort(key=lambda x: x[0])
        short = next(x for x in eqs if x[0] >= 12)
        long_ = eqs[-1]
        for what, (n, p, e) in (('a long numbered equation', long_), ('a short numbered equation', short)):
            out.append(label(what + ' (%d characters of TeX)' % n, p.name) + p.frag(e))
            took.append({'component': what, 'from': p.name, 'id': e.attrs.get('id')})
        # a figure whose chapter script touches only that figure
        for p in chs:
            figs = p.find(lambda e: e.tag == 'figure' and 'fig' in e.cls)
            if len(figs) != 1:
                continue
            body_scripts = [e for e in p.tree.iter() if e.tag == 'script' and 'src' not in e.attrs
                            and e.start > p.col.end]
            js = ''.join(p.frag(s) for s in body_scripts)
            ids = set(re.findall(r"getElementById\(\s*'([^']+)'\s*\)", js)) \
                | set(re.findall(r'getElementById\(\s*"([^"]+)"\s*\)', js))
            ids |= set(re.findall(r"'((?:v|o|b|fig)-[\w-]+)'", js))
            have = {e.attrs.get('id') for e in figs[0].iter()} - {None}
            if js and ids and ids <= have:
                out.append(label('a figure, with its chapter script', p.name) + p.frag(figs[0]))
                scripts = [p.frag(s) for s in body_scripts]
                took.append({'component': 'figure', 'from': p.name})
                break
        # the longest sitting break
        pauses = [(len(text(p.src, e)), p, e) for p in chs for e in p.find(lambda e: 'pause' in e.cls)]
        n, p, e = max(pauses, key=lambda x: x[0])
        out.append(label('a sitting break (the longest label)', p.name) + p.frag(e))
        took.append({'component': 'sitting break', 'from': p.name})
        for cls, what in (('worked', 'a worked example'), ('grind', 'a grind block')):
            cand = [(abs(len(text(p.src, e)) - 900), p, e) for p in chs
                    for e in p.find(lambda e, c=cls: c in e.cls and e.tag in ('div', 'details'))]
            if cand:
                _n, p, e = min(cand, key=lambda x: x[0])
                out.append(label(what, p.name) + p.frag(e))
                took.append({'component': what, 'from': p.name})

    # the chapter foot, from the template
    foot = tpl.find(lambda e: e.tag == 'nav' and 'chapnav' in e.cls)
    if foot:
        out.append(label('the chapter foot', tpl.name) + tpl.frag(foot[0]))
        took.append({'component': 'chapter foot', 'from': tpl.name})

    # assemble: the template with its column replaced, the TOC emptied, its own scripts swapped
    src = tpl.src
    col = tpl.col
    inner_start = src.find('>', col.start) + 1
    inner_end = col.end - len('</div>')
    body = '\n\n'.join(out)
    page = src[:inner_start] + '\n\n' + body + '\n\n' + src[inner_end:]
    page = re.sub(r'(<div id="sb-toc">).*?(</div>)', r'\1\2', page, count=1, flags=re.S)
    page = re.sub(r'<title>.*?</title>', '<title>Proof page, %s</title>' % slug, page, count=1, flags=re.S)
    # drop the template's own inline chapter scripts (after the column), keep book.js, add the figure's
    tail_at = page.find('<script src="assets/book.js"></script>')
    if tail_at >= 0:
        rest = page[tail_at:]
        head_part = page[:tail_at]
        rest = re.sub(r'<script>(?:(?!</script>).)*</script>', '', rest, flags=re.S)
        rest = rest.replace('<script src="assets/book.js"></script>',
                            '<script src="assets/book.js"></script>\n' + '\n'.join(scripts), 1)
        page = head_part + rest
    d = os.path.join(OUT, slug)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, '_proof.html'), 'w', encoding='utf-8').write(page)
    json.dump({'template': tpl.name, 'components': took}, open(os.path.join(d, '_proof.json'), 'w'), indent=1)
    print('%s: %d components -> %s' % (slug, len(took), os.path.join(d, '_proof.html')))
    for t in took:
        print('   %-34s %s' % (t['component'], t.get('from') or ('-- ' + t.get('note', ''))))


build('breast-cancer', 'BC-900.html', r'BC-.*\.html')
build('newton-to-mtheory', 'ch2-1.html', r'ch\d+-\d+\.html')
