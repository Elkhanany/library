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
