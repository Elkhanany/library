# Mathematics review — Chapter 4.8, *The Oscillator, and the Ladder*

Independent re-derivation of `src/ch4-8.html` (14,700 words of prose by `registercheck`, 1,921 lines
including the figure script). Every algebraic result below was derived from scratch — in `sympy`
where it could be, in `mpmath` at 25 digits where it could not — before the page was consulted. Every
printed number was recomputed. The figure's grid Hamiltonian was re-implemented in Python, including
a line-by-line port of its cyclic Jacobi routine, because the quoted error figures are
implementation-dependent at the level they are quoted to.

**Counts: 0 BLOCKER, 2 MAJOR, 16 MINOR.**

Scratch work: `/tmp/mathrev48/`. Nothing in the repository was edited.

---

## What came out clean

Recorded because the brief asked for these specifically, and because a reviewer who reports only
defects has not said where the chapter is load-bearing.

* **§2's factorisation is exactly right, and the claim is carried rather than gestured at.**
  `(X̂−iP̂)(X̂+iP̂) = X̂²+P̂²+i[X̂,P̂]`; with `[X̂,P̂]=i` the residue is `−i[X̂,P̂]=+1`, so
  `Ĥ = (ħω/2)(X̂−iP̂)(X̂+iP̂) + ħω/2`. Every factor of `mω` and `ħ` checks: `x₀=√(ħ/mω)` and
  `p₀=√(ħmω)` are the unique length and momentum buildable from `ħ, m, ω` (I did the dimensional
  solve), `x₀p₀=ħ`, `â = √(mω/2ħ)(x̂ + ip̂/mω)` is exactly `(X̂+iP̂)/√2` with `x₀` substituted back,
  and `x̂ = (x₀/√2)(â+â†)`, `p̂ = (p₀/i√2)(â−â†)` invert correctly. `[â,â†]=1`, and the remark that
  without the `1/√2` it would be `2` is right. `â†â = ½(X̂−iP̂)(X̂+iP̂)` gives `Ĥ = ħω(â†â+½)`.
* **§3's two commutators.** `[N̂,â†] = â†[â,â†] = â†` and `[N̂,â] = [â†,â]â = −â`, both correct, both
  from `[â,â†]=1` and nothing else. The disjunction in §3.3 ("either an eigenvector with eigenvalue
  ν+1 *or* the zero vector") is stated at the point it is needed and used correctly in §4.
* **§4.3 genuinely excludes a non-integer eigenvalue** rather than merely bounding the spectrum below.
  The chain is complete: `‖â|ν⟩‖² = ν‖|ν⟩‖²` forces `ν` real *and* non-negative (the complex case is
  excluded automatically by that equation, though the chapter does not remark on it); the descent can
  stop only where the eigenvalue being lowered from is zero; a non-integer never reaches zero by
  integer subtraction; so the descent runs past zero and contradicts the bound. The upward half
  (`‖â†|n⟩‖² = (n+1)‖|n⟩‖² > 0`) closes the converse. This is the step most books skip and it is
  done here. See M1 for the one thing wrong with it, which is the licence rather than the logic.
* **§5.4's identification is not circular.** What is imported from 4.5 is `H_{n+1}=2ξH_n−H_n'`
  (proved in 4.5 §5.2's grind box as a statement about polynomials) and the normalising constant
  `√(2ⁿn!√π)` (4.5 §5.1). Neither says anything about energies. I verified symbolically that the
  ladder-generated `ψ_n` equals 4.5's `h_n` **exactly, including sign and constant, for n = 0…6**
  (`ψ_n − h_n` simplifies to `0` in sympy at every one). The normalisation step
  `√(2^{n+1}(n+1)!)/(√2·√(2ⁿn!)) = √(n+1)` is right. The eigenvalues in §4 come from `[â,â†]=1` and
  the inner-product axiom and would be what they are if 4.5 had never been written.
* **§4 imports no eigenvalue, no eigenfunction and no Hermite equation from 4.5.** I traced every
  citation in §§2–4: 4.2 §8 (the commutator), 0.5 §1.1 (positive definiteness), 0.5 §4 (the adjoint
  rules `(αA)†=ᾱA†` and `(AB)†=B†A†`, both derived there), and 4.5 §5.5 for *which* self-adjoint
  operator the formula denotes. Nothing else. Completeness is cited from 4.5 §5.4 and not reproved,
  which is what 4.3's closing brick licensed.
* **§5.6's parity route.** `Π̂â†Π̂ = −â†` from linearity in `x̂` and `p̂`; `Π̂|0⟩=|0⟩` because the
  Gaussian is even; inserting `Π̂²=Î` between the `n` copies gives `Π̂|n⟩=(−1)ⁿ|n⟩`. No wavefunction
  used, as claimed. The node count is right: I counted sign changes of the *numerically computed*
  eigenvectors over the figure's drawn window and got exactly `n` for every `n = 0…15`.
* **§6's phase-space collection is correct and is honest about its scope.** `⟨x̂²⟩=(n+½)ħ/mω`,
  `⟨p̂²⟩=(n+½)ħmω`, `ΔxΔp=(n+½)ħ`, equipartition between kinetic and potential at every rung, and
  substituting into 0.8 §4.4's ellipse gives `½+½=1` — all verified. The area `∮p dq = πab =
  π√(2E/mω²)·√(2mE) = 2πE/ω = (n+½)h` is right. §6.3 says in as many words that the general
  Bohr–Sommerfeld statement is 4.10's, that this is one case derived exactly, and that the reason it
  is exact is that the algebra has no small parameter. That is the honest boundary the brief asked for.
* **§6.1 does not pre-empt 4.9.** It attributes the `p=ħk` substitution to **Chapter 4.6 §10.2**, and
  4.6 §10.2 does indeed make it and does indeed say "The general inequality for an arbitrary pair of
  observables is Chapter 4.9's". §6.1 also says explicitly that "the general inequality … belongs to
  Chapter 4.9 §2 and is not needed here". (There *is* a stale promise in this area, but it is 0.9's
  and 4.6's, not 4.8's — see m12.)
* **§7 is right throughout.** `c_{n+1}√(n+1) = αc_n` unwinds to `c_n = αⁿc₀/√(n!)`; `c₀ = e^{−|α|²/2}`;
  `⟨x̂⟩=√2x₀Reα`, `⟨p̂⟩=√2p₀Imα`; the widths are `x₀/√2` and `p₀/√2`, independent of `α`, product
  `ħ/2`; `|α,t⟩ = e^{−iωt/2}|αe^{−iωt}⟩`, so `|α|` and hence both widths are constant and
  `⟨x̂⟩(t)=√2x₀|α|cos(ωt−θ)` is 0.8's classical solution with the right amplitude and phase;
  `⟨N̂⟩=|α|²`, `ΔN=|α|`, `|c_n|²` Poisson with mean `|α|²`. The claim about not being an energy
  eigenstate is correct and the `1/|α|` scaling is right. **The width claim against 4.6 checks
  against 4.6's own figure**: `S.s0 = Math.SQRT1_2` in `ch4-6.html`'s script, and 4.6 §10.8 says
  `σ₀=1/√2` "so that it matches the ground state". 4.6's closing brick does hand this forward to 4.8
  in the words 4.8 quotes.
* **The figure's replacement test really is independent.** I read the whole script. The Hamiltonian is
  a sinc/Colbert–Miller kinetic matrix plus `x²/2` on the diagonal, diagonalised by cyclic Jacobi;
  the drawing uses the sinc cardinal series. There is **no ladder operator, no Hermite function and
  no generating function anywhere in the computation** — `(n+0.5)` appears only as the comparison
  target in the two error readouts, never as an input. `⟨x̂²⟩` is `Σ c_j²x_j²` off the grid and
  `⟨p̂²⟩` is `2 vᵀTv`, both legitimate. Its stated numbers reproduce (table rows 1–6).
* **Conventions.** Exactly one ⚑ in the file. No `\dv[2]` or `\pdv[2]`. `\ann` used twice, both in
  one display (`e-fac`), labels in prose. No American `-ise` forms. The three occurrences of "just"
  are temporal ("just generated", "just derived", "the brick you just laid"), not hedges. One `where`,
  one `brick` ending with **Where this gets spent.**, one `familiar`, two `warn`, two `pause` rules.
  `registercheck.py --new` passes all four targets (em-dash 0.41/kw, semicolon 0.88/kw, >35w 11.9%,
  abrupt bridges 0%). `tagcheck.py` and `xrefcheck.py` clean.
* **The `familiar` box is sound.** `ℓ(θ) ≈ ℓ(θ̂) − ½I(θ̂)(θ−θ̂)²` with `I=−ℓ''`, Wald width `1/√I`,
  `mω²` in the part of `I`, and the two named failures (the width needs `ħ` as a second constant;
  there is no ladder in a log-likelihood) are both correct and correctly limited.

---

## MAJOR

### M1 · §4.2 — the domain licence does not cover the state the argument is applied to, and does not cover §7 at all

> "it needs $\ket\psi$ to be in the domain of $\hat a$ and $\hat a\ket\psi$ in the domain of
> $\hat a^{\dagger}$. Section 5 exhibits the states this chapter uses, they are polynomials times a
> Gaussian, and every one of them satisfies both. Given that, [e-norm] says that the expectation
> value of $\hat N$ is non-negative *in every state*."

The §2.4 warn box promises that the restriction "is stated out loud in §4.2 below, which is the one
place in the chapter where it does real work". It is stated — and then justified for exactly the set
of states the argument must *not* assume it has.

§4.3's reductio begins "Suppose $\nu$ is an eigenvalue and is not a non-negative integer." That
hypothetical `|ν⟩` is, by construction, **not** one of §5's polynomial-times-Gaussian states — those
are precisely the integer rungs. So the licence granted in §4.2 covers every state except the one the
chapter needs it for. The leap from "every one of §5's states satisfies both" to "in every state" is
the whole of the gap, and it sits under the chapter's flagship argument.

The repair is one sentence and needs nothing new. `N̂ = â†â` is a product of operators, whose natural
domain *is* `{ψ ∈ D(â) : âψ ∈ D(â†)}`; an eigenvector of `N̂` lies in `D(N̂)` by the meaning of the
word; so both conditions hold automatically for any eigenvector, integer or not. That is a statement
about the definition of the product, available before §5 and independent of it.

The same restriction is too narrow in the other direction as well. §2.4 says "The states this chapter
actually works with are the Hermite functions of §5 **and finite combinations of them**." §7 works
with `|α⟩ = e^{−|α|²/2} Σ αⁿ|n⟩/√(n!)`, an *infinite* combination, and moves `â` across an inner
product in §7.3, §7.5 and Problem 3(a) — including `⟨α|â†ââ†â|α⟩`. §5.5 says "Section 7 uses that
licence hard", but the licence it means is 4.5's *completeness*, not §2.4's *domain*, and nothing in
the chapter widens the domain statement to cover `|α⟩`. Again the repair is one sentence: the
coefficients `|c_n|² = e^{−|α|²}|α|^{2n}/n!` make `Σ n^k|c_n|²` finite for every `k`, so `|α⟩` is in
the domain of every polynomial in `â` and `â†`.

Neither conclusion is wrong. Both are unestablished as the chapter stands, at the two places the
chapter itself identifies as the ones where domains matter.

### M2 · §8, Worked example 1(c) — two premises used but not derived, carrying no mark, against a closing brick that says there are none

The chapter's flag budget is met in letter — one ⚑, on the spectroscopic data — but two further
statements are used and not derived, each *announcing itself in words while carrying no mark*, which
`CONVENTIONS.md` names as the exact failure mode the ⚑ contract exists to prevent.

> "The force constant is a property of the electronic energy curve, which depends on the charges and
> not on the nuclear masses, so the two isotopologues should share it. **That is a hypothesis about
> the electronic problem, and this chapter does not derive it.**"

> "Suppose a reaction rate goes as $\ee^{-\Delta/RT}$ in the energy needed to reach the top of a
> barrier, **which is a premise about chemistry rather than a result of this chapter.**"

Neither is derived here or in any chapter of this book, written or planned. The second is
load-bearing for a printed number: the kinetic-isotope-effect factor of 7.7 is a result of Worked
example 1 and rests entirely on the Arrhenius form. The first is load-bearing for the prediction
`ν̃_D = 2145.12 cm⁻¹`.

Three statements in the chapter are contradicted by this:

* the `where` callout: "One result in this chapter is quoted rather than derived and it is
  experimental … **There are no others.**" (This sentence is also short of the ⚑ box's own second
  paragraph, which quotes a bond length and three atomic masses.)
* the ⚑ box: "predicts the second molecule's frequency from the first's **using nothing but the
  masses**" — the prediction uses the masses *and* the shared-force-constant hypothesis, which the
  body of 1(c) says plainly and the box does not.
* the closing brick: "**Every other result in this chapter is derived here or in a chapter that
  derived it.**"

For contrast, the two *forward* borrowings the brick does name — 4.17's `x̂` coupling in Worked
example 2(c) and 4.15's first-order formula in Problem 4(b) — are consistent with book practice (4.6
§8.7 states Ehrenfest and defers it without a mark) and are not findings. These two are different:
nothing in this book will ever derive them.

---

## MINOR

### m1 · §5.2, `e-ground` — a false equality between two different normalisations

> $$ \psi_{0}(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^{2}}{2\hbar}\right) = \pi^{-1/4}\,\ee^{-\xi^{2}/2} $$

The two sides are not equal. `(mω/πħ)^{1/4} = π^{−1/4}x₀^{−1/2}`, so the left-hand side is
`π^{−1/4}x₀^{−1/2}e^{−ξ²/2}`. The left is normalised against `dx` and carries dimension
`length^{−1/2}`; the right is normalised against `dξ` and is dimensionless. They differ by `√x₀`.

Nothing downstream breaks — `e-psin`, §5.3's `ψ₁` and `ψ₂`, and §5.4's identification with `h_n` all
use the `ξ`-normalised convention consistently, and 4.5's `h_n` is `ξ`-normalised too. But the
convention the reviewer is checking against says that a chapter working in dimensionless units "must
say so **and say how to get back**", and the rescaling of the *wavefunction* (as opposed to lengths)
is never stated. One clause — "with wavefunctions normalised against $\dd\xi$, so that the
$x$-normalised form carries a further $x_{0}^{-1/2}$" — closes it.

### m2 · §8, Worked example 1(b) — the seventh figure of ω is wrong

> "$\omega=2\pi c\tilde\nu$, which for $2990.95\ \mathrm{cm^{-1}}$ gives
> $5.633900\times10^{14}\ \mathrm{s^{-1}}$"

`2π × 299792458 × 299095 m⁻¹ = 5.633908×10¹⁴ s⁻¹`. Printed to seven figures, the last is wrong:
**5.633908**, not 5.633900.

### m3 · §8, Worked example 1(c) — both force constants are wrong in the sixth figure

> "the force constants extracted separately from the two molecules are $516.313$ and
> $516.336\ \mathrm{N\,m^{-1}}$, agreeing to four parts in a hundred thousand"

I get `k_H = μ_H ω_H² = 516.314` and `k_D = 516.334` N m⁻¹ (CODATA-2018 `u`; CODATA-2014 changes the
seventh figure only). The `516.313` is what you get from the chapter's own truncated
`ω = 5.6339×10¹⁴` (516.3127), so it is downstream of m2. `516.336` I cannot reproduce by any
rounding I tried.

The **claim survives**: my residual is `(k_D−k_H)/k_H = 3.88×10⁻⁵`, which is "four parts in a hundred
thousand" as printed. It is also exactly twice the frequency-ratio residual, as it must be since
`k ∝ ν̃²` — the chapter's two statements are internally consistent.

### m4 · §8, Worked example 1(c) — the measured ratio is wrong in the sixth decimal

> "The measured ratio is $2145.16/2990.95=0.717219$."

`2145.16/2990.95 = 0.7172169…`, i.e. **0.717217**. (The predicted `0.717203` is right, and the
departure "two parts in a hundred thousand" is right: I get `1.94×10⁻⁵`.)

### m5 · §6.4 — the matrix described is not the second derivative, and the grid does not span 9

> "represent the second derivative on that grid exactly … Its entries are $\pi^{2}/3$ on the diagonal
> and $2(-1)^{j-k}/(j-k)^{2}$ off it, all divided by twice the squared spacing."

That matrix, divided by `Δ²`, is `−d²/dx²`, not `d²/dx²` — I checked it against `f=e^{−x²/2}`, whose
exact `f''=(x²−1)f`, and got exactly `−f''`. Divided by `2Δ²` it is `−(ħ²/2m)d²/dx²`, the kinetic
energy at `ħ=m=1`. A reader who took the sentence literally and then "added the potential `½x²` down
the diagonal" would build `+d²/dx² + x²/2`, the wrong operator. The script's own comment gets this
right (it calls the object `T_jk`); the prose does not.

Separately: `NG=60`, `LG=18`, so `d=0.3` and the grid **points** run from `−8.85` to `+8.85`, not
`|x| ≤ 9`. (The 60 cells do span 18, so the sentence is defensible; it is worth one word.)

### m6 · §4.4 and the `where` callout — "no differential equation" over-claims what §4 established

> §4.4: "No differential equation was solved, no series was summed and no boundary condition was
> imposed."
> `where`: "Out of that comes $E_n=(n+\half)\hbar\omega$, from the algebra and nothing else."

One paragraph earlier, §4.3 says the opposite and says it honestly: "All of it rests on a state
annihilated by $\hat a$ existing at all, which is not yet proved. Section 5 proves it by solving one
first-order differential equation." The algebra alone establishes which values are *permitted*; that
any of them is *occupied* — and hence that the boxed `e-spectrum` is a spectrum rather than an empty
constraint — needs §5.2's differential equation. Both sentences above should carry the same
qualification §4.3 already supplies.

### m7 · §4.5 — the second half of `e-ladact` is forced, not chosen

> "the multiple is fixed up to a phase, which we fix once and for all by choosing it to be $+1$ at
> every rung"

Only one phase is free. Defining `|n+1⟩ ≡ â†|n⟩/√(n+1)` immediately gives
`â|n+1⟩ = ââ†|n⟩/√(n+1) = (N̂+1)|n⟩/√(n+1) = √(n+1)|n⟩`, which is the second relation with the same
sign — not an independent convention. As written the reader is invited to make two choices that
could conflict, and the one line showing they cannot is missing.

### m8 · §2.2 — the identification is asserted before two of its three ingredients arrive

> "**The $\half\hbar\omega$ is already here.** … Anything that later calls itself the zero-point
> energy of this oscillator is this term"

What §2.2 has proved is that `Ĥ = ħω â†â + ħω/2` identically. That this term *is* the ground-state
energy — rather than an offset above which the spectrum might start anywhere — needs `â†â ≥ 0` (§4.2)
and the existence of a state with `â|0⟩=0` (§5.2). Both arrive, in this chapter; the claim is true.
But the chapter never marks the debt at the point it is incurred, and §4.4's back-reference ("§2.2
showed it is the commutator") is the only place the loop is closed, obliquely. The pedagogical claim
the section exists to make is carried; the logical order is not signposted.

### m9 · Closing brick — "three marks leaned on" is short by one

> "Three marks standing elsewhere are leaned on and cited rather than raised again."

There is a fourth. §5.2's non-degeneracy — "Chapter 0.8 §3.1 showed that the solution space of a
homogeneous linear differential equation has dimension equal to its order" — rests on 0.8 §3.1, whose
proof is explicitly "where the quoted theorem of §1 gets spent", and 0.8 §1 carries
**⚑ Quoted, not proved — Picard–Lindelöf**. The contract itself is satisfied (the mark is raised in
0.8, and 4.8 cites 0.8 §3.1 by name); it is the brick's enumeration that is incomplete, and
non-degeneracy of the whole spectrum is not a small thing to leave off a list of what the chapter
leans on.

### m10 · Closing brick — "collects Chapter 1.3 §4.4's Bohr–Sommerfeld mark" over-claims

§6.3 draws the boundary correctly and at length: 1.3's condition is general, this chapter derived one
case, the general statement is 4.10 §6's. The brick then compresses that to "That collects … Chapter
1.3 §4.4's Bohr–Sommerfeld mark", without the qualifier, in the one paragraph a reader takes away.

Related, and upstream: 1.3 §4.4's mark still reads "⚑ **Quoted forward to Chapter 4.8**" for a
statement 4.8 correctly declines to prove in general. That pointer now needs to name 4.10, or both.

### m11 · §4.4 and §6.2 — two italicised quotations attributed to the wrong section of 0.8

> §4.4: "Chapter 0.8 §4.4 promised *ladder operators, and the $\tfrac12\hbar\omega$ that will not go
> away*"
> §6.2: "Chapter 0.8 §4.4 said … and called the area *the area that Chapter 4.8 will quantise*"

Both phrases are verbatim, and both are in **0.8's closing brick** (`src/ch0-8.html` lines 1882 and
1894), not in its §4.4. §4.4 does compute the area and does say "Chapter 4.8 derives this properly
with ladder operators", so the substance is where it is claimed to be; the words are not. Italics
marking a quotation should point at the sentence it came from.

### m12 · §6.1 — the `p=ħk` promise is collected in two places and neither is the one 0.9 names

4.8 says, accurately, that Chapter 4.6 §10.2 turned the bandwidth theorem into `Δx Δp ≥ ħ/2` "using
the single substitution $p=\hbar k$", and 4.6 §10.2 does exactly that. But Chapter 0.9 promises that
substitution to **Chapter 4.9** in four separate places — its opening (line 26), §6's closing remarks
(lines 1080, 1114) and its closing list ("**The bandwidth theorem** → Chapter 4.9, which adds
`p=ħk` and nothing else"). The defect is 0.9's or 4.6's rather than 4.8's, and 4.8 does *not*
pre-empt 4.9 (it says the general two-observable inequality "belongs to Chapter 4.9 §2"). It is
recorded here because 4.8 is now the second chapter repeating a collection 0.9 still assigns to a
third, and 4.9 is being written in parallel.

### m13 · The figure's readouts use `n` for the destination rung, `e-ladact` for the source

> raise: `'the state climbed to n = ' + lev + ', … multiplied its length by sqrt(n) = ' + Math.sqrt(lev)`
> lower: `'the state fell to n = ' + lev + ', … multiplied its length by sqrt(n+1) = ' + Math.sqrt(lev+1)`

Both are **numerically correct** — the increment happens before the message is built, so `sqrt(lev)`
after a raise is `√(n_old+1)` and `sqrt(lev+1)` after a lower is `√(n_old)`. But `e-ladact`, which
the figure caption points at, writes `â†|n⟩=√(n+1)|n+1⟩` and `â|n⟩=√n|n−1⟩` with `n` the *starting*
rung. A reader who presses "raise" from the ground state reads "sqrt(n) = 1.000000" beside an
equation that says the factor is `√(n+1)`. Same number, clashing label.

### m14 · Worked example 2(b) — the `⟨m|x̂²|n⟩` display overflows its box

Rendered from `.staging` at 1100–1440px viewport: the `.worked` box is 660px and the display needs
681px, so it acquires a horizontal scrollbar. (The main `.eq` column measures 704px and every display
in it fits; this one is inside a worked example, which is narrower.) It is the only overflow in the
chapter at any width I tested. Splitting the three Kronecker terms over two lines fixes it.

### m15 · §6.4 — "exact to the last bit" is hyperbole

> "Between those two the window is wide and the answer inside it is exact to the last bit."

The worst departure inside the window is `1.2×10⁻¹³` on a level of `15.5`, which is about 35 units in
the last place, not one. "At the level of double-precision rounding for a matrix of this size" — the
chapter's own earlier phrasing — is correct and is what this sentence should say.

### m16 · §1.3 — "got it two ways" attributed to 4.7 §3.3

> "Chapter 4.7 §3.3 found that the states of a symmetric potential alternate even and odd up the
> ladder, and got it two ways, from a non-degeneracy argument and from the roots of a matching
> condition."

4.7 §3.3 gets it a *third* way, by substituting `x→x+L/2` in the infinite well's solutions; the
non-degeneracy argument is its §2.4 and the matching-condition-branch argument is its §4.3. §5.6 of
this chapter gets all three attributions right, so this is a slip in the forward-look only.

---

## Every number I reproduced independently

Agreement column: ✓ = reproduces to the precision printed; ✗ = does not.

### The grid Hamiltonian (§6.4, the brick, the figure)

| Quantity | Printed | Mine | Agree |
|---|---|---|---|
| lowest 16 eigenvalues | $0.5,1.5,\dots,15.5$ | $0.5,1.5,\dots,15.5$ | ✓ |
| worst $\lvert E_n-(n+\tfrac12)\rvert$, 16 levels | $1.2\times10^{-13}$ | $1.207923\times10^{-13}$ | ✓ |
| worst $\lvert$gap$-1\rvert$ | $6.2\times10^{-14}$ | $6.217249\times10^{-14}$ | ✓ |
| worst rel. $\lvert\langle x^2\rangle-(n+\tfrac12)\rvert$ | $1.5\times10^{-14}$ | $1.471839\times10^{-14}$ | ✓ |
| $\Delta x\,\Delta p$ vs $(n+\tfrac12)\hbar$ | "twelve figures" | worst rel. $1.088\times10^{-14}$ (≈14 figs) | ✓ |
| 16th level, span shrunk to $\lvert x\rvert\le7.5$ | $4\times10^{-7}$ | $4.170\times10^{-7}$ | ✓ |
| 16th level, span stretched to $\lvert x\rvert\le14$ | $1\times10^{-3}$ | $1.086\times10^{-3}$ | ✓ |
| nodes of numerical $\psi_n$, $n=0\dots15$ | exactly $n$ | exactly $n$ (sign changes on $\lvert x\rvert\le6.6$) | ✓ |
| ground-state phase-space disc area | $h/2$ | $\pi r^2x_0p_0=\pi\hbar=h/2$ at $r=\sqrt{2E_0}=1$ | ✓ |

The three error figures are reproducible only with the figure's own **cyclic Jacobi** routine, ported
line by line; LAPACK `eigh` on the same matrix gives $7.1\times10^{-15}$, $7.2\times10^{-15}$,
$9.3\times10^{-15}$. The printed values are the ones the page will actually display.

### Worked example 1 — hydrogen chloride

| Quantity | Printed | Mine | Agree |
|---|---|---|---|
| $\mu_{\mathrm H}$ | $0.979593\ \mathrm u$ | $0.9795925$ | ✓ |
| $\mu_{\mathrm H}$ | $1.626652\times10^{-27}\ \mathrm{kg}$ | $1.6266516\times10^{-27}$ | ✓ |
| $\mu_{\mathrm D}$ | $1.904413\ \mathrm u$ | $1.9044134$ | ✓ |
| $\omega_{\mathrm H}$ | $5.633900\times10^{14}\ \mathrm{s^{-1}}$ | $5.633908\times10^{14}$ | ✗ (m2) |
| $k$ (2 d.p.) | $516.31\ \mathrm{N\,m^{-1}}$ | $516.314$ | ✓ |
| zero-point energy | $0.185415\ \mathrm{eV}$ | $0.1854153$ | ✓ |
| zero-point energy | $17.890\ \mathrm{kJ\,mol^{-1}}$ | $17.88985$ | ✓ |
| zero-point energy | $1495.5\ \mathrm{cm^{-1}}$ | $1495.475$ | ✓ |
| $k_BT$ at room temperature | $0.02569\ \mathrm{eV}$ | $0.025693$ at $298.15\ \mathrm K$ | ✓ |
| ZPE / $k_BT$ | "seven times" | $7.22$ | ✓ |
| $\ee^{-\hbar\omega/k_BT}$ at $300\ \mathrm K$ | $5.9\times10^{-7}$ | $5.893\times10^{-7}$ | ✓ |
| $x_0$ | $10.727\ \mathrm{pm}$ | $10.72719$ | ✓ |
| $x_0/\sqrt2$ | $7.585\ \mathrm{pm}$ | $7.58527$ | ✓ |
| rms / bond length | "about six percent" | $5.95\ \%$ | ✓ |
| predicted $\omega_{\mathrm D}/\omega_{\mathrm H}$ | $0.717203$ | $0.7172030$ | ✓ |
| measured $\tilde\nu_{\mathrm D}/\tilde\nu_{\mathrm H}$ | $0.717219$ | $0.7172169$ | ✗ (m4) |
| predicted $\tilde\nu_{\mathrm D}$ | $2145.12\ \mathrm{cm^{-1}}$ | $2145.1184$ | ✓ |
| departure of that prediction | "two parts in $10^{5}$" | $1.941\times10^{-5}$ | ✓ |
| $k$ from $^{1}$H$^{35}$Cl | $516.313\ \mathrm{N\,m^{-1}}$ | $516.3141$ | ✗ (m3) |
| $k$ from $^{2}$H$^{35}$Cl | $516.336\ \mathrm{N\,m^{-1}}$ | $516.3342$ | ✗ (m3) |
| agreement of the two $k$ | "four parts in $10^{5}$" | $3.882\times10^{-5}$ | ✓ |
| $\Delta$(zero-point energy) | $5.06\ \mathrm{kJ\,mol^{-1}}$ | $5.0589$ | ✓ |
| kinetic isotope effect | factor $7.7$ | $7.704$ at $298.15\ \mathrm K$ | ✓ |
| overtone / fundamental | $5667.98/2885.98=1.96397$ | $1.9639706$ | ✓ |
| shortfall from $2$ | $1.80\ \%$ | $1.8015\ \%$ | ✓ |
| fundamental below harmonic | $3.51\ \%$ | $3.5096\ \%$ | ✓ |

### Worked example 2(d) — matrix elements by direct integration of the Hermite functions

| Quantity | Printed | Mine (mpmath, 25 dps) | Agree |
|---|---|---|---|
| $\avg{0\lvert\hat x\rvert1}/x_0$ | $0.7071067812$ | $0.707106781187$ | ✓ |
| $\avg{1\lvert\hat x\rvert2}/x_0$ | $1.0000000000$ | $1.000000000000$ | ✓ |
| $\avg{2\lvert\hat x\rvert3}/x_0$ | $1.2247448714$ | $1.224744871392$ | ✓ |
| $\avg{0\lvert\hat x\rvert3}$, $\avg{2\lvert\hat x\rvert2}$ | vanish to 11 d.p. | $1.8\times10^{-33}$, $0$ | ✓ |
| $\avg{n\lvert\hat x^{2}\rvert n}/x_0^{2}$, $n=0,1,3$ | $0.5,\ 1.5,\ 3.5$ | $0.5,\ 1.5,\ 3.5$ | ✓ |
| $\avg{0\lvert\hat x^{2}\rvert2}/x_0^{2}$ | $0.7071067812$ | $0.707106781187$ | ✓ |
| $\avg{1\lvert\hat x^{2}\rvert3}/x_0^{2}$ | $1.2247448714$ | $1.224744871392$ | ✓ |

### Worked example 3(c) — the trapped ion and the bound electron

| Quantity | Printed | Mine | Agree |
|---|---|---|---|
| $x_0$, $^{40}$Ca$^{+}$ at $1\ \mathrm{MHz}$ | $15.90\ \mathrm{nm}$ | $15.9036$ | ✓ |
| $\hbar\omega$ | $4.14\ \mathrm{neV}$ | $4.1357$ | ✓ |
| $x_s$ at $1\ \mathrm{V\,m^{-1}}$ | $61.2\ \mathrm{nm}$ | $61.157$ | ✓ |
| $x_s/x_0$ | $3.85$ | $3.8455$ | ✓ |
| $\abs\lambda^{2}$ (and the drop in quanta) | $7.39$ | $7.3939$ | ✓ |
| field for $1\%$ of the electron's spacing | $5.1\times10^{8}\ \mathrm{V\,m^{-1}}$ | $5.123\times10^{8}$ | ✓ |
| $m\omega^{2}$, electron at $\hbar\omega=1\ \mathrm{eV}$ | $2.10\ \mathrm{N\,m^{-1}}$ | $2.1026$ | ✓ |
| $m\omega^{2}$, ion | $2.62\times10^{-12}\ \mathrm{N\,m^{-1}}$ | $2.6198\times10^{-12}$ | ✓ |
| ratio of the two | "twelve orders of magnitude" | $8.03\times10^{11}$ ($11.90$ orders) | ✓ |

### Problems

| Quantity | Printed | Mine | Agree |
|---|---|---|---|
| P1(b) degeneracies, $n=0\dots6$ | $1,3,6,10,15,21,28$ | $\tfrac12(n+1)(n+2)$ → same | ✓ |
| P1(d) $2\ell+1$ decomposition | $6=5+1$, $10=7+3$, $15=9+5+1$ | same | ✓ |
| P2(a) descent from $\nu=\tfrac52$ | contradiction at the third step | $\tfrac32,\tfrac12,-\tfrac12$ | ✓ |
| P2(b) upward bound | $\nu\ge-1$ | $\nu\ge-1$ | ✓ |
| P2(d) $\norm{\hat c^{\dagger}\ket0}^{2}$ | $-1$ | $-1$ | ✓ |
| P3(b) photon energy at $633\ \mathrm{nm}$ | $3.14\times10^{-19}\ \mathrm J$ | $3.1382\times10^{-19}$ | ✓ |
| P3(b) $\abs\alpha^{2}$ | $3.2\times10^{6}$ | $3.187\times10^{6}$ | ✓ |
| P3(b) $1/\abs\alpha$ | $5.6\times10^{-4}$ | $5.601\times10^{-4}$ | ✓ |
| P3(c) $\abs{\avg{\beta\vert\alpha}}^{2}$ | $\ee^{-\abs{\alpha-\beta}^{2}}$ | derived, same | ✓ |
| P4(a) $\avg{n\lvert\hat x^{4}\rvert n}/x_0^{4}$, $n=0,1,2,3,5$ | $0.75,3.75,9.75,18.75,45.75$ | same, by integration and by $\tfrac34(2n^{2}+2n+1)$ | ✓ |
| P4(b) change in the $n\to n+1$ gap | $\tfrac34\lambda x_0^{4}\cdot4(n+1)$ | same | ✓ |
| P4(d) overtone shortfall | $3\abs\lambda x_0^{4}$ | same | ✓ |
| P4(d) $\abs\lambda x_0^{4}$ | $\approx0.012\,\hbar\omega$ | $0.0116\,\hbar\omega$ | ✓ |

### Symbolic identities re-derived rather than read

| Statement | Result |
|---|---|
| $(\hat X-\ii\hat P)(\hat X+\ii\hat P)=\hat X^{2}+\hat P^{2}+\ii[\hat X,\hat P]$ | ✓ |
| $[\hat a,\hat a^{\dagger}]=1$; without the $1/\sqrt2$, $=2$ | ✓ |
| $(\xi+\dd/\dd\xi)(\xi-\dd/\dd\xi)-\text{reverse}=2$ on a test function | ✓ |
| $\psi_n=h_n$ exactly, sign and constant, $n=0\dots6$ | ✓ (sympy: difference simplifies to $0$) |
| $\sqrt{2^{n+1}(n+1)!}\big/\big(\sqrt2\sqrt{2^{n}n!}\big)=\sqrt{n+1}$ | ✓ |
| $\Pi\ket n=(-1)^{n}\ket n$ from $\Pi\hat a^{\dagger}\Pi=-\hat a^{\dagger}$ | ✓ |
| $\oint p\,\dd q=\pi\sqrt{2E/m\omega^{2}}\sqrt{2mE}=2\pi E/\omega=(n+\half)h$ | ✓ |
| $\avg{\hat p^{2}}/2mE_n+\avg{\hat x^{2}}m\omega^{2}/2E_n=\half+\half=1$ | ✓ |
| kinetic $=$ potential $=\tfrac14(2n+1)\hbar\omega$, sum $=E_n$ | ✓ |
| $\ket{\alpha,t}=\ee^{-\ii\omega t/2}\ket{\alpha\ee^{-\ii\omega t}}$ | ✓ |
| $\Delta N=\abs\alpha$ from $\avg{\hat N^{2}}=\abs\alpha^{4}+\abs\alpha^{2}$ | ✓ |
| WE3: $\lambda=q\mathcal Ex_0/\sqrt2\hbar\omega$, shift $=\abs\lambda^{2}\hbar\omega=q^{2}\mathcal E^{2}/2m\omega^{2}$ | ✓ |
| WE3: $\half m\omega^{2}x^{2}-q\mathcal Ex$ completes the square with $x_s=q\mathcal E/m\omega^{2}$ | ✓ |
| WE3(d): second-order sum $=\dfrac{x_0^{2}q^{2}\mathcal E^{2}}{2}\Big[\dfrac{n+1}{-\hbar\omega}+\dfrac{n}{\hbar\omega}\Big]=-\dfrac{q^{2}\mathcal E^{2}}{2m\omega^{2}}$, $n$-independent | ✓ |
| Colbert–Miller matrix $\times\Delta^{-2}$ equals $-\dd^{2}/\dd x^{2}$, not $+$ | ✓ (m5) |
