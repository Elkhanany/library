# How this book is written

A reference on breast cancer for practising medical oncologists and for fellows. Sixteen
parts, ninety-three chapters, seven hundred and seventy-eight sections. It is the first book in
the library whose structure is data rather than a hand-kept list, because at this size it has
to be.

## The three rules

**1. Identifiers are permanent and carry no position.** `PT-##` for a part, `BC-###` for a
chapter, `BS-####` for a section. A chapter keeps its identifier when it moves between parts.
Filenames, anchors, citations and cross-references all bind to the identifier, so restructuring
the book breaks nothing.

**2. Position is list position.** Move a block in `outline.yaml` to move a node. Insert a block
to insert one. Nothing else in the file changes. `BC-345` would sit between `BC-340` and
`BC-350`, which is what an insertion looks like in practice.

**3. Display numbers are computed at build time.** `Part VI`, `Chapter 28`, and the `4 ·` in
front of a section heading exist only in the output. Nothing in the source knows its own
number.

## Where things live

| File | Role |
|---|---|
| `outline.yaml` | Structure. Parts, chapters, sections, tags, appendices. Hand-edited. |
| `chapters/BC-###.md` | Chapter prose, one file per chapter, named for the identifier. Hand-edited. |
| `references.yaml` | Every citation in the book. Hand-edited or imported. |
| `trials.yaml` | Trial registry. Hand-edited. |
| `glossary.yaml` | Defined terms. Hand-edited. |
| `book.json` | Title, theme, and the reader-facing copy for each part. Hand-edited. |
| `curriculum.json` | What the library builds from. **Generated.** |
| `src/BC-###.html` | Chapter fragments. **Generated.** |
| `src/_landing.html` | The book's front door. Hand-edited. |

`src/` is generated for this book, which is a deliberate exception to the library's rule that
`src/` is the only hand-edited tree. Edit a fragment there and the edit is lost on the next
run. The prose lives in `chapters/`.

## The build

```bash
python3 tools/bc.py            # outline.yaml -> curriculum.json, chapters/*.md -> src/*.html
python3 tools/bc.py --check    # fail if either is stale
python3 tools/webbuild.py      # the whole library -> docs/
```

`bc.py` refuses to write anything if a citation key, cross-reference, trial or glossary term
does not resolve, or if a section heading disagrees with `outline.yaml`. Run it before every
commit. It is cheap and it is the only thing standing between a typo and a dead link in a
published chapter.

## Writing a chapter

Add the file as `chapters/BC-###.md`, named for an identifier that already exists in
`outline.yaml`. Front matter carries the identifier and the title, and both are checked against
the outline:

```markdown
---
id: BC-280
title: "HER2 heterogeneity"
subtitle: "What a heterogeneous report changes, and what it does not."
status: drafted
updated: 2026-09-13
---

## BS-2250 Definitions and thresholds, spatial, clonal, and the ten percent convention

Prose.
```

Every heading carries its section identifier, and the text after it must match the title in
`outline.yaml` exactly. Write the heading as `## BS-2250` alone and the title is filled in from
the outline. Sections you have not written yet are collected into a **Still to be written**
block at the foot of the chapter, so the plan is visible rather than silent.

To add a section, write it as a bare string under the right chapter in `outline.yaml`:

```yaml
    sections:
    - id: BS-2390
      title: What to do with a heterogeneous HER2 report in clinic today
    - Reversion mutations and restored repair
```

then `python3 tools/bc.py --mint`, which turns it into an `{id, title}` pair with a freshly
minted permanent identifier. `--mint --dry-run` reports what it would do and writes nothing.
Identifiers come from the highest one in use plus ten, so a deleted identifier is never handed
out again and an old link never quietly starts resolving to something else. Nothing that
already carries one is touched.

To promote a section to a chapter, move it up a level, give it a free `BC-###`, and record its
old `BS-####` in a `was:` list.

## Citations, trials, cross-references, terms

Four syntaxes, all resolved by `bc.py`, all bound to permanent keys:

```
[@slamon1987]                 one citation
[@slamon1987; @shou2004]      grouped into a single bracket
{{trial:katherine}}           a named trial, from the registry
[[BC-280]]  [[BS-2290]]       a chapter or a section
[[term:her2-low]]             a defined term, from the glossary
```

Never inline a citation. No bare PubMed identifiers, DOIs or author-year strings in prose.
Every one goes through `references.yaml`, where the key is the first author's surname and the
year. **Never rename a key.** Add an alias instead, so links written against the old spelling
keep resolving.

**A chapter may not cite an unverified reference.** An entry marked `verify: true` is one whose
identifier has been claimed but not checked against the source, and `bc.py` fails the build on any
chapter that cites one. This is stricter than it sounds and deliberately so: an unverified citation
is worse than a missing one, because it reads to a clinician as though someone confirmed it. To add
a reference, find the paper on PubMed, confirm the hit is the primary publication rather than a
subgroup analysis or commentary, and record the exact identifier with `verified: true`. A trial
acronym returns many secondary papers, so read the title before accepting one.

Write a citation with a space before the bracket, the way it is comfortable to type:
`...an adaptive survival mechanism [@ali2020].` The build closes that space, so the mark sets
against the word it qualifies rather than floating off it.

Every citation gets a reference card for free. Hovering the mark on a mouse opens a card, tapping
it on a phone opens a sheet, and both read the entry out of the chapter's own reference list, so
there is nothing to add to a chapter and nothing to keep in step. Never hand-write a tooltip or
repeat a reference inline to make one appear.

Citations are numbered in order of first appearance within a page, which is the right
convention when each chapter is its own page. Because the key is permanent, reordering chapters
changes the printed numeral and nothing else.

A cross-reference to a chapter that has not been written yet renders as its title, in muted
type, and is deliberately not a link. Naming a thing the book intends to cover is honest.
Sending a reader to a page that does not exist is not.

DARE names two different studies in this literature. They are keyed separately as `dare-ctdna`
and `dare-tbcrc`. **Never merge them.**

## Fenced blocks

```
​```interplay target=BC-350
One paragraph tying this chapter's subject back to the heterogeneity argument.
​```

​```practice
What to do on Monday. Reserved for the sections that are about a decision rather than a
mechanism.
​```

​```caution
A place where the obvious reading of the evidence is wrong.
​```
```

Every disease-focused chapter in Parts VIII, IX and X should carry at least one interplay
block, tying its subject back to Part VI.

## Voice

The library's `house-style` skill governs. It is three layers: the library's own measured rule,
which comes to **do not chain independent clauses, give each its own sentence**; the
[Google developer documentation style guide](https://developers.google.com/style) underneath it
for everything the measurement did not cover; and six declared deviations from that guide, which
`python3 tools/stylecheck.py --deviations` prints with the reason for each.

Two of those deviations matter most here. This book is **British** and stays British, so
randomised, tumour and oestrogen are correct. It is written in the **third person** and in full
forms, because it is a reference rather than a tutorial and there is no reader being walked
through a task.

On top of the skill, four things this book asks for:

- No em dashes at all. Recast the sentence or use a full stop. This is stricter than the guide,
  which only asks for the dash to be unspaced.
- Say what a number is a number *of*. A hazard ratio without its comparison is decoration.
- Separate biology from measurement in every claim. If a statement is about an assay
  threshold, a sampling scheme or a scoring convention, say so. Most of the disagreement in
  this field lives in that gap.
- Present tense for what a trial shows. `will` belongs only to a trial that has not reported,
  which is why `stylecheck.py` lowers that rule to a suggestion for this book and no other.

The reader already treats this disease. Do not explain what neoadjuvant means. Do explain why a
convention was chosen, because that is what nobody writes down.

Check a draft with `python3 tools/stylecheck.py breast-cancer` alongside `prosecheck.py`. The
first reads the guide, the second reads the sentence architecture, and they do not overlap.

## The evidence block

Parts PT-15 and PT-16 are evidence chapters. They carry the phase II and III trial record for one
subtype, setting and modality, and they are expected to change as new data read out.

They do not hard-code trial results in prose. They declare a table:

````
```evidence setting=early subtype=HR+/HER2- line=adjuvant modality=endocrine
```
````

The block has no body. The build renders the matching rows from `trials.yaml`. A new readout is
therefore added once, to the registry, and appears in every chapter whose filter matches it.

Filter keys are ANDed; a comma-separated value is ORed. A trial with `subtype: all` appears in every
subtype's table, which is correct for an all-comers trial. That wildcard does not extend to `setting`,
`line` or `modality`.

`setting: cns` is a population rather than a point in the disease course. It marks a trial that
required brain or leptomeningeal disease to enter, which is why such a trial does not appear in a
general metastatic table: a whole-brain radiotherapy trial has no business under first-line
chemotherapy. A systemic trial that later reported a CNS subgroup stays `metastatic`, because its
population was never CNS-restricted.

| Key | Values |
|---|---|
| `setting` | early, metastatic, dcis, prevention, mrd, screening, surveillance, recurrence, cns |
| `subtype` | HR+/HER2-, HER2+, HR+/HER2+, TNBC, HER2-low, BRCA, all |
| `line` | neoadjuvant, adjuvant, post-neoadjuvant, 1L, 2L, 3L+ |
| `modality` | endocrine, cdk4-6, chemo, her2, adc, immunotherapy, parp, pi3k-akt, surgery, radiation, bone, supportive |
| `phase`, `status`, `topic` | filters |
| `sort`, `cols`, `caption` | directives, not filters |

Validate with `python3 tools/evidence.py --check`. It fails on a filter that matches no trial, on a
block with a body, on any registry value outside the controlled vocabulary, on two keys that look like
one trial, and on a `primary_ref` missing from its own `pubs`. `--render "<filter>"` previews a table,
`--coverage` lists every block with its match count, `--orphans` lists registry trials no block picks
up, `--axes` checks every trial's axes against the heading the source document filed it under, and
`--topics` reports trials that read like the rest of a tag-filtered table but lack its tag.

**`topic` is doing two jobs.** A filter like `topic=platinum` matches the prose; a filter like
`topic=extended-endocrine` matches a tag appended to it. Both are useful, but a tag only works if
every trial that belongs gets one, and nothing fails when a trial is missed: the table renders, it
is simply short. aTTom was absent from the tamoxifen-duration table for exactly this reason, and
GIM4 and SOLE from the extended-endocrine one, while still appearing in their chapter's overview
table so nothing looked wrong. Append a tag as its own clause after a comma, because `topic` is
printed to the reader, and run `--topics` after adding a trial.

**Adding axes to a trial changes published tables.** A table is a filter, so a trial starts appearing
in one the moment it starts matching. Before merging any batch of axes, render every affected block and
read the prose above it: a paragraph that says "four randomised trials" over a table of six is the
drift this layer exists to prevent, and it is introduced by curating the registry rather than by
editing the chapter.

**Tables enumerate. Prose argues.** Never restate in prose a number the table already carries. The
exception is a number you are arguing *from*, where two trials disagree and the comparison is the
point. A number that lives in two places drifts when one is updated, which is the failure this rule
exists to prevent.

## How deep a management chapter goes

The management chapters in Parts X, XI and XII render the trial record. A section there is
measured against the evidence it shows, not against a word count. It owns every trial its table
carries, and a reader who sees a row and finds nothing in the prose that accounts for it is
entitled to ask why the row is there.

Engaging a table means four things, in whatever order the argument wants them:

- Where the trials agree, said once, rather than trial by trial.
- Where they diverge, and whether the divergence is design, population or endpoint rather than
  drug. This is the sentence most chapters leave out, and it is the one a reader cannot
  reconstruct from the table.
- Which trial the decision actually rests on, and what makes that one load-bearing.
- What the table cannot show. A column that does not exist, a comparison nobody randomised, a
  population nobody enrolled.

That takes longer than the 120 to 250 words a mechanism section needs. A section rendering twenty
trials is not finished in 250. Expect 400 to 700 words where the table is heavy, and 4,000 to
5,000 words for a chapter whose tables carry thirty trials or more.

Length follows the evidence in both directions. A chapter whose tables hold six trials stays
short, and padding it to look like its neighbours is the failure this rule exists to prevent.
`python3 tools/evidence.py --coverage` gives each block's match count, which is the number to
write against.

## Registry fields

`trials.yaml` entries carry `acronym`, `phase`, `setting`, `subtype`, `line`, `modality`,
`population` (free text entry criteria), `n` (randomised), `arms` (experimental vs control),
`endpoint`, `result` (primary endpoint with its comparison, never a bare hazard ratio), `os`
(the overall survival result, or `not reached in either arm`, or `not yet reported` — never blank
to imply a negative), `year`, `status`, `primary_ref` and `cited_by`.

Adding a trial means filling those fields and verifying `primary_ref` against PubMed. Nothing else
has to change for it to appear in the book.

## The trial registry and Appendix A

`trials.yaml` is the book's trial database. Every evidence table in every chapter is generated
from it, and so is Appendix A, the registry page, so a trial cannot say one thing in a chapter
and another in the appendix.

Beyond the axes a filter uses (`setting`, `subtype`, `line`, `modality`, `phase`, `status`) and
the fields a table prints (`n`, `arms`, `endpoint`, `result`, `os`), a record carries its
publication history:

```yaml
  cleopatra:
    primary_ref: swain2020          # the paper the tabulated result comes from
    pubs:
      - {role: primary,      kind: primary,  ref: baselga2011}
      - {role: os,           kind: survival, ref: swain2013}
      - {role: end-of-study, kind: update,   ref: swain2020}
    chapters: [BC-570, BC-900]      # where the trial is meant to be discussed
    reviewed: 2026-09-14            # when the entry was last checked
```

`role` is whatever the source called it. `kind` is the controlled axis: `primary`, `update`,
`survival`, `follow-up`, `biomarker`, `subgroup`, `endpoint`, `protocol`, `pooled`, `quality`,
`other`.

Three more fields carry what the record cannot say in a table cell:

```yaml
  source:                           # where the pivotal-trials document listed it
    - {section: Metastatic disease, ch: 69, group: First line}
  digest:                           # the paper's own account, for a quick look
    methods: One paragraph, from the methods of the abstract.
    results: One paragraph, from the results. Background and conclusions are not kept.
  note: One sentence a reader of the row needs and the row cannot hold.
```

`source` is the document's own filing, and it is a second opinion on the axes rather than a
citation. The document groups by modality and its chapter headings name setting, subtype and
line, so `python3 tools/evidence.py --axes` compares the two and prints every trial where they
disagree. A trial listed under two headings is claimed by both and agreeing with either is
agreement. A bullet that only points at another chapter is marked `xref: true` and asserts
nothing.

`digest` is generated into `src/data/digests.json` rather than into `trials.json`, because the
appendix needs the table to draw and needs a digest only when a reader opens a card.

**What a record says about the result is three states, not a flag.** `tools/evidence.py`
computes it, and both the appendix and the workbook read it from there:

| | |
|---|---|
| `tabulated` | the `result` field is filled, and the evidence tables print it |
| `extracted` | no `result`, but `digest.results` carries what the paper found |
| `none` | nothing on the record says what the trial showed |

This replaced a single "has a result" derived from `tabulated: false`, which counted eleven
ongoing trials with nothing entered as complete, because an ongoing trial never had the flag set.
`none` is the honest state for a trial still running and a gap for one that has reported.

`note` is for the caveat that changes how a row should be read. "The trial enrolled brain
metastases from any primary tumour, not breast cancer only" belongs here. A number does not.

**`primary_ref` is not the trial's first paper.** It is the paper the tabulated result is taken
from, which for a mature trial is usually a long-term report: HERA's is the eleven-year
follow-up, not the 2005 original. Both appear in `pubs`. Every `primary_ref` must also appear
there, so the publication history always contains the paper the table quotes.

`chapters` is editorial intent, and the chapters that actually cite the trial are read out of
the prose. They are allowed to differ, and `python3 tools/evidence.py --gaps` reports both
directions: a trial assigned to a chapter that never mentions it is a gap in the text, and the
reverse is an appendix entry to extend.

A trial the book names but has not tabulated a result for carries `tabulated: false`. It is
listed in the appendix and deliberately has no filter axes, so it cannot appear in an evidence
table until someone enters what it showed.

## Taking the registry out of the book

`python3 tools/export.py` writes `src/data/breast-cancer-trials.xlsx`, which the appendix offers
for download. Six sheets: what the file is, the chapter stories one row per clinical question,
the trials, the publications, one row per chapter-and-trial pair, and every generated table in
the book with the filter that produces it and what it renders today.

It is a working document rather than a report. The **Chapters** sheet filtered to *assigned yes,
cited blank* is the list of chapters that owe a trial a mention, and the **Evidence tables**
sheet says what each chapter already tabulates, which is what stops a number being written into
prose that a table already carries. The **Chapter Stories** sheet is the one to edit a chapter
from, because it says what each group of trials is for and where the argument is still open. The
same division of labour holds inside the workbook as in the book: the story sheet carries no
figures and the trial sheet carries nothing but.

The workbook is deterministic and dated by the registry's latest `reviewed` rather than by the
clock, so two exports of the same data are the same bytes. `tools/sitecheck.py` fails if it has
drifted from `trials.yaml`, because a stale spreadsheet opens and looks right, which is worse
than a broken link.

The appendix also exports whatever is currently filtered, as a CSV, in the browser.

**When a trial reports again**, add the publication to `pubs` with `added: <date>`, add its
reference to `references.yaml` verified, and rebuild. `python3 tools/evidence.py --stale` then
lists the trial, what is new, and every chapter that cites it and may now be out of date. Update
the prose, then set `reviewed` to today to clear it.

## Chapter Stories

The registry says what each trial showed. The evidence table says what else is in the same cell.
Neither says what we were trying to find out, and that is the thing a chapter actually opens with.

`books/breast-cancer/stories.yaml` is that layer. A **story** is one position in the treatment
landscape and an ordered list of the **clinical questions** asked there. The hierarchy is
deliberately shallow:

```
setting (early | metastatic | cns)
  subtype (HR+/HER2- | HER2+ | HR+/HER2+ | TNBC | BRCA | all)
    stage  early: neoadjuvant | adjuvant | post-neoadjuvant
           metastatic: 1L | later | any
      question          <- the deepest level, always
```

The depth belongs in the question, not in the tree. A drug class is not a question: PALOMA-3,
SERENA-4, PADA-1 and SONIA all carry `cdk4-6,endocrine` and ask whether to **add**, to
**substitute**, to **select** and to **sequence** respectively. So the last level is always
something a clinic wants to know, written as a sentence ending in a question mark.

Every question is written in the same five moves, all required:

```
rationale    why the idea was worth testing
experiment   what was actually done to test it
finding      what came back
limitation   what the design cannot tell you
next         the question the finding leaves open
```

A story that cannot fill `limitation` is a story that has not been read properly.

**A story carries no figures.** The number belongs to the registry and is printed by the evidence
table, so a story and a table can never disagree. A story names trials by registry key and a trial
appears under every question it speaks to, which is the point.

In a chapter:

```
​```story ST-010
​```                        the whole story

​```story SQ-0010,SQ-0020
​```                        just those questions, in the order written
```

Ids are permanent. `ST-###` for a position, `SQ-####` for a question, both globally minted and
never renumbered; a question moves between stories by editing its story, not by changing its id.

`python3 tools/stories.py --check` validates the whole layer and runs inside `tools/sitecheck.py`.
`--tree` prints the hierarchy, `--orphans` lists registry trials no question names, and `--axes`
reports questions whose trials disagree with the position they are filed under. A disagreement is
not automatically wrong — a lobular window study belongs in an adjuvant argument, and a story
about what to do after CDK4/6 progression legitimately cites the first-line trial that created the
situation. It is reported so the choice is deliberate rather than accidental.

`docs/breast-cancer/stories.html` draws the whole landscape from `src/data/stories.json`, filtered
and searchable, with each trial linked into the registry appendix.

## Evidence weight

A trial may carry one more axis, and it is the only one a filter has to ask for by name:

```
weight   practice-defining | supporting | exploratory
```

An evidence table enumerates the record a decision rests on. A three-week single-arm window
study is not part of that record, and setting it next to a randomised phase III trial in the
same table with nothing to tell a reader which is which makes both harder to read. So:

- a block that says **nothing** about weight gets everything **except** the exploratory trials
- a block that wants them says `weight=exploratory`, or `weight=any` for the lot

Every trial in the registry before the axis existed has no `weight`, which reads as "not
exploratory", so adding the axis changed no table.

**Exploratory trials are not hidden.** They are in the registry, in Appendix A tagged as such,
in the downloadable workbook, and in the Chapter Stories, which is where a proof of concept
earns its place: under the question it was built to answer, with what its design cannot settle
written next to it. That is the division: a table says what is known, a story says what was
being asked, and an exploratory trial has much more to offer the second than the first.

`python3 tools/evidence.py --weights` reports how the axis is filled and which tables are
currently holding exploratory trials back, with the keys, so the decision to leave one out of a
table is visible rather than silent.
