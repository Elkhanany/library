# Mathematics review — Chapter 4.7, *Wells, Barriers, and Tunnelling*

Independent re-derivation of `src/ch4-7.html` (≈21,300 words of prose, 2,435 lines including the
figure scripts). Every algebraic result below was derived from scratch — in `sympy` where it could be,
by hand and then checked in `mpmath` at 40 digits where it could not — before the page was consulted.
Every printed number was recomputed. The finite-well spectrum was additionally checked by a
tridiagonal finite-difference diagonalisation that shares no algebra with the transcendental
condition, and the barrier transmission by an independent Python port of the figure's Runge–Kutta
integrator.

**Counts: 2 BLOCKER, 4 MAJOR, 15 MINOR.**

Scratch work: `/tmp/mathrev/c1.py … c20.py`. Nothing in the repository was edited.

---

## What came out clean

These are recorded because the brief asked for them specifically and because a reviewer who reports
only defects has not told you where the chapter is load-bearing.

* **§1.3's derivation of the matching conditions is valid.** `Ĥu ∈ L²` with `V` bounded forces
  `u'' ∈ L²_loc`; the display `u'(x) = u'(x₀−ε) + ∫f` plus `|∫_I f| ≤ ‖f‖√|I|` gives continuity of
  `u'`, hence of `u`. The delta-language restatement is the same statement and is correct.
* **§5.4–§5.5.** The cross terms in `u*u'` cancel exactly as claimed
  (`ik(z̄ − z)` is real, so contributes nothing to `Im`). `T + R = 1` verified **symbolically** for
  the step with `E > V₀` (sympy: `T+R−1 → 0` identically) and for the rectangular barrier from a full
  4×4 solve of the matching conditions (`T+R−1 → 0`). The `k′/k` factor is used, not `|t|²`, and
  §5.5's warn box gives the correct reason with correct numbers.
* **§6.2 / e-baramp.** Solving all four matching conditions in sympy and subtracting the chapter's
  `1/t = e^{ikw}[cosh κw + (i/2)(κ/k − k/κ) sinh κw]` gives exactly zero. Every line of the grind box
  checks, including `(1 + ik/κ)(1 − iκ/k) = 2 + iΣ` and `1 + Σ²/4 = (k²+κ²)²/4k²κ²`.
* **§4.2–§4.4.** Both transcendental conditions re-derived independently and agree. The
  dimensionless parametrisation is right (`z² + y² = z₀²`, `tan z = y/z`, `−cot z = y/z`). The
  bound-state count `N = ⌈2z₀/π⌉` is correct including the exact-threshold case (where the new state
  sits at `κ = 0` and is correctly *not* counted). The "at least one, always" argument is a valid
  intermediate-value argument. The 3D threshold `V₀a² > π²ħ²/8m` is right.
* **§4.6, the delta well.** The limit is right, including the trap: `z² = √(z₀²−z²)` gives
  `z² = z₀² − z₀⁴ + O(z₀⁶)`, so `κa = z² → z₀² = maλ/ħ²` and `E = −mλ²/2ħ²`. The second route
  (integrating across the origin) and the jump condition `Δu′ = −2mλu(0)/ħ²` both check.
* **§2.** `Π̂² = Î ⇒ λ = ±1`, the even/odd splitting, `[Π̂,Ĥ] = 0 ⟺ V` even, and the domain remark
  are all correct. **The non-degeneracy theorem is proved, not quoted and not assumed** — the
  Wronskian argument is in §2.4 and Problem 2(a) asks the reader to complete it. (One step of it is
  incomplete; see M3.)
* **§6.5's resonance claim is *not* the plan's false one.** `MATHPLAN-4.md` item 10 says "it is the
  same condition as a bound state of the well, analytically continued". The chapter does not say
  that. It says the resonance `qw = nπ` is the condition for the *interior, walled off* to hold an
  infinite-well level — true — and separately that the **poles of `t` at negative energy are the bound
  states**. I verified the pole condition both ways:
  * continuing `1/t` with `κ_interior = −iq` and `k = iκ` gives `cot(qw) = (q² − κ²)/(2qκ)`, exactly
    the chapter's `e-poles`;
  * with `c = cot(qw/2)` and `X = q/κ`, `(c²−1)/2c = (X²−1)/2X ⟺ (c − X)(Xc + 1) = 0`, i.e. exactly
    the even condition `c = X` or the odd condition `c = −1/X`. "Both parities, with nothing left
    over" is exact, not approximate;
  * numerically, `e-poles` has residual `< 2×10⁻⁴⁰` at both bound states of the quoted well.
  The chapter is therefore honest about the difference: it names the infinite well for the resonance
  and the finite well's bound states for the poles, and never conflates them.
* **The ⚑ budget is met exactly.** One ⚑ in the file (line 1371), and it is the STM / α-decay box.
  No `\dv[2]`, no American `-ize` spellings, no forbidden hedges, no bare `<` in maths.

---

## BLOCKER

### B1 · Worked example 2(b) — the standing-wave displacement is the wrong function of the phase

> "What the shift does is displace the standing-wave pattern on the left: the nodes sit where they
> would for a hard wall placed a distance $\theta/k$ further to the right"

With `r = e^{−2iθ}`, `tan θ = κ/k`, the solution on the left is
`u = A(e^{ikx} + r e^{−ikx}) = 2Ae^{−iθ} cos(kx + θ)`, whose nodes are at `x = (π/2 + nπ − θ)/k`. A
hard wall at `x_w` has nodes at `x_w − nπ/k`. Matching the two node sets gives

```
x_w = (π/2 − θ)/k = arctan(k/κ)/k ,   not  θ/k .
```

The two agree only at `E = V₀/2`, where `θ = π/4`. Everywhere else the chapter's expression is wrong,
and in the limit it is qualitatively wrong in the opposite direction:

| `E/V₀` | `θ` | chapter's `θ/k` | correct `(π/2−θ)/k` | `1/κ` |
|---|---|---|---|---|
| 0.999 | 0.03163 | 0.02238 | **1.08890** | 22.361 |
| 0.900 | 0.32175 | 0.23982 | **0.93098** | 2.2361 |
| 0.500 | 0.78540 | 0.78540 | **0.78540** | 1.0000 |
| 0.100 | 1.24905 | 2.79295 | **0.71946** | 0.74536 |
| 0.010 | 1.47063 | 10.39892 | **0.70829** | 0.71067 |
| 0.001 | 1.53917 | 34.41685 | **0.70722** | 0.70746 |

(units `ħ = m = V₀ = 1`.) As `E → 0` the step becomes a hard wall *at the origin* — `r → −1` exactly,
which the chapter itself says in part (d) — so the displacement must go to **zero**, and the correct
expression does (`(π/2−θ)/k → 1/κ → 0`). The chapter's `θ/k` **diverges** there. As `E → V₀` the wave
penetrates arbitrarily far and the displacement must grow; the correct expression gives `π/2k`,
the chapter's gives `0`. The claim is exactly backwards.

**Should say:** the nodes sit where they would for a hard wall a distance `(π/2 − θ)/k = arctan(k/κ)/k`
to the right of the step — which is the penetration depth `1/κ` at low energy and `π/2k` as the energy
approaches the top. Equivalently: write `r = −e^{2iδ}` with `δ = π/2 − θ` the phase shift measured
from hard-wall reflection, and the displacement is `δ/k`. The sentence that follows ("so the phase is
measurable as a shift in the fringes") survives unchanged.

### B2 · Worked example 3(b) — the order of the delta-limit correction is stated backwards

> "The approach is slow because the correction is of order $\kappa w$ rather than $(\kappa w)^{2}$"

Expanding the exact `1/T` at fixed `λ = V₀w` (sympy, `series` in `w`):

```
1/T = 1 + β² + β²(κw)²/3 + O(w²),      β² = mλ²/2Eħ² ,   (κw)² = 2mλw/ħ² .
```

The relative correction is **exactly of order `(κw)²`**, which is *first* order in the width `w`, not
of order `κw ∝ √w`. The chapter's own three numbers refute its sentence: taking `λ = 1 eV·nm` and
`E = 0.5 eV`, the shortfall `1 − T/T_δ` is

| `w` /nm | `κw` | `T` | `1 − T/T_δ` |
|---|---|---|---|
| 0.1 | 1.5791 | 3.4036e−2 | 0.5193 |
| 0.05 | 1.1312 | 4.8151e−2 | 0.3199 |
| 0.02 | 0.7209 | 6.0385e−2 | 0.1472 |
| 0.01 | 0.5110 | 6.5332e−2 | 0.0773 |
| 0.005 | 0.3618 | 6.7999e−2 | 0.0396 |
| 0.001 | 0.1620 | 7.0232e−2 | 0.0081 |

Halving `w` halves the error (0.1472 → 0.0773 → 0.0396), i.e. the error is linear in `w`. `κw` only
falls by `√2` across the same step, so the error cannot be `O(κw)`.

**Should say:** the correction is of relative order `(κw)²/3 = mλw/3ħ²`, which is *first* order in the
width — the delta is approached only linearly in `w`, not quadratically, which is why three
successive halvings still leave 8% at `w = 0.001 nm`. (The three printed transmissions themselves are
correct — see the table at the end.)

---

## MAJOR

### M1 · §1.6 — the self-adjointness sweep does not cover the delta well, and says it does

> "Every potential in §§4 to 6 is a bounded step function, so every one of them is covered by that
> sentence."

§4.6's `V(x) = −λδ(x)` lives inside §4 and is not a bounded step function; nor is Worked example 3's
`+λδ(x)`, nor Worked example 1's pair of deltas. §1.6 opens by setting the chapter's own standard —
*"no general theorem is quoted for the self-adjointness of `p̂²/2m + V`, and each case is checked
where it arises. There are two cases in this chapter and both are short."* — and there are three.
The delta Hamiltonian's self-adjointness is never checked; §4.6 substitutes an appeal
("sitting inside the same classification Chapter 4.4 §6 counted"), which is a count of extensions,
not a verification that this particular one is self-adjoint.

The result is true, and the check is genuinely short (the boundary form on `ℝ∖{0}` is
`[ū v′ − ū′ v]` across the origin; imposing `u` continuous and `Δu′ = −(2mλ/ħ²)u(0)` on both members
makes it vanish, and the adjoint's domain closes because `v(0)` and `Δv′` cannot be varied
independently once the jump condition is imposed). What is needed is the check, plus a corrected
sentence naming three cases rather than two.

### M2 · §4.4 — the two-dimensional claim is an unflagged import

> "Two dimensions sits between the two and always binds, for a reason that is not visible from this
> argument."

This is a real theorem (weak-coupling binding in 2D for `∫V ≤ 0`), it is used to make the
one-dimension/three-dimension contrast land, and it is neither derived nor flagged. The chapter's own
Conventions paragraph says *"One result is quoted rather than derived, and it is experimental… There
are no others."* That sentence is false while this claim stands unmarked.

The same over-reach appears once more in a plainer form: plain-terms box 4.7.4 says *"a
one-dimensional attraction always traps something"*, where §4.4 proved it only for the square well.
The general 1D statement is also a theorem, also true, also underived.

**Options:** (a) delete the 2D sentence and the generalised 1D one, keeping the square-well results
the chapter actually proves; (b) raise a second ⚑ — but the chapter's stated budget is one, so (a) is
the cheaper repair. Do not leave both as they stand.

### M3 · §2.4 — the Wronskian argument fails exactly at the nodes

> "Setting $W=0$ says $u_{2}'/u_{2}=u_{1}'/u_{1}$ wherever the functions are non-zero, so their ratio
> has zero derivative and $u_{2}$ is a multiple of $u_{1}$."

`d/dx (u₂/u₁) = −W/u₁²` is only defined where `u₁ ≠ 0`. What the argument establishes is that `u₂` is
a constant multiple of `u₁` **on each interval between zeros of `u₁`** — with, so far as the argument
goes, a different constant on each. Every excited bound state of the finite well has interior nodes,
so this is not a pathological case; it is the generic one for the states §4.5 tabulates.

The missing step is one sentence: at a zero `x₀` of `u₁`, `W = 0` gives `u₁′(x₀)u₂(x₀) = 0`, and
`u₁′(x₀) ≠ 0` because `(u₁,u₁′)` cannot both vanish (uniqueness for the initial-value problem), so
`u₂(x₀) = 0` too; L'Hôpital then gives `u₂/u₁ → u₂′(x₀)/u₁′(x₀)` from both sides, so the constant is
the same across the node. Problem 2(a) repeats the same shortcut and needs the same sentence.

### M4 · §5.2 — the wave-packet statement is asserted, and its citation does not support it

> "Chapter 4.6 §10 supplies the physical picture underneath. Build a genuine normalised packet out of
> these solutions… and the probability of finding the particle on the far side tends to the number
> computed below."

This is the statement that the stationary-state flux ratio equals the asymptotic transmission
probability of a normalised packet — the thing that makes the whole of §§5–6 mean anything physical.
It is a theorem of scattering theory and it is not proved here. The cited support, `ch4-6` §10, is
"A free packet: group velocity, and spreading"; it treats `V = 0` only and contains no scattering off
a step (I read it). So the citation carries no weight and the claim stands bare.

The chapter's logical chain does not actually rest on this — the legitimacy argument in the preceding
sentences is Chapter 4.5 §7.4's ratio procedure, which is fine — so the cheapest repair is to demote
the sentence to what it is (a statement of what the ratio is *for*, whose proof is not in this book)
rather than a result, or to say plainly that the packet calculation is not done here.

---

## MINOR

**m1 · §3.5, a digit.** `Δx = 0.180757 L`. Exact value `√(3π²−18)/(6π) = 0.180756027596…`, so the
sixth decimal should be **6**, not 7. (`ΔxΔp = 0.567862 ħ` is right: `0.5678618084`.)

**m2 · Worked example 1(c), an over-claim.** "at $qb=5$ they agree to seven figures". Exact splitting
`9.07998857e−5`; formula `4|E₀|e^{−2qb} = 9.07998595e−5`. Relative difference `2.886×10⁻⁷` — they
agree to **six** figures and differ in the seventh.

**m3 · Brick, an over-claim.** "a well $3\ \mathrm{eV}$ deep and $0.6\ \mathrm{nm}$ wide demonstrates
it to nine figures". §6.5 prints seven significant figures (`−2.457819`) and six (`−0.985835`).
"Seven" is what the page shows.

**m4 · §1.5, two stale internal pointers.** "Section 3.1 does this limit with the numbers in hand,
and §4.5 checks it against the exact finite-well levels." §3.1 does no limit (it sets up the Dirichlet
operator and points *back* to §1.5, so the pair is circular), and §4.5 tabulates finite-well levels
without comparing them to the infinite well. The limit with numbers is **Worked example 2(d)**; the
check against the exact finite-well levels is **Problem 3(b)**. This matters more than an ordinary
stale citation because §1.5 asserts the rate ("the value falls like `1/κ`") and defers its
justification to these two addresses.

**m5 · §1.3, a mis-aimed citation.** "in the form Chapter 4.4 §5.3 used twice". `ch4-4` §5.3's two
uses of Cauchy–Schwarz are of the form *"a product of two `L²` functions is `L¹`"*. The form used here
— `|∫_I f| ≤ ‖f‖ √|I|` — is the one stated at `ch4-4` §5.2 ("`L²` functions are integrable on bounded
subintervals by Cauchy–Schwarz").

**m6 · §4.3, the count argument omits the truncated branch.** "each one that begins below `z₀` climbs
to infinity while the falling curve stays finite, so each contributes exactly one crossing." True for
branches lying wholly below `z₀`; the last branch is cut off at `z = z₀`, where the rising curve has
*not* climbed to infinity. There is still exactly one crossing there (the falling curve reaches zero
at `z₀` while `tan z > 0`, and the difference is strictly monotone), and §4.4 gives that argument —
but only for the first branch. One clause in §4.3 closes the boxed formula's proof.

**m7 · §3.1–§3.2 never exclude `E ≤ 0`.** §3.1 writes `u = A sin kx + B cos kx` with
`k = √(2mE)/ħ` and says "the oscillating case for every positive `E`", without saying that `E ≤ 0` is
being set aside. At `E = 0` that basis degenerates (the true solution space is `{1, x}`), and `E < 0`
is not considered at all. Both are empty under Dirichlet, and §3.6's completeness argument closes the
spectrum retroactively, so no printed result is wrong — but the sentence "so the levels are the
squares of the positive integers" is one step ahead of its derivation at the point it is made.

**m8 · §4.4, the radial reduction is the `ℓ = 0` case and does not say so.** "Chapter 4.13 reduces a
spherically symmetric problem to a radial equation of exactly the form (e-tise1d) for the function
`u(r) = rR(r)`, with one extra requirement: `u(0)=0`." That is the s-wave; for `ℓ > 0` the radial
equation carries `+ℓ(ℓ+1)ħ²/2mr²` and is *not* of the form of e-tise1d with the same `V`. The
conclusion "a three-dimensional well binds nothing at all unless `z₀ > π/2`" survives, because the
centrifugal term only makes binding harder — but that monotonicity step is not on the page.

**m9 · Figure 1, bottom panel: odd states are not scaled to unit height.**
```js
peak = rs[i].even ? 1 : Math.max(Math.abs(Math.sin(z)), 1e-9);
if (rs[i].even) peak = Math.max(1, Math.abs(Math.cos(z)));
```
Every odd root has `z ≥ π/2`, so `max_{|x|≤1}|sin(zx)| = 1`, but `peak` is set to `|sin z| ≤ 1`. The
drawn amplitude is therefore `0.30/|sin z|` rather than `0.30`. At the **"six states" preset**
(`z₀ = 9`) the second state has `|sin z| = 0.3136`, so it is drawn at **0.957** in `E/V₀` units — it
spans `−1.86 … +0.06`, crosses several neighbouring levels and the well floor at `−1`, and is clipped
by `ymin = −1.22`. `peak` should be `1` for both parities. (The first line's `even` branch is dead
code.) Separately, the caption says "the **normalised** bound states" while the panel's own label says
"each scaled to unit height" — those are different things and the label is the accurate one.

**m10 · Three slider values are not aligned to their `step`, so browsers snap them.**
Range inputs round to the nearest step-aligned value (step base = `min`).
* `fig-fw` `#fw-z`: `min="0.15" step="0.005"`, `value="2.561584"` → snaps to **2.56**. The default no
  longer reproduces §4.5's first table row (`E/V₀ = −0.809075` instead of `−0.809239`).
* `fig-scat` `#sc-e`: `min="0.02" step="0.005"`. The **"on a resonance"** preset sets `1.376` → snaps
  to **1.375**; `T` becomes `0.999991009` and the readout prints `q w / pi = 0.998629` instead of
  ≈1.000000. The **"a well"** preset sets `1.178` → snaps to **1.18**, giving `qw/π = 2.000452`.
  (The true resonances are at `1.376030` and `1.178113 eV`.)
The HTML Standard is explicit here: on a step mismatch "the user agent must round the element's
value to the nearest number for which the element would not suffer from a step mismatch". The grid
contains neither resonance (`1.375`/`1.380` straddle `1.376030`; `1.175`/`1.180` straddle `1.178113`;
`2.560`/`2.565` straddle `2.561584`), so the fix is to make the steps finer — `step="0.001"` on
`#sc-e` and `step="0.001"` (or a `value` of `2.560`) on `#fw-z` — rather than to move the presets.

**m11 · §4.6, a misleading clause.** "With `z₀` small, `z` is smaller still". In fact
`z ≈ z₀(1 − z₀²/2)` — at `z₀ = 0.1` the root is `z = 0.0995`, smaller by half a per cent. The
subsequent algebra is right and depends on `z ≈ z₀`, not on `z ≪ z₀`, so the clause works against the
step it introduces.

**m12 · §6.5, the symbol `κ` changes meaning inside the subsection.** In `e-baramp`, `κ` is the
*interior* decay constant. In `e-poles` two paragraphs later, `κ` is the *exterior* decay constant
(`k = iκ`) and the interior is `q`. Both are decays, so the chapter's stated convention is not
violated, but the reader has to notice the swap unaided; it is worth one clause.

**m13 · `\ann` is used three times.** All three are inside `e-Tbarrier`, which is one display, but
the convention is "one or two per chapter" and the third annotation sits on a second aligned line
(`1/κ = ħ/√(2m(V₀−E))`) that is a definition rather than the headline result.

**m14 · Figure 2 script comment over-claims its own tolerance.** "The two answers agree to about
1e-12." Over a 594-point sweep of the three sliders the worst relative difference between the closed
form and the RK4 integration is `4.6×10⁻¹¹` (at `V₀ = 4 eV`, `w = 2 nm`, `E = 0.02 eV`, where
`T ≈ 1.4×10⁻¹⁹`); typical values are `10⁻¹⁴`–`10⁻¹⁵`. Nothing on the page claims a bound — the
readout prints the actual number — so this is a comment, not a defect in the figure.

**m15 · Plan document, not the chapter.** `PLAN-FORWARD.md` line 359 lists 4.7's dependency as
"the probability current (**4.6** §5)". The current is built in `ch4-6` **§8** (§8.1 statement, §8.2
derivation, §8.3 phase reading, §8.6 "what the current is for"). `MATHPLAN-4.md` items 7 and 8 have it
right. **The chapter's prose is correct throughout** — every one of its citations to §8, §8.3, §8.5,
§8.6 checks out against `ch4-6`. Only `PLAN-FORWARD.md` is stale.

---

## Cross-references spot-checked and correct

`ch4-4` §5.4 (the `p̂_θ` circle), §5.5 (the half-line), §6.2 (the classification, itself a ⚑ in 4.4),
§7.1 (the boundary form `[ū v′ − ū′ v]₀^L`), §7.2 (Dirichlet as one point of the `U(2)`), §7.3 (the
Robin argument the §1.6 proof compresses), §7.4 (different extensions, different spectra), Worked
example 2 (two Dirichlet eigenfunctions demanding incompatible `θ` — matches §3.7's summary exactly).
`ch4-5` §2, §3, §4.3, §7.1, §7.4, §8.2 and Worked example 1 (the free Hamiltonian; the "degeneracy is
a statement about the preimage" reading is quoted accurately). `ch4-6` §4.2, §4.4, §6.3, §6.4 ("one
dimension is exact rather than approximate" — verbatim), §8, §8.3 (`J = ρ∇S/m`; a real function
carries no current; `∫J = ⟨p̂⟩/m`), §8.5, §8.6, §9.1–§9.4, §10.6, Worked example 2, Worked example 3,
Problem 2. `ch4-3` §8 (the Fourier basis is a basis). `ch4-2` §3, §4.3, §10.2 (barrier `0.2504 eV`,
splitting `98.72 μeV`, ratio `2536` — all three match `ch4-2` verbatim). `ch0-9` §5.3, §5.4 ("the step
function has a derivative, and that derivative is `δ`"), §6.4. `ch0-8` §3.1, §3.3. `ch0-5` §8.
`ch0-2` §3.2. `xrefcheck.py` reports no dangling references book-wide.

---

## Every number I reproduced independently

`ħ = 1.054571817×10⁻³⁴ J s`, `m_e = 9.1093837015×10⁻³¹ kg`, `e = 1.602176634×10⁻¹⁹ C`
(the figure script's set; the chapter's rounded display values in `e-barnum` give the same 7 figures).
All computed at `mp.dps = 40` unless noted.

| § | Quantity | Printed | Mine | ✓ |
|---|---|---|---|---|
| 3.4 | `π²ħ²/2m_eL²`, `L=1 nm` | 0.376030 eV | 0.3760301622 | ✓ |
| 3.4 | `E₁,E₂,ΔE` at 1 nm | 0.3760, 1.5041, 1.1281 | 0.376030, 1.504121, 1.128091 | ✓ |
| 3.4 | gap wavelength, 1 nm | 1099 nm | 1099.06 | ✓ |
| 3.4 | `E₁,E₂,ΔE` at 0.5 nm | 1.5041, 6.0165, 4.5124 | 1.504121, 6.016483, 4.512362 | ✓ |
| 3.4 | gap wavelength, 0.5 nm | 274.8 nm | 274.766 | ✓ |
| 3.4 | `E₁,E₂,ΔE` at 0.2 nm | 9.4008, 37.603, 28.202 | 9.400754, 37.60302, 28.20226 | ✓ |
| 3.4 | gap wavelength, 0.2 nm | 43.96 nm | 43.9625 | ✓ |
| 3.5 | `⟨x²⟩` coefficient | `⅓ − 1/2π²` | `⅓ − 1/2π²` (sympy) | ✓ |
| 3.5 | `Δx/L` | **0.180757** | **0.1807560276** | ✗ m1 |
| 3.5 | `ΔxΔp/ħ` | 0.567862 | 0.5678618084 | ✓ |
| 3.5 | ratio to `ħ/2` | 1.1357 | 1.1357236 | ✓ |
| 3.5 | `ħ²/8m(Δx)²` | 3.826 `ħ²/mL²` | 3.8258191 | ✓ |
| 3.5 | true `E₁` | 4.935 `ħ²/mL²` | 4.9348022 | ✓ |
| 3.5 | fraction recovered | 78 % | 77.53 % | ✓ |
| 4.5 | `z₀` at 1, 5, 20 eV | 2.561584, 5.727875, 11.455750 | 2.5615836, 5.7278751, 11.4557502 | ✓ |
| 4.5 | `N` at 1, 5, 20 eV | 2, 4, 8 | 2, 4, 8 | ✓ |
| 4.5 | levels, `V₀=1 eV` | −0.809239, −0.297230 | −0.80923945, −0.29723043 | ✓ |
| 4.5 | levels, `V₀=5 eV` | −4.728196, −3.922604, −2.620794, −0.940658 | −4.7281962, −3.9226041, −2.6207944, −0.9406577 | ✓ |
| 4.5 | levels, `V₀=20 eV` (8) | −19.68206 … −0.865509 | −19.6820609, −18.7299223, −17.1489736, −14.9495835, −12.1501525, −8.7849026, −4.9293991, −0.8655095 | ✓ |
| 4.5 | grid check, worst rel. | 4.6×10⁻¹⁰ | 3.5×10⁻¹⁰ (edge-aligned grid) / 8.3×10⁻¹⁰ (sharp sampling); counts 2/4/8 | ✓ (order) |
| 5.6 | `k′/k` at `ε=`1.01,1.1,2,10 | 0.0995, 0.3015, 0.7071, 0.9487 | 0.0995037, 0.3015113, 0.7071068, 0.9486833 | ✓ |
| 5.6 | `R` | 0.6708, 0.2880, 0.02944, 0.000693 | 0.6707651, 0.2880201, 0.0294373, 0.00069348 | ✓ |
| 5.6 | `T` | 0.3292, 0.7120, 0.97056, 0.999307 | 0.3292349, 0.7119799, 0.9705627, 0.9993065 | ✓ |
| 5.5 warn | `|t|²+|r|²` at `E=2V₀` | 1.402 | 1.4020203 | ✓ |
| 5.5 warn | `|t|²+|r|²` at `E=1.1V₀` | 2.649 | 2.6493903 | ✓ |
| 6.4 | `κ` (0.5 eV, `m_e`) | 3.622626×10⁹ m⁻¹ | 3.6226263×10⁹ | ✓ |
| 6.4 | `1/κ` | 0.2760 nm | 0.2760428 | ✓ |
| 6.4 | `κw` (`w=1 nm`) | 3.6226 | 3.6226263 | ✓ |
| 6.4 | `T` closed form | 2.850147×10⁻³ | 2.8501467×10⁻³ | ✓ |
| 6.4 | `4e^{−2κw}` | 2.854216×10⁻³ | 2.8542156×10⁻³ | ✓ |
| 6.4 | thick-form excess | 0.14 % | 0.14276 % | ✓ |
| 6.4 | `T` to 14 digits | 2.8501467163972×10⁻³ | 2.85014671639722×10⁻³ | ✓ |
| 6.4 | `R` to 14 digits | 9.9714985328360×10⁻¹ | 9.97149853283603×10⁻¹ (`=1−T`) | ✓ |
| 6.4 | width table `κw` | 1.811, 3.623, 5.434, 7.245 | 1.8113131, 3.6226263, 5.4339394, 7.2452526 | ✓ |
| 6.4 | width table `T` | 1.014e−1, 2.850e−3, 7.624e−5, 2.037e−6 | 1.0136213e−1, 2.8501467e−3, 7.6240128e−5, 2.0366346e−6 | ✓ |
| 6.4 | factor per 0.5 nm | 35.6, 37.4, 37.4 | 35.564, 37.384, 37.434 | ✓ |
| 6.4 | `e^{2κ·0.5nm}` | 37.44 | 37.4358 | ✓ |
| 6.4 | ammonia ratio | 2536 | 2536.3 | ✓ |
| 6.4 ⚑ | `κ` (4 eV) | 1.025×10¹⁰ | 1.0246334×10¹⁰ | ✓ |
| 6.4 ⚑ | `e^{−2κ·1 Å}` | 1/7.8 | 1/7.7622 | ✓ |
| familiar | `e^{−2κw(√1836−1)}` | ≈10⁻¹³² | 2.064×10⁻¹³² | ✓ |
| 6.5 | bound states, 3 eV / 0.6 nm | −2.457819, −0.985835 | −2.45781881, −0.98583544 | ✓ |
| 6.5 | resonances | 1.178113, 6.400754 | 1.17811291, 6.40075405 | ✓ |
| 6.5 | `e-poles` at those two levels | "agreeing in every digit" | residual < 2×10⁻⁴⁰ | ✓ |
| 6.5 | `T` at 0.3 eV | 0.5151 | 0.51510384 | ✓ |
| WE1 | exact splitting, `qb=3` | 4.958968×10⁻³ | 4.9589675×10⁻³ | ✓ |
| WE1 | formula, `qb=3` | 4.957504×10⁻³ | 4.9575044×10⁻³ | ✓ |
| WE1 | agreement at `qb=5` | "seven figures" | six (9.0799886 vs 9.0799860 ×10⁻⁵) | ✗ m2 |
| WE2 | `|C/A|² = 4E/V₀` | 2 | 2 (exact) | ✓ |
| WE2 | `1/2κ`, 1 eV step | 0.138 nm | 0.1380214 | ✓ |
| WE2 | `1/2κ`, 10 eV step | 0.0317 nm | 0.0316646 | ✓ |
| WE3 | `T_δ` | 7.0804×10⁻² | 7.0804374×10⁻² | ✓ |
| WE3 | `T`, `w=0.1 nm` | 3.404×10⁻² | 3.4036270×10⁻² | ✓ |
| WE3 | `T`, `w=0.02 nm` | 6.039×10⁻² | 6.0385416×10⁻² | ✓ |
| WE3 | `T`, `w=0.01 nm` | 6.533×10⁻² | 6.5332267×10⁻² | ✓ |
| WE3 | order of the correction | `O(κw)` | `O((κw)²)` | ✗ B2 |
| P1(c) | Dirichlet / Neumann / periodic gaps | 1.128, 0.376, 1.504 eV | 1.128091, 0.376030, 1.504121 | ✓ |
| P1(c) | periodic first excited | 1.504121 eV | 1.5041206 | ✓ |
| P3(a) | thresholds, 2nd/3rd/4th state | 0.376030, 1.504121, 3.384271 eV | 0.3760302, 1.5041206, 3.3842715 | ✓ |
| P3(b) | exact lowest root, `z₀=11.4558` | 1.444377 | 1.44437674 | ✓ |
| P3(b) | `(π/2)/(1+1/z₀)` | 1.444686 | 1.44468619 | ✓ |
| P3(c) | `E/E_δ` at `z₀=0.1` | 0.98667 / 0.98687 | 0.9866667 / 0.9868678 | ✓ |
| P3(c) | `E/E_δ` at `z₀=0.181131` | 0.95626 / 0.95834 | 0.9562554 / 0.9583424 | ✓ |
| P3(d) | 3D threshold, `a=0.1 nm` | 9.4008 eV | 9.4007541 | ✓ |
| P4(a) | `√(m_p/m_e)` | 42.8504 | 42.850352 | ✓ |
| P4(a) | `κ_p`, `κ_p w` | 1.55231×10¹¹, 155.231 | 1.5523081×10¹¹, 155.23081 | ✓ |
| P4(a) | `T_p` | 5.89×10⁻¹³⁵ | 5.89237×10⁻¹³⁵ | ✓ |
| P4(b) | `ln(4×10⁶)` | 15.2018 | 15.201805 | ✓ |
| P4(b) | thick-form `w` | 2.0982 nm | 2.0981746 | ✓ |
| P4(b) | exact `w` | 2.09817 nm | 2.0981745 | ✓ |
| P4(c) | `κ` (4 eV) | 1.02463×10¹⁰ | 1.02463344×10¹⁰ | ✓ |
| P4(c) | `2κ/ln10`, decades/Å, factor | 8.900×10⁹, 0.890, 7.76 | 8.899853×10⁹, 0.8899853, 7.76221 | ✓ |
| P4(d) | `π²ħ²/2mw²`, `w=0.6 nm` | 1.044528 eV | 1.0445282 | ✓ |
| P4(d) | four candidates | −1.955472, 1.178113, 6.400754, 13.712452 | −1.9554718, 1.1781129, 6.4007541, 13.7124517 | ✓ |
| fig 2 | `T + R − 1` | "1e−12 at every setting" | worst 7.8×10⁻¹⁶ over 594 settings | ✓ |
| fig 2 | closed form vs ODE | "six figures" (plan) | worst rel. 4.6×10⁻¹¹, typical 10⁻¹⁴ | ✓ |
| fig 2 | resonances at `qw = nπ` | marked at `n²π²ħ²/2mw² + V₀` | verified against `q w/π` readout | ✓ |
| fig 1 | `⌈2z₀/π⌉` vs root finder | "agree at every setting" | agree at `z₀ =` 1.2, 2.56, 2.561584, 3.145, 6, 8, 9 and at exact multiples of `π/2` | ✓ |
| fig 1 | root residuals | "double-precision rounding" | ≤ 2.8×10⁻¹⁴ (worst at the near-threshold preset) | ✓ |

Independent-of-the-algebra checks performed: (i) tridiagonal finite-difference diagonalisation of the
finite well on 24 000 and 48 000 points across 12 nm with Richardson extrapolation, reproducing all
fourteen levels and all three counts; (ii) a Python re-implementation of the figure's RK4 integrator,
reproducing `T` for the 1 eV / 1 nm / 0.5 eV barrier to 14 digits and `T+R−1` to `10⁻¹⁶`;
(iii) sympy solution of the full 4×4 barrier matching system, reproducing `e-baramp` and `1/T` exactly.
