# Front doors and appendices: how the four books read as one library

Evidence is in `shots/front-doors/`. The top level holds viewport shots at 390 and 1280 px, in light and dark. The subfolders and helpers are:

- `full/`: full-page shots.
- Clips: `bc-landing-*`, `nmt-landing-*`, `bc-contents-partIX-*`, `trials-row-open-1280`, `stories-open-1280`.
- Hover states: `hub-hover-*`.
- A first-visit theme walk: `themeflow-*`.
- Probe scripts: `_measure.py`, `_clip.py`, `_open.py`, `_hover.py`, `_themeflow.py`.

Screenshots come from a Linux Chromium, so the serif shown is a fallback. The families and weights in these notes were measured as computed styles.

## Findings, ranked by cost to the reader

1. **Appendix A is set entirely in semibold sans.** The in-prose trial mark `.trial` in `book.css:233` also matches every `<details class="trial">` row in `_trials.html:42`.
   - Each row inherits sans at weight 600, .88em, with `cursor:help`.
   - 10,675 text nodes are at weight 600, including every abstract, Result row and publication.
   - Evidence: `trials-row-open-1280.png`.
2. **The theme fragments across the front doors.** This overlaps with the navigation lens.
   - `book.js:8` defaults to light and overrides the boot script's OS-dark choice.
   - The hub CSS reads only `prefers-color-scheme` (`webbuild.py:356`).
   - The clinical landing, Stories and Trials pages have no toggle at all.
   - Evidence, a dark-OS first visit: hub dark → BC landing dark → contents light → BC landing light → the hub dark again, even though `data-theme` is light.
3. **Hub dark mode does not swap the book accents.** The tile's `--bk-accent` is always the light accent (`webbuild.py:434`).
   - Kickers and "Read →" measure 1.98:1 (physics), 2.22:1 (clinical), 2.38:1 (TLA) and 3.38:1 (atlas).
4. **There are two type systems.**
   - The hub, landings, contents and appendices use Iowan Old Style/Palatino with the system sans.
   - The atlas and the timeline name Spectral, IBM Plex Sans and IBM Plex Mono, but no font file ships, so they render in Georgia and the system sans.
   - Result: two different serifs in one library.
   - Sans weights in use: 400, 500, 550, 600, 650 and 700.
5. **The hub eyebrow is 18.24 px, 700 weight, 4 px tracking.** `.lede p` (`webbuild.py:293`) beats `.eyebrow` (`:289`).
   - It is 1.6 times the size of every other eyebrow on the site, and it competes with the H1.
6. **Every page in a book sets the title differently.** In the clinical book:

   | Page | Title | Eyebrow | Stats |
   |---|---|---|---|
   | Landing | serif 83 px | grey, .22em | serif stat cells between hairlines |
   | Contents | sans 36 px, weight 700 | accent colour, .13em | "98 of 98 chapters built" in prose |
   | Stories and Trials | serif 43 px | accent colour, .13em | sans stats at weight 650, no cells |

   - Across the site the small uppercase label comes in nine versions, from 9.5 to 11.8 px.
7. **book.css class names collide with front-door classes.**
   - `.hero` (`book.css:579`) puts a full-bleed rule and a 40 px margin under the landing hero. That rule cuts through the figure on a phone.
   - `.story` (`book.css:420`) gives every Stories row a 3 px pink bar and 32 px margins.
   - The h2 default border on the contents `.part-head` makes a double hairline between parts.
8. **The philosophy books have no front door in the library's register.**
   - Each opens straight into its instrument, under a second header that repeats the bar's title.
   - The book.json `thesis` is never shown.
   - TLA's eyebrow "A build-it-yourself book" is copied from the physics book.
9. **The atlas guide panel has no side padding.** `.guide{padding:4px 0}` (`_landing.html:447`) overrides `.pscroll` (`:409`).
   - The intro sits flush against the panel rule at x=923. It is the first thing a desktop reader sees.
10. **Contents pages invert the hierarchy.**
    - Part titles are 11.8 px tracked capitals; Part IX runs to 3 lines on a phone.
    - Chapter titles beneath them are 19 px bold accent-colour serif.
    - Every row carries a green READY chip, and the physics book adds a purple MATH chip.
    - `build.py:153` itself says that a badge on every row is decoration.
11. **The hub does not use the house register.**
    - Its tiles are boxed, blurred, lifting and shadowed cards, which `landing.css` rejects.
    - Every tile has the same height, so the Ages tile is mostly empty.
    - Tile counts read "0 chapters planned" and "8 chapters planned".
12. **Hero figures sit under the words.**
    - The physics light-cone lines cross the H1, the lede and the thesis at both widths.
    - The stat hairlines cut through the clinical book's core.
    - On a phone the caption sits on the densest cells and says "Above:" of a figure that is behind it.
13. Smaller items:
    - Four left edges and measures across the clinical book's front pages.
    - Naming drift: Appendix A has a letter and Stories has none; the Through-Line's eyebrow says "Reference".
    - The orphan atlas contents page reads "0 of 0 chapters built" and still ships offline.
    - The TLA contents page is eight grey non-links.
    - The physics contents H1 breaks as "M-" / "Theory" at 390.
    - The physics link-columns look identical to the clinical book's non-link columns.
    - The atlas and TLA hard-code palettes that drift from book.json.

## What must survive

- The hub's per-book weather. Hovering a tile tints the whole page from book.json `field` and the accent, translucently, so it survives dark mode.
- landing.css's register:
  - the serif for prose, the sans for labels, hairlines instead of boxes;
  - one primary button, with the other ways in as text links.
- The landing's stat row, computed at build time, and the generated part index: numeral column, tabular right-aligned counts, "planned" set on its own line.
- Each landing's figure as the thesis drawn: the light cone, and a biopsy core passing over clones. Both respect reduced motion and are coloured from the accent.
- The thesis set as a rule-led italic blockquote rather than in quotation marks.
- One nav bar from nav.py: `aria-current`, the short brand name, 44 px touch targets.
- Stories' five-move grid: Rationale, Experiment, Finding, Limitation, Next question.
- The atlas's drawn age rail and the timeline's world lanes. They are real identity; keep them.
