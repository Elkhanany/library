# Part III — where one more interactive figure would earn its place

*An audit, not a build. Nothing in `src/` was edited.*

Read for this: all nine chapters of Part III including every `<figure>` block and every
`<!--SCRIPT-->…<!--/SCRIPT-->`; all 36 `callout warn` boxes in the part — an even split, 18
`⚠` difficulty markers and 18 `⚑` provenance flags, with the `⚠` count running
3, 2, 2, **0**, 1, 3, 2, 3, 2 across 3.1–3.9; `MATHPLAN-3.md`, `MATHPLAN-3.7-3.9.md`,
`PLAIN-TERMS-PLAN.md` §2, `CONVENTIONS.md`, `reports/README.md`; `assets/book.js` and
`assets/book.css`. Every candidate below was checked numerically in Python before being
proposed — the "moment of insight" in each case is a thing I have watched happen, not a
thing I expect to happen.

**Three candidates accepted. Eight rejected.**

---

## The bar, and what it excluded

The five tests were applied as written. Two of them did most of the killing:

- **Test 1 (the insight lives in the change).** Most good ideas about Part III are good
  *static* ideas. The Flamm paraboloid, the conformal cosmological diagram, the Riemann
  symmetry count, the geodesic-deviation ellipse — all of these are published as static
  figures because static is what they need. Anything whose core survives being printed once
  was cut.
- **Test 4 (not already covered).** Part III's nine figures are unusually strong and
  unusually wide. `fig-tide` already owns tidal deviation *and* the traceless-matrix
  arithmetic; `fig-holo` already owns holonomy *and* the shrinking-loop limit; `fig-veff`
  already owns the ISCO *and* the non-existence of orbits below `2√3`. Several plausible
  proposals turned out to be second helpings.

One structural gap is worth naming up front, because it feeds the first candidate:

> **No script in Part III ever integrates the connection.** Verified by inspection of all
> nine `<!--SCRIPT-->` blocks: none contains the string `Gamma`, `christ`, or `connection`.
> `fig-transp` (3.2), `fig-ptrans` (3.3) and `fig-holo` (3.4) all transport vectors by the
> *extrinsic* trick — chop the path into short great-circle arcs and apply the 3-D rotation
> taking each arc's start to its end. That is legitimate and the captions say so honestly,
> but it works only because a round sphere is embeddable and homogeneous. The object the
> chapter spent seven pages deriving, `Γ^λ_{μν}`, has never once been switched on and made
> to do anything on screen.

---

# Accepted, in build order

---

## 1 · "The two rules you cannot tell apart" — Chapter 3.3, §2

**Build this first.**

### The confusion it dissolves

Chapter 3.3 §2 opens:

> "This section exists to destroy a belief before it forms. The belief is: **if the metric
> components depend on position, the space is curved.** It is false, it is the single most
> common misunderstanding at this stage, **and it will wreck the next two chapters for
> anyone holding it.**"

The `⚠` box that closes §2.2 then asks, in so many words, for exactly this figure:

> "**The sharpest form of the warning is a comparison.** The unit sphere carries
> `ds² = dθ² + sin²θ dφ²` and the flat plane carries `ds² = dr² + r² dθ²`. Both have one
> constant component and one that varies with the other coordinate. One of the two spaces is
> curved and one is not. **Inspection of the components cannot tell them apart**, and
> therefore a genuine test for curvature has to be built."

And the second `⚠`, closing §7:

> "The plane is flat. Its connection coefficients in Cartesian coordinates are zero and in
> polar coordinates are not… **So a non-zero connection is not evidence of curvature**, any
> more than position-dependent metric components were."

Plain terms 3.3.2 restates it a third time: *"no amount of staring at the two rules will
tell you which is which."* Three separate passages in one chapter, and the one thing none of
them can do on the page is show the reader the two rules failing to differ and the two
outcomes differing anyway.

### Why a static figure cannot do it

A static figure can show one loop on the plane and one loop on the sphere with the arrows
drawn — and a reader who has just been told the plane is a trap will assume the loop was
chosen to make the point. The claim is not *"here is a loop where nothing happens."* It is
*"here is a space where nothing happens at any loop you can construct, while the components
and the connection coefficients are churning the whole time."* Universality over a family is
what the reader has to be convinced of, and the only cheap way to convince someone of a
universal claim is to hand them the dial and let them fail to break it. The three existing
transport figures already establish this idiom in the book — 3.3's *make the path a
geodesic*, 3.4's *halve the loop* — and both are there for exactly this reason.

There is a second thing a static figure cannot do at all. On the plane the *components*
`V^r, V^θ` swing violently around the loop while the *arrow* does not move by a part in
`10^12`. Seeing those two facts as one event, with a common cause, is the whole lesson, and
it is an animation of a single object, not two pictures.

### What is computed

Two panels, two metrics, one integrator.

- Left: the Euclidean plane in polar coordinates, `g = diag(1, r²)`, with the connection the
  chapter derives in §7.8 — `Γ^r_{θθ} = −r`, `Γ^θ_{rθ} = Γ^θ_{θr} = 1/r`, everything else
  zero.
- Right: the unit sphere, `g = diag(1, sin²θ)`, with `Γ^θ_{φφ} = −sinθ cosθ`,
  `Γ^φ_{θφ} = Γ^φ_{φθ} = cotθ`.

The same routine runs on both: integrate the parallel-transport equation of §6,

```
dV^μ/dλ  =  −Γ^μ_{νρ}(x) V^ν (dx^ρ/dλ),
```

by RK2/RK4 along a **closed rectangle in coordinate space** — out in the first coordinate,
round in the second, back, and round again. Nothing about the sphere's embedding is used;
nothing but the two coordinates and the two Christoffel formulas enters. Held fixed: the
metrics, the starting vector. Varying: the rectangle's four corners (two sliders per panel,
or one drag on each), which is the whole family of loops.

Plotted: the transported arrow at ~14 stations round each loop, drawn to scale in the metric
of its own space; the departure and arrival arrows superposed at the base point; and three
readouts —

1. the vector's length at start and end, to fourteen places (metric compatibility, true on
   **both**, so it is not the discriminator);
2. the live components `V^r, V^θ` (resp. `V^θ, V^φ`) at the marker, and — on the plane
   only — the same vector's Cartesian components;
3. the closing angle, against `enclosed area / a²` on the sphere and against zero on the
   plane.

Verified numerically (`checkA.py`, `checkA2.py`):

| space | loop | length drift | closing angle | enclosed area |
|---|---|---|---|---|
| polar plane | `r∈[1.0,2.5], θ∈[0.3,1.4]` | `3×10⁻⁹` | `1.2×10⁻⁶°` | — |
| polar plane | `r∈[0.4,3.0], θ∈[0.0,2.6]` | `1×10⁻⁷` | `7.8×10⁻⁶°` | — |
| unit sphere | `θ∈[0.7,1.3], φ∈[0.0,0.9]` | `2×10⁻¹⁰` | `25.646108°` | `25.646108°` |
| unit sphere | `θ∈[0.5,1.5], φ∈[0.0,2.0]` | `6×10⁻¹⁰` | `92.457670°` | `92.457668°` |

The plane's residuals are integrator round-off and shrink with step size, exactly as 1.4's
figure reports its `3×10⁻¹³`. The sphere's angle is the enclosed area to six figures at every
setting.

**On overlap, honestly.** The right-hand panel does reproduce what `fig-holo` in 3.4 already
establishes — holonomy equals enclosed area. That is deliberate and it is the *control*, not
the content: the reader is being shown two spaces treated identically by one piece of code so
that the difference in outcome cannot be blamed on the treatment. It also arrives a chapter
earlier than `fig-holo`, so it is a forward-pointer rather than a repetition, and the two
figures compute it by different means — this one from `Γ`, `fig-holo` from the extrinsic
rotation. If the overlap still reads as too much, the sphere panel can be reduced to the
closing-angle readout with no arrows, and the figure loses very little.

And the component trace on the plane, one loop, every 1000 steps:

```
 r=1.00 θ=0.300   V^r=+0.6000  V^θ=+0.2500  |  Cartesian (+0.499322,+0.416146)
 r=2.50 θ=0.300   V^r=+0.6000  V^θ=+0.1000  |  Cartesian (+0.499322,+0.416146)
 r=2.50 θ=1.400   V^r=+0.4950  V^θ=−0.1685  |  Cartesian (+0.499322,+0.416146)
 r=1.00 θ=1.400   V^r=+0.4950  V^θ=−0.4213  |  Cartesian (+0.499322,+0.416146)
 r=1.00 θ=0.300   V^r=+0.6000  V^θ=+0.2500  |  Cartesian (+0.499322,+0.416146)
```

`V^θ` runs from `+0.25` through `+0.10` to `−0.42` and back. The arrow does not move in the
sixth decimal place.

### The controls

- **Two sliders per panel** setting the coordinate rectangle (`r₁,r₂` / `θ₁,θ₂` on the left;
  `θ₁,θ₂` / `φ₁,φ₂` on the right), plus a marker slider that walks a dot round both loops
  together.
- A button, **"shrink both loops"**, halving each rectangle — the sphere's angle falls by
  four, the plane's stays at zero.
- A button, **"show the connection at the marker"**, printing the four non-zero `Γ`
  components live on both sides.

What to watch while dragging the marker: the two numbers in readout 2 on the left panel — the
polar components thrashing, the Cartesian pair frozen — and readout 3 on both panels.

### The moment of insight

**The reader walks the marker round the plane, watches `V^θ` swing from `+0.25` to `−0.42`
and back with the Christoffel symbols visibly non-zero the whole way, and the arrow on screen
never moves at all.**

### Cost

**Roughly 240–280 lines**, at the upper end of the house range (existing Part III scripts run
135–235). Breakdown: general Christoffel-driven transport integrator, new, ~35 lines; two
`christ(x)` functions, ~12; coordinate-rectangle path builder, ~15; the sphere panel's
hand-rolled orthographic projection, ~60 — but this is **copied wholesale** from `fig-ptrans`
in 3.3, which already sits in the same file (`CAM/EX/EY`, `proj`, `front`, `drawPolyline`,
`drawVec`); the plane panel is plain 2-D and needs none of it. Side-by-side panels on one
canvas: the `cx`-offset idiom from `fig-kill` in 3.5. Readouts and controls, ~60.

**Nothing is missing from `NMT.Plot`.** `path`, `seg`, `dot`, `text` and `NMT.css` cover it;
the arrowhead helper is eight lines and every Part III figure already carries its own copy.
The 3-D cost warning in the brief does not bite here: only one of the two panels is spherical,
the projection code exists and is proven in this exact file, and the sphere is drawn from the
outside purely as scenery — the physics is computed in `(θ,φ)` and never leaves the chart.

**Risk to flag:** the plane panel must be drawn in *Cartesian* space with the polar grid
overlaid, not in `(r,θ)` space. Drawing it in `(r,θ)` would make the arrow appear to rotate
and would teach the opposite of the lesson.

---

## 2 · "Where the missing half was" — Chapter 3.8, §4

### The confusion it dissolves

This is the book's most explicitly registered debt. Chapter 3.1's `⚠` box:

> "**⚠ This answer is wrong, by a factor of exactly two.** … Our estimate is short by a factor
> of `2.000`. This is not a rounding error, an arithmetic slip, or a subtlety about which
> radius to use. It is a structural failure of the argument, it was Einstein's own published
> prediction in 1911… **We record it here as a debt, payable in Chapter 3.8.**"

3.8 §4 opens by naming itself as the collection point — *"This is the section Chapter 3.1 §7.3
named in writing"* — and `MATHPLAN-3.7-3.9.md` item 8 calls it "**The chapter's central
payoff**". The sentence the whole apparatus exists to deliver is:

> "A massive slow particle spends its 'motion' almost entirely in the time direction and
> barely notices the spatial curvature; light divides its motion equally, and gets both
> halves."

§4.4 then turns that into `α_space/α_time = v²/c²` and a four-row table running from Mercury
(`3.9×10⁻⁸`) to light (`1`). The table is the tell: the author reached for a *sweep* and the
page could only give him four rows of it.

### Why a static figure cannot do it

A static figure can draw three rays past a mass — time-only, space-only, full — and show the
first two being equal for light. That is the *conclusion*, drawn once, at one speed, and a
reader is entitled to suspect it of being a coincidence at that speed. The content of §4.4 is
not "they are equal for light"; it is "**they are equal only for light**, and the reason is
that the ratio is `v²/c²`". That is a statement about a function of `v` over four decades, and
the table is what a static medium does when it wants that and cannot have it.

There is also a specific thing worth being honest about: the two curves `α_time(v)` and
`α_space(v)` do something a static plot renders as a fact and an interactive renders as a
surprise — `α_space` is *flat*. It does not depend on `v` at all. A reader dragging the slider
and watching one curve slide while the other sits still learns why the ratio is what it is;
a reader shown both curves at once reads a graph.

### What is computed

Three integrations of the orbit equation of §3.1, differing only in their source term, all
started on the incoming asymptote `u = 0`, `du/dφ = 1/b`:

```
time-only    u'' + u =  GM/(v²b²)
space-only   u'' + u = −GM/(c²b²) + 3GM u²/c²
full         u'' + u =  GM/(v²b²) − GM/(c²b²) + 3GM u²/c²
```

RK4 in `φ` until `u` returns to zero; the crossing angle minus `π` is the deflection. Nothing
is read off a formula. The three closed forms — `2GM/v²b`, `2GM/c²b`, and their sum — are
overlaid as dashed guides so the figure **checks** §4.2–§4.4 rather than illustrating them,
which is the pattern `fig-veff` and `fig-holo` already use.

Held fixed: `M` (the Sun) and `b` (the solar limb, `6.957×10⁸ m`). Varying: `v/c` on a
logarithmic slider from `0.01` to `1`.

Main panel: `α_time` and `α_space`, both computed, against `v/c`, on log–log axes, in units of
`2GM/c²b` so the numbers are `c²/v²` and `1`. Inset panel: the three ray paths at the current
`v`, with the transverse scale magnified by a stated factor (declared in the caption, as
2.6's drift speed and 3.7's unit convention already are).

Verified numerically (`checkB.py`, `GM = c = 1`, `b = 2000`):

| `v/c` | `α_time` integrated | `2GM/v²b` | `α_space` integrated | `2GM/c²b` | ratio | `v²/c²` |
|---|---|---|---|---|---|---|
| `1.000` | `9.99999×10⁻⁴` | `1.0×10⁻³` | `1.00059×10⁻³` | `1.0×10⁻³` | `1.001` | `1.000` |
| `0.500` | `3.99999×10⁻³` | `4.0×10⁻³` | `1.00059×10⁻³` | `1.0×10⁻³` | `0.2501` | `0.2500` |
| `0.100` | `9.99168×10⁻²` | `1.0×10⁻¹` | `1.00059×10⁻³` | `1.0×10⁻³` | `0.01001` | `0.0100` |

and at `v = c` the two integrated halves sum to `2.00059×10⁻³` against `4GM/c²b = 2.0×10⁻³` —
the residual is the second-order term in `GM/c²b`, so it grows as `b` is brought in towards
the mass and dies away as `b` is pushed out. That is worth a readout of its own: it is the
figure showing the reader the exact sense in which "the two halves add" is a first-order
statement.

### The controls

- **`v/c` on a log slider**, `0.01` → `1`, with preset buttons **Mercury**, **a 10 MeV
  electron**, **light** — the three interesting rows of §4.4's table.
- **`b` on a slider** in units of `R_⊙`, whose only job is to let the reader watch the
  first-order residual grow as `b` shrinks and confirm that the split is a first-order
  statement.

What to watch: the `α_space` curve, which does not move when `v` does.

### The moment of insight

**The reader drags `v` upward and watches `α_time` fall towards `α_space` — which has not
moved once — until at exactly `v = c` the two curves cross, and the factor of two is standing
there as the point where a falling line meets a flat one.**

### Cost

**Roughly 200–230 lines.** RK4 on a second-order ODE, ~25; asymptote crossing by linear
interpolation on the sign change, ~10 (`fig-veff`'s `extrema()` is the established pattern for
this kind of bracketing); `u(φ) → (x,y)` conversion for the inset rays, ~15; two panels, ~70;
readouts and presets, ~60. `NMT.Plot` needs nothing new — log axes are handled the way `fig-at`
in 3.9 handles them, by plotting `log10` of the quantity and labelling the axis accordingly.

**Risk to flag:** below about `v = 0.01c` the deflection stops being small and first-order
perturbation theory fails (at `v = 0.001c`, `α_time` comes out at `4.2` radians). The slider
must stop at `0.01`, and the caption should say why rather than leaving a reader to discover a
regime the figure is silently lying about. Mercury's actual `1.6×10⁻⁴ c` is off the left edge;
the **Mercury** preset should therefore report the ratio from the formula and say that the
integration is not being run there, which is more honest than extending the axis.

---

## 3 · "Which small parameter is doing the work" — Chapter 3.7, §8

### The confusion it dissolves

§8.3 stops mid-derivation to warn about its own approximation, and the warning is unusual
because it says the *obvious* justification is wrong:

> "The term in `w²` is dropped, and this is the only approximation in the section — **but be
> careful about why it is safe, because the obvious reason is the wrong one.** The obvious
> reason would be that `w/u_c`, the fractional variation of `1/r` around the orbit, is small;
> for Mercury that quantity is the eccentricity `e = 0.206`, **which is not small at all**, and
> a 20% error in `Δφ` would be four arcseconds per century, a hundred times the precision §8.5
> claims."

The §8.4 `⚑` box makes the same kind of argument again for `L² = GMp`. So the reader is asked,
twice in one section, to accept an approximation on grounds that are not the ones their
instincts supply, and then to trust the result against a measurement good to one part in a
thousand. That is a lot of trust with nothing to check it against.

### Why a static figure cannot do it

A static figure could be a contour plot of `|measured − formula|` over the `(e, GM/c²p)` plane,
and it would carry the arithmetic. What it would not carry is the collision between what the
orbit *looks* like and what the number *says*. The persuasive event here is that the reader
pushes the eccentricity to `0.9`, the trajectory on screen becomes a violent rosette that
looks like nothing the word "perturbation" should be allowed near, and the agreement in the
readout below does not budge. Then they nudge the *other* dial by a hair and it collapses. Two
dials, opposite behaviours, one of them counter-intuitive — that is a comparison that has to
be made by hand, and the contour plot is precisely the thing that hides the surprise by making
both axes look alike.

It is also the chapter's only chance to draw an orbit at all. **Part III never draws a
trajectory.** `fig-veff` plots the potential that governs one and stops there.

### What is computed

The full **nonlinear** orbit equation of §8.1, integrated by RK4 with no linearisation
anywhere:

```
d²u/dφ² + u = GM/L² + 3GM u²/c²,     started at perihelion, u = (1+e)/p, du/dφ = 0
```

Perihelia are located by bracketing the sign change of `du/dφ` and interpolating; the measured
advance is the perihelion-to-perihelion angle minus `2π`, averaged over three orbits.

Three quantities are then compared, in the two-error idiom `fig-tide` established in 3.1:

- **measured** — from the nonlinear integration;
- **linearised-exact** — `2π/ω − 2π` with `ω² = 1 − 6GM u_c/c²` and `u_c` the *exact* root of
  §8.3 step 1. The gap to the measured value is **error 1: the price of dropping `w²`**.
- **the printed formula** — `6πGM/c²p`. The gap from linearised-exact is **error 2: the price
  of the binomial expansion of §8.4 together with `L² = GMp`.**

Held fixed: `GM`. Varying: `e` and `GM/c²p`, one slider each.

Verified numerically (`checkC.py`, `checkC2.py`):

| `GM/c²p` | `e` | error 1 (`w²` dropped) | error 2 (binomial + `L²=GMp`) |
|---|---|---|---|
| `1.0×10⁻⁴` | `0.20` | `5.0×10⁻⁶` | `7.56×10⁻⁴` |
| `1.0×10⁻⁴` | `0.60` | `4.5×10⁻⁵` | `7.96×10⁻⁴` |
| `1.0×10⁻⁴` | `0.90` | `1.0×10⁻⁴` | `8.52×10⁻⁴` |
| `1.0×10⁻³` | `0.20` | `4.9×10⁻⁵` | `7.62×10⁻³` |
| `5.0×10⁻³` | `0.20` | `2.2×10⁻⁴` | `3.95×10⁻²` |
| `1.7×10⁻²` | `0.20` | `5.0×10⁻⁴` | `1.48×10⁻¹` |

Read the table twice. **Down the eccentricity**: error 2 barely notices `e` at all —
`7.56 → 7.96 → 8.52` in units of `10⁻⁴` while `e` more than quadruples. **Down the relativistic
parameter**: both errors scale straight off it, error 2 by a factor of ten per decade.

And the thing the book states but never weighs: at Mercury's eccentricity the approximation
everyone is invited to worry about, dropping `w²`, costs **about 150 times less** than the
binomial expansion nobody worries about. That is not a correction to the chapter — §8.4 flags
its binomial step openly and bounds the small parameter at `1.6×10⁻⁷` — it is a comparison the
page has no room to make.

### The controls

- **eccentricity `e`**, `0.05` → `0.95`.
- **`GM/c²p`** on a log slider, `10⁻⁵` → `2×10⁻²`, with a **Mercury** preset
  (`GM/c²p = 2.7×10⁻⁸`, off the low end, reported from the formula) and a **strong field**
  preset near the ISCO.
- **orbits drawn**, 1 → 6, so the rosette can be built up or cleared.

What to watch: the two error readouts, and specifically which of them moves when `e` moves.

### The moment of insight

**The reader pushes eccentricity from `0.2` to `0.9`, the orbit on screen turns into a
star-shaped rosette that looks nothing like a perturbed ellipse, and the dominant error
readout underneath moves in the fourth significant figure.**

### Cost

**Roughly 190–220 lines.** RK4 on the orbit ODE, ~25; perihelion bracketing and averaging,
~30; `u(φ) → (x,y)` for the rosette, ~10; a second small panel showing `Δφ` per orbit against
`GM/c²p` with the measured points and the `6πGM/c²p` line, ~50; readouts, ~50. `NMT.Plot`
needs nothing new.

Note that this shares its whole integrator with candidate 2 — build either one and the other
is roughly 60 lines cheaper.

**A free collection.** Chapter 3.5 §9's promise ("Killing ⇒ conserved quantity along
geodesics") is spent in 3.7 §5 and never shown. Printing `E` and `L` along the integrated
orbit, flat to twelve places, costs four lines here and pays that debt in passing. It is not
a reason to build the figure, but it should not be left on the floor.

---

# Rejected, and why

Listed roughly in descending order of how nearly they made it.

### 1. "`r` is not the distance to the centre" — 3.7 §2. *The closest miss.*

The `⚠` box behind it is the strongest single difficulty marker in Part III: *"The definition
is a choice… and it is **the single most misread line in this subject**. `r` is not the
distance to the centre."* Nothing in Part III shows it. The figure would integrate
`∫√B dr = ∫dr/√(1−r_s/r)` and lay proper-length rulers inward, watching the coordinate labels
bunch up.

**Rejected on test 1.** The whole content is one monotone curve — proper distance against
areal radius, with the identity line for comparison — and a well-drawn static version of that
curve carries it completely. The one genuinely change-shaped fact underneath (the integrand
diverges at `r_s` while the integral converges, because the divergence is
`(r−r_s)^{−1/2}`) is a readout, not a figure. Worth a static figure if one is ever wanted;
not worth an interactive.

### 2. The FLRW light cone in proper distance — 3.9 §5.3.

Genuinely fine physics, well documented (§5.3 *"a consequence that stops people"*; worked
example 2(e) *"why can we nonetheless see things beyond it?"*), and completely uncovered by
`fig-at`. The photon we receive from `z = 3` spent its first few billion years moving *away*
from us in proper distance before turning round.

**Rejected on test 1.** This diagram is published in the literature as a static figure,
because static is what it needs — the turn-around is visible in a single printed curve. The
one thing the slider would add (drag `Ω_Λ` and watch an event horizon appear, so that a
matter-only universe eventually shows you everything and ours does not) is real and is
secondary; it would be a garnish on a figure whose point was already made before anyone
touched anything.

### 3. Geodesic deviation and conjugate points — 3.4 §4.

Two nearby geodesics with the separation measured directly and compared against
`D²ξ/dτ² = −R^μ_{νρσ}u^ν ξ^ρ u^σ`, with curvature on a slider: converging and crossing at
`K > 0`, parallel at `K = 0`, diverging at `K < 0`.

**Rejected on tests 3 and 4.** Chapter 3.4's only two warn boxes are `⚑` provenance flags
(Weyl; the converse of "flat ⟺ Riemann vanishes"); there is no documented difficulty here,
only a documented *importance* ("where Part III's thesis lands"). And 3.1's `fig-tide` already
shows the deviating ellipse computed three independent ways, so the new content would be the
identification rather than the phenomenon — which is a sentence, and the chapter already
writes it.

### 4. The commutator `[X,Y]` as a failure to close — 3.2 §8.

Flow `ε` along `X` then `Y`, then the other order; the gap is `ε²[X,Y] + O(ε³)`; shrink `ε`
and watch `gap/ε²` converge.

**Rejected on tests 3 and 4.** Chapter 3.2's warn boxes are about the 0.7 cheque (covered by
`fig-transp`) and about *why almost nothing needs rebuilding* — neither is this. And the
"shrink it and watch the ratio hold" move is already the *halve the loop* button in 3.4's
`fig-holo`; doing it twice in one part spends the surprise.

### 5. Killing vectors buying conserved quantities — 3.5 §9.

**Rejected on test 4**, and folded into candidate 3 instead, where it costs four lines. A
figure whose entire content is "two readouts stay flat" is a readout.

### 6. Gauge freedom in the field equations — 3.6 §7.

Apply an arbitrary coordinate change to a solution; watch all ten `g_{μν}` churn while a
curvature invariant sits still. Ten equations, four identities, six independent, four
coordinate freedoms.

**Rejected on test 3 and on cost.** Chapter 3.6's three `⚠` boxes are the derivative-ordering
ambiguity and two sign traps; none of them is this. And the cost is real — computing a
curvature invariant numerically from a general metric means second differences of a
four-metric, which is a different order of expense from anything else here.

### 7. The size of a local inertial frame — 3.1 §5.

Permitted laboratory size against measurement precision. **Rejected on test 1**: it is the
plot of a closed-form inequality, and dragging the precision slides a curve along itself.

### 8. Riemann's twenty independent components — 3.4 §5.

A live `4×4×4×4` array with the symmetries knocking entries out until twenty remain.
**Rejected on test 5.** It would be a satisfying thing to click and would teach an index
convention, not a fact about the world. This is the decoration the standing rule exists to
keep out.

---

## One observation outside the brief

`fig-press` in 3.6 is the weakest figure in Part III by a distance. What it draws is
`1 + 3w`, a straight line, plus a ball with arrows whose length is `|1+3w|` — an illustration
of a claim rather than a result computed from the physics, which is the one thing every other
figure in the part scrupulously is, and says it is. Its *subject* is right (§6's "the one term
the argument cannot exclude" is the correct target), so the answer is not another figure in
3.6. If 3.6 is ever revisited, the repair is to make that figure compute something — the
simplest honest version being to integrate a test particle's radial geodesic deviation in the
weak field of a uniform lump of fluid with equation of state `w`, so that the arrow lengths
are an output rather than an input. That is a separate piece of work and is noted here only
so it is not lost.
