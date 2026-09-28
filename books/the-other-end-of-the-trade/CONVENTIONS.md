# How this book is written

This book is rewritten from two sources: the Dealer Mechanics Lab's curriculum and the SPX/XSP
Edge Book (both in `source/`). The rewrite has four aims, and every chapter serves all four:

1. **Assume very little.** The reader knows algebra and introductory statistics (mean, standard
   deviation, the normal curve, a p-value). Everything else is taught where it is first needed:
   logarithms, compounding, probability distributions, expectation, and the calculus ideas
   (a derivative as a rate of change, an integral as accumulation).
2. **Competent maths.** Formulas are stated exactly, every symbol is defined, derivations are
   kept and built step by step, and every formula is worked once with real numbers.
3. **Practical.** Every idea ends in what it means for a real account: costs, taxes, margin,
   sizing, and a rule for when to act and when not to.
4. **Plain, direct wording.** The Google developer documentation style guide, with the
   library's house-style rules on top (`.claude/skills/house-style/SKILL.md`).

The reader is an oncologist: at home with clinical statistics, trial design and evidence, new
to markets. Write for that reader.

## Where things live

```
outline.json          parts and chapters: numbers, titles, sources, figures. Titles live here only.
chapters/<slug>.md    one file per chapter, in the house markdown below
glossary/<part>.json  glossary entries, one file per part (glossary/I.json, glossary/X.json, ...)
notes/<slug>.md       what the rewrite dropped, changed or could not settle, per chapter
figures/<id>.html     the interactive figures (do not edit them while writing a chapter)
source/dealer-lab/    the Dealer Mechanics Lab text as imported; source/dealer-lab/outline.json
                      maps its sections to the old chapter numbers used below
source/spx-book/      the SPX/XSP Edge Book
```

`python3 tools/spx.py --sources <slug>` prints everything a chapter is rewritten from.

## Voice and style

The house-style skill governs. The points that matter most here:

- **One idea per sentence.** Do not chain independent clauses. Aim for a mean of 15 to 18 words a
  sentence and nothing over about 35. Lists are not chains: a colon introducing a series is fine.
- **Short paragraphs.** Two to five sentences. One point each.
- **Talk to the reader.** Use "you" and the imperative ("Drag the strike to 105"). This book
  teaches, so the house default of third person does not apply; the physics book is the same.
  Never "we", "us" or "our".
- **American spelling** (behavior, color, analyze). The subject is US markets, the sources are
  American, and the Google guide asks for it. The rest of the library is British; this book is
  the declared exception.
- **Present tense, active voice.** Say who does what.
- **No contractions** ("do not", "cannot").
- **No em dashes.** Use a colon, a comma, parentheses or a full stop. Use "to" for ranges in prose
  ("2 to 20 days").
- **Headings in sentence case**, no full stop, no numbers in them (the build numbers chapters).
- **No Latin abbreviations.** "for example", "that is", "and so on".
- **Nothing time-anchored.** Not "currently", "nowadays", "recently". Give the year.
- **No hype and no guarantees.** Not "always works", "guaranteed", "risk-free profit" (unless the
  term is the technical one, as in "risk-free rate").
- **Numbers.** Numerals for 10 and above, and for anything with a unit, a percent sign or a
  dollar sign. Say what a number is a number of: "a 55% win rate over 1,000 trades", not "55%".
  Annualized volatility is written as a percent in prose (20%) and as a decimal in formulas (0.20).

## The shape of a chapter

Most chapters follow this order. Use the parts that fit; a mechanics chapter may have no
"evidence", a reference chapter no toy example. The edge chapters of Part X should use all of it.

1. `::: where` **Where we are.** Two or three sentences: what came before, what this chapter does,
   why it matters. (The first chapter of the book has none.)
2. `::: tools` **What you need first.** The earlier chapters and ideas this one relies on, as a
   short list with chapter references. Omit it when nothing is needed.
3. **The intuition** in plain words, often as a `::: plain` callout.
4. **A toy example** with numbers small enough to do in your head, as a `::: worked` block.
5. **The maths.** The formula, every symbol defined, one worked calculation. Long algebra goes in a
   `::: grind` box so a reader can skip it and still follow.
6. **The evidence.** What studies and data show, with authors and years, and with every hedge the
   source uses.
7. **Why it exists.** The mechanism: who pays, who is forced, who is mistaken.
8. **In practice.** A `::: practice` callout: how it works in a real account, what it costs, how
   it degrades.
9. **When it fails.** A `::: warn` callout titled "When it fails".
10. **A decision rule.** A `::: rule` callout: when to act, when not to, and how much.
11. **Common mistakes.** One or two `::: warn` callouts titled "Common mistake: ...".
12. **Familiar ground.** Where it genuinely helps, a `::: familiar` callout that explains the idea
    through something the reader knows from clinical research. At most one or two a chapter, and
    only when the analogy is accurate.
13. `::: recap` **What to carry forward.** Three to five bullets.
14. `::: check` **Check yourself.** Three to six questions, each with a worked answer.

Good analogies for this reader, where they fit: base rates and positive predictive value (a
signal's hit rate); multiple comparisons (backtest overfitting, the deflated Sharpe ratio);
publication bias (why published edges decay); intention-to-treat against per-protocol results
(paper against live performance); regression to the mean; dose and toxicity (position size and
tail risk); a Kaplan-Meier curve (a drawdown path); screening sensitivity and specificity (a regime
filter). Never force one.

## The house markdown

A chapter file has no title line: the title and subtitle come from `outline.json`. It starts
with its first callout or paragraph.

**Headings.** `##` for sections, `###` for subsections. Nothing deeper.

**Text.** `**bold**` for a term at the moment it is defined, `*italic*` for emphasis, sparingly.
Lists with `-` or `1.`. Tables in pipe form, with a header row; they become the house data table.
A block quote (`>`) is for a quotation from a source, with its attribution on the last line.

**Maths.** Inline maths between `\(` and `\)`. Display maths on lines of its own:

```
\[ \mathbb{E}[X] = \sum_i p_i\, x_i \]
```

A display may carry a label on the line after it, `{#eq:ev}`, and prose can then cite it as
`[eq:ev]`, which becomes its number, "(1C.2)". Labels work within a chapter only. Never use `$`
for maths: the dollar sign is money in this book. Inside maths, write money as `\$`.

**Callouts.** A fenced block, with an optional title after the kind:

```
::: practice
Text of the callout.
:::

::: warn When it fails
Text.
:::
```

| kind | default title | use |
|---|---|---|
| `where` | Where we are | chapter opening |
| `tools` | What you need first | prerequisites, as a list |
| `plain` | In plain terms | the idea without maths |
| `worked` | Worked example | a calculation, step by step; give it a title |
| `grind` | The full derivation | long algebra a reader may skip (it opens on a click) |
| `insight` | Key idea | the one thing to remember from a section |
| `practice` | In practice | real accounts, costs, taxes, behavior |
| `rule` | Decision rule | when to act, when not, how much |
| `warn` | (title required) | "When it fails", "Common mistake: ..." |
| `familiar` | Familiar ground | a clinical analogy |
| `recap` | What to carry forward | chapter summary |
| `check` | Check yourself | self-test, see below |

A worked example's steps are paragraphs that start with a bold label: `**Step 1: write the
payoff.**` Callouts do not nest, except that maths, lists and tables are fine inside them.

**Self-check.** Inside `::: check`, a question starts a line with `?? ` and its answer with
`!! `. Either may run over several paragraphs until the next `??` or the end of the block.

```
::: check
?? A strategy wins 90% of the time. Can it lose money?
!! Yes. If each loss is ten times the size of each win, the expected value is
\(0.9 \times 1 - 0.1 \times 10 = -0.1\) per trade.
:::
```

**Glossary.** Mark a term with `[[term]]`, or `[[shown text|term]]` when the words on the page
differ from the entry (`[[calls|call option]]`). The reader gets the definition on a card. Mark a
term at its first use in each chapter, not every time. Every marked term needs an entry in
`glossary/<part>.json`:

```json
{
  "call option": {"def": "A contract giving its holder the right, not the obligation, to buy the underlying at the strike price on or before expiry.", "chapter": "5A"}
}
```

`chapter` is where the term is properly explained. A definition is one or two plain sentences,
with no maths markup and no glossary marks inside it. Before adding a term, check the other
parts' files: if it exists, use it as it is; if its definition is wrong for your use, say so in
your notes rather than adding a second entry.

**Chapter references.** Write "Chapter 5C" (or "Part V") in the text; the build turns it into a
link. Only the new numbers in `outline.json` exist.

**Figures.** Place each figure the outline lists for the chapter with a line of its own:
`[FIGURE: skew-simulator]`. Every one must be placed. Before it, tell the reader what the figure
shows and what to try; after it, what they should have seen. Read `figures/<id>.html` first so the
prose matches the figure's controls, defaults and caption.

**Figure ideas.** Mark every place where a new figure would help the reader, generously: the
author wants more figures. On a line of its own:

```
[FIGURE IDEA: A drawdown curve for the S&P 500 from 2000 to 2013, with the reader choosing a start
date, showing how long each loss took to recover.]
```

Say what it would draw, what the reader would control, and what it would make clear. Figure
ideas are not shown in the book; they are collected into `FIGURE-IDEAS.md`.

**Code blocks.** A fenced block without a language is set as a formula block, in monospace, and
keeps its line breaks. Use it for things whose meaning is in their columns, such as an order book
ladder. Use real maths (above) for formulas.

## Maths notation

Use the same symbol for the same thing everywhere. Define each symbol at its first use in every
chapter that uses it.

| symbol | meaning |
|---|---|
| \(S\), \(S_t\) | price of the underlying (at time \(t\)) |
| \(K\) | strike price |
| \(T\) | time to expiry, in years (30 days is \(30/365\)) |
| \(R_t\) | simple return, \(S_t/S_{t-1} - 1\) |
| \(r_t\) | log return, \(\ln(S_t/S_{t-1})\) |
| \(r\) | risk-free interest rate (no subscript); write \(r_f\) where log returns also appear |
| \(q\) | dividend yield |
| \(\mu\) | mean (expected) return |
| \(\sigma\) | volatility: annualized standard deviation of log returns |
| \(\sigma_I\), \(\sigma_R\) | implied and realized volatility |
| \(\mathbb{E}[X]\), \(\operatorname{Var}(X)\) | expected value and variance |
| \(\Pr(A)\) | probability |
| \(N(x)\), \(\varphi(x)\) | standard normal distribution function and density |
| \(d_1\), \(d_2\) | the Black-Scholes quantities |
| \(\Delta, \Gamma, \Theta, \nu\) | delta, gamma, theta, vega |
| \(\rho\) | correlation; the Greek rho is written as a word |
| \(\text{SR}\) | Sharpe ratio |

## Facts: what must survive, what to fix, what to add

This follows the house-style rule "add nothing", adjusted for a teaching rewrite.

**Keep.** Every number, date, name, study, source, instrument and qualifier in the sections a
chapter is rewritten from, and every hedge ("suggests", "roughly", "in the authors' sample",
"low confidence") at its original strength. If something is truly redundant, you may drop it,
but list it under "Dropped" in the chapter's notes with the reason. `python3 tools/spx.py
--facts <slug>` lists numbers and names from the sources that the chapter no longer contains.
Account for each: restore it, or list it as dropped.

**Fix.** Known errors, listed at the end of this file. Make the text right and say so in the notes.

**Add teaching, not facts.** Definitions, explanations, derivations, analogies, and toy examples
are welcome; that is the point of the rewrite. A toy example is plainly hypothetical ("Suppose a
coin pays..."), and its arithmetic must be right. Do not add empirical claims, statistics,
studies, dates, prices or events that are not in the sources. If the reader needs a fact the
sources do not give, write the question in your notes instead.

**Disagreements stay disagreements.** The two sources sometimes differ. The Edge Book rejects
systematic iron condors and scalping around gamma-exposure levels for retail accounts; the Dealer
Mechanics Lab teaches both. Where they differ, state both positions, with each one's reasons,
and link the chapters to each other. Do not quietly pick one.

**Translate old references.** The sources cite themselves by their own numbers. Rewrite every such
reference to the new chapter numbers:

| Dealer Mechanics Lab | new | | Dealer Mechanics Lab | new |
|---|---|---|---|---|
| Section 1 (Foundation) | Part I | | 6A, 6B / 6C / 6D / 6E / 6F | 6A / 6B / 6C / 6D / 6E |
| 1A | 1B, and 1D for the Sharpe parts | | 7A / 7B | 7A / 7B |
| 1B / 1C / 1D | 1A / 1C / 1D | | 8A to 8D, 9A to 9C | same numbers |
| Section 2 (Quant) | Part III | | Section 10 (Tactical) | Part XI |
| 2A / 2B / 2C / 2E | 3A / 3B / 3C / 3D | | 10A / 10A.5 / 10B / 10C / 10D | 11A / 11B / 11C / 11D / 11E |
| 2D | 2C | | 10E / 10F / 10G / 10H / 10H.2 | 11F / 11G / 11H / 11I / 11J |
| Section 3 (Markets) | Part II | | 10I / 10J / 10K / 10L | 11K / 11L / 11M / 11N |
| 3A / 3B / 3C / 3D / 3E | 2A / 2B / 2E / 2C / 2D | | Section 11 (Atlas), 11.0 to 11.7 | Part XII, 12A to 12H |
| Section 4, 4A to 4C | Part IV, same | | Section 12 (Discipline) | Part XIII |
| Section 5, 5A to 5G | Part V, same | | 12A / 12B / 12C / 12D / 12E / 12F | 13A / 13B / 13C / 13D / 13F / 13H |

| Edge Book | new |
|---|---|
| Chapter 0 | 1B (0.1, 0.2), 1E (0.3 to 0.5, 0.7), 1F (0.6, 0.8 to 0.11) |
| Chapter 1 | 1G |
| Chapter 2 | 1C (2.2), 1B (2.3, 2.4), 1D (the rest) |
| Chapter 3 / 4 | 13A / 13B (4.11 goes to 13C) |
| Chapter 5 / 6 | 10A / 10B (6.1), 10C (6.2), 10D (6.3), 10E (6.4 to 6.6) |
| Chapter 7 / 8 / 9 / 10 | 10F / 10G / 10H / 10I |
| Chapter 11 / 12 / 13 / 14 | 13E / 13F / 13C / 13G |
| Chapter 15 | R1 to R4 |

## Notes, per chapter

`notes/<slug>.md` records what a reviewer needs to trust the rewrite:

```
## Sources
dl:1A (distributions part), spx:0.1, spx:0.2 ...
## Dropped
- "..." (spx:0.1): repeated in 1D.
## Changed
- Fixed: ... (why).
## Conflicts
- ...
## Questions for the author
- ...
## Figures
- Caption of skew-simulator says ..., the text now says ...
```

## Checks before a chapter is done

```bash
python3 tools/spx.py --lint <slug>              # markup, maths, glossary, references, figures
python3 tools/spx.py --facts <slug>             # source numbers and names not in the chapter
python3 tools/prosecheck.py the-other-end-of-the-trade <slug>   # sentence lengths
python3 tools/stylecheck.py the-other-end-of-the-trade          # Google rules
```

## Known errors to fix

In the prose (each is also listed in `README.md`):

- Old 2B (new 3B): the AR(1) paths fan out as the weight goes toward +1 and draw in toward −1; the
  source says they fan out toward ±1.
- 5D: with the strike below spot, \(d_1\) and \(d_2\) are positive, not negative. Vanna is still
  negative there, because \(d_2 > 0\).
- 7B: the text after the higher-order Greeks figure describes gamma, which that figure does not
  draw. It draws vanna, charm, volga, speed and color.
- 8A: "net short calls (from buying retail calls)" contradicts itself. Buying calls from retail
  makes dealers long calls. State the 0DTE-era positioning without the contradiction, and say
  plainly that the sign conventions are an assumption about who holds what.
- 9A: the VIX strip builder moves its whole smile with the forward, so it cannot show the claim
  that a fall re-prices the put wing more than a rise re-prices the call wing. Keep the claim,
  explain its mechanism, and say the figure does not model it.
- 9A: "Initial delta-hedge: long approximately 410 shares." A dealer who is short puts is long
  delta and hedges by selling stock, and 1,000 contracts of 100 shares make the hedge tens of
  thousands of shares.
- Old 12D (new 13D): Example 2's conviction product is 0.341, not 0.343. Example 4 takes a trade at
  C = 0.282, below the 0.3 threshold of 13B: either say why that is allowed or say it is a pass.
- Old 12F (new 13H): the vega monitor has no delta input and does not use days to expiry, and its
  three targets are the target vega (flat, half, full), not three sizes of hedge.

In the figures, corrected where the widget contradicted its own maths (the prose must agree with
the figure): see "Where the import departs from the app" in `README.md`.
