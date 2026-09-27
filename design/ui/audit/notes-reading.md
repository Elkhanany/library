# Reading-experience audit: chapter pages across the four books

Lens: typography and reading on chapter pages. Everything below was measured on the built pages in
/home/user/library/docs served over HTTP (Chromium, 390x844 and 1280x900, light and dark; also 1024
and 1920 where noted). Screenshots are in `shots/reading/` (top of page), `shots/reading/spots/`
(clips around components, `*.segNN.*` = consecutive screens of one page) and
`shots/reading/full/` (full pages). Measuring scripts are `shots/reading/{measure,spot,tables,probe390,simtable.js,interact}.py`.

Caveat on fonts: the renderer has none of the named faces. Body falls back to Liberation Serif
(Times metrics) and sans to Liberation Sans. Characters per line are therefore given as a range:
Times-class, Georgia/Iowan-class (estimated), and a wide Noto-class serif (measured with DejaVu Serif).

## Measurements

| page | width | column | body | chars/line (Times / Iowan est. / Noto-class) |
|---|---|---|---|---|
| BC-900, BC-870, BC-490 | 1280 | 704px (`--measure:44rem`) at x=304..1008 | 19px / 1.68 | 83 / ~70 / 65 |
| same | 390 | 361px | 17px / 1.62 | 48 / ~40 / 37 |
| ch1-2, ch3-5 | 1280 | 704px | 19px / 1.68 | 83-96 (math lines) |
| Long Argument study (Spinoza) | 1280 | `.sp` 72ch = 594px | 16.5px / 1.66 Spectral->Georgia | 80 (Times) / ~67 |
| Atlas dossier | 1280 | 393px panel | 13px / 1.55 IBM Plex Sans->system sans | - |

Heading scale actually rendered (desktop and phone are the SAME, see finding R1):
h1 36px sans 700, h2 22.7px sans 650 + rule, h3 17.3px sans 650, body 19px serif.

## Findings, ranked by reader cost

### High
- **R-01 Evidence tables collapse to min-content columns.** `.evidence table.trials th{white-space:nowrap}` (book.css:405) plus uppercase letter-spaced headers (book.css:386) force the table past 100%, and auto layout then gives every column its min-content width: Population 101-106px, Result 85-131px at both 390 and 1280. Rows are 336-373px median, 612-728px tallest; BC-900's five tables are 13,311px tall at 1280 (34% of the chapter; BC-870 39%). While scrolling a row the header is gone and the right-hand columns (Result, OS) are off the clipped edge with no scroll cue: in BC-490 seg03 at 1280 the visible last column is "Primary endpoint" ("...against a non-inferiority boundary of 92%"), which reads as a result. Simulation (simtable.js 'minW2'): headers wrap, Population min 17rem, Result/OS/Experimental min 12rem, table width auto: total height 13,311 -> 6,286px (-53%) at 1280, 11,916 -> 5,396px at 390; median row 373 -> 176px. Also: caption (`.ct-cap`, bc.py:415) comes after the table though it says how to read it; there is 272px (1280) to 608px (1920) of empty page to the right of the clipped table. Shots: spots/breast-cancer__BC-900.html.evidence-0.*, spots/breast-cancer__BC-490.html.seg03.1280.light.png, spots/*SIMULATED*.
- **R-02 The phone type scale and the phone equation layout are dead CSS.** book.css:115-133 (`@media (max-width:760px)`) sets h1 1.7rem, h2 1.2rem, h3 1.02rem, `.eq{padding:0 0 1.5rem}`, `.eqnum{top:auto;bottom:0}`, `.katex{font-size:1em}`, `.ctrls` gap, range width, `#themer` offset. The unconditional rules for the same selectors come later (h1-h4 :147-152, .eq/.eqnum :316-319, .katex :324, .ctrls :369, range :373, #themer :555) with equal specificity, so they win. Measured at 390: h1 36px, h2 22.72px, h3 17.28px, `.eq` padding-right 51.2px, eqnum vertically centred. Cost: BC-490's title is 4 lines/180px and the first paragraph starts at y=542 of 844 (fixed: 68px, y=421). In ch3-5, 41 of 84 numbered equations overflow their 310px box; (3.5.5) shows "for every i", (3.5.7) loses its fourth term, with no sign that it scrolls; moving the number below as intended rescues 13 of them. Shot: spots/newton-to-mtheory__ch3-5.html.eq-3.390.light.png.
- **R-03 Sitting-break labels overflow at every width.** `.pause span{white-space:nowrap}` (book.css:197) with 185-228 character labels: 638-1209px at 390 and 1247-1381px at 1280, in a 361/704px column. Label is cut at the viewport edge and the rules either side collapse to zero; a whole sentence set in 11px letter-spaced capitals. All 24 pauses (ch4-2..ch4-9). Shots: spots/newton-to-mtheory__ch4-6.html.pause-0.1280.light.png, ch4-2 ...390.dark.png.

### Medium
- **R-04 No text face is shipped; four books read in four different type systems.** book.css:28 `--serif` begins with Iowan Old Style (Apple only), then Palatino Linotype (Windows); Android gets Noto Serif. The two philosophy books name Spectral and IBM Plex (the-long-argument/src/_landing.html `--f-disp/--f-ui`) but no @font-face exists anywhere (0 in all four books), so they render in Georgia/Times and system sans. On one Mac the physics book is Iowan, the Long Argument is Georgia, and the atlas dossier is 13px system sans. Chars per line at 1280 range from 65 to 83 depending on the device's fallback. KaTeX fonts are already vendored (shared/vendor/katex), so vendoring one text face follows an existing pattern.
- **R-05 Citation superscripts break the leading.** sup .cite at 11.7px bold sans (book.css:230) raises the line box: in BC-900 paragraphs with citations, 25 of 109 baseline gaps are 35-36px instead of 32 at 1280 (27 of 202 at 390). `sup{line-height:0}` with .cite at .78em makes them all 31-32px. On coarse pointers `.cite{padding:.35em .45em;margin:0 -.15em}` (book.css:262) pushes "registered ⁸ ." apart and puts a space before the period (spots/cite-before.390.light.png).
- **R-06 Trial names are the loudest words on the page and do nothing.** `.trial` is sans 600 .88em in --ink with a rule underline (book.css:233); BC-900 has 134 of them; the comment at book.css:222 says "small caps" and "each mark is quiet". The detail sits only in a native `title` (bc.py:274): invisible on touch, slow and unstyled with a mouse. The chips under each story question (`.sq-trials`) are drawn as bordered buttons, and book.css:436-437 styles `a.trial` hover, but no trial is a link (0 anchors). Glossary terms (`.gloss`) likewise title-only.
- **R-07 On phone, the reader scrolls 4-10 screens of references to reach Next.** BC-870: 74 refs, 8,558px at 390 (10.1 screens), 5.4 screens at 1280; BC-900 7.6 screens; chapnav is only after the list (build.py:93-107, bc.py:591-597). Refcards already bring each reference to its citation.
- **R-08 Physics chapter preambles are long tinted panels.** "Where we are" + "Tools you'll need" before section 1: ch3-5 2,509px at 390 (3 screens; where 1,656px, tools 407px), 1.6 screens at 1280; ch4-6 the same. The `where` callout is a filled panel with a 3px rule (book.css:176) holding 4-6 paragraphs; the tools box is 13px sans (book.css:213).
- **R-09 The library bar is not sticky at 1000px and below.** book.css:116 and :632 set `html,body{overflow-x:hidden}`; body becomes a scroll container, so `.topnav{position:sticky}` (nav.css) sticks to nothing: at scrollY=3000 the bar is at -3000 at 390 and 900, at 0 at 1280. book.css:482-484 still assumes a sticky 56px bar. `overflow-x:clip` keeps the no-sideways-scroll guarantee without breaking sticky.
- **R-10 The desktop layout is left-heavy and wastes the right margin.** `.wrap{max-width:82rem}` + `.col{max-width:44rem}` (book.css:75,82): at 1280 the column ends at 1008 leaving 272px empty; at 1920 the sidebar floats as a grey slab from x=304 and 608px is empty right of the text, while tables are clipped. The Long Argument study uses the same space for a sticky context rail.
- **R-11 Story blocks invert their own hierarchy and read as secondary.** `.st-title` sans 15.7px (book.css:423) under a 10px kicker, while `.sq-ask` is serif 19px 600 (book.css:427), so the question outranks the story title; `.sq-moves dd` (the argument) is --ink-soft (book.css:432), `dt` labels are 10px --ink-faint (3.4:1). The same title and kicker repeat verbatim at each section a story spans (BC-900: 3x; BC-870: 4 alternations).
- **R-12 Low-contrast small text.** --ink-faint is 3.41:1 (BC light), 3.6:1 (NMT) and is used for 10-12px labels: story dt, chapnav "PREVIOUS/NEXT", sidebar lvl3 TOC (3.12:1 on --bg-alt), eqnum, `.prob .pnum`, `.sb-title`. The Long Argument's --ink-4 (1.84:1 on paper) colours its study section tabs `.snav a` 11px (src/_landing.html:593), `.wkk` 9.5px (:623), `.argfoot h5` 9px (:996). The atlas already states the rule ("--ink-3 is the palest ink a WORD may use: 4.9:1").
- **R-13 The Long Argument's reading unit has no address.** 133 studies (each ~4,300px of prose) open through `openStudy()` with no hash or query state (0 uses of location.hash); a study cannot be linked, bookmarked, restored by Back or reload, or resumed. The atlas has 133 dossiers for the same 133 ids and neither book links to the other.

### Low
- **R-14 Colour-only cross-references in the clinical book.** `.xref` underline is --accent-soft, 1.17:1 against the page (book.css:236); link vs body text is 2.24:1 (BC light), 2.13:1 dark. The physics book uses real underlines on `a`, so the two books mark links differently.
- **R-15 Micro-label sprawl.** Nine uppercase letter-spaced label styles between 10 and 11.5px with tracking .08-.15em: .eyebrow :154, .callout .ct :172, .pause :194, .tools b :216, .refs-head :252, th :386, .st-where :421, .sq-moves dt :430, .chapnav span :464, .prob .pnum :349, .sb-title :138.
- **R-16 Body size in px.** `body{font-size:19px}` (book.css:67; 18/17px in media queries) ignores the reader's default font size, while headings and margins are in rem and do scale, so a reader with a 20px default gets larger headings and the same body.
- **R-17 Duplicate element ids.** bc.py:445 gives the story wrapper its first question's id and the question keeps it: 93 duplicate ids on 24 BC chapters (e.g. BC-490 SQ-0040).
- **R-18 Atlas phone header pushes the theme button off-screen** when a thinker is selected: #btnTheme at x=386-403 in a 390px viewport. Long Argument "Happening meanwhile" dates collide with titles: `.scard .wrow{grid-template-columns:46px 1fr}` (src/_landing.html:640) for "1618–1648" at 11px mono = 60px.
- **R-19 No `text-wrap:balance` on headings, no phone hyphenation.** BC-900 h1 at 390 breaks "Metastatic therapy / from first line / onwards"; 17px ragged serif with terms like "leptomeningeal".

## Strengths to keep
- The reference card and sheet (book.js:529-661): hover card on a mouse, bottom sheet on touch, both built from the page's own list and working offline. It is the best reading affordance in the library.
- Scroll-spy sidebar TOC with nested sections and the phone section drawer.
- The physics book's maths: vendored KaTeX, numbered equations with `.eqref` back-links, the MathML copy contained (book.css:91-112), and the equation scroller.
- The callout vocabulary is semantic and calm ("In plain terms" as a panel, `.worked`, grind boxes as details, problem/solution toggles).
- Dark mode is complete and well balanced on chapter pages: ink 13:1, accents re-derived per book.
- Sticky first column on evidence tables, and the evidence block owns its horizontal scroll.
- The Long Argument study page: serif display headings, dated works timeline, sticky section tabs and a context rail. The best-designed reading page in the library and a model for the chapter pages' right margin.
- Paragraph rhythm on the 704px column: 19px/1.68 serif is comfortable, and prose is ~70 cpl on Apple devices.
