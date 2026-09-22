# Guideline gap passes

What an external guideline cites that this book does not. The input is the
guideline's own reference list, parsed to one row per numbered reference, with
the PubMed identifier and the sentence the guideline attached to it. The
identifier is what makes the diff mechanical; the sentence is what makes the
result readable, because a missing identifier then arrives as a clinical claim
rather than as a citation.

```bash
python3 tools/guidelinediff.py gaps/nccn-breast-v6.2026-references.csv
python3 tools/guidelinediff.py gaps/<file>.csv --topic systemic
python3 tools/guidelinediff.py gaps/<file>.csv --covered
```

## Reading the output

The raw count of absent identifiers overstates the gap and should not be
quoted on its own. This book and a guideline are different objects. A guideline
has to cite a source for every regimen it lists, including combinations from
the 1990s and the imaging and surgical literature; this book argues from the
evidence that decides something and carries 1,101 identifiers of its own, most
of which the guideline does not cite either. Two documents can disagree about
every citation and agree about every recommendation.

Three questions make the output useful, in this order.

**Is the absence recent?** Sort the misses by year. On the NCCN v6.2026 pass,
173 of the 657 identifiers absent from the book sat in the two systemic therapy
buckets, and only 10 of those 173 were published in 2020 or later. An old miss
is usually the guideline's regimen-listing obligation. A recent one is usually
a real omission.

**Does the guideline carry it without an identifier?** 94 rows of that pass had
no PubMed identifier, and the newest readouts sit there. Of the 68 in systemic
therapy, 28 matched a reference already in this book on title alone. An
identifier-free row is not a gap until it has been resolved.

**Does the book assert the absence?** This is the one worth the pass. Three
sections named a hole that a paper the guideline cites had already filled. That
is not a missing citation. It is a sentence that is no longer true.
