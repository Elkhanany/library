# Where one more interactive figure would earn its place

*Audit of Part I (`src/ch1-1.html` … `ch1-4.html`) and Part II (`src/ch2-1.html` … `ch2-6.html`).
Ten chapters read in full, including every `<figure>` block and every `<!--SCRIPT-->` body; all
51 `⚠`/`⚑` callouts in the two parts extracted and read (14 across Part I, 37 across
Part II); `CONVENTIONS.md`,
`MATHPLAN-2.5-2.6.md`, `PLAIN-TERMS-PLAN.md` §2, `GAPS.md` G5, and `assets/book.js` read.
No file was edited. Every numerical claim below was checked before it was written.*

---

## Summary

**Two proposals. Nine rejections.**

| Rank | Figure | Chapter | Goes after |
|---|---|---|---|
| **1** | **The conjugate point** — where "least action" stops being least | 1.2 §5 | the `⚠ Why this isn't obvious` at `src/ch1-2.html:757` |
| **2** | **The boost orbit in field space** — which fields can be transformed away, and which cannot | 2.6 §7 | the `Reading the invariants as a classification` insight callout, before plain-terms 2.6.7 |

Both were tested against all five conditions and both pass all five. Nine further ideas were
tested and failed; they are listed at the end with the condition each failed, because that list is
the evidence the bar was applied rather than described.

**On the two you already suspected:** the Legendre transform (1.3) **fails** — reasoning in
R1, and it fails for a reason that matters to `GAPS.md` G5 rather than to the figure. The field
tensor under a boost (2.6) **fails as you posed it** and **passes in a different form** — the
difference is R2 versus Proposal 2, and it is not a quibble: the version you described animates an
identity the book has already measured once, and the version below shows something the chapter
states in a table and cannot draw.

---

## Proposal 1 — The conjugate point

**Chapter 1.2 §5, immediately below the `⚠` callout at `src/ch1-2.html:757`.**

### The confusion it dissolves

The book warns about this misconception **twice, in two chapters**, and its existing figures
demonstrate the exception rather than the rule.

Chapter 1.1 §5 (`src/ch1-1.html:1030`):

> **⚠ Why this isn't obvious — "least" is the wrong word.** […] the same correction will be
> needed for the "principle of least action" in Chapter 1.2 §5, **where the space of paths is
> infinite-dimensional and saddle points are not the exception but the rule.**

Chapter 1.2 §5 (`src/ch1-2.html:757`):

> **⚠ Why this isn't obvious.** The principle is called "least action" and the quantity is very
> often not least. […] For $\mathcal T > \pi/\omega$ — a trip lasting longer than half a
> period — it is negative: we have exhibited a nearby path with strictly smaller action. The
> stationary path is a saddle. […] **⚑ The general theory — Jacobi's theorem, that the second
> variation is positive definite precisely up to the first conjugate point — is quoted, not
> proved.**

And plain-terms 1.2.5, which asserts the whole thing and can show none of it:

> In a space with infinitely many directions saddles are not the exception, and an oscillator
> travelling for longer than half a period supplies a stationary path with neighbours of strictly
> smaller action.

Now read what the chapter's existing figure and the text under it actually establish. `fig-vary`
takes free fall, deforms the parabola in three sine modes, and the body text at
`src/ch1-2.html:735` concludes:

> manifestly non-negative and zero only for $\eta\equiv0$. **For this system the action is a
> genuine minimum, not merely stationary.**

So the reader is warned twice, in words, that stationary usually is not least — and shown once, in
pixels, a case where it is. That is the specific defect: the only demonstration in Part I points
the wrong way.

### Why a static figure cannot do it

A static figure can show a saddle: plot $\Delta S$ against the amplitude $A$ at three durations and
you get a parabola that opens up, flattens, and opens down. That carries the *fact*. What it cannot
carry is the *reason*, which is Jacobi's theorem, and Jacobi's theorem is a statement that **two
independent things happen at the same instant**: the fan of extremals launched from the initial
event refocuses, and the second variation loses a positive direction. Neither implies the other by
inspection — the book quotes the theorem joining them under a `⚑` — and the only way to see that
they are the same event is to have one control that moves both and to watch them arrive together.
That is bar 1's second clause exactly: a comparison between two things that must be seen
simultaneously. Three static panels place the two facts side by side; only a shared control shows
that they are one fact.

### What is computed

The system is the chapter's own: $L = \tfrac12m\dot x^2 - \tfrac12 m\omega^2 x^2$, units
$m=\omega=1$ declared in the caption, extremal $x_\ast(t)\equiv 0$ on $[0,\mathcal T]$ with
$x(0)=x(\mathcal T)=0$. **Held fixed:** $m$, $\omega$, both endpoints. **Varies:** the trip
duration $\mathcal T$, and the amplitude of the trial deformation.

Three *independent* computations, which must agree and which the caption reports as agreeing:

1. **The fan of extremals.** Twenty-odd solutions of $\ddot x = -\omega^2 x$ launched from
   $(0,0)$ with initial speeds spread over a range, each advanced by fourth-order Runge–Kutta at
   step $10^{-3}$ — not drawn from the closed-form sine. They all return to $x=0$ at
   $t=\pi/\omega$. *The focus is measured, not asserted.*
2. **The second variation.** $\Delta S = S[x_\ast+\eta]-S[x_\ast] = \int_0^{\mathcal T}
   \tfrac12 m(\dot\eta^2-\omega^2\eta^2)\,\dd t$ by direct quadrature, in the style `fig-vary`
   already uses. Checked against the modal identity
   $\Delta S = \tfrac{m\mathcal T}{4}\sum_n a_n^2\big[(n\pi/\mathcal T)^2-\omega^2\big]$:
   quadrature and identity agree to nine decimals at every duration tested
   ($\mathcal T = 1.0,\ \pi/2,\ \pi,\ 4,\ 2\pi,\ 3.4\pi$).
3. **The Jacobi equation.** The grind box's own equation,
   $\dv{}{t}(P\dot u)-Qu=0$ with $P=\partial^2L/\partial\dot x^2 = m$ and
   $Q=\partial^2L/\partial x^2 = -m\omega^2$, integrated by RK4 from $u(0)=0$, $\dot u(0)=1$, its
   zeros located by bisection on the integrator output. Verified: $3.1415927$, $6.2831853$,
   $9.4247780$ — exactly $n\pi/\omega$ to seven digits, found by an ODE solver that was never told
   the answer.

The three agree because they are the same theorem. That is the point, and the caption says so.

### The panels and the controls

**Panel A — the $(t,x)$ plane** over $[0,\mathcal T_{\max}]$: the extremal $x_\ast\equiv0$ in
bold; the fan of extremals faint behind it; the Jacobi field $u(t)$ dashed; the current trial path
$x_\ast+\eta$ in purple; a moving vertical line at $t=\mathcal T$; small ticks on the axis at each
conjugate point found by computation 3.

**Panel B — the mode spectrum**: eight bars, $\big[(n\pi/\mathcal T)^2-\omega^2\big]$ for
$n=1\ldots8$, against a zero line. Below them, $\Delta S$ as a function of the amplitude of the
selected mode — a parabola that inverts.

**Controls.** One slider that matters: the duration $\mathcal T$, over $[0.3\,\pi/\omega,\
4\,\pi/\omega]$. One amplitude slider. Buttons: *jump to the first conjugate point*, *show the
second extremal*, *reset*.

**What to watch while dragging $\mathcal T$:** the fan in Panel A, the first bar in Panel B, and
the readout `negative directions: k`.

### The moment of insight

**Push the duration past half a period and the first bar crosses zero at the same instant the fan
of extremals closes on the axis — the direction in which the action is flat *is* the second path
through the same two endpoints, and one step further it becomes a direction in which the action
falls.**

A second moment, free: keep dragging. At $2\pi/\omega$ the second bar goes, at $3\pi/\omega$ the
third. The negative directions arrive one at a time and can be counted. That is the Morse index,
and it is also `PLAIN-TERMS-PLAN.md` §2's motif *"falling apart into independent pieces"* turning
up where the reader would never look for it: the second variation is a quadratic form, it
diagonalises in the sine basis, and its eigenvalues cross zero in order.

### Cost

**≈220–260 lines** — within the range of the existing scripts (131 in 1.2, 334 in 2.1). Two
canvases inside one `<figure class="fig">`, the pattern of `ch1-1`, `ch1-4` and `ch2-1`.

Nothing is missing from `NMT.Plot` in kind. `.axes() .fn() .path() .dot() .seg() .text()` cover
everything except filled bars, and every existing script already reaches through to `p.g` for
`fillRect` (see `ch2-6`'s `box()` helper, ≈12 lines, directly reusable). No 3-D, no library, no
new API. `NMT.figure()` gives theme reactivity for free.

### Where it points

The `⚠` it sits under already names the destinations: *"In Chapter 3.8 those two arcs become the
two images of a gravitationally lensed quasar, and the conjugate point becomes the caustic."* It
also repairs a tension the reader will otherwise hit in Part II, where 2.3 §6 and 2.5 §5 need the
worldline to *maximise* proper time — a sign the 1.2 grind box explains and no figure supports.

---

## Proposal 2 — The boost orbit in field space

**Chapter 2.6 §7, after the `Reading the invariants as a classification` insight callout at
`src/ch2-6.html:1305`, before plain-terms 2.6.7.**

### The confusion it dissolves

`src/ch2-6.html:886`:

> **⚠ "$\vv E$ and $\vv B$ are the same thing" — what that does and does not mean.** It does not
> mean you can turn an electric field into a magnetic field by running. The invariants of §7 forbid
> it in general: if $\vv E\cdot\vv B\neq0$ in one frame it is nonzero in every frame, so a field
> configuration with both fields present and non-orthogonal has no frame where either vanishes.

And §7.3, which states as a table what it cannot draw:

> And if $\vv E\cdot\vv B\neq0$, **neither field can be removed in any frame, ever.** The two
> fields are then irreducibly both present, and the best you can do is find a frame where they are
> parallel.

> The pair $\big(F_{\mu\nu}F^{\mu\nu},\ \epsilon FF\big)$ classifies field configurations into
> frame-independent types, **exactly as the sign of $\Delta s^{2}$ classified pairs of events in
> Chapter 2.3** into timelike, spacelike and null.

That last sentence is a promise the chapter makes and does not keep. Chapter 2.3 got a figure in
which the causal classification is a picture — regions, hyperbolae, a light cone. Chapter 2.6 gets
a four-row table.

### What `fig-wire` does not do

`fig-wire` is the chapter's thesis measured against a bench, and it is excellent. It is also **one
point of the classification**: a lab-neutral wire has $\vv E=\vv 0$, so $\vv E\cdot\vv B=0$ and
$B^2-E^2/c^2>0$ — the *magnetic* row, and nothing else. It never displays either invariant. It has
no configuration in which a field cannot be transformed away, so the `⚠` above has no
demonstration anywhere in the chapter. And its boost slider runs $[0,1]$ toward one particular
frame, so the reader never sees an orbit — only a journey between two endpoints.

### Why a static figure cannot do it

Honestly: **most of what you proposed can be done statically.** A two-column table, lab frame
against boosted frame, with six components in each column and the two invariants computed
independently at the foot, carries "six things change and two do not" completely — and Chapter 2.4
has already *measured* precisely that claim once, in `fig-duality`, where $V^i\omega_i$ sits at
$3.50000000$ while all four components wander. Doing it again with more numbers is not a new
claim.

What no static figure carries is the **orbit**. The invariant is not a number that fails to move;
it is the curve the configuration is confined to. Which curve you are on decides whether some
observer can see a pure electric field, a pure magnetic field, or neither — and the boundary
between those cases is a single line at $45°$ which is the *same line*, on the same kind of axes,
as the light cone in `fig-mink` and the massless asymptote in `fig-shell`. You cannot show that a
point is confined to a curve by drawing it at one place on the curve. You have to push it and watch
it fail to leave.

### What is computed

**The configuration, chosen so that boosts along $\hat{\vv x}$ close on two dimensions** —
verified numerically, not assumed:

$$\vv E = (E_\parallel,\ E_\perp,\ 0), \qquad \vv B = (B_\parallel,\ 0,\ B_\perp).$$

Under $F' = \Lambda F\Lambda^{\mathsf T}$ with $\Lambda$ the boost of §5 at rapidity $\phi$:

* $E'_\parallel = E_\parallel$ and $B'_\parallel = B_\parallel$ — untouched, exactly;
* $E'_z$ and $B'_y$ stay identically zero;
* $\big(E_\perp/c,\ B_\perp\big)$ undergoes **exactly a hyperbolic rotation by $\phi$**:
  $e' = e\cosh\phi - b\sinh\phi$, $b' = b\cosh\phi - e\sinh\phi$.

Checked against a full $4\times4$ $\Lambda F\Lambda^{\mathsf T}$ at $\beta=0,\ \pm0.3,\ 0.6,\ 0.9,\
-0.5$ for $\vv E=(0.3,0.8,0)$, $\vv B=(0.5,0,0.35)$: agreement to five decimals on every component,
with $F_{\mu\nu}F^{\mu\nu} = -0.71500000$ and $\epsilon FF = 1.20000000$ constant across the range.

**Held fixed:** the lab-frame configuration, set by four sliders. **Varies:** the rapidity $\phi$.

**Computed at draw time, never stored:** $F^{\mu\nu}$ assembled from the six components; $F'$ by
two matrix multiplications; the six primed components read back off $F'$; and — this matters for
the caption's honesty — **both invariants by explicit contraction of $F'$**,
$\eta_{\mu\alpha}\eta_{\nu\beta}F'^{\alpha\beta}F'^{\mu\nu}$ and a genuine 24-term sum over the
permutations of $\epsilon_{\mu\nu\rho\sigma}$, rather than from the $\vv E,\vv B$ formulae of §7.1
and §7.2. The readouts are then two independent computations that agree, which is what the caption
is entitled to claim.

### The panels and the controls

**Panel A — the transverse plane.** Horizontal $E_\perp/c$, vertical $B_\perp$. The faint family
of invariant hyperbolae $b^2-e^2 = \text{const}$; the two null lines $b=\pm e$ in orange; the bold
hyperbola through the current configuration; the marker; ticks along the bold curve at intervals
$\Delta\phi = 0.5$, so the reader sees the boost sliding the point *uniformly in rapidity* — the
same device `fig-mink` uses, deliberately.

**Panel B — the longitudinal plane.** Same axes, $E_\parallel/c$ and $B_\parallel$, one marker.
It does not move. The whole panel is one sentence: these two are what a boost along $\hat{\vv x}$
cannot touch — and in this configuration their product *is* $\vv E\cdot\vv B$, so the second
invariant is invariant for a reason you can see rather than for a reason you were told.

**Readouts.** $\vv E'$, $\vv B'$; both invariants to ten digits; the frame-independent type,
*computed from the invariants* — electric / magnetic / null / generic; and, when a frame exists
that removes one field, the rapidity required and how far along you are.

**Presets.** *a light wave* · *the wire of §6* · *crossed fields (a velocity selector)* ·
*$\vv E\cdot\vv B\neq0$ — neither can be removed*.

### The moment of insight

**Press *a light wave* and drag the rapidity as hard as it will go: the marker slides down the
$45°$ line toward the origin, both fields shrinking together, and it never leaves the line and
never arrives — you have Doppler-shifted a light wave through every frame there is and failed
either to change what it is or to bring it to rest.**

The second moment is the `⚠`: turn on both longitudinal fields, watch the type readout flip to
*generic*, drag the rapidity across its whole range, and watch Panel B's marker not move by a
pixel. Neither field can be removed, and you can see why — the parts that would have to go are the
parts a boost along the motion never touches.

### Cost

**≈250–280 lines**, comparable to `ch2-6`'s existing 306 and `ch2-3`'s 312. Two canvases in one
`<figure>`. Hyperbola branches drawn parametrically through `.path()` over $\phi\in[-3,3]$ rather
than as functions, which avoids the asymptote problem `.fn()` would have. The 24-permutation
$\epsilon$ contraction is ~15 lines and is worth writing rather than shortcutting to the three
pair-splittings, because the caption's claim of two independent computations should be true.

Nothing is missing from `NMT.Plot`. Drag-on-canvas to place the configuration, if wanted, follows
the pattern already hand-rolled in `ch2-3` and `ch2-5`. No 3-D: the closure of the transverse pair
is what makes this two-dimensional, and it is exact rather than a simplification.

### Where it points

This is `PLAIN-TERMS-PLAN.md` §2's first motif — *"a choice of perspective"* — in its sharpest
form, and it is the **third** appearance of one geometry: the invariant hyperbolae of 2.3
(spacetime), of 2.5 (momentum space, where `fig-shell`'s caption already names the connection), and
now of 2.6 (field space). The caption should say so. It also arms 6.5's $\theta$-term, which the
chapter's own `⚑` at `src/ch2-6.html:1245` flags as a multiple of the second invariant.

---

## Rejected

Nine. Each names the condition it failed.

**R1 · The Legendre transform, with a control that flattens the curvature (1.3 §1).**
*Fails bar 1, and fails bar 3.* The convex-hull story — $f$ with the common tangent, $g^{**}$ with
its flat segment, the argmax $x(p)$ with its jump — is the classic static thermodynamics figure and
has been carried statically for a century; the chapter's own grind box already draws it in words,
does the double well, and names the Maxwell construction. On bar 3, §1 carries **no `⚠`**; the
difficulty is marked only by a `⚑` (Fenchel–Moreau, quoted not proved) and by plain-terms 1.3.1.

The degeneracy variant — the one `GAPS.md` G5 is about — fails differently and worse. §2.2 says the
constrained case *"is quoted here and not developed"*. A figure could therefore show only **that**
the transform breaks, never what replaces it, which is precisely the reader's current position. G5
offers three options — build it in 6.3, route around it via Faddeev–Popov, or declare the deferral
once and prominently — and warns that the worst outcome is the decision being made silently by
default. **A figure is none of the three.** It would make the gap more visible without making it
smaller, and it would let the decision be postponed again while looking like progress. The honest
recommendation is that G5 needs a paragraph in 6.3, not a widget in 1.3.

The closest version considered and dropped: two panels showing the momentum map
$\dot q \mapsto p = W\dot q$ with $W=\mathrm{diag}(1,\varepsilon)$, the velocity plane collapsing
onto the line $p_2=0$ as $\varepsilon\to0$, and the fibres of the collapse being the gauge orbits.
Genuinely illuminating — and rejected because *the fibres are the gauge orbits* is not derived
anywhere in the book, and a figure whose caption asserts underived physics breaks the contract every
other figure in this book keeps.

**R2 · The field tensor's six components under a boost, with the two invariants live (2.6, as
posed).** *Fails bar 1.* A static two-column table, lab frame against boosted frame, with the
invariants computed independently in each column, carries it entirely. And the claim it makes —
a scalar is a scalar — was proved in 2.4 §5.1 and *measured* in 2.4's `fig-duality`, which holds
$V^i\omega_i$ at $3.50000000$ while every component wanders and then breaks the wrong pairing to
$77.144991$. Repeating that demonstration with six numbers instead of two is not a second claim.
Proposal 2 keeps the physics and throws away the framing: the invariant is the orbit, not a number
that sits still.

**R3 · $\vv F$ and $\vv a$ are not parallel (2.5 §6.3).** *Fails bar 1.* One static figure — a
circle of force directions with the corresponding response ellipse, semi-axes $F/\gamma^3m$ and
$F/\gamma m$, four paired arrows — carries the non-parallelism, the anisotropy, and §6.4's "no
scalar can be the mass" argument. Only the eccentricity varies with $\beta$, and the text already
gives the ratio as $\gamma^2$. The one fact a figure would add — the maximum misalignment satisfies
$\tan\delta_{\max} = \gamma\beta^2/2$, so $\vv F$ and $\vv a$ are $42.9°$ apart at $\beta=0.9$ and
approach perpendicular — is a sentence, and belongs in the grind box.

**R4 · The Wigner rotation (2.2 §4, the `⚠` at `src/ch2-2.html:571`).** The closest miss. It has a
`⚠`, it is genuinely counterintuitive, and it is computed — compose two boosts, decompose the
product, extract the residual rotation. *Fails on scope.* The chapter deliberately routes it to
Problem 3 — *"Problem 3 derives that the effect must exist, in two lines"* — and a figure sitting
above the problem does the reader's work for them. Secondarily, the composite acts on $(ct,x,y)$
and the honest picture needs three axes hand-projected.

**R5 · Every observable generates a flow — the two-way street (1.3 §7).** *Fails bar 5.* The
chapter calls §7 *"the deepest section in the chapter"*, which is real evidence, and a figure could
run the $H$-flow and the $G$-flow side by side with both readouts going flat together. But the
depth is in an identification, not in a behaviour: what would be on screen is
$\{G,H\}=-\{H,G\}$, one line of antisymmetry, already believed by anyone who has read §6.3. Nothing
surprising happens. And 1.4's `fig-orbit` already owns "break a symmetry, watch the matching law
fail, and only that one".

**R6 · Why colliders exist (2.5 §8).** *Fails bar 1.* Two curves on log–log axes,
$\sqrt s = \sqrt{2mc^2E}$ against $\sqrt s = 2E$, slopes $\tfrac12$ and $1$. Important, quantitative,
and wholly static — the same shape as `fig-mmscale`, which is a *panel* of an existing figure, not a
figure.

**R7 · The field carries the missing momentum (2.6 §10, paying 1.1 §3.3's IOU).** *Fails bar 1, and
expensive.* This is the longest-running promise in Parts I–II and the temptation is real, but the
payment is a bookkeeping identity evaluated once at one configuration; there is no parameter whose
variation carries the insight. Drawing $\epsilon_0\vv E\times\vv B$ for two charges moving in
different directions needs a hand-projected 3-D vector field, and §10's own `⚠` records that the
self terms diverge — the figure would have to display a subtraction the text performs in closed
form.

**R8 · The field of a uniformly moving charge — the "pancake" (2.6 §5).** *Fails bars 1 and 3.*
Three static panels at $\beta = 0,\ 0.6,\ 0.95$ carry it; there is no `⚠` about it anywhere; and
the chapter works through the transformation rules rather than the field-line picture, so the figure
would illustrate a claim the text does not make.

**R9 · Off shell versus on shell (1.4 §1).** *Fails bar 1.* The text says getting these two
quantifiers backwards *"is the single most common way to misstate this theorem"*, which is strong
evidence — but the demonstration would be $\delta L$ evaluated along paths that solve nothing, and
nothing visually distinguishes such a path from a solution. The failure is logical, not geometric,
and §7's scaling counterexample already carries it in four lines.

*Also considered and dropped without argument, as plainly decorative under the standing rule: a
double-pendulum animation for 1.2 §6 (the chapter's claim there is about counting unknowns, not
about chaos); a Galilean-boosted wave packet for 2.1 §4 (the failure is an algebraic cross term);
and a ladder-and-barn animation for 2.2 §7 (`fig-lt` already contains the simultaneity slices that
resolve it).*

---

## Two notes on the API, for whoever builds these

* **`NMT.Plot` is sufficient for both.** Neither proposal needs 3-D and neither needs a library.
  The only recurring absence is an arrow with a head, which four existing scripts each hand-roll in
  ~15 lines (`ch2-4`'s `arrow()` is the cleanest); if a third figure ever wants one it is worth
  lifting into `book.js` rather than writing a fifth copy. Filled bars and boxes likewise —
  `ch2-6`'s `box()` is directly reusable.
* **Both figures should declare their units in the caption**, per `CONVENTIONS.md`'s ruling that
  local $c=1$ is permitted inside a figure where it is declared at the point of use. Proposal 2
  needs it (fields in units where $c=1$, so $E$ and $B$ share an axis); Proposal 1 needs
  $m=\omega=1$ stated, as `fig-orbit` already does.
