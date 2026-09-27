#!/usr/bin/env python3
"""Scratch run of tools/navcheck.py with selectors that do not exist (W0-HARNESS acceptance).

    sh locked.sh env NAVCHECK_PORT=8951 python3 navcheck_missing.py

The repo file is not edited: its source is read, a few selectors are swapped for ones that
match nothing, and the result is executed in memory as __main__ with navcheck's own __file__,
so DOCS and the imports resolve as usual. Expected: FAIL lines naming each page and missing
selector, the later sections (the bar, sideways, equation numbers, the sweep) still run,
and the final 'navcheck: N failure(s)' summary is printed (exit 1)."""
import os, sys
SRC = '/home/user/library/tools/navcheck.py'
src = open(SRC).read()
swaps = [("'#mnav .mn-dest'", "'#mnav .mn-nonexistent'"),          # waitsel in the drawer block
         ("'#mnav .mn-kicker'", "'#mnav .mn-kicker-nonexistent'"), # text() in the drawer block
         ("'#mnav-btn'", "'#mnav-btn-nonexistent'"),               # click()
         ("'.main a[href$=\".html\"]'", "'.main a.nonexistent'")]  # click in standalone
for a, b in swaps:
    assert a in src, a
    src = src.replace(a, b)
# and a wait_for_function that can never succeed
src = src.replace('READY = "() => window.LibraryPWA && window.LibraryPWA.nav().index >= 0"',
                  'READY = "() => window.NoSuchThing === 1"')
assert 'window.NoSuchThing' in src
print('scratch navcheck: %d selectors swapped for ones that match nothing, READY never true\n'
      % len(swaps), flush=True)
sys.argv = [SRC]
g = {'__name__': '__main__', '__file__': SRC}
try:
    exec(compile(src, SRC + ' (scratch copy)', 'exec'), g)
except SystemExit as e:
    print('\nscratch navcheck exited with', e.code, '(ran to the end: the summary above is its last line)')
    sys.exit(0 if e.code == 1 else 1)
print('\nscratch navcheck exited 0: the missing selectors were NOT reported')
sys.exit(1)
