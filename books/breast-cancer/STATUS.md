# Status

Skeleton and infrastructure. One chapter of prose.

## What works

- **Structure.** All 14 parts, 79 chapters and 673 sections are in `outline.yaml` with
  permanent identifiers. `tools/bc.py` derives `curriculum.json` from it, so display numbers
  are computed and the outline is the only place structure is stated.
- **The contents page** lists every planned chapter under its part, marks the one that is
  written, and shows a live count.
- **Chapter pages.** `chapters/BC-###.md` becomes `src/BC-###.html` becomes a built page.
  `BC-280` exercises the whole path.
- **Citations** resolve from `references.yaml` to numbered superscripts and a per-chapter
  reference list with PubMed links. 50 references seeded.
- **Trials** resolve from `trials.yaml` to the acronym, carrying phase, setting and topic.
  23 seeded.
- **Cross-references** resolve by permanent identifier, to a link when the target is written
  and to muted unlinked text when it is not.
- **Interplay, practice and caution blocks** render as styled asides.
- **The app layer** is whatever the library already gives every book: installable to a home
  screen, readable with the network off, scroll position remembered per chapter, a
  download-everything control, safe-area handling, light and dark.

## What is not built yet

These are the parts of the original specification that the library has no machinery for. None
of them blocks writing prose.

1. **Citation bottom sheets.** Tapping a superscript currently jumps to the foot of the
   chapter. It should open a sheet with the reference, its link and its *cited in* list, and
   dismiss back to the exact scroll position. This is the single biggest reading-experience
   item on a phone.
2. **Cross-reference preview sheets.** Same shape: tap to preview the target's title and
   opening lines, with a *go there* action.
3. **Search.** The library has none, for any book. Needs an offline inverted index over
   chapter and section titles, tags, body text and reference keys.
4. **The generated appendices.** Nine are declared in `outline.yaml`, five of them generated:
   the trial registry (APP-A), the glossary (APP-B), the interplay map (APP-F), the research
   agenda (APP-G) and the full bibliography with *cited in* backlinks (APP-I). `bc.py` already
   collects the interplay edges it would need.
5. **Tags.** An 18-term vocabulary is declared and applied to 67 chapters. Nothing reads it
   yet.
6. **Section-level navigation across chapters.** Sections are anchors within a chapter and
   appear in the sidebar. They are not yet first-class in the contents page or in search.

## Next

Write prose. The original plan said not to start until the app layer worked, and it does. The
three chapters that exercise the most machinery are `BC-280` (written), `BC-300` (temporal
heterogeneity and clonal evolution) and `BC-350` (integrative biological interplay, which
APP-F is generated from).
