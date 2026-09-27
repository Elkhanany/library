# A Library: the design system

Revision 2. This revision answers two design reviews: one on reading quality, one on
buildability. What changed from revision 1 is listed in §12.

The aim is one series from one press, not four websites. Every book has the same trim,
type, furniture and way of moving through it. Each book is told apart by its cover: its
colours from `book.json` `theme`, its `field` on the hub, and the figure on its front door.
The two instruments also keep their masthead.

This file is the spec that the work packages implement. Where a package brief and this
file disagree, this file wins, and the brief needs correcting.

---

## 1. Principles

1. **The page is the book and the chrome is the binding.** Chrome gets out of the way while
   the reader reads down the page. It comes back when they deliberately scroll up, reach the
   end, or ask for it.
2. **One of everything.** One bar, one theme control, one name per destination, two label
   styles, one link style, one "has a card" mark, one focus ring, and one way to mark "you
   are here".
3. **Identity is carried by colour, figure and masthead, not layout.** All books share the
   same frame, type and navigation. `accent`, `accent_dark`, `ink`, `paper` and `field` are
   the only values that differ. The front doors keep their figures, and the instruments keep
   their masthead lockups on wide screens.
4. **Serif for what is read, sans for what is operated.** Titles, headings, prose, questions,
   chapter titles, trial names in prose, and the instruments' dossier text are set in the
   serif. Navigation, labels, table cells, captions, UI numbers and controls are set in the
   sans.
5. **No word falls below 4.5:1 contrast.** To de-emphasise, use size, weight or position,
   never paler ink or opacity. Hairline colours are never used for text.
6. **Nothing moves unless the reader moved it.** The theme is final at first paint. Bar items
   never shift between page types or when scripts arrive. `prefers-reduced-motion` is
   honoured everywhere, including scrolling.
7. **Every control works by thumb and by keyboard.** Targets are 44 px under
   `pointer:coarse`. Focus is visible, and DOM order matches visual order.
8. **Up, across and back are always one step away, on every device.**
   - Up: Library leaves the book. The sidebar breadcrumb, or the drawer's first row on a
     phone, leaves the chapter for its part in the contents.
   - Across: previous and next chapter, always labelled with the chapter number.
   - Back: the browser, or the installed app's back control.
9. **Facts are built, not typed.** Counts, labels, neighbours, start chapters and positions
   come from `book.json`, the curriculum and the data files, at build time where possible.
10. **Presentation only.** No chapter prose, trial fact, reference or registry data changes.
    Offline stays whole and the checks stay green. New UI copy uses no em dashes.
11. **Every stage degrades safely.** A reader's installed copy may run a new page on an old
    shell, or an old page on a new shell, and the Dropbox build has no shell at all. Each of
    them still has a working theme control and working chapter navigation.

---

## 2. Type

**Stacks.** Only system faces are used. No font is fetched, and none is vendored except
KaTeX's maths faces. The stacks are defined once in `nav.css`, which every docs page loads,
as `--lib-serif`, `--lib-sans` and `--lib-mono`. Every stylesheet reads them with a literal
fallback:

```
--lib-serif: "Iowan Old Style", Charter, "Bitstream Charter", "Palatino Linotype",
             "Sitka Text", Palatino, "Source Serif 4", "Noto Serif",
             Georgia, Cambria, serif;
--lib-sans:  system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, sans-serif;
--lib-mono:  ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
```

- Palatino Linotype sits ahead of Sitka Text, so Windows never sets Sitka's text optical
  size at display sizes. The Windows face is confirmed in the wave-1 review (§9).
- `book.css` uses `--serif: var(--lib-serif, <same literal stack>)`, and likewise for
  `--sans` and `--mono`.
- The atlas and the timeline map `--f-disp` to `--lib-serif`, `--f-ui` to `--lib-sans` and
  `--f-mono` to `--lib-mono`. The unshipped names "Spectral" and "IBM Plex" are deleted.

**Weights, stated as they render.** None of Iowan, Charter, Palatino or Georgia has a
semibold, so a declared 600 renders as bold on most platforms and as a true semibold only
where a variable Noto or Source Serif resolves. The system therefore declares only weights
that render the same everywhere:
- Serif: 400, 400 italic, and 700. `--fw-title: 400` for `--fs-display` and `--fs-title`;
  `--fw-head: 700` for h2 and h3. Both are tokens, so the wave-1 review can change them in
  one place.
- Sans: 400 for text, 600 for UI, links and emphasis, 700 for uppercase labels only.

**Scale.** All sizes are in rem, and the body size is in rem, so the reader's default font
size scales everything. The ratios hold at every width, not only at the sample widths.

| token | value | at 390 / 1280 | used for |
|---|---|---|---|
| `--fs-body` | 1.1875rem at ≥1000 px; 1.125rem at 640 to 999; 1.0625rem below 640 | 17 / 19 px | chapter prose |
| `--lh-body` | 1.66 at ≥640 px; 1.62 below | | |
| `--line` | `calc(var(--fs-body) * var(--lh-body))` | 27.5 / 31.5 px | the vertical unit (see Rhythm) |
| `--fs-display` | `clamp(2.6rem, 1.2rem + 5.4vw, 5rem)` | 41.6 / 80 px | front-door title only; serif 400, -0.02em, lh 1.02 |
| `--fs-title` | `clamp(1.75rem, 1.2rem + 2.2vw, 2.6rem)` | 28 / 41.6 px | every page h1; serif 400, -0.015em, lh 1.12; ≤28px at 390 |
| `--fs-sub` | `clamp(1.15rem, 1rem + .6vw, 1.4rem)` | 18.4 / 22.4 px | `.subtitle`; serif italic 400, `--ink-soft`; always larger than the body |
| `--fs-h2` | `clamp(1.35rem, 1.1rem + 1vw, 1.75rem)` | 21.6 / 28 px | serif 700, lh 1.22 |
| `--fs-h3` | `clamp(1.15rem, 1.06rem + .4vw, 1.3rem)` | 18.5 / 20.8 px | serif 700; ≥1.08 × body at every width |
| `--fs-h4` | .95rem | | sans 600, `--ink-soft` |
| `--fs-small` | .875rem | | captions, table cells, references, figcaptions |
| `--fs-ui` | .8125rem (13px) | | bar, sidebar, buttons, drawer; never smaller on phones |
| `--fs-label` | .7rem | | uppercase labels |

**Rhythm.** Space between blocks is set in multiples of `--line`, the body's line height,
so sections are marked by space in proportion to the text. The tokens are defined once in
`book.css` and applied by the component owners:

| token | value | applies to |
|---|---|---|
| `--sp-eq` | `.75 * --line` | display equations, lists |
| `--sp-block` | `1 * --line` | callouts, figures, stories, evidence tables |
| `--sp-h3` | `1.25 * --line` above, `.35` below | h3 |
| `--sp-h2` | `2 * --line` above, `.6` below | h2 (no rule; space alone marks the section) |
| `--sp-break` | `2 * --line` above and below | sitting breaks |

Paragraph spacing is unchanged. Small component spacing uses `--sp-1` to `--sp-8` (.25, .5,
.75, 1, 1.5, 2, 3 and 4.5rem).

**Line breaking and hyphenation.**
- `h1, h2, h3, .subtitle, .pause .t` get `text-wrap: balance`. `.col p` gets
  `text-wrap: pretty`.
- Below 640 px, `.col p` and `.col li` get `hyphens: auto; -webkit-hyphens: auto;
  hyphenate-limit-chars: 6 3 3`. Evidence-table prose cells (population, arms, endpoint,
  result, OS) get the same below 640 px.
- Never hyphenated: headings, eyebrows and labels, `.trial`, `.cite`, `code`, `.katex`,
  table heads, and the trial name cell. (`<html lang="en">` is already on every page.)

**Measure.** Measure is set in em, so it follows the text size:
- `--measure: 35em`: about 665 px at 19px, or 64 to 72 characters per line. This is the
  measure for all continuous prose, the Through-Line included.
- `--measure-wide: 48em`: only the contents page and the Math Ledger, whose lines are short
  rows and tables.
- Front matter: `--fm-wide: 62rem` for the page frame and 34rem for the landing lede. Reading
  bodies on appendix rows (registry topic, result and digest; story premise and moves) are
  capped at **36em of their own font size**, never in rem, so they stay at 64 to 72
  characters however small they are set.

**Two label styles, and no others.**
- **Kicker**: `font: 700 var(--fs-label)/1.3 var(--sans); letter-spacing: .12em;
  text-transform: uppercase; color: var(--accent)`. Eyebrows on every page type, callout
  type labels, the story where-line and the "continued" line.
- **Label**: the same, with `letter-spacing: .1em; color: var(--ink-faint)`. Used for `dt`,
  chapnav direction, the sidebar's position, stat captions, the sitting-break kicker, part
  numerals, the drawer kicker and tags.
- Uppercase is reserved for words of one or two short tokens. Multi-word column heads
  ("Experimental vs control", "Overall survival") are **not** labels: they are sans 600 at
  `--fs-small`, sentence case, `--ink-soft`, with no tracking.

---

## 3. Colour

A book sets four colours in `book.json` (`accent`, `accent_dark`, `ink`, `paper`).
`themecss()`, which moves into `library.py` so both builds use it, emits **only these**:
`--bg` (paper), `--ink` and `--accent` on `:root`, and `--accent` (accent_dark) under
`html[data-theme="dark"]`. It no longer emits static `--bg-alt` or `--accent-soft`: a later
`:root` rule would win in both themes and give the dark theme a light sidebar.

**Everything else is derived in `book.css` with `color-mix(in srgb, …)`**, so a book's tint
carries into its rules, washes and dark ground. The derivations sit inside
`@supports (color: color-mix(in srgb, red, blue))`, with today's static values as the
fallback (light `--ink-faint` fallback `#63636a`, dark `#84868c`).

### Light (on `:root`)

| role | derivation | measured floor, clinical / physics |
|---|---|---|
| `--bg` | `paper` | |
| `--bg-alt` (sidebar, drawer) | `color-mix(in srgb, var(--ink) 4.5%, var(--bg))` | |
| `--paper` (raised: figures, cards, sheets, tiles) | `color-mix(in srgb, #fff 65%, var(--bg))` | |
| `--ink` | `ink` | 16.1 / 16.5 |
| `--ink-soft` | `color-mix(in srgb, var(--ink) 76%, var(--bg))` | 7.05 / 7.00 on `--bg-alt` |
| `--ink-faint`, the palest ink a word may use | `color-mix(in srgb, var(--ink) 68%, var(--bg))` | 5.36 / 5.31 on `--bg-alt` |
| `--rule`, `--rule-soft` (hairlines only) | ink 13% and 7% into `--bg` | never text |
| `--accent` | `accent` | 6.14 / 7.24 on `--accent-soft` |
| `--accent-soft` (active rows, `:target`) | `color-mix(in srgb, var(--accent) 10%, var(--bg))` | |
| `--accent-line` (link underline) | `color-mix(in srgb, var(--accent) 45%, transparent)` | |

### Dark (`html[data-theme="dark"]`)

The dark block redeclares every role whose light formula would be wrong on a dark ground.

| role | derivation | measured floor, clinical / physics |
|---|---|---|
| `--bg` | `color-mix(in srgb, var(--accent) 5%, #15171b)` (accent is now accent_dark) | |
| `--paper` | `color-mix(in srgb, #fff 3%, var(--bg))`: a raised surface is a shade **lighter** than the ground, as today (#191c21 over #15171b) | |
| `--ink` | `#e2e1dc` | 12.9 / 12.7 |
| `--ink-soft` | `color-mix(in srgb, var(--ink) 74%, var(--bg))` | 7.01 / 6.93 on `--paper` |
| `--ink-faint` | `color-mix(in srgb, var(--ink) 60%, var(--bg))` | 4.91 / 4.86 on `--bg-alt`; 5.04 / 4.99 on `--paper` |
| `--accent` | `accent_dark` | 4.97 / 6.13 on `--accent-soft` |

`--bg-alt`, `--rule`, `--rule-soft`, `--accent-soft` and `--accent-line` keep their light
formulas, which are correct on a dark ground because they mix the (now light) ink or accent
into the (now dark) ground.

**Print** ignores the dark theme: `@media print` restates the light roles under
`html[data-theme="dark"]`.

**The two instruments** do not load `book.css`, and after wave 1 neither has a `book.css`
page. Their book.json palettes are therefore not held to the derived floors (with the
derivations the atlas's light `--ink-faint` would reach only 4.36:1 on `--bg-alt`). If
either book ever gains a chapter page, its `book.json` must first carry an `ink_faint`
override of 72%.

**`book.json` corrections.**
- The Long Argument: `accent_dark` becomes `#e4635f`, the timeline's own dark rubric.
- The Ages of Thought: `accent` `#93412a` (the page's accent-deep), `accent_dark` `#d97f5c`,
  `paper` `#e6dbc3`, `ink` `#2b2115`.

**Semantic hues.** The meanings already agree across books, so they are kept:

| hue | role | light / dark |
|---|---|---|
| `--insight` | a takeaway to act on ("Insight", "In practice") | `#15654a` / `#6dc9a5` |
| `--familiar` | a connection elsewhere ("Familiar ground", "Interplay") | `#5c3d86` / `#b79ce0` |
| `--warn` | caution | `#9a4a12` / `#e0a06a` |
| `--plain` | plain-language restatement | `#9c4257` / `#e3a0ac` |
| `--grind` | aside | `#5a5a64` / `#9a9ca4` |

Every wash is `color-mix(in srgb, var(--hue) 8%, var(--bg))`. Every filled component sets
`--surface` to its own ground (a wash, `--paper` or `--bg-alt`), so scroll-edge cues inside
it are painted in the right colour.

**Other colour rules.**
- `color-scheme: light` on `:root` and `dark` on `[data-theme=dark]`.
- `<meta name="theme-color">` follows the active `--bg`.
- Text on an accent fill uses `var(--bg)`, never `#fff`.
- **Reading a colour in script.** `getPropertyValue('--x')` returns the unresolved
  `color-mix(…)` text, and computed colours serialise as `color(srgb …)`. Script that needs a
  colour (theme-color, canvas figures, the landing figures) resolves it by painting
  `var(--x)` into a 1×1 canvas and reading the pixel back as `#rrggbb`. `book.js` exposes
  this as `NMT.color(name)`, and `pwa.js` has its own copy.

**Pages that don't load `book.css`.**
- **The hub** defines the same role names on its `:root` in both themes (`--bg`, `--paper`,
  `--ink`, `--ink-soft`, `--ink-faint` at ≥4.5:1, `--rule`), keyed on `data-theme` with the
  media query only as a fallback. Each tile carries `--bk-accent` and `--bk-accent-2`, and the
  dark theme uses the second.
- **The atlas and the timeline** keep their own palettes and obey the same floor: `--ink-3` is
  the palest word colour and `--ink-4` is for hairlines only. They expose `--accent-ink`, a
  text-safe accent that the bar reads first.

---

## 4. Theme: one model, one control

- **Resolution** happens once, in the `<head>` boot script (`pwa.py` BOOT), before first
  paint. It checks, in order:
  1. `library:v1.look`, written only by a press of the toggle;
  2. legacy `nmt-theme`, which was also only ever written by a press;
  3. `prefers-color-scheme`.

  `library:v1.theme` is never read again. It was written passively and pinned OS-dark
  readers to light. BOOT also adds `js` to `<html>`.
- **The control** is `button.nav-theme`, the last item in the library bar on every barred
  page, the hub included.
  - One glyph everywhere: an inline SVG circle half-filled with `currentColor`.
  - `aria-pressed` (true when dark), `aria-label="Dark theme"`, and a `title` of "Switch to
    dark" or "Switch to light".
  - 36 px square on desktop, 44 px under `pointer:coarse`.
  - `nav.py` emits it with the `hidden` attribute. `pwa.js` removes `hidden` when it wires the
    button, and sets `html.theme-wired`. Under `html.js`, `nav.css` reserves the button's slot
    (`visibility: hidden`) while it is still hidden, so nothing shifts when it appears. A
    page whose shell predates it (old `nav.css`) never shows a dead button, because the UA
    hides `[hidden]`.
- **On a press**, `pwa.js` flips `data-theme`, saves `look`, updates `aria-pressed`, `title`
  and theme-color, and dispatches `window` `library:theme` `{detail:{theme}}`. `book.js`
  calls `NMT.redrawAll()` on that event and on any `data-theme` mutation. The atlas and
  timeline observe `data-theme`.
- **No other theme control exists** on a page whose shell is current: no floating pill, no
  drawer button, no app-header moon.
- **The fallback.** `book.js` creates the floating `#themer`, which writes `nmt-theme`,
  when `html.theme-wired` is still absent at window `load`. That covers the Dropbox build
  (`file://`, no `pwa.js`) and an installed reader whose shell is older than the page. When
  `<html>` has no `data-theme` (no BOOT), `book.js` resolves `nmt-theme`, then the OS
  setting, and stamps it. It no longer forces "light".
- **`continue.html` and `offline.html`** run the same three-step resolution inline and style
  both `[data-theme]` values.

---

## 5. Layout per page type

| breakpoint | job |
|---|---|
| **1500** | the chapter's column and margin block centres in the space right of the sidebar |
| **1200** | a margin track appears on chapters; evidence tables bleed |
| **1000** | sidebar ↔ phone chrome (folio bar, drawer, headroom) |
| **640** | phone: type steps down, and the bar's destinations fold under Menu |
| **430** | narrowest tightening |

`landing.css`'s 720 becomes 640 where it is the phone switch.

**One inset.** `nav.css` defines `--lib-inset`: 1.25rem at ≥640 px, 1rem below. The bar's
`padding-inline`, the sidebar's `padding-inline`, and the inner gutter of every centred frame
(hub, landing, appendix) read it. **The bar is full-bleed on every page and never reads a
frame width.** The brand therefore sits at the same x on every page of the library, and on
chapter pages it lines up with the sidebar's text.

**Bar height.** `--lib-bar-h` is 2.75rem (44 px) at every width, plus
`env(safe-area-inset-top)` in the installed app. `nav.css` owns `--lib-bar-h`, the bar, and
the sidebar's `top` and `height`. The Dropbox build, which has no bar, sets
`--lib-bar-h: 0px` after the inlined `nav.css`.

**Overflow.** `html, body { overflow-x: clip }`, with `hidden` only under
`@supports not (overflow: clip)`, so the bar is sticky at every width. Because clip hides
real overflow, navcheck's masked sweep (§9) is the overflow test from wave 0 onward.

**Scroll padding** is `calc(var(--lib-bar-h) + .75rem)`. **Smooth scrolling** happens only
under `prefers-reduced-motion: no-preference`.

**z-index scale** (in `nav.css`, `--lib-z-*`): bar 40, folio 40, bar menu panel 45, scrim 50,
sheet (drawer, reference sheet) 60, hover card 70, toast 80. The toast sits above the folio
bar when there is one (`bottom: calc(3rem + env(safe-area-inset-bottom) + 1rem)`).

```
HUB  (content frame 64rem, centred; the bar is full-bleed)
┌ bar: A Library ······································· [◐] ┐
│ eyebrow (label) / h1 serif / lede                               │
│ CONTINUE READING  (only when there is something to continue)    │
│  ▌Breast Cancer   68 · Deciding whether to treat…   ▁▁▁▁ 40%    │
│ ┌ tile ─────────────┐ ┌ tile ─────────────┐  2 columns ≥640    │
│ │▬ kicker           │ │▬                  │                     │
│ │Title (serif)      │ │                   │                     │
│ │tagline            │ │                   │                     │
│ │98 chapters  Read→ │ │                   │                     │
│ │[Download · 2 MB]  │ │                   │                     │
│ └───────────────────┘ └───────────────────┘                     │
│ Using 42 MB on this device · Reset offline data (quiet)         │
└─────────────────────────────────────────────────────────────────┘

FRONT DOOR  (landing.css; content frame --fm-wide 62rem)
  kicker eyebrow · display title · lede (34rem) · thesis (rule-led italic)
  stats: chapters (written of planned) and parts only, hairline cells capped at the text measure
  CTA: [primary] then text links →
    sequential book (physics): [Begin / 0.1 · What a Derivative Really Is]; returning:
      [Continue reading / 1.1 · …]
    reference book (clinical): [Contents]; returning: first .go "Continue at 68 · …"
  figure: behind the hero, masked from the text column's right edge (≥720 px);
          its own band with its caption under it at ≤640 px
  sections: "Ways in" / "The parts" (arc rows) / "How it is built"

APPENDIX  (stories, trials: the same front-matter header, frame 62rem)
  kicker "Appendix A" (trials) or "Stories" · title (serif, --fs-title) · lede · stats cells
  sticky filter bar at top: var(--lib-bar-h) (at ≤640 px: one "Filters (n)" row that expands)
  rows: bodies at 1rem, capped at 36em

CONTENTS  (chapter shell: sidebar + wide column 48em)
  sidebar: ← <Book title> · PARTS · part list          │ kicker <Book title>
                                                        │ h1 Contents
                                                        │ "98 chapters in 17 parts" (label line)
                                                        │ [Find a chapter ____________]
                                                        │ PART IX (label) · 3 of 9 written
                                                        │ serif part title / italic sub
                                                        │ 59  Adjuvant chemotherapy …   (serif ink rows)
                                                        │ 1.4 Planned title  (ink-soft italic, no link)

CHAPTER ≥1200:
┌ bar (full bleed; brand at --lib-inset = the sidebar's text inset) ────────────────┐
│ sidebar 16rem, flush left, │   text column 35em        │ margin track ≤18rem      │
│ bg to the viewport edge    │   (eyebrow, h1, subtitle, │ (--breakout: equation    │
│ ← Part XII · HER2-…        │    prose…)                │  numbers hang here;      │
│ ‹ 72  CHAPTER 73 OF 98  74 ›│                          │  wide figures extend)    │
│ 1 · Scope …  (spy)         │ ┌ evidence table bleeds to .main's right edge ────┐ │
│ 2 · …                      │ └──────────────────────────────────────────────────┘ │
│                            │  [chapter foot: two cards]│                          │
└──────────────────────────────────────────────────────────────────────────────────┘
  At ≥1500 px the column and margin block is centred in the space right of the sidebar,
  and an evidence table spans the whole of .main (minus --lib-inset), symmetric about
  the column.
  From 1000 to 1200 px: sidebar and column; no margin track; tables scroll with a cue.

CHAPTER <1000 (phone and tablet):
  bar (sticky; hides on reading down, returns on a deliberate scroll up)
  text column, full width minus --gutter, 17 or 18px body
  folio bar (fixed bottom, hides with the bar): [‹ 72]  3 · Second-line conjugate… ▴  [74 ›]
  drawer = bottom sheet: ← Part XII · … / kicker · title · [Close] / prev·next cards / sections

APP BOOKS  (atlas, timeline: full window)
  bar / one app header row: at ≥1000 px the masthead lockup (serif, unlinked) then controls,
  tabs and search; below 1000 px no masthead (the bar names the book) / the instrument
```

**Chapter geometry, in detail.**
- The sidebar is flush to the viewport's left edge, 16rem wide, `--bg-alt` from x = 0,
  sticky under the bar, scrolling on its own.
- `.col` is `max-width: var(--measure)`.
- `--breakout` (the margin track) is a registered `@property` length on `.main`: 0 below
  1200 px, and from 1200 px the free space right of the column, capped at 18rem. It is
  consumed by hanging equation numbers and wide figures.
- **Evidence tables are not capped by the margin track.** At ≥1200 px `.main` is an
  inline-size container (`container-type: inline-size`), and `.col > .evidence` sets its
  margins from `100cqi` (the width of `.main`'s content box) against `100%` (the column):
  - 1200 to 1499 px: the column sits at the left of `.main`; the table runs from the
    column's left edge to `.main`'s right content edge (`margin-inline-end:
    calc(100% - 100cqi)`).
  - ≥1500 px: the column is offset to centre the column-and-margin block; the table spans
    the whole content box, bleeding left as well as right.
  - Without container-unit support the margins resolve to 0 and the table scrolls inside the
    column, as it does below 1200 px.

---

## 6. Components

### The library bar (`nav.py` emits; `nav.css` styles; `pwa.js` gives it behaviour)

```
<a class="skip" href="#text">Skip to text</a>
<nav class="topnav" aria-label="Library" data-book="<slug>">
  <a class="nav-brand [two]" href="index.html" [aria-current]>Full name<span class="nav-short">Short</span></a>
  <button class="nav-menu" type="button" aria-expanded="false" aria-controls="nav-dest" hidden>Menu</button>   (only if the book has destinations)
  <div class="topnav-links" id="nav-dest"> <a …>Contents</a> <a …>Stories</a> <a …>Trial Registry</a> </div>
  <a class="up" href="../index.html">Library</a>
  <button class="nav-theme" type="button" aria-pressed="false" aria-label="Dark theme" hidden><svg…/></button>
</nav>
```

- **Height and row.** Exactly `--lib-bar-h`, one row (`nowrap`), text `--fs-ui` at every width,
  links sans 600 in `--ink-soft`. The current page carries `aria-current` and is shown in
  `--ink`. Inset `--lib-inset` on both sides.
- **Divider.** Only `.topnav-links + .up` draws the hairline divider.
- **At 640 px and below**, under `html.js`:
  - `.topnav-links` is a panel under the bar: full width, `--bg`, a hairline below, rows at
    least 48 px, 15px text, and a 3 px accent rule on the current row.
  - `.nav-menu` (its slot reserved while `hidden`) toggles the panel and `aria-expanded`.
    Escape closes it and returns focus to the button, as do an outside tap and choosing a
    link.
  - Without JS the links stay inline and may wrap.
- **The hub** gets the same bar: the brand "A Library" (current) and the theme button only.
- **Accent** reads `var(--accent-ink, var(--accent, var(--rubric, …)))`.
- **Installed app.** The bar is `--lib-bar-h` plus `env(safe-area-inset-top)` (never 0).
  Under `html.standalone`, `.topnav:not(:has(.pwa-back))::before` reserves a 2.25rem slot
  before the brand. When `pwa.js` inserts `button.pwa-back` the pseudo-element disappears,
  so the brand never moves.
- **Skip link.** Visually hidden until focused; the target is `#text`: `<main id="text">` on
  chapter-shell pages, landings and appendices, and `pwa.js` sets `id="text"` on the first
  `main, .main, .app, .hero` of any page that has none.
- **Print** hides the bar, the skip link and the menu panel.

### Headroom (chapter shell below 1000 px)

`html.chrome-hidden` translates the bar and the folio bar out of view (transforms only;
instant under reduced motion).
- It hides after the reader scrolls down more than 8 px, once past 120 px.
- It returns after **at least 48 px of cumulative upward scroll**, or on an upward flick
  (velocity), and the count resets on any downward movement. A nudge up to re-read a line
  does not bring back 130 px of chrome.
- It always shows within the last 1.5 viewports of the page, while focus is inside the bar
  or folio, and while the drawer or the bar menu is open.

### Sidebar (chapter shell, ≥1000 px)

Emitted by the build, so the Dropbox build has it too.
- **Up-link** (`.sb-home`): sans `--fs-ui`, `--ink-soft`, not uppercase, at most two lines.
  - Chapter: "← Part XII · HER2-positive disease" → `contents.html#sec-<part index>` on the
    site, `index.html#sec-<part index>` in the Dropbox build.
  - Contents, ledger or through-line: "← <Book title>" → `index.html`.
- **Folio row** (`.sb-folio`): `a.sb-prev` "‹ 72", then `p.sb-title` in the label style,
  then `a.sb-next` "74 ›". Missing neighbours keep their slot.
  - `.sb-title` is written at build time: "Chapter 73 of 98" when every chapter is written
    and the number equals the ordinal; "Chapter 1.1 · 3 of 37 written" otherwise; "Parts",
    "Math Ledger" or "In Plain Terms" on the other pages. `pwa.js` no longer appends a
    position.
  - Link titles name the chapter and the key: "Next chapter: 74 · Metastatic triple-positive
    disease (→)".
- **Section list** (`#sb-toc`): h2 entries, h3 entries indented in `--ink-faint`.
  - The active entry has a 2 px accent rule and is set in accent at 600.
  - It is the last heading whose top is above the bar's visible bottom edge + 24 px,
    computed on scroll (rAF-throttled), on load, on `hashchange`, and after a restored
    position. Nothing is active only above the first heading.
  - The sidebar keeps the active entry in view (`nearest`) without scrolling the page.

### Folio bar and drawer (below 1000 px, chapter shell)

- **Folio bar** (`.folio`): fixed at the bottom, `3rem + env(safe-area-inset-bottom)`, on
  `--bg` at 94% with a blur and a hairline top.
  - Left: `‹ 72`. Right: `74 ›`. The **chapter numbers** say these are chapters, not
    sections. 44 px links built from the page's `.chapnav a.prev` and `a.next`, with
    `aria-label` "Previous chapter: 72 · When the target changes…". A missing neighbour
    keeps its slot, disabled, so the centre never moves.
  - Centre: `#mnav-btn` (styled as `.folio #mnav-btn`), the current section from the spy,
    ellipsised, with a ▴ caret: "Sections" above the first heading, "Parts" on contents.
  - In the DOM it follows the bar (or starts `<body>` where there is no bar). `.main` bottom
    padding clears it.
  - The legacy `body > #mnav-btn` floating button rule stays in `nav.css`, so an older
    stored page keeps its drawer button under the new shell.
- **Drawer (`#mnav`)**: a bottom sheet in the reference sheet's idiom: 14px top corners, a
  handle, the scrim, a maximum height of 80dvh, every row inset 1.15rem on both sides.
  1. `a.mn-up`, a copy of `.sb-home` ("← Part XII · HER2-positive disease"), at least
     48 px tall. This is the phone's route up.
  2. The head: the position kicker (the `.sb-title` text) and the chapter title, with a
     visible Close button.
  3. `.mn-seq`: previous and next cards with chapter titles.
  4. `.mn-list`: the sections.
  - No destinations (the bar's menu has them) and no theme button.
  - Glyphs are inline SVG drawn in `currentColor`. Escape and Close return focus to
    `#mnav-btn`.
  - **Handles are real.** Dragging the sheet head down more than 64 px closes the drawer and
    the reference sheet alike.

### Chapter head and prose

- Eyebrow: kicker. `h1` at `--fs-title`, weight 400. Subtitle at `--fs-sub`.
- `h2`: `--sp-h2` above, no rule. `h3`: `--sp-h3`.
- **Prose links**: `.col :is(p, li, dd, td, figcaption) a:not(.cite, .eqref, .chip)` and
  `.xref`: `text-decoration: underline 1px var(--accent-line); text-underline-offset: .18em`,
  in accent, fully accent on hover. Contents rows, chapter-foot cards and heading links are
  excluded.

### Cards (one mark, one behaviour)

A dotted 1px `--ink-faint` underline means "this has a card". Hover or focus shows the
card; a tap shows the bottom sheet; Escape closes either. The card shows at most the facts
and one link.
- **Citation** (`.cite`): `sup { line-height: 0 }`; `.cite` is sans .75em 600 in accent,
  with no padding; under touch its hit area is an `::after` inset −.6em −.5em. It opens the
  reference (unchanged).
- **Trial mark** (`.col .trial[data-trial]`): **serif, at text size, in `--ink`**, with the
  dotted underline; never bold, never sans in prose (sans only inside table cells and
  chips). The card: the acronym, the facts (from the `title` attribute, which `book.js` moves
  to `data-facts` on first run, idempotently, so the browser's tooltip does not double the
  card), and "Full record in the Trial Registry →" to `trials.html#t-<key>` (omitted under
  `file:`). The first mark of each key in each h2 section gets `tabindex="0"` and
  `role="button"`; repeats in the same section are pointer-only, so a chapter with 134
  marks does not add 134 tab stops.
- **Glossary term** (`.col .gloss`): the same mark, a card with the definition.
- **Equation reference** (`a.eqref`, physics): hover or focus shows a card holding a clone
  of the target `.eq` display and its number, plus "Go to equation"; a tap shows the sheet.
  The link itself still jumps. Offline, presentation only.

### Evidence tables (clinical)

- **Title and note above the table.** `bc.py` splits the authored caption: the first
  sentence becomes `p.ev-title` (sans 600, `--fs-small`, `--ink`), the rest `p.ev-note`
  (sans, `--fs-small`, `--ink-soft`). `bc.py --check` verifies that each split lands on a
  sentence end.
- **Identity folded into the first cell.** Ph, N and Status are metadata that identify a
  row rather than compare it. `bc.py` moves them into a meta line inside the pinned trial
  cell (`span.m[data-col=ph|n|status]`, sans `--fs-small`, label colour, joined by " · "),
  and moves the Ref citation beside the trial name. The cell texts are unchanged; the words
  "Phase " and "n = " are CSS `::before` content. A 10-column table becomes 6 columns.
- **Heads.** Sans 600 `--fs-small`, sentence case, `--ink-soft`, no tracking, bottom-aligned.
- **Cells.** Sans `--fs-small`, lh 1.45, tabular numerals. Column classes from the header
  key: `c-trial`, `c-pop` (min 17rem; 13rem below 640), `c-arms`, `c-result`, `c-os` (min
  12rem; 10rem below 640), `c-endpoint`, `c-other`.
- **Every cell names its column on a phone.** `bc.py` emits `data-label` on every `td`.
  Below 640 px, `td:not(:first-child)::before { content: attr(data-label) }` sets a label
  line in each cell, so an endpoint can never be read as a result once the head has
  scrolled away. The trial name may break at its hyphen below 640 px.
- **Width.** `width: auto; min-width: 100%`; first column pinned; the bleed as in §5.
- **Scroll cues.** Edge shadows painted in `var(--surface)`, plus a "→ more columns" cue
  while `scrollWidth > clientWidth` and not at the right end. No vertical cap, no nested
  vertical scrolling.

### Stories (clinical)

Set in em of the body, so the block the authors call "the spine of the section" is never
smaller than a callout: `.col .story { font-size: .95em }`, `.st-title` 1.2em serif 700,
`.sq-ask` 1.05em serif 700, moves `dd` at 1em in `--ink`, `dt` as a label. Title outranks
question, question outranks moves, and none is smaller than callout text. The
where-line is a kicker. A story's second and later appearances in one chapter get only a
compact "<title>, continued" kicker. The wrapper id is `story-<first question id>`, so no id
repeats and `#SQ-…` still lands on the question. Trial chips are
`span.trial.chip[data-trial]`, which `book.js` upgrades to links to `trials.html#t-<key>`
except under `file:`.

### References

- `h2#references` stays (it is in the TOC), followed by
  `<details class="refs-list"><summary>All 58 references</summary><ol class="refs">…`.
- `book.js` opens the list for `#references` and `#r-…` hashes (on load and on
  `hashchange`), before a mouse-click citation jump, and on `beforeprint` (restoring the
  state on `afterprint`). The card and sheet read entries from the collapsed list.

### Callouts, preambles and sitting breaks

- **Callout family**: a 3 px left rule in the hue, the wash, radius 6px, 1rem 1.15rem of
  padding, the type label as a kicker in the hue, `--sp-block` around it.
- **"Where we are"** (physics) is set as prose: the kicker only, no fill, no rule.
- **"Tools you'll need"**: serif at `--fs-small` (it carries inline maths), a label-style
  kicker, a hairline top border, no fill.
- **"In plain terms"** keeps its tinted panel. On the Through-Line page, `.bridge` is set in
  roman with its plain-hue rule; italic is kept only for the thesis sentence.
- **Sitting break** (`.pause`): rule, kicker (`.k`), rule on one row; beneath it the line
  (`.t`) as wrapping serif italic at .95em in `--ink-soft`, centred, at most 32em, balanced,
  with its first letter capitalised by CSS. `book.js` splits the authored text on the first
  `/\s*·\s*/` (JavaScript's `\s` includes the U+00A0 in the authored `&nbsp;·&nbsp;`),
  idempotently. `nowrap` is never used. `--sp-break` above and below.

### Equations and figures (physics)

- **Inline maths** keeps `.katex { font-size: 1.045em }` at every width. It is never shrunk
  on phones.
- **Display maths** that overflows its box by 12% or less is fitted: `book.js` sets a
  font-size down to a floor of .9em. Beyond that it keeps its size and scrolls inside its
  box with edge cues in `var(--surface)`. The fit is recomputed on load and on resize, so a
  value captured at build time is harmless.
- **Equation numbers** stay on the equation's line when both fit, and drop below it,
  right-aligned, only when they don't. The display stays centred on the column. At ≥1200 px
  the number hangs in the margin track, so displays get the full measure, and no display in
  the book overflows at 1280.
- **Figures**: a `--paper` panel, a hairline, radius 6px, `--surface: var(--paper)`.
  Controls are 44 px under touch, and the active state uses `var(--bg)` text on the accent.

### Chapter foot

- `nav.chapnav[aria-label="Previous and next chapter"]` holds `a.prev` and `a.next` cards,
  or a `.dead` span.
- Each card: the direction as a label; the number and title in the serif; the part name
  when it differs from this chapter's. At least 56 px tall, hairline, radius 6px, accent
  border on hover or focus.

### Contents

- **Head** (`.toc-head`): kicker (the book title), h1 "Contents", one count line in the label
  style ("98 chapters in 17 parts" or "37 of 76 chapters written, in 8 parts"). For an
  incomplete book, one legend line: "Titles in italic are planned."
- **Find a chapter.** `book.js` inserts one `input[type=search]` ("Find a chapter") after
  the count line. It filters `.clist li` by number and title as the reader types, hides
  parts with no match, says "No chapter matches" when nothing does, and clears on Escape.
  Built from the page itself, so it works offline and in the Dropbox build.
- **Parts**: `h2.part-head` with `id="sec-<i>"` **emitted by `build.py`**, the only h2s on the
  page. A label numeral ("Part IX", plus "3 of 9 written" when the part is incomplete), the
  serif title, and `p.part-sub` in italic `--ink-soft`.
- **Rows**: number in tabular sans in the label colour; title in the serif at 400 in `--ink`,
  accent on hover or focus; "Math" as a label word. Planned rows: the title in `--ink-soft`
  italic, no link, **no per-row label**. At least 44 px under touch, with the anchor as the
  target. No READY tags.
- **Last read** (`li[data-last]`): a 3 px accent rule and `span.tag.last` "Last read", with a
  "Jump to where you were" link above the first part. Filled by `pwa.js`.

### Front matter (`landing.css`: landings, stories, trials)

- **Header**: eyebrow as a kicker; title at `--fs-display` (landing) or `--fs-title`
  (appendix), weight 400; lede; thesis as a 2 px accent rule with serif italic; stats as
  hairline cells with serif tabular numerals over a label caption, capped at the text
  measure.
- **Stats say what helps a reader decide.** Front doors: chapters (written of planned) and
  parts only; words and equation counts go. The registry: trials, publications and "with a
  tabulated result"; the QA counters ("still to be tabulated", "not yet cited in the text")
  appear only when non-zero.
- **CTA**: exactly one `.cta > .btn` (accent fill, `var(--bg)` text, radius 6px, ≥44 px),
  then `.go` text links with arrows. `a.col-item` gets an arrow; `div.col-item` stays.
  - The primary has two lines when it names a chapter: `span.btn-main` ("Begin" or
    "Continue reading") in button weight, and `span.btn-sub` ("0.1 · What a Derivative
    Really Is") in regular weight. The full text is its `aria-label`.
  - Start labels come from the build (`{{START_HREF}}`, `{{START_NUM}}`, `{{START_TITLE}}`).
- **What the primary is** depends on `book.json` `"reading"`:
  - `"sequential"` (physics): the primary is "Begin" at the first written chapter; for a
    returning reader `pwa.js` rewrites it to "Continue reading" at their place and keeps
    "Begin" as the first `.go`.
  - `"reference"` (clinical): the primary is always Contents. For a returning reader
    `pwa.js` inserts "Continue at 68 · Deciding whether…" as the first `.go`.
- **Appendix rows**: name sans 600 `--ink`; meta sans 400 in the label colour; topic, result
  and digest serif 400 at 1rem, capped at 36em. Page-specific class names (`.reg-row`,
  `.st-row`) never shared with chapter components. Inputs, selects and segments ≥44 px under
  touch; the segmented control's on-state text is `var(--bg)`.

### Hub

- **Lede**: eyebrow as a label, serif h1, lede.
- **Continue strip** (`section.continue[data-continue] hidden`), filled by `pwa.js`: one row
  per opened book, most recent first: the book name in its dark-safe accent, "68 · Deciding
  whether…", and a thin progress rule.
- **Tiles** (`article.book`): hairline border, radius 6px, translucent `--paper`; no lift,
  shadow, blur or min-height. The title link is stretched over the tile. A 2.4rem × 3px
  accent rule, a kicker, the serif title and the tagline; a foot with the status in the
  book's own unit, computed at build ("98 chapters", "37 of 76 chapters written", "133
  thinkers across ten ages" from `book.json` `"shelf"`), "Read →", and
  `button[data-offline]` above the stretched link. Keyboard focus drives the weather through
  `focusin`/`focusout`, and the tile shows `:focus-within` with the tile-accent ring.
- **Weather**: unchanged.
- **Below the grid**: one quiet line for storage use and "Reset offline data" (44 px under
  touch).

### Buttons, chips, tags and focus

- `.btn` primary, at most one per page. `.go` text action (sans 600 `--ink-soft`, "→",
  accent on hover). Icon button 36 px (44 px under touch). `.chip` is a link or a button,
  never decoration. Tags use the label style; only `.tag.last` is filled.
- **Focus**: `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }`
  everywhere, hub tiles included. The atlas and the timeline keep their own `--focus` ring.

### Print

Print is a first-class reader: a chapter printed for a tumour board keeps its evidence.
- Hidden: the bar, skip link, menu panel, folio bar, drawer, sidebar, cues, the refs
  `summary`, and headroom transforms.
- References print open (`beforeprint`). Evidence tables print whole: `overflow: visible`,
  no bleed, `min-width: 0` on every cell, `white-space: normal`, 8pt type. KaTeX displays
  are not clipped. The light theme is always used.

---

## 7. Navigation model

| move | desktop | phone | keyboard |
|---|---|---|---|
| **Between books** | bar "Library" → hub; tiles; Continue strip | same | skip link → text; Tab through the bar |
| **Into a book** | tile → front door → primary | same | |
| **Within a book** | bar destinations; landing `.go` links; contents rows and "Find a chapter"; arc rows → contents#sec-N | bar "Menu" at ≤640 px | |
| **Up from a chapter** | sidebar "← Part …" → contents#sec-N; bar brand → front door | drawer's first row "← Part …"; bar brand | |
| **Across chapters** | sidebar ‹ 72 · 74 ›; chapter-foot cards | folio ‹ 72 · 74 ›; drawer cards; foot cards | ← → (named in the link titles) |
| **Within a chapter** | sidebar TOC with accurate spy; equation cards | folio centre shows the section; drawer lists sections | |
| **Back** | browser | browser; installed app: `.pwa-back` in the bar | |
| **Resume** | hub Continue strip; front door (primary for a sequential book, first `.go` for a reference book); contents "Last read"; `continue.html?b=` | same | |

**One name per destination**, used verbatim in the bar, landing links, sidebar heads,
`<title>` and shortcuts:

- Contents
- In Plain Terms (eyebrow "In Plain Terms"; h1 stays "The Through-Line")
- Math Ledger (eyebrow is the book title, as on Contents, so the eyebrow does not repeat the
  h1 "The Math Ledger")
- Stories
- Trial Registry (eyebrow "Appendix A"; h1 "The trial registry")
- Library

**Dead ends removed.** A book with no written chapter offers no Contents and builds no
contents page. The Long Argument and The Ages of Thought show only brand, Library and theme.

---

## 8. Contracts between packages

Change one only together with its consumers.

- **Text-pass anchors.** `<body>` stays bare (`nav.py` anchors on it); the viewport meta
  string stays as it is (`pwa.py` anchors on it).
- **`book.js` boot shape.** Both builds ship `book.js` through `runtime_js()`, which replaces
  `numberEquations();` and deletes everything from `if (window.katex) { typeset(); }` to the
  handler's closing `\n  });`. So:
  - the `DOMContentLoaded` boot handler keeps `numberEquations();` as its first statement
    and ends with the katex `if/else` block;
  - new boot calls go **after** `numberEquations();` and **before** `if (window.katex)`;
  - anything that needs rendered KaTeX or layout (display fitting, spy, folio, headroom)
    registers its own `load`/`resize`/`scroll` listeners outside the boot handler.
  Both `runtime_js()` copies raise unless each substitution happens exactly once (wave 0).
- **Build-time capture.** The build runs `book.js` on the staged page (file://, 1280×1000)
  and then saves `.main .col` and `#sb-toc`. Every insertion `book.js` makes inside them is
  idempotent (it checks before inserting: cues, `.k`/`.t` spans, chip upgrades, the find
  box, `data-facts`), or lives outside them (folio, drawer, cards). No `active` or state class
  is left on a saved node.
- **The bar.** Structure as in §6. `.topnav[data-book]` is the slug, and `pwa.js` prefers it
  to the path, setting `ROOT='../'` whenever it is present. `button.nav-theme` and
  `button.nav-menu` ship `hidden` and are wired (and un-hidden) by `pwa.js`, which sets
  `html.theme-wired`.
- **Custom properties.** Every custom property `nav.css` defines is prefixed `--lib-`:
  `--lib-serif`, `--lib-sans`, `--lib-mono`, `--lib-bar-h`, `--lib-inset`, `--lib-z-*`.
  The timeline already uses `--bar-h` and `--focus`, and `nav.css` loads last on it. There is
  no `--lib-frame`: nothing aligns the bar to a frame.
- **Geometry.** `--breakout` (registered length, 0 below 1200 px, ≤18rem) is set on `.main`
  by the frame. At ≥1200 px `.main` is an inline-size container; `.evidence` computes its
  bleed from `100cqi`.
- **`nav.json`** gains `"reading"` (wave 3). Positions are no longer computed in the browser,
  so it does not need `"planned"`.
- **Sidebar and chapter foot.** `.sb-home` is the up-link; `.sb-folio` holds `a.sb-prev`,
  `p.sb-title`, `a.sb-next`, written at build. `.chapnav a.prev`/`a.next` carry the
  neighbours' hrefs and text; the folio bar and drawer read them.
- **Contents.** Part heads are `h2.part-head#sec-<i>`, emitted by `build.py`, the only h2s.
  Rows are `.clist li`; the last-read hook is `li[data-last]` with `span.tag.last`. The head is
  `.toc-head`.
- **Drawer.** navcheck relies on `#mnav`, `#mnav-btn`, `.mn-up`, `.mn-kicker`, `.mn-title`,
  `.mn-list`, `.mn-seq .prev/.next .mn-ch` and `.mn-seq > span` for a missing neighbour.
- **Front door.** The primary is `.cta > .btn`, with `.btn-main` and `.btn-sub`. The start
  placeholders `{{START_HREF}}`, `{{START_NUM}}`, `{{START_TITLE}}` come from `page_stats`
  (wave 2). `pwa.js` reads `nav.json` `"reading"` to decide between rewriting the primary and
  inserting a `.go`.
- **Theme.** Event `window` `library:theme` `{detail:{theme}}`. Stored keys:
  `library:v1.look` and `library:v1.lastBy[slug] = {url, num, title, pct, at}`.
- **Clinical markup (bc.py).** `span.trial[data-trial="<key>"]`; chips
  `span.trial.chip[data-trial]`; `p.ev-title`, `p.ev-note`; `td[data-label]`;
  `span.m[data-col]`; story wrappers `story-<id>`; `details.refs-list`. Registry rows keep
  `id="t-<key>"`; `#SQ-…` ids stay on the questions.
- **Offline listing.** A book counts as downloaded only when its `lib:book:<slug>` cache holds
  `__resident__` with `complete: true` (the test `pwa.js` `resident()` uses).

---

## 9. Measuring and gates

The helpers live in `…/scratchpad/ui/` and `…/scratchpad/ui/architect/`. They hard-code
`ROOT=/home/user/library`, so a worktree does not isolate them. **Every run that writes or
reads `docs/` goes through `architect/locked.sh`** (a `flock` on `scratchpad/ui/docs.lock`),
and each package runs navcheck with its own `NAVCHECK_PORT`.

| helper | what it does |
|---|---|
| `restyle.py` | pushes `shared/assets` CSS and JS, and the `nav.py`/`pwa.py` passes, into `docs/` in ~20 s |
| `onebook.py <slug>` | rebuilds one book (SHELL, `build.py`, `webbuild`, `src` changes) |
| `architect/frontdoor.py <slug>` | re-emits one front door and its extra pages in seconds; byte-identical to the build |
| `architect/hubonly.py` | re-emits `docs/index.html` in seconds; byte-identical |
| `shoot.py` | root-served shots |
| `architect/prodshot.py` | served under `/library/` as in production; `--touch --standalone --nostore --scroll --click --eval --full`; wave 0 adds `--overlay DIR` (the proof pages) and `--engine` |
| `architect/contrast.js` | text-contrast census for `--eval`. Reads `rgb()`, `color(srgb …)` and anything a canvas can paint. **Pass = failing 0, unparsed 0, and measured ≥ the page's baseline** in `baselines/contrast.json` |
| `architect/locked.sh` | the docs lock |
| wave 0 adds: `textdiff.py`, `mixshell.py`, `proof.py`, `baseline.py` | see the W0 package |

**Engines and faces.** Only Chromium is installed. Wave 0 tries to install WebKit for
Playwright; if it cannot, every `@supports` fallback (color-mix, overflow clip, container
units, `:has`, `text-wrap`) gets a written review in W5. Screenshots here render Bitstream
Charter and DejaVu Sans, not Iowan and SF: bar-fit tests are conservative, and judgements of
"one family" are made on the fallback faces.

**Repo checks** (each package runs these through the lock):

```
python3 tools/nav.py --check
python3 tools/pwa.py --check           # wave 0: also regenerates PAGE, manifests and nav.json in memory and compares
python3 tools/sitecheck.py             # wave 0: SITE-prefixed hrefs and #fragments checked; --build <slug> for build/
python3 tools/navcheck.py              # wave 0: waits fail instead of aborting; masked overflow sweep
NMT_BOOK=breast-cancer python3 tools/make.py && NMT_BOOK=breast-cancer python3 tools/verify.py
NMT_BOOK=newton-to-mtheory python3 tools/make.py && NMT_BOOK=newton-to-mtheory python3 tools/verify.py
python3 tools/figcheck.py $(cd build && ls newton-to-mtheory/ch*.html | sed 's/.html$//')   # from the repo root
python3 tools/sitecheck.py --build breast-cancer && python3 tools/sitecheck.py --build newton-to-mtheory
python3 tools/bc.py --check            # any package touching bc.py
```

`build/` is gitignored and only as fresh as the last `make.py`. Physics `verify.py` may
report the displays listed in `baselines/eq-wide.json` (those wider than 35em) as needing
attention until W4-MATH lands; nothing else above its baseline.

**Wave gate.** At the end of each wave, on the merged tree: rebuild what the wave touched,
run every check above, the contrast census over the sample set, `mixshell.py` (from wave 1),
and proof-page shots at 390 and 1280 in both themes. The architect reviews the shots before
the next wave starts. Wave 1's review is the one that matters most: the scale, weights and
colour roles are cheap to change in tokens then and expensive afterwards.

---

## 10. Waves

All work lands on one UI branch. `docs/` reaches `main` only after W5.

- **Wave 0, harness**: W0-HARNESS.
- **Wave 1, foundations**: W1-HEAD (bar, theme, hub colours), W1-TOKENS (tokens and type),
  W1-PHILO (the atlas and the timeline, framed).
- **Wave 2, the frame**: W2-FRAME (chapter geometry, sidebar, contents, chapter foot,
  Through-Line), W2-PHONE (spy, folio, drawer, headroom, find a chapter).
- **Wave 3, the apparatus and the front**: W3-CLINIC (evidence tables, cards, stories,
  references, print), W3-FM (front doors and appendices), W3-HUB (hub and the returning
  reader).
- **Wave 4, the mathematics**: W4-MATH (equations, equation cards, sitting breaks,
  preambles).
- **Wave 5**: W5-INTEGRATE, the full rebuild and library-wide review.

Within a wave, packages own disjoint files. Two moves span waves on purpose:
- The drawer and `#themer` rules are **copied** into `nav.css` in wave 1 (W1-HEAD, by
  selector, without book.css's `scroll-padding-top` line) and **deleted** from `book.css` in
  wave 2 (W2-FRAME). Identical duplicates in between are harmless.
- `.mn-seq` styles move from `pwa.css` to `nav.css` in wave 2 (W2-PHONE).

---

## 11. Deliberately not doing

- **Vendoring a text face.** Only system or already-vendored assets.
- **Weight work**, including lazy-loading `formal.json` (dropped in revision 2: the Long
  Argument's search index, thinker panels and theme views read it on load). Also no
  MathML-only KaTeX, chapter splitting, `content-visibility`, minifying, a shared
  `book.css`, `shelf.js`, or registry pagination.
- **Rewriting the physics chapters' authored eyebrows** (" — Chapter 1.1").
- **Hub tile snapshots of each figure.** The weather, accent rule and status line carry
  identity.
- **A first-visit title strip for the instruments.** Their masthead (kept at ≥1000 px), the
  bar and the hub tile name them.
- **The timeline's tabs in the library bar.**
- **Part chips on the contents page.** The sidebar, the drawer and "Find a chapter" cover it.
- **A vertical cap with a sticky head on evidence tables.** The phone labels do the head's
  job without nested scrolling.
- **Keeping Contents inline in the phone bar** with the rest under "More". At 360 px (common
  Android) it does not fit without another breakpoint; from a chapter the drawer's first row
  reaches the part in the contents in two taps, and on the front door Contents is the
  primary.
- **Auto-opening the references when the reader reaches them.** It would push the chapter
  foot away again.
- **Remapping callout colours**, changing the `<title>` separator, or restyling the atlas's
  age rail and the timeline's lanes.

---

## 12. What changed in revision 2

- Dark `--paper` was wrong (light grey panels at 1.65:1); it is now 3% white into the dark
  ground. Floors are measured per book, and the instruments are stated as outside them.
- `themecss()` emits only the four chosen colours; derived roles live in `book.css` alone.
- The bar is full-bleed with one `--lib-inset`, shared with the sidebar and the frames.
  `--lib-frame` is gone, which fixes the 144 px jump and the 4 px sidebar misalignment.
- Type: h3 and the subtitle now outrank the body; display and title are 400, heads 700;
  vertical rhythm is in body lines; hyphenation is specified.
- Measure: the Through-Line is set at 35em with hanging passage numbers; appendix bodies are
  capped at 36em of their own size.
- Evidence tables bleed across `.main`, fold identity columns into the trial cell, use
  sentence-case heads, and label every cell on a phone.
- Stories are sized in em of the body; trial marks are serif; there is one "has a card" mark,
  and equation references get cards too.
- Folio arrows carry chapter numbers; the drawer's first row goes up; headroom needs a
  deliberate scroll up; sheet handles really drag; the sidebar gets one folio row.
- The clinical front door keeps Contents as its primary; resume is a `.go` there.
- The atlas and the timeline keep their masthead at ≥1000 px.
- Print is specified.
- Safety for mixed shell and page versions, the `runtime_js` contract, the build-capture
  contract, and a z-index scale.
- A wave-0 harness package, a docs lock, a fixed contrast census, physics checks in every
  gate, and a separate wave for the mathematics.
