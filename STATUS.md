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

---

# Batch F1 — Chapters 3.7 and 3.8 (18 August 2026)

**Part III is now nine chapters.** Chapter 3.7 was carrying 34 forward promises from four earlier
chapters plus eight planned derivations; `PLAN-FORWARD.md` §4 argued for the split and it was taken.
The division is where the physics divides: everything in 3.7 is a timelike geodesic in an effective
potential, everything in 3.8 is null or about causal structure.

| | |
|---|---|
| **3.7** | Schwarzschild: The Solution and Its Orbits — 15,800 words, 73 equations |
| **3.8** | Light, Redshift, and What a Horizon Is — 17,900 words, 71 equations |
| **3.9** | Cosmology, and a Loose Thread — 18,500 words, 62 equations |

All 393 forward references were re-aimed in the same pass, and the section numbers those references
cite are fixed by `MATHPLAN-3.7-3.9.md`. The debt load on the old 3.7 is now 22 and 12.

## What the independent verification found

Per the standing rule, an agent that did not write the chapters re-derived everything. Every
symbolic result reproduced exactly — the nine Christoffel symbols, the $(AB)'=0$ collapse, Birkhoff
genuinely derived rather than sketched, the ISCO, $\omega^2$, the photon sphere, the exactly-zero
first-order null residual, the two-halves split of the deflection, the Kretschmann scalar, both null
slopes. **The signature never slipped.**

It found **3 BLOCKERs and 4 MAJORs**:

- Three wrong printed numbers — two metre-to-kilometre conversions done as $\div10^{6}$, and a
  proper time out by a factor of ten.
- **Four unescaped `<` characters that silently deleted text from the rendered page.** HTML5 opens a
  tag whenever `<` is followed by a letter, so `$r<r_{+}$` swallowed everything to the next `>`. One
  site removed the sign analysis identifying which root is the orbital maximum; another removed part
  (c) of a problem. Nothing looked wrong: no error, no warning, just missing sentences. The review
  caught two; a parser sweep written in response caught two more.
- A stated error bound that would have destroyed the chapter's own headline result — it justified
  dropping a quadratic term by a first-order argument, admitting a 4″ error where the text then
  compares against $42.98\pm0.04$. The real argument is that a quadratic term averages to zero over
  a cycle and shifts the frequency only at second order; numerically the formula is good to
  $2.7\times10^{-8}$.

Plus sixteen minors, mostly cross-references pointing at sections that do not say what was claimed.
All applied.

**`tagcheck.py` is new and now runs as the first step of `verify.py`.** It parses every chapter with
a real HTML parser and fails the build on any `<` that a browser would read as a tag. That class of
fault is invisible to a rendered-page audit, because by the time you measure the page the text is
already gone.

## Two corrections to my own plan, worth remembering

Both writing agents independently caught the same error: the plan computed $G\times M_{\odot}$ where
it should have used the measured $GM_{\odot}$. $GM_{\odot}$ is known to ten significant figures and
$G$ alone to five, so multiplying discards five digits — enough to move Mercury by 0.01″ and the
solar deflection by 0.0004″, on exactly the two numbers a reader checks against a measurement.
`CONVENTIONS.md` now carries the rule. The plan also said eight Christoffel symbols where there are
nine.

That is now **five planning errors caught by writing or reviewing agents across this build**, and
zero errors that reached a reader. The pipeline is the product.

---

# Batch F2 — Chapter 3.9, and Part III closed (19 August 2026)

**Part III is complete: nine chapters, 28 of 60 written.** 360,000 words, 22,616 typeset
expressions, 210 plain-language passages.

Chapter 3.9 derives the FLRW metric from the cosmological principle stated as a Killing-vector
condition, gets Friedmann I from $G_{00}$, and then makes the point the chapter exists for: the
acceleration equation follows from the $11$ component **only after Friedmann I is substituted**, and
differentiating I and subtracting II leaves exactly the fluid equation. That is the contracted
Bianchi identity of 3.6 in cosmological clothes — the same structural fact the reader has already
met once.

Its thesis is §6: **energy is not conserved in an expanding universe**, presented as a consequence of
a theorem the reader proved himself rather than as a curiosity. It collects the oldest promise in the
book, made in Chapter 1.1 and repeated in 1.4 §4.3 and 3.5 §9.

## What the independent verification found

0 BLOCKERs, 4 MAJORs, 16 MINORs. Every symbolic result reproduced exactly — thirteen FLRW
Christoffels, Friedmann I with every factor of $c$ intact, the Bianchi combination including its
sign, an honest separable ODE for the constant-curvature classification, the Einstein-static
perturbation, and all three worked constructions with residual exactly zero.

**The most important finding is a logical one.** §6.3 — the chapter's central argument — ran Noether's
theorem in the direction it does not run: *no symmetry, therefore no conserved energy* is denying the
antecedent, and licenses nothing. The book proves the converse it actually needs, at Chapter 1.4
§7.2, and the chapter never picked it up. A conserved energy would *generate* a time translation,
that translation would be a timelike Killing vector, and §6.2 proves there is none. The section now
runs that way, with a scope note that the converse is a statement about Hamiltonian systems and that
what rules out a global energy is §6.5's later tiers.

Also: an age bound applied to a universe that violates its own stated hypothesis ($p\ge0$, in a
universe that is 68.5% cosmological term); a figure caption naming a slider preset that produces a
different curve from the one described; and a wrong printed integrand.

## The Part III reunification pass

72 plain-language passages read end to end with no chapters. **Part III holds as one essay**, and the
three new chapters read as the same hand — they clear all four of the tells that caught Chapter 2.4
earlier in this build. Nineteen repairs applied. The three that mattered:

- **The 3.6→3.7 seam** — the point where the part stops building machinery and starts spending it,
  and no passage said so. 3.6 closes by saying exact solutions are rare; 3.7 immediately produces
  one, unremarked.
- **The plain layer never said the universe is observed to expand.** Every passage from 3.9.3 on
  assumed it. A reader of the plain layer alone got all of cosmology's machinery and its conclusion
  without ever being told that distant spectra arrive reddened.
- **3.8.8 promised to name the assumption carrying the weight and then named it only in the main
  text**, losing the sentence that ties 3.8 to 3.9.

Two motifs were revived in their canonical words, and the Through-Line's closing passage — which
still said Part III stopped at six chapters of eight — now closes the part properly.

## Next

**Batch F3: Chapters 4.1 and 4.2**, the first of Part IV. Before it starts, three things
`PLAN-FORWARD.md` §11 says must happen first, not during:

1. **Write `MATHPLAN-4.md`.** The Part III experience is the evidence: the plan is why it came out well.
2. **Renumber Parts IV–VII in `build.py`** to the revised curriculum, and **remap the forward
   references** — roughly half of the 393 are invalidated by it. One scripted pass with a
   hand-checked mapping table, before Part IV is written rather than after.
3. **Extract the per-chapter debt list** from `GAPS.md` §4 into each chapter's brief. Five-line
   script, and the highest-value process change available.

And one decision to make in print before Part V: from Chapter 5.8 the ⚑ changes meaning, from *"I
chose not to prove this"* to *"nobody has proved this, and physics uses it anyway."*

---

# Before Part IV — the three prerequisites (19 August 2026)

`PLAN-FORWARD.md` §11 said these had to happen before batch F3, not during it. They are done.

## 1 · `MATHPLAN-4.md`

The binding derivation plan for all eleven chapters of Part IV: 17,500 words, **313 numbered build
items**, a fixed section list per chapter so forward references can be pinned to it, and an explicit
⚑ budget per chapter — 51 for the part, of which exactly one is a substantial mathematical flag.

That one is the spectral theorem for unbounded self-adjoint operators, and `GAPS.md` G1's proposal
is taken: state it in multiplication-operator form and then **verify it by hand on the only three
operators the book ever applies it to** — position, momentum via Fourier, and the oscillator
Hamiltonian via Hermite completeness. The reader ends holding a quoted theorem they have personally
checked everywhere it is used, which is the best available outcome.

**G1 and G3 close entirely** in Part IV. **G2 is explicitly declined** — the plan found a route to
Hermite completeness needing only dominated convergence and Plancherel, so no contour integral
appears anywhere in Part IV and complex analysis waits for 5.4, where it is built properly.

The plan verified its own physics before specifying it — the ladder algebra, su(2) and the 720°
spinor sign, the hydrogen spectrum and its $n^2$ degeneracy, **all five Runge–Lenz identities
symbolically**, Rayleigh–Schrödinger to second order, the fine structure against the measured
10.969 GHz, and the CHSH bound. On that last one it caught its own first draft: the commonly quoted
angles $(0°, 90°, 45°, -45°)$ give **exactly zero**, not $2\sqrt2$. Independently confirmed here.

## 2 · Parts IV–VII renumbered, and 360 forward references re-aimed

`build.py` now carries the revised curriculum: **67 chapters, 23 of them mathematics.**

The remap was the delicate part, because **two pairs of chapters exchange places** — the path
integral and the Feynman rules (old 5.8 and 5.6), and conformal symmetry and the bosonic string
(old 7.2 and 7.3) — and four old chapters split in two. A mechanical find-and-replace would have
produced plausible-looking nonsense in every one of those cases. Each of the 187 changed references
was read in its own sentence and decided on content: old 4.3 split 8/9 between the new 4.3 and 4.4,
old 4.5 split 17/3/2 across 4.6, 4.9 and 4.10, old 5.9 split 7/10 between 5.10 and 5.11. Nine
references promising contour integration or the $i\epsilon$ prescription were pulled into the new
5.4, which is `GAPS.md` G2's hole finally getting an owner.

Census conserved exactly: **360 before, 360 after**, no reference naming a chapter outside the
curriculum.

## 3 · `debts.py`

`python3 debts.py 4.3` prints every sentence in the written book that names Chapter 4.3.
`--census` counts them all. Each writing brief from here on carries its chapter's extracted debt
list, which turns 360 hopes into 360 requirements — `GAPS.md` §7 called this the highest-value
process change available, and it is nine lines of code.

## Corrections found along the way

Both agents found errors in my own planning, which is now the norm rather than the exception:

- **The particle in a box does not have a one-parameter family of self-adjoint extensions.** Its
  deficiency indices are $(2,2)$, so the extensions form $U(2)$ — four real parameters. The
  one-parameter family belongs to *momentum on an interval*, indices $(1,1)$. Confirmed here.
- **The book has never defined a Cauchy sequence** — `grep` across 28 chapters finds only
  Cauchy–Schwarz, the Cauchy distribution and Cauchy's functional equation. 4.3 must define
  completeness from scratch rather than cite it.
- **The canonical commutator was routed to 4.7 but is needed by 4.5, 4.6 and 4.8.** It is introduced
  in 4.2, as a postulate in its own box.
- Batch F8 was two chapters; 4.10 is the largest chapter in the part and now runs alone.

## Next

**Batch F3: Chapters 4.1 and 4.2.** Everything they need is in place.
