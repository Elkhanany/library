# Status

**Complete.** 16 parts, 93 chapters, 778 of 778 sections. No chapter is partial.

834 references and 206 trials in the registries, every identifier PubMed-verified. 824 references
are cited. 195 caution blocks, 107 in-practice blocks, 70 interplay edges, 65 evidence tables.

## The evidence layer

The thing that makes this book maintainable rather than dated. An evidence chapter does not write
trial results into prose. It declares a filter, the block carries no body, and rows render from
`trials.yaml` at build time. **A new readout is entered once in the registry and appears in every
chapter whose filter matches it.** There is no prose to hunt down when data change.

`bc.py` fails the build on a filter matching no trial, or on a block with a body, so a table cannot
silently go empty. `tools/evidence.py --check`, `--coverage`, `--orphans` and `--render` inspect the
layer without building.

The rule that keeps the two from drifting: **never restate in prose a number the table carries**,
unless you are arguing from it, because a number living in two places drifts when one is updated.

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
- **No ongoing metastatic trials in the registry** for HER2-positive, triple-positive or TNBC. The
  early-disease chapters have them, so their "what reads out next" sections are generated; the
  metastatic ones are prose only.
- **50 registry trials match no evidence block.** Correct rather than a gap: they are the surgical,
  radiation, screening and prevention trials belonging to the setting-level chapters.
  `tools/evidence.py --orphans` lists them.

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
