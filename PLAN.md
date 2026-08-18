# From Newton to M-Theory
## A Build-It-Yourself Book — Architecture & Curriculum Plan

*Version 2.0 — 15 Aug 2026 — math foundation deepened*

> **Superseded forward of Chapter 3.7.** This document remains the plan of record for Chapters 0.1
> to 3.6, all of which are written. From 3.7 onward it is superseded by
> [`PLAN-FORWARD.md`](PLAN-FORWARD.md), which revises the curriculum from 59 chapters to 67 after
> the review of August 2026, and by [`GAPS.md`](GAPS.md), the standing register of what the book has
> used but not built. Read those two before writing anything after 3.6.

---

## 0. The premise

You can grasp anything, but you refuse to be handed a result you can't derive. So the rule for this
entire book is:

> **Nothing is asserted that hasn't been built.** No "it can be shown that." No magic constants.
> No borrowed intuition standing in for a calculation.

That rule has a price: the book is long, and the physics doesn't start immediately. It also has a
payoff — by Part VII you will be able to read `D = 26` and know *exactly* where the 26 came from,
because you'll have computed the normal-ordering constant yourself.

**v2.0 change:** the math is now the investment, not the overhead. Part 0 goes from 4 chapters to 9.
Every just-in-time math topic that was crammed into a physics chapter gets its own chapter. Total
goes from 44 to **59 chapters** — of which **21 are dedicated math chapters**, about a third of the
book. That's the right ratio for what you're trying to do.

---

## 1. The spine

Seven subjects, one idea. Every theory in this book is the same three moves:

**Pick a symmetry → write the most general action invariant under it → quantize.**

| Theory | Symmetry | Action | Quantized? |
|---|---|---|---|
| Classical mechanics | Galilean | ∫L dt | no |
| Special relativity | Lorentz | −mc²∫dτ | no |
| Electromagnetism | Lorentz × U(1) local | −¼∫F<sub>μν</sub>F<sup>μν</sup> | no |
| General relativity | diffeomorphism | ∫R √−g d⁴x | not yet |
| Quantum mechanics | Galilean | path integral | yes |
| QED / QCD / EW | U(1) / SU(3) / SU(2)×U(1) local | Yang–Mills + matter | yes |
| String theory | worldsheet diffeo × Weyl | Polyakov | yes |

If you can see that table as one sentence rather than seven rows, the book has worked. Two other
threads run all the way through and get flagged explicitly whenever they resurface:

- **The harmonic oscillator.** It is the pendulum in Part I, the ladder operator in Part IV, the
  particle in Part V, and the string mode in Part VII. Same math, four disguises.
- **Symmetry ⇒ conservation (Noether).** Introduced in Chapter 1.4 and used, without exaggeration,
  in every part after it.

---

## 2. The math doctrine — "relatable math"

This is the part that changed most in v2.0, and it's the part that will decide whether the book
works. Every mathematical object introduced anywhere in these 59 chapters gets **four things,
in this order, without exception**:

**1 · The question it answers.**
No object is ever introduced as a definition out of the blue. It arrives because we asked something
we couldn't answer. *"We need to compare vectors at two different points on a curved surface, and we
discover we literally cannot — that gap is what a connection is for."* Definition follows need.

**2 · A picture or a physical anchor.**
Determinant = the factor by which a map scales volume. Trace = the divergence of the flow it
generates. Eigenvector = the direction a map doesn't turn. One-form = a stack of level surfaces,
and the "index" counts how many your vector pierces. If I can't give you a picture, I say so
explicitly rather than pretending.

**3 · A familiar cousin — including from your own field.**
New math gets connected to math you already own. Sometimes that's earlier in the book ("a tensor is
what a matrix wanted to be"; "a Lie algebra is a rotation, examined infinitesimally"). Sometimes it's
from clinical and quantitative work you already do daily. These get a **Familiar Ground** callout,
and I only use them where the mathematics is *actually identical*, never as decoration:

| Something you already use | Same math as |
|---|---|
| First-order drug elimination, t½ | Radioactive decay, RC circuits, and every exponential in the book |
| Two-compartment PK models | Coupled linear ODEs → normal modes → field modes |
| Superposition of repeat dosing | Convolution → Green's functions → propagators |
| S(t) = exp(−∫₀ᵗ h(τ)dτ), survival from hazard | **The Dyson series.** U(t) = T exp(−(i/ℏ)∫H dt′) is the same object; the only new ingredient is time-ordering |
| Log-odds, logistic regression | Boltzmann weights, partition functions |
| Poisson counting in low-event trials | Photon counting, shot noise, vacuum fluctuations |
| PCA on an expression matrix | Diagonalization → normal modes → energy eigenstates |
| Kaplan–Meier as a product of conditionals | Path integral as a product of infinitesimal time steps |

That survival-function/Dyson-series identity is not an analogy. It is literally the same equation,
and when it lands in Chapter 5.6 you'll have known it for twenty years.

**4 · A calculation you actually do with it.**
Nothing is introduced and shelved. Every tool is spent in the chapter that introduces it, and the
chapter closes by naming exactly which later chapter cashes it in again.

### The Math Ledger

A running index — its own page in the book — of every mathematical object: where it was defined,
what it was defined *for*, and every later chapter that uses it. When a `Γᵏᵢⱼ` shows up in Chapter
3.7 and you want to know where it came from, one click. It grows with every batch.

### Two more recurring devices

- **⚠ Why this isn't obvious** — flags the specific places where everyone's intuition breaks, said
  out loud instead of glossed. The point where "the derivative is a slope" stops being adequate.
  Why raising an index is not just moving a letter. Why a self-adjoint operator is not the same as
  a Hermitian matrix once the space is infinite-dimensional.
- **▸ Grind box** — a collapsible block holding routine algebra and index gymnastics. The main line
  of argument stays readable; open the box any time you want to audit the machinery. Nothing is
  skipped, it's just folded.

---

## 3. Decisions locked in

| Question | Choice |
|---|---|
| Math | **Deep Part 0 primer (9 ch), then generous just-in-time.** Every math topic gets its own chapter, introduced at the moment physics demands it — tensors when SR needs them, manifolds and forms when GR needs them, function spaces when QM needs them, Lie theory and rep theory when gauge theory needs them, Grassmann numbers when fermions need them. |
| Derivations | **Complete, with routine algebra collapsible** in Grind boxes. |
| Layout | **One self-contained HTML file per chapter + an index hub** with persistent TOC, prev/next, and cross-links to the Math Ledger. |
| Practice | **Worked examples inline + "Your turn" problems** with click-to-reveal full solutions. |
| Pace | Slow on purpose. Math chapters are allowed to be long. |

---

## 4. Chapter template

1. **Where we are** — one paragraph placing this chapter in the arc.
2. **Tools you'll need** — explicit back-links.
3. **The build** — numbered equations, every step present, Grind boxes for the algebra.
4. **Worked example** — a real calculation, start to finish.
5. **Interactive** — *only when it teaches something a static figure cannot.*
6. **Your turn** — 2–4 problems, solutions hidden behind a click.
7. **The brick you just laid** — what is now available downstream, and which chapter spends it.

---

## 5. Full curriculum — 59 chapters, 8 parts

`※` marks a dedicated math chapter — 21 of the 59.

### PART 0 · THE TOOLKIT (9 ch) ※ all
*Rebuild the floor, properly. No physics yet, but every example is drawn from physics or from
quantitative work you already do.*

| # | Chapter | Key content |
|---|---|---|
| 0.1 | What a Derivative Really Is | Limits; **the derivative as local linearization** (the reframe that makes everything later work); rules derived, not memorized; higher derivatives; Leibniz vs Newton vs operator notation |
| 0.2 | Integration and Accumulation | Riemann sums; both fundamental theorems; substitution and by parts; **the Gaussian integral** via the polar trick (you will use it a hundred times); improper integrals |
| 0.3 | Series, Approximation, Orders of Magnitude | Taylor and Maclaurin; radius of convergence; asymptotic vs convergent series; small-parameter expansion as the physicist's native mode; dimensional analysis; Fermi estimation |
| 0.4 | Vector Spaces and Linear Maps | Abstract vector spaces; basis and dimension; matrices *as maps*; composition; **determinant as signed volume**; trace; invertibility; change of basis (the seed of "tensor") |
| 0.5 | Inner Products, Eigenvectors, Spectral Theorem | Inner products and orthonormality; Gram–Schmidt; adjoints; Hermitian and unitary; diagonalization; **why Hermitian ⇒ real eigenvalues** — the measurement postulate of QM, pre-loaded four parts early |
| 0.6 | Multivariable Calculus | Partials; the total derivative as *the* linear approximation; chain rule; Jacobians; Hessian; Lagrange multipliers; gradient quietly introduced as a one-form |
| 0.7 | Fields, Flux, and the Big Theorems | Divergence and curl; line and surface integrals; Green, Stokes, divergence theorems as one theorem in three costumes; conservative fields; **the continuity equation** (which recurs in every part) |
| 0.8 | Differential Equations and the Oscillator | First-order linear ODEs (exponential decay — familiar ground); second-order linear; damped and driven oscillator; resonance; phase space; **coupled oscillators and normal modes** |
| 0.9 | Fourier, Delta Functions, Probability | Fourier series and transform; convolution; the Dirac delta handled honestly; **the bandwidth theorem — the uncertainty principle, four parts before quantum mechanics**; distributions, expectation, variance, Gaussians, CLT |

*Interactives:* zoom-into-a-curve until it's a straight line (0.1). Taylor order slider on cos x (0.3). Matrix acting on the unit circle → eigenvectors as the directions that don't turn (0.5). Two coupled pendulums decomposing into normal modes (0.8). Fourier synthesis builder + the width-vs-bandwidth tradeoff shown live (0.9).

---

### PART I · THE ACTION PRINCIPLE (4 ch)
*The most-skipped prerequisite in physics, and the reason most readers wall out at GR and again at QFT.*

| # | Chapter | Key content |
|---|---|---|
| 1.1 | What's Wrong With Forces | Newton recap; energy and momentum; where the force picture starts to creak |
| 1.2 | Stationary Action ※ | Calculus of variations built from scratch; **Euler–Lagrange derived**; Newton recovered; constraints become trivial |
| 1.3 | Hamilton and Phase Space | Legendre transform; canonical equations; Poisson brackets; Liouville; phase-space flow |
| 1.4 | Noether's Theorem | Continuous symmetry ⇒ conserved current, **proved**; energy, momentum, angular momentum as three instances of one theorem |

*Interactive:* drag a trial path between two fixed points and watch S(path) change live, bottoming out exactly at the true trajectory.

---

### PART II · SPECIAL RELATIVITY (6 ch)

| # | Chapter | Key content |
|---|---|---|
| 2.1 | The Crisis of 1900 | Galilean relativity vs Maxwell; why c sits inside Maxwell's equations; the two postulates |
| 2.2 | The Lorentz Transformation, Derived | From the postulates, not asserted; time dilation, length contraction, **relativity of simultaneity** |
| 2.3 | Minkowski Geometry | The invariant interval as a metric; proper time; light cones; causal structure |
| 2.4 | Tensors, Honestly ※ | What an index *is*; multilinear maps; the transformation law as the definition; upper vs lower; the metric as index-mover; contraction; why this is not just bookkeeping |
| 2.5 | Relativistic Dynamics | Four-velocity, four-momentum; **E = mc² derived**; relativistic Lagrangian; massless particles |
| 2.6 | Electromagnetism Is Relativity | F<sup>μν</sup>; four Maxwell equations become two; the EM Lagrangian; A<sup>μ</sup> and the **first appearance of gauge invariance** — seed for all of Part VI |

*Interactives:* Minkowski diagram with a boost slider (watch simultaneity lines scissor); pole-in-the-barn resolved on that same diagram.

---

### PART III · GENERAL RELATIVITY (8 ch)

| # | Chapter | Key content |
|---|---|---|
| 3.1 | The Equivalence Principle | Gravity as the odd one out; **tidal forces** as the part you cannot transform away |
| 3.2 | Manifolds ※ | Charts; tangent spaces; vectors as directional derivatives; one-forms; what an index has *actually* meant all along |
| 3.3 | Metric and Connection ※ | Metric tensor; the problem of comparing vectors at different points; covariant derivative; Christoffels; parallel transport; **geodesic equation from an action** |
| 3.4 | Curvature ※ | Riemann tensor from the commutator of covariant derivatives; geodesic deviation; Ricci; the Ricci scalar; Bianchi identities |
| 3.5 | Forms, Lie Derivatives, Killing Vectors ※ | Differential forms and the exterior derivative; integration on manifolds; Lie derivative; **Killing vectors ⇒ conserved quantities** (Noether, geometrized) |
| 3.6 | The Einstein Field Equations | Motivated, then **derived from the Einstein–Hilbert action**; stress-energy tensor; Newtonian limit recovers Poisson |
| 3.7 | Schwarzschild | Solution derived in full; orbits and the ISCO; perihelion precession; light bending; redshift; what a horizon really is |
| 3.8 | Cosmology and a Loose Thread | FLRW; Friedmann equations; expansion; **black hole entropy S = A/4** — deliberately left dangling until 7.8 |

*Interactives:* parallel transport around a loop on a sphere (holonomy — *the* insight for curvature); Schwarzschild effective potential with a slider, watching the ISCO appear where Newton has nothing; light-bending ray tracer.

---

### PART IV · QUANTUM MECHANICS (8 ch)

| # | Chapter | Key content |
|---|---|---|
| 4.1 | What Classical Physics Cannot Do | Blackbody, photoelectric, line spectra, double slit — each a specific, quantified failure |
| 4.2 | The Linear Algebra of Quantum States ※ | Finite-dimensional first: states as vectors, operators, Hermiticity, spectral theorem, Dirac notation, tensor products. QM *is* linear algebra |
| 4.3 | Function Spaces and Infinite Dimensions ※ | L²; completeness; continuous spectra; delta normalization; **why self-adjoint ≠ Hermitian once the space is infinite-dimensional**, and why physicists usually get away with ignoring it |
| 4.4 | The Schrödinger Equation | Wavefunctions; probability current; free particle; wave packets; group velocity |
| 4.5 | Systems You Can Solve | Infinite well; harmonic oscillator **twice** (series *and* ladder operators — ladders are the seed of particle creation); tunneling; hydrogen in full |
| 4.6 | Commutators, Uncertainty, the Classical Limit | Generalized uncertainty relation derived; compatible observables; Ehrenfest; ℏ → 0 |
| 4.7 | Angular Momentum and Spin | The algebra; **SU(2)**; spinors; the 720° rotation; Pauli matrices; addition of angular momentum — your first real Lie group |
| 4.8 | Entanglement and Measurement | Identical particles; bosons and fermions; **Bell's inequality derived and violated**; density matrices; decoherence; an honest account of what remains unresolved |

*Interactives:* live TDSE solver — wave packet hits a barrier, tunneling probability vs barrier height and width; spinor under continuous rotation (the belt trick, quantitatively); Bell correlation vs detector angle, quantum curve against the classical bound.

---

### PART V · QUANTUM FIELD THEORY (9 ch)

| # | Chapter | Key content |
|---|---|---|
| 5.1 | Why QM + SR Forces Fields | Particle number isn't conserved; causality; the Klein–Gordon negative-probability problem and its resolution |
| 5.2 | Classical Field Theory | Lagrangian density; field equations; **Noether currents for fields**; stress-energy tensor again |
| 5.3 | Quantizing a Field | Canonical quantization of the scalar field; a field *is* infinitely many oscillators; a<sup>†</sup> creates a particle; vacuum energy |
| 5.4 | The Dirac Equation | Derived; Clifford algebra; spinors done properly; **antiparticles fall out**; spin-statistics |
| 5.5 | Gaussian and Functional Integrals ※ | Multidimensional Gaussians; generating functionals; **Grassmann numbers** and integration over anticommuting variables; the machinery the path integral runs on |
| 5.6 | Interactions and Feynman Rules | Interaction picture; S-matrix; **Dyson series** (= your survival function, time-ordered); Wick's theorem; **Feynman rules derived, not handed over** |
| 5.7 | A Real Calculation | One scattering process from Lagrangian to cross section, every step, nothing skipped |
| 5.8 | The Path Integral | Double slit → sum over histories → field path integral; recovers everything above; becomes the language of the rest of the book |
| 5.9 | Loops, Infinities, and the RG | Regularization; **renormalization**; running coupling; the renormalization group; effective field theory — why physics is possible without knowing everything |

*Interactives:* diagram builder (assemble vertices → read off the amplitude structure); running coupling α(μ) with QED and QCD on the same axes — that one plot is the whole punchline of Part VI.

---

### PART VI · GAUGE THEORY AND THE STANDARD MODEL (7 ch)

| # | Chapter | Key content |
|---|---|---|
| 6.1 | Lie Groups and Lie Algebras ※ | Continuous symmetry made precise; generators; exponential map; structure constants; U(1), SU(2), SU(3) |
| 6.2 | Representation Theory ※ | Reps, weights, roots, Casimirs; how SU(3) reps organize the hadrons; why matter comes in the multiplets it does |
| 6.3 | The Gauge Principle | Demand *local* symmetry → the gauge field appears for free; **QED derived this way** |
| 6.4 | Yang–Mills | Non-abelian gauge fields; self-interacting bosons; the field strength that doesn't commute |
| 6.5 | QCD | Color; gluons; **compute the sign of the beta function** → asymptotic freedom; confinement; lattice; chiral symmetry breaking; where the proton's mass actually comes from (not the Higgs) |
| 6.6 | Symmetry Breaking and the Higgs | Spontaneous symmetry breaking; Goldstone's theorem; **Higgs mechanism derived**; mass generation; CKM |
| 6.7 | The Standard Model, Assembled | The full Lagrangian, term by term, each one explained. Then: gravity, hierarchy, dark matter, neutrino mass, 19 free parameters — the motivation for Part VII |

*Interactive:* tiltable Mexican-hat potential — massless Goldstone direction vs massive radial direction, i.e. the Higgs mechanism in one picture.

---

### PART VII · STRINGS AND M-THEORY (8 ch)

| # | Chapter | Key content |
|---|---|---|
| 7.1 | Why Quantum Gravity Is Hard | Perturbative non-renormalizability of GR by explicit power counting; the Planck scale; what "UV completion" means |
| 7.2 | Conformal Symmetry in Two Dimensions ※ | Why 2D is special; the conformal algebra; Virasoro; central charge — the machinery that makes string quantization work |
| 7.3 | The Bosonic String | Nambu–Goto and Polyakov actions; worldsheet symmetries; gauge fixing; mode expansion |
| 7.4 | Quantizing the String | Commutators of modes; Virasoro constraints; normal ordering; **D = 26 derived** |
| 7.5 | The Spectrum | Tachyon; massless states = **graviton + dilaton + B-field**. Gravity is not put in — it comes out. This is the entire reason anyone cares |
| 7.6 | Superstrings | Worldsheet supersymmetry; GSO projection; D = 10; the five superstring theories |
| 7.7 | Branes, Dualities, M-Theory | D-branes; T- and S-duality; five theories + 11D supergravity become one; compactification; Calabi–Yau; the landscape problem |
| 7.8 | Holography and Honest Accounting | **Black hole entropy counted from D-brane microstates** — the loose thread from 3.8, tied off; AdS/CFT; then a straight assessment of what is established mathematics, what is conjecture, what is untested physics. Loop quantum gravity and asymptotic safety stated fairly |

*Interactives:* string mode visualizer (open vs closed, first several modes); watch a dimension compactify and the Kaluza–Klein tower appear; Calabi–Yau cross-section.

---

## 6. One honest caveat about the far end

Parts 0–VI can be built at full rigor: every equation derivable with tools the book has already laid
down. **Part VII cannot be, and I won't pretend otherwise.**

Chapters 7.1–7.5 are fully derivable — you will genuinely quantize the bosonic string and produce 26
and the graviton yourself. From 7.6 onward, complete rigor would require supersymmetry algebras,
full conformal field theory, and algebraic geometry: three more books. So 7.6–7.8 will be
*structurally rigorous* — the logic, the key calculations, the actual equations — with the deepest
technical machinery quoted and clearly flagged. Every quoted-not-derived step is marked **⚑** so you
always know exactly what you're standing on.

---

## 7. Build order and batches

| Batch | Contents | Ch |
|---|---|---|
| **1** | Scaffold, house style, Math Ledger + **0.1–0.3** (derivatives, integration, series) | 3 |
| **2** | **0.4–0.6** (linear algebra, spectral theorem, multivariable) | 3 |
| **3** | **0.7–0.9** (vector calculus, ODEs/oscillators, Fourier/probability) | 3 |
| **4** | **Part I** — the action principle | 4 |
| **5** | **2.1–2.3** — SR crisis through Minkowski | 3 |
| **6** | **2.4–2.6** — tensors, dynamics, EM | 3 |
| **7** | **3.1–3.4** — equivalence principle, manifolds, connection, curvature | 4 |
| **8** | **3.5–3.8** — forms, field equations, Schwarzschild, cosmology | 4 |
| **9** | **4.1–4.4** — crisis, linear algebra of QM, function spaces, Schrödinger | 4 |
| **10** | **4.5–4.8** — solvable systems, uncertainty, spin, entanglement | 4 |
| **11** | **5.1–5.5** — fields, quantization, Dirac, Gaussian/Grassmann | 5 |
| **12** | **5.6–5.9** — Feynman rules, a real calculation, path integral, RG | 4 |
| **13** | **6.1–6.4** — Lie theory, rep theory, gauge principle, Yang–Mills | 4 |
| **14** | **6.5–6.7** — QCD, Higgs, the Standard Model | 3 |
| **15** | **7.1–7.4** — quantum gravity, 2D CFT, the string, D = 26 | 4 |
| **16** | **7.5–7.8** — spectrum, superstrings, M-theory, holography | 4 |

**Total: 59 chapters, 16 batches, 21 of them dedicated math chapters.**

---

## 8. Technical build

- **Math rendering:** KaTeX (auto-render, CDN) — markedly faster than MathJax at this equation
  density. Numbered, referenceable display equations.
- **Self-contained chapters:** each `.html` carries its own CSS and JS inline, so any single chapter
  opens and works standalone. Cross-chapter links resolve when the folder is intact.
- **Interactives:** hand-written canvas/SVG, no heavyweight frameworks. Numerics (RK4 for geodesics,
  Crank–Nicolson for the TDSE) run natively in the browser. Every interactive must pass one test:
  *does this teach something a static figure cannot?* If no, it doesn't get built.
- **Build pipeline:** chapter content lives as HTML fragments; a build script wraps each in the
  shared shell. Style changes propagate across all 59 chapters at once instead of being re-edited
  59 times.
- **Verification:** every chapter is rendered headlessly in Chromium and screenshotted before
  delivery — equations typeset, interactives running, navigation live.
- **Delivery:** individual chapter files as finished, a zipped folder per batch, and a living index hub.
