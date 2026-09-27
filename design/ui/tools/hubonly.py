#!/usr/bin/env python3
"""Regenerate ONLY the library hub (docs/index.html) in a few seconds, then re-run the
bar and app-layer text passes over the site. For iterating on the hub without the
fifteen-minute webbuild.

    python3 hubonly.py            # writes docs/index.html, then nav.py + pwa.py passes
    python3 hubonly.py --out DIR  # writes DIR/index.html only (no passes); for diffing

Exact, not approximate: webbuild.hub() only needs each book's count of written
chapters, which is len(bk.written()) -- the same number build_book() returns.
Works whether hub() still lives in webbuild.py or has been moved to tools/hub.py
(it looks in both)."""
import os, sys
ROOT = '/home/user/library'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import library, webbuild
out = None
if '--out' in sys.argv:
    out = sys.argv[sys.argv.index('--out') + 1]
    os.makedirs(out, exist_ok=True)
mods = [webbuild]
_hp = os.path.join(ROOT, 'tools', 'hub.py')
if os.path.exists(_hp):           # loaded by path: this helper is not that module
    import importlib.util
    _sp = importlib.util.spec_from_file_location('tools_hub', _hp)
    _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
    mods.insert(0, _m)
fn = None
for m in mods:
    if hasattr(m, 'hub') and callable(getattr(m, 'hub')):
        fn = getattr(m, 'hub'); break
if fn is None:
    raise SystemExit('hubonly.py: no hub() in webbuild or tools/hub.py')
if out:
    for m in mods:
        if hasattr(m, 'DOCS'):
            m.DOCS = out
books = library.books()
n = fn([(bk, len(bk.written()), {}) for bk in books])
print('hub: %s tiles -> %s' % (n, os.path.join(out or library.DOCS, 'index.html')))
if not out:
    import subprocess
    for t in ('nav.py', 'pwa.py'):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], cwd=ROOT,
                           capture_output=True, text=True)
        print(t, 'ok' if r.returncode == 0 else 'FAILED\n' + r.stdout[-800:] + r.stderr[-800:])
