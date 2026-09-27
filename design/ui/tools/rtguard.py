#!/usr/bin/env python3
"""Prove the runtime_js() guards in tools/webbuild.py and tools/make.py (W0-HARNESS).

    python3 rtguard.py            # reads docs/: run through locked.sh

1. Both runtime_js() return bytes identical to docs/<slug>/assets/book.js for every book
   that ships one (book.js carries no themecss; that goes into book.css).
2. With library.read monkeypatched to serve a scratch copy of book.js, both raise when
   - the literal 'numberEquations();' is missing,
   - it appears twice,
   - the katex block is missing, or
   - the boot-contract comment appears twice.
   The repo is never edited.

make.py runs its whole build at import time, so its runtime_js() is lifted out with ast
and executed alone, with the same globals it would see (library, os, re)."""
import ast, os, re, sys
ROOT = '/home/user/library'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import library, webbuild

fails = []
def ok(name, cond, detail=''):
    print(('  PASS  ' if cond else '  FAIL  ') + name + (('  ' + str(detail)) if detail else ''))
    if not cond:
        fails.append(name)

src = open(os.path.join(ROOT, 'tools', 'make.py')).read()
fn = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == 'runtime_js')
mod = ast.Module(body=[fn], type_ignores=[])
g = {'library': library, 'os': os, 're': re}
exec(compile(mod, 'make.py:runtime_js', 'exec'), g)
make_rt = g['runtime_js']

real = library.read
BOOKJS = os.path.join(library.ASSETS, 'book.js')
orig = real(BOOKJS)

print('byte identity with docs/')
for name, f in (('webbuild', webbuild.runtime_js), ('make', make_rt)):
    out = f()
    for bk in library.books():
        p = os.path.join(bk.out, 'assets', 'book.js')
        if os.path.exists(p):
            with open(p, encoding='utf-8', newline='') as fh:
                shipped = fh.read()
            ok('%s.runtime_js() == docs/%s/assets/book.js' % (name, bk.slug), out == shipped,
               '' if out == shipped else 'len %d vs %d' % (len(out), len(shipped)))

def patched(text):
    def rd(path, *a, **kw):
        if os.path.abspath(path) == os.path.abspath(BOOKJS):
            return text
        return real(path, *a, **kw)
    return rd

cases = {
    "no 'numberEquations();'": orig.replace('numberEquations();', 'numberEquations ();'),
    "two 'numberEquations();'": orig.replace('numberEquations();', 'numberEquations(); numberEquations();'),
    'no katex block': orig.replace('if (window.katex) { typeset(); }', 'if (window.katex) typeset();'),
    'two contract comments': orig.replace('  /* ---------- boot ---------- */',
        '  /* ---------- boot ---------- */\n  /* ---------- boot contract x */', 1),
}
print('\nguards (library.read monkeypatched; the repo is not edited)')
for label, text in cases.items():
    ok('scratch copy differs from book.js: ' + label, text != orig)
    for name, f in (('webbuild', webbuild.runtime_js), ('make', make_rt)):
        library.read = patched(text)
        try:
            f(); raised = None
        except RuntimeError as e:
            raised = str(e)
        finally:
            library.read = real
        ok('%s.runtime_js() raises: %s' % (name, label),
           raised is not None and 'DESIGN.md section 8' in raised, (raised or 'no exception')[:150])

# the contract comment is dropped, so the shipped file does not grow when it is edited
print('\nthe contract comment')
ok('book.js carries the boot-contract comment', '/* ---------- boot contract' in orig)
ok('runtime_js() drops it', '---------- boot contract' not in webbuild.runtime_js())
print('\nrtguard: %s' % ('%d failure(s)' % len(fails) if fails else 'PASS'))
sys.exit(1 if fails else 0)
