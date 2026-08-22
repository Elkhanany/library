#!/usr/bin/env bash
# Apply the newest batch bundle from Downloads, then push.
#
# Cowork sessions cannot push to GitHub: the git proxy refuses any repo that is
# not in "the session's authorized repository set", and no control to add one
# exists (anthropics/claude-code#76248, open). So each batch arrives as a git
# bundle instead — the commits themselves, with their messages, not a zip of
# files. This script finds the newest one and applies it.
#
#   ./apply-batch.sh              # newest bundle in ~/Downloads
#   ./apply-batch.sh path/to.bundle
#
set -euo pipefail
cd "$(dirname "$0")"

B="${1:-}"
if [ -z "$B" ]; then
  B=$(ls -t "$HOME/Downloads"/*.bundle 2>/dev/null | head -1 || true)
  [ -n "$B" ] || { echo "No .bundle found in ~/Downloads. Pass the path explicitly."; exit 1; }
fi
echo "bundle:  $B"

# A bundle names the commit it must sit on top of. If that is not the commit you
# are on, applying it would either fail or silently produce a merge — better to
# stop and say so.
NEED=$(git bundle verify "$B" 2>&1 | grep -A1 "requires this ref" | tail -1 | awk '{print $1}' || true)
HERE=$(git rev-parse HEAD)
if [ -n "$NEED" ] && [ "$NEED" != "$HERE" ]; then
  echo
  echo "This bundle applies on top of ${NEED:0:7}, but you are on ${HERE:0:7}."
  echo "Either you have local commits, or this bundle is stale. Not touching anything."
  exit 1
fi

git pull --ff-only "$B" main
echo
git --no-pager log --oneline "$HERE"..HEAD
echo
git push origin main
echo
echo "Pushed. GitHub Pages redeploys on its own; give it a couple of minutes."
