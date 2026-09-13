# Quarantine

`BC-040.md.unverified` was drafted by a writing agent that was terminated by a rate limit before
it returned its reference patch. The chapter cites nine keys that are not in `references.yaml`
and that nobody has verified:

    asselinlabat2010  boyd2007  cghfbc2002  kumar2023  lim2009
    mallepell2006  milanese2006  nishimura2023  vankeymeulen2011

Of these, only `lim2009` has been resolved so far, to PMID 19648928.

The prose is probably fine. The citations are not established, and a chapter in this book may not
cite an unverified reference. To recover it: verify each key against PubMed, add the entries to
`references.yaml` with `verified: true`, move the file back to `chapters/BC-040.md`, and run
`python3 tools/bc.py`. Do not merge the keys without checking that each hit is the paper the
sentence actually claims.
