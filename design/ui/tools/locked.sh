#!/bin/sh
# Serialise every run that writes or reads docs/ (restyle, onebook, frontdoor, hubonly,
# webbuild, make/verify, navcheck, sitecheck, prodshot, shoot). The helpers hard-code
# ROOT=/home/user/library, so worktrees do not isolate them; this lock does.
#   sh locked.sh python3 ../restyle.py
#   sh locked.sh env NAVCHECK_PORT=8940 python3 /home/user/library/tools/navcheck.py
LOCK=/tmp/claude-0/-home-user-library/95ff2fbb-089e-5856-80da-39df1d378c0f/scratchpad/ui/docs.lock
exec flock "$LOCK" "$@"
