# Navigation lens: the library shell, between and within books

Evidence lives in `shots/navigation/`. The `prod/` subfolder was served under `/library/`, the way GitHub Pages serves the site. The probe scripts are in `shots/navigation/*.py`: probe, bars, bottom, cont, seq, sa, spy2 and off.

## Read this before using shoot.py

`shoot.py` serves `docs/` at the site root. `pwa.js:38-44` reads the book slug from a `/<prefix>/<slug>/` path, so every root-served shot has `SLUG = null`. Those shots are missing the following:

- the drawer's prev/next row and its destinations
- the sidebar position text ("· 68 of 98")
- arrow-key navigation
- reading-position memory
- the standalone back button

To see what readers actually get, serve under `/library/` as `tools/navcheck.py` does. `shots/navigation/probe.py` shows how.

## Journeys: taps in production today

| Journey | Today | Could be |
|---|---|---|
| New reader: hub to chapter 1 of the clinical book | 3 taps (tile, "All chapters", ch 1). The contents page first repeats the whole front door, so on a phone ch 1 sits at y=736 of 844. | 2 |
| Returning reader: resume chapter 68 | 3 taps (hub, landing, Chapters) plus a scroll through a 10,159 px contents page on a phone. No surface offers "continue". continue.html is only reachable from the Android shortcut. | 1 |
| Next chapter, desktop | Scroll to the foot of the chapter (ch1.1 is 33,325 px), or press the right-arrow key, which nothing on the page mentions. | 1 visible control |
| Next chapter, phone | 2 taps (drawer button, Next). The Next link at the chapter foot sits under the drawer button. | 1 |
| Clinical chapter to physics chapter 1.1 | 4 taps and a scroll (Library, tile, "Start reading" opens contents, 1.1). | 3 |
| The Long Argument: "Chapters" in the bar | Dead end: 0 of 8 chapters written, every row grey. | n/a |
| Change theme on the clinical front door, Stories or Trials | Not possible: those pages have no toggle. | 1 |

## Findings (ranked by cost to the reader)

The full evidence for each finding is in the structured output. This is the short version.

1. **No "continue reading" anywhere a reader looks**
   - The hub, the landings and the contents pages offer nothing, even though `pwa.js` records the position of every page.
   - `continue.html?b=<slug>` says "Nothing recorded yet" whenever the last page read was in a different book (`pwa.py:491`).
2. **The theme flips and fragments**
   - `book.js:8` defaults to light and overrides the boot script's OS-dark choice. `pwa.js` then saves that light setting for the whole library.
   - The hub ignores the stored theme entirely.
   - There are four toggle designs, and the clinical book's landing, Stories and Trials pages have none.
3. **The phone bar wraps to two rows (104 px) on the clinical landing, Stories and Trials**
   - Cause: the coarse-pointer gutter in `nav.css:183-189` is reserved on pages that have no toggle.
   - On the physics landing the floating toggle drops below the bar. In the installed app it covers "Library".
4. **The Long Argument's "Chapters" is a dead end on every page of that book**
   - The Ages of Thought ships an orphaned contents page reading "0 of 0 chapters built".
5. **The contents page restates the front door**
   - On a phone the first chapter is below the fold.
   - Every written row carries a READY badge (98 of 98 in the clinical book, 37 of 37 in the physics book).
   - The sidebar's "← All chapters" links the page to itself.
6. **Phone: the drawer button covers the Next link at the chapter foot.**
7. **Drawer rows added by pwa.js are flush to the panel edge**
   - They have no inset and run to the screen edge.
   - The destination pills repeat the sticky bar, which is always visible.
8. **The sidebar scroll-spy is wrong when scrolling up**
   - 51 of 61 samples highlighted the wrong section.
   - Nothing is highlighted after a jump, a restored position, or at the top of the page.
9. **One destination, many names**
   - In Plain Terms, The Through-Line, Through-Line, and "The whole book, no mathematics" are the same page.
   - Trials, The trial registry and Appendix A are the same page.
   - Chapters, All chapters and Start reading all lead to the contents page.
10. **Controls move between page types**
    - The bar's links shift 74 px left on pages that have the floating toggle.
    - The toggle sits 8 px below the bar's text line.
11. **The Long Argument and The Ages of Thought each have two stacked headers that repeat the book title**
    - The atlas header's title links out to the library hub.
    - On a phone the timeline spends about 218 px on chrome.
12. **Hub dark mode**
    - The Download buttons have a contrast of 1.25:1.
    - The accent kickers and "Read →" links have a contrast of 2.0 to 2.4:1.
13. **Hub tiles**
    - The Ages of Thought says "0 chapters planned".
    - The Long Argument says "8 chapters planned", beside a "Read →" link.
    - The offline shelf lists the four books a second time.
14. **Landing calls to action differ**
    - "Start reading" (physics) opens the contents page, not chapter 0.1.
    - The clinical book says "All chapters".
15. **The offline fallback's only link resolves to the book's folder, not the hub**
    - The fallback page is served at the requested URL, so `href="./"` resolves relative to that page.
16. **Desktop chapters have no visible prev/next above the foot**
    - "10 of 37" in the sidebar counts written chapters, while the contents page says "37 of 76".
17. **Wide screens: the bar is full-bleed while the content is a centred 82 rem box**
    - There is a 5 px gap between the bar and the sidebar.
18. **Standalone (installed app): the bar loses its top padding**
    - The app headers (`.top`) get the safe-area padding too, even though they are no longer at the top of the screen.
19. **pwa.js slug detection depends on the path prefix.**
20. **93 duplicate ids in 24 clinical chapters (`bc.py:445`).**
21. **Phone bar type is 11.5 px for the primary navigation.**

## Strengths to keep

- One producer for the bar (`nav.py`), built from `book.json`:
  - the same order on every page, with `aria-current` on the current entry
  - Library always last and set apart
  - one sticky height of 37 px at desktop width
- The drawer:
  - "68 of 98" position
  - two-column prev/next that keeps its shape on the first and last chapter
  - focus handling, Escape to close, reduced motion respected
- Arrow-key chapter paging.
- `nav.json` works offline.
- Reading-position restore respects a `#hash` in the URL.
- Landing arc rows deep-link into `contents#sec-N`.
- The chapter foot shows the number and title of the previous and next chapters.
- Hub tiles: the whole tile is clickable, and the page takes on each book's colour field before the click.
- The offline shelf quotes both the download size and the stored size.
- `continue.html` and `offline.html` have no dependencies.
- `scroll-padding-top` accounts for the sticky bar.
- The contents page shows unwritten chapters in grey.
- Touch targets in the bar and the drawer are 44 px.
