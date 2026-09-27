#!/usr/bin/env python3
"""Re-emit ONE book's front door (index.html from src/_landing.html) and its declared extra
pages (book.json "pages": the clinical book's stories.html and trials.html) in seconds, then
re-run the bar and app-layer passes. For iterating on front-door and appendix pages without
onebook.py, which re-renders every chapter first (5-6 minutes for the clinical book).

    python3 frontdoor.py <slug>              # writes docs/<slug>/..., then nav.py + pwa.py
    python3 frontdoor.py <slug> --out DIR    # writes DIR/... only, no passes (for diffing)

The page stats ({{CH}} {{PARTS}} {{WORDS}} {{EQ}} {{BOXES}}) are recomputed from the
chapters already built in docs/<slug>/, the way webbuild counts them. Also copies
shared/assets/landing.css into docs/<slug>/assets/ when the book ships one.
Contents, chapters, ledger and through-line are NOT rebuilt: those need onebook.py."""
import os, re, sys, html.parser
ROOT = '/home/user/library'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import library, webbuild
slug = sys.argv[1]
out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
bk = library.book(slug)
bp = webbuild.bp
bp.use(bk)
docs_book = bk.out

class Words(html.parser.HTMLParser):
    """textContent of .main .col minus .katex, script and style -- WORDCOUNT_JS in Python."""
    VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'wbr', 'source', 'col', 'area'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.buf, self.col, self.skip = [], [], None, None
    def handle_starttag(self, tag, attrs):
        if tag in self.VOID: return
        cls = dict(attrs).get('class') or ''
        self.stack.append(tag)
        d = len(self.stack)
        if self.col is None and tag == 'div' and cls.split()[:1] == ['col']:
            self.col = d
        elif self.col and self.skip is None and (tag in ('script', 'style') or 'katex' in cls.split()):
            self.skip = d
    def handle_endtag(self, tag):
        if tag in self.VOID or not self.stack: return
        d = len(self.stack)
        if self.skip == d: self.skip = None
        if self.col == d: self.col = 0
        self.stack.pop()
    def handle_data(self, data):
        if self.col and self.skip is None: self.buf.append(data)

n = words = eq = boxes = 0
for num, cslug, title, part, _m in bp.FLAT:
    p = os.path.join(docs_book, cslug + '.html')
    if not os.path.exists(bk.chapter_path(cslug)) or not os.path.exists(p):
        continue
    t = library.read(p)
    m = re.search(r'<div class="col[^"]*">(.*)</div>\s*</main>', t, re.S)
    body = m.group(1) if m else ''
    w = Words(); w.feed(t)
    words += len(re.findall(r"[A-Za-z0-9’'-]+", ''.join(w.buf)))
    eq += len(re.findall(r'class="katex"', body))
    boxes += len(re.findall(r'class="callout plain"', body))
    n += 1
human = lambda x: f"{x/1000:.0f}k" if x >= 10000 else f"{x:,}"
stats = {"CH": f"{n} / {len(bp.FLAT)}", "WORDS": human(words), "EQ": human(eq),
         "BOXES": str(boxes), "PARTS": str(len(bp.PARTS))}
stats.update(webbuild.start_stats(bk))   # {{START_HREF}} {{START_NUM}} {{START_TITLE}}, as webbuild does
print(slug, stats)
if out:
    bk.out = os.path.join(out, slug)
    os.makedirs(bk.out, exist_ok=True)
webbuild.extra_pages(bk, stats)
webbuild.landing_page(bk, stats)
lp = os.path.join(bk.src, '_landing.html')
if os.path.exists(lp) and 'assets/landing.css' in library.read(lp):
    library.write(os.path.join(bk.out, 'assets', 'landing.css'),
                  library.read(os.path.join(library.ASSETS, 'landing.css')))
print('front door + %d extra page(s) -> %s' % (len(bk.cfg.get('pages') or []), bk.out))
if not out:
    import subprocess
    for t in ('nav.py', 'pwa.py'):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], cwd=ROOT,
                           capture_output=True, text=True)
        print(t, 'ok' if r.returncode == 0 else 'FAILED\n' + r.stdout[-800:] + r.stderr[-800:])
