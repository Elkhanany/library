# Part III — General Relativity: derivation plan

*Eight chapters, four of them dedicated mathematics. This is the hardest stretch of the book and
the place readers historically fall off. Everything below is **derived in the text**; items marked
⚑ are the only permitted exceptions and must be flagged in place.*

---

## 0. Pacing — what "slow" means here

Part III fails if it is merely correct. The instruction for every chapter in this part:

1. **Announce the destination before starting.** "We want an object that measures whether a space is
   curved, using only measurements made inside it. Three steps: first…, then…, finally…" The reader
   should always know which step they are on.
2. **One manipulation per line.** Never combine "relabel the dummy index and use the symmetry of the
   connection" into a single move. Two things happened; show two lines.
3. **Name the technique as you use it.** *"Now integrate by parts — the boundary term dies because
   the variation vanishes at the endpoints."* Not just the resulting expression.
4. **Say what was done after any line that is not obvious**, in a half-sentence. The reader should
   never have to reverse-engineer which rule was applied.
5. **Index gymnastics are spelled out.** Where an index is raised, lowered, relabelled or a symmetry
   is used, say so. These are exactly the steps where a rusty reader silently loses the thread.
6. **Grind boxes hold length, never logic.** A long computation may be folded, but the *argument*
   and the reason each step is legal stay in the main text. A reader who never opens a grind box
   must still be able to follow the reasoning.
7. **Recap after any derivation longer than about ten lines.** Two sentences: what went in, what came
   out, what it cost.
8. **Prefer two derivations of the important results** — one that shows where it comes from and one
   that shows why it had to be that. Geodesics get both; so does the Einstein tensor.

Every chapter is written **with its "In plain terms" boxes in place**, by the same author, in one
pass — see `PLAIN-TERMS-PLAN.md` §7.

---

## Conventions (binding, extending `CONVENTIONS.md`)

- Signature $(+,-,-,-)$ throughout, as in Part II. Greek indices $0\ldots3$, Latin $1\ldots3$.
- $g_{\mu\nu}(x)$ for the general metric; $\eta_{\mu\nu}$ reserved for flat.
- $\Gamma^{\lambda}{}_{\mu\nu}$ for the Levi-Civita connection; $\nabla_\mu$ for covariant derivative.
- Riemann: $[\nabla_\mu,\nabla_\nu]V^{\rho}=R^{\rho}{}_{\sigma\mu\nu}V^{\sigma}$. Ricci
  $R_{\mu\nu}=R^{\lambda}{}_{\mu\lambda\nu}$. State the sign convention loudly, once, and note that
  books differ.
- Geometrised units are **not** used; keep $G$ and $c$ explicit through 3.7, then note the
  convention for 3.8. Nothing is harder for a rusty reader than a vanished constant.

---

## 3.1 · The Equivalence Principle

*Light on machinery, heavy on consequence. The chapter that decides gravity is geometry.*

| # | Built | From |
|---|---|---|
| 1 | Inertial vs gravitational mass; their equality | stated as experiment (⚑ Eötvös/lunar-ranging precision quoted) |
| 2 | Weak equivalence principle ⇒ trajectory independent of composition | item 1 |
| 3 | Einstein equivalence principle | strengthening item 2 to all local physics |
| 4 | **Tidal deviation** — two nearby freely-falling particles | expand Newtonian $g$ about a point; get relative acceleration $\sim(GM/r^{3})d$, **stretching along the field and squeezing across it**. This is the part of gravity you cannot transform away, and it is the whole content of the chapter. **Careful with the standard slogan:** a *ring* in the plane containing the radial direction gains area at second order; what is preserved is the *volume* of a three-dimensional ball, because the tidal matrix is traceless, which is Laplace's equation. Do not repeat the usual "constant area" claim |
| 5 | Size of a local inertial frame | require tidal effects below measurement precision; get an explicit bound |
| 6 | Gravitational redshift $\Delta\nu/\nu=gh/c^{2}$ | accelerating-cabin argument + Doppler, **with no general relativity used at all** |
| 7 | Light bending in the cabin | same argument; obtain the deflection and then state plainly that it is **half** the observed value, with the reason deferred to 3.7 — do not fudge this |
| 8 | Why gravity alone can be geometrised | universality: every body follows the same path, so the path can belong to the arena rather than the body. Contrast electromagnetism, where charge-to-mass ratios differ |

**Figure:** a ring of free particles released around a mass, deforming into an ellipse — stretched
along the field and squeezed across it. Its area is *not* constant — the traceless tidal matrix preserves the volume of a ball in three dimensions, not the area of a ring in two, and 3.1 works the arithmetic rather than repeating the slogan. That shape *is* item 4, and
Chapter 3.4 will recover it from the curvature tensor.

## 3.2 · Manifolds ※

*The chapter where the arrow-in-a-background picture is taken away and replaced. Go slowly.*

| # | Built | From |
|---|---|---|
| 1 | Why a new object is needed | spacetime need not be $\R^{4}$ globally, and no background is available to draw arrows in |
| 2 | Charts, atlases, transition maps | the sphere, with an explicit two-chart atlas and a proof that one chart cannot suffice |
| 3 | Smooth structure | smoothness of transition maps |
| 4 | **Tangent vector as a directional derivative** | curves through a point → the operator $\dv{}{\lambda}$ acting on functions. Show the coordinate vector fields form a basis. **Say explicitly why the ambient-arrow picture is abandoned and what replaces it** |
| 5 | The tangent space $T_pM$ | a *different* vector space at every point — the single most important sentence in the chapter, since it is why vectors at different points cannot be compared |
| 6 | Cotangent space, $\dd x^{\mu}$, duality $\langle \dd x^\mu,\partial_\nu\rangle=\delta^\mu{}_\nu$ | 0.6 §4 and 2.4 §3, now on a manifold |
| 7 | Tensors on a manifold | 2.4's definition verbatim, with the transformation matrix now the position-dependent Jacobian of a chart change |
| 8 | Vector fields; the commutator $[X,Y]$ | show the second-derivative terms cancel so the result is again a vector field |

**Figure:** two vectors at two different points of a sphere and the demonstration that "are these
parallel?" has no answer — the result depends on the path you carry one along. That question is left
open here and answered in 3.3.

## 3.3 · Metric and Connection ※

| # | Built | From |
|---|---|---|
| 1 | Metric $g_{\mu\nu}(x)$, line element | an inner product on each tangent space, varying with position |
| 2 | **Flat space in polar coordinates** | worked early and deliberately: the metric components are not constant, yet the space is flat. Kills the assumption that varying components mean curvature before it forms |
| 3 | Proper time; $S=-mc^{2}\!\int\dd\tau$ | 2.5, unchanged except that $\dd\tau$ now uses $g$ |
| 4 | **$\partial_\mu V^\nu$ is not a tensor** | differentiate the transformation law; the second-derivative term is the obstruction. Show it in full |
| 5 | Covariant derivative and the connection | *define* $\Gamma$ as whatever cancels item 4; derive the inhomogeneous transformation law $\Gamma$ must obey, and note it is therefore **not** a tensor |
| 6 | Parallel transport | $\nabla_u V=0$ along a curve |
| 7 | **The Christoffel formula** | impose metric compatibility and vanishing torsion; derive by the cyclic-permutation trick, **every step shown** |
| 8 | Geodesics, twice | (a) parallel transport of one's own tangent; (b) extremise $\int\dd\tau$ by Euler–Lagrange (1.2). Show the two agree |
| 9 | Worked: the sphere | Christoffels computed, geodesics shown to be great circles |

**Figure:** parallel transport along a path on a curved surface, with the transported vector held as
parallel as the surface permits. The closed-loop version is saved for 3.4.

## 3.4 · Curvature ※

*The centre of Part III.*

| # | Built | From |
|---|---|---|
| 1 | The question: curvature detected from inside | transport a vector around a closed loop and see whether it returns unchanged |
| 2 | **Riemann tensor** $[\nabla_\mu,\nabla_\nu]V^{\rho}=R^{\rho}{}_{\sigma\mu\nu}V^{\sigma}$ | the commutator, computed in full. Long; grind-box the algebra, keep the argument outside |
| 3 | It is a tensor | the non-tensorial pieces of $\Gamma$ cancel in the commutator — the payoff for item 2's length |
| 4 | **Geodesic deviation** $\tfrac{D^{2}\xi^{\mu}}{\dd\tau^{2}}=-R^{\mu}{}_{\nu\rho\sigma}u^{\nu}\xi^{\rho}u^{\sigma}$ | two nearby geodesics. **Then identify it with 3.1's tidal deviation.** Tidal force *is* curvature; this is where Part III's thesis lands |
| 5 | Symmetries of Riemann; 20 independent components in four dimensions | derive the count, do not assert it |
| 6 | Ricci tensor and scalar; what contraction discards | and name the discarded part (Weyl) without developing it |
| 7 | **Second Bianchi identity ⇒ $\nabla_\mu G^{\mu\nu}=0$** | derived. This single fact dictates the form of the field equations in 3.6 |
| 8 | Flat ⟺ Riemann vanishes | prove the easy direction; ⚑ the converse |

**Figure:** parallel transport around a closed loop on a sphere, with the holonomy angle **measured**
and compared against enclosed area times curvature. Curvature made visible and numerical.

## 3.5 · Forms, Lie Derivatives, Killing Vectors ※

| # | Built | From |
|---|---|---|
| 1 | Differential forms, wedge product | antisymmetry is what integration wants |
| 2 | Exterior derivative; $\dd^{2}=0$ | and the collection: this is 0.7's two vector identities **and** 2.6's homogeneous Maxwell pair, all one statement |
| 3 | Generalised Stokes $\int_M\dd\omega=\oint_{\partial M}\omega$ | collecting 0.7's promise that four theorems are one |
| 4 | Volume element $\sqrt{-g}\,\dd^{4}x$ | 0.6's Jacobian determinant, on a manifold |
| 5 | Lie derivative; $\mathcal L_XY=[X,Y]$ | dragging a tensor along a flow and comparing with itself |
| 6 | **Killing vectors** $\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0$ | $\mathcal L_\xi g=0$ |
| 7 | **Killing ⇒ conserved quantity along geodesics** | derived. Noether (1.4) geometrised — and the tool that makes 3.7 solvable |
| 8 | Maxwell in form language | $F=\dd A$, $\dd F=0$, $\dd\star F=\star J$ |

**Figure:** optional, and only if it earns its place — a rotational flow on a sphere leaving the
metric unchanged, against a flow that visibly distorts it.

## 3.6 · The Einstein Field Equations

| # | Built | From |
|---|---|---|
| 1 | What sources gravity is $T^{\mu\nu}$, not mass | 2.6 built it; energy, momentum, pressure and stress all gravitate |
| 2 | Constraints on the equation | second order in $g$, tensorial, divergence-free, correct Newtonian limit |
| 3 | $G_{\mu\nu}=R_{\mu\nu}-\half R\,g_{\mu\nu}$ is forced | 3.4 item 7 supplies the divergence-free part; ⚑ Lovelock for uniqueness |
| 4 | **Einstein–Hilbert action, varied** | $\delta\sqrt{-g}$, $\delta R_{\mu\nu}$ and the total-derivative term each derived in their own grind box, with the logic outside |
| 5 | **Newtonian limit fixes the constant** | weak field, slow motion, $g_{00}\approx 1+2\Phi/c^{2}$ **(note the sign: this is our $(+,-,-,-)$ signature; texts using $(-,+,+,+)$ write $-(1+2\Phi/c^{2})$, and 3.1 §6 derives our version from the redshift)**; recover Poisson's equation and read off $8\pi G/c^{4}$ |
| 6 | Cosmological constant | where it may enter and why nothing forbids it |

## 3.7 · Schwarzschild

| # | Built | From |
|---|---|---|
| 1 | The symmetric ansatz | staticity and spherical symmetry |
| 2 | **The solution**, derived | solve $R_{\mu\nu}=0$; long, grind-boxed, logic outside. ⚑ Birkhoff stated |
| 3 | Conserved energy and angular momentum | Killing vectors from 3.5 — the payoff for that chapter |
| 4 | Effective potential; the ISCO at $6GM/c^{2}$ | and the contrast with Newton, which has no innermost stable orbit |
| 5 | **Perihelion precession**, with Mercury's 43″ per century | derived |
| 6 | **Light bending**, 1.75″ — and why 3.1's estimate was exactly half | the missing half is spatial curvature; collect the debt explicitly |
| 7 | Redshift from the metric | compare with 3.1's cabin derivation |
| 8 | Horizon: coordinate vs genuine singularity | Kretschmann scalar finite at one, divergent at the other |

**Figure:** effective potential with an angular-momentum slider, the ISCO appearing where Newton
offers nothing.

## 3.8 · Cosmology, and a Loose Thread

| # | Built | From |
|---|---|---|
| 1 | FLRW metric | homogeneity and isotropy, derived rather than quoted |
| 2 | **Friedmann equations** | Einstein's equations with a perfect fluid |
| 3 | Matter-, radiation- and $\Lambda$-dominated solutions | integrate item 2 |
| 4 | Redshift and the scale factor | null geodesics in FLRW |
| 5 | **Energy is not conserved in an expanding universe** | no time-translation Killing vector, so 1.4's theorem simply does not apply. Collects Chapter 1.4's honest note |
| 6 | Horizons | integrate the null condition |
| 7 | **Black-hole entropy $S=A/4$** ⚑ | quoted, not derived — it needs quantum field theory in curved spacetime. Say why it is shocking: entropy scaling with **area** rather than volume. This is the thread 7.8 picks up |

**Figure:** scale factor against time for different matter/radiation/$\Lambda$ mixtures.

---

## Batch order

**3.1 + 3.2** → **3.3 + 3.4** → **3.5 + 3.6** → **3.7 + 3.8**. Two per agent; 3.3 and 3.4 are the
longest and hardest and should not be paired with anything else.
