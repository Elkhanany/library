#!/usr/bin/env python3
"""Push stylesheet and script changes into docs/ in seconds, without the full webbuild.

    python3 restyle.py

Rewrites, for every book, docs/<slug>/assets/book.css (house sheet + the book's theme),
book.js and landing.css (where the book already ships one), then re-runs the two text passes
(nav.py copies nav.css and stamps the bar; pwa.py re-emits pwa.css/pwa.js, manifests and the
offline digests). Anything that changes page STRUCTURE (webbuild SHELL, build.py, the hub,
a book's src/) needs onebook.py or the full build instead."""
import os, sys, subprocess
ROOT = '/home/user/library'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import library, webbuild
n = 0
for bk in library.books():
    a = os.path.join(bk.out, 'assets')
    if not os.path.isdir(a):
        continue
    library.write(os.path.join(a, 'book.css'),
                  library.read(os.path.join(library.ASSETS, 'book.css')) + webbuild.themecss(bk))
    library.write(os.path.join(a, 'book.js'), webbuild.runtime_js())
    if os.path.exists(os.path.join(a, 'landing.css')):
        library.write(os.path.join(a, 'landing.css'), library.read(os.path.join(library.ASSETS, 'landing.css')))
    n += 1
for t in ('nav.py', 'pwa.py'):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], cwd=ROOT, capture_output=True, text=True)
    print(t, 'ok' if r.returncode == 0 else 'FAILED\n' + r.stdout[-800:] + r.stderr[-800:])
print('restyled %d books' % n)
