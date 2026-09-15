# Status

**Complete.** 16 parts, 93 chapters, 778 of 778 sections. No chapter is partial.

1,099 references and 389 trials in the registries, every identifier PubMed-verified. 195 caution
blocks, 107 in-practice blocks, 70 interplay edges, 67 evidence tables, and
17 Chapter Stories carrying 97 clinical questions.

## Chapter Stories

`stories.yaml` is the argument layer and `stories.html` is its reader-facing face. One position in
the treatment landscape, one ordered list of the clinical questions asked there, each written in
five moves: rationale, experiment, finding, limitation, and the question the finding leaves open.
309 of 389 trials sit under a question.

A story carries no figures at all. The number belongs to the registry and the evidence table prints
it, so a story and a table cannot disagree about one. `tools/stories.py --axes` reports where a
question's trials disagree with the position it is filed under, which is usually deliberate and
always worth seeing.

Thirteen chapters open their argument with a story block before their first table.

## Appendix A, the trial registry

`trials.yaml` is the book's trial database and `trials.html` is its reader-facing face. 389
trials, 506 publications. The same records generate both the in-chapter evidence tables and the
appendix, so the two cannot disagree.

The appendix filters on the axes the evidence blocks already use (setting, subtype, line,
modality, status) and searches name, topic, population and result. It reads in two ways: one
list of everything, or grouped under the chapter each trial is assigned to. Expanding a trial
shows the paper's own account of what was done and what was found, any caveat the row cannot
hold, its full publication history with PubMed links, the chapters it is assigned to, and the
chapters that actually cite it.

Five counts sit at the head of it, and three of them are worklists:

| | |
|---|---|
| 389 trials, 506 publications | the database |
| 303 with a tabulated result | a result field the evidence tables print |
| 51 extracted, not tabulated | the paper's findings are on the record, nobody has written the one-line result |
| 35 with no result at all | mostly trials still running, which is the truth rather than a gap |
| 44 marked exploratory | held back from the chapter tables by design, and placed in a story instead |

**When a trial reports again**: add the publication to its `pubs` with `added: <date>`, add the
reference verified, rebuild. `tools/evidence.py --stale` then names the trial, what is new, and
every chapter citing it that may now be out of date. Update the prose and set `reviewed` to
today to clear it. `--gaps` reports the other axis: trials assigned to a chapter that never
mentions them (154 today) and trials a chapter cites that the source document does not list (65).

The appendix is a web page rather than a chapter, because it fetches its data at runtime. It is
precached like everything else, so it works offline on the published site; it is deliberately
absent from the self-contained `build/` tree, where `file://` forbids the fetch.

## The quick look

306 of the 307 trials with a publication carry a `digest`: the methods and the results of the
paper the registry quotes, in the paper's own terms, with the background and the conclusion left
out. The background restates what the reader already knows and the conclusion is the authors'
reading rather than the finding, so neither is kept.

The digests are generated into `src/data/digests.json` rather than into `trials.json`, because
drawing the table needs none of them and opening one card needs one. The appendix fetches the
file the first time a reader expands a trial.

The one trial without a digest is the Ahmed phase I study of radiotherapy followed by intrathecal
trastuzumab and pertuzumab, whose abstract never reached the registry.

## Taking it out of the book

`python3 tools/export.py` writes the registry to a spreadsheet, and the appendix offers it for
download. Five sheets: what the file is and the rules that govern an edit, the trials, the
publications, one row per chapter-and-trial pair, and every generated table in the book with its
filter and what it renders today.

The **Chapters** sheet is the point of it. Its *To do* column says what is owed, and the counts
are the work:

| | |
|---|---|
| 62 | a chapter is meant to discuss a trial, no table carries it, and the prose does not mention it |
| 110 | a table in the chapter already carries the trial and the prose does not take it up |
| 184 | a chapter cites a trial the registry does not assign to it, so the registry entry wants extending |

The **Evidence tables** sheet is the guard against the failure this whole layer exists to
prevent. It says what each chapter already tabulates, so a number is not written into prose that
a table beside it already carries.

The workbook is deterministic and dated by the registry's latest `reviewed` rather than by the
clock, so two exports of unchanged data are the same bytes and `tools/sitecheck.py` can fail on a
stale one. It is written by `tools/xlsx.py`, about a hundred lines of the standard library, so a
clone produces it without installing anything.

The appendix also exports whatever is currently filtered, as a CSV, in the browser.

## What the source document is used for

Every trial that came from the pivotal-trials document records where it was listed: the section,
the numbered chapter, and the grouping heading under it. That path is an independent assertion
about the trial's axes, because the document groups by modality and its chapter headings name
setting, subtype and line.

`tools/evidence.py --axes` compares the two and prints every disagreement. It found four, of
which one was a registry error: BOLERO-2 carried `modality: endocrine,other` when everolimus is
an mTOR inhibitor and the vocabulary's slot for it is `pi3k-akt`. The consequence was visible in
the book. BC-870 says "one pathway, six trials" over a table filtered on `pi3k-akt`, and BOLERO-2
was missing from it. The other three were the check being too strict, and the expectation table
carries a comment at each of them saying why.

## What a reviewer found, and what changed

An oncologist reviewed the workbook against the publications. Five findings, all of which held up:

**One record held two trials.** ADAPT is an umbrella, and the entry labelled WSG-ADAPT HER2+/HR+
carried the hormone receptor-negative sub-trial's two papers alongside the receptor-positive
primary, while duplicating the separate WSG-ADAPT-TP record. The hand-written entry had described
the triple-positive trial, and the import then matched the document's "HER2+/HR−" line to it by
name. The two keys now hold the trials their names claim, and BC-840 cites the one it meant.

**"Has a result" counted eleven ongoing trials as complete**, because it was derived from a flag
those trials never carried. It is now computed from the record, which today reads 303 tabulated,
51 extracted and 35 with nothing. The claim of 303 was the flag's, not the registry's.

**VIKTORIA-1 read `awaited` with its phase III result already on the record**, and its N of 701
was the whole trial where the published result belongs to the 392-patient PIK3CA wild-type cohort.
**NeoTRIP** tabulates a pathological complete response while its primary event-free survival
endpoint is conference-reported only, which the record now says rather than implies.

**Four generated tables were short**, each for the same reason: `topic` is both prose and a filter
tag, and four trials never got the tag. aTTom, GIM4, SOLE and lidERA are in their tables now, and
`tools/evidence.py --topics` reports the next one. Reading its output added ABCSG-8/ARNO 95 and
FATA-GIM3 to the aromatase-inhibitor-against-tamoxifen table, and BS-6760 and BS-6780 were rewritten
to match what their tables now hold.

**Four trials were missing** and are in: INSEMA, EA2108, AZURE at ten years, and D-CARE.

Also from the same review: **209 trials now carry a registration identifier**, up from 6, read out
of the abstracts already on file rather than looked up. Eight are ambiguous because their
publications name more than one registration, usually because one paper reports two trials, and
those are deliberately left empty. 111 state none at all, most of them older than the practice.

## Two open editorial questions

**1. Spelling.** The prose is overwhelmingly British: 1,293 `tumour` against 32 `tumor`, 225
`oestrogen` against 5, 131 `signalling` against 14. `outline.yaml` is still American, and section
headings render from the outline, so every chapter reads with an American heading over British
prose. This was flagged at 24 chapters and is unchanged at 93.

The cheap direction is now clear. Changing the outline is about 50 words in structured data, plus
the matching `## BS-####` heading lines in the chapter files, which is one mechanical substitution
that `bc.py` verifies exactly. Changing the prose is roughly 1,700 edits across 236,000 words.
Nothing is broken either way, and it wants one decision.

**2. Prose that duplicates a table.** Two known cases, both the drift the rule above exists to
prevent:

- `BC-500` restates NeoSphere, TRAIN-2, DESTINY-Breast11, KATHERINE and APHINITY numbers that the
  new `BC-820` and `BC-830` tables now carry.
- `BC-170` carries full clinical reporting of SOLAR-1, CAPItello-291 and INAVO120 that duplicates
  `BC-450` and `BC-870`.

No contradiction in either, so neither is urgent. Both are a pass with the tables open.

## Also open

- **The nine appendices have no inbound references.** `APP-A` through `APP-I` are declared and
  nothing in any chapter points at them.
- **17 CNS trials reach no table.** The radiotherapy foundations, the leptomeningeal radiotherapy
  trials and the cross-subtype brain metastasis studies are assigned to `BC-600`, which is not an
  evidence chapter, so nothing generates a table for them. The 20 HER2-directed ones are in
  `BS-7610`. Either `BC-600` gains a table or those records stay appendix-only.
- **76 registry trials match no evidence block.** Most are correct rather than a gap: the
  surgical, radiation, screening, prevention and DCIS trials belong to setting-level chapters
  that carry no evidence block. `tools/evidence.py --orphans` lists them.
- **156 trials are assigned to a chapter that does not mention them.** This is the import's
  editorial intent meeting prose written before it, and it is the worklist for extending the
  text rather than a defect.

## What the machinery still does not do

None of it blocks reading, and all of it is library-wide rather than specific to this book.

1. **The *cited in* list on a reference.** The reference card is built: hovering a citation on a
   mouse opens a card, tapping one on a phone opens a sheet, and both read the entry out of the
   page's own reference list so they work with the network off. What the card cannot yet show is
   which *other* chapters cite the same paper, because that needs a cross-chapter index the build
   does not emit.
2. **Cross-reference preview sheets.** Same shape, for `[[BC-###]]`: the target's title and opening
   lines, with a *go there* action.
3. **Search.** The library has none, for any book. At 236,000 words this book needs it most.
4. **The generated appendices.** Five of the nine are meant to be generated: trials (`APP-A`),
   glossary (`APP-B`), the interplay map (`APP-F`), the research agenda (`APP-G`) and the full
   bibliography with *cited in* backlinks (`APP-I`). `bc.py` already collects the 70 interplay edges
   `APP-F` needs.
5. **Tags.** Declared, applied, and read by nothing.
