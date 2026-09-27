#!/usr/bin/env python3
"""Synthetic-tree test for tools/sitecheck.py (W0-HARNESS acceptance). Touches neither docs/
nor build/: it writes a small tree under scratchpad and points sitecheck at it.

    python3 sitecheck_synth.py

Expected:
  - href="/library/x.html#nope" is reported as a missing fragment;
  - href="/library/index.html", "/library/", "/library/x.html#yes" and "../x.html#yes" resolve;
  - "#here" resolves on its own page, "#gone" does not, "#who=spinoza" is skipped (a route);
  - "/library/nothere.html" is a missing file;
  - in --build semantics (no site root) "/library/index.html" is missing, since a Dropbox copy
    has no /library/;
  - main() on the tree prints NO SUCH FRAGMENT for /library/x.html#nope and exits 1."""
import io, os, shutil, sys, contextlib
sys.path.insert(0, '/home/user/library/tools')
import library, sitecheck

T = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                 'sitecheck-synth')
shutil.rmtree(T, ignore_errors=True)
os.makedirs(os.path.join(T, 'book'))
page = lambda body: '<!DOCTYPE html><html><body>%s</body></html>' % body
open(os.path.join(T, 'index.html'), 'w').write(page('<h1 id="top">hub</h1>'))
open(os.path.join(T, 'x.html'), 'w').write(page('<p id="yes">x</p>'))
open(os.path.join(T, 'book', 'p.html'), 'w').write(page(
    '<a href="/library/x.html#nope">a</a> <a href="/library/index.html">b</a> '
    '<a href="/library/">c</a> <a href="/library/x.html#yes">d</a> <a href="../x.html#yes">e</a> '
    '<p id="here"></p><a href="#here">f</a> <a href="#gone">g</a> <a href="#who=spinoza">h</a> '
    '<a href="/library/nothere.html">i</a> <a href="https://example.org/#x">j</a>'))

fails = []
def ok(name, cond, detail=''):
    print(('  PASS  ' if cond else '  FAIL  ') + name + ('  ' + str(detail) if detail else ''))
    if not cond:
        fails.append(name)

missing, external, frags, n_pages, n_links, n_frags = sitecheck.links(T, T, True)
ok('/library/x.html#nope is a missing fragment', ('book/p.html', '/library/x.html#nope') in frags, frags)
ok('#gone is a missing fragment on its own page', ('book/p.html', '#gone') in frags)
ok('no other fragment is reported (#here, #yes resolve; #who= skipped)', len(frags) == 2, frags)
ok('/library/index.html resolves against the tree', not any(u == '/library/index.html' for _r, u in missing), missing)
ok('/library/ resolves to index.html', not any(u == '/library/' for _r, u in missing))
ok('/library/nothere.html is missing', ('book/p.html', '/library/nothere.html') in missing, missing)
ok('the external link is not a dependency', not external, external)

missing_b, _e, frags_b, *_ = sitecheck.links(T, None, False)
ok('--build semantics: /library/index.html cannot resolve without a site root',
   ('book/p.html', '/library/index.html') in missing_b, missing_b)

real = library.DOCS
library.DOCS = T
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        rc = sitecheck.main()
finally:
    library.DOCS = real
out = buf.getvalue()
print('    main() on the tree said:\n      ' + '\n      '.join(out.strip().splitlines()))
ok('main() reports NO SUCH FRAGMENT for /library/x.html#nope',
   'NO SUCH FRAGMENT  book/p.html  ->  /library/x.html#nope' in out)
ok('main() does not report /library/index.html as MISSING', '->  /library/index.html' not in out)
ok('main() exits 1', rc == 1, rc)
print('\nsitecheck synthetic tree: %s' % ('PASS' if not fails else '%d failure(s)' % len(fails)))
sys.exit(1 if fails else 0)
