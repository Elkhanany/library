# Status

24 of 79 chapters written. 203 of the 211 sections those chapters plan, and about 72,000 words.

Wave 1 covers Part IV (molecular biology, 8 chapters), Part V (immunology and the
microenvironment, 5) and Part VI (heterogeneity, evolution and metastatic biology, 11). That is
the biological core, and it is the half of the book every clinical chapter is meant to be able
to assume.

## What works

- **Structure.** All 14 parts, 79 chapters and 673 sections in `outline.yaml` with permanent
  identifiers. `tools/bc.py` derives `curriculum.json` from it, so display numbers are computed
  and the outline is the only place structure is stated.
- **Prose.** `chapters/BC-###.md` becomes `src/BC-###.html` becomes a built page. 591 citations,
  30 trial mentions, 6 glossary terms and 26 interplay blocks resolve across the 24.
- **The reference store** holds 295 entries, 285 of them cited. Every one carries a confirmed
  identifier, and `bc.py` now refuses to build a chapter that cites a reference marked
  unverified.
- **Trials** 38 entries, including the two different studies both called DARE, which stay
  keyed apart.
- **Cross-references** resolve by permanent identifier: a link when the target is written, muted
  unlinked text when it is not. 116 of the latter, which is what 55 unwritten chapters look like.
- **The app layer** is whatever the library gives every book: installable, readable with the
  network off, scroll position per chapter, download-everything, light and dark.

## Open editorial question

**Spelling.** All 24 chapters are consistently British: 528 `tumour` against 16 `tumor`, 103
`oestrogen` against 1 `estrogen`. `outline.yaml` is consistently American, and section headings
are rendered from the outline, so a chapter currently reads with an American heading over
British prose. Both fixes are large and neither is mechanical:

- Change the outline to British and 673 section titles move.
- Change the prose to American and 72,000 words of someone's voice move.

Nothing is broken either way. It wants deciding before wave 2 doubles the cost.

## Quarantined

`_quarantine/BC-040.md.unverified` is a drafted chapter whose writing agent was cut off before
it returned its reference patch. It cites nine keys that are not in `references.yaml` and that
nobody has checked. The prose is probably fine. It may not be published until each identifier is
confirmed against the source, which is now enforced rather than remembered: `bc.py` fails the
build on an unverified citation.

## What is not built yet

None of it blocks writing prose.

1. **Citation bottom sheets.** Tapping a superscript jumps to the foot of the chapter. It should
   open a sheet with the reference, its link and its *cited in* list, and dismiss back to the
   exact scroll position. With 591 citations live, this is now the biggest reading-experience
   item on a phone.
2. **Cross-reference preview sheets.** Same shape, for `[[BC-###]]`.
3. **Search.** The library has none, for any book.
4. **The generated appendices.** Nine declared, five generated: trials (APP-A), glossary
   (APP-B), the interplay map (APP-F), the research agenda (APP-G) and the full bibliography
   with *cited in* backlinks (APP-I). `bc.py` already collects the interplay edges APP-F needs.
5. **Tags.** 18 declared, applied to 67 chapters, read by nothing.

## Next

Parts I, II, III and VII, which are the rest of the foundation. Then the treatment parts, which
can be written short because they cite Part VIII rather than repeating it. `briefs/PT-XX.md`
carries the argument for each, and `_specs/BC-###.txt` the exact section titles.
