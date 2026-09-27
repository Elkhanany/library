#!/bin/sh
# W0 baseline builds: make.py + verify.py for both chaptered books, then figcheck on the
# physics chapters. Each step takes the docs/build lock on its own, so other locked runs can
# interleave. Logs go to scratchpad/ui/baselines/logs/.
UI=/tmp/claude-0/-home-user-library/95ff2fbb-089e-5856-80da-39df1d378c0f/scratchpad/ui
L=$UI/baselines/logs
LK="sh $UI/architect/locked.sh"
cd /home/user/library || exit 1
for b in breast-cancer newton-to-mtheory; do
  $LK env NMT_BOOK=$b python3 tools/make.py > $L/make-$b.log 2>&1; echo "exit=$?" >> $L/make-$b.log
  $LK env NMT_BOOK=$b python3 tools/verify.py > $L/verify-$b.log 2>&1; echo "exit=$?" >> $L/verify-$b.log
done
$LK sh -c 'python3 tools/figcheck.py $(cd build && ls newton-to-mtheory/ch*.html | sed "s/.html$//")' > $L/figcheck.log 2>&1
echo "exit=$?" >> $L/figcheck.log
echo done > $L/w0builds.done
