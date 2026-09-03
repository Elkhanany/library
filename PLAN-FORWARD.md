# From Newton to M-Theory — the forward curriculum

## Chapters 3.7 to the end: a revised plan

*Version 1.0 — 18 Aug 2026 — written against the book as it actually stands at 25 chapters, not
against `PLAN.md` v2.0.*

---

## 0 · What this document is, and what it replaces

`PLAN.md` v2.0 set out 59 chapters. Twenty-five are written. This document revises the remaining
curriculum in the light of what those twenty-five turned out to be — which is denser, slower and
more complete than v2.0 anticipated, and therefore has a much larger appetite for prerequisite
mathematics than v2.0 budgeted for.

It is written to be executed. `MATHPLAN-3.md` is the model: numbered, derivation-by-derivation,
with the mathematical input for each item named. Its §0 pacing specification is inherited verbatim
and is not restated here except where the forward material needs something added.

What this document supersedes: §5 of `PLAN.md` from Part III onward, and §7 (the batch schedule).
What it does not touch: §2 (the relatable-math doctrine), §4 (the chapter template), §6 (the caveat
about Part VII), or `CONVENTIONS.md`. Those are working and should not be disturbed.

Its companion is `GAPS.md`, which is the register of what the book has *not* built. Where this plan
says "closes the debt in `GAPS.md` §N", it means exactly that, and the entry there should be struck
when the chapter ships.

### How the twenty-five written chapters calibrate the estimate

Measured, not guessed:

| | Range across the 25 | Median |
|---|---|---|
| Words per chapter | 5,700 – 20,900 | 14,000 |
| Numbered display equations | 13 – 102 | 52 |
| `<h2>` sections | 7 – 12 | 9 |
| Grind boxes | 0 – 9 | 5 |
| "In plain terms" boxes | 5 – 10 | 7 |

Chapter 0.1 (5,700 words) is the outlier at the bottom and was written before the house voice
settled. From 0.4 onward nothing is under 12,000 words. **The working unit of this book is a
13,000–17,000-word chapter carrying 40–70 derived equations.** Every chapter-count judgement below
is made against that unit. When I say a proposed chapter "cannot hold" its material, I mean it
would run past 25,000 words, which is where the evidence says the reader is lost — Part 0 was
expanded from 4 chapters to 9 for exactly that reason, and Parts I–III move fast because of it.

---

## 1 · The chapter-count changes, summarised

| Part | `PLAN.md` v2.0 | Revised | Δ | The one-line reason |
|---|---|---|---|---|
| III · General Relativity | 8 | **9** | +1 | Schwarzschild is carrying six separate promises from four earlier chapters and cannot hold them in one chapter |
| IV · Quantum Mechanics | 8 | **20** | +12 | Chapter 4.3 alone is owed six distinct mathematical debts by Part 0; hydrogen is scheduled *before* the angular momentum it needs; and the eight chapters that remained were carrying eleven new objects each, against a book that runs at five or six. See §5 |
| V · Quantum Field Theory | 9 | **11** | +2 | Complex analysis and distributions have never been built anywhere in the book; and one chapter cannot both regulate a loop and run the renormalisation group |
| VI · Gauge Theory & the SM | 7 | **8** | +1 | "The Standard Model, assembled" as written is a tabulation; splitting off electroweak lets the structure be derived instead |
| VII · Strings & M-Theory | 8 | **9** | +1 | T-duality and D-branes are genuinely derivable and are wasted as a third of a survey chapter |
| **Total** | **59** | **76** | **+17** | |

Remaining to write: **51 chapters** (was 34).

For comparison: Part 0's expansion was 4 → 9, a 125% increase in that part and 34% in the book.
This is 29% — but it is two decisions, not one, and only the first is an addition of content. The
+8 argued in §§4–8 (59 → 67) is new material: complex analysis, distributions, perturbation theory,
electroweak. The further +9 is Part IV alone, re-cut from eleven chapters into twenty by
`reports/part4-replan.md` with **no material added and none dropped**, because the chapters as
planned were carrying twice the objects a sitting holds. On content the expansion is still 14%. I
have looked hard for merges and cuts to offset it; §§4–8 record the three I found and why I
rejected two of them.

### Where I would *not* add

Three places where the instinct to expand should be resisted, recorded so the argument does not
have to be had again:

- **Part VI does not need a fibre-bundle chapter.** The book has already built a connection (3.3)
  and its curvature (3.4) as *the* answer to "how do you compare things at two different points".
  Gauge theory is that construction with an internal index. What bundles add on top is global
  topology, and that is a ⚑, not a chapter. See §3.
- **Part VII does not need a supersymmetry chapter.** Worldsheet supersymmetry in two dimensions is
  cheap and derivable and belongs inside 7.6. Spacetime supersymmetry in four dimensions is a
  different subject and is ⚑'d. See §3.
- **There is no separate statistical-mechanics chapter, and there should not be.** Chapter 0.6
  already derives the Boltzmann distribution and the partition function from maximum entropy and
  Lagrange multipliers, which is most of what the book needs. The missing pieces — the density of
  states and the Planck spectrum — fit inside 4.1, and the microcanonical count fits inside 7.9.
  See §3 and `GAPS.md` §3.4.

---

## 2 · Pacing — what is added to `MATHPLAN-3.md` §0

Items 1–8 of `MATHPLAN-3.md` §0 stand unchanged and are binding on every chapter below. Three
further rules are needed because the forward material differs from Part III in one respect: from
Part IV on, the physics is *unfamiliar as well as difficult*, where in Part III it was difficult
but the phenomena (tides, orbits, light bending) were already known to the reader.

9. **Every new physical postulate is announced as a postulate, in its own box, before it is used.**
   Part III never had to do this: general relativity was cornered rather than posited. Quantum
   mechanics cannot be. The Born rule is not derivable, and the book's credibility depends on
   saying so at the moment it enters rather than letting it seep in. The same applies to the
   canonical commutation relation, to the spin-statistics assignment before 5.5 derives it, and to
   the choice of gauge group in Part VI.

10. **Where a result exists in the literature only under hypotheses the book has not verified, say
    which hypotheses.** "Quoted" is not enough by itself from Part V onward, because in field theory
    the hypotheses are usually the whole content — a theorem about a theory with a mass gap says
    nothing about a theory without one. A ⚑ from here on carries the hypotheses.

11. **Numerical confirmation, wherever it is available, in the text.** Chapters 3.4, 3.5 and 3.6
    do this already and it is the single most persuasive device in Part III: the holonomy angle
    measured against area times curvature, the Riemann symmetries checked to 10⁻¹³ on a generic
    metric, the Palatini identity checked symbolically. Parts IV–VII have more of this available,
    not less — a numerically integrated TDSE, a numerically diagonalised Hamiltonian, a one-loop
    integral evaluated two ways, the Virasoro algebra checked on explicit mode matrices. Every
    chapter from here should carry at least one.

---

## 3 · The crux — build it, or flag it

This is the section that decides whether the forward half of the book keeps its promise. For each
piece of mathematics the physics needs, the question is only ever: *is this derivable with a
budget the book can afford, and if not, can it be flagged in a way that leaves the reader able to
check the cases actually used?*

The standard I apply: **a ⚑ is honest if the reader can verify the quoted result in every instance
the book relies on it.** A ⚑ that hands over a general theorem the reader cannot test anywhere is a
failure dressed as candour. So most of the "flag it" decisions below come with a required
companion: state the theorem, then verify it explicitly in the two or three cases the book spends
it on.

### 3.1 · Part IV — quantum mechanics

| Machinery | Decision | Where | Cost | Argument |
|---|---|---|---|---|
| Lebesgue integral and L² | **BUILD**, with the construction of Lebesgue measure ⚑'d | 4.3, ~⅔ chapter | 8–9k words | Chapter 0.2 wrote the cheque out loud: *"In Chapter 4.3 we will throw away and rebuild the integral from scratch."* It is not optional now. But the *construction* of the measure (outer measure, Carathéodory) buys the reader nothing: build the integral from a measure whose countable additivity is quoted, and everything the physics needs — dominated convergence, completeness of L² — follows |
| Completeness of L² (Riesz–Fischer) | **⚑, then verify** | 4.3 | ½ section | The proof is a diagonal argument that teaches nothing physical. Quote it, then *show* the reader the failure it repairs: exhibit a Cauchy sequence of continuous functions with no continuous limit, so they see why the Riemann integral had to go |
| Completeness of the Fourier basis | **BUILD** | 4.3 | 1 section | Closes 0.9's ⚑ directly. Given L² and Riesz–Fischer this is Parseval plus a density argument, and the density argument (trigonometric polynomials are dense) can be done by Fejér's theorem, which is elementary and constructive |
| Unbounded operators and domains | **BUILD** | 4.4 | 2 sections | Cheap, essential, and *concrete*: the momentum operator is not defined on all of L², the adjoint's domain is not the operator's domain, and the boundary term Chapter 0.2 waved through when it made $-\ii\hbar\partial_x$ Hermitian is exactly where the domain lives. Chapter 0.6 already promised this: *"In infinite dimensions linear maps can be unbounded, $\dv{}{x}$ being the standard offender"* |
| Hermitian ≠ self-adjoint | **BUILD** | 4.4 | 2 sections | This is the payoff of the whole chapter and `PLAN.md` §2 already advertises it. Do it on the two examples that make it bite: (i) the particle in a box, whose Hamiltonian has deficiency indices $(2,2)$ and therefore a $U(2)$ — four-real-parameter — family of self-adjoint extensions, so the *boundary condition is a physical choice*, not a technicality (the familiar one-parameter family belongs to **momentum** on an interval, whose indices are $(1,1)$; do not conflate them); (ii) momentum on the half-line, which is symmetric and has **no** self-adjoint extension, so "momentum of a particle on a half-line" is not an observable. Deficiency indices may be ⚑'d; these two cases can be worked in full |
| Spectral theorem, infinite dimensions | **⚑, then verify in every case used** | 4.5 | 1 section + 3 verifications | The general proof (Cayley transform → bounded case → continuous functional calculus → Riesz representation) is three chapters of analysis and is the one place I would spend a flag without hesitation. But state it in the *multiplication-operator* form — every self-adjoint operator is multiplication by a real function on some L²(μ) — say plainly that this is the infinite-dimensional reading of Chapter 0.5's $A=UDU^{\dagger}$, and then verify it by hand for the only three operators the book ever uses it on: $\hat x$ (already multiplication), $\hat p$ (multiplication after Fourier transform, which is 0.9), and $\hat H_{\text{osc}}$ (discrete spectrum, Hermite completeness). The reader then has the theorem *and* has checked it wherever it matters. This closes 0.5's *"Chapter 4.5 pays this bill in full"* honestly |
| Stone's theorem | **BUILD one direction, ⚑ the other** | 4.5 §9 | ½ section | $H$ self-adjoint ⇒ $\ee^{-\ii Ht/\hbar}$ unitary is three lines given the functional calculus. The converse (every strongly continuous one-parameter unitary group has a self-adjoint generator) is the hard half and is ⚑'d. This is what makes "time evolution is unitary" and "the Hamiltonian is self-adjoint" the same statement, which is the sentence Chapter 0.5 has been pointing at since §7 |
| Rigged Hilbert space / Gelfand triple | **⚑, with the concrete content stated** | 4.5 §6 | 1 section | The reader does not need the triple. They need to know precisely one thing: $\ket{x}$ and $\ket{p}$ are not vectors in the space, they are continuous functionals on a smaller space of well-behaved functions, and every manipulation using them is shorthand for a wave-packet statement. Give the honest version (box normalisation, then the limit) so the reader has a crutch that always works, quote Gelfand–Maurin, and move on. Full distribution theory arrives in 5.4, where the physics genuinely forces it |
| Quantum statistics (Bose/Fermi distributions) | **BUILD**, but not where you would expect | 4.1 and 4.18 | 1 section each | 4.1 needs the Planck spectrum on page one, and Bose–Einstein statistics is not available that early — the symmetrisation postulate is 4.18. Resolution: derive the Planck law **Einstein's way**, from the A and B coefficients plus detailed balance plus 0.6's Boltzmann distribution. That is fully derivable with what the book has, and it is better physics besides, because it derives stimulated emission on the way. The occupation-number distributions then arrive properly in 4.18 once exchange symmetry exists |
| Special functions (Hermite, Legendre, Laguerre, spherical harmonics) | **BUILD, algebraically — never by series** | 4.8, 4.12, 4.13 | absorbed | The book has no theory of special functions and does not need one. Hermite functions come out of the ladder operators; spherical harmonics come out of the $\mathfrak{su}(2)$ raising/lowering algebra; the hydrogen radial functions come out of a factorisation (the same ladder trick, with an $\ell$-dependent shift). All three are *algebra*, they reuse the one technique, and they are far better teaching than a Frobenius series. This is a real saving: it is why 4.13 fits in one chapter |
| Measurement / the Born rule | **POSTULATE, said out loud** | 4.2, revisited 4.20 | — | Not derivable. Say so in the box where it enters, and say so again in 4.20 with a fair account of what decoherence does and does not explain. `GAPS.md` §7 |

**Net for Part IV: build almost all of it.** The one substantial ⚑ is the spectral theorem, and it
is discharged into three explicit verifications. This is the right call because Part 0 has already
promised it four times in writing, and because the reader — a physician who has been told since
Chapter 0.5 that quantum mechanics *is* this linear algebra — will notice immediately if the
infinite-dimensional case is waved through.

### 3.2 · Part V — quantum field theory

| Machinery | Decision | Where | Cost | Argument |
|---|---|---|---|---|
| **Complex analysis** — Cauchy's theorem, residues, contour deformation, analytic continuation | **BUILD** | 5.4, ~½ chapter | 6–7k words | This is the largest genuinely *invisible* hole in the book. It has never been built anywhere, it has already been used once without a flag (0.9 quotes the Cauchy characteristic function as "a contour integral"), and 0.3 has promised in writing that Chapter 5.9 will read poles as particles, poles off the axis as resonances and branch cuts as thresholds. Without it, the Feynman propagator, the $\ii\epsilon$ prescription, dimensional regularisation and Wick rotation are all assertions. It is also cheap — Cauchy's theorem follows from Green's theorem, which is Chapter 0.7 — and it pays for itself immediately by evaluating the four contours that give the four Green's functions of the Klein–Gordon operator |
| Distributions, properly | **BUILD** | 5.4 | ~⅓ chapter | Chapter 0.9 handled the delta by what it does, which was right then. Field theory needs more: $\delta^{4}(x-y)$, derivatives of distributions, the distributional identity $1/(x\pm\ii\epsilon)=\mathrm{P}(1/x)\mp\ii\pi\delta(x)$ (which *is* the optical theorem in embryo), and the Fourier transform on tempered distributions. Given 0.9, this is a short build, and it closes the rigged-Hilbert-space ⚑ from 4.5 retrospectively |
| Saddle point / stationary phase | **BUILD** | 5.4 | 1 section | Used implicitly from 1.2 on ("stationary phase is the only place a wildly oscillating sum can leave a residue" — 1.2, unflagged), and the classical limit of the path integral is nothing else. It is one Gaussian integral and one Taylor expansion, both from Part 0 |
| Wigner's classification (particles = irreps of the Poincaré group) | **⚑, but state it and use it** | 5.1 | 1 section | The proof is a serious piece of representation theory. But the *statement* is the single most illuminating thing that can be said at the Part IV / Part V seam — that "particle" means an irreducible unitary representation of the symmetry group of spacetime, labelled by mass and spin, and therefore that Part II and Part IV together already dictate what kinds of particle can exist. Quote it, verify the massive and massless little groups by hand (SO(3) and ISO(2) — both elementary), and let the reader see helicity fall out |
| Canonical quantisation of the free field | **BUILD in full** | 5.3 | 1 chapter | This is 0.8's coupled oscillators with the limit taken, and the book has been advertising it since Chapter 0.8. No shortcuts |
| Spin-statistics theorem | **⚑ the general theorem, BUILD the two cases** | 5.5 | 1 section | The general theorem needs analyticity and the Wightman axioms. But both halves of the physical content are derivable with what 5.3 and 5.5 have: quantise the Dirac field with *commutators* and get a Hamiltonian unbounded below; quantise the scalar with *anticommutators* and get $[\phi(x),\phi(y)]\neq0$ at spacelike separation. Do both computations. The reader then knows exactly why the rule is what it is, and the flag sits only on "and no other possibility exists" |
| Grassmann numbers and Berezin integration | **BUILD** | 5.7 | ~⅓ chapter | Short, self-contained, and genuinely fun: the whole subject is $\theta^{2}=0$ and one convention. Note the placement change in §6 — it belongs immediately before the fermionic path integral, not three chapters earlier |
| The path-integral measure | **⚑, prominently** | 5.6 | 1 box | There is no measure on the space of paths for real time. This is not a technicality that goes away; it is the reason lattice field theory works in Euclidean signature and not in Lorentzian. Flag it where the path integral is defined, define everything by the time-sliced limit, and say that the limit's existence is verified case by case, not in general |
| Haag's theorem | **⚑, prominently, at the moment the interaction picture is introduced** | 5.8 | 1 box | The interaction picture, on which the Dyson series and every textbook derivation of the Feynman rules rests, provably does not exist for an interacting relativistic field theory. Every book uses it anyway. The reader has been promised "nothing asserted that hasn't been built" and will not forgive discovering this later. Flag it, say what the honest constructions are (LSZ, which the book will use for 5.9, and lattice regularisation), and note that this is *why* 5.9's calculation goes through LSZ rather than through the interaction picture |
| Renormalisability of the theories used | **⚑** | 5.11 | 1 box | Proved to all orders only for specific theories, by arguments (BPHZ, Zimmermann's forest formula) that are combinatorial rather than illuminating. Quote, and verify renormalisability by power counting at one loop, which the reader can do |
| Convergence of the perturbation series | **BUILD the negative result** | 5.11 | 1 section | The series is *asymptotic and divergent*, and Chapter 0.3 has already built asymptotic series honestly and said so. This is one of the places the book gets to cash a Part 0 investment for a genuinely shocking result: QED's perturbation series has zero radius of convergence, and Dyson's 1952 argument for why is two paragraphs and completely accessible |

**Net for Part V: build the mathematics, flag the field-theoretic foundations.** The distinction is
deliberate. Contour integration and distributions are *mathematics the book skipped* and can be
repaired at a known cost. Haag's theorem and the path-integral measure are *problems the subject
has not solved*, and pretending otherwise would be the first genuine dishonesty in the book.

### 3.3 · Part VI — gauge theory

| Machinery | Decision | Where | Cost | Argument |
|---|---|---|---|---|
| Lie groups, Lie algebras, the exponential map | **BUILD** | 6.1 | 1 chapter | Already planned, and by the time the reader arrives they will have met one-parameter groups five times (2.2's boosts, 2.3's rapidity, 0.5's $\ee^{\ii A}$, 1.3's generators-generate-flows, 4.11's angular momentum). 6.1's job is to notice that these were the same thing |
| Baker–Campbell–Hausdorff | **BUILD to second order, ⚑ the full series** | 6.1 | ½ section | 2.2 already ⚑'d it forward. Second order is all that is ever used (it is what produces the Thomas–Wigner rotation and the structure constants) and it is a direct computation |
| Representation theory: Schur, weights, roots, Casimirs | **BUILD, at reduced cost** | 6.2 | 1 chapter | This is only affordable because Part IV pays a large deposit: 4.11 and 4.12 build all of $\mathfrak{su}(2)$'s representation theory as *physics* (the ladder and the $(2j+1)$-fold multiplets in 4.11, Clebsch–Gordan in 4.12). 6.2 then has to do SU(3) only, and can do it by the concrete tensor method (upper and lower indices, symmetrise, remove traces) rather than by Dynkin diagrams. $\mathbf 3\otimes\bar{\mathbf 3}=\mathbf 8\oplus\mathbf 1$ becomes an index computation the reader can do. **Dynkin diagrams and the classification of simple Lie algebras: ⚑, and not used** |
| **Fibre bundles** | **BUILD the definition, ⚑ the classification** | 6.3 | 1 section | This is the decision the brief asks about, and the answer is that the book has already built the honest substitute and does not know it. A connection is "the thing that lets you compare at two nearby points" (3.3); its curvature is the commutator of covariant derivatives (3.4); $F=\dd A$ and $\dd^{2}=0$ are 3.5. Gauge theory is that construction with an *internal* index in place of a spacetime index, and every formula the reader needs — $D_\mu=\partial_\mu-\ii g A_\mu$, $F_{\mu\nu}=(\ii/g)[D_\mu,D_\nu]$, the Bianchi identity, the inhomogeneous transformation law of $A_\mu$ — is derivable by copying Part III's derivations with one substitution. That is not an analogy; it is the same computation. What bundles add is *global* structure, and given 3.2's charts and transition maps the definition of a principal bundle costs one page: it is an atlas whose transition functions take values in a group. Build that much, because it makes instantons, the $\theta$-vacuum and Dirac's monopole quantisation *statable*. ⚑ the classification (characteristic classes, $\pi_3(G)=\Z$) |
| Anomalies and the triangle diagram | **BUILD** | 6.7 | 2 sections | This is the change that turns "the Standard Model, tabulated" into "the Standard Model, cornered". The hypercharge assignments of the quarks and leptons are not arbitrary: they are the unique solution of the anomaly-cancellation conditions given the gauge group and the representation content. That is *the* structural fact about the Standard Model, and it is derivable — the triangle diagram is a one-loop calculation of exactly the kind 5.10 will have already done in full. Without it, 6.7 is a table |
| Lattice gauge theory, confinement | **⚑** | 6.5 | 1 section | Confinement is not proved. Say so plainly — it is a Millennium Prize problem — and give the reader the two things that *can* be shown: the strong-coupling expansion on a lattice, which gives an area law in three lines, and the numerical evidence. Do not let "quarks are confined" pass as a derived statement |
| Asymptotic freedom (sign of the QCD beta function) | **BUILD** | 6.5 | 2 sections | The chapter exists for this. It is affordable only because 5.10 splits off from 5.11 and computes one loop integral completely first |
| Instantons, $\theta$-vacuum, strong CP | **⚑, stated with the topology from 6.3** | 6.5 | 1 section | Chapter 0.3 already flagged $\ee^{-1/g^{2}}$ as "the part of the answer perturbation theory cannot see" and named 6.5. Collect that, state the winding number using 6.3's bundle definition, ⚑ the instanton solution itself |
| Neutrino mass, seesaw | **⚑** | 6.8 | ½ section | Beyond the Standard Model by construction; belongs in the open-questions section |

### 3.4 · Part VII — strings

| Machinery | Decision | Where | Cost | Argument |
|---|---|---|---|---|
| Conformal field theory: OPE, radial quantisation, primaries, modular invariance | **⚑ almost all of it — build only the Virasoro algebra** | 7.3 | 1 chapter, narrowed | This is where the biggest single saving is, and `PLAN.md` v2.0's 7.2 is scoped for a subject the book cannot afford. But $D=26$ does not need CFT. It needs: the residual symmetry left after conformal gauge fixing, the mode expansion, the Virasoro generators as bilinears in oscillators, and the central term computed by normal-ordering a commutator. All of that is *direct algebra* on the modes, using only 4.8's ladder operators and 5.3's field quantisation. Build that. ⚑ the operator formalism, the OPE and modular invariance, and note which later statements depend on them |
| Faddeev–Popov, ghosts, BRST | **⚑, with the $c=-26$ counted** | 7.4 | 1 section | The reader can be shown the *arithmetic* — $26$ bosonic coordinates at $c=1$ each against a ghost system at $c=-26$ — without the full machinery, provided the ghost central charge is quoted and flagged. The alternative (light-cone gauge) gets $D=26$ with no ghosts at all and *is* fully derivable. **Recommendation: derive $D=26$ in light-cone gauge, where every step is available, and give the covariant/BRST count as the flagged cross-check.** That way the headline result of Part VII is genuinely the reader's own |
| Worldsheet supersymmetry | **BUILD** | 7.6 | ~½ chapter | Two-dimensional $\mathcal N=(1,1)$ supersymmetry is tractable: two anticommuting worldsheet fields, a super-Virasoro algebra whose central charge is computed the same way as 7.4's, and $D=10$ falls out by the identical arithmetic. Grassmann numbers are already built in 5.7. This is the most satisfying possible use of that investment |
| Spacetime supersymmetry, the 4D SUSY algebra, the MSSM | **⚑** | 7.6, 7.8 | 1 box | A different subject. The reader gets: what the algebra says, why it forces equal numbers of bosons and fermions, and why it is the standard motivation for the hierarchy problem — all quoted. `GAPS.md` §7 |
| T-duality | **BUILD in full** | 7.7 | 2 sections | Genuinely derivable and short: compactify one coordinate on a circle, mode-expand, observe that momentum modes and winding modes exchange under $R\to\alpha'/R$, and check the spectrum is identical. This is the cleanest "the theory does not distinguish large from small" statement in physics and the reader can own it completely |
| D-branes | **BUILD the origin, ⚑ the dynamics** | 7.7 | 2 sections | Apply T-duality to an open string with Neumann conditions and the conditions become Dirichlet — the endpoints are stuck to a hyperplane, which was not put in. That derivation is available. The Dirac–Born–Infeld action, brane tension and brane bound states are ⚑ |
| Calabi–Yau compactification | **⚑** | 7.8 | 1 section | Algebraic geometry. State the requirement (Ricci-flat, SU(3) holonomy, from requiring an unbroken supersymmetry) and why it fixes the generation count topologically; ⚑ everything else |
| S-duality, M-theory, 11D supergravity | **⚑** | 7.8 | — | Conjectural. This is where the ledger of §10 does its work |
| Cardy formula and black-hole microstate counting | **BUILD** | 7.9 | 2 sections | The single most important "build it" decision in Part VII. The Cardy formula is usually derived from modular invariance, which has just been ⚑'d — but it can also be obtained by a **saddle-point count of oscillator states**, using only the partition function of a collection of harmonic oscillators (0.8, 4.8, 5.3) and the saddle-point method (5.4). The reader then counts the states of a D1–D5 system and gets $S=A/4$ — the number Chapter 3.9 will have quoted and left dangling. That closes the longest-running deliberate loose thread in the book, *by a calculation the reader performs*. It is worth reorganising 7.9 around |
| AdS/CFT | **⚑** | 7.9 | 1 section | A conjecture. Say so, state what evidence there is, and put it in the ledger's middle column |

---

## 4 · Part III, completed — 9 chapters

### The argument for splitting 3.7

`MATHPLAN-3.md` gives Chapter 3.7 eight numbered items: the symmetric ansatz, the full solution of
$R_{\mu\nu}=0$, conserved quantities from Killing vectors, the effective potential and the ISCO,
perihelion precession with Mercury's 43″, light bending at 1.75″ with the missing half collected,
redshift from the metric, and the coordinate-versus-genuine singularity distinction. On top of that
the written text has piled four further debts on 3.7 specifically: gravitational lensing as the
conjugate-point phenomenon (promised in 1.2 and again in 2.3), the Rindler-horizon comparison
(2.3), Clairaut's relation as a rehearsal (3.5 Problem 4), and the factor-of-two confession (3.1
§7.3, which calls it "the register of debts").

Set that against the measured working unit. The Schwarzschild solution alone — ansatz, the four
non-trivial Einstein equations, the integration, Birkhoff — is comparable to Chapter 3.6's §4, which
took three grind boxes and about 6,000 words. Perihelion precession is another 3,000 with the
numbers. Light bending with the integral done properly is 2,500. The horizon material, if it is to
be more than a paragraph, needs Eddington–Finkelstein or Kruskal coordinates and the Kretschmann
scalar, which is another 3,000. That is a 25,000-word chapter, and it would be the chapter the
reader has been walking toward for eight chapters.

The split I recommend puts *orbits* in one chapter and *light and horizons* in the next, because
that is where the physics divides — everything in 3.7 is a timelike geodesic in an effective
potential, and everything in 3.8 is either null or about the causal structure.

**Confidence: medium.** This is the least certain of my recommendations. The fallback, if the author
prefers to hold Part III at 8, is to keep 3.7 whole and grind-box the solution of $R_{\mu\nu}=0$
aggressively — the argument survives folding, the algebra does not need to be on the page. I would
not fight hard for the split; I would fight hard against a 25,000-word 3.7 with the horizon
material compressed to two paragraphs.

### 4.1 · Chapter table

| # | Slug | Title | The chapter exists to | Mathematical prerequisites (supplier) | The one result derived |
|---|---|---|---|---|---|
| 3.7 | `ch3-7` | Schwarzschild: The Solution and Its Orbits | Solve Einstein's equations for the first time, and find the orbit that Newton has no name for | Killing vectors and conserved quantities along geodesics (**3.5** §8–9); geodesic equation (**3.3** §8); $R_{\mu\nu}$ from the connection (**3.4** §6); vacuum field equations (**3.6** §5); effective-potential method and phase portraits (**0.8** §8.2, **1.3** §4.3); perturbation of a closed orbit (**1.4** WE2, the LRL vector) | **The ISCO at $r=6GM/c^{2}$, and Mercury's $43''$ per century**, both from one effective potential |
| 3.8 | `ch3-8` | Light, Redshift, and What a Horizon Is | Collect the factor of two Chapter 3.1 confessed, and distinguish a coordinate singularity from a real one | Null geodesics (**3.3** §8); the weak-field spatial metric (**3.6** Problem 3); the Kretschmann scalar from Riemann (**3.4** §5); charts and transition maps, and the fact that "the chart fails here" is not "the space fails here" (**3.2** §2); the Rindler wedge (**2.3** Problem 3) | **$1.75''$ of deflection, with the missing half identified as spatial curvature**; and $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=48G^{2}M^{2}/c^{4}r^{6}$, finite at $r_{s}$ and divergent at $r=0$ |
| 3.9 | `ch3-9` | Cosmology, and a Loose Thread | Put the largest possible source on the right-hand side, and leave one number deliberately unpaid | Perfect-fluid $T^{\mu\nu}$ and the radiation equation of state (**3.6** §1.3); the field equations (**3.6** §5); null geodesics (**3.3**); absence of a timelike Killing vector (**3.5** §8), which collects **1.4** §4.3's honest note; separable first-order ODEs (**0.8** §2.1) | **The Friedmann equations, and the statement that energy is not conserved in an expanding universe** — not as a puzzle but as a direct consequence of Noether's theorem having no symmetry to work with |

### 4.2 · What 3.9 must promise so Part IV can collect

See §9.1. In short: 3.9's closing section is the one place in the book where the reader can be told,
before it happens, that Parts IV–VI are done on flat spacetime and that gravity does not reappear
until 7.1 — and *why* that is not a cheat but the actual state of physics.

---

## 5 · Part IV — Quantum Mechanics, 20 chapters

**Two revisions, and both are recorded here.** §§5.1–5.2 argue Part IV up from `PLAN.md` v2.0's
eight chapters to eleven, and the argument is about *content*: debts Part 0 wrote that 4.3 cannot
pay alone, an ordering bug that puts hydrogen before the angular momentum it needs, and a missing
perturbation-theory chapter that three chapters have already promised.
`reports/part4-replan.md` then takes the eleven to **twenty**, and that argument is about *pacing*
rather than content: measured against the written 4.1–4.3, the eight chapters still unwritten were
carrying eleven new objects each where the book's own rate is five or six, so 4.4–4.11 are cut into
4.4–4.20 with **nothing dropped anywhere**. Three objects are added, two of them things the written
text had already promised and the old plan had no build item for — the rotating-wave reduction and
the selection rules, both in 4.17. §5.3 is the twenty-chapter table; §11 carries the batches.

### 5.1 · The three arguments for expanding

**(a) Chapter 4.3 is owed six separate debts and cannot pay them in one chapter.**

Written into the text of Part 0, by name, are the following promises to Chapter 4.3:

- 0.2: the Riemann integral will be "thrown away and rebuilt from scratch (the Lebesgue integral)"
- 0.2: dominated convergence "proved properly in Chapter 4.3"
- 0.5: the projection form of the spectral theorem "survives to infinite dimensions in Chapter 4.3"
- 0.5: "Chapter 4.3 pays this bill in full" — the continuous spectrum, projection-valued measures,
  and re-proving completeness
- 0.5, closing: "Quantum mechanics happens in infinite dimensions. Chapter 4.3 is where the bill
  comes due" — listing four separate places finite-dimensionality was used
- 0.6: unbounded operators, "$\dv{}{x}$ being the standard offender"
- 0.9, twice: completeness of the Fourier basis, and the fact that $\ee^{\ii kx}\notin L^2$

Seven, in fact. Chapter 0.5 spent 13,100 words on the *finite-dimensional* spectral theorem alone.
One chapter cannot do the infinite-dimensional case plus measure theory plus the Fourier debts.
*(The seven sentences are quoted as they stood on 18 August 2026, when every one of them named
Chapter 4.3. Three were paid by 4.3 as written; the other four have since been re-aimed to 4.4 and
4.5, and `GAPS.md` G1 carries the current table.)*

The split follows the precedent the book has already set and which worked: **0.4 built the space,
0.5 built the operators on it.** 4.3 builds the space (L², completeness, the Fourier basis as an
honest orthonormal basis at last); **4.4 and 4.5** build the operators — 4.4 the domains, the
adjoint's own domain and the difference between symmetric and self-adjoint, 4.5 the spectrum, the
spectral theorem, the meaning of $\ket x$ and $\ket p$, and Stone. A reader who has done 0.4 and 0.5
will recognise the shape immediately, which is itself worth something.

**(b) There is an ordering bug: hydrogen is scheduled before the angular momentum it requires.**

`PLAN.md` v2.0 puts "hydrogen in full" in 4.5 and "angular momentum and spin, SU(2), the algebra"
in 4.7 — v2.0's numbering, in which those are now **4.13** and **4.11**–**4.12**.
The hydrogen atom cannot be solved without separating the angular part, and separating the angular
part *is* the representation theory of $\mathfrak{su}(2)$. Under any other book's rules this would
be a scheduling inconvenience. Under this book's rule — nothing asserted that hasn't been built —
it is a violation, and the reader who has been trained by twenty-five chapters to check exactly
this will catch it. **Angular momentum must precede hydrogen.**

Once it does, hydrogen deserves its own chapter, because with the algebra in hand it can be done
properly: the radial equation, the factorisation that produces the radial ladder, the exact
spectrum, the degeneracy, and then the collection of Chapter 1.4's SO(4) promise — *the accidental
degeneracy of hydrogen is the quantum shadow of the closed Kepler orbit, and 1.4 ⚑'d it forward
by name.* That is a chapter with a thesis, not a worked example — two of them, in the end:
**4.13** derives the spectrum and leaves the degeneracy as a question, and **4.14** answers it by
deriving the same spectrum a second time from $\mathfrak{so}(4)$.

**(c) Perturbation theory is absent, and three chapters have already promised it.**

`PLAN.md` has no perturbation theory anywhere. But: 0.3's Worked Example 2 flags the relativistic
$p^{4}/8m^{3}c^{2}$ correction and cannot yet explain it; 2.5 §3.3 repeats the flag and says
"Chapter 4.16 computes the full splitting"; 1.3 ⚑'s the adiabatic theorem forward to Part IV. And structurally, Part V's Dyson
series is time-dependent perturbation theory in a relativistic costume — the reader who meets the
interaction picture for the first time in 5.8, in a field theory, with Haag's theorem hanging over
it, has been set up to fail. They should meet it first in ordinary quantum mechanics, where the
Hilbert space is concrete and Fermi's golden rule can be checked against a real transition rate.

This is also where `PLAN.md`'s best Familiar Ground row finally lands: the survival function
$S(t)=\exp(-\int_0^t h(\tau)\dd\tau)$ and the Dyson series are the same object, and the reader
should meet that identity in 4.17 — in ordinary quantum mechanics — so that when it recurs in 5.8
it is a recognition rather than an introduction.

### 5.2 · The one restructuring, not an addition

`PLAN.md` v2.0's 4.6 ("Commutators, Uncertainty, the Classical Limit" — v2.0's numbering; the
material is now split between **4.9** and **4.10**) is thinner than it looks, and the
book says so itself. Chapter 0.5, having proved Cauchy–Schwarz, states: *"That inequality, applied
to two particular vectors assembled from a state and a pair of measurements, is the uncertainty
principle… nothing is added to it afterwards except an interpretation of the letters."* Chapter 0.9
proves the bandwidth theorem and calls it the uncertainty principle outright. Chapter 0.5 §8 proves
simultaneous diagonalisation of commuting operators.

So the uncertainty relation and compatible observables are *already done*. Rebuilding them in Part
IV would be the one thing this book has never done — repeating itself. The chapter's real remaining
content is the **classical limit**, which is substantial and which three chapters have promised:
Ehrenfest's theorem, the WKB approximation, the Hamilton–Jacobi equation as the $\hbar\to0$ limit
(1.3 ⚑'d this explicitly), the Bohr–Sommerfeld condition (1.3 ⚑ again), and the
Groenewold–van Hove obstruction that says the correspondence cannot be made exact (1.3 ⚑ a third
time). That is a chapter, and it is a better one. **Same count, different content, and the
uncertainty material is *spent* in twenty minutes rather than re-derived.**

### 5.3 · Chapter table

| # | Slug | Title | The chapter exists to | Mathematical prerequisites (supplier) | The one result derived |
|---|---|---|---|---|---|
| 4.1 | `ch4-1` | What Classical Physics Cannot Do | Make the failures quantitative, so that quantisation is forced rather than proposed | Boltzmann distribution and the partition function (**0.6** WE1); mode counting in a box (**0.7**, **0.8** §7); Rayleigh–Jeans from equipartition; Compton kinematics (**2.5** WE1) | **The Planck spectrum, derived Einstein's way** — A and B coefficients plus detailed balance plus 0.6's Boltzmann weights — with the ultraviolet catastrophe shown to be a divergent integral, not a metaphor |
| 4.2 | `ch4-2` | The Linear Algebra of Quantum States | Show that Chapter 0.5 was quantum mechanics with the physics stripped off, and put the physics back | Everything in **0.5**: inner products, adjoints, Hermitian and unitary, the spectral theorem, projections, commuting observables, $\ee^{\ii A}$; tensor products (**0.4**) | **The postulates, as a table of renamings** — plus the one genuinely new input, the Born rule, announced as a postulate in its own box and not smuggled |
| 4.3 | `ch4-3` | Function Spaces: Measure, L², and Completeness ※ | Rebuild the integral so that the space of states is actually a space | Riemann integral and its failure on $\chi_{\Q}$ (**0.2** §1); **note that Cauchy sequences have never been defined anywhere in this book — `grep` finds only Cauchy–Schwarz, the Cauchy distribution and Cauchy's functional equation — so 4.3 must define completeness from scratch rather than cite it**; inner product on function spaces (**0.5** §1); Fourier series and the completeness ⚑ (**0.9** §1.3); Cauchy sequences and convergence (**0.3**) | **L² is complete, and the Fourier basis is a basis** — closing 0.9's ⚑ and 0.2's promise in one chapter |
| 4.4 | `ch4-4` | Domains, and the Adjoint's Domain ※ | Show that in infinite dimensions an operator is not a formula but a formula *together with a domain*, and that the domain is forced rather than chosen | All of **4.3**; the finite-dimensional spectral theorem and its proof (**0.5** §6); integration by parts and its boundary term (**0.2** §3.2); the closed graph theorem, ⚑, for Hellinger–Toeplitz | **A symmetric operator need not be self-adjoint** — worked on the particle in a box, whose deficiency indices $(2,2)$ give a $U(2)$ of extensions, so the boundary condition is physics; and on momentum on a half-line, which has no extension at all, so it is not an observable |
| 4.5 | `ch4-5` | The Spectral Theorem in Infinite Dimensions ※ | Replace 0.5's $A=UDU^{\dagger}$ with the statement that survives, verify it everywhere the book will use it, and give $\ket x$ and $\ket p$ a meaning | **4.4**'s domains and adjoints; Fourier transform as a unitary map (**0.9** §2.3); the delta (**0.9** §5); dominated convergence (**4.3** §4.3) | **The spectral theorem in multiplication-operator form, ⚑ and then checked by hand on $\hat x$, $\hat p$ and $\hat H_{\text{osc}}$** — with the Hermite functions *proved* complete rather than quoted, and Stone's forward direction built. This is the one substantial mathematical flag of Part IV |
| 4.6 | `ch4-6` | The Schrödinger Equation | Get the equation from two things already built — a unitary flow with a self-adjoint generator, and one physical identification | Stone and $\ee^{-\ii\hat Ht/\hbar}$ (**4.5** §9, **0.5** §7); continuity equation (**0.7** §6); Fourier transform and group velocity (**0.9** §3); Gaussian integral (**0.2** §4); dispersion (**0.8** §7.6) | **The probability current and $\partial_t\rho+\nabla\cdot\vv J=0$** — the same continuity equation as 0.7, which is what makes "the wavefunction stays normalised" a theorem rather than a hope |
| 4.7 | `ch4-7` | Wells, Barriers, and Tunnelling | Turn the equation into numbers on the problems that matching conditions solve exactly, and show that the boundary condition is a choice the reader watched being made | Boundary conditions as domain choices (**4.4** §7); second-order linear ODEs (**0.8** §3); the delta (**0.9** §5); the probability current (**4.6** §8) | **$T+R=1$ from the current, not from hand-waving**, with the transmission through a 1 eV barrier computed exactly — and parity introduced as the first *symmetry ⇒ commuting observable ⇒ label* move, which 4.11 then runs on rotations |
| 4.8 | `ch4-8` | The Oscillator, and the Ladder | Do the oscillator by algebra, because that method — not the answer — is the whole of Parts V and VII | Adjoints and the ladder algebra (**0.5**); Hermite completeness, cited not re-proved (**4.5** §4); phase-space area (**0.8** §4.4, **1.3** §4.4); the Gaussian bound (**0.9** §6.5) | **$E_n=(n+\half)\hbar\omega$ from the ladder algebra alone**, with no differential equation solved — collecting 0.8's phase-space-area calculation and 1.3's Bohr–Sommerfeld ⚑ |
| 4.9 | `ch4-9` | Commutators, Uncertainty, and Symmetry | *Spend* the uncertainty relation rather than re-derive it, and show that the commutator which bounds a product of spreads also generates the motion | Cauchy–Schwarz and the uncertainty inequality, already proved (**0.5** §1, **0.9** §6); Poisson brackets and generators (**1.3** §§6–7); the canonical commutator (**4.2** §8) | **$\Delta A\,\Delta B\ge\half\lvert\langle[\hat A,\hat B]\rangle\rvert$ in one line, then the Heisenberg equation and Ehrenfest's theorem** — the largest single block of debts in Part IV, most of them paid in a sentence each, which is the point |
| 4.10 | `ch4-10` | The Classical Limit | Say honestly how classical mechanics emerges, recover Bohr–Sommerfeld from a real approximation scheme, and then prove the correspondence cannot be exact | Hamilton–Jacobi (**1.3** §8.2); asymptotic series (**0.3** §4); stationary phase, ⚑ until **5.4**; phase-space area (**4.8**) | **The Hamilton–Jacobi equation as the $\hbar\to0$ limit of Schrödinger** — collecting 1.3's ⚑ — followed by Groenewold–van Hove with the $\tfrac13\hbar^{2}$ obstruction computed on the page rather than quoted |
| 4.11 | `ch4-11` | The Angular Momentum Algebra | Build the reader's first Lie algebra from a commutator they can compute, and derive the whole spectrum from it and nothing else | $[\hat L_i,\hat L_j]=\ii\hbar\epsilon_{ijk}\hat L_k$ from the canonical commutators (**4.2** §8); the classical bracket version already computed (**1.3** Problem 2, **1.4** §7.3); the ladder technique (**4.8**) | **$2j$ a whole number, $\hat{\vv J}^{2}=j(j+1)\hbar^{2}$, $2j+1$ states — from the algebra alone.** The chapter carries no ⚑ at all, which is 1.4's *"from nothing but that algebra"* met literally |
| 4.12 | `ch4-12` | Spin, Orbitals, and Adding Angular Momenta | Find out which of 4.11's representations nature uses, discover one with no wavefunction at all, and learn to add two of them | **4.11**'s multiplets and matrix elements; $\ee^{\ii\theta\sigma_x}$ (**0.5** WE2); tensor products (**0.4**, **4.2**) | **The spherical harmonics from $\hat L_+Y_\ell^{\ell}=0$ and no series anywhere**, and with them the half-integer representations that force the $720^{\circ}$ rotation — the fact 0.5 said was "already visible coming" |
| 4.13 | `ch4-13` | The Hydrogen Atom | Solve the one system whose exact solution built the subject, using the ladder for the third time | Separation of variables; spherical harmonics from **4.12**, not from a series; radial factorisation (the ladder trick again, **4.8**); reduced mass (**1.1**) | **$E_n=-13.6\,\mathrm{eV}/n^{2}$, and the fact that it depends on $n$ alone** — derived, and then left as a puzzle, because the rotational symmetry used to derive it cannot explain the degeneracy it produces |
| 4.14 | `ch4-14` | The Degeneracy, and $SO(4)$ | Answer the question 4.13 ended on, and derive the same spectrum a second time from an algebra | The LRL vector and its $SO(4)$ algebra, computed classically (**1.4** WE2); **4.11** applied twice; addition of angular momenta (**4.12** §5) | **$n=2j+1$ and a degeneracy of $(2j+1)^{2}=n^{2}$, as a dimension count** — the accidental degeneracy as the quantum shadow of the closed Kepler orbit, collecting 1.4's ⚑ by name |
| 4.15 | `ch4-15` | Perturbation Theory | Build the approximation scheme the rest of the book runs on, in the one setting where it can be checked against an exact diagonalisation | Small-parameter and asymptotic series (**0.3** §4); degenerate eigenvalue problems (**0.5** §6); the spectral decomposition (**4.5** §5) | **$E_a^{(2)}=\sum_{b\ne a}\lvert V_{ab}\rvert^{2}/(E_a-E_b)$, with the residual against exact diagonalisation scaling as $\lambda^{3}$** — and the series then shown to be asymptotic, by Dyson's argument, which pre-pays `GAPS.md` G12 |
| 4.16 | `ch4-16` | The Fine Structure of Hydrogen | Compute the three corrections of relative order $\alpha^{2}$ and print the residual against measurement | **4.15**'s degenerate machinery; $\hat{\vv L}\cdot\hat{\vv S}$ (**4.12**); the relativistic expansion (**0.3** WE2, **2.5** §3.3); the radial expectation values (**4.13**) | **$E_{n,j}$ — three separate corrections combining into one formula that depends on $j$ and not on $\ell$**, collecting 0.3's and 2.5's promise of the full splitting |
| 4.17 | `ch4-17` | Transitions | Do perturbation theory when the Hamiltonian depends on time, where the group law fails and the exponential becomes a series | The interaction picture; the delta as a limit (**0.9** §5); the Dirac comb and $\sin^{2}$ kernel; $B_{12}=B_{21}$ and detailed balance (**4.1**); parity (**4.7**) | **Fermi's golden rule**, derived and then checked against a numerically integrated two-level system — and the **Dyson series recognised as the survival function** $S(t)=\exp(-\int h)$, with time-ordering as the only new ingredient |
| 4.18 | `ch4-18` | Identical Particles | Show that "these two are the same kind of thing" is a statement with arithmetic consequences | Tensor products (**0.4**, **4.2**); the symmetric group on two letters; Boltzmann statistics to contrast with (**0.6** WE1); the mode count of **4.1** | **The Pauli principle as a corollary of the Slater determinant, and the Planck law a second time** — from occupation numbers, closing the loop 4.1 opened by deriving it Einstein's way instead |
| 4.19 | `ch4-19` | Density Matrices and Entanglement | Build the object that answers "what is the state of *this half*", and show by computation that it transmits nothing | The trace inner product $\operatorname{tr}(A^{\dagger}B)$ (**0.5** §1 table); projections and P7 (**4.2**); probability and correlation (**0.9** §7) | **Half a singlet is $\half\hat I$, and no-signalling proved rather than asserted** — with entanglement *defined* by $\operatorname{tr}\hat\rho_A^{2}<1$ rather than described. The chapter carries no ⚑ |
| 4.20 | `ch4-20` | Bell, Decoherence, and What Is Settled | Turn "could they have had definite values all along" into a number, and close Part IV by saying precisely what has and has not been explained | **4.19**'s reduced states; the spin algebra (**4.12**); Cauchy–Schwarz (**0.5** §1); correlation of two measurements (**0.9** §7) | **Bell's inequality, derived and then violated** — with the singlet correlation $-\cos\theta$, the Tsirelson bound $2\sqrt2$ derived rather than quoted, and an honest statement of what is and is not thereby settled |

### 5.4 · Fallback if the count is too many

*Written against the eleven-chapter plan, and superseded by `reports/part4-replan.md`, which caps
every chapter at about six new objects and finds no merge that survives the cap — and which points
out that the renumbering cost is paid in full at the first split, so there is no saving in splitting
less. Kept because the trade it names is still the first one to make if the count ever has to come
down.*

If Part IV must hold at 10: merge 4.9 and 4.10 — now **4.13**/**4.14** and **4.15**–**4.17** — into
one chapter, "The Hydrogen Atom and Its Corrections", grind-boxing the radial factorisation and
treating perturbation theory as the tool that produces the fine structure rather than as a subject.
The cost is that Fermi's golden rule loses its own section and the survival-function identity has to
be made in passing. I would accept that trade before I would accept merging 4.3 and 4.4 — now 4.3
and the pair **4.4** + **4.5**.

---

## 6 · Part V — Quantum Field Theory, 11 chapters

### 6.1 · Two structural changes, and the argument for each

**(a) The path integral must come before the Feynman rules, not after.**

`PLAN.md` orders: quantise canonically (5.3) → Dirac (5.4) → Gaussian/Grassmann machinery (5.5) →
interactions and Feynman rules canonically (5.6) → a real calculation (5.7) → *then* the path
integral (5.8), which "recovers everything above".

That ordering has the reader derive the Feynman rules once by the canonical route, and then be told
the whole thing can be done again more cleanly. It also puts the Grassmann machinery three chapters
before anything anticommutes in an integral. Both violate the doctrine that the tool arrives when
the physics demands it (`PLAN.md` §2, item 1: "No object is ever introduced as a definition out of
the blue").

Worse, it walks into Haag's theorem. The canonical derivation of the Feynman rules runs through the
interaction picture, which does not exist. The path-integral derivation runs through the generating
functional, which has its own problem (no measure) but at least has a definition by limits that
the reader can inspect.

**Correction, 19 August 2026.** `MATHPLAN-4.md` found that this table routes Chapter 1.3's
canonical-quantisation promises to 4.7, but 4.5, 4.6 and 4.8 all need the commutator before then —
and §5.3's own 4.8 row already assumes the earlier delivery. **The canonical commutator is
introduced in 4.2, as a postulate in its own box.** 4.7 then spends it rather than introducing it.
*(Numbers as they stood on 19 August 2026. Under the twenty-chapter Part IV the spender is **4.9**,
and the three chapters needing the commutator first are **4.6**, **4.7**–**4.8** and
**4.11**–**4.12**. The decision itself stands: P6 is stated in 4.2 §8, and 4.9 spends it.)*

Revised order: canonical quantisation first (because it makes "a field is infinitely many
oscillators" concrete and cashes Chapter 0.8), then Dirac, then the path integral as the language,
then Grassmann immediately before it is needed for fermions, then the Feynman rules read off the
generating functional, then a full calculation.

**(b) The renormalisation chapter must split.**

`PLAN.md`'s 5.9 carries regularisation, renormalisation, the running coupling, the renormalisation
group and effective field theory. That is two chapters by the measured working unit — and the
constraint is downstream: Chapter 6.5 exists to **compute the sign of the QCD beta function**. You
cannot do that unless one loop integral has already been evaluated completely, with the divergence
isolated and a regulator derived rather than announced. If 5.10 does not do that in full, 6.5's
headline result becomes a quoted number, and Part VI loses its best derivation.

### 6.2 · Chapter table

| # | Slug | Title | The chapter exists to | Mathematical prerequisites (supplier) | The one result derived |
|---|---|---|---|---|---|
| 5.1 | `ch5-1` | Why Quantum Mechanics and Relativity Force Fields | Show that the two theories already built are jointly inconsistent unless particle number is allowed to change | Four-momentum and the mass shell (**2.5** §4); the Schrödinger equation's asymmetry between $\partial_t$ and $\nabla^{2}$ (**4.6**); probability current (**0.7** §6, **4.6**); light cones and spacelike separation (**2.3** §4) | **The Klein–Gordon negative-probability problem, and its resolution** — plus the localisation argument: confining a particle to $\Delta x<\hbar/mc$ costs enough energy to make another one. Wigner's classification stated (⚑) with the massive and massless little groups verified by hand |
| 5.2 | `ch5-2` | Classical Field Theory | Run Chapter 1.2 and Chapter 1.4 again with a continuous index, and get a stress-energy tensor that Part III had to assume | Euler–Lagrange and the fundamental lemma (**1.2** §3); Noether's theorem (**1.4** §2, §6); the continuity equation (**0.7** §6); the field-theoretic $T^{\mu\nu}$ already built once for electromagnetism (**2.6** §10) | **The Noether current for a general field symmetry, and $\partial_\mu T^{\mu\nu}=0$** — the object Chapter 3.6 put on the right-hand side of Einstein's equations, now derived rather than assembled |
| 5.3 | `ch5-3` | Quantising a Field | Take Chapter 0.8's coupled-oscillator limit seriously and discover that its quanta are particles | Normal modes and the $N\to\infty$ limit (**0.8** §7); ladder operators (**4.8**); Fourier expansion in a box (**0.9**); canonical quantisation (**1.3** §6.4) | **$a^{\dagger}_{\vv k}$ creates a particle of momentum $\hbar\vv k$** — with the vacuum energy $\half\hbar\omega$ per mode summed, shown to diverge, and the Casimir force extracted from the *difference*, which is finite and measured |
| 5.4 | `ch5-4` | Distributions, Contours, and the Propagator ※ | Build the two pieces of mathematics the book has been using on credit, and cash them immediately | Green's theorem (**0.7** §5) → Cauchy's theorem; the delta as a functional (**0.9** §5); Fourier transforms (**0.9**); Gaussian integrals (**0.2** §4); asymptotic expansion (**0.3** §4) | **The four Green's functions of the Klein–Gordon operator as four contours around the same two poles** — retarded, advanced, Feynman, Dyson — with the $\ii\epsilon$ prescription derived as a contour choice rather than announced as a rule |
| 5.5 | `ch5-5` | The Dirac Equation | Take the square root of the Klein–Gordon operator and be forced into antiparticles | Clifford algebra from $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$; $\mathfrak{su}(2)$ and half-integer representations (**4.11**, **4.12**); Lorentz generators as antisymmetric matrices (**2.3**, **2.2** ⚑); the mass shell (**2.5**) | **Antiparticles fall out of the negative-energy solutions, and the electron's $g=2$** — the latter derived, not quoted, which is the cleanest single victory in Part V. Spin-statistics: the general theorem ⚑, both physical failures computed |
| 5.6 | `ch5-6` | The Path Integral | Replace the operator formalism with a sum over histories, and recover everything so far | Stationary action (**1.2**); Hamilton–Jacobi and $\ee^{\ii S/\hbar}$ (**1.3** §8.2, **4.10**); Gaussian integrals in many variables (**0.2** §4, **0.6** §8); saddle point (**5.4**); the Kaplan–Meier-style product of conditionals (Familiar Ground) | **$\braket{x_f,t_f\,\vert\,x_i,t_i}=\int\mathcal Dx\,\ee^{\ii S/\hbar}$ from time-slicing**, with the free-particle propagator computed exactly and shown to agree with 4.6. The non-existence of the measure ⚑'d in place |
| 5.7 | `ch5-7` | Gaussian and Grassmann Integration ※ | Build the algebra of anticommuting numbers at the moment fermions need it | Multidimensional Gaussians and $\det$ (**0.4** §5, **0.2** §4); parameter differentiation as a source (**0.2** §4.4); determinants as signed volume (**0.4** §5) | **$\int\dd\theta\,\dd\bar\theta\,\ee^{-\bar\theta A\theta}=\det A$** — the determinant upstairs rather than downstairs, which is the entire reason fermion loops carry a minus sign |
| 5.8 | `ch5-8` | Interactions, Wick's Theorem, and the Feynman Rules | Derive the rules rather than receive them, and be honest about the foundation | Generating functional $Z[J]$ (**5.6**, **5.7**); parameter differentiation (**0.2** §4.4); convolution and Green's functions (**0.9** §4); the Dyson series as a time-ordered survival function (**4.17**) | **Every Feynman rule, read off $Z[J]$ by functional differentiation** — with Wick's theorem proved combinatorially and Haag's theorem flagged in place |
| 5.9 | `ch5-9` | A Real Calculation | Take one process from Lagrangian to number, with nothing skipped and nothing quoted | Everything above; Mandelstam $s$ and the centre-of-momentum frame (**2.5** §8); the Lorentz-invariant phase-space measure; the Breit–Wigner curve, already derived as a driven oscillator (**0.8** §6.4) | **One differential cross section, computed and compared with data** — $\ee^{+}\ee^{-}\to\mu^{+}\mu^{-}$, chosen because every ingredient is available and the answer is measured to four figures |
| 5.10 | `ch5-10` | Loops, Divergences, and Regularisation | Compute a divergent integral honestly and isolate exactly what diverges | Contour integration and Wick rotation (**5.4**); Feynman parametrisation; $\Gamma$-function analytic continuation (**5.4**); power counting and dimensional analysis (**0.3** §5) | **One loop integral evaluated in full in $d=4-\epsilon$ dimensions**, with dimensional regularisation *derived* — the $d$-dimensional Gaussian is 0.2's integral with a different exponent — rather than declared |
| 5.11 | `ch5-11` | Renormalisation and the Renormalisation Group | Explain why physics is possible without knowing everything | **5.10**'s divergence; asymptotic and divergent series (**0.3** §4); scaling and dimensional analysis (**0.3** §5); the flow picture from phase space (**1.3** §4) | **The running coupling $\alpha(\mu)$ from the Callan–Symanzik equation**, plotted for QED and QCD on the same axes — the plot that is the whole punchline of Part VI. Dyson's argument that the series has zero radius of convergence, derived |

---

## 7 · Part VI — Gauge Theory and the Standard Model, 8 chapters

### 7.1 · The argument for splitting 6.7

`PLAN.md`'s 6.7 is "The Standard Model, Assembled — the full Lagrangian, term by term, each one
explained. Then: gravity, hierarchy, dark matter, neutrino mass, 19 free parameters."

"Term by term, each one explained" is tabulation, and this book does not tabulate. The question the
reader will actually have is *why this and not something else* — why three colours, why the weak
force acts only on left-handed fields, why the hypercharges are the peculiar numbers they are, why
there is a Cabibbo angle at all.

Two of those have real answers the book can derive:

1. **The hypercharges are forced by anomaly cancellation.** Given the gauge group and the
   representation content of one generation, the requirement that the gauge symmetry survive
   quantisation is a set of algebraic conditions whose unique solution (up to normalisation) is the
   observed hypercharge assignment — including the otherwise inexplicable $-1/3$ and $+2/3$. That
   is a derivation, it is available once 5.10 has done a one-loop triangle, and it is the single
   most persuasive structural fact about the Standard Model.
2. **The CKM matrix is forced by the mismatch of two bases.** Once the Yukawa couplings are written
   down, the mass eigenbasis and the weak eigenbasis are different bases of the same space, and the
   unitary matrix relating them is the CKM matrix. Its parameter count — three angles and one phase
   — is Chapter 0.4's change-of-basis argument plus a phase-removal count, and it is *why* CP
   violation requires three generations. Derivable.

Neither fits in a chapter that is also introducing the electroweak gauge group, deriving the
Weinberg angle, and computing $M_W/M_Z=\cos\theta_W$. Hence the split: 6.7 builds the electroweak
theory and derives its structure; 6.8 assembles, counts the free parameters, and lists what is
unexplained. 6.8 then becomes what it should be — the chapter that motivates Part VII — rather than
a Lagrangian printed in small type.

### 7.2 · Chapter table

| # | Slug | Title | The chapter exists to | Mathematical prerequisites (supplier) | The one result derived |
|---|---|---|---|---|---|
| 6.1 | `ch6-1` | Lie Groups and Lie Algebras ※ | Name the structure the reader has met five times without being told what it was | One-parameter families and $\ee^{\phi K}$ (**2.2** ⚑, **2.3** §3.1); generators generating flows (**1.3** §7); $\ee^{\ii A}$ Hermitian ⇒ unitary (**0.5** §7); $\det\ee^{A}=\ee^{\mathrm{tr}A}$ (**0.4** §6); Poisson-bracket and commutator algebras (**1.4** §7.3, **4.11**) | **$\mathfrak{su}(N)$ has $N^{2}-1$ generators** — collecting 0.4's traceless-generator count and delivering the eight gluons as an arithmetic consequence rather than a fact |
| 6.2 | `ch6-2` | Representations ※ | Explain why matter comes in the multiplets it does | Irreducibility and Schur's lemma; $\mathfrak{su}(2)$ representation theory, **already built as physics** (**4.11**, **4.12**); tensors with upper and lower indices (**2.4** §5); Casimirs from commuting operators (**0.5** §8) | **$\mathbf 3\otimes\bar{\mathbf 3}=\mathbf 8\oplus\mathbf 1$, by index gymnastics the reader can do** — and with it the meson octet, which is why the hadrons of the 1960s organised themselves |
| 6.3 | `ch6-3` | The Gauge Principle | Demand a symmetry locally and watch a force appear to enforce it | The global U(1) current (**1.4** §6.2, **2.6** ⚑); the covariant derivative as the repair for a non-tensorial derivative — **the identical argument, with an internal index** (**3.3** §4–5); $F=\dd A$ and $\dd^{2}=0$ (**3.5** §2–3); minimal coupling from the Legendre transform (**1.3** WE1) | **Electromagnetism, generated** — $D_\mu=\partial_\mu-\ii eA_\mu$ forced by demanding local phase invariance, and $\vv p\to\vv p-e\vv A$ recognised as the thing 1.3 derived classically. Aharonov–Bohm phase derived, closing 0.7's and 1.3's ⚑s |
| 6.4 | `ch6-4` | Yang–Mills | Do the same with a group whose elements do not commute, and find that the force carries its own charge | **6.1**, **6.2**, **6.3**; the curvature of a connection as a commutator (**3.4** §2 — the same computation, index for index); the Bianchi identity (**3.4** §7) | **$F_{\mu\nu}^{a}$ with its quadratic term, and the self-interaction that follows** — the structural difference between a photon and a gluon, derived from one commutator |
| 6.5 | `ch6-5` | QCD and Asymptotic Freedom | Compute the sign that changes everything | One-loop integrals in full (**5.10**); the running coupling and Callan–Symanzik (**5.11**); Casimirs of SU(3) (**6.2**); non-analytic terms $\ee^{-1/g^{2}}$ (**0.3** §4) | **$\beta(g)<0$, with the coefficient $11-\tfrac23 n_f$ computed** — the gluon self-coupling of 6.4 overwhelming the fermion screening, and the plot of 5.11 explained. Confinement ⚑'d honestly, with the strong-coupling area law as the one thing that can be shown |
| 6.6 | `ch6-6` | Spontaneous Symmetry Breaking and the Higgs Mechanism | Give a gauge boson a mass without breaking the symmetry that forbade it | Critical points classified by the Hessian (**0.6** §6.3); normal modes and zero-frequency modes (**0.8** §7); degenerate ground states; the gauge freedom of **6.3** | **Goldstone's theorem, and then its evasion** — the massless mode of a global symmetry is eaten by the gauge field, and the counting of degrees of freedom before and after is shown to balance exactly |
| 6.7 | `ch6-7` | The Electroweak Theory | Derive the structure that looks arbitrary, and show it is not | **6.6**; chirality and left-handed projections (**5.5**); the triangle diagram (**5.10**); change of basis and phase counting (**0.4** §4) | **The hypercharge assignments, forced by anomaly cancellation** — with $M_W=M_Z\cos\theta_W$ falling out of the same symmetry breaking, and the CKM matrix's three angles and one phase counted, which is why CP violation needs three generations |
| 6.8 | `ch6-8` | The Standard Model, and What It Does Not Explain | Say what has been built, count what has not, and hand the reader the motivation for Part VII | Everything above | **The nineteen free parameters, enumerated and grouped by where they come from** — followed by the five things the theory does not contain, each stated precisely enough to be a research problem rather than a complaint |

---

## 8 · Part VII — Strings and M-Theory, 9 chapters

### 8.1 · Two structural changes

**(a) The string comes before the conformal field theory.**

`PLAN.md` orders 7.2 (2D conformal symmetry) then 7.3 (the bosonic string). Reverse it. The book's
method is that mathematics arrives when the physics has *asked a question it cannot answer*
(`PLAN.md` §2, item 1), and Part III is the proof that this works: manifolds arrived because the
arrow-in-a-background picture had broken, connections arrived because vectors at different points
could not be compared. Conformal symmetry should arrive the same way — write the Polyakov action,
gauge-fix using worldsheet diffeomorphisms and Weyl invariance, and *discover* that the gauge
fixing has not used up all the freedom. The residual symmetry is infinite-dimensional, and that is
the question the CFT chapter answers.

Presented the other way round, the reader spends a chapter on Virasoro algebras before knowing what
a string is, which is exactly the failure mode Part 0 was expanded to avoid.

**(b) T-duality and D-branes get their own chapter.**

`PLAN.md`'s 7.7 carries D-branes, T-duality, S-duality, the unification of the five theories with
11D supergravity, compactification, Calabi–Yau, and the landscape. Two of those are *derivable in
full* — T-duality is a mode-expansion calculation on a circle, and the existence of D-branes follows
from applying T-duality to open-string boundary conditions — and the rest are not derivable at all.
Mixing them in one chapter means the reader cannot tell which is which, which is precisely the
failure Part VII is supposed to avoid. Split them, and the split does the honesty work for free:
7.7 is a chapter of derivations, 7.8 is a chapter of flagged conjectures.

### 8.2 · Chapter table

| # | Slug | Title | The chapter exists to | Mathematical prerequisites (supplier) | The one result derived |
|---|---|---|---|---|---|
| 7.1 | `ch7-1` | Why Quantum Gravity Is Hard | Diagnose the failure precisely, by counting, rather than gesturing at it | Power counting and dimensional analysis (**0.3** §5, where $\ell_P$ was already computed); the nonlinearity of $G_{\mu\nu}$ (**3.6** §7.3); renormalisation by power counting (**5.10**, **5.11**); Ostrogradsky's theorem (**1.2** ⚑, **3.6** ⚑) | **$[G]=\mathrm{length}^{2}$ ⇒ a new counterterm at every order**, computed — and then the reason the obvious repair fails: higher-derivative terms buy a ghost, which is the Ostrogradsky flag now collected |
| 7.2 | `ch7-2` | The Bosonic String | Write the most general action for a one-dimensional object and gauge-fix it | Reparametrisation-invariant actions and the relativistic point particle $S=-mc^{2}\!\int\!\dd\tau$ (**2.5** §5, **3.3** §3); induced metrics (**3.3**); constrained systems (**1.3** ⚑); the volume element $\sqrt{-g}$ (**3.5** §6) | **Polyakov's action, and the mode expansion in conformal gauge** — with the demonstration that Weyl plus diffeomorphism invariance is *just* enough freedom to reach the flat worldsheet metric, and not quite all of it is used |
| 7.3 | `ch7-3` | Conformal Symmetry and the Virasoro Algebra ※ | Answer the question 7.2 asked: what freedom is left after gauge fixing | **7.2**'s residual symmetry; Lie algebras and central extensions (**6.1**); ladder operators (**4.8**); normal ordering (**5.3**) | **$[L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}m(m^{2}-1)\delta_{m+n,0}$, with the central term computed by hand** from the oscillator commutators — no operator-product expansion required. OPE, radial quantisation and modular invariance ⚑'d and their uses named |
| 7.4 | `ch7-4` | Quantising the String, and D = 26 | Let the reader produce the most famous number in the subject themselves | **7.3**; light-cone gauge; the zero-point sum $\sum n$ and its $\zeta$-regularisation, set against the honest cut-off computation; Lorentz algebra closure (**6.1**) | **$D=26$**, derived in light-cone gauge where every step is available, from the requirement that the Lorentz algebra close — with the covariant/BRST ghost count given as the flagged cross-check |
| 7.5 | `ch7-5` | The Spectrum | Show that gravity was not put in | **7.4**'s mass formula; representations of the little group (**5.1**'s Wigner ⚑, now spent); massless field content (**2.6**, **3.6**) | **A massless spin-2 state in the closed-string spectrum** — identified as a graviton because a massless spin-2 field has only one possible low-energy action, which is Chapter 3.6's. This is the chapter the book exists for |
| 7.6 | `ch7-6` | Superstrings and D = 10 | Remove the tachyon, and get fermions, by the same arithmetic that gave 26 | Grassmann numbers (**5.7**); worldsheet fermions; super-Virasoro (**7.3**'s method again); GSO projection | **$D=10$, by the identical central-charge count as 7.4** — the most satisfying possible reuse of 7.3's machinery. Spacetime supersymmetry ⚑'d and kept out of the derivation |
| 7.7 | `ch7-7` | T-Duality and D-Branes | Derive two things nobody would have guessed, using only the mode expansion | **7.2**'s mode expansion; compactification on a circle; winding number as a topological label (**0.7** §2.4's counterexample, **3.5** §4.3) | **$R\leftrightarrow\alpha'/R$ with momentum and winding exchanged, and the spectra shown identical** — followed by the observation that T-dualising an open string turns Neumann into Dirichlet, so a D-brane is not postulated, it is forced |
| 7.8 | `ch7-8` | Compactification, Dualities, M-Theory | Present the structure honestly, with every step's status marked | **7.7**; Kaluza–Klein towers, derivable; Calabi–Yau conditions, stated; S-duality, quoted | **The Kaluza–Klein tower, derived in full** — the one thing in this chapter that is a calculation — with everything else placed in the §10 ledger by name. This chapter's honesty ratio is the test of whether Part VII works |
| 7.9 | `ch7-9` | Black Hole Entropy, Holography, and the Accounting | Count the states of a black hole, and then state exactly where the building ends | **7.7**'s D-branes; the microcanonical count $S=\ln W$ (**0.6** WE1); saddle point (**5.4**); the oscillator partition function (**4.8**, **5.3**); $S=A/4$ as quoted in **3.9** | **$S=A/4$, obtained by counting oscillator states** via a saddle-point evaluation of the D1–D5 degeneracy — closing the loose thread 3.9 deliberately left. Then the ledger of §10, in full |

---

## 9 · The seams

Four joins, each of which is where a reader loses a book if it is done badly.

### 9.1 · III → IV — what Part III must promise so Part IV can collect

Chapter 3.9's closing section is the handoff, and it has four jobs.

1. **Say that Parts IV–VI are done on flat spacetime, and why that is not a cheat.** The reader has
   just spent nine chapters learning that spacetime is dynamical. They are about to spend
   twenty-five chapters in which it is not. Unaddressed, this reads as the book quietly abandoning
   its own result. Addressed, it is a genuine physical statement: the curvature scale near anything
   the reader cares about is $10^{-23}\,\mathrm{m^{-2}}$ (Chapter 3.4 §4.5 computed it), so flat
   spacetime is not an approximation of convenience but an approximation with a measured error bar,
   and Chapter 7.1 is where it fails.

2. **Hand forward the action, explicitly.** Chapter 3.3 kept $S=-mc^{2}\!\int\!\dd\tau$ and changed
   only how $\dd\tau$ is computed. Chapter 1.3 already told the reader that the phase of a
   wavefunction is the classical action over $\hbar$. Chapter 3.9 should state the connection as a
   promise: *the quantity you have been extremising is the quantity that will be exponentiated*, and
   name 5.6.

3. **Hand forward the symmetry machinery.** Killing vectors give conserved quantities along
   geodesics (3.5 §9); commuting Hermitian operators give simultaneous quantum numbers (0.5 §8).
   Both are "symmetry ⇒ label". Part IV should be told in advance that its quantum numbers are
   Part III's Killing vectors in a different costume, so that 4.11's $\mathfrak{su}(2)$ arrives as a
   recognition.

4. **Leave $S=A/4$ visibly unpaid.** This is already in `MATHPLAN-3.md` and is the right decision.
   Add one sentence naming Chapter 7.9 and saying what will be counted.

### 9.2 · IV → V — where relativity and quantum mechanics are stitched

The stitch is Chapter 5.1, and the standard framing ("QM + SR = QFT") is wrong and should not be
used. What is actually true is that **quantum mechanics, plus Lorentz invariance, plus locality,
plus a lowest-energy state, forces fields** — and each of those four is doing work:

- *Lorentz invariance* alone gives the Klein–Gordon equation and its negative-energy solutions.
- *A lowest-energy state* is what makes those solutions intolerable and forces reinterpretation.
- *Locality* (operators at spacelike separation commute) is what forces antiparticles to exist with
  exactly the mass of the particle — this is derivable and should be derived.
- *Quantum mechanics* supplies $\Delta E\,\Delta t\gtrsim\hbar$, which combined with $E=mc^{2}$
  makes particle number unfixable.

The strongest single thing that can be said at this seam is Wigner's: a particle *is* an irreducible
unitary representation of the Poincaré group, labelled by mass and spin. Part II built the group;
Part IV built unitary representations; the classification is the statement that they have already,
between them, determined what kinds of particle can exist. Quote the theorem, verify the little
groups, and the seam becomes the payoff rather than the join.

The second stitch is technical and belongs in 5.3: the field operator $\hat\phi(\vv x)$ is not an
operator, it is an operator-valued distribution, and Chapter 4.5's rigged-Hilbert-space flag is
where that was foreseen. Collect it.

### 9.3 · V → VI — how the Standard Model gets motivated rather than tabulated

Three moves, in order.

1. **Present the gauge principle as a repetition, not a novelty.** The reader has already built a
   connection, in Chapter 3.3, as the answer to "the ordinary derivative of a vector field is not a
   tensor, so define whatever object cancels the offending term". Chapter 6.3 should open by running
   the *identical* argument with an internal phase in place of a coordinate index, and the reader
   should recognise every line. Then the punchline lands: *you built electromagnetism in Chapter
   3.3 and did not know it.* Curvature, the Bianchi identity, the inhomogeneous transformation law
   of the connection — all four are copied across with one substitution.

2. **Derive the structure that looks arbitrary.** Three colours, left-handed doublets, the
   hypercharges, the Cabibbo angle. Anomaly cancellation and basis mismatch account for two of the
   four; say plainly that three colours is measured (from $R$ in $\ee^{+}\ee^{-}$, and from the
   $\pi^{0}$ decay rate — both quotable experiments with derivable predictions) and that the
   left-handedness of the weak interaction is measured and unexplained.

3. **End with a count, not a Lagrangian.** Nineteen parameters, grouped: three gauge couplings
   (running, and the reader has computed one of the runnings), nine charged-fermion masses, four
   CKM parameters, two Higgs parameters, one $\theta_{\text{QCD}}$. Each group should be traceable
   to the chapter that introduced it. Then five failures, precisely stated. That is the motivation
   for Part VII, and it is honest because it is arithmetic.

### 9.4 · VI → VII, and how Part VII stays honest

`PLAN.md` §6 already promises that every quoted step in Part VII carries a ⚑. That is necessary and
not sufficient, because by Part VII the reader will have seen 150 flags and stopped counting. What
Part VII needs is a **ledger**, maintained across all nine chapters and printed in full in 7.9, with
three columns and nothing in between.

**Derived here** — the reader has done the calculation and could redo it:
the power-counting failure of quantised GR (7.1); the Polyakov action and its gauge fixing (7.2);
the Virasoro algebra with its central term (7.3); $D=26$ (7.4); the massless spin-2 state and its
identification as the graviton (7.5); $D=10$ (7.6); T-duality and the necessity of D-branes (7.7);
the Kaluza–Klein tower (7.8); the microstate count giving $S=A/4$ (7.9).

**Conjectured** — the mathematics is incomplete or the statement is a conjecture with evidence:
the equivalence of the five superstring theories under duality; the existence of M-theory as a
theory rather than as a name for a web of limits; AdS/CFT; the finiteness of superstring
perturbation theory beyond low genus; the non-perturbative definition of the theory at all.

**Untested** — no experiment distinguishes this from its absence:
supersymmetry at any accessible scale; extra dimensions at any accessible scale; the entire
string scale; every prediction that survives compactification; the landscape and any statistical
argument built on it.

Then a fourth section, which is not a column: **fairly stated alternatives.** Loop quantum gravity,
asymptotic safety, causal set theory — each in a paragraph, each with its strongest claim and its
sharpest difficulty, and no thumb on the scale. `PLAN.md` §6 already asks for this and it should be
written by someone who would be content to have it read by a proponent of each.

The test for whether Part VII has worked: **a reader should be able to answer, for any statement in
it, which column it is in — without looking it up.** That is achievable only if the columns are
declared at the start of 7.1, not assembled at the end of 7.9.

---

## 10 · The honest ledger, as a maintained artefact

The ledger of §9.4 should not be written once at the end. It should be a file — `LEDGER-VII.md` —
appended to as each chapter of Part VII ships, and rendered into 7.9 by extraction, exactly as
`throughline.py` extracts the plain-terms passages. That way it cannot drift, and the discipline of
having to file each claim in a column while the chapter is being written is what keeps the chapter
honest.

The same argument applies one level up: `GAPS.md` should be regenerated, not hand-maintained. A
short script that greps `src/ch*.html` for the flag character and the forward-reference pattern and
emits the tables would keep it current for the cost of one build step, and would catch the case
that matters most — a debt that was promised to a chapter and quietly not paid when that chapter
shipped.

---

## 11 · Revised batch schedule

The Part III experience is the guide: two chapters per agent, and the hardest math chapters (3.3,
3.4) not paired with anything. Applying that forward, with three-chapter batches only where the
material is light or continuous:

| Batch | Contents | Ch | Notes |
|---|---|---|---|
| **F1** | 3.7 + 3.8 | 2 | Schwarzschild and its consequences. Write `MATHPLAN-3.7-3.9.md` first |
| **F2** | 3.9 + Part III reunification pass | 1 | Plain-terms continuity pass across all of Part III (per `PLAIN-TERMS-PLAN.md` §7) |
| **F3** | 4.1 + 4.2 | 2 | The crisis, and the translation of Chapter 0.5 |
| **F4** | 4.3 | 1 | **Alone.** The measure-theory chapter is the 3.3 of Part IV |
| **F5** | 4.4 + 4.5 | 2 | The two halves of one repair — the domains, then the spectrum. One agent: item 1 of each is the same sentence split |
| **F6** | 4.6 + 4.7 | 2 | The equation, then the first systems it solves |
| **F7** | 4.8 + 4.9 | 2 | The ladder, then the commutator that generates it |
| **F8** | 4.10 + 4.11 | 2 | The classical limit, then the first Lie algebra |
| **F9** | 4.12 + 4.13 | 2 | Spin and addition, then the atom that needs both |
| **F10** | 4.14 | 1 | **Alone.** Five symbolic identities and a representation-theoretic argument — the 3.4 of this stretch |
| **F11** | 4.15 + 4.16 | 2 | The tool, then the case that decides it |
| **F12** | 4.17 + 4.18 | 2 | |
| **F13** | 4.19 + 4.20 + Part IV reunification | 2 | Plain-terms continuity pass across all of Part IV (per `PLAIN-TERMS-PLAN.md` §7) |
| **F14** | 5.1 + 5.2 | 2 | |
| **F15** | 5.3 + 5.4 | 2 | 5.4 is a math chapter; consider splitting the batch if it runs long |
| **F16** | 5.5 + 5.6 | 2 | Dirac, then the path integral |
| **F17** | 5.7 + 5.8 | 2 | Grassmann, then the Feynman rules |
| **F18** | 5.9 | 1 | **Alone.** The full calculation must not be rushed |
| **F19** | 5.10 + 5.11 | 2 | |
| **F20** | 6.1 + 6.2 | 2 | Part V reunification pass runs alongside |
| **F21** | 6.3 + 6.4 | 2 | |
| **F22** | 6.5 + 6.6 | 2 | |
| **F23** | 6.7 + 6.8 | 2 | |
| **F24** | 7.1 + 7.2 | 2 | Part VI reunification pass runs alongside. Start `LEDGER-VII.md` |
| **F25** | 7.3 + 7.4 | 2 | **The hardest batch in the book.** Consider one per agent |
| **F26** | 7.5 + 7.6 | 2 | |
| **F27** | 7.7 + 7.8 | 2 | |
| **F28** | 7.9 + full reunification + final `GAPS.md` regeneration | 1 | |

**51 chapters, 28 batches**, numbered `F1`–`F28` so as not to collide with `PLAN.md` §7's original
sixteen. **The Part IV batches were renumbered when the part was re-cut from eleven chapters to
twenty**: the old `F5`–`F9` (and `F8b`) become `F5`–`F13`, and every batch from Part V onward moves
up by four. The batches do not double — sixteen chapters of 9,000–12,000 words pair naturally where
the old plan's twenty-thousand-word chapters could not, so three extra batches carry nine extra
chapters. Dedicated mathematics chapters in the remainder: 4.2, 4.3, 4.4, 4.5, 5.4, 5.7, 6.1, 6.2,
7.3 — nine, against fifteen already written, bringing the book's total to **24 of 76**, or 32% —
close to the ratio `PLAN.md` §0 committed to (21 of 59, 36%) and which Parts I–III vindicate.

**Three mechanical tasks that had to happen before batch F3, not during it** — all three were done
in August 2026, and the Part IV re-plan required the first two a second time:

1. **Update `build.py`'s `PARTS` list**, which is the authoritative curriculum and which the index
   hub, the chapter navigation and the progress count all read from. The renumbering of Parts IV–VII
   touches every entry from `ch4-1` onward.
2. **Remap the forward references.** `GAPS.md` §4 counted 390 references in the written text to
   chapters that did not exist, and the renumbering invalidates roughly half of them. This is a
   single scripted pass with a hand-checked mapping table, and it must be done before Part IV is
   written rather than after, because new chapters will immediately add more.
3. **Extract the debt list per chapter and put it in that chapter's brief.** See `GAPS.md` §7 — this
   is the highest-value process change available, and it is a five-line script. It exists:
   `debts.py`.

**And the first two again before batch F5**, per `reports/part4-replan.md`: apply the promise remap
of its Deliverable 2 in one commit; regenerate `python3 debts.py 4.N` for every N from 4 to 20; and
confirm `build.py`'s `PARTS` list carries the twenty Part IV titles. The remap surface is larger
than `debts.py` alone reports — `src/_ledger.html`'s "spent in" cells, the plural runs
(*"Chapters 4.6, 4.8 and 4.11"*), `GAPS.md` and `STATUS.md` are all outside the per-chapter report,
and the ledger is the one most easily forgotten because nothing in the toolchain reads it.

**Two further process changes, both cheap:**

- **Write the math plan before the batch, not with it.** `MATHPLAN-3.md` is why Part III came out
  well. There should be a `MATHPLAN-4.md`, `MATHPLAN-5.md`, `MATHPLAN-6.md` and `MATHPLAN-7.md`,
  each written and reviewed before its first batch starts. The Part IV plan is the urgent one and
  should be written before batch 19, not before batch 20.
- **Regenerate `GAPS.md` at the end of every batch**, and check that every debt naming a
  just-shipped chapter has been struck. A promise that quietly expires is worse than one that was
  never made, because the reader remembers.

---

## 12 · Where I am uncertain

Recorded so that these are read as judgements rather than findings.

1. **The 3.7 split is the weakest recommendation here.** The case rests on word count and debt load,
   both of which can be managed by aggressive grind-boxing. If the author's instinct is that Part
   III should end at 8 chapters for shape, that instinct may be right and the cost is one dense
   chapter rather than a structural problem.

2. **Whether 4.3 and 4.4 should be one chapter or two is genuinely close.** Two is right if the
   Lebesgue integral is built. If the author decides instead to ⚑ the integral wholesale and work
   with $L^{2}$ as a completion (which is defensible, and which is what most physics texts do), then
   one chapter suffices — but three explicit promises in Part 0 would then need to be revisited and
   the ⚑ made prominent. I would not make that choice silently. *(Settled: two. And the operators
half has since become two chapters of its own, 4.4 and 4.5 — see `reports/part4-replan.md` §1.)*

3. **The light-cone route to $D=26$** gives the reader a complete derivation but hides where the
   $-26$ actually comes from. The covariant route shows the structure but needs Faddeev–Popov. My
   recommendation is light-cone-primary, covariant-as-check, but a reader who wants to understand
   *why* 26 rather than to *compute* 26 is better served the other way round. This is a real trade
   and the author should make it deliberately.

4. **The Cardy-by-saddle-point route in 7.9** is the recommendation I am least sure is executable at
   the level of rigour the book demands. The counting is available; whether it can be connected to
   the specific D1–D5 degeneracy without importing more supersymmetry than 7.6 builds is something
   I would want to prototype before committing the chapter to it. The fallback is to compute the
   *free-string* oscillator degeneracy exactly — which is Hardy–Ramanujan and is beautiful and
   complete — and quote the D-brane bookkeeping that connects it to the horizon area.

5. **I have assumed the reader wants Part V's foundational problems flagged rather than avoided.**
   Haag's theorem and the non-existence of the path-integral measure are true, load-bearing, and
   almost universally suppressed in textbooks. A reader who has asked for nothing to be asserted
   will want them. A reader who wants to *learn field theory* might be better served by a footnote.
   Given everything in the twenty-five written chapters, I am confident it is the former — but it is
   an assumption about a person, not a fact about physics.
