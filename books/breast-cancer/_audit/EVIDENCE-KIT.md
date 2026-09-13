# Evidence chapter kit — the contract for Parts PT-15 and PT-16

Read this with WRITING-KIT.md. Everything there still applies: the citation rule, the voice rules,
the four macros. This adds the one thing that is new.

## What an evidence chapter is for

Ahmed's brief: "I will want to compile phase 2/3 trials in these settings, especially specific
combinations. These will continue to update as new data reel in."

So these chapters have a division of labour that the rest of the book does not.

**Tables enumerate. Prose argues.**

The table is generated from `trials.yaml` at build time. You do not write it. You declare it:

````
```evidence setting=early subtype=HR+/HER2- line=adjuvant modality=endocrine
```
````

The block has **no body**. Just the filter line, then the closing fence. The build renders the
matching rows. That is what makes the chapter self-updating: a new readout is added once to
`trials.yaml` and appears in every chapter whose filter matches it.

## The filter axes

| Key | Values |
|---|---|
| `setting` | early, metastatic, dcis, prevention, mrd, screening, surveillance, recurrence |
| `subtype` | HR+/HER2-, HER2+, HR+/HER2+, TNBC, HER2-low, BRCA, all |
| `line` | neoadjuvant, adjuvant, post-neoadjuvant, 1L, 2L, 3L+ |
| `modality` | endocrine, cdk4-6, chemo, her2, adc, immunotherapy, parp, pi3k-akt, surgery, radiation, bone, supportive |
| `phase` | 2, 2/3, 3 |
| `status` | reported, ongoing, awaited |
| `topic` | substring match |
| `sort` | year, acronym, n |
| `cols` | subset of acronym,phase,n,population,arms,endpoint,result,os,status |
| `caption` | one line under the table, underscores become spaces |

Keys are ANDed. A value may be comma-separated, which is ORed. A trial with `subtype: all` appears
in every subtype's table, which is correct for an all-comers trial. That wildcard does not extend to
setting, line or modality.

Check your filters before you rely on them:

```
python3 tools/evidence.py --render "setting=early subtype=TNBC line=neoadjuvant modality=immunotherapy"
python3 tools/evidence.py --check
python3 tools/evidence.py --coverage
```

A filter matching zero trials fails `--check`. So does a block with a body.

## The rule that keeps the two from drifting

**Never restate in prose a number the table already carries.** If the table gives DESTINY-Breast05
its iDFS figures, the prose does not repeat them. The prose says what the result means, what the
population was selected for, what the comparison could not settle, and what a reader should do
differently on Monday.

The exception is a number you are *arguing from*. If the whole point of a paragraph is that two
trials of one drug class disagree, quote the two figures and make the argument. Then it is analysis,
not enumeration.

This is not a style preference. A number that lives in two places drifts when one is updated.

## Enriching trials.yaml

Your table is only as good as the registry. For every trial your chapter's tables surface, fill in
the fields below if they are missing, verifying each against the primary publication on PubMed.

```yaml
  keynote522:
    acronym: KEYNOTE-522
    phase: 3
    setting: early
    subtype: TNBC
    line: neoadjuvant
    modality: immunotherapy,chemo
    population: stage II-III TNBC, PD-L1 unselected
    n: 1174
    arms: pembrolizumab plus chemotherapy vs placebo plus chemotherapy
    endpoint: pathological complete response and event-free survival
    result: pCR 64.8% vs 51.2%; EFS HR 0.63
    os: 5-year OS 86.6% vs 81.7%, HR 0.66
    year: 2020
    status: reported
    primary_ref: schmid2020
    cited_by: [BC-510, BC-860]
```

Rules for these fields:

- `n` is the number randomised. If a trial reports randomised and analysed separately, `n` is
  randomised and the difference goes in `population` if it matters.
- `arms` is experimental against control, in that order, short enough to read in a table cell.
- `result` carries the primary endpoint result with its comparison. Never a bare hazard ratio.
- `os` is the overall survival result, or `not reached in either arm`, or `not yet reported`, or
  `no significant difference`. Do not leave it blank to imply a negative.
- `status` is `reported`, `awaited` (accrual complete, primary analysis pending) or `ongoing`.
- `year` is the year of the publication in `primary_ref`.

**Do not edit trials.yaml directly.** Write your additions and changes to
`_audit/PATCH-trials-<your-chapter-ids>.yaml` as a mapping of trial key to the fields you are adding
or changing. Same for new references, to `_audit/PATCH-refs-<your-chapter-ids>.yaml`. They get merged
centrally, because several of you are working at once.

If a trial your chapter needs is not in the registry at all, add it to your patch with a key in the
existing style (lowercase acronym) and every field above filled in, including a verified
`primary_ref` that you also add to your refs patch.

## Chapter shape

Each of these chapters opens with a scope section. That section says what the chapter covers, what it
deliberately leaves to a neighbouring chapter, and how to read the tables. Write it as orientation for
a reader who will return to this chapter repeatedly, because they will.

Each closes with an unresolved-questions section. Name the trials that are running and what each would
settle, using `status=ongoing` or `status=awaited` in an evidence block so that section stays current
too. Be specific about what a readout would change.

In between, organise by the clinical question, not by drug. A section per decision the reader makes.
