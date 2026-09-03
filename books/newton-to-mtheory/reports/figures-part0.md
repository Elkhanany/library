# Additional interactive figures in Part 0 — an audit

*Nine chapters read in full, including all twelve existing `<figure>` blocks, the twelve
`<!--SCRIPT-->` bodies behind them, and every `⚠`/`⚑` callout in the part. Proposals only;
nothing in `src/` was edited.*

---

## 1 · What is already there

| Ch | Figure | Section it serves | What it computes |
|---|---|---|---|
| 0.1 | `fig-secant` | §1 | chord slope → tangent slope, as $h\to0$ |
| 0.1 | `fig-zoom` | §3 | error$/h$ → 0 **and** error$/h^{2}$ → a constant |
| 0.2 | `fig-riemann` | §1 | tagged sums; $N\!\times\!$err vs $N^{2}\!\times\!$err for left/mid/right |
| 0.2 | `fig-gauss` | §4 | Simpson's rule on the normalised Gaussian; three invariants |
| 0.3 | `fig-taylor` | §3 | Taylor partial sums; measured trust radius |
| 0.3 | `fig-asym` | §4 | $\log_{10}$ error of a divergent series vs $N$; optimal truncation |
| 0.4 | `fig-lin` | §5 | one $2\times2$ matrix on the square and circle; $\det$, $\operatorname{tr}$ |
| 0.5 | `fig-eig` | §5 | one $2\times2$ matrix on the unit circle; turn angle; eigen-lines colliding |
| 0.6 | `fig-grad` | §3/§7 | contours, gradient field, $\nabla f\cdot\hat t$ at $10^{-12}$, Lagrange overlay |
| 0.7 | `fig-flow` | §4 | RK-integrated flow of a tracer ring; measured div and curl vs analytic |
| 0.8 | `fig-res`, `fig-phase` | §6 | exact absorbed power; measured FWHM vs $2\gamma$; phase lag |
| 0.8 | `fig-coupled` ×3 | §7 | normal-mode decomposition, animated; mode energies separately constant |
| 0.9 | `fig-bw-x/k` | §6 | honest $O(N^{2})$ DFT; second moments of both densities |

Three sections carry a `⚠` and **no** figure anywhere near them: **0.4 §4.2** (the matrix
is not the map; matrices do not commute), **0.7 §2** (curl-free is local, has-a-potential
is global), **0.6 §1** (which variable is held fixed). Two of the three are the basis of
the proposals below; the third is rejected in §5.

The idioms the existing scripts establish, which the proposals are written against:
`NMT.figure(id, draw)` · `new NMT.Plot(canvas, {xmin…, equal:true})` · `.axes() .fn()
.path() .dot() .seg() .text()` · `NMT.css('--accent'|'--insight'|'--warn'|'--familiar'|
'--rule'|'--ink-faint')` · `NMT.redrawAll()` on every `input`. Each figure hand-rolls its
own `arrow()` and its own `clipped()` wrapper; `fig-zoom` and `fig-asym` carry $\log_{10}$
values in the slider's `value` and exponentiate on read; `fig-coupled` runs a
`requestAnimationFrame` loop behind a play button; `fig-grad` and `fig-flow` add canvas
dragging via `invX/invY` (mouse only — no touch handlers anywhere in Part 0).

---

## 2 · The chapter you asked me to test: 0.5 §8

### Verdict on the proposal as briefed: it does not clear the bar.

The brief was *two Hermitian matrices, a control that tunes the commutator continuously to
zero, and the two eigenframes drawn together, so the reader watches the frames rotate into
alignment exactly as the commutator vanishes.*

For real symmetric $2\times2$ matrices — the only case `NMT.Plot` can draw as two frames in
a plane — write $A = \alpha_0 I + \alpha\,(\cos2a,\sin2a)\!\cdot\!(\sigma_z,\sigma_x)$ and
likewise for $B$ with angle $b$. Then

$$\lVert[A,B]\rVert_F \;=\; 2\sqrt2\,\alpha\beta\,\bigl|\sin 2(a-b)\bigr|,$$

and $a-b$ *is* the misalignment of the two eigenframes. "The frames align exactly as the
commutator vanishes" is therefore $|\sin\theta|\to0$ as $\theta\to0$. Nothing is discovered:
the figure would compute a quantity the reader can already read off the theorem statement he
has just been given with an *if and only if* in the middle. It fails **bar 1** — the insight
does not live in the change, it lives in the definition — and it fails **bar 3**, because
0.5's only `⚠` (§6.5) is about non-diagonalisable matrices, which `fig-eig` already covers
at $c=1$.

Worse, it shows the wrong half. §8.1 (forward, three lines) is what two aligned frames
depict. §8.2 is labelled *"Reverse direction (**the real content**)"* and its content is
degeneracy — and a $2\times2$ Hermitian matrix with a degenerate eigenvalue is a multiple of
the identity, so the interesting case cannot occur in the picture at all.

### But there is a figure in §8, and it is not that one.

The thing §8 actually contains that appears nowhere else in the book is Step 4 of the grind
box, which is currently folded shut:

> *"This is exactly where degeneracy is handled: within a degenerate eigenspace of $A$, the
> operator $B$ chooses the basis that $A$ could not."*

and §6.4's setup for it:

> *"any orthonormal basis of the eigenspace $E_\lambda$ will do — the choice is not unique,
> and no theorem prefers one."*

I built the numerical case while auditing. It is sharper than I expected, and it is the
reason candidate **B** below is in the list. Take

$$A=\operatorname{diag}(1+\delta,\,1,\,-1),\qquad
B=\begin{pmatrix}0&b&0\\ b&0&0\\ 0&0&2\end{pmatrix},\quad b=0.6 .$$

| $\delta$ | $\lVert[A,B]\rVert_F$ | $\Delta B$ in the eigenvectors a solver returns for $A$ |
|---|---|---|
| 1.00 | 0.84853 | $(0,\;0.6,\;0.6)$ |
| 0.20 | 0.16971 | $(0,\;0.6,\;0.6)$ |
| 0.01 | 0.00849 | $(0,\;0.6,\;0.6)$ |
| **0.00** | **0.00000** | **$(0,\;0.6,\;0.6)$** |

The commutator goes to zero and the incompatibility does not move. At $\delta=0$ the two
operators commute *exactly* and a standard eigensolver still hands back states in which $B$
has a spread of $0.6$ — because inside the degenerate plane it returned *an* eigenbasis of
$A$ rather than *the* one $B$ prefers. The theorem promises a common eigenbasis exists; it
does not promise the basis in front of you is it, and you must go inside the eigenspace and
choose. That is Step 4, and it is invisible in the text because Step 4 is inside a
`<details>`.

That is a fact about how something varies with a parameter, it is a genuine surprise, it is
computed, and no static figure states it. It is also exactly what 4.9 (hydrogen's degeneracy
in $n$, resolved by $\ell$ and $m$) and 4.10 (degenerate perturbation theory) are going to
need. So: the *territory* you identified is right; the *figure* has to be a different one.

---

## 3 · The proposals

Three. Ranked. If only two get built, build 1 and 2 — they are a matched pair (0.4 gives the
commutator a geometric meaning; 0.5 spends it), and together they cover the object this book
uses more often than any other.

---

### 1 · **The gap that does not close** — Chapter 0.4, §4.2 (`⚠`), placed after §3.3

**The confusion it dissolves.** 0.4's `⚠` box says the commutator is important and then draws
nothing:

> *"(b) **Matrices do not commute, and the reason is not algebraic.** … Follow the single
> vector $e_1=(1,0)$: rotating first sends it to $(0,1)$ and then reflecting sends it to
> $(0,-1)$; reflecting first leaves it at $(1,0)$ and then rotating sends it to $(0,+1)$.
> Same start, opposite finish. … The quantity $[A,B]=AB-BA$ measuring the failure is the
> **commutator**, and its non-vanishing is not a nuisance to be tidied away. **It is most of
> modern physics.** $[\hat x,\hat p]=\ii\hbar$ is the uncertainty principle (Chapter 4.7) …
> The commutator of two covariant derivatives is the curvature of spacetime (Chapter 3.4) —
> transporting a vector east-then-north differs from north-then-east, and the difference is
> gravity. And the commutator of two gauge fields is why gluons interact with each other
> while photons do not (Chapter 6.4)."*

The reader finishes that box knowing $[A,B]$ is a difference of two products and that it
matters enormously. He does not know **what it is**, and the three cash-outs the box promises
— curvature, uncertainty, gluon self-interaction — are all *infinitesimal* statements, none
of which the finite reflect-then-rotate example reaches. The specific gap: the failure to
commute is a **second-order** effect. It vanishes to first order, which is why nobody noticed
it for three centuries, and the number that survives is the limit of gap$/\varepsilon^{2}$.

**Why a static figure cannot do it.** A static picture at one step size $\varepsilon$ shows a
quadrilateral with a gap in it, and gives the reader no way to know whether that gap is
$O(\varepsilon)$, $O(\varepsilon^{2})$ or $O(1)$ — which is the entire content. The order in
$\varepsilon$ is not a thing a drawing can assert; it is a thing a ratio can converge to.
This is precisely the manoeuvre `fig-zoom` already performs in 0.1 ("the error divided by
$h^{2}$ settles on a finite constant"), so the reader has been trained on the rhetoric and
will recognise it. The figure is the second performance of a move he has already been sold.

**What is computed.** Two $2\times2$ matrices $A,B$ from sliders or presets. For the current
$\varepsilon$, form the four linear maps $I+\varepsilon A$, $I+\varepsilon B$ and their exact
inverses, apply them in order to the dragged base point $x$, and plot the four-leg path
$x \to (I{+}\varepsilon A)x \to \cdots$. The residual is
$r(\varepsilon)=\bigl[(I{+}\varepsilon A)(I{+}\varepsilon B)(I{+}\varepsilon A)^{-1}
(I{+}\varepsilon B)^{-1}-I\bigr]x$, verified algebraically to be
$\varepsilon^{2}[A,B]x+O(\varepsilon^{3})$. Readouts: $|r|/\varepsilon$, $|r|/\varepsilon^{2}$,
the printed matrix $[A,B]$, the printed vector $[A,B]x$, and the angle between $r$ and
$[A,B]x$. Run for the preset $A=$ rotation generator, $B=$ squeeze generator, $x=(1,0.3)$:

| $\varepsilon$ | $|r|/\varepsilon$ | $|r|/\varepsilon^{2}$ |
|---|---|---|
| 0.40 | 0.6476 | 1.6191 |
| 0.10 | 0.1927 | 1.9269 |
| 0.02 | 0.0411 | 2.0537 |
| 0.01 | 0.0207 | 2.0708 |

against $\bigl|[A,B]x\bigr| = 2.08806$. The first column crashes; the second climbs onto the
printed constant. For a commuting pair (rotation and dilation) the residual is
$2.1\times10^{-16}$ at $\varepsilon=0.4$ — **the loop closes exactly, at every step size**,
which is what commuting *is*.

**The controls.** A $\log$-spaced $\varepsilon$ slider (same idiom as `fig-zoom`'s
`min="-3.2"`), with the plot window auto-scaling as $\varepsilon^{1}$ so the quadrilateral
stays the same size on screen while the readouts change. Four entries of $A$ and four of $B$,
or presets: **rotate + reflect** (the `⚠` box's own example, run in "finite" mode where the
two two-leg paths land at $(0,-1)$ and $(0,+1)$ — same start, opposite finish, gap $O(1)$);
**rotate + squeeze**; **rotate + dilate** (commuting, gap identically zero); **two shears**.
A draggable base point $x$, so the reader sees that $[A,B]x$ is a *field* — the gap points
differently at different places, which is what makes it curvature later. What to watch while
dragging $\varepsilon$: the two ratio readouts, in opposite directions.

**The moment of insight.** *You shrink the step and the quadrilateral closes — but the gap
divided by the square of the step climbs onto a fixed number and stops, and the residual
arrow lies along $[A,B]x$: the failure to commute is not a first-order effect at all, it is
the area you enclosed.*

**Cost.** ~180 lines. Needs a $2\times2$ multiply/inverse/apply trio (~15 lines), an `arrow()`
(hand-rolled as in `fig-eig`), a `clipped()` (hand-rolled as in `fig-grad`), and the
$\varepsilon$-tracking window (hand-rolled as in `fig-zoom`). Nothing new from `NMT.Plot`.

**What it pre-loads.** 3.4 (curvature as the commutator of covariant derivatives — the
east-then-north picture, literally this figure with a connection in it), 4.7 item 2
($\Delta A\Delta B\ge\tfrac12|\langle[A,B]\rangle|$), 4.8 items 1–7 (the entire angular
momentum theory derived from *nothing but* a commutator), 6.1 (Lie bracket), 6.4 (gluon
self-interaction). The `⚠` box names three of the five by chapter number.

---

### 2 · **The joint spectrum, and the choice inside a degeneracy** — Chapter 0.5, §8, after §8.2

**The confusion it dissolves.** Not a `⚠` — 0.5's only `⚠` is elsewhere — but a plain-terms
box under visible strain and a proof step folded shut. 0.5.8 has to carry Step 4 in one
sentence with no picture available:

> *"Wherever the first map cannot distinguish between several directions, having given them
> all the same number, the second goes inside that ambiguity and chooses, and between them
> they produce one set of directions suiting both."*

and then the whole notion of a complete set:

> *"…the labels fixing the state completely once there are enough maps to leave no ambiguity."*

Everything in those two clauses is unrepresented anywhere in the book. The insight box makes
the claim that will carry the reader through three Part IV chapters —

> *"the reason a state can have a definite $\ell$ **and** a definite $m$ at the same time — is
> Step 4 above, and nothing else"*

— and Step 4 is inside a `<details class="grind">` that most readers will not open. Meanwhile
§6.4 has already told him the thing that makes it bite: *"any orthonormal basis of the
eigenspace $E_\lambda$ will do — the choice is not unique, and no theorem prefers one."*

**Why a static figure cannot do it.** The control space has two independent axes — how badly
the operators fail to commute, and how degenerate $A$ is — and the whole content is in the
*corners and the paths between them*. Commuting and non-degenerate: sharp joint labels.
Non-commuting and non-degenerate: labels with spread. Commuting and degenerate: the case
where a naïve reading of the theorem is wrong, because the labels are sharp only if you make
the right choice inside the eigenspace. A static figure can show one corner. Showing four
would be four figures, and would still not show that the third corner is reached *without the
spread ever shrinking* — the fact in the table in §2 above, which is the surprise.

**What is computed.** Real symmetric $3\times3$ $A$ and $B$ (Hermitian; §6.5 licenses the real
case), diagonalised by cyclic Jacobi rotations to machine precision — no closed forms, no
hard-coded eigenvectors. Then, plotted in the $(a,b)$ plane:

* for each eigenvector $v_i$ of $A$: a point at $\bigl(a_i,\ \langle v_i,Bv_i\rangle\bigr)$
  with a vertical bar of half-length $\Delta B_i=\sqrt{\langle v_i,B^2v_i\rangle-\langle
  v_i,Bv_i\rangle^{2}}$;
* for each eigenvector $w_j$ of $B$: a point at $\bigl(\langle w_j,Aw_j\rangle,\ b_j\bigr)$
  with a horizontal bar $\Delta A_j$;
* $\lVert[A,B]\rVert_F$, computed;
* when $A$ has a degenerate pair, a **shaded vertical band** at that $a$ spanning the
  numerical range of $B$ over the degenerate plane — the full interval of $\langle B\rangle$
  values that *some* legitimate eigenbasis of $A$ would report. Its endpoints are computed by
  diagonalising $B$ restricted to the plane, and they turn out to be exactly the two
  eigenvalues $B$ has there.

**The controls.** (i) $c$ — the strength of the part of $B$ that does not commute with $A$;
(ii) $\delta$ — the gap between $A$'s first two eigenvalues, driven to zero; (iii) a button
**"let $B$ choose"**, which replaces the solver's arbitrary basis of the degenerate eigenspace
with the one that diagonalises $B|_{E_\lambda}$; (iv) a button adding a third commuting
operator $C$, with the readout **"labels distinct: 2 of 3"** → **"3 of 3 — complete set"**.
What to watch: the bars, and whether the two families of points have merged into one set of
dots.

**The moment of insight.** *You drive the commutator to exactly zero, and the error bars do
not move — then you press "let $B$ choose", the eigenvectors swing inside the degenerate
plane without $A$ noticing at all, and the bars collapse to nothing as three joint labels
snap into place.*

**Cost.** ~230 lines, the largest of the three. Needs a symmetric Jacobi eigensolver (~45
lines), a $3\times3$ matrix helper set (~25 lines), error bars (two `.seg` calls each), the
shaded band (`.path({fill})`), `arrow()` and `clipped()`. **Design risk, stated:** near
$\delta=0$ and before "let $B$ choose", the returned eigenvectors inside the near-degenerate
plane are genuinely ill-conditioned and the dots will jitter as the slider moves. That is the
truth being displayed, not a bug, but it has to be *labelled* as such in the caption or it
will read as broken. The shaded band is the honest rendering and should appear as soon as the
gap falls below a stated tolerance.

**What it pre-loads.** 4.2 item 8 (quantum numbers, defined — *"Collects 0.5's promise by
name"*), 4.7 item 5 (compatible observables and the complete set — logged in `MATHPLAN-4.md`
as **"0.5 §8, unchanged"**, meaning 4.7 adds nothing and a reader who did not get §8 will not
get another chance), 4.9 (hydrogen's degeneracy in $n$, resolved by $\ell$ and $m$), 4.10
(degenerate perturbation theory, which is nothing but "choose the right basis inside the
eigenspace first"). 0.5 is the largest single creditor in Part IV's debt map — 12 debts to
4.2 alone — and this is the one section of it with no figure of any kind.

---

### 3 · **The circulation that does not care about the loop** — Chapter 0.7, §2.4

**The confusion it dissolves.** The sharpest `⚠` in Part 0, and §2 has no figure at all
(`fig-flow` serves §4):

> *"**'Curl-free' is a local statement. 'Has a potential' is a global one.** This is the trap
> of §2, and it is worth stating as sharply as possible. The field
> $\vv F=(-y,x)/(x^{2}+y^{2})$ is smooth on its whole domain and its curl vanishes at every
> single point of that domain. **There is no point at which any local measurement detects
> anything unusual.** And yet no single-valued potential exists, and the circulation around
> the hole is $2\pi$. What went wrong is not analysis; **it is the shape of the region.** …
> This is the first place in the book where a topological fact has a measurable consequence."*

There is a specific suspicion the text invites and cannot kill. §2.4 computes $\oint=2\pi$ on
*a circle centred on the origin*, where "the factors of $R$ cancel exactly". A reader with
any residual instinct for how integrals behave will file that as a coincidence of a
symmetrical choice. It is not — the number is the same for a lopsided, off-centre, five-lobed
loop — and the only way to establish that is to let him maul the loop himself.

**Why a static figure cannot do it.** The content is *deformation invariance*: one number,
$6.28318$, that does not respond to any change in the loop's shape, size or centre, and then
falls discontinuously to zero the instant the loop stops enclosing the puncture. A static
figure can draw one loop, or three, and must then assert the invariance in the caption —
which is exactly the assertion the reader has no reason to accept. Invariance under
continuous deformation is, definitionally, a fact you can only exhibit by deforming.

**What is computed.** (i) $\oint_C \vv F\cdot\dd\vv r$ by midpoint summation over the
reader's loop, sampled at $N\!\approx\!2000$ points — verified: $6.283186$ for a loop centred
at $(0.3,-0.2)$ with $45\%$ three-fold and $30\%$ five-fold lobes, $6.283198$ for one centred
at $(0.6,0.4)$, $0.000000$ for one centred at $(2.5,0)$. (ii) The curl at sample points along
the loop, by central differences, printed as $\sim\!10^{-11}$ — *the local measurement that
detects nothing*. (iii) The running potential $\phi(s)=\int_0^s\vv F\cdot\dd\vv r$ against
arclength, in a second panel: it climbs and **fails to return to where it started**, by
exactly $2\pi$, and the residual is drawn as a bracket. (iv) The winding number
$\oint/2\pi$, printed as an integer to five decimals.

**The controls.** Drag the loop's centre directly on the canvas (`invX/invY`, as `fig-grad`
does). A **lumpiness** slider adding $\cos3\theta$ and $\sin5\theta$ harmonics to $r(\theta)$
— the shape becomes grotesque and the number does not move. A radius slider. A **two turns**
preset ($4\pi$). A field toggle: the vortex against $\nabla(xy)$, a genuinely conservative
field on the same domain, whose running-potential trace closes for every loop.

**The moment of insight.** *You drag the loop off the origin and the running-potential trace
in the lower panel snaps shut while the circulation readout falls from $6.28318$ to $10^{-14}$
— and then, with the loop back around the hole, you can twist it into any shape you like and
the number will not move a digit.*

**Cost.** ~190 lines, two stacked canvases. Needs `arrow()`, `clipped()`, the drag handler
(copy `fig-grad`'s), and nothing else. Cheapest of the three per unit of payoff.

**What it pre-loads.** 3.5 (cohomology — the `⚠` says so: *"Chapter 3.5's cohomology is the
machinery for saying it once"*), 6.3 (Aharonov–Bohm, which §2.5 has already set up in full:
$\vv B=\vv0$ everywhere the electron goes and the interference pattern moves anyway), 6.5
(the $\theta$-vacuum), 7.7 (soliton and brane stability). Weaker Part IV yield than 1 and 2,
which is why it ranks third rather than first despite having the strongest documented
difficulty in the part.

---

## 4 · Ranking

| | Figure | Chapter | `⚠` evidence | Part IV yield | Build risk |
|---|---|---|---|---|---|
| **1** | The gap that does not close | 0.4 §4.2 | **explicit and unspent** | high (4.7, 4.8) + 3.4 + 6.1/6.4 | low |
| **2** | The joint spectrum | 0.5 §8 | strained plain-terms box; folded proof step | **highest** (4.2, 4.7, 4.9, 4.10) | medium — degenerate solver |
| **3** | The circulation | 0.7 §2.4 | **strongest in the part** | low; 3.5/6.3/6.5/7.7 instead | low |

If one gets built: **1**. It gives a geometric meaning to the object this book uses more
often than any other, and it targets a `⚠` that currently promises the reader that something
is "most of modern physics" and then shows him nothing.

If two: **1 and 2**, in that order and in that pairing. 0.4 defines the commutator as the
gap in a loop; 0.5 spends it on what a *vanishing* commutator buys. That is `PLAN.md` §2's
four-part rule — question, picture, cousin, calculation — applied to figures.

---

## 5 · Candidates considered and rejected

**0.5 §8, as briefed** — two eigenframes rotating into alignment. Rejected: for real
symmetric $2\times2$ the commutator norm is $2\sqrt2\,\alpha\beta|\sin2(a-b)|$ with $a-b$ the
frame misalignment, so the figure animates $|\sin\theta|\to0$; it depicts the easy forward
direction and cannot reach §8.2's degeneracy at all, because a degenerate Hermitian
$2\times2$ is a multiple of the identity. Reconstructed as candidate 2. Full argument in §2.

**0.6 §4 — the one-form as a stack of level lines, the gradient as an arrow, with a metric
knob.** The closest call in the audit, and the one I most regret cutting. §4 is where "raising
an index is not just moving a letter" is introduced, the chapter itself concedes *"the whole
issue can seem like pedantry"*, and plain-terms 0.6.4 ends on the line the figure would draw:
*"The measuring device is always there; the arrow is not."* `fig-grad` shows contours and a
gradient arrow but never separates them. Rejected because **the only control that makes it
move is unmotivated at this point in the book.** A slider labelled "now pretend the inner
product is something else" is a knob for its own sake — the precise failure mode the standing
rule exists to prevent. The motivated version has the reader change *coordinates* and watch
$\partial_i f$ transform with the Jacobian while $(\nabla f)^i$ transforms with its inverse
transpose, invariant pairing printed between them — and that figure belongs to Chapter 2.4,
which this audit did not cover. **Recommend it be reconsidered when 2.4 is audited.**

**0.7 §5 — the cancellation mechanism (interior faces cancel in pairs, only the boundary
survives).** Fails bar 1 outright. One well-drawn static grid with opposed arrows on every
shared edge carries the whole argument, which is why the prose carries it already: *"add up
local changes, watch the interior cancel in pairs, keep what is left on the boundary."*
Nothing varies.

**0.9 §7 — convolve-and-rescale toward the Gaussian, with the Cauchy counterexample.**
Rejected on audience. The Familiar Ground box in that section says it plainly: the standard
error is *"the most expensive line of algebra in clinical research"*. This reader has owned
the CLT and the $1/\sqrt n$ for twenty years; a figure showing him densities becoming
Gaussian teaches him nothing. The one genuinely novel item — that averaging a million Cauchy
samples buys the precision of one — is closed in three lines of algebra in the existing grind
box and does not need pixels.

**0.9 §4 — the sliding convolution / Green's function.** The canonical decoration. The
sliding-and-overlapping animation is what every signal-processing course draws, and it
illustrates a definition rather than resolving a difficulty. The section's real content —
that the transfer function *is* the transformed Green's function, and that $G(u)=0$ for $u<0$
*is* causality — is algebraic, already crisp, and `fig-res` in 0.8 already owns the resonance
side of it.

**0.9 §5 — the delta as a limit of narrowing bumps.** Actively harmful. The `⚠` there says
*"The delta is not a function, and pretending otherwise produces real damage"*, and a picture
of a tall narrow bump is precisely the pretence. `fig-gauss` in 0.2 already sends the reader
here with the right framing (*"push $\sigma$ to its minimum and you are watching the Dirac
delta of Chapter 0.9 form"*), and that is as far as the picture should go.

**0.5 §7 — $\ee^{\ii A}$ as a unitary flow on a state.** Rejected on budget, not on merit.
`MATHPLAN-4.md` assigns a Bloch sphere to 4.2 (*"watch the state precess"*) and a second one
to 4.8 (*"the sphere returns at $360^\circ$ and the phase does not"*). Building it in 0.5
spends the payoff two parts early and makes two Part IV interactives redundant.

**0.3 §3 — drag the expansion centre, watch the trust radius track $\sqrt{1+a^{2}}$, the
distance to the invisible pole at $\pm\ii$.** Genuinely tempting and cheap. Rejected because
the difficulty is already closed in the text: `fig-taylor` stalls the trust radius dead at
$|x|=1$, the Abel lemma in §3.3 proves the convergence set is a disc, and the insight box
lands it (*"The real line does not know why its own series fails; the complex plane does"*).
The extra fact is a verification of a settled claim, not a difficulty.

**0.8 §3 — the confluent limit, two roots colliding and the difference quotient becoming
$t\ee^{\lambda t}$.** Fully derived in the grind box, and the *collision* imagery is already
carried by `fig-eig`'s two eigen-directions merging at $c=1$ — the same visual would be doing
its second tour.

**0.6 §1 `⚠` — $(\partial f/\partial x)_y=0$ versus $(\partial f/\partial x)_z=-1$.** A real
`⚠`, and the reason thermodynamics is written with subscripts. Rejected because the two-line
demonstration in the box is already the cleanest possible statement of it, and what a figure
would add — two different directions drawn through one point — is a static figure.

**0.8 §8 — a nonlinear or chaotic oscillator.** The most attractive-looking thing in Part 0
and one of the emptiest. The `⚠` there says *"Superposition is a privilege, not a law of
nature"*, and that claim is one line of algebra about the linearity of $L$; watching a driven
pendulum go chaotic illustrates a different subject.

---

## 6 · What is missing from `NMT.Plot`

None of the three proposals needs a new primitive to be *possible*; all three would be
cheaper and less duplicative if these existed. In rough order of how often Part 0 already
re-implements them by hand:

1. **`Plot.prototype.arrow(x1,y1,x2,y2,opts)`** — hand-rolled four times already, in two
   incompatible styles (`fig-grad` builds the head from three `.seg` calls in data
   coordinates; `fig-eig` fills a triangle in screen coordinates). All three proposals need
   arrows. This is the single highest-value addition.
2. **Clipping on `.seg()`, `.dot()`, `.text()`** — `.fn()` and `.path()` clip; the other three
   do not, so `fig-grad` and `fig-flow` each carry their own `clipped()` wrapper. All three
   proposals draw segments that can run off the plot area.
3. **`Plot.prototype.bar(x,y,half,opts)`** — an error bar with caps. Candidate 2 draws six of
   them. Trivially two `.seg` calls, but it will otherwise be re-derived.
4. **Touch handling in the drag idiom.** `fig-grad` and `fig-flow` bind `mousedown`/`mousemove`
   only; there are no `touchstart` handlers anywhere in Part 0, so canvas dragging is
   silently dead on a tablet. Candidate 3 is a drag-first figure and would inherit the
   defect. Worth fixing centrally rather than per figure.
5. **A small matrix module** (`mul`, `inv`, `apply`, `symEig` for $2\times2$ and $3\times3$).
   `fig-eig` already carries a $2\times2$ eigensolver; candidate 1 needs $2\times2$
   inverse-and-multiply; candidate 2 needs a symmetric $3\times3$ Jacobi routine. Three
   chapters, three private copies, unless it is shared.
6. **An `xscale:'log'` axis option.** Not needed by any of the three — `fig-zoom`, `fig-asym`
   and candidate 1 all carry $\log_{10}$ in the slider value and exponentiate on read, which
   works — but it is the one genuine gap in the axis code and candidate 1 would be the fourth
   figure to work around it.

No 3-D projection is required by anything above, and none is proposed. Candidate 2's
degeneracy is rendered in the $(a,b)$ label plane and as a shaded interval, not as a plane in
$\R^3$, specifically so that a hand-rolled wireframe never has to exist.
