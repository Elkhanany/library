# Status

**Complete.** 16 parts, 93 chapters, 778 of 778 sections. No chapter is partial.

1,033 references and 325 trials in the registries, every identifier PubMed-verified. 195 caution
blocks, 107 in-practice blocks, 70 interplay edges, 66 evidence tables.

## Appendix A, the trial registry

`trials.yaml` is the book's trial database and `trials.html` is its reader-facing face. 325
trials, 436 publications. The same records generate both the in-chapter evidence tables and the
appendix, so the two cannot disagree.

The appendix filters on the axes the evidence blocks already use (setting, subtype, line,
modality, status) and searches name, topic, population and result. It reads in two ways: one
list of everything, or grouped under the chapter each trial is assigned to. Expanding a trial
shows the paper's own account of what was done and what was found, any caveat the row cannot
hold, its full publication history with PubMed links, the chapters it is assigned to, and the
chapters that actually cite it.

Four counts sit at the head of it, and two of them are worklists:

| | |
|---|---|
| 325 trials, 436 publications | the database |
| 22 awaiting a tabulated result | named in the book's scope, no result entered, so they cannot appear in an evidence table |
| 141 not yet cited in the text | in the registry, no chapter mentions them |

**When a trial reports again**: add the publication to its `pubs` with `added: <date>`, add the
reference verified, rebuild. `tools/evidence.py --stale` then names the trial, what is new, and
every chapter citing it that may now be out of date. Update the prose and set `reviewed` to
today to clear it. `--gaps` reports the other axis: trials assigned to a chapter that never
mentions them (156 today) and trials a chapter cites that the source document does not list (66).

The appendix is a web page rather than a chapter, because it fetches its data at runtime. It is
precached like everything else, so it works offline on the published site; it is deliberately
absent from the self-contained `build/` tree, where `file://` forbids the fetch.

## The quick look

302 of the 303 trials with a publication carry a `digest`: the methods and the results of the
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
