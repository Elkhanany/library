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
python3 tools/guidelinediff.py gaps/<file>.csv --resolved gaps/<file>-nopmid.yaml
```

## Reading the output

The raw count of absent identifiers overstates the gap and should not be
quoted on its own. This book and a guideline are different objects. A guideline
has to cite a source for every regimen it lists, including combinations from
the 1990s and the imaging and surgical literature; this book argues from the
evidence that decides something, and it carried 1,101 identifiers of its own at
the first pass, most of which the guideline does not cite either. Two documents can disagree about
every citation and agree about every recommendation.

Three questions make the output useful, in this order.

**Is the absence recent?** Sort the misses by year. On the first NCCN v6.2026
pass, 173 of the identifiers absent from the book sat in the two systemic therapy
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

## Where the NCCN v6.2026 pass ended

All 657 identifiers are now in `references.yaml` and cited in at least one
chapter, and `nccn-v6.2026-diff.txt` reports none absent. Each paper was read
against its abstract before it was cited. It was cited where the guideline's
claim belongs, attached to an existing sentence or to a short new one that its
abstract supports, and never as a list.

The 94 rows with no identifier are resolved in `nccn-v6.2026-nopmid.yaml`, one
entry per row, with the keys that carry it and the basis for saying so. 53 are
journal articles the parsed list carried without an identifier. 28 are meeting
abstracts whose full publication the book cites. 3 are abstracts never
published in full, whose trial the book names and cites through its published
reports. 2 cite the AJCC seventh edition, and 1 is a trial registry record.

Seven rows cannot be cited under the rule that a chapter may not cite an
unverified reference, because none has a PubMed record: two websites, the
ribociclib label, two textbook chapters, an unindexed commentary, and the AMBRE
abstract, which had no full publication when the pass closed. `--resolved`
lists them with the reason, and fails if any recorded key is missing from the
store or cited by no chapter.

Reading the claims against the papers changed sentences as well as citations.
Among them: extended endocrine therapy on a molecular signal had been described
as untested, and has been tested retrospectively; the Milan sentinel node trial
had been reported at its first follow-up only, and one axillary recurrence has
since appeared among the 167 women spared dissection; the 2013 and 2015
CLEOPATRA survival analyses had been conflated; RIGHT Choice had been called the
only randomised test of first-line endocrine therapy against chemotherapy, and
PADMA is a second; and D-CARE had been set against the fracture-dose
denosumab trial without that trial's disease-free survival result.
