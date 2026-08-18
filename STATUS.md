# From Newton to M-Theory — status

*Last updated 18 August 2026, after the review of Parts 0–III.*

## Where the book stands

**25 of 59 chapters written** (67 under the revised plan). Parts 0, I and II complete; Part III
complete through the field equations — 6 of 8.

- 311,000 words · 19,993 typeset expressions · 187 "In plain terms" passages · 126 ⚑ marks
- Every page verified at desktop and phone widths **with all network requests blocked**: zero
  KaTeX errors, zero unresolved cross-references, zero overflow, zero external requests.

| Part | Chapters | State |
|---|---|---|
| 0 · The Toolkit | 0.1–0.9 | complete |
| I · The Action Principle | 1.1–1.4 | complete |
| II · Special Relativity | 2.1–2.6 | complete |
| III · General Relativity | 3.1–3.6 | 6 of 8 — **3.7 Schwarzschild and 3.8 Cosmology are next** |
| IV–VII | — | not started |

## Where it lives

- **The repository** was handed to Ahmed as a zip to push himself (no credential of his has ever
  been near the build machine). `docs/` is the GitHub Pages site; `PUSH-ME.md` in the repo root
  has the three commands.
- **The offline copy** is published to `Dropbox/claude_code/books/physics/` — one self-contained
  file per chapter, opens correctly in isolation on a phone with no signal.

## How it is built

Two targets from one source. `src/ch*.html` are HTML fragments and are the only thing edited by
hand. `make.py` → `build/` (self-contained, fonts inlined, for Dropbox). `webbuild.py` → `docs/`
(shared assets, for the web). Both render the mathematics **at build time** in headless Chromium
and write the finished DOM to disk, so nothing typesets in the reader's browser.

`throughline.py` extracts every plain-terms box in book order into the Through-Line, so that page
can never drift. `verify.py` is the gate — network blocked, both widths, every page.

## The three standing documents

- **`PLAN.md`** — plan of record through 3.6. Superseded forward of 3.7.
- **`PLAN-FORWARD.md`** — the revised curriculum, 59 chapters → 67, with the argument for each
  addition and, for every piece of mathematics the remaining physics needs, an explicit decision to
  build it or to ⚑ it.
- **`GAPS.md`** — what the book has used but not built, ranked by what each gap costs the reader.

## What the review of August 2026 established

Five independent agents over Parts 0–III. **No result in twenty-five chapters was wrong** — about
ninety symbolic identities and forty numerical values re-derived from scratch and agreed, the second
Bianchi identity to 1e−31 at sixty digits, κ = +8πG/c⁴ derived from the book's own definitions.
Three printed values and signs were corrected, all with correct final answers, which is why they had
survived.

The material finding was editorial: **the ⚑ convention was not applied at all in Chapters 0.1–0.7**,
which import eight named theorems and marked none. All eight are now flagged and `GAPS.md` exists so
it cannot recur silently.

**The standing rule this produced:** an agent that writes a chapter cannot review it. Each part gets
an independent pass before the next begins — one agent per concern, each re-deriving rather than
reading, each reporting to `reports/` rather than editing, so findings are applied in one serialized
pass and nothing is silently clobbered. Three of the errors caught across this build were in *the
plan*, not the book.

## Decisions outstanding

1. **From Chapter 5.8 the ⚑ changes meaning** — from *"I chose not to prove this"* to *"nobody has
   proved this, and physics uses it anyway"* (Haag's theorem; the non-existence of the path-integral
   measure). Ahmed should decide **in print, before Part V**, whether the contract is amended, rather
   than let the mark quietly change register mid-book.
2. **Whether Part III ends at 8 chapters or 9.** 3.7 carries 34 forward debts plus eight planned
   items; the plan recommends a split, and calls it its own weakest recommendation.
3. **Whether to build the Lebesgue integral or ⚑ it.** Three explicit promises in Part 0 depend on
   the answer.

## How to resume

Next batch is **F1: Chapters 3.7 and 3.8**. Write `MATHPLAN-3.7-3.9.md` first — the derivation-by-
derivation plan, in the shape of `MATHPLAN-3.md`, which is why Part III came out well. Extract every
debt naming 3.7 from `GAPS.md` §4 and put it in the writing agent's brief. Chapters from Part III
onward are written **with their plain-terms boxes inline, in one pass, by the same agent**.
