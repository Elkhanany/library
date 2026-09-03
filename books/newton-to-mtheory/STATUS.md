# From Newton to M-Theory — status

*Last updated 29 August 2026, after Chapters 4.8 and 4.9 — Part IV is now nine chapters deep.*

## Where the book stands

**37 of 76 chapters written.** Parts 0, I, II and III complete; Part IV under way at 9 of 20.
**All thirty-seven written chapters are in the plain-language register.** The `clear` tag has therefore
disappeared from the contents list — `build.py` suppresses it once every written chapter carries the
marker, since a badge on every row is decoration rather than information. It returns on its own if
one ever does not.

- 564,115 words · 32,077 typeset expressions · 278 "In plain terms" passages · 189 ⚑ marks
- Every page verified at desktop and phone widths **with all network requests blocked**: zero
  KaTeX errors, zero unresolved cross-references, zero overflow, zero external requests.

| Part | Chapters | State |
|---|---|---|
| 0 · The Toolkit | 0.1–0.9 | complete |
| I · The Action Principle | 1.1–1.4 | complete |
| II · Special Relativity | 2.1–2.6 | complete |
| III · General Relativity | 3.1–3.9 | complete |
| IV · Quantum Mechanics | 4.1–4.9 | 9 of 20 — **4.10 is next** |
| V–VII | — | not started |

## The batch of 29 August: 4.5, 4.6, 4.7

Three chapters, ~59,000 words, written under the six-object cap and then reviewed by five agents that
did not write them: one mathematics pass over 4.7 re-deriving every result in sympy, and one
narrative-flow pass over each of the three.

| | 4.5 · The Spectral Theorem in Infinite Dimensions | 4.6 · The Schrödinger Equation | 4.7 · Wells, Barriers, and Tunnelling |
|---|---|---|---|
| words | 20,300 | 19,200 | 20,100 |
| sections | 11 | 12 | 8 |
| objects | 6 | 7 | 6 |
| ⚑ | 3 | 3 | 1 |
| flow findings | 10 | 14 | 15 |
| maths findings | — | — | 2 BLOCKER · 4 MAJOR · 15 MINOR |

**The two blockers, both in 4.7's worked examples, both confirmed independently before they were
touched.** Worked example 2(b) had the standing-wave displacement as $\theta/k$; it is
$(\pi/2-\theta)/k$. The two agree at $E=V_0/2$ and nowhere else, which is why the error survived: the
chapter's version *diverges* as $E\to0$ where the correct one goes to zero. Worked example 3(b) said
the delta limit is approached with a correction of order $\kappa w$ rather than $(\kappa w)^2$; it is
the other way round, the correction is first order in the width, and the chapter's own three printed
transmissions refute the sentence standing above them.

**The four majors are all of one kind — a true statement standing where nothing proves it.** §1.6's
self-adjointness sweep claimed to cover every potential in §§4–6 and missed the delta, which is the
one Hamiltonian in the chapter whose domain condition best illustrates the chapter's thesis; the
check is now there and is the third of three. §4.4's two-dimensional binding claim was an unflagged
import and is deleted, because the chapter's flag budget is one and it is spent on the experiments.
§2.4's Wronskian argument for non-degeneracy breaks at the nodes of every excited state, which is the
generic case, not a pathology; the missing line is in. And §5.2's wave-packet statement was cited to
`ch4-6` §10, which treats a free particle and never sends one at a step, so it now stands as an
interpretation of the ratio rather than as a result derived here.

**The flow reviews found what no checker can count.** The worst stall in 4.7 was a symbol: $\kappa$
means the decay *inside* the barrier through the whole of §6, and then silently means the decay
*outside* a well in the subordinate clause that opens the chapter's best result. In 4.6 it was the
arrival — the equation the chapter is named after was produced by the last two clauses of a paragraph
about passing a limit through a bounded operator, and nothing read it. In 4.5 it was $\hat U$ carrying
two jobs in the sentence that points at the equation using the other one.

**Three figure defects, none of which any script could see.** The finite-well figure drew odd states
at up to 3.2× their intended height, so at the "six states" preset a wavefunction crossed several
neighbouring levels. Three slider `value` attributes were not aligned to their `step`, so browsers
rounded them and the button marked "on a resonance" landed off resonance; it now reads
$T=1.000000000$. And the highlighted preset at load said "one state" while the readout underneath it
said two.

**The Math Ledger** gained nineteen rows and the last pending entry was discharged: Part IV now
carries 63 objects across seven chapters.

## The batch of 4.8 and 4.9

Written concurrently, then reviewed by four agents that wrote neither: a mathematics pass and a
narrative-flow pass over each.

| | 4.8 · The Oscillator, and the Ladder | 4.9 · Commutators, Uncertainty, and Symmetry |
|---|---|---|
| words | 16,000 | 15,100 |
| sections | 9 | 8 |
| objects | 6 | 5 |
| ⚑ | 1 | 1 |
| maths | 0 BLOCKER · 2 MAJOR · 16 MINOR | 2 BLOCKER · 5 MAJOR · 17 MINOR |
| flow | 10 findings | 24 findings |

**The best catch was in the plan, not the prose, and it was the writer who made it.** The plan's
numerical confirmation for 4.8 was to diagonalise the oscillator on a 60-state truncation and check
the levels come out equally spaced. That test is vacuous: build $\hat H=\half(\hat X^{2}+\hat P^{2})$
out of truncated ladder matrices and the matrix is *identically diagonal* with entries $n+\half$,
because the $\hat a^{2}$ and $\hat a^{\dagger2}$ pieces cancel exactly whatever the truncation. I
confirmed it: the largest off-diagonal entry is $3.6\times10^{-15}$, and the only wrong level is the
top one. The check measured floating-point addition. What 4.8 does instead is a position-space grid
Hamiltonian containing no ladder operator, no Hermite function and no generating function.
**The lesson generalises and is now recorded in the plan: a numerical check built out of the same
algebra as the result is not a check.**

**4.9's two blockers were both in one callout, and both were inferences rather than assertions.** The
box said the product of two spreads "has a floor that no state gets under" — true for position and
momentum, where the commutator is $\ii\hbar\hat I$, and false in general. For spin-1 $\hat L_x,\hat
L_y$ in the $m=0$ state both spreads are $1$ and the floor is exactly zero, which the chapter's own §3.1
and §6.3 rely on. The second was subtler: the box argued that *if* each system carried a true pair
$(x,p)$ *then* some preparation could narrow both marginals, and the next sentence denied the
consequent — handing the reader, by modus tollens, precisely the strong claim the following paragraph
disowned. The conditional is false, and Bohmian mechanics is the standing counterexample. An earlier
pass had removed the assertion and left the inference.

**A third false claim, and a true conclusion resting on it.** Chapter 4.9 §6.5 said there is no
one-parameter family of which parity is a member. There is: let $\hat P_-$ project onto the odd
subspace, and $\varepsilon\mapsto\ee^{\ii\pi\varepsilon\hat P_-}$ is a strongly continuous unitary
group passing through $\hat\Pi$ at $\varepsilon=1$. Verified. The conclusion the section wanted is
sound and now rests on the true reason: the generator is itself a function of parity, so the family
produces no observable that was not already there.

**Two seams were fixed at both ends rather than one.** Chapter 4.5's familiar-ground box asserted in
passing that two observables have no joint distribution beneath them; 4.9 correctly refuses to derive
that from an inequality, so 4.5 now raises the question and leaves it open, and 4.9's three references
to it were brought into line. And Chapter 1.3's Bohr–Sommerfeld ⚑ pointed all of itself at 4.8, which
proves only the oscillator case — exactly, not semiclassically — so it now names 4.10 for the general
statement.

**The Math Ledger** gained eleven rows. Part IV carries 74 objects across nine chapters.

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

---

# Seven interactive figures (19 August 2026)

An audit of all 28 written chapters for places where an **additional** interactive figure would
genuinely illuminate something. Every chapter already had one, so the bar was five conditions, all
required: the insight must live in the *change*; the figure must be **computed, not drawn**; it must
target a difficulty the chapter itself documents (a ⚠ box, or a plain-terms passage visibly
straining); it must not duplicate the existing figure; and it must repay a minute of fiddling with
something durable.

**Twenty-seven candidates were considered and eight survived.** Seven are built. The rejections are
recorded in `reports/figures-part0.md`, `reports/figures-part1-2.md` and `reports/figures-part3.md`,
because the list of what did not clear the bar is the evidence that the bar was applied.

| chapter | figure | what it makes visible |
|---|---|---|
| 0.4 §4.2 | `fig-comm` | The commutator, drawn. A four-leg loop closes at order $\epsilon^{2}$, and the residual over $\epsilon^{2}$ climbs onto $\lvert[A,B]x\rvert$ — 1.9269, 2.0708, 2.0863 against 2.0881. A commuting pair closes to $2\times10^{-16}$ at every $\epsilon$ |
| 0.5 §8 | `fig-joint` | Drive $\lVert[A,B]\rVert$ to **exactly zero** and a standard solver still returns incompatible states, with the spread in $B$ pinned at 0.600000 — because it handed back *an* eigenbasis of $A$ rather than the one $B$ prefers. That is why simultaneous diagonalisation needs a proof |
| 0.7 §2.4 | `fig-wind` | Circulation 6.2831853 round any lopsided loop enclosing the puncture, $-1.9\times10^{-10}$ the moment it does not, with the curl reading zero throughout |
| 1.2 §5 | `fig-conj` | The conjugate point. The number of negative directions equals the number of Jacobi zeros inside the interval — 1 and 1, then 3 and 3 as the trip lengthens. **Morse's theorem, measured** |
| 2.6 §7 | `fig-forbit` | The invariant is not a number that fails to move; it is **the hyperbola the configuration cannot leave**. Set the light-wave preset and the marker slides down the 45° line forever without arriving |
| 3.3 §2.2 | `fig-tworules` | One integrator, two spaces. On the plane the polar components swing from $+0.25$ to $-0.78$ with the Christoffel symbols printed live — and the arrow does not move, closing to $4\times10^{-15}$ degrees. On the sphere the same code returns 45.059816966°, the enclosed area to twelve figures |
| 3.8 §4 | `fig-half` | The deflection integrated three ways against speed. The time-only curve falls towards the space-only curve, which never moves, and they meet at exactly $v=c$. The factor of two is a falling line meeting a flat one |

The 3.3 figure was ranked first for a reason the audit found by grepping: **no script anywhere in
Part III contained the string `Gamma`.** The connection — the central object of the part — had never
been switched on and made to do anything on screen.

The 1.2 figure fixes something worse than an omission. The chapter warns twice that "least action"
is the wrong phrase, and its existing figure demonstrates stationarity on free fall, where the
extremal genuinely *is* a minimum. The reader was told one thing and shown its opposite.

## `figcheck.py`

New. It loads every built chapter at 1280 px and 390 px, in light and dark, exercises **every slider
at three positions and clicks every button**, and then confirms every canvas on the page still has
ink in it and no error reached the console. 28 chapters, 52 canvases, 0 failures. A figure that
throws on load is worse than no figure, and neither the page audit nor the source checks can see it.

---

# Batch F3 — Part IV begins (22 August 2026)

**30 of 67 chapters.** 400,875 words, 24,898 typeset expressions, 227 plain-language passages.

## A change of register, from here on

Set by the reader after twenty-eight chapters: *"the language remains fairly dry. I am OK with that,
but just slightly make it more approachable — run it through the lens of an oncologist with a robust
mathematical background at this point, but still building these concepts from scratch."*

`CONVENTIONS.md` now closes with a section that makes this precise, because the instruction is easy
to over-execute. It is **not** licence to soften the mathematics, add analogies, or merge the main
text into the warmer voice of the plain-terms boxes — those exist so the main text does not have to
do that job, and the two-register structure stays. Four things change: the **motive for each step
goes in front of the step** rather than behind it; connectives replace clipped declaratives; the
reader's daily quantitative fluency may be drawn on **in the main text** where the mathematics is
genuinely identical; and a hard step is named as hard. The forbidden hedges, the ⚑ contract, terse
grind boxes and second person all stand.

The independent review measured it: connective density up to 11.6 per thousand words against about
9 through Part III, motive-before-step throughout, no forbidden hedge in either chapter, grind boxes
still terse. **The instruction's one predicted casualty did materialise** — two clinical analogies
in the main text claimed an identity that was not exact, which is precisely the failure mode this
reader would catch. Both are fixed and both are recorded, because they are the pattern to watch for
in every chapter from here.

## The chapters

| | |
|---|---|
| **4.1** What Classical Physics Cannot Do | ~17,500 words. Four classical failures made *quantitative*. The Planck spectrum by Einstein's A and B coefficients — a route needing no quantum statistics, which do not exist in this book until 4.11. **Stimulated emission is forced by the argument, not added to it**, and the Rayleigh–Jeans law is used as a boundary condition, which is why the classical failure has to be derived in full first |
| **4.2** The Linear Algebra of Quantum States | ~22,000 words. The chapter Part 0 was built for. A 22-row renaming table, each row citing a numbered result in 0.5, plus seven postulates — P1 to P7, each announced in its own box before anything leans on it. The Born rule is named as the first thing in the book posited rather than cornered |

## What the independent verification found

0 BLOCKERs, 4 MAJORs, 14 MINORs, 1 gap in the chain — all applied.

Both chapters survive re-derivation, and the two claims flagged as highest-risk both hold exactly:
$g_1B_{12}=g_2B_{21}$ really does follow from the $T\to\infty$ limit once degeneracies are carried,
and 4.2's own addition — that $\lVert[\hat x,\hat p]-\ii\hbar\hat I\rVert_F \ge \hbar\sqrt{n}$ with
equality **only** for commuting pairs — is correct including the equality condition. That is the
cleanest signal in the part that infinite dimensions are forced rather than chosen.

The four MAJORs are worth recording because two are register failures rather than arithmetic:

- **The mass-action analogy mismapped the one coefficient its section exists to introduce.** It set
  Einstein's $B$ coefficients against $k_{\text{on}}$ and $k_{\text{off}}$; the exact map is
  $B_{12}\leftrightarrow k_{\text{on}}$ and $A_{21}\leftrightarrow k_{\text{off}}$, and $B_{21}$ has
  no mass-action counterpart at all — which is *precisely why* the two-process balance fails to
  close and the third process is forced. In front of a reader who computes $K_D$ for a living.
- **"A rate matrix has real eigenvalues"** — false in general; a three-state cyclic generator has
  complex ones. True for the two-state case the box was discussing, which is now what it says.
- A three-magnet Stern–Gerlach comparison quoting a branch-restricted $\tfrac14$ against a marginal
  $0$, comparing unlike quantities.
- Probability conservation listed on the *proved* side of the chapter's own ledger when §7.1 imposes
  it as a hypothesis and derives unitarity from it.

## Next

**Batch F4: Chapter 4.3**, alone — `PLAN-FORWARD.md` §11 calls it the 3.3 of Part IV. It builds the
space: measure, $L^2$, completeness, and the Fourier basis as an honest orthonormal basis at last.
Then **F5: 4.4**, also alone, which builds the operators on it and is where `GAPS.md` G1's seven
promises finally come due.


---

# The plain-language register — Part I converted (24 August 2026)

The reader's verdict after twenty-eight chapters: *"very dense and theatrical without classical
simplicity that can make deep understanding clear."* He was right, and it was measurable.

| | main text, before | the plain-terms boxes he reads comfortably |
|---|---|---|
| em-dashes / 1,000 words | 12 | 0.9 |
| semicolons / 1,000 words | 5 | 2.0 |
| sentences over 35 words | 11% | 14% |

Sentence *length* was never the problem — the boxes are longer. The problem was **interruption**:
premise, algebraic action and physical consequence packed into one breath with dashes holding them
together, alternating with clipped aphorisms. Plus a second fault the first pilot missed and a
later measurement caught: **8–10% of consecutive equations had no bridging prose at all**, so the
algebra was complete and the thread was not.

## Chapters 1.1, 1.2, 1.3 — converted

| | em-dash/kw | semicolon/kw | >35w | abrupt bridges | length |
|---|---|---|---|---|---|
| 1.1 | 11.9 → **0.2** | 5.2 → **0.3** | 11.0% → **2.8%** | 8% → **0** | 107% |
| 1.2 | 11.7 → **0.5** | 3.8 → **0.2** | 11.4% → **3.8%** | 10% → **0** | 104% |
| 1.3 | 11.9 → **0.5** | 4.3 → **0.1** | 10.9% → **6.2%** | 2% → **0** | 108% |

**The fix is in place, not layered over.** No second copy of any chapter exists. An overlay would be
a second source of truth, and every one of the sixty-odd corrections verification has produced would
then need applying twice.

## The machinery

**`registercheck.py old new`** proves a rewrite changed the prose and nothing else. It compares
equations, headings, ids, `eqref` anchors, canvases, the figure script, ⚑ marks and every
"In plain terms" box byte for byte, then enforces four targets: em-dashes ≤ 1.0/kw, semicolons ≤
2.5/kw, sentences over 35 words ≤ 14%, and abrupt equation bridges ≤ 3%. Headings, callout titles
and figure labels are excluded from the dash count, since a dash in a title is a separator rather
than an interruption.

**The `clear` tag is derived, never declared.** A converted chapter carries `<!--REGISTER:clear-->`
as its first line and `build.py` reads that marker out of the file, so the contents list cannot claim
a chapter was converted when it wasn't.

**`reports/register-sample.md`** holds the reader's own rewrite of Chapter 2.1 §1. It is the binding
specification, and it outranks any rule in `CONVENTIONS.md` that disagrees with it.

## Five real errors surfaced by rewriting

Re-delivering an argument means reading it very closely, which turns things up:

- **1.1** closing summary said failures "(a) and (b)" where the paragraph above contrasts (b) and (c).
- **1.1** Worked example 2 computed escape velocity from $G$ and $M$ separately, which
  `CONVENTIONS.md` forbids. Now uses $GM_{\oplus}$.
- **1.2** §8.1's table put the Dirac action in 5.4 (Distributions and the Propagator) and the
  Polyakov action in 7.3 (Conformal Symmetry). They are 5.5 and 7.2.
- **1.3** attributed the Groenewold–van Hove obstruction to "cubic order" and then illustrated it
  with $\{q^{2},p^{2}\}$, which is quartic. Now says "beyond quadratic", which is what its own
  summary sentence already said.

## Where the register fights the material

Recorded because it decides how the remaining chapters go. Grind boxes carry a third of some
chapters' em-dashes and get **dash-and-semicolon surgery only** — no added warmth, no resequencing,
since they hold algebra the reader opens deliberately. Dense figure captions that inventory several
numerical computations keep their parenthetical rhythm; unpacking every dash there made them longer
and no clearer. And a few equations are pure notation-introduction with genuinely nothing to say
between them, where the bridge has to be built by stating the motive one step earlier than the
original did.

## Remaining

27 chapters unconverted: Part 0 (9), 1.4, Part II (6), Part III (9), 4.1 and 4.2.


---

# Batch F3 — Part 0 in the plain-language register, and thirty-one corrections (24 August 2026)

Nine chapters, 106,718 words of main prose, converted in place by nine agents in parallel. Twelve of
the thirty written chapters now carry the `clear` tag.

| | em-dash/kw | semicolon/kw | >35w | abrupt bridges | length |
|---|---|---|---|---|---|
| 0.1 | 12.21 → 0.72 | 3.28 → 0.96 | 7.6% → 2.5% | 10% → 0 | 124% |
| 0.2 | 9.63 → 0.60 | 4.69 → 0.36 | 10.5% → 6.9% | 8% → 0 | 106% |
| 0.3 | 9.85 → 0.59 | 5.91 → 0.24 | 11.6% → 4.1% | 4% → 0 | 104% |
| 0.4 | 12.11 → 0.19 | 4.76 → 0.19 | 12.3% → 3.7% | 0% → 0 | 110% |
| 0.5 | 10.86 → 0.95 | 4.56 → 0.86 | 8.2% → 4.1% | 2% → 0 | 113% |
| 0.6 | 10.46 → 0.89 | 5.23 → 0.56 | 12.7% → 4.2% | 6% → 0 | 114% |
| 0.7 | 8.78 → 0.42 | 4.57 → 0.14 | 11.6% → 5.1% | 3% → 0 | 103% |
| 0.8 | 12.86 → 0.62 | 4.34 → 0.69 | 10.6% → 3.1% | 0% → 0 | 106% |
| 0.9 | 10.70 → 0.70 | 3.12 → 0.26 | 10.5% → 3.3% | 3% → 0 | 109% |

## The finding that matters more than the register

Converting a chapter means reading every sentence of it closely, and that keeps turning up content
errors eight verification passes did not. **Thirty-one this batch**, all in `reports/part0-corrections.md`.

Fifteen came out of the conversion itself: a tangent triangle placed inside the circle it necessarily
pokes out of; *"both go to zero at the same rate"*, false wherever $f'(a)=0$; a duplicated section
number with two live cross-references to it; twelve significant figures called thirteen; two matrices
said to share no entry that share one; the Cauchy–Schwarz phase chosen with the wrong sign; the Higgs
flat direction placed at the symmetric point, where the Hessian is strictly negative, rather than at
the minimum; a 3×3 Jacobian decomposed into eleven numbers; $Q$ asserted to be exactly what it is
only approximately; a carrier whose sign flipped between a problem and its solution.

Five of those fifteen were **cross-references that resolved to a real chapter about the wrong
subject** — the free-particle propagator attributed to *The Path Integral*, contour integration
attributed to *Vector Spaces and Linear Maps*. That is a class no build error can catch, and it is
invisible to a math review (which checks the derivation) and to a language review (which checks the
sentence), because it lives in the seam between them.

**So `xrefcheck.py` was written**, and pointed at all thirty chapters. It proves every "Chapter N.M"
resolves and prints the 590 distinct source–target pairs beside the title each actually lands on.
Three agents scanned that page and found **sixteen more**, of which the largest was one shared wrong
belief: four chapters sent the reader to 3.3 for the invariant volume element, and `src/ch3-3.html`
contains no $\sqrt{-g}$ and does not use the word "volume". Chapter 3.5 has twenty-three, and 3.5
§6.2 already said *"Chapter 0.6 §8.3 told you this was coming."* `GAPS.md` had even recorded that
debt as paid in 3.5 §6.4 without noticing 0.7's prose still named 3.3.

Two of the sixteen were worse than reader-facing. `debts.py` hands every promise to whoever writes
the target chapter, so **7.1's brief was carrying a requirement to derive the Born–Infeld action**
and **4.5's was carrying a tunnelling barrier**, neither of which belongs in those chapters.

One finding was not a reference error at all. Chapter 1.3 invokes *"the inverse function theorem of
Chapter 0.6"* twice and rests its whole Legendre-transform argument on it; Chapter 0.6 states only
the **implicit** function theorem. The right chapter was named — the theorem was simply never stated
anywhere in the book. It is now stated in 0.6 §8, ⚑-marked, noting its equivalence to the implicit
version quoted in §7.

**The standing recommendation this produces:** run `xrefcheck.py --all` and scan it whenever a part
is finished. It costs about one agent-hour per part, and it is the only check in the pipeline that
looks at whether a promise is about the right thing.

## Remaining

18 chapters unconverted: 1.4, Part II (6), Part III (9), 4.1 and 4.2.

---

# Batch F4 — Chapter 1.4 and Part II converted, and seventeen more corrections (24 August 2026)

Seven chapters, 112,531 words of main prose. **Parts 0, I and II are now entirely in the
plain-language register** — nineteen of the thirty written chapters carry the `clear` tag.

| | em-dash/kw | semicolon/kw | >35w | abrupt bridges | length |
|---|---|---|---|---|---|
| 1.4 | 10.95 → 0.88 | 4.44 → 0.18 | 12.8% → 3.5% | 7% → 0 | 103% |
| 2.1 | 11.61 → 0.89 | 3.69 → 0.25 | 13.8% → 4.4% | 8% → 0 | 103% |
| 2.2 | 14.34 → 0.15 | 4.20 → 0.52 | 10.1% → 3.3% | **16% → 0** | 106% |
| 2.3 | 10.38 → 0.92 | 5.12 → 0.79 | 10.4% → 5.7% | 5% → 0 | 107% |
| 2.4 | 10.98 → 0.90 | 4.16 → 0.18 | 8.9% → 2.5% | 0% → 0 | 105% |
| 2.5 | 11.93 → 0.73 | 5.40 → 0.53 | 11.7% → 3.2% | 8% → 0 | 106% |
| 2.6 | 11.00 → 0.62 | 3.54 → 0.34 | 10.6% → 3.9% | 10% → 0 | 110% |

**Chapter 2.1 §1 is the reader's own prose.** `reports/register-sample.md` is his rewrite of that
section, and it is the specification the whole register was calibrated against. Rather than
paraphrase it, the converting agent installed his text, put the real equations back where his
`[EQUATION]` placeholders were, and restored the eleven things his version passed over — he was
demonstrating a voice, not auditing content. Among them: *"and it is correct"*; Newton's own words
for absolute time; the flag that $t'=t$ is *"put in explicitly so that we can watch it die"*; and the
simultaneity clause inside the physical claim.

**Chapter 2.2 had the worst equation-bridge score in the book** — 16% of consecutive display
equations had nothing said between them. It is one long derivation, two postulates in and the
transformation out, which is exactly the shape where the algebra can be complete and the thread still
drop. Now 0 of 51.

**Chapter 2.4 was the one chapter an earlier review found did not read as the same hand as its
neighbours.** Converting it was the chance to fix that rather than preserve it, and the four tells
are gone: *obviously*, *simply* used to wave past work, the clipped aphorisms (*"Six. Not four…"*,
*"Short section, high yield."*), and the doubled-dash paragraphs.

## Seventeen corrections

In `reports/part1-2-corrections.md`. Four are arithmetic that survived every earlier pass because
the final answer was right anyway or nothing downstream used the number:

- **A satellite number computed at the wrong speed.** 2.2 §2.5 fixes $v=30\ \mathrm{km\,s^{-1}}$,
  then scales $x$ to orbit and reports $0.9\ \mathrm{\mu s}$. Scaling $x$ alone gives
  $6.7\ \mathrm{\mu s}$. The quoted pair is self-consistent but requires a GPS satellite's own
  orbital speed, silently substituted mid-sentence.
- **A factor of $c$ inside one equation.** 2.5 §8.2 defines
  $\vv\beta_{\rm cm}=\vv Pc/P^{0}=c\sum\vv p_i/\sum E_i$; the two halves differ by $c$, and the
  left one is a velocity, not a $\beta$. The right-hand form is what the rest of the section uses,
  which is why it survived.
- **A term count off by sixteen.** 2.4's Problem 3 says relabelling leaves "the same $256$ terms";
  a double sum over two four-valued indices has $16$, which is the $n^2$ the same paragraph claims
  two sentences later. $256=4^4$ belongs to the rank-4 $\epsilon$ in §8.1.
- **"Twelve-odd scalar equations."** Maxwell's four expand to eight. 2.6 §3.2 establishes that itself,
  one section earlier.

Two more were arguments that cited machinery the book does not have. 2.2's §2 preamble said a fourth
condition came from "an overall rescaling of both frames", and no rescaling argument appears anywhere
in the chapter — what actually happens is that condition (ii) yields two equations, because a light
pulse can go either way along $x$. And 2.1 attributed Michelson's 1886 drag measurement,
$0.434\pm0.02$, to Fizeau in 1851, who agreed with Fresnel only to within a few per cent.

The same two categories dominate as last batch: **five cross-references or section numbers**, and
**four counts stated in prose about equations that are themselves correct**. Both survive a
mathematics review, which checks the derivation, and a language review, which checks the sentence,
because they live in the seam between them.

## `tagcheck.py` now checks block balance

An unclosed `<p>` had been sitting in Chapter 2.6's §5 grind box since it was written. HTML5 closes
it implicitly at the next `<p>`, so the page rendered correctly and no rendered-page audit could see
it — the same invisibility as the unescaped `<` that produced `tagcheck.py` in the first place. It
was found only because a converting agent counted opens against closes as a private self-check.

That count is now in `tagcheck.py`, across twenty-three element types. The whole corpus balances
exactly, so it is enforcing rather than advisory from the start, and putting the missing `</p>` back
makes it fire.

## Remaining

None. The conversion is finished.

---

# Batch F5 — Part III, 4.1 and 4.2, and the conversion finished (24 August 2026)

Eleven chapters, 163,688 words of main prose, converted in place by eleven agents in parallel. **The
whole written book is now in the plain-language register.**

| | em-dash/kw | semicolon/kw | >35w | abrupt bridges | length |
|---|---|---|---|---|---|
| 3.1 | 7.98 → 0.59 | 3.94 → 0.20 | 11.8% → 4.7% | 9% → 0 | 106% |
| 3.2 | 8.13 → 0.78 | 2.98 → 0.22 | 9.1% → 4.8% | 3% → 0 | 103% |
| 3.3 | 5.66 → 0.81 | 4.49 → 0.72 | 10.0% → 6.1% | 7% → 0 | 108% |
| 3.4 | 7.11 → 0.83 | 4.23 → 0.37 | 9.7% → 4.9% | 7% → 0 | 104% |
| 3.5 | 8.32 → 0.66 | 3.77 → 0.59 | 10.2% → 4.5% | 5% → 0 | 106% |
| 3.6 | 7.43 → 0.62 | 4.38 → 0.27 | 9.8% → 2.6% | 8% → 0 | 107% |
| 3.7 | 8.25 → 0.68 | 5.58 → 0.38 | 13.3% → 7.2% | 3% → 0 | 101% |
| 3.8 | 7.52 → 0.57 | 5.04 → 0.95 | **18.5% → 7.7%** | 3% → 0 | 103% |
| 3.9 | 7.45 → 0.44 | 5.03 → 0.31 | 12.6% → 4.7% | 3% → 0 | 102% |
| 4.1 | 8.10 → 0.13 | 5.22 → 0.07 | **16.7% → 4.7%** | 10% → 0 | 101% |
| 4.2 | 8.78 → 0.74 | 6.21 → 0.53 | **18.2% → 3.9%** | 0% → 0 | 102% |

The three chapters with the worst long-sentence rates in the book were 3.8, 4.1 and 4.2 — all
between 16.7% and 18.5% of sentences over 35 words. All three are now under 8%.

**4.1 and 4.2 were different from the rest.** They were written under the earlier, intermediate
instruction — *"slightly more approachable, through the lens of an oncologist with a robust
mathematical background"* — so they already put the motive before the step in many places and
already drew on clinical fluency in the main text. The brief told both agents not to undo any of
that: punctuation and equation bridges only, no change of stance, and above all **no new clinical
analogy and no extension of an existing one by so much as a clause**, since the failure mode there
is an analogy that is nearly right in front of a reader who computes $K_D$ for a living. Both held
the line; 4.1 came out at 0.13 em-dashes per thousand words, the lowest figure in the book.

## The tag has retired itself

`build.py` now suppresses the **clear** tag whenever every written chapter carries the marker, and
brings it back the moment one does not. A badge on all thirty rows is decoration rather than
information. Chapters keep writing `<!--REGISTER:clear-->` as line 1 — it costs one line and it is
what makes the suppression honest. `CONVENTIONS.md` now states that this is the book's register
rather than a variant, and that 4.3 onward are written in it from the start.

## Twenty-three corrections

In `reports/part3-4-corrections.md`, together with the nineteen items examined and deliberately left
alone. Forty-two were reported; each was re-verified before anything was touched. The ones worth
knowing:

- **3.1's electron charge-to-mass ratio lost its minus sign**, in a list that is otherwise signed and
  in a chapter whose own §8.1 table gives it correctly as $-1.7588	imes10^{11}$.
- **3.2 §8.4 contradicted its own Worked example 2** about where the centrifugal term comes from.
  The worked example is right: the term survives the change of basis, because $\partial_r$ and
  $\partial_	heta$ commute, and its real source is the connection.
- **3.4's Weyl box stated conformal invariance for the wrong index placement.** It holds for
  $C^{
ho}{}_{\sigma\mu
u}$; the fully lowered form picks up $\Omega^2$.
- **3.6 could not agree how many sign traps it has** — the opening announces two, §5 calls one "the
  second of the two" and mentions a third, and §6.1's box is titled "The third sign trap".
- **3.8 gave a time the units of a distance.** The Rindler characteristic time $c/a$ is about a
  *year* at $a=g$; the light-year is $c^2/g$, which is where the horizon sits, and which is what
  Chapter 3.1 §6.1 actually says.
- **3.9's counterexample for homogeneous-but-not-isotropic was a cone**, which is flat away from its
  apex — as this book uses it elsewhere — hence locally isotropic, and is not homogeneous in the
  section's own sense either. Now the infinite cylinder.
- **4.1's Problem 1(d) named the wrong one of its two ingredients**, which inverted the conclusion
  its own parts (a) and (b) had set up.

**One flag was a false positive**, and it is recorded as such so nobody re-spends the hour: 3.8's
`fig-half` caption uses coefficients $1.18$ and $pprox3$ for two quantities that genuinely differ
— the residual in a ratio, and the gap in the total deflection. Both are right.

## Where the errors were, across all three conversion batches

| batch | items fixed | cross-refs & section numbers | counts in prose | arithmetic | logic |
|---|---|---|---|---|---|
| Part 0 | 15 | 5 | 3 | 2 | 5 |
| 1.4 + Part II | 17 | 5 | 4 | 4 | 4 |
| Part III + 4.1–4.2 | 23 | 3 | 5 | 5 | 10 |

**Fifty-five corrections across 383,000 words**, none catchable by a build error, and almost none
changing a final answer. That is the signature of the class: they survive because the derivation is
right and the sentence about it is wrong, and no reviewer looks at both at once. It is also the
argument for reading a chapter closely enough to re-say it — which is what a register pass is, and
what no review had previously required.

## Next

**Batch F6: Chapter 4.3**, alone — `PLAN-FORWARD.md` §11 calls it the 3.3 of Part IV. Measure, $L^2$,
completeness, and the Fourier basis as an honest orthonormal basis at last. It is the first chapter
written in the plain-language register from the start, so `registercheck.py`'s four targets should be
checked against it before it ships rather than after.

Then **F7: 4.4**, also alone, where `GAPS.md` G1's seven promises come due.


---

# Batch F6 — Chapter 4.3, and the writing pipeline tested (25 August 2026)

**Chapter 4.3, Function Spaces: Measure, $L^{2}$, and Completeness.** ~19,300 words of main prose,
54 numbered equations, 4 grind boxes, 3 worked examples, 5 problems, one two-canvas interactive,
plain-terms boxes 4.3.1–4.3.8, exactly two ⚑.

This is **the first chapter written in the plain-language register from the start** rather than
converted into it, so it is also the first test of `reports/writing-brief.md` and of the flow-review
pass. Both worked. The chapter came in at 0.36 em-dashes and 0.10 semicolons per thousand words —
better than any converted chapter — with 0% abrupt equation bridges and 7.4% of sentences over 35
words, all on the first draft.

It collects the oldest outstanding promise in the book. Chapter 0.2 said the integral would be
thrown away and rebuilt; 0.5 said its abstraction was "the entire reason Chapter 4.3 is possible";
0.9 flagged completeness as quoted. Fifteen promises from six chapters named this chapter and all
fifteen are paid, one of them in a weaker form than its wording, with the shortfall stated in print.

## The writer found three errors in my plan

The most important is **build item 3**, which would have hollowed out the chapter's central payoff.
The plan said to use Chapter 0.2's own sequence $f_n$ — equal to 1 at $q_1,\dots,q_n$ — as the
Cauchy sequence with no Riemann-integrable limit. But $f_n$ and $f_m$ differ on a **finite** set, so
$\lVert f_n-f_m\rVert_2=0$: every $f_n$ is the same vector in $L^{2}$, namely zero, which the
Riemann class already contains. It shows the seminorm failure and the non-closure failure and **not
incompleteness at all**, so item 12's "watch the exact sequence from item 3 now converge" would have
been a payoff with nothing behind it.

The chapter as written uses 0.2's sequence for the two failures it genuinely shows, says out loud
that it is too thin for the third, and then *thickens* 0.2's own enumeration into indicators of small
intervals around each rational — whose limit $\mathbf 1_U$, with $\abs U\le\tfrac14$, is genuinely
not Riemann integrable. The reader still recognises 0.2's construction, which was the point.

Also: **item 13's stated source is impossible** (no non-zero polynomial is in $L^{2}(\R)$, so
polynomials cannot be dense in it — that is Weierstrass on a compact interval, a different space),
and **item 17's instruction to strike Chapter 0.9's flag contradicts the book's own convention**,
which is that a ⚑ stays at the point of use and names the chapter that proves it. Chapter 0.7 §7.3's
Poincaré lemma is still flagged today and was proved in 3.5. All three are now recorded in
`MATHPLAN-4.md` beside the items that were wrong.

**That is eight planning errors caught by agents across this build, and still zero errors reaching a
reader.**

## What the three verification passes found

Per the standing rule, none of them wrote the chapter.

**Mathematics — 2 BLOCKERs, 0 MAJORs, 11 MINORs.** Both blockers were real and both were confirmed
here at 30 digits before being fixed:

- Worked example 2(d) printed $E(N)\sqrt{N+1}$ while claiming $E(N)\sqrt N$ — and the figure computes
  $E\sqrt N$, so a reader moving the slider to the quoted $N$ would have seen different numbers than
  the worked example claimed. The passage now gives the right numbers and names the
  $\sqrt{N/(N+1)}$ deficit, which is still half a per cent at $N=101$.
- Worked example 3(d) claimed a window $[-R,2R]$ makes the Cauchy mean diverge. It gives
  $\tfrac{a}{\pi}\ln 2$, finite. Every linear family $[-R,cR]$ gives the finite $\tfrac a\pi\ln c$;
  divergence needs a super-linear family such as $[-R,R^{2}]$. Both facts are now in the text, and
  the point being made is stronger for it.

**Narrative flow — the new pass, run for the first time, and it earned its place.** Thirteen findings,
of which two were things no other check could have caught: §6.2 stated a true claim and then
supported it with a pointer to §8.4 that says the opposite, and §8.5's heading and body asserted
"two orthonormal bases" three lines above a ⚠ box saying "they are not, and nothing above claims they
are". It also caught a physics error inside an analogy — that $\abs\psi^{2}$ "determines everything
measurable" about $\psi$, which the same chapter's §8.5 refutes by building $\abs{\tilde\psi}^{2}$.

**Cross-references — 4 wrong out of 151 outbound, 54 cross-chapter section pointers and 158 internal
ones.** All four were section- or equation-level: Cauchy–Schwarz cited as (0.5.9) when it is (0.5.6),
the triangle inequality attributed to 0.5 §1.3 rather than §1.4, a verbatim quotation located in a
grind box when it lives in a problem solution, and one internal pointer naming §4.2 for work done in
§4.1.

## Three document reconciliations, adjudicated with evidence

- **`GAPS.md`'s Fubini row** routed Chapter 0.2's mark to 4.3. It should not: Fubini needs *product*
  measure, a second construction beyond the one 4.3 quotes, and 4.3 §4.1 declines it in print. Now
  **Permanent, correctly**, which is the same status the register already gives 0.6's implicit
  function theorem and 0.8's Picard–Lindelöf.
- **`MATHPLAN-4.md`'s Part IV debt table was stale in all eleven rows** — 119 promises when written,
  **242** now. Subtracting the contributions of 4.1, 4.2 and 4.3 reproduces every original number
  exactly, creditor breakdown included, so the table was right and simply never regenerated. It now
  says to regenerate it after every batch. Worth knowing before 4.11 is written: it was planned as a
  light-debt chapter at 2 and is now carrying **25**, nineteen of them from 4.2 alone.
- **`xrefcheck.py` could not see ranges.** Its separator list omitted *to*, so "Chapters 4.5 to 4.7"
  counted as one reference to 4.5 and the 4.7 was invisible. Fixed, and the census moved by 12.

## Next

**Chapter 4.4, Operators in Infinite Dimensions**, alone. It is where `GAPS.md` G1's seven promises
come due, and it now carries 25 inbound promises rather than the 9 the plan recorded — seven of them
from 4.3, written this batch. Run `python3 debts.py 4.4` into the writing brief before starting.

The one decision still outstanding, and it should be made in print before Part V: from Chapter 5.8
the ⚑ changes meaning, from *"I chose not to prove this"* to *"nobody has proved this, and physics
uses it anyway."*

---

# Batch F7 — Part IV re-planned at six objects per chapter (26 August 2026)

**Part IV goes from 11 chapters to 20; the curriculum from 67 to 76.** Nothing is dropped and nothing
is added but three objects the written text had already promised and no build item covered.

The reader, after reading 4.1–4.3: *"I value now slow (very slow one by one) pace than intense pace
that feels like running around."* Counting new objects per chapter — an object being what earns a
Math Ledger row — Part 0 runs 5–8, Parts I–III run 3–10, and Part IV as written runs **12–13**.
Chapter 4.3 alone introduces thirteen. The chapters were not badly written. They were too big.

| old | objects | becomes | objects each |
|---|---|---|---|
| 4.4 Operators in Infinite Dimensions | 12 | 4.4 Domains, and the Adjoint's Domain · 4.5 The Spectral Theorem in Infinite Dimensions | 6 · 6 |
| 4.5 The Schrödinger Equation | 8 | 4.6, unsplit | 7 |
| 4.6 Systems You Can Solve in One Dimension | 11 | 4.7 Wells, Barriers, and Tunnelling · 4.8 The Oscillator, and the Ladder | 6 · 6 |
| 4.7 Symmetry, Commutators, and the Classical Limit | 9 | 4.9 Commutators, Uncertainty, and Symmetry · 4.10 The Classical Limit | 5 · 5 |
| 4.8 Angular Momentum and Spin | 12 | 4.11 The Angular Momentum Algebra · 4.12 Spin, Orbitals, and Adding Angular Momenta | 6 · 6 |
| 4.9 The Hydrogen Atom | 10 | 4.13 The Hydrogen Atom · 4.14 The Degeneracy, and $SO(4)$ | 6 · 4 |
| 4.10 Perturbation Theory and Transitions | 12 | 4.15 Perturbation Theory · 4.16 The Fine Structure of Hydrogen · 4.17 Transitions | 4 · 4 · 6 |
| 4.11 Identical Particles, Entanglement, and Measurement | 14 | 4.18 Identical Particles · 4.19 Density Matrices and Entanglement · 4.20 Bell, Decoherence, and What Is Settled | 5 · 5 · 4 |

Mean 5.4, and the only seven is 4.6, whose seventh object is three lines from 4.5's spectral theorem.
⚑ budget unchanged at 51. Every one of the seventeen carries inbound promises; none is orphaned.

## The re-aim, and what my own premise got wrong

I proposed splitting so that **the first piece keeps its number**, expecting that to protect most of
the 171 promises naming 4.4–4.11. It protects **six**. A shift renumbers every chapter after the
first split whether it split or not, so 165 of 171 needed an edit — my estimate was out by a factor
of eight. The bill was still worth paying, and the corollary is the useful part: **the renumbering
cost is paid in full at the first split**, so there is no reason to split conservatively. That is why
the plan takes seventeen chapters rather than the fourteen I guessed.

The real cost was **23 sentences rewritten** — thirteen widened to name two chapters, six split so
different clauses point at different ones, four re-aimed to a different subject. The other 142 were
decided substitutions. Six agents worked disjoint file groups so no two touched the same file, each
locating every span against the original text and applying in descending offset order, because
old 4.5 → 4.6 and old 4.6 → 4.7 in the same pass and a sequential replace would have silently sent
everything that was 4.5 to 4.7.

## Four kinds of reference no checker could see

Each had already produced a real error that survived an earlier renumbering.

1. **A number ending a sentence.** `xrefcheck`'s ledger pattern ended `(?![\d.])`, which rejects a
   following full stop — so *"…cannot be written down until 4.11."* was invisible. Three real
   references sat in that blind spot. The lookahead is now `(?![\d])(?!\.\d)`, and the ledger's
   visible reference count went 809 → 859.
2. **A bare number in chapter prose.** *"Density matrices (4.11)"* in a table cell, *"re-derived in
   4.11 from the other side"* in a closing brick. `debts.py` requires the literal word "Chapter";
   `xrefcheck` read bare numbers only in the ledger. Three found and re-aimed.
3. **A plural run.** *"Chapters 4.5, 4.6 and 4.8"* — `debts.py` saw only the first. This was found
   yesterday and fixed; it accounts for much of why the census moved 242 → 372 → **420**.
4. **"Section 4.5".** Neither the word Chapter nor a §. Both instances turned out to be genuine
   own-chapter references, but nothing in the toolchain could have told the difference.

`xrefcheck.py --bare` now lists every cross-part bare number in chapter prose for a human — 56 of
them, all real chapter references written without the word "Chapter". It is advisory, because it
cannot decide which are pointers and which are measured values, and a check that guesses is worse
than one that lists.

## GAPS.md was carrying two numbering schemes at once

Commit `f8006d2` renumbered Part IV from eight chapters to eleven and re-aimed 360 references across
55 files. It never touched `GAPS.md` or `PLAN-FORWARD.md`. So `GAPS.md` §2's column was on the
eleven-chapter numbering while §4's census was still on the eight-chapter one, and each hit had to be
identified before it could be remapped.

Worse: **G1, the book's largest single debt, pointed all seven of its promises at Chapter 4.3, which
is written and pays three of them.** The spectral theorem, continuous spectra and the plane-wave gap
are not 4.3's and never were. Three/four split, now recorded with a *Due at* column. G11 had the
same defect.

And §0's maintenance instruction was `grep -o 'Chapter [4-7]\.[0-9]'` — one digit. Against a Part IV
running to 4.20 that silently truncates *Chapter 4.20* to *Chapter 4.2* and files the debt against a
written chapter. Replaced with `python3 debts.py --census`, which is what the register should have
been regenerated from all along. Current census: **420**.

## Next

**Chapter 4.4, Domains, and the Adjoint's Domain** — six objects, ※ mathematics, and the first
chapter written under the cap. `reports/writing-brief.md` carries the cap, the sitting breaks and
`\ann`. Run `python3 debts.py 4.4` into the brief; it now returns 18, not the 9 the old plan
recorded.

---

# Batch F8 — Chapter 4.4, and the cap tested (28 August 2026)

**Chapter 4.4, Domains, and the Adjoint's Domain.** ~15,600 words, nine sections, two ⚑, six new
objects — the first chapter written under the pacing cap.

**The cap worked, and the measurement says so.** Six objects at about 2,600 words each, against
Part IV-as-written's twelve and thirteen at 1,600. The flow review, which reads the chapter cold
against 4.3, put it plainly: §5 spends 3,098 words asking one question of one operator three times,
and *"the reader is never asked to hold two unfamiliar things at once."*

The chapter's pedagogical bet is the ordering. §5 takes $\hat p=-\ii\hbar\,\dd/\dd x$ on three
intervals and gets three different answers from integration by parts alone — nothing quoted anywhere
in the section. Only then does §6 state von Neumann's classification, so the flag is discharged into
arithmetic the reader has already done, and the three cases come out $(0,0)$, $(1,1)$, $(1,0)$,
matching §5 exactly. The review's verdict: *"the moment the bet visibly wins is §6.3's final
paragraph, where the theorem stops being quoted and becomes something the reader owns."*

## What the cap nearly bought instead

The flow review found the failure mode `CONVENTIONS.md` had warned about in the abstract, and it was
real. **Scaffolding — roadmaps, plain-terms boxes, the brick — reached 25.2% of the chapter against
4.3's 21.1%.** The body shrank 30% and the restatement apparatus only 12%, so a quarter of the
chapter had become the chapter talking about itself. The three-interval result was stated **nine
times**, and the chapter explained its own pedagogical strategy three separate times. Trimmed to
22.8%.

**And the slack was unevenly spent.** §5 makes about six moves in 3,098 words; §7 made about
fourteen in 2,073 — four times the density, after the last sitting break, thirteen thousand words in.
Three of the review's other findings all fell in that stretch. §7 was given room and a sitting break
added at §6|§7, which is the chapter's largest change of subject.

That is the lesson for the remaining sixteen chapters of Part IV: **the cap counts objects, and
objects can crowd into one section while the chapter's average looks fine.** Density per section is
what the flow review should keep measuring.

## What the two independent passes found

**Mathematics — 1 BLOCKER, 2 MAJORs, 5 MINORs**, all applied.

- **The blocker.** Problem 3(d) said the phase relabelling $\hat U\psi=\ee^{\ii\theta x/L}\psi$
  *"does not commute with position, so it changes what the state says about where the particle is."*
  Both clauses are false, and I confirmed all three facts in sympy: $\hat U$ and $\hat x$ are both
  multiplication by a function, so $[\hat U,\hat x]=0$ exactly; $\abs{\hat U\psi}^2=\abs\psi^2$
  pointwise, so it changes *nothing* about position; and it is **momentum** that fails to commute,
  which is what part (c) had just proved. A reader who checked the one-line commutator — which this
  chapter trains them to do — would have found the book asserting something false.
- **§7.2 never said which operator it was extending**, in a chapter whose §6.3 insists, in bold, that
  you must. The only prior meaning of "minimal" was §5.4's, and that operator is Dirichlet, which
  §7.2's own bullet list calls self-adjoint — so the reader reached a flat contradiction four lines
  later. The operator that actually works needs all four boundary values zero, and that domain was
  never written down.
- **Worked example 2(d) contradicted §5.4** — it claimed no momentum observable exists on half a box,
  where §5.4 proves a whole circle of them exists on any bounded interval.

**Flow — 13 findings**, including that the second `\ann` did not earn its place (the label repeated
a sentence the reader had read sixty words earlier, on a display with nothing to disambiguate) and
that §6.3's endpoint heuristic was silently broken by §7 and never repaired. One annotation now, not
two, which is the intended frequency for the device on its first outing.

The review also confirmed the chapter reads as the same hand as 3.6 and 4.2, and singled out §5.5's
closing paragraph — which pays off §1's fourth item after eight thousand words and re-glosses its
symbol in the same breath — as the best writing in it.

## Next

**Chapter 4.5, The Spectral Theorem in Infinite Dimensions** — six objects, ※ mathematics, and where
`GAPS.md` G1's four remaining promises come due. `python3 debts.py 4.5` returns 29. It also owes the
other half of 0.5's *"the bill comes due"*, which 4.4 §1 announced as a two-chapter payment.