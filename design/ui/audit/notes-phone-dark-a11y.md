# Lens: phone, dark mode, accessibility and weight

Evidence is in `shots/phone-dark-a11y/`:

- Screenshots: `<page>.<width>.<theme>.png`, plus `focus/`, `osdark-nostore.*`, `sticky.*`, `scrolled.*`, `clip.*`, `drawer.*`, `forced.*` and `lastudy.*`.
- Probes: `probe/*.py`. Every probe serves `docs/` under `/library/`, the way GitHub Pages does, so `pwa.js` knows the book slug.
- Raw results: `probe/*.json`.

Pages covered are the hub, and the front door, contents page and one chapter of each book. The atlas "chapter" is its dossier (`#who=spinoza`). The timeline "chapter" is a study, opened with `openStudy`.

Shots were taken at 390 px (light and dark) and at 1280 px (dark).

## Numbers

### WCAG contrast from the CSS values

Sources:

- `book.css:5-55` defaults, plus `themecss()` in `tools/webbuild.py:49-79` from each `book.json`.
- Light and dark are shown as L / D.

| book (book.css pages) | body ink | ink-soft | ink-faint | link = accent | accent on accent-soft | link vs body text |
|---|---|---|---|---|---|---|
| Breast Cancer | 16.13 / 13.05 | 8.00 / 7.75 | **3.41** / 4.37 | 7.21 / 6.12 | 6.14 / 5.34 | 2.24 / 2.13 |
| Newton to M-Theory | 16.48 / 13.05 | 8.43 / 7.75 | **3.60** / 4.37 | 8.51 / 7.93 | 7.66 / 6.70 | (underlined) |
| Ages of Thought (contents) | 13.80 / 13.05 | 7.48 / 7.75 | **3.19** / 4.37 | **4.43** / 5.96 | **3.91** / 5.21 | |
| Long Argument (contents) | 14.92 / 13.05 | 7.24 / 7.75 | **3.09** / 4.37 | 6.10 / **3.88** | 5.19 / **3.56** | |

**On bg-alt (the sidebar and the drawer):**

- ink-faint is 2.84 to 3.33 in light and 4.02 in dark.

**The two books' own palettes:**

- The atlas:
  - `--ink-3` is 4.86 (L) and 8.15 (D).
  - `--accent` is 3.48 (L) on paper.
- The timeline:
  - `--ink-3` is **3.15** (L) and 4.58 (D).
  - `--ink-4`, used as text, is **1.84** (L) and **2.78** (D).

**The hub in dark mode** (tile background #181b1f):

- The kicker and "Read →" are **2.00** (Newton), **2.24** (Breast Cancer), **2.40** (Long Argument) and **3.41** (Ages).
- The Download buttons are **1.25**, because the text is #e6e6e2 on a #fff button.

**Tokens that pass 4.5:1 on all four papers and on bg-alt:**

| token | light | dark |
|---|---|---|
| ink-faint | #63636a | #84868c |
| Long Argument accent_dark | #e4635f (the timeline's own rubric): 5.34, and 4.74 on soft | |
| Ages accent | #974d26: 5.24, and 4.58 on soft | |

### Census of failing text groups

This is a per-page census of every visible text node (`probe/census.*.json`). Each entry gives the count of text nodes below AA.

**The trial registry:**

| element | nodes | ratio L / D |
|---|---|---|
| `.tmeta i` | 1,162 | 3.41 / 4.37 |
| `dl dt` | 935 | 3.41 / 4.37 |
| `.body h4` | 621 | 3.41 / 4.37 |

**The stories page:**

| element | nodes | ratio L / D |
|---|---|---|
| `.sq-moves dt` | 570 | 3.41 / 4.37 |
| `.yr` | 486 | 3.76 / 4.16 |

**The contents pages:**

- `.cnum` fails on every row.
- `.pending` chapter titles at 17 to 19 px are 3.09 to 3.60 in light.

**Chapter pages:**

| element | ratio |
|---|---|
| eqnum ×57 | 3.60 / 4.37 |
| `.pnum` | 3.60 / 4.37 |
| `.chapnav span` | 3.60 / 4.37 |
| `.callout.plain .pnum` (opacity .62) | 2.73 / 3.90 |
| `.ctrl button.on` in dark (#fff on #7fb0e8) | 2.26 |

### Keyboard

These results come from Tab presses in Chromium (`probe/focus.py`, `probe/taborder.py`, `focus/*.png`).

- **Book pages:**
  - The user agent ring is never removed.
  - The ring is clearly visible on dark (see `focus/breast-cancer__BC-900.html.1280.dark.step02.png`, step09 and step17).
  - No page defines `:focus-visible`.
- **BC-900:**
  - 208 tab stops, of which 100 are citations, 58 reference-list links and 32 cross-references.
  - 15 stops come before the first one in `<main>`.
  - There is no skip link.
- **ch1-2:** 131 stops, 31 of them before `<main>`.
- **The floating theme toggle is the last stop:** 208 of 208 on BC-900 and 131 of 131 on ch1-2. Cause: it is appended to `<body>`, `book.js:22`.
- **The section drawer button is also last:** 198 of 198 at 390 px. Cause: `book.js:232`.
- **Hub tiles:**
  - `outline:none` (`webbuild.py:310-315`) leaves a 1 px border in the light-mode accent as the only focus sign on the tile.
  - That border is 2.0 to 3.4:1 on dark.
- **Timeline and atlas:**
  - A designed 2 px ring in `--focus`.
  - The timeline has a "Skip the timeline" link.

### Reduced motion

Measured with `probe/motion.py`, using Playwright's `reduced_motion='reduce'`.

- `html{scroll-behavior:smooth}` (`book.css:60`) has no reduced-motion override.
- Sidebar jump on BC-900 at 1280, `scrollY` sampled every 60 ms: 0 → 270 → 1,526 → 3,863 → 7,231 → 11,375 → 15,814 → 19,959. This is identical with and without the preference.
- The drawer jump at 390 goes 0 → 26,304 px, animated.
- `book.js:282-290` passes `behavior:'auto'`, which resolves back to the CSS `smooth`.
- The landing canvases are still under reduce: two frames 1 s apart are identical.
- The drawer, the reference card and the landing transitions all have overrides.
- The atlas sets every transition to 1e-5 s.
- The timeline keeps a 0.18 s transform on 133 `.plate` buttons.
- The timeline and the atlas call `scrollIntoView({behavior:'smooth'})` 7 and 2 times, with no JS check for reduced motion.

### Overflow at 390 px

152 pages were swept (`probe/overflow.py`).

- No page's `scrollWidth` exceeds 390, because `book.css:116` and `:632` set `html,body{overflow-x:hidden}` at 1000 px and below.
- With that mask removed, 31 pages are wider than the viewport:
  - 23 clinical chapters by 2 px. `.evidence` has `margin-inline:-1rem` (`book.css:449`) against a `.main` padding of `.9rem` (`book.css:121`).
  - ch4-2 to ch4-9 by 226 to 1,155 px. The cause is `.pause span{white-space:nowrap}` (`book.css:197`), with natural widths of 616 to 1,545 px. The label text is cut off.
- Atlas dossier: `#btnTheme` is clipped at x=386 to 403.

### Sticky and fixed chrome

Measured with `probe/sticky.py`, `scrolled.*` and `lastudy.*`.

**At 390, after scrolling 1,500 px:**

- On book.css pages, no library bar remains: the overflow mask stops `position:sticky` working.
- The 47 px drawer button stays over the text column. It covered text at every sampled position:
  - "2 · First-line dual blockade w…" and "The first-generation conjugate…" on BC-900
  - equation glyphs on ch1-2
- The open drawer (z 62) covers the button (z 60). The ✕ state is never visible, and the drawer closes only by the scrim or Escape.

**At 1280 on trials and stories:**

- The sticky `.bar` (`z-index:5; top:0`; `src/_trials.html:24`, `src/_stories.html:21`) slides under the library bar (z 40, 37 px).
- The top 37 px of the filter controls are hidden (`scrolled.breast-cancer__trials.html.1280.dark.y1500.png`).

**Timeline study at 390:**

- The first prose line sits at y=240: 236 px (28%) of the screen is chrome that stays.
- That chrome is five stacked bars: the library bar, the app header, the view tabs, the open-studies bar and the section tabs.

### Tap targets at 390 with pointer:coarse

Measured with `probe/taps.py`.

**At or above 44 px:**

| target | height |
|---|---|
| bar links | 44 |
| drawer rows | 42 to 80 |
| drawer destinations | 44 |
| drawer previous and next | 68.5 |
| drawer button | 47 |
| landing CTA | 46.7 |
| hub tiles | 224 |
| figure buttons and sliders | 44 |

**Below 44 px:**

| target | height |
|---|---|
| `#themer` on the physics landing, the page's only theme control | 23.6 |
| contents chapter links | 38.7 (54 of 98 clinical, 31 of 37 physics) |
| trials and stories filters | 38 (12 of 12) |
| timeline study tabs `.snav a` | 24.5 |
| timeline chips | 40 |
| atlas tool buttons | 34 (13 to 15 of 35 to 41) |
| grind and problem toggles | 30.7 minimum |
| landing footer link | 14 |
| hub "Reset offline data" | 18 |

Inline citations (19.6 to 25.9 px, 45 of 100 under 24 px wide) and equation references (12 to 16 px) fall under the inline exemption.

### Weight per page type

Sizes are raw / gzip (`probe/weight.json`, `coverage.json`, `perf.py`). Timings use 4× CPU throttling.

| page | HTML | CSS (linked + inline) | JS (linked + inline) | data | fonts | DOM | DCL |
|---|---|---|---|---|---|---|---|
| hub | 13.0 / 4.5 KB | 8.7 + 8.2 KB | 29.2 + 1.1 KB | 10.3 KB | – | 98 | 79 ms |
| landing (Breast Cancer) | 20.2 / 7.3 | 65.4 / 21.3 | 29.2 + 7.9 | 19.1 | – | 180 | |
| contents (Breast Cancer) | 24.5 / 5.5 | 52.7 / 17.2 | 56.7 / 18.2 | 19.1 | – | 653 | |
| chapter BC-900 | 126.8 / 31.2 | 52.7 / 17.2 | 56.7 / 18.2 | 19.1 | – | 1,183 | 604 ms |
| chapter ch1-2 | **2,081 / 147** | 75.7 / 20.6 | 56.7 + 23.9 | 6.2 | **155.6** | **52,667** | **4,904 ms** |
| ledger | 1,526 / 142 | 75.7 | 56.7 | 6.2 | 135.4 | 38,858 | 4,505 ms |
| trials | 25.8 | 52.7 + 6.5 | 29.2 + 16.1 | **799 / 176** | – | 17,661 | |
| atlas | 138 / 38.5 | 18.4 + 36.5 | 29.2 + 94.2 | 163 / 58 | – | 797 | 282 ms |
| timeline | 391 / 134 | 18.4 + 71.8 | 29.2 + 306 | **1,233 / 444** | – | 3,432 | 1,265 ms |

Notes on the table:

- **KaTeX:**
  - The MathML copies are 359 KB of ch1-2's 2 MB.
  - The page carries 923 KaTeX spans.
  - `katex.min.css` is 18% used.
- **Timeline data:** `formal.json` (298 KB) is fetched on load, whether or not the Formal tab is opened.
- **Comments:** they are this share of each shipped file:

  | file | comments |
  |---|---|
  | book.css | 26% |
  | landing.css | 41% |
  | nav.css | 67% |
  | pwa.css | 40% |
  | book.js | 24% |
  | pwa.js | 33% |

  Stripping comments and collapsing whitespace takes a chapter's CSS and JS from 122 KB raw / 35 KB gzip to about 62 / 19.
- **pwa.css:**
  - It is render-blocking in every `<head>`.
  - It is 0% used on the landings and 0 to 15% used elsewhere.
- **pwa.js:** lines 202-456 are hub-only (download, install coaching and the shelf, 10.2 KB) and ship on every page.
- **Landing pages:** they load 34 KB of book.css and use 6 to 8% of it.
- **Per-book copies:** book.css and book.js are copied into each book's `assets/`, making 4 cache entries. The 27,461-byte book.js is byte-identical in all four.

### Dead and duplicated rules

Found with `probe/cssparse.py` and `probe/unused.py`.

**Dead declarations in `book.css:115-133`:**

- 29 declarations in the phone block `@media (max-width:760px)` are dead.
- They are overridden by later rules of equal specificity: the unconditional rules at `:148-152`, `:316-324`, `:369-373` and `:555`, and the 1000 px restatement at `:632-635`.
- Only these survive: `:117` clip, `:119`, `:120` body 17 px, `:121` .main padding and `:128`.

**Duplicates:**

| what | where |
|---|---|
| `.katex-display` declared three times | `:127`, `:325`, `:630` |
| `html,body` overflow declared twice | `:116`, `:632` |
| the table scroller declared twice | `:129`, `:635` |
| `th` border-bottom, the first overridden | `:384` by `:386` |
| `.pwa-offline` `left`, `transform` and `font-size`, all dead | `pwa.css:13` against `:63` |
| `.eyebrow`, same name with two looks | `book.css:154` (accent, .13em) and `landing.css:64` (ink-faint, .22em) |
| `.hero`, declared in both files | `book.css:579` and `landing.css:42` |

**Rules that match no built page:**

- `.xref.pending` (`:241`)
- `.to-come` (`:249-250`)
- `.story .st-premise` (`:425`)
- `.story .sq-trials a.trial` (`:436-437`)
- `.tag.clear` (`:596`)
- `hr` (`:162`)

**Breakpoints in use:** 1000, 760, 720, 640, 560, 520 and 430 px.

**Touch-target rules** are spread over three files: `nav.css:177-190`, `book.css:261-264` and `:652-664`, and `pwa.css:292`.

### Dark-mode behaviour

Probes: `osdark.py`, `flash.py`, `forced.py`.

**OS dark with nothing stored:**

| page | theme |
|---|---|
| hub | dark |
| clinical landing | dark |
| contents | light, and `library:v1` becomes `{"theme":"light"}` |
| every later page | light |

- The cause is `book.js:7-9`, which defaults to `'light'`.
- It also causes a visible flip from dark to light:
  - BC-900: dark at 556 ms, light at 753 ms.
  - ch1-2: dark at 732 ms, light at **7,338 ms**.

**Browser chrome and native controls:**

- `theme-color` has a single light value on every book page (`tools/pwa.py:232`). Only the hub has the dark media pair (`:228-229`).
- `book.css` never declares `color-scheme`; the computed value is `normal` in dark. Native controls and scrollbars therefore keep their light style.

**Forced colours:** the drawer button's three-bar glyph (`book.css:499`, `background:currentColor`) disappears, leaving an empty circle (`forced.BC-900.390.png`).
