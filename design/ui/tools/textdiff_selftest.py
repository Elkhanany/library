#!/usr/bin/env python3
"""Self-test for textdiff.py: it must PASS a correct W3-CLINIC-shaped rewrite of the clinical
chapters and FAIL each kind of wrong one. Reads docs/ (run through locked.sh); writes only to
scratchpad.

    python3 textdiff_selftest.py

The correct rewrite, applied with regexes to copies of every BC-*.html:
  - p.ct-cap split at its first sentence end into p.ev-title + p.ev-note, placed before the table;
  - Ph, N and Status folded into the trial cell as span.m[data-col] joined by ' · ', the Ref
    citation moved beside the trial name, and those heads removed; data-label on every td;
  - ol.refs wrapped in <details class="refs-list"><summary>All N references</summary>;
  - a story's second and later appearances in a chapter lose where and title and gain a
    '<title>, continued' kicker; wrapper ids become story-<first question id>.
Then five single-point mutations of that rewrite, each of which must FAIL under its rule."""
import os, re, shutil, subprocess, sys
UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = '/home/user/library/docs/breast-cancer'
OUT = os.path.join(os.path.dirname(UI), 'textdiff-selftest')
TD = os.path.join(UI, 'architect', 'textdiff.py')
META = {'Ph': 'ph', 'N': 'n', 'Status': 'status'}


def table(m):
    t = m.group(0)
    heads = re.findall(r'<th>(.*?)</th>', t)
    keep = [i for i, h in enumerate(heads) if h not in META and h != 'Ref']
    def row(rm):
        tds = re.findall(r'<td>(.*?)</td>', rm.group(1), re.S)
        if len(tds) != len(heads):
            return rm.group(0)
        meta = ['<span class="m" data-col="%s">%s</span>' % (META[h], tds[i])
                for i, h in enumerate(heads) if h in META and tds[i].strip()]
        ref = ''.join(tds[i] for i, h in enumerate(heads) if h == 'Ref')
        first = tds[0] + (' ' + ref if ref else '') + \
            ('<span class="mline">' + ' · '.join(meta) + '</span>' if meta else '')
        cells = [first] + [tds[i] for i in keep[1:]]
        labels = [heads[i] for i in keep]
        return '<tr>' + ''.join('<td data-label="%s">%s</td>' % (l, c)
                                for l, c in zip(labels, cells)) + '</tr>'
    body = re.sub(r'<tr>((?:(?!<tr>).)*?<td>.*?)</tr>', row, t, flags=re.S)
    body = re.sub(r'<thead><tr>.*?</tr></thead>',
                  '<thead><tr>' + ''.join('<th>%s</th>' % heads[i] for i in keep) + '</tr></thead>',
                  body, flags=re.S)
    return body


def evidence(m):
    ev = m.group(0)
    cap = re.search(r'<p class="ct-cap">(.*?)</p>', ev, re.S)
    ev = re.sub(r'<table class="trials">.*?</table>', table, ev, flags=re.S)
    if cap:
        ev = ev.replace(cap.group(0), '')
        txt = cap.group(1)
        k = re.search(r'\.\s', txt)
        title, note = (txt[:k.start() + 1], txt[k.end():]) if k else (txt, '')
        ev = ev.replace('<div class="evidence">', '<div class="evidence"><p class="ev-title">%s</p>'
                        '<p class="ev-note">%s</p>' % (title, note), 1)
    return ev


def rewrite(t):
    t = re.sub(r'<div class="evidence">.*?</table>(?:<p class="ct-cap">.*?</p>)?</div>', evidence,
               t, flags=re.S)
    t = re.sub(r'<ol class="refs">(.*?)</ol>',
               lambda m: '<details class="refs-list"><summary>All %d references</summary>'
                         '<ol class="refs">%s</ol></details>' % (m.group(1).count('<li'), m.group(1)),
               t, flags=re.S)
    seen = set()
    def story(m):
        s, title = m.group(0), m.group(2)
        s = s.replace('<div class="story" id="%s">' % m.group(1),
                      '<div class="story" id="story-%s">' % m.group(1), 1)
        if title in seen:
            s = re.sub(r'<p class="st-where">.*?</p>', '', s, count=1, flags=re.S)
            s = s.replace('<p class="st-title">%s</p>' % title,
                          '<p class="st-cont">%s, continued</p>' % title, 1)
        seen.add(title)
        return s
    t = re.sub(r'<div class="story" id="([^"]+)"><p class="st-where">.*?</p><p class="st-title">(.*?)</p>',
               story, t, flags=re.S)
    return t


def run(label, expect_pass):
    r = subprocess.run([sys.executable, TD, 'compare', '--new', OUT], capture_output=True, text=True)
    last = (r.stdout.strip().splitlines() or ['?'])[-1]
    good = (r.returncode == 0) == expect_pass
    print(('  PASS  ' if good else '  FAIL  ') + label + '  -> ' + last[:120])
    if not good or not expect_pass:
        body = [l for l in r.stdout.splitlines() if l.startswith('    ')][:3]
        for l in body:
            print('          ' + l.strip()[:150])
    return good


shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
n = folded = cont = 0
for f in sorted(os.listdir(SRC)):
    if re.fullmatch(r'BC-.*\.html', f):
        t = open(os.path.join(SRC, f), encoding='utf-8').read()
        u = rewrite(t)
        folded += u.count('data-col=')
        cont += u.count(', continued</p>')
        open(os.path.join(OUT, f), 'w', encoding='utf-8').write(u)
        n += 1
print('rewrote %d chapters: %d meta spans folded, %d continued kickers, %d reference summaries'
      % (n, folded, cont, sum(open(os.path.join(OUT, f)).read().count('refs-list') for f in os.listdir(OUT))))
ok = [run('a correct W3-CLINIC-shaped rewrite passes', True)]

def mutate(f, old, new, label, count=1):
    p = os.path.join(OUT, f)
    t = open(p, encoding='utf-8').read()
    assert old in t, (f, old[:60])
    open(p, 'w', encoding='utf-8').write(t.replace(old, new, count))
    ok.append(run(label, False))
    open(p, 'w', encoding='utf-8').write(t)

b9 = open(os.path.join(OUT, 'BC-900.html'), encoding='utf-8').read()
mutate('BC-900.html', 'The prose argues the decision.', 'The prose argues a decision.',
       '(i) one word of prose changed fails')
mutate('BC-900.html', 'median progression-free survival 40.7 vs 26.9 months',
       'median progression-free survival 40.7 vs 26.8 months', '(ii) one evidence cell changed fails')
mutate('BC-900.html', 'Does blocking HER2 at more than one site do more than blocking it at one?',
       'Does blocking HER2 at two sites do more than blocking it at one?', '(iii) a story question changed fails')
mutate('BC-900.html', 'Trastuzumab deruxtecan plus pertuzumab for HER2-positive metastatic breast cancer.',
       'Trastuzumab deruxtecan and pertuzumab for HER2-positive metastatic breast cancer.',
       '(iv) a reference changed fails')
mutate('BC-900.html', '<p class="ev-title">', '<span class="cue">→ more columns</span><p class="ev-title">',
       '(v) a new visible string fails')
k = re.search(r'<summary>All (\d+) references</summary>', b9)
mutate('BC-900.html', k.group(0), '<summary>All %d references</summary>' % (int(k.group(1)) + 1),
       '(iv) a summary that miscounts fails')
print('\ntextdiff self-test: %s' % ('PASS' if all(ok) else 'FAIL'))
sys.exit(0 if all(ok) else 1)
