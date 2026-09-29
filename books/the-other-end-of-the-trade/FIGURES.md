# How a figure is written

Every interactive widget of the Dealer Mechanics Lab app is rewritten for this book as a
library figure. Each widget becomes ONE file, `figures/<id>.html`, named for the id its
`[INTERACTIVE: id]` marker uses. Paths below are relative to the repository root, and the
app's sources are in a checkout of `Elkhanany/dealer-lab` beside it (`../dealer-lab`).

## Read these first (do not skip)

1. The three finished reference figures, which show every pattern you need:
   - `figures/skew-simulator.html`: a canvas chart driven by a slider, readouts.
   - `figures/ev-bet-builder.html`: a calculator with presets, a chart and a written verdict.
   - `figures/gex-sign-truth-table.html`: segmented choices driving tables, no canvas.
2. `figures/_lib.js`: the `DL` helper every figure uses. It already contains the app's
   `lib/math.js` (N, phi, d1, d2, bsm, bsPrice, bsDelta, bsGamma, bsVega, bsTheta, bsRho,
   bsVanna, bsCharm, rng = mulberry32, gauss), `lib/synth.js` (ohlc = generateOHLC,
   aggregate = aggregateOHLC, REGIMES) and `lib/indicators.js` (sma, ema, stdDev, bollinger,
   trueRange, atr, donchian, rsi, macd, adx), with the same defaults (r = 0.04, q = 0).
   Plus formatting (num, signed, pct, spct, usd, compact, MINUS), page helpers ($, out, val,
   checked, bind, seg, still, figure) and drawing helpers on NMT.Plot (axes, bars, hbars,
   band, line, hline, vline, candles, legend, xticks, fade, color, clip).
3. `shared/assets/book.js`, lines 726-940: `NMT.Plot` (constructor
   options xmin/xmax/ymin/ymax/pad/xlabel/ylabel/grid/equal; methods X, Y, invX, invY,
   axes, fn, path, dot, seg, text) and `NMT.figure`, `NMT.onSnapshot`.
4. `shared/assets/book.css`, section "interactives" (search for
   `figure.fig`): the only figure styling there is. Do not add CSS anywhere.
5. For each widget: the app source `../dealer-lab/src/interactives/<Name>.jsx`
   (and anything it imports from `../lib` or `../refdata`), and the chapter prose around
   its marker: `grep -n "INTERACTIVE: <id>" books/the-other-end-of-the-trade/source/dealer-lab/*.md`
   and read about 40 lines either side, so the caption agrees with the text.

## The file format

```html
<!--
name: <a short lowercase name for the figure, used when the prose names it inline>
source: src/interactives/<Name>.jsx
-->
<figure class="fig" id="fig-{{uid}}">
  <canvas id="{{uid}}-c" data-h="260"></canvas>          (optional; more than one is fine)
  <div class="ctrls"> ... .ctrl groups ... </div>        (controls, then readouts)
  <p class="readout" aria-live="polite">...</p>          (optional: a sentence the figure writes)
  <figcaption><b>A title sentence.</b> Two to four sentences.</figcaption>
</figure>
<script>
(function () {
  var U = '{{uid}}';
  ...
})();
</script>
```

- `{{uid}}` is replaced with a unique instance id. EVERY id in the file must be built from
  it (`{{uid}}-c`, `{{uid}}-sigma`, `U + '-sigma'` in the script). The figure element must be
  `id="fig-{{uid}}"`. The same figure may appear twice on one page.
- Exactly one `<script>` at the end, holding one IIFE. It runs after `_lib.js` and after
  `book.js`, at the end of `<body>`, so the DOM is there and `DL`/`NMT` exist.

## Controls and readouts: the house markup

- Slider: `<div class="ctrl"><label for="{{uid}}-k">strike</label><input type="range"
  id="{{uid}}-k" min=.. max=.. step=.. value=..><output id="{{uid}}-k-o" for="{{uid}}-k"></output></div>`
- A choice between a few values: `<div class="ctrl" role="group" aria-label="Option type"
  id="{{uid}}-type"><label>option</label><button type="button" data-v="call" class="on"
  aria-pressed="true">call</button><button type="button" data-v="put" aria-pressed="false">put</button></div>`
  and `var type = DL.seg(U + '-type', draw);` then `type()` gives the value. Mark the default
  `.on` in the markup.
- A plain action (reset, step, new paths, a preset): `<button type="button" id="{{uid}}-reset">reset</button>`
  inside a `.ctrl`. EVERY button needs `type="button"`.
- A checkbox: `<div class="ctrl"><input type="checkbox" id="{{uid}}-x" checked><label for="{{uid}}-x">show x</label></div>`.
- Readouts: `<div class="ctrl"><output id="{{uid}}-mean"></output></div>` in a `.ctrls` row,
  written as `label = value` (`DL.out(U + '-mean', 'mean μ = ' + DL.num(m, 3))`). Keep each
  output under about 34 characters so it fits a phone; longer text goes in a `p.readout`.
- A verdict or recommendation sentence: `<p class="readout" aria-live="polite"><b id="{{uid}}-vk"></b>
  <span id="{{uid}}-vt"></span></p>` and write both with DL.out.
- A table: the house data table, `<div class="evidence"><div class="ev-scroll"><table class="trials">`
  with `<th>`/`<td>`, the first column's cells `class="c-trial"`. For three or more columns give
  every non-first `td` a `data-label="<its column head>"` (a phone prints it above the cell).
  A highlighted row is `tr.on` (toggle the class from the script). Write cell text with DL.out.
- Labels are lowercase words, as in the references ("strike", "days to expiry", "IV"). Use
  the app's own labels and units wherever they exist.

## The rules the build enforces (break one and the book fails its checks)

1. **Static markup.** The script only writes text (`DL.out`), toggles classes/attributes, sets
   input values, and draws on canvases. It never creates, removes or rewrites elements: no
   innerHTML, createElement, appendChild, insertAdjacentHTML, removeChild. If the app renders a
   variable-length list, render the maximum number of rows in the markup and hide unused ones
   with the `hidden` attribute (`el.hidden = true`), or redesign it as a canvas.
2. **A fixed first state.** The build loads the page, lets the scripts run, and saves the
   column's HTML; two builds must be identical. No Math.random, no Date, no clock. Randomness is
   `DL.rng(seed)` with a constant starting seed; a "new paths" button or a seed slider changes it.
3. **Nothing moves unless the reader moved it.** No autoplay. An animation starts from a button,
   uses requestAnimationFrame, checks `DL.still()` (reduced motion: jump straight to the end
   state), and registers `NMT.onSnapshot(reset)` so the build always saves the first frame.
   No setInterval.
4. **Colours from the theme only.** `DL.color('accent' | 'familiar' | 'insight' | 'warn' |
   'plain' | 'ink' | 'ink-soft' | 'ink-faint' | 'rule' | 'rule-soft' | 'paper')`, and
   `DL.fade(DL.color(role), alpha)` for fills. Never a literal colour. The app's amber is
   `accent`; its cyan and violet are `familiar`; its green/emerald `insight`; its rose/red
   `plain`; its yellow `warn`; its stone greys `ink-soft`/`ink-faint`. Read colours inside the
   draw function (they change with the theme; the figure is redrawn on a theme change).
5. **Draw through NMT.Plot.** `var draw = DL.figure(U + '-c', function (c) { var p = new
   NMT.Plot(c, {...}); DL.axes(p, {...}); ... });` then `DL.bind([ids], draw)`. Use the draw
   function DL.figure returns (redraw only this figure). A figure without a canvas registers
   its update with `DL.figure('fig-' + U, update)` as the truth table does. Canvas text: 11-12px
   `DL.color('sans')`, via `p.text(...)`, in ink-soft/ink-faint or a series colour. Use DL.axes
   rather than p.axes when the two axes need different formats or you want explicit ticks.
6. **It fits a phone.** At 390px nothing may be wider than the figure: short outputs, controls
   that wrap, text on the canvas that stays inside it (check the 390 screenshot for overlapping
   labels and shorten or move them).
7. **Accessible.** Every input has a `<label for>` (or aria-label). Button groups carry
   role="group" and aria-label. Canvases are decorative (the readouts carry the numbers).

## Faithfulness

- Port the widget's computation exactly: same formulas, constants, defaults, ranges, steps,
  seeds and presets. If the widget computes something, the figure computes the same thing.
- Keep every control and readout that carries information. You may add a small canvas chart to
  a calculator that had none if it shows only quantities the widget already computes (as
  ev-bet-builder does); never invent new analytics, numbers or claims.
- The app often shows a note or "Aside" inside the widget. If its content is not already in the
  prose next to the marker, carry it into the caption or a `p.readout`. If it is already in the
  prose, do not repeat it.
- If the widget contains a mistake (a label that contradicts its own maths, say), make the
  figure agree with the maths and the prose, and report the mistake in your final message.
- Data the widget imports (e.g. a refdata JSON) is embedded as a literal in the script. If the
  data is synthetic or illustrative, the caption must say so plainly.

## The caption

`<figcaption><b>Title sentence.</b> ...</figcaption>`: say what is drawn and what the controls
do, in two to four plain sentences, and what to watch for if the prose makes that point. Use
the chapter's own terms and American spelling (the prose is American). No em dashes (use a
colon, a comma or a full stop). No "we"; the imperative is fine ("Drag the strike..."). No
contractions. Do not claim anything the widget and the prose do not support.

## Test every figure, and look at it

```bash
python3 tools/spxfig.py --shots <your shots dir> <id> [<id> ...]
```

It checks the static rules above, labels and button types, that nothing throws, that every
canvas paints before and after every control is exercised, that the figure fits at 390px, and
that two loads save identical HTML. Iterate until it prints `ok` for every figure. Then OPEN
the screenshots (`<id>-1280-light.png`, `<id>-390-dark.png`) with the Read tool and fix what
looks wrong: overlapping or clipped labels, empty plots, illegible contrast, a chart squashed
into a corner. The final state in the screenshots is after the harness pressed every control,
so the last button of each group is selected; that is expected.

## Porting status

`python3 tools/spx.py` fails while any `[INTERACTIVE]` marker has no figure; `--draft`
builds anyway, with a placeholder in each missing figure's place. `python3 tools/spxfig.py
--all` tries every figure that exists.
