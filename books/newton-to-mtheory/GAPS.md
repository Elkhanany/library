# GAPS

## The register of what this book has not built

*Version 1.0 — 18 Aug 2026 — compiled against `src/ch0-1.html` … `src/ch3-6.html`, the
twenty-five chapters written to date.*

---

## 0 · What this document is

The book is written under one rule: nothing is asserted that has not been built. That rule is kept
far more often than it is broken, but it is not kept absolutely, and it cannot be. This file is the
honest accounting of the difference.

It exists because the rule is only as good as the register that goes with it. A ⚑ in the text tells
you that *this* step was quoted. It does not tell you how many there are, whether they cluster,
whether any of them could be closed, or which of them the book has promised to come back for and
has not. That is what this file is for. **Read it as the floor plan of the building with the
unfinished rooms marked.**

### The four classes

| | Class | Meaning | Should it ever close? |
|---|---|---|---|
| **E** | Experimental input | A measurement. Not derivable from anything, by anyone, ever | No. Quoting it is correct |
| **M** | Mathematical theorem quoted | True, provable, and the proof was judged not worth its cost here | Only if the cost falls |
| **F** | Forward debt | Quoted now, promised to a named later chapter | **Yes — and this file tracks whether it did** |
| **D** | Deferred permanently | Named, not developed, no chapter owes it | No, but the reader should know it is there |
| **A** | Assumption in disguise | A physical assumption presented as a mathematical convenience | It should at least be relabelled |

**E is not a gap.** Quoting Michelson and Morley's fringe count is not a failure of rigour; it is
what the word "physics" means. The E entries are listed for completeness and are not ranked.

**F is the class that matters**, because an F that is never collected silently becomes a D, and the
reader — who was told a chapter number — has no way to know.

### The census, as of 25 chapters

- **178 ⚑ marks**, across 28 of the 31 chapters (recount with
`sum of ⚑ over src/ch*.html` after every batch — this line fed forward into chapter briefs while it
said 126). (This was 117 when the register was first written;
  the review pass of August 2026 added nine, eight of them in Part 0 — see the note below.)
- **Four chapters carry none**: 0.1, 0.3, 0.5 and — as a real fact rather than an oversight — no
  chapter in Parts I to III. Chapter 3.5 carried none until the review found that its general-$p$
  Poincaré lemma was asserted on a sketch; it now carries one, and the rest of that chapter —
  forms, Lie derivatives, Killing vectors, generalised Stokes — remains derived end to end.
- **The Part 0 correction.** The register's first edition recorded that chapters 0.1–0.7 carried no
  flags at all, and read that as a clean bill. It was the opposite: those chapters import
  Heine–Cantor, Fubini, Liouville on elementary antiderivatives, the fundamental theorem of algebra,
  the implicit function theorem, Picard–Lindelöf, generalised Stokes and the Poincaré lemma, several
  of them announcing the fact in words while carrying no mark. A reader who had learned to scan for
  ⚑ would have read Part 0 as fully derived when it was not. All eight are now flagged. This is the
  single most useful thing the review found, and it is the reason this file exists.
- The distribution is lumpy and the lumps are informative. Chapter 2.1 carries 20, of which
  seventeen are experimental — that is the chapter whose entire subject is what the nineteenth
  century measured. Chapter 3.1 carries 10, of which all ten are experimental — the equivalence
  principle is an experimental fact and the chapter says so nine separate times. Chapter 1.3 carries
  10, of which four are permanent deferrals, and that is the one distribution in the book that is a
  warning rather than a description.
- Approximate split: **E ≈ 45, M ≈ 35, F ≈ 27, D ≈ 10**, with the remaining ~8 being cross-references,
  attributions of wording, or internal pointers rather than quoted results. The classification is a
  judgement and reasonable people would move a handful of entries.

### How to maintain this file

Regenerate it at the end of every batch. The two commands that matter:

```bash
grep -c '⚑' src/ch*.html                       # the flag census
python3 debts.py --census                      # every debt naming an unwritten chapter
```

Use the script, not a bare grep. Since Part IV runs to 4.20, `grep -o 'Chapter [4-7]\.[0-9]'` reads
*Chapter 4.20* as *Chapter 4.2* and files the debt against a written chapter; and it cannot see the
plural form — *"Chapters 4.6, 4.8 and 4.11"* — at all. `debts.py` handles both.

When a chapter ships, check §4 for every debt naming it and strike or re-file each one. **A debt
that quietly expires is worse than one that was never incurred**, because the reader remembers being
told a chapter number.

---

## 1 · The ranked register

Ranked by **what the gap costs the reader** — how much of what they have been told rests on it —
not by how hard it would be to close. A gap that is trivial to fix and load-bearing outranks a gap
that is impossible to fix and decorative.

### G1 · The spectral theorem in infinite dimensions — seven promises, four still due

**Cost: severe. This is the largest outstanding debt in the book.**

Chapter 0.5 proves the spectral theorem in finite dimensions and then tells the reader, in its own
words, that *"every postulate of quantum mechanics is a statement about Hermitian operators on an
inner-product space… not modelled by, not analogous to — is."* That claim is the load-bearing wall
of the whole design: Part 0 is nine chapters long because the mathematics is supposed to *be* the
physics, and Chapter 4.2 is supposed to be "a translation exercise: a table of renamings, not a new
subject".

Every word of that is true in finite dimensions and none of it is proved in infinite dimensions,
which is where quantum mechanics happens. Chapter 0.5's closing paragraph says so directly:
*"Every proof above used finite dimension — in the induction, in rank–nullity, in the interchange of
sums, in the claim that an injective map is surjective. Quantum mechanics happens in infinite
dimensions. Chapters 4.4 and 4.5 are where the bill comes due."*

Seven separate promises were made in writing. **Chapter 4.3, now written, paid three of them; the
remaining four fall to Chapters 4.4 and 4.5**, and every one of the quoted sentences has been
re-aimed in the text to say so:

| Promised in | The promise | Due at |
|---|---|---|
| 0.2 §1 | *"In Chapter 4.3 we will throw away and rebuild the integral from scratch (the Lebesgue integral)"* | **Paid, 4.3** |
| 0.2 §4.4 | Dominated convergence *"proved properly in Chapter 4.3"* | **Paid, 4.3** |
| 0.5 §6 | The projection form $A=\sum_k\lambda_kP_k$ *"is the one that survives to infinite dimensions in Chapter 4.5"* | **4.5** |
| 0.5 §6 | Continuous spectra, $\int\lambda\,\dd P(\lambda)$ over projection-valued measures, completeness re-proved — *"Chapter 4.5 pays this bill in full"* | **4.5** |
| 0.6 §2 | Unbounded operators, *"$\dv{}{x}$ being the standard offender"* | **4.4** |
| 0.9 §1.3 | Completeness of the Fourier basis — the ⚑ | **Paid, 4.3** |
| 0.9 §5.3 | $\ee^{\ii kx}\notin L^{2}$: *"the difficulty Chapter 4.5 has to work to make legitimate"* | **4.5** |

**Can it be closed with the tools the book has?** Partly. L², completeness of an orthonormal system,
unbounded operators, domains and the distinction between symmetric and self-adjoint are all fully
derivable from Part 0 plus one quoted measure. The spectral theorem for unbounded self-adjoint
operators is not — its proof is three or four chapters of analysis.

**Cost to close:** two chapters — **4.4** for the domains and the adjoint, **4.5** for the spectrum
(see `PLAN-FORWARD.md` §5). The residual ⚑ should be the spectral theorem itself, stated in multiplication-operator form and then *verified by hand* on the only three
operators the book ever applies it to — $\hat x$, $\hat p$ (via Fourier), and the oscillator
Hamiltonian (via Hermite completeness). That leaves the reader holding a quoted theorem they have
personally checked everywhere it is used, which is the best available outcome.

**The risk if it is not closed properly:** this is the one place where softening the promise would
retroactively damage Part 0. The reader was sold nine chapters of mathematics on the strength of
this payment.

### G2 · Complex analysis has never been built — and the reader cannot see the hole

**Cost: severe, and invisible, which makes it worse than G1.**

There is no Cauchy's theorem in this book. No residues, no contour deformation, no analytic
continuation, no Laurent series. `grep` finds: `Cauchy's theorem` 0 hits, `analytic continuation` 0,
`Laurent` 0, `holomorphic` 0, `contour integr` 1 — and that one hit is Chapter 0.9 evaluating the
characteristic function of the Cauchy distribution and writing *"(a contour integral, quoted here)"*
**with no ⚑ at all.**

Meanwhile Chapter 0.3 has promised, in some detail, what Part V will do with it:

> *"In Chapter 5.9 a scattering amplitude is treated as an analytic function of complex energy, and
> then: poles on the real axis are stable particles, poles just off it are resonances with lifetimes
> given by the imaginary part, and branch cuts are thresholds where new particles can be produced."*

None of that is available. Nor is the Feynman propagator, whose entire content is *which way you go
around two poles*; nor the $\ii\epsilon$ prescription; nor Wick rotation as anything more than a
substitution; nor dimensional regularisation, which is analytic continuation in the number of
dimensions.

**Can it be closed?** Yes, and cheaply. Cauchy's theorem follows from Green's theorem, which is
Chapter 0.7 §5. The residue theorem is one Laurent expansion. Analytic continuation needs the
identity theorem, which is one more page. This is perhaps 6,000 words of genuinely elementary
material that the book skipped because Parts I–III never needed it.

**Cost to close:** half a chapter, and it pays for itself the same afternoon by producing the four
Green's functions of the Klein–Gordon operator as four contours around the same two poles. See
`PLAN-FORWARD.md` §6, chapter 5.4.

**Also missing from the same family:** the saddle-point / stationary-phase method. Chapter 1.2 says,
in the main text and unflagged, that *"stationary phase is the only place a wildly oscillating sum
can leave a residue"* — which is a correct and beautiful statement of a theorem the book has not
proved. It is needed again for the classical limit of the path integral and for the state count in
7.9.

### G3 · Quantum statistics and the density of states — half-built, and unowned

**Cost: high, and it bites on the first page of Part IV.**

Chapter 0.6's Worked Example 1 derives the Boltzmann distribution and the partition function from
maximum entropy and two Lagrange multipliers, and it is one of the best things in Part 0 — it
obtains the microcanonical postulate as a *theorem* rather than an assumption. That is a substantial
down-payment on statistical mechanics.

What is not built anywhere, and is not scheduled anywhere in the 59-chapter plan:

- the density of states / mode counting in a box (Chapter 0.8 §7.6 gets close, in the $N\to\infty$
  limit, but never counts modes per unit frequency);
- Bose–Einstein and Fermi–Dirac occupation numbers;
- the Planck spectrum.

Chapter 4.1 exists to make the failures of classical physics *quantitative*, and the first of the
four is the blackbody spectrum. Without a density of states there is no Rayleigh–Jeans law to
diverge, and without quantum statistics there is no Planck law to replace it.

There is also a **circularity** if this is not handled deliberately: Bose–Einstein statistics
requires the symmetrisation postulate, which requires identical particles, which is the last chapter
of Part IV.

**Can it be closed?** Yes, elegantly, and the resolution is better physics than the usual route.
Derive the Planck law **Einstein's way** — A and B coefficients, detailed balance, and Chapter 0.6's
Boltzmann weights. That uses only what the book has, needs no quantum statistics at all, and
produces stimulated emission as a by-product. The occupation-number distributions then arrive
properly in 4.18 once exchange symmetry exists.

**Cost to close:** one section in 4.1, one in 4.18. No new chapter. See `PLAN-FORWARD.md` §3.1.

**Downstream:** the whole black-hole entropy thread — $S=A/4$ quoted in 3.9, counted in 7.9 — is a
statistical-mechanics calculation, and 0.6's $S=\ln W$ is the only foothold the book currently has
for it.

### G4 · The fundamental theorem of algebra, imported ~~without a flag~~ — flagged, August 2026

**Cost: high relative to how easy it is to state.** *(The flag was added in the review pass; the
gap itself is unchanged, and this entry stays because the gap, not the marking, is the point.)*

Chapter 0.4 §7, establishing that every square complex matrix has an eigenvalue:

> *"By the fundamental theorem of algebra, every non-constant polynomial with complex coefficients
> has a complex root. (This is the one result in this chapter we import rather than prove; it is a
> theorem of complex analysis…)"*

The chapter is candid about it, and then does not flag it. It is the only load-bearing quoted result
in the whole of Part 0's linear algebra, and everything downstream stands on it: Step 1 of Chapter
0.5's spectral theorem proof is *"Because $V$ is complex, [0.4] supplies an eigenvalue"*. Remove the
theorem and the spectral theorem falls, and with it every measurement postulate in Part IV.

**Can it be closed?** Not without complex analysis — the shortest honest proofs are Liouville's
theorem or a winding-number argument. But **once G2 is closed in Chapter 5.4, this becomes a
three-line corollary**, and the book could go back and collect it. That would be a satisfying
closure: the deepest unproved statement in Part 0, paid off in Part V by machinery built for a
different purpose.

**Minimum action, and it cost nothing:** put a ⚑ on it. Done — `src/ch0-4.html` now opens that
parenthesis with the mark. The reader is entitled to know, and now does.

### G5 · Constrained Hamiltonian systems — declared not-to-be-built, and then declared universally necessary

**Cost: high, and it is a decision the author should make now rather than in Part VII.**

Chapter 1.3 ⚑'s the failure of the Legendre transform when the Hessian $W$ is degenerate:

> *"the transform is not invertible and the system is called constrained. Dirac built a whole
> formalism for that case; it is quoted here and not developed, but you should know it is where
> gauge theories live (Chapter 6.3: the Lagrangian of electromagnetism has no $\dot A_0$ at all) and
> where the reparametrisation-invariant string action lives (Chapter 7.3). **Every fundamental
> theory in Part VI and VII is a constrained system**, so the honest statement is: the clean
> Legendre transform of this section is the easy case, and it is the only case we do."*

That paragraph is completely honest and it is also a problem. It says: a tool needed by every
remaining fundamental theory in the book will not be built. Chapter 3.6 §7.2 then meets constraints
again, from the other side — four of Einstein's ten equations are constraints, and the chapter
handles it well — without connecting it back.

**Three options, and the author should pick one deliberately:**

1. **Build it** — primary and secondary constraints, first and second class, Dirac brackets — as a
   section in 6.3 where gauge redundancy is the subject anyway. Cost: two sections. This also
   collects Chapter 1.4's ⚑ on **Noether's second theorem**, which is the statement that a symmetry
   with function-valued parameters gives identities rather than conservation laws, and which is why
   6.3 *cannot* simply run 1.4 §6 again.
2. **Route around it** — path-integral gauge fixing via Faddeev–Popov, which does not require the
   Hamiltonian constraint analysis. Viable, but then 7.2's string action has no Hamiltonian
   treatment and the Virasoro constraints have to be introduced by hand.
3. **Leave it deferred** and say so once, prominently, in 6.3 — that the book works in the
   Lagrangian and path-integral formalisms throughout Parts VI and VII precisely because the
   Hamiltonian one requires machinery not built.

Option 3 is honest and cheap. Option 1 is best. Option 2 is what will happen by default if no choice
is made, and it will happen silently, which is the worst outcome.

### G6 · Haag's theorem — the interaction picture does not exist

**Cost: high when Part V arrives; currently zero because Part V has not been written.**

Listed now because it is structurally guaranteed. The Dyson series, the interaction picture, and
every textbook derivation of the Feynman rules rest on a picture that provably does not exist for an
interacting relativistic field theory. Almost every book uses it anyway without comment.

A reader who has been promised that nothing is asserted without being built, and who has been trained
by twenty-five chapters to check exactly this kind of thing, will not forgive discovering it
afterwards. **It must be flagged at the moment the interaction picture is introduced**, together
with what the honest constructions are (LSZ reduction; lattice regularisation), and it should
determine the route Chapter 5.9's real calculation takes.

### G7 · The path-integral measure does not exist

**Cost: high when Part V arrives.**

There is no measure on the space of paths in Lorentzian signature. The path integral is defined by a
time-sliced limit whose existence is checked case by case, not in general. Chapter 1.2 has already
made a gesture at the neighbourhood of this problem — noting that variations need only be smooth
"almost everywhere", *"which is exactly the loophole that permits collisions, shocks, and the kinked
worldlines of Chapter 5.8's path integral"* — which is a good sign that the author is aware. It needs
a flag at the definition, and it should be connected to why Euclidean (Wick-rotated) field theory is
mathematically better behaved than the real-time theory.

### G8 · The Cauchy problem for Einstein's equations — never mentioned

**Cost: moderate, and rising once 3.7 solves an equation.**

`grep` finds zero occurrences of `Cauchy problem`, `initial value formulation`, `globally
hyperbolic`, or `geodesic completeness`.

Chapter 3.6 §7 counts ten equations and four identities and identifies which four are constraints,
which is the initial-value formulation in embryo and is done well. But nowhere does the book say
that the Einstein equations have a well-posed initial-value problem — that is Choquet-Bruhat's
theorem, 1952 — nor that the solution is unique only up to diffeomorphism, nor that the maximal
development may be geodesically incomplete, which is what a singularity theorem is about.

The reader currently has no reason to believe Einstein's equations have solutions at all, and is
about to be shown one. Chapter 3.7 should say, in one paragraph with a ⚑, that existence and
uniqueness hold, under what conditions, and in what sense.

**Can it be closed?** No — the proof is a book. **Cost to flag: one paragraph.**

### G9 · Smoothness is assumed everywhere, and physics is not smooth

**Cost: moderate, concentrated in Part III and Part V.**

The book assumes $C^{\infty}$ throughout: Lagrangians (1.2, explicitly: "with $L$ smooth"), metrics
and manifolds (3.2, 3.3), fields. That is the right working assumption. Three places where it is
doing real and unstated work:

1. **Junction conditions.** `grep` finds `junction` twice, neither in the relevant sense. Chapter 3.7
   will produce the Schwarzschild exterior; matching it to a stellar interior requires the metric to
   be $C^{1}$ but not $C^{2}$ across the surface, with a distributional Ricci tensor there. Not
   mentioned. Any reader who asks "so what is the metric *inside* the Sun?" hits this immediately.
2. **Shocks and caustics.** Chapter 3.4 §4.1 constructs a one-parameter family of geodesics and
   differentiates freely along both parameters. That assumes the congruence is smooth and free of
   caustics. At a caustic — which is exactly the gravitational lensing that Chapters 1.2 and 2.3
   have both promised to 3.7 — the separation vector degenerates and the derivation's hypotheses
   fail. Worth one sentence in 3.4 and a proper treatment in 3.8.
3. **Path-integral paths are nowhere differentiable.** Flagged obliquely in 1.2 (see G7).

### G10 · Torsion-free is an assumption about nature, wearing mathematical clothes

**Cost: moderate. Class A — the only clear instance in the book.**

Chapter 3.3 derives the Christoffel formula from two demands: metric compatibility and vanishing
torsion. The second is ⚑'d, and the flag is scrupulous:

> *"That general relativity chooses the torsion-free connection is an assumption about nature, and
> theories with torsion have been constructed and tested; the observational situation…"*

The flag is right. What is worth noticing is the *shape* of it. Everywhere else in Part III, the
chapter's rhetoric is that the answer was cornered — the connection is "defined as the repair", the
Einstein tensor is "forced", the factor of one half "was never chosen". Vanishing torsion is the one
place where a genuine physical choice sits inside a derivation that reads as a cornering, and the
reader could easily come away thinking the Levi-Civita connection was inevitable.

**Cost to close:** it already is closed, honestly. The entry is here so that Chapter 3.4 §2's
"$T_{6}$ dies by vanishing torsion" and Chapter 3.4 §5's first Bianchi identity — both of which
depend on it — can be traced back to a *physical* assumption, not a mathematical one. Every result
that would change with torsion should be collected in one place.

### G11 · Distributions are used, not built

**Cost: moderate now, severe in Part V.**

Chapter 0.9 §5 handles the Dirac delta by what it does to a test function, which is exactly right
and is more honest than most treatments. What it does not build: the space of test functions as a
topological vector space, derivatives of distributions, the Fourier transform on tempered
distributions, or the distributional identity
$1/(x\pm\ii\epsilon)=\mathrm P(1/x)\mp\ii\pi\delta(x)$ — which is the optical theorem in embryo and
which Part V cannot avoid.

Chapter 0.9 is candid about the specific hole it leaves: the plane waves that serve as a basis for
$L^{2}$ *"do not belong to the space they are supposed to be a basis of"*, and *"that gap is real.
Chapter 4.5 closes it."*

**Cost to close:** one third of Chapter 5.4 (see `PLAN-FORWARD.md` §6), with a partial payment in
4.5 (box normalisation worked in full, then the rigged-Hilbert-space flag behind it). The debt was
addressed to 4.3 when this register was compiled and 4.3 does not pay it; it has since been re-aimed
to 4.5 — this is exactly the kind of quiet reassignment this register exists to catch.

### G12 · Convergence of perturbation series

**Cost: low now, moderate in Part V.**

Chapter 0.3 §4 does asymptotic versus convergent series properly and is one of the book's strongest
sections, so the foundation is laid. The bill arrives in 5.11: QED's perturbation series has zero
radius of convergence, and Dyson's argument for why is two paragraphs and completely accessible with
what 0.3 built. This should be *derived*, not flagged — it is one of the few places where the book
gets to cash a Part 0 investment for a genuinely shocking result.

### G13 · Gaps that are correctly permanent

Listed so the reader knows the edge of the building. None of these will close, and none of them
should be presented as if they might.

| Gap | Why it will not close |
|---|---|
| **Universality of free fall** ($m_G=m_I$) — 3.1 | An experimental fact, flagged nine times in one chapter. Chapter 3.1 says it plainly: *"It is not derivable from anything in this book, and in the theory as it stands it is not derivable at all."* Everything in Part III rests on it |
| **Maxwell's equations** — 2.1, 2.6 | Empirical input. The book derives their relativistic *form* (2.6) and will derive them from a symmetry principle (6.3), but the symmetry principle is chosen to reproduce them |
| **The Born rule** — Part IV | Not derivable. Decoherence explains why the interference terms become unobservable; it does not explain why the probabilities are $\lvert\psi\rvert^{2}$. Chapter 4.20 must say so |
| **Confinement** — 6.5 | Not proved. A Millennium Prize problem. The strong-coupling lattice argument and the numerical evidence are what can be shown |
| **The cosmological constant's value** — 3.6 | Chapter 3.6 already says it: *"Nothing in this book explains it, and nothing anywhere else does either"* |
| **The measurement problem** — 4.20 | Unresolved in physics, not merely in this book |
| **Everything in Part VII from 7.8 onward** | `PLAN.md` §6 already commits to this. `PLAN-FORWARD.md` §9.4 gives it a three-column ledger |

---

## 2 · Every ⚑ in the book

By chapter. `→ Ch N` in the Status column means a forward debt naming that chapter; **bold** means
the debt has since been collected.

### Part 0 — 11 flags across 9 chapters

The first eight rows below did not exist when this register was written. They are the imports the
review found unmarked in Chapters 0.2, 0.4, 0.6 and 0.7 — the ones the reader could not see.

| Ch | What was quoted | Class | Derivable with what the book has? | Cost to close | Status |
|---|---|---|---|---|---|
| 0.2 | Heine–Cantor: a continuous function on a closed bounded interval is uniformly continuous | M | No — needs compactness, which Part 0 does not build | ~1 section, or leave it | Permanent, correctly |
| 0.2 | Fubini: a product of integrals is a double integral | M | No | Needs **product** measure and Fubini–Tonelli, a second quoted construction beyond the one 4.3 §2.3 makes; 4.3 §4.1 declines it in print. **Spent, not repaid, in 4.4 §5.2** — identifying $\operatorname{dom}(\hat p^{\dagger})$ needs the du Bois-Reymond interchange, and 4.4 cites this mark where it stands rather than raising a third flag of its own | **Permanent, correctly** |
| 0.2 | Liouville: $\ee^{-x^{2}}$ and its relatives have no elementary antiderivative | M | No — differential Galois theory, and nothing else in the book touches it | Will not be paid | Permanent, correctly |
| 0.4 | The fundamental theorem of algebra | M | No — the honest proofs are Liouville's theorem or a winding number | Becomes a 3-line corollary once 5.4 builds complex analysis | → Ch 5.4 (see G4) |
| 0.6 | The implicit function theorem | M | No — needs the contraction mapping principle | ~1 section, after 4.3 | Permanent, correctly |
| 0.7 | Picard–Lindelöf, quoted early and stated properly in 0.8 | M | See 0.8 below | — | Collected in **0.8** |
| 0.7 | Generalised Stokes in its general form | M | Partly — 3.5 derives it for the cases the book uses | Paid | Collected in **3.5** |
| 0.7 | The Poincaré lemma | M | Yes for $p=2$ in three dimensions | Paid in part | Collected in **3.5**, which flags the general $p$ |
| 0.8 | Picard–Lindelöf: existence and uniqueness for the initial-value problem, given continuity and a Lipschitz condition | M | No — needs the contraction mapping principle on a function space | ~1 section, and only after 4.3 builds completeness | Permanent, correctly |
| 0.9 | Completeness of the Fourier basis: the $\ee^{\ii k_nx}$ are enough, not merely orthonormal | F | No, not with Riemann integration | 1 section of 4.3 | → **Ch 4.3** |
| 0.9 | The central limit theorem: the sketch omits uniform control of the $O(n^{-3/2})$ remainder and Lévy's continuity theorem | M | Partially — the mechanism is derived, the analysis is not | ~2 sections; Lindeberg is the honest general statement | Permanent, correctly |

**The notable feature of Part 0 is chapters 0.1–0.7 carrying no flags at all.** That is 84,000 words
of mathematics with nothing quoted, and it is the strongest evidence in the project that the
approach works. The two genuinely quoted results in those seven chapters — the fundamental theorem
of algebra (0.4) and the implicit function theorem (0.6) — are candidly labelled in prose but
**not flagged**, which is §3.1 below.

### Part I — 32 flags across 4 chapters

| Ch | What was quoted | Class | Derivable? | Cost | Status |
|---|---|---|---|---|---|
| 1.1 | The Lorentz force law, and the field of a uniformly moving charge | E / F | The covariant form, yes (2.6); the retarded field of an accelerating charge, no | The retarded field needs Green's functions of $\Box$ — available after 5.4 | Partly → **Ch 2.6** |
| 1.1 | The dropped radiation term in the moving-charge field | M | It is justified in place by an order-of-magnitude estimate | — | Adequately handled |
| 1.1 | Observables are self-adjoint operators on a Hilbert space | F | No | — | → Ch 4.2, 4.4 |
| 1.2 | Interchanging $\dv{}{\epsilon}$ with $\int\dd t$ in the first variation | M | No — needs dominated convergence | **The tool now exists**: 4.3 §4.3 proves differentiation under the integral sign | Not collected by name. 1.2 discharges its own mark in place under a continuity-and-compactness hypothesis, and never says "Chapter 4.3", so `debts.py` cannot see it. Closable in one sentence whenever 1.2 is next touched |
| 1.2 | Ostrogradsky's theorem: a Lagrangian depending on $\ddot q$ has an unbounded-below energy | M | Yes, in principle — it is 1.3's Hamiltonian machinery applied to a case 1.3 skipped | ~1 section | Re-flagged in 3.6; needed by 7.1 |
| 1.2 | The preview paragraph on the path integral | F | No | — | → Ch 5.6 |
| 1.2 | Jacobi's theorem: the second variation is positive definite exactly up to the first conjugate point | M | Partially — the geometric example is worked | ~2 sections | → Ch 3.7/3.8 for the lensing application |
| 1.2 | Legendre's condition is necessary, not sufficient | M | Same as above | — | Same |
| 1.2 | The table of eight actions in §8.1 | F | Each is derived in its own chapter | — | 4 of 8 collected (2.5, 2.6, 3.6, and 1.2 itself) |
| 1.2 | $L=\half m\dot{\vv x}^{2}-e\varphi+e\vv A\cdot\dot{\vv x}$, quoted forward | F | Yes | — | **Collected, Ch 2.6** |
| 1.3 | Invertibility of the Legendre transform for non-convex $f$ | M | Yes, with effort | ~1 section | Permanent, correctly |
| 1.3 | The Aharonov–Bohm effect (Chambers 1960; Tonomura 1986) | E + F | The measurement, no; the phase, yes | — | → Ch 6.3 for the phase |
| 1.3 | **Dirac's formalism for constrained systems** | **D** | Yes — it is Hamiltonian mechanics | ~2 sections | **See G5. Nothing owes it, and everything needs it** |
| 1.3 | The Bohr–Sommerfeld quantisation condition | F | No, not classically | — | → Ch 4.8 (the oscillator case, exactly), 4.10 §6 (in general) |
| 1.3 | Adiabatic invariance of the action variable | F | Partially | — | → Ch 4.17 §8 |
| 1.3 | Poincaré's recurrence theorem | D | Yes — it is Liouville plus pigeonhole | ~1 section | Permanent |
| 1.3 | Groenewold–van Hove: no exact quantisation map exists | D / M | No | — | → Ch 4.10 §8 should collect it as the honest limit of the correspondence |
| 1.3 | $\det M=+1$ for canonical transformations, via a Pfaffian argument | M | Yes, with the Pfaffian built | ~1 section | Permanent, correctly |
| 1.3 | The WKB substitution giving Hamilton–Jacobi as the $\hbar\to0$ limit | F | No | — | → Ch 4.10 |
| 1.3 | KAM theory | D | No | — | Permanent |
| 1.4 | Bloch's theorem / crystal momentum | D | Partially, after 4.6 | ~1 section | Permanent |
| 1.4 | The FLRW scale factor $a(t)$ | F | Yes | — | → Ch 3.9 |
| 1.4 | No time-translation symmetry in a general curved spacetime ⇒ no total energy | F | Yes | — | **Collected, Ch 3.5** (Killing vectors); completes in 3.9 |
| 1.4 | The local statement $\nabla_\mu T^{\mu\nu}=0$ | F | Yes | — | **Collected, Ch 3.6** |
| 1.4 | ADM energy for asymptotically flat spacetimes | D | Partially | ~1 section | Permanent |
| 1.4 | $P$ and $CP$ violation in the weak interaction | E + F | The measurement, no; the mechanism, yes | — | → Ch 6.7 |
| 1.4 | The CPT theorem | M / D | No — needs analyticity and locality | — | Permanent |
| 1.4 | **Noether's second theorem** — symmetries with function-valued parameters give identities, not conservation laws | F | Yes | ~1 section | → **Ch 6.3.** This is why 6.3 cannot simply repeat 1.4 §6, and it is tied to G5 |
| 1.4 | The LRL vector's algebra closes on $\mathfrak{so}(4)$ | F | Yes — the brackets are computed in place | — | → Ch 6.1 for the naming |
| 1.4 | Hydrogen's degeneracy in $\ell$ inherits that same $SO(4)$ | F | Yes | — | → Ch 4.14 |
| 1.4 | Conformal invariance of the $1/r^{2}$ Lagrangian, $SL(2,\R)$ | F | Partially | — | → Ch 7.3 |
| 1.4 | The two signs of the Noether charge become particle and antiparticle | F | Yes | — | → Ch 5.5 |

### Part II — 54 flags across 6 chapters

Chapter 2.1's twenty are almost entirely experimental and are correct as they stand. They are
grouped rather than tabulated individually.

| Ch | What was quoted | Class | Notes |
|---|---|---|---|
| 2.1 (×17) | Maxwell's four equations; $\epsilon_0$ and $\mu_0$ from bench measurements; the Weber–Kohlrausch value of $c$; the Michelson–Morley apparatus parameters and null result; modern optical-resonator bounds; Bradley's aberration constant; Fizeau's drag coefficient; de Sitter's and Brecher's binary-star bounds; Alväger's 1964 $\pi^{0}$ result; Kennedy–Thorndike; Airy's water telescope | **E** | Not gaps. Chapter 2.1's subject *is* the experimental record, and the chapter derives every prediction those measurements are compared against |
| 2.1 (×2) | Galileo's *Dialogo* paraphrase; Maxwell's 1862 sentence | — | Attributions of wording |
| 2.1 (×1) | A meta-flag noting which items in the section are quoted results | — | Housekeeping |
| 2.2 | Additivity plus continuity at one point ⇒ linearity (the Cauchy functional equation) | M | Sketched in one dimension in place |
| 2.2 | Every line-preserving bijection is projective (fundamental theorem of projective geometry) | M | Permanent |
| 2.2 | Terrell–Penrose: a small object photographs as rotated, a sphere as a circular disc | M | Derivable with light-travel-time bookkeeping; ~1 section |
| 2.2 (×2) | A smooth one-parameter group is $\exp(\phi K)$ | F | → Ch 6.1 |
| 2.2 (×3) | The muon lifetime $2.2\,\mu s$; the sea-level muon flux; Rossi and Hall's 1941 counts | E | Not gaps |
| 2.2 | The exact Wigner angle for perpendicular boosts | M | Derivable; the low-speed limit *is* derived |
| 2.2 | The polar decomposition $M=BR$ | M | Derivable after the spectral theorem; ~1 section |
| 2.2 | Baker–Campbell–Hausdorff | F | → Ch 6.1 (second order only is ever used) |
| 2.3 | The Lorentz group has four connected components in four dimensions | F | → Ch 6.1 |
| 2.3 | $\Lambda^{\mathsf T}\eta\Lambda=\eta$ is the definition of $\mathrm O(1,3)$ | F | → Ch 6.1 |
| 2.3 | Tachyons are not consistent quantum-mechanically | F | → Ch 5.1 |
| 2.3 | The clock hypothesis, tested to $10^{18}g$ in storage rings | E | Not a gap |
| 2.3 | The Rindler wedge and its adapted coordinates | F / D | → Ch 3.8 for the horizon comparison; the Unruh effect is not owed to anyone |
| 2.3 | The field strength of a gauge theory lives in the Lie algebra of its group | F | → Ch 6.1, 6.4 |
| 2.4 | For a general coordinate change the Levi-Civita symbol is a tensor *density* | D | Partially collected by 3.5 §6's $\sqrt{-g}$; densities as such are never developed |
| 2.5 (×6) | Ives–Stilwell 1938; the Bevatron's design energy; particle masses from tables; quark masses; $E=hc/\lambda$; LHC machine parameters | E | Not gaps. Every one is labelled "we quote the experiment; the algebra is ours" |
| 2.5 | Spin-statistics: fermion number conservation forces the antiproton threshold | F | → Ch 5.5 |
| 2.6 | Maxwell's equations and the frame-independence of charge, as the chapter's two inputs | E | Declared in a single opening box. Model behaviour |
| 2.6 | $j^\mu$ will come from a global phase symmetry | F | → Ch 6.3 |
| 2.6 | The homogeneous Maxwell pair is $\dd^{2}=0$ | F | **Collected, Ch 3.5 §3.3** |
| 2.6 | Solvability of $\Box\chi=-f$ for reasonable sources | M | Closable after 5.4's Green's functions; ~1 section |
| 2.6 (×3) | Commentary on the field concept; a pseudoscalar cross-reference; a derived pancake-field result | — | Not quoted results |

### Part III — 29 flags across 6 chapters

| Ch | What was quoted | Class | Derivable? | Status |
|---|---|---|---|---|
| 3.1 (×10) | The universality of free fall; the Eötvös/torsion-balance/lunar-ranging bounds; clock-comparison limits on a composition-dependent redshift; the strong-EP self-energy bound; Pound–Rebka; the GPS numbers; the 2010 aluminium-ion clock at 33 cm; the $1.75''$ solar deflection from Eddington and VLBI | **E** | No, and correctly so | The chapter says nine times that this is measurement, not derivation. See G13 |
| 3.2 | Whitney's embedding theorem | M | No | Quoted and explicitly **not used** — the safest possible flag |
| 3.2 | The extreme value theorem in several variables | M | Yes, with compactness | Permanent |
| 3.2 | Frobenius: $n$ vector fields form a coordinate basis iff all brackets vanish | M | Yes, with effort | Quoted and not used except in one direction |
| 3.3 | Sylvester's law of inertia plus a connectedness argument, fixing the signature | M | Yes, with effort | Permanent |
| 3.3 | Existence and uniqueness for the linear transport ODE along a curve | M | Same as 0.8's Picard–Lindelöf | Duplicate of an existing flag |
| 3.3 | **Vanishing torsion is an assumption about nature** | **A** | Not a theorem at all | See G10 |
| 3.4 (×2) | The Weyl tensor: named, three properties quoted, none used | D | Yes, with effort | Nothing owes it. 7.3 will meet conformal invariance again |
| 3.4 | Lovelock's theorem | F | No | **Collected, Ch 3.6 §3.3** |
| 3.4 | The converse: Riemann $=0$ on a simply connected region ⇒ flat | M | Partially — the easy direction is proved, the converse sketched | Permanent, correctly |
| 3.6 | Ostrogradsky, again | M | See 1.2 | → Ch 7.1 leans on it |
| 3.6 (×2) | Lovelock's theorem, stated and used | M | No — a classification argument | Permanent, correctly |
| 3.6 (×2) | The Gibbons–Hawking–York boundary term | F | Yes, with effort | → Ch 7.9, where the action's value becomes an entropy |
| 3.6 | The sign convention of the gravitational action against 1.2's table | — | Internal cross-reference | Housekeeping |
| 3.6 | $\Lambda\approx1.1\times10^{-52}\,\mathrm m^{-2}$ and the vacuum energy discrepancy | E | No | See G13 |

---

## 3 · Unstated assumptions

These are worse than ⚑s, because the reader cannot see them. Ordered by cost.

### 3.1 · Quoted results with no flag

Three results are candidly labelled as imported in the prose and carry no ⚑, so they do not appear
in any count the reader can make:

| Where | What | Why it matters |
|---|---|---|
| 0.4 §7 | **The fundamental theorem of algebra**, "imported rather than proved" | See G4. It is the foundation of the spectral theorem and therefore of Part IV |
| 0.6 §7 | **The implicit function theorem**, "which we quote" | Underwrites the claim that the tangent space to a constraint surface is $(\mathrm{span}\,\nabla g)^{\perp}$, hence all of Lagrange multipliers, hence 0.6's Boltzmann derivation |
| 0.9 §7.5 | **The Cauchy characteristic function**, "(a contour integral, quoted here)" | See G2. It is also the only place in the book where complex analysis is used at all, which makes the absence of a flag doubly unfortunate |

**Done — all three are now flagged**, along with five more the review found in 0.2 and 0.7. The cost
was three characters each and the benefit is that the flag census is now trustworthy. This section
stays because the *gaps* are unchanged; only their visibility is.

Two further quoted results are handled well and are noted only for completeness: 0.7's existence and
uniqueness for field lines (properly stated in 0.8 with its own ⚑), and 0.7's general curvilinear
divergence formula (derived in 3.5 §6.4 — debt paid).

### 3.2 · Smoothness, and where it is doing work

See G9. Specifically:
- 1.2 assumes $L$ smooth; the smoothness class needed for the fundamental lemma is $C^{1}$ and the
  chapter is careful about that, which is good practice.
- 3.2 and 3.3 assume $C^{\infty}$ manifolds and metrics without comment. Real solutions are not
  smooth at matter boundaries.
- 3.4 §4.1's geodesic congruence is assumed caustic-free.

### 3.3 · Interchange of limits

Flagged where it matters most (1.2's $\dv{}{\epsilon}\int$), and semi-flagged in 0.5's closing note
("the interchange of sums"). Not flagged in:
- 0.9's term-by-term differentiation and integration of Fourier series;
- 0.9's exchange of the two integration orders in deriving the convolution theorem;
- 0.2's differentiation under the integral sign, where the dominated-convergence hypothesis is
  stated but its verification is deferred to 4.3.

None of these is wrong. All are legitimate under hypotheses the book has not stated. A single
paragraph in 4.3, once dominated convergence exists, could retroactively license the lot — and that
would be an elegant collection.

### 3.4 · Existence of solutions

- **Einstein's equations**: see G8. Nothing anywhere asserts that solutions exist.
- **The wave equation** $\Box\chi=-f$: ⚑'d in 2.6, closable after 5.4.
- **Schrödinger's equation**: will need self-adjointness of $H$, which is exactly what 4.4 builds —
  a nice case of a gap and its closure being scheduled together.
- **Yang–Mills**: existence and the mass gap is an open problem. Must be flagged in 6.4/6.5.

### 3.5 · Global versus local

The book is unusually good here — 0.7 §2.4's punctured-plane counterexample, 3.5 §4's closed-versus-
exact treatment, and 3.4 §8's simply-connectedness condition all address it head on. Two places
where it is still implicit:

- **Coordinate patches in Part II.** All of Part II works in a single global inertial chart and
  never says that this is a privilege of flat spacetime. Chapter 3.2 §1.1 makes the point
  retrospectively, but a reader who stops after Part II will not have met it.
- **Gauge fields on topologically non-trivial spaces.** Part VI will need this (monopoles,
  instantons, Aharonov–Bohm) and it is exactly what a fibre bundle formalises. See
  `PLAN-FORWARD.md` §3.3.

### 3.6 · Physical assumptions carried silently

- **The geodesic hypothesis.** Chapter 3.6 Problem 2 does this beautifully — the geodesic equation
  is *derived* from $\nabla_\mu T^{\mu\nu}=0$ for dust, and the solution's part (d) makes the
  logical point explicitly. What is silent: the derivation is for pressureless dust and for a test
  body with no self-field. The general statement (Geroch–Jang) has hypotheses. One sentence.
- **Energy conditions.** Never mentioned. Used implicitly wherever "matter has positive energy
  density" is assumed, and they are the hypothesis of every singularity theorem.
- **Test particles do not backreact.** Assumed throughout 3.7's orbit analysis (to come).

---

## 4 · Promised, and not yet delivered

Every reference in the written text to a chapter that does not exist. Counted by
`python3 debts.py --census`:

| Owed to | Debts | Owed to | Debts | Owed to | Debts |
|---|---|---|---|---|---|
| 4.4 | 8 | 5.1 | 4 | 6.1 | 23 |
| 4.5 | 12 | 5.2 | 18 | 6.2 | 1 |
| 4.6 | **32** | 5.3 | 16 | 6.3 | **35** |
| 4.7 | 2 | 5.4 | 16 | 6.4 | 11 |
| 4.8 | 14 | 5.5 | 5 | 6.5 | 9 |
| 4.9 | **32** | 5.6 | 17 | 6.6 | 11 |
| 4.10 | 9 | 5.7 | 10 | 6.7 | 0 |
| 4.11 | 9 | 5.8 | 9 | 6.8 | 5 |
| 4.12 | 7 | 5.9 | 5 | 7.1 | 11 |
| 4.13 | 6 | 5.10 | 7 | 7.2 | 3 |
| 4.14 | 1 | 5.11 | 11 | 7.3 | 5 |
| 4.15 | 2 | | | 7.4 | 4 |
| 4.16 | 1 | | | 7.5 | 1 |
| 4.17 | 8 | | | 7.6 | 0 |
| 4.18 | 7 | | | 7.7 | 2 |
| 4.19 | 6 | | | 7.8 | 2 |
| 4.20 | 13 | | | 7.9 | 10 |

**Total: 420 forward references to unwritten chapters.**

> **Updated 28 August 2026.** Recounted after the Part IV re-plan
> (`reports/part4-replan.md`), which cuts the eight unwritten chapters 4.4–4.11 into seventeen,
> 4.4–4.20, each capped at about six new objects. The previous edition of this table read
> **393** and was two renumberings out of date. The two totals are not comparable: 3.7–3.9 and
> 4.1–4.3 have been written and have left the table, three chapters of new text have entered it,
> and `debts.py` now matches the plural form — *"Chapters 4.6, 4.8 and 4.11"* — which the old
> `grep 'Chapter 4\.N'` could not see at all.

> **Updated 18 August 2026.** Chapter 3.7 has been split — 3.7 now carries the Schwarzschild
> solution and its timelike orbits, 3.8 carries light, redshift and horizons, and cosmology moves to
> 3.9. That was done *because* of the 34-debt load recorded here, and it worked: the load is now
> 22 and 12. Every reference was re-aimed in the same commit, and the section numbers in those
> references are fixed by `MATHPLAN-3.7-3.9.md`.

### The four heaviest, and what they actually owe

**Chapter 3.7 — was 34 debts, now 22 after the split.** It was the heaviest single load in the
book, from four different chapters, and that is why Part III is now nine chapters:
- 1.2 §5.1 and 2.3 §6.2: conjugate points become the multiple images of a lensed quasar, and the
  caustic is where the second variation stops being positive. *Two chapters have promised this
  specific illustration.*
- 2.3 Problem 3: the Rindler horizon has "exactly the same local character" as the Schwarzschild
  horizon, and the argument that it is not a real singularity.
- 3.1 §7.3: the factor-of-exactly-two confession, which 3.1 calls "the register of debts".
- 3.5 Problem 4: Clairaut's relation on the sphere, explicitly "a rehearsal for Chapter 3.7".
- 3.6 Problem 3 (d): the spatial part of the weak-field metric, needed for the missing half.

This debt load, plus `MATHPLAN-3.md`'s eight numbered items, is the evidence for splitting 3.7. See
`PLAN-FORWARD.md` §4.

**Chapter 6.3 — 33 debts, from eight different chapters.** The largest cross-book promise, and
Chapter 1.4 names it as such: *"That is Chapter 6.3, and it is the single largest cheque this book
writes."* What is owed:
- 0.3: U(1) and SO(2) are the same group, and the circle-valued phase generates electromagnetism.
- 0.7 (four separate places): the Aharonov–Bohm phase derived; gauge freedom $\vv A\to\vv A+\nabla\chi$
  as "the seed of Chapter 6.3"; the holonomy $\oint A_\mu\dd x^\mu$ as the physical object; the
  non-simply-connected solenoid.
- 1.2, 1.3 (five places): minimal coupling $\vv p\to\vv p-e\vv A$ derived classically, with the
  explicit promise *"When Chapter 6.3 tells you that the covariant derivative $D_\mu=\partial_\mu-\ii eA_\mu$
  is forced, you will recognise it as this worked example wearing indices."*
- 1.4: Noether's second theorem, and the gauge principle as generator rather than accommodation.
- 2.6 (six places): gauge invariance promoted from convenience to generating principle; charge
  conservation and gauge invariance as one fact; $j^\mu$ from a global phase.
- 3.5, 3.6: the exterior derivative existing before the metric, and the constraint structure of a
  gauge theory mirroring that of gravity.

Chapter 6.3 is the convergence point of the entire book's structure. **It should not be written by
an agent who has not read the eight chapters that promised it.**

**Chapter 4.6 — 32 debts, Chapter 4.9 — 32 debts.** These two now carry the Part IV load. 4.6 is
the Schrödinger equation, which Part 0 has been writing cheques against since 0.2 and which 4.2
names five times; 4.9 is the uncertainty relation and its neighbours, which 0.5 and 0.9 built in
full and deliberately did not spend, so almost every one of its debts is paid in a sentence rather
than a section. Both are collection chapters rather than construction chapters, and neither should
be written without `python3 debts.py 4.6` and `python3 debts.py 4.9` in the brief.

The remapping this entry used to call for has now been done twice — in August 2026 when Part IV
went from eight chapters to eleven, and again in the re-plan that took it from eleven to twenty.
The lesson stands as written: it is a single scripted pass with a hand-checked mapping table, done
before the batch rather than chapter by chapter afterwards.

### The debts that named a chapter which would not pay them

All of these have been re-aimed in the text. The middle column records what the sentences said when
this register was compiled; the right-hand column is where each promise lands under the
twenty-chapter Part IV, and is the live target.

| Promise | Named, 18 Aug 2026 | Now names, and pays |
|---|---|---|
| The Lebesgue integral, dominated convergence, completeness of L² | 4.3 | **4.3** — written, and paid |
| The infinite-dimensional spectral theorem, continuous spectra, self-adjointness | 4.3 | self-adjointness **4.4**; the spectrum and the theorem **4.5** |
| Plane waves not being in $L^{2}$; the rigged-Hilbert-space repair | 4.3 | **4.5**, completing in **5.4** |
| Poles as particles, branch cuts as thresholds (0.3 §3) | 5.9 | **5.11**, with the machinery in **5.4** |
| The fine structure of hydrogen (0.3 WE2, 2.5 §3.3) | 4.5 | **4.16** |
| Ladder operators and $E_n=(n+\half)\hbar\omega$ | 4.5 | **4.8** |
| The adiabatic theorem (1.3) | 4.5 | **4.17** §8 |
| Hydrogen's $SO(4)$ degeneracy (1.4) | 4.5 | **4.14** |

---

## 5 · Mathematical machinery used before it was built

Three instances, all minor, all already handled with more care than most books manage:

1. **The metric, used in 3.2 before 3.3 defines it.** Chapter 3.2 §9's worked example needs
   $\hat e_\theta = \tfrac1r\partial_\theta$ to normalise a basis, and says so in place: *"This step
   is the only one needing a metric, which is why it belongs to Chapter 3.3 and is quoted here."*
   Correctly handled.
2. **The Poincaré lemma, quoted in 0.7 and proved in 3.5.** Chapter 0.7 §7.3 quotes it, names 3.5,
   and 3.5 §4.2 proves it and says so. **Debt paid**, and it is the model for how this should work.
3. **The divergence in curvilinear coordinates, quoted in 0.7 to check a derivation.** Derived in
   3.5 §6.4. **Debt paid.**

The book's record here is good. The only genuine forward-use is the fundamental theorem of algebra
(§3.1), whose own prerequisite — complex analysis — the book has never built and, under the current
plan, never will. It is used in 0.4 and spent in 0.5, and its proof would not become available
until Chapter 5.4 at the earliest.

---

## 6 · Known deferrals — deliberately postponed, with the collector named

| Deferred | Deferred in | Collector | Status |
|---|---|---|---|
| $S=A/4$ for a black hole | 3.9 (planned) | **7.9** | The book's one deliberate loose thread. `PLAN.md` §5 and `MATHPLAN-3.md` both designate it |
| The Gibbons–Hawking–York boundary term | 3.6 §4.5 | **7.9** | Named and deferred in place, twice |
| The Weyl tensor | 3.4 §6.2 | *nobody* | Named, three properties quoted, none used. 7.3 will meet conformal invariance from the other side but does not owe this |
| Tensor densities | 2.4 §8.1 | partly 3.5 §6 | $\sqrt{-g}$ is built; densities as a class are not |
| Dirac's constrained-system formalism | 1.3 | *nobody* | **See G5 — this is the deferral to worry about** |
| Noether's second theorem | 1.4 §6 | 6.3 | Owed, and tied to the above |
| The Unruh effect / Rindler thermodynamics | 2.3 Problem 3 | *nobody explicitly* | Natural home is 7.9, alongside the entropy count |
| Lebesgue integration | 0.2 §1 | 4.3 | Explicitly promised |
| The classical limit and Hamilton–Jacobi | 1.3 §8.2 | **4.10** | |
| Bohr–Sommerfeld, derived properly | 0.8 §4.4, 1.3 §4.4 | **4.8**, then **4.10** §6 | Promised twice with the arithmetic already done. 4.8 does the oscillator, where it is exact; 4.10 §6 recovers it from WKB in general and scores it |

---

## 7 · What this register says about the book

Three observations, offered because they are what the numbers actually show.

**The flag discipline is real — but it was not, until this register was written.** The first edition
of this file recorded that Part 0's first seven chapters, 84,000 words, carried no flags at all, and
read that as evidence of rigour. It was the reverse: those chapters import eight named theorems and
marked none of them, several while saying in words that they were quoting. Part 0 now carries eleven
flags, and that number is the honest one. The lesson is the reason for the whole document — **an
absence of flags is not evidence of derivation, and only a register that is compiled independently
of the author can tell the two apart.**

What the discipline does get right, from Chapter 1.1 onward, is real. Chapter 2.6 opens with a box
declaring its two inputs and then says *"Everything else below is derived"*, and it is. Chapter 3.5
derives the whole apparatus of differential forms, Lie derivatives, Killing vectors and generalised
Stokes with one flag, on the one step — the general-degree Poincaré lemma — that is genuinely a
sketch. The review found **no false flag anywhere**: nothing is marked as quoted that the book in
fact derived. The failure mode here is under-marking, never over-marking.

**The concentration of flags is diagnostic, and one concentration is a warning.** Chapters 2.1 and
3.1 carry thirty flags between them and almost all are experimental, which is exactly right — those
are the two chapters whose subject is what was measured. Chapter 1.3 carries ten, of which four are
permanent deferrals (constrained systems, Poincaré recurrence, Groenewold–van Hove, KAM). That is
the only chapter in the book whose flags are mostly *"we are not going to do this"* rather than
*"here is the measurement"* or *"here is the chapter that will"*. It is also the chapter whose
deferral matters most downstream (G5).

**The forward debts are the real exposure.** 420 references to unwritten chapters, 35 of them to
Chapter 6.3 alone. Every one of those was written in good faith by an author who knew what the later
chapter was going to say. The risk is not that they are wrong; it is that a later agent, writing
6.3 with a different plan in front of them, does not know that eight earlier chapters have told the
reader precisely what 6.3 will do. **The single most valuable process change this register suggests
is that each chapter's brief should carry the extracted list of every debt naming it.** That is a
five-line script — it now exists, as `debts.py` — and it converts 420 hopes into 420 requirements.
