# From Newton to M-Theory
## A Build-It-Yourself Book — Architecture & Curriculum Plan

*Version 2.0 — 15 Aug 2026 — math foundation deepened*

> **Superseded forward of Chapter 3.7.** This document remains the plan of record for Chapters 0.1
> to 3.6, all of which are written. From 3.7 onward it is superseded by
> [`PLAN-FORWARD.md`](PLAN-FORWARD.md), which revises the curriculum from 67 chapters to 67 after
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
goes from 44 to **67 chapters** — of which **23 are dedicated math chapters**, about a third of the
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
works. Every mathematical object introduced anywhere in these 67 chapters gets **four things,
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

## 5. Full curriculum — 67 chapters, 8 parts

`※` marks a dedicated math chapter — 23 of the 67.

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

### PART III · GENERAL RELATIVITY (9 ch)

| # | Chapter | Key content |
|---|---|---|
| 3.1 | The Equivalence Principle | Gravity as the odd one out; **tidal forces** as the part you cannot transform away |
| 3.2 | Manifolds ※ | Charts; tangent spaces; vectors as directional derivatives; one-forms; what an index has *actually* meant all along |
| 3.3 | Metric and Connection ※ | Metric tensor; the problem of comparing vectors at different points; covariant derivative; Christoffels; parallel transport; **geodesic equation from an action** |
| 3.4 | Curvature ※ | Riemann tensor from the commutator of covariant derivatives; geodesic deviation; Ricci; the Ricci scalar; Bianchi identities |
| 3.5 | Forms, Lie Derivatives, Killing Vectors ※ | Differential forms and the exterior derivative; integration on manifolds; Lie derivative; **Killing vectors ⇒ conserved quantities** (Noether, geometrized) |
| 3.6 | The Einstein Field Equations | Motivated, then **derived from the Einstein–Hilbert action**; stress-energy tensor; Newtonian limit recovers Poisson |
| 3.7 | Schwarzschild: The Solution and Its Orbits | The solution derived in full from the symmetric ansatz; Birkhoff; conserved quantities from Killing vectors; the effective potential; **the ISCO at r = 6GM/c²**, which Newton has no name for; **Mercury's 43″ per century** |
| 3.8 | Light, Redshift, and What a Horizon Is | Null geodesics; **1.75″ of deflection with the missing half identified as spatial curvature** — the factor of two Chapter 3.1 confessed; gravitational redshift from the metric; Eddington–Finkelstein; the Kretschmann scalar, finite at the horizon and divergent at the centre |
| 3.9 | Cosmology, and a Loose Thread | FLRW; Friedmann equations; expansion; **why energy is not conserved in an expanding universe** — no timelike Killing vector, so Noether has nothing to work with; **black hole entropy S = A/4** deliberately left dangling until 7.9 |

*Interactives:* parallel transport around a loop on a sphere (holonomy — *the* insight for curvature); Schwarzschild effective potential with a slider, watching the ISCO appear where Newton has nothing; light-bending ray tracer.

---

### PART IV · QUANTUM MECHANICS (11 ch)

| # | Chapter | Key content |
|---|---|---|
| 4.1 | What Classical Physics Cannot Do | Make the failures quantitative, so that quantization is forced rather than proposed: blackbody, photoelectric, line spectra, double slit. **The Planck spectrum derived Einstein's way** — A and B coefficients, detailed balance, 0.6's Boltzmann weights — with the ultraviolet catastrophe shown to be a divergent integral, not a metaphor |
| 4.2 | The Linear Algebra of Quantum States ※ | Show that Chapter 0.5 was quantum mechanics with the physics stripped off, and put the physics back. **The postulates, as a table of renamings** — plus the one genuinely new input, the Born rule, announced as a postulate and not smuggled |
| 4.3 | Function Spaces: Measure, L², and Completeness ※ | Rebuild the integral so that the space of states is actually a space: the Lebesgue integral, dominated convergence, Cauchy sequences. **L² is complete, and the Fourier basis is a basis** — closing 0.9's flag and 0.2's promise in one chapter |
| 4.4 | Operators in Infinite Dimensions ※ | Say exactly which of Chapter 0.5's theorems survive, which need repair, and which are false: unbounded operators and domains, continuous spectra, projection-valued measures, plane waves that are not in L², rigged Hilbert spaces. **A symmetric operator need not be self-adjoint** — worked on the particle in a box and on momentum on a half-line |
| 4.5 | The Schrödinger Equation | Get the equation from the two things already built — a unitary flow with a Hermitian generator, and de Broglie's identification. Wavefunctions; free particle; wave packets; group velocity. **The probability current and ∂ρ/∂t + ∇·j = 0**, the same continuity equation as 0.7 |
| 4.6 | Systems You Can Solve in One Dimension | Infinite well; tunneling; the oscillator twice, because the second way is the whole of Parts V and VII. **Eₙ = (n+½)ℏω from the ladder algebra alone**, with no differential equation solved — collecting 0.8's phase-space area and 1.3's Bohr–Sommerfeld flag |
| 4.7 | Symmetry, Commutators, and the Classical Limit | Spend the uncertainty relation rather than re-derive it, and say honestly how classical mechanics emerges: Ehrenfest, WKB, ℏ → 0. **The Hamilton–Jacobi equation as the ℏ → 0 limit of Schrödinger**, followed by Groenewold–van Hove, which says the correspondence cannot be made exact |
| 4.8 | Angular Momentum and Spin | Build the reader's first Lie algebra from a commutator they can compute. **The spectrum j = 0, ½, 1, … from the algebra alone**, and with it the half-integer representations that force the 720° rotation — your first real Lie group |
| 4.9 | The Hydrogen Atom | Solve the one system whose exact solution built the subject, and explain a degeneracy no one asked for. Spherical harmonics from 4.8's algebra rather than from a series; the radial ladder. **Eₙ = −13.6 eV/n², and the fact that it depends on n alone** — the accidental degeneracy as the quantum shadow of the closed Kepler orbit |
| 4.10 | Perturbation Theory and Transitions | Build the approximation scheme the rest of the book runs on, in a setting where it can be checked: fine structure, the adiabatic theorem, the interaction picture. **Fermi's golden rule**, checked against a numerically integrated two-level system — and the **Dyson series recognized as the survival function**, with time-ordering the only new ingredient |
| 4.11 | Identical Particles, Entanglement, and Measurement | What quantum mechanics says about *two* things, which is where all the strangeness lives: bosons and fermions, density matrices, decoherence. **Bell's inequality, derived and then violated**, with an honest statement of what is and is not thereby settled |

*Interactives:* live TDSE solver — wave packet hits a barrier, tunneling probability vs barrier height and width; spinor under continuous rotation (the belt trick, quantitatively); Bell correlation vs detector angle, quantum curve against the classical bound.

---

### PART V · QUANTUM FIELD THEORY (11 ch)

| # | Chapter | Key content |
|---|---|---|
| 5.1 | Why QM + SR Forces Fields | Show that the two theories already built are jointly inconsistent unless particle number can change. **The Klein–Gordon negative-probability problem, and its resolution** — plus the localization argument: confining a particle to Δx < ℏ/mc costs enough energy to make another one |
| 5.2 | Classical Field Theory | Run Chapters 1.2 and 1.4 again with a continuous index. Lagrangian density; field equations. **The Noether current for a general field symmetry, and ∂<sub>μ</sub>T<sup>μν</sup> = 0** — the object Chapter 3.6 put on the right-hand side of Einstein's equations, now derived rather than assembled |
| 5.3 | Quantizing a Field | Take Chapter 0.8's coupled-oscillator limit seriously and discover that its quanta are particles. **a<sup>†</sup> creates a particle of momentum ℏk** — with the vacuum energy summed, shown to diverge, and the Casimir force extracted from the *difference*, which is finite and measured |
| 5.4 | Distributions, Contours, and the Propagator ※ | Build the two pieces of mathematics the book has been using on credit — complex analysis (Cauchy, residues, analytic continuation) and distributions — and cash them immediately. **The four Green's functions of the Klein–Gordon operator as four contours around the same two poles**, with the iε prescription derived as a contour choice rather than announced as a rule |
| 5.5 | The Dirac Equation | Take the square root of the Klein–Gordon operator and be forced into antiparticles. Clifford algebra; spinors done properly; chirality. **Antiparticles fall out of the negative-energy solutions, and the electron's g = 2** — derived, not quoted. Spin-statistics stated, both physical failures computed |
| 5.6 | The Path Integral | Replace the operator formalism with a sum over histories, and recover everything so far. **The propagator as ∫𝒟x e<sup>iS/ℏ</sup>, from time-slicing** — with the free-particle propagator computed exactly and shown to agree with 4.5, and the non-existence of the measure flagged in place |
| 5.7 | Gaussian and Grassmann Integration ※ | Build the algebra of anticommuting numbers at the moment fermions need it. Multidimensional Gaussians; differentiation with respect to a source. **∫dθ dθ̄ e<sup>−θ̄Aθ</sup> = det A** — the determinant upstairs rather than downstairs, which is the entire reason fermion loops carry a minus sign |
| 5.8 | Interactions, Wick's Theorem, and the Feynman Rules | Derive the rules rather than receive them, and be honest about the foundation. **Every Feynman rule, read off Z[J] by functional differentiation** — with Wick's theorem proved combinatorially and Haag's theorem flagged in place |
| 5.9 | A Real Calculation | One process from Lagrangian to number, nothing skipped and nothing quoted. **One differential cross section, computed and compared with data** — e⁺e⁻ → μ⁺μ⁻, chosen because every ingredient is available and the answer is measured to four figures |
| 5.10 | Loops, Divergences, and Regularization | Compute a divergent integral honestly and isolate exactly what diverges. **One loop integral evaluated in full in d = 4 − ε dimensions**, with dimensional regularization *derived* — the d-dimensional Gaussian is 0.2's integral with a different exponent — rather than declared |
| 5.11 | Renormalization and the Renormalization Group | Explain why physics is possible without knowing everything: effective field theory, and poles and branch cuts as particles and thresholds. **The running coupling α(μ) from the Callan–Symanzik equation**, plotted for QED and QCD on the same axes; Dyson's argument that the series has zero radius of convergence, derived |

*Interactives:* diagram builder (assemble vertices → read off the amplitude structure); running coupling α(μ) with QED and QCD on the same axes — that one plot is the whole punchline of Part VI.

---

### PART VI · GAUGE THEORY AND THE STANDARD MODEL (8 ch)

| # | Chapter | Key content |
|---|---|---|
| 6.1 | Lie Groups and Lie Algebras ※ | Name the structure the reader has met five times without being told what it was: generators, the exponential map, structure constants; U(1), SU(2), SU(3). **su(N) has N² − 1 generators** — delivering the eight gluons as an arithmetic consequence rather than a fact |
| 6.2 | Representations ※ | Explain why matter comes in the multiplets it does: irreducibility, Schur's lemma, weights, Casimirs. **3 ⊗ 3̄ = 8 ⊕ 1, by index gymnastics the reader can do** — and with it the meson octet, which is why the hadrons of the 1960s organized themselves |
| 6.3 | The Gauge Principle | Demand a symmetry locally and watch a force appear to enforce it. **Electromagnetism, generated** — D<sub>μ</sub> = ∂<sub>μ</sub> − ieA<sub>μ</sub> forced by demanding local phase invariance, with p → p − eA recognized as the thing 1.3 derived classically, and the Aharonov–Bohm phase derived |
| 6.4 | Yang–Mills | Do the same with a group whose elements do not commute, and find that the force carries its own charge. **F<sup>a</sup><sub>μν</sub> with its quadratic term, and the self-interaction that follows** — the structural difference between a photon and a gluon, derived from one commutator |
| 6.5 | QCD and Asymptotic Freedom | Compute the sign that changes everything. **β(g) < 0, with the coefficient 11 − ⅔n<sub>f</sub> computed** — 6.4's gluon self-coupling overwhelming the fermion screening. Confinement flagged honestly, with the strong-coupling area law as the one thing that can be shown |
| 6.6 | Spontaneous Symmetry Breaking and the Higgs Mechanism | Give a gauge boson a mass without breaking the symmetry that forbade it. **Goldstone's theorem, and then its evasion** — the massless mode of a global symmetry eaten by the gauge field, with the degrees of freedom counted before and after and shown to balance exactly |
| 6.7 | The Electroweak Theory | Derive the structure that looks arbitrary, and show it is not: SU(2)×U(1), mixing, mass generation for fermions. **The hypercharge assignments, forced by anomaly cancellation** — with M<sub>W</sub> = M<sub>Z</sub> cos θ<sub>W</sub> falling out of the same symmetry breaking, and the CKM matrix's three angles and one phase counted, which is why CP violation needs three generations |
| 6.8 | The Standard Model, and What It Does Not Explain | Say what has been built, count what has not, and hand the reader the motivation for Part VII. The full Lagrangian, term by term. **The nineteen free parameters, enumerated and grouped by where they come from** — followed by gravity, hierarchy, dark matter and neutrino mass, each stated precisely enough to be a research problem rather than a complaint |

*Interactive:* tiltable Mexican-hat potential — massless Goldstone direction vs massive radial direction, i.e. the Higgs mechanism in one picture.

---

### PART VII · STRINGS AND M-THEORY (9 ch)

| # | Chapter | Key content |
|---|---|---|
| 7.1 | Why Quantum Gravity Is Hard | Diagnose the failure precisely, by counting rather than gesturing at it. **[G] = length² ⇒ a new counterterm at every order**, computed — and then the reason the obvious repair fails: higher-derivative terms buy a ghost, which is the Ostrogradsky flag now collected |
| 7.2 | The Bosonic String | Write the most general action for a one-dimensional object and gauge-fix it. Nambu–Goto and Polyakov; worldsheet symmetries. **Polyakov's action, and the mode expansion in conformal gauge** — with the demonstration that Weyl plus diffeomorphism invariance is *just* enough freedom to reach the flat worldsheet metric |
| 7.3 | Conformal Symmetry and the Virasoro Algebra ※ | Answer the question 7.2 asked: what freedom is left after gauge fixing. Why 2D is special; the conformal algebra; central charge. **[L<sub>m</sub>,L<sub>n</sub>] = (m−n)L<sub>m+n</sub> + (c/12)m(m²−1)δ<sub>m+n,0</sub>, with the central term computed by hand** from the oscillator commutators — no operator-product expansion required |
| 7.4 | Quantizing the String, and D = 26 | Let the reader produce the most famous number in the subject themselves. Mode commutators; Virasoro constraints; normal ordering; the zero-point sum and its ζ-regularization set against an honest cut-off. **D = 26**, derived in light-cone gauge from the requirement that the Lorentz algebra close |
| 7.5 | The Spectrum | Show that gravity was not put in. Tachyon; massless states = **graviton + dilaton + B-field**. **A massless spin-2 state in the closed-string spectrum** — identified as a graviton because a massless spin-2 field has only one possible low-energy action, which is Chapter 3.6's. This is the chapter the book exists for |
| 7.6 | Superstrings and D = 10 | Remove the tachyon, and get fermions, by the same arithmetic that gave 26: worldsheet fermions, super-Virasoro, GSO projection. **D = 10, by the identical central-charge count as 7.4** — the most satisfying possible reuse of 7.3's machinery |
| 7.7 | T-Duality and D-Branes | Derive two things nobody would have guessed, using only the mode expansion. **R ↔ α′/R with momentum and winding exchanged, and the spectra shown identical** — followed by the observation that T-dualizing an open string turns Neumann into Dirichlet, so a D-brane is not postulated, it is forced |
| 7.8 | Compactification, Dualities, M-Theory | Present the structure honestly, with every step's status marked: S-duality quoted, Calabi–Yau conditions stated, the five theories and 11D supergravity becoming one, the landscape named. **The Kaluza–Klein tower, derived in full** — the one thing here that is a calculation, with everything else placed in the ledger by name |
| 7.9 | Black Hole Entropy, Holography, and the Accounting | Count the states of a black hole, and then state exactly where the building ends. **S = A/4, obtained by counting oscillator states** via a saddle-point evaluation of the D1–D5 degeneracy — closing the loose thread 3.9 deliberately left. Then AdS/CFT, and the ledger in full: what is established mathematics, what is conjecture, what is untested physics |

*Interactives:* string mode visualizer (open vs closed, first several modes); watch a dimension compactify and the Kaluza–Klein tower appear; Calabi–Yau cross-section.

---

## 6. One honest caveat about the far end

Parts 0–VI can be built at full rigor: every equation derivable with tools the book has already laid
down. **Part VII cannot be, and I won't pretend otherwise.**

Chapters 7.1–7.5 are fully derivable — you will genuinely quantize the bosonic string and produce 26
and the graviton yourself. From 7.6 onward, complete rigor would require supersymmetry algebras,
full conformal field theory, and algebraic geometry: three more books. So 7.6–7.9 will be
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

**Total: 67 chapters, 16 batches, 23 of them dedicated math chapters.**

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
  shared shell. Style changes propagate across all 67 chapters at once instead of being re-edited
  59 times.
- **Verification:** every chapter is rendered headlessly in Chromium and screenshotted before
  delivery — equations typeset, interactives running, navigation live.
- **Delivery:** individual chapter files as finished, a zipped folder per batch, and a living index hub.
