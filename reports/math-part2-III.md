# Mathematical verification — Part II (ch2-1…ch2-6) and Part III (ch3-1…ch3-6)

*Scope: `src/ch2-1.html` … `src/ch2-6.html`, `src/ch3-1.html` … `src/ch3-6.html`, read in order and in
full. Nothing was edited. Every result below was re-derived independently in sympy / mpmath / numpy
before being compared with the text; scratch scripts live in `/tmp/bk/`. Conventions taken as binding:
`CONVENTIONS.md` for Part II, `MATHPLAN-3.md` for Part III.*

---

## Verdict

Twelve chapters, and the mathematics holds: no result in either part is wrong, no derivation has a
step that fails to follow from its predecessor, and the sign conventions — the flagged high-risk
surface — are mutually consistent everywhere I could reach them, with κ = +8πG/c⁴, ∇^μG_{μν} = 0 and
the Einstein–Hilbert action sign all falling out of the book's own definitions rather than being
asserted. Two genuine defects survive verification, both arithmetic slips inside solution text in
`src/ch3-3.html` whose stated answers are nonetheless correct, and both fixable by a one-character
edit. Three further items are presentational rather than mathematical: one mis-cited internal
reference in `src/ch3-6.html`, one asserted-but-unproved algebraic step in `src/ch3-4.html`, and one
unflagged quotation in `src/ch3-5.html`.

**Counts — BLOCKER 0 · MAJOR 0 · MINOR 3** (plus 3 gap-class items in §2 that are not scored as
errors).

---

## §1 · Errors

### 1. MINOR — `src/ch3-3.html`, line 1448: sign of the cross term in Worked Example 2

**File:** `/home/claude/physics-book/src/ch3-3.html` (Worked Example 2, "Γ^r_θθ from the
transformation law")

**Exact current string** (grep-findable, one line):

```
$$ \Gamma^{r}{}_{\theta\theta} = -\Big[ r^{2}\sin^{2}\theta\cdot\frac{y^{2}}{r^{3}} - 2r^{2}\sin\theta\cos\theta\cdot\frac{xy}{r^{3}}\cdot(-1)\cdot(-1) + r^{2}\cos^{2}\theta\cdot\frac{x^{2}}{r^{3}} \Big], $$
```

**Exact corrected string** (single character changed: the `-` before `2r^{2}` becomes `+`):

```
$$ \Gamma^{r}{}_{\theta\theta} = -\Big[ r^{2}\sin^{2}\theta\cdot\frac{y^{2}}{r^{3}} + 2r^{2}\sin\theta\cos\theta\cdot\frac{xy}{r^{3}}\cdot(-1)\cdot(-1) + r^{2}\cos^{2}\theta\cdot\frac{x^{2}}{r^{3}} \Big], $$
```

With `+`, the two explicit `(-1)` factors have their intended referents — one is the sign of
∂x/∂θ = −r sinθ, the other the sign of ∂²r/∂x∂y = −xy/r³ — and the term evaluates to
+2r²sinθcosθ·xy/r³, which is what the *next* line of the text already uses
(`+ 2r\sin^{2}\theta\cos^{2}\theta` inside the bracket). As currently written the middle term
carries three minus signs and evaluates to −2r sin²θcos²θ, so the displayed bracket sums to
r cos²2θ and the line yields −r cos²2θ, not −r.

**Verification** (`/tmp/bk/v_ch33.py`):

```
book's 2nd derivs of r  : {('x','x'): y**2/(x**2+y**2)**(3/2),
                           ('x','y'): -x*y/(x**2+y**2)**(3/2),
                           ('y','y'): x**2/(x**2+y**2)**(3/2)}
dx/dth, dy/dth           : -r*sin(theta) , r*cos(theta)
term xx                  : r*sin(theta)**4
term xy (the middle one) : r*(1 - cos(4*theta))/4          <-- = +2 r sin^2 cos^2, POSITIVE
term yy                  : r*cos(theta)**4
Gamma^r_{th th}          : -r
book middle term literal : r*(cos(4*theta) - 1)/4          <-- = -2 r sin^2 cos^2, sign flipped
correct middle term      : r*(1 - cos(4*theta))/4
book total literal       : -r*(cos(4*theta) + 1)/2         <-- = -r cos^2(2 theta),  NOT -r
metric route Gamma^r_thth: -r    Gamma^th_rth: 1/r
```

The book's second derivatives of r, its Jacobian entries, its next line and its final answer −r are
all correct; only the one sign in the displayed equation is wrong.

---

### 2. MINOR — `src/ch3-3.html`, line 1481: wrong power of *a* in Problem 1(b)

**File:** `/home/claude/physics-book/src/ch3-3.html` (Problem 1, solution part (b))

**Exact current string** (spans lines 1481–1482; the unique grep target is `first by $a^{2}$`):

```
    $\Gamma^{v}{}_{uv}=\cos\theta/(a\sin\theta)$. Converting from $u$ back to $\theta$ divides the
    first by $a^{2}$ and multiplies the second by $a$, giving $-\sin\theta\cos\theta$ and
```

**Exact corrected string:**

```
    $\Gamma^{v}{}_{uv}=\cos\theta/(a\sin\theta)$. Converting from $u$ back to $\theta$ divides the
    first by $a$ and multiplies the second by $a$, giving $-\sin\theta\cos\theta$ and
```

Γ^θ_{vv} = (∂θ/∂u) Γ^u_{vv} = (1/a)(−a sinθcosθ) = −sinθcosθ. One factor of 1/a, not 1/a². A
dimensional check settles it without any computation: Γ^u_{vv} has dimensions of length, so dividing
by a² would leave 1/length, which cannot equal the dimensionless −sinθcosθ.

**Verification** (`/tmp/bk/v_ch33b.py`):

```
Gamma^u_vv (in u)  = -a*sin(2*u/a)/2   -> at u=a*theta: -a*sin(2*theta)/2
Gamma^v_uv (in u)  = 1/(a*tan(u/a))    -> at u=a*theta: 1/(a*tan(theta))
dtheta/du = 1/a; Gamma^theta_vv = -sin(2*theta)/2
Gamma^v_{theta v} = (du/dtheta) Gamma^v_uv = 1/tan(theta)
sphere direct: Gamma^theta_phiphi = -sin(2*theta)/2   Gamma^phi_{theta phi} = 1/tan(theta)
a^2 division would give: -sin(2*theta)/(2*a)          <-- what the text as written produces
```

The two stated answers (−sinθcosθ and cotθ) and the phrase "multiplies the second by a" are correct;
only the exponent on the first *a* is wrong.

---

### 3. MINOR — `src/ch3-5.html`, line 677: unflagged quotation of the general-*p* Poincaré lemma

`MATHPLAN-3.md` line 5: *"Everything below is **derived in the text**; items marked ⚑ are the only
permitted exceptions and must be flagged in place."* `src/ch3-5.html` contains **zero** ⚑ marks
(counted across all twelve chapters: ch2-1 20, ch2-2 12, ch2-3 6, ch2-4 1, ch2-5 8, ch2-6 7, ch3-1
10, ch3-2 3, ch3-3 4, ch3-4 4, **ch3-5 0**, ch3-6 7), yet §4.2's grind box asserts the general-degree
Poincaré lemma on the strength of a two-clause sketch.

**Exact current string** (lines 677–681):

```
    potential, quoted at Chapter 0.7 §7.3 with the note that Chapter 3.5 would prove it. The general
    $p$ runs the same way: the epsilon identity is replaced by the expansion of $\dd\omega$, the
    hypothesis $\dd\omega=0$ is spent at the same single step, and what survives is again a total
    derivative in $t$ whose endpoints give $\omega$.</p>
```

**Exact corrected string:**

```
    potential, quoted at Chapter 0.7 §7.3 with the note that Chapter 3.5 would prove it. ⚑ The general
    $p$ runs the same way — the epsilon identity is replaced by the expansion of $\dd\omega$, the
    hypothesis $\dd\omega=0$ is spent at the same single step, and what survives is again a total
    derivative in $t$ whose endpoints give $\omega$ — but that is a sketch and not a proof, and the
    general-degree statement is quoted here rather than derived. The two cases Chapter 0.7 §7.3 asked
    for, $p=1$ and $p=2$, are both proved in full above.</p>
```

The chapter's own promise ("Chapter 0.7 §7.3 quoted the Poincaré lemma and said that this chapter
would prove it; §4 does", line 27) *is* discharged, because 0.7 §7.3 asked only about the vector
potential (p = 2) and §4.2 proves p = 1 and p = 2 completely. So this is a flagging defect, not a
mathematical one — and the sketched claim is true.

**Verification that the sketch is correct** (`/tmp/bk/v_poincare2.py`), applying the homotopy
operator (Kω)_{μ₁…μ_{p−1}} = ∫₀¹ t^{p−1} x^ν ω_{νμ₁…μ_{p−1}}(tx) dt to closed forms of degree 1, 2, 3:

```
p=1:  d(K om) = [-1.38503447  0.520375  0.36706297]
        om    = [-1.38503447  0.520375  0.36706297]   max diff = 3.40e-11
p=2:  max| d(KB) - B | = 2.66e-08     vs scale max|B| = 1.485
p=3:  d(KC)_012 = 0.3635931386   C_012 = 0.3635931369   diff = 1.73e-09
```

(residuals are the finite-difference floor, h = 10⁻⁴).

---

## §2 · Gaps in the chain

Three places where a step is taken that the text does not justify. None changes a result; each is a
line that should be inserted.

### G1 — `src/ch3-4.html` §5.2, Stage 3 (lines 903–922): the total-antisymmetry step is asserted

Current text (lines 912–914):

```
<p>The reason is that the cyclic sum
$R_{abcd}+R_{acdb}+R_{adbc}$, once the pair symmetries are imposed, is itself totally antisymmetric
in all four indices, and any totally antisymmetric four-index array in $n$ dimensions has</p>
```

That the cyclic sum is *totally* antisymmetric — not merely antisymmetric in the pairs it inherits —
is the whole load-bearing content of Stage 3, and it is stated without argument. It is true, but it
needs the argument. **Insert immediately after "…is itself totally antisymmetric in all four
indices"**, as a new sentence:

```
Here is why. Call the cyclic sum $C_{abcd}$, and antisymmetrise $R$ over all four indices:
$R_{[abcd]}=\frac{1}{4!}\sum_{\sigma}\operatorname{sgn}(\sigma)R_{\sigma(a)\sigma(b)\sigma(c)\sigma(d)}$.
Sort the $24$ permutations by which <em>unordered</em> pair of pairs
$\{\sigma(a)\sigma(b)\mid\sigma(c)\sigma(d)\}$ they produce. There are three such splittings —
$ab|cd$, $ac|bd$, $ad|bc$ — and each is produced by $8$ permutations: two orderings inside the first
pair, two inside the second, and two choices of which pair comes first. Every one of those eight
carries the same signed value, because reordering inside a pair costs a sign under (S1) or (S2) and
the permutation costs the matching sign, and exchanging the two pairs costs nothing under (S4) and is
an even permutation. So each class contributes $8$ copies of one term and
$$ R_{[abcd]} \;=\; \frac{8}{24}\Big(R_{abcd}+R_{acdb}+R_{adbc}\Big) \;=\; \tfrac13\,C_{abcd}. $$
Being three times a total antisymmetrisation, $C_{abcd}$ is totally antisymmetric — and the cyclic
identity (S3), $C_{abcd}=0$, is the single condition $R_{[abcd]}=0$.
```

**Verification** (`/tmp/bk/v_cyc.py`) — build a random 4-index array satisfying (S1), (S2) and (S4)
but deliberately *not* (S3), then test its cyclic sum against all 24 permutations:

```
S1 holds?  0.0
S2 holds?  0.0
S4 holds?  0.0
S3 holds? (should NOT) max|C| = 4.165344524811752
book's claim: C_{abcd} is TOTALLY ANTISYMMETRIC -> max deviation over all 24 perms = 0
scale max|C| = 4.165344524811752
```

Exactly zero over all 24 permutations. And the counting argument above is confirmed directly
(`/tmp/bk/v_cyc4.py`):

```
pair-partition classes: 3  sizes: [8, 8, 8]
  class [(0, 1), (2, 3)]     size 8  distinct signed values: {-6.0084709289}
  class [(0, 2), (1, 3)]     size 8  distinct signed values: {-2.6883418761}
  class [(0, 3), (1, 2)]     size 8  distinct signed values: {4.5314682802}

Sum over all 24 sgn(p) A[p] / 24  = R_[abcd] = -1.388448174937251
C_{0123}/3                                   = -1.3884481749372508
difference                                   = -2.220446049250313e-16
```

Each class really does contain exactly 8 permutations all sharing one signed value, and
$C_{abcd}=3R_{[abcd]}$ to machine precision. The book's claim is right; only the justification is
missing.

The count that Stage 3 feeds is itself independently confirmed (`/tmp/bk/v_count.py`), by computing
the rank of the full (S1)–(S4) linear constraint system on n⁴ unknowns:

```
n : [2, 3, 4, 5, 6]
independent components (rank computation) : [1, 6, 20, 50, 105]
closed form n^2(n^2-1)/12                 : [1, 6, 20, 50, 105]
```

### G2 — `src/ch3-6.html` line 272: the uniqueness claim is attributed to a section that does not prove it

Current text:

```
second order. Chapter 3.4 §2 showed that the only <em>tensor</em> that can be built from the metric
and its first two derivatives is the Riemann tensor — the first derivatives alone give the
connection, which is not a tensor, and the second derivatives enter tensorially only in the
combination <a href="ch3-4.html">(3.4.13)</a>. So the ingredients are $g_{\mu\nu}$ and
$R^{\rho}{}_{\sigma\mu\nu}$.</p>
```

Chapter 3.4 §2 is titled "The commutator, and the tensor it produces". It proves that the Riemann
combination **is** a tensor. It does not prove that it is the **only** one — no uniqueness statement
appears anywhere in that section. (Equation (3.4.13) is correctly identified: it is `e-riemcomp`, the
component formula, the 13th numbered equation of ch3-4.) The support the book actually possesses for
the uniqueness is (a) §5.3's 80-versus-100 count, whose 20 survivors are exactly Riemann's component
count, and (b) for the general case, the ⚑-flagged Lovelock theorem quoted at ch3-6 §3.3. Suggested
replacement for the first sentence:

```
second order. Chapter 3.4 §2 showed that the Riemann tensor <em>is</em> a tensor built from exactly
those ingredients, and §5.3's count showed that its twenty components are precisely the twenty
combinations of second derivatives that survive at a point after normal coordinates have used up the
rest — the first derivatives alone give the connection, which is not a tensor, and the second
derivatives enter tensorially only in the combination <a href="ch3-4.html">(3.4.13)</a>. That the
list is exhaustive is the content of the theorem quoted in §3.3 below. So the ingredients are
$g_{\mu\nu}$ and $R^{\rho}{}_{\sigma\mu\nu}$.
```

### G3 — `src/ch3-5.html` §5.3 (lines 823–852): the cell decomposition is used, and its hypotheses are stated only afterwards

§5.3 opens "Chop $M$ into small cells, each of which can be mapped to a cube", derives generalised
Stokes from it, and only in the `callout familiar` that follows says "the cells must fit the region,
the region's boundary must be piecewise smooth, and the forms must be continuously differentiable".
The hypotheses *are* stated, and stated honestly — so this is not a missing-hypothesis defect — but
they are stated after the boxed result rather than before it, and the existence of the decomposition
itself is assumed. A one-clause insertion at the start of §5.3 fixes the ordering:

```
<p>Assume $M$ admits such a decomposition — that it can be chopped into finitely many small cells,
each smoothly mapped to a cube, with piecewise-smooth boundary; the callout below says what that
costs. Chop $M$ into small cells, each of which can be mapped to a cube. Write the theorem for each
cell and add.
```

---

## §3 · Convention audit

Every row was computed from scratch, never recalled. "Book's expression" is what the source says;
"independently computed" is what my own code returned from the book's own definitions.

| # | Quantity | Book's expression | Independently computed | Agrees? |
|---|---|---|---|---|
| 1 | Metric signature | η = diag(1,−1,−1,−1), timelike Δs² > 0 | used consistently in all twelve chapters | ✔ |
| 2 | Boost invariance | Λᵀ η Λ = η | `Lambda^T eta Lambda - eta = zeros(4,4)` | ✔ |
| 3 | Rapidity | β = tanh φ, γ = cosh φ, γβ = sinh φ | `Lr - L.subs(b,tanh(ph)) = zeros(4,4)` | ✔ |
| 4 | Rapidity additivity | Λ(φ₁)Λ(φ₂) = Λ(φ₁+φ₂) | `= zeros(4,4)` | ✔ |
| 5 | Velocity addition | (β₁+β₂)/(1+β₁β₂) | `tanh(φ₁+φ₂) = (tanh φ₁ + tanh φ₂)/(1 + tanh φ₁ tanh φ₂)` | ✔ |
| 6 | Four-velocity norm | u·u = c² | `u.u = c**2` | ✔ |
| 7 | Four-momentum norm | p·p = m²c², m rest mass | `p.p = c**2*m**2` | ✔ |
| 8 | Mass shell | E² = p²c² + m²c⁴ | `E**2 - P2*c**2 - m**2*c**4 = 0` | ✔ |
| 9 | Compton | 1/E′ − 1/E = (1−cosθ)/(m_e c²) | `(1 - cos(theta))/(c**2*m_e)` | ✔ |
| 10 | Four-potential | A^μ = (φ/c, **A**), A_μ = η_{μν}A^ν | `c·F_{10} = ∂_t A_x + ∂_x φ` ⇒ E_x | ✔ |
| 11 | Field tensor | F^{μν} = ∂^μA^ν − ∂^νA^μ; F^{0i} = −E^i/c, F^{ij} = −ε^{ijk}B^k | reproduced from A_μ(x) | ✔ |
| 12 | Scalar invariant | F_{μν}F^{μν} = 2(B² − E²/c²) | `2*(-E1**2-E2**2-E3**2 + c**2*(B1**2+B2**2+B3**2))/c**2` | ✔ |
| 13 | Pseudoscalar invariant | ε_{μνρσ}F^{μν}F^{ρσ} = (8/c)**E**·**B**, ε_{0123} = +1 | `8*(B1*E1+B2*E2+B3*E3)/c`; difference 0 | ✔ |
| 14 | ε index placement | book uses lower-index ε only | det η = −1 ⇒ ε^{0123} = −1; upper-index form never used, so no clash | ✔ |
| 15 | EM stress tensor | T^{μν} = (1/μ₀)(F^{μλ}F_λ{}^ν + ¼η^{μν}F_{αβ}F^{αβ}) | symmetric (residual 0), traceless (`η_{μν}T^{μν} = 0`) | ✔ |
| 16 | Energy density | T^{00} = ε₀E²/2 + B²/2μ₀ | `ε₀(E² + c²B²)/2` — identical | ✔ |
| 17 | Poynting | T^{0i} = S^i/c, **S** = **E**×**B**/μ₀ | `(-B2*E3 + B3*E2)/(c*μ₀)` = (E×B)_x/(μ₀c) | ✔ |
| 18 | Christoffel | Γ^λ_{μν} = ½g^{λσ}(∂_μg_{νσ}+∂_νg_{σμ}−∂_σg_{μν}) | polar: Γ^r_θθ = −r, Γ^θ_{rθ} = 1/r | ✔ |
| 19 | Riemann sign | [∇_μ,∇_ν]V^ρ = R^ρ_{σμν}V^σ ⇒ R^ρ_{σμν} = ∂_μΓ^ρ_{νσ} − ∂_νΓ^ρ_{μσ} + ΓΓ − ΓΓ | implemented literally in `/tmp/bk/gr.py`; all downstream rows use it | ✔ |
| 20 | Ricci | R_{μν} = R^λ_{μλν} | sphere: R_{θθ} = 1, R_{φφ} = sin²θ | ✔ |
| 21 | Ricci scalar sign | sphere of radius a has R = +2/a² | `R (Ricci scalar) = 2/a**2` | ✔ |
| 22 | Einstein tensor | G_{μν} = R_{μν} − ½Rg_{μν} | 2-sphere gives `Matrix([[0,0],[0,0]])`, as it must in n = 2 | ✔ |
| 23 | Riemann symmetries S1–S4 | antisym/antisym/1st Bianchi/pair exchange | generic Lorentzian 4-metric: 4.0e−9, 0.0, 1.4e−17, 2.0e−9 against scale 4.5e−2 | ✔ |
| 24 | Component count | n²(n²−1)/12; 20 in n = 4 | rank computation: [1, 6, 20, 50, 105] | ✔ |
| 25 | Weyl tensor | Riemann with all traces removed; 10 components in n = 4 | all traces `2.66e-15` against scale 3.76 | ✔ |
| 26 | 2nd Bianchi | ∇_{[λ}R_{μν]ρσ} = 0 | 60-digit mpmath: `1.03717e-31` against ‖∇R‖ = 0.116 | ✔ |
| 27 | Contracted Bianchi | ∇^μR_{μν} = ½∂_νR | agree to 3.5e−32 in all four components | ✔ |
| 28 | Divergence-free G | ∇^μG_{μν} = 0 | `3.49845e-32` against ‖G‖ = 0.047 | ✔ |
| 29 | Cornering B = −A/2 | (C4) forces B = −A/2 | A(½∂_νR) + B∂_νR = 0 ∀ metrics ⇔ B = −A/2 — follows from row 27 | ✔ |
| 30 | Geodesic deviation | D²ξ^μ/dτ² = −R^μ_{νρσ}u^νξ^ρu^σ | reorder of `e-gd4` with R antisym in last two indices; relabel γ→ν, β→ρ, α→σ | ✔ |
| 31 | Newtonian tidal limit | d²ξ^i/dt² = −c²R^i_{0j0}ξ^j | u^μ ≈ (c,0,0,0), ξ^μ = (0,ξ^j) — sums collapse exactly as stated | ✔ |
| 32 | Weak-field g₀₀ | g₀₀ = 1 + 2Φ/c² (this signature) | Γ^1_{00} = `∂_x Φ/c**2`; R^1_{010} = `Φ_,11/c**2`; R₀₀ = `∇²Φ/c**2` | ✔ |
| 33 | Sign check on row 32 | tidal tensor must be +Φ_,ij | d²ξ^i/dt² = −c²R^i_{0j0}ξ^j = −Φ_,ijξ^j ✔ Newton; the opposite g₀₀ sign would give anti-gravity | ✔ |
| 34 | Spatial-metric independence | R₀₀ = ∇²Φ/c² regardless of the spatial part | computed with g_{ij} = −(1−2sΦ/c²)δ_{ij} for symbolic s; result has no s | ✔ |
| 35 | Trace reverse | R_{μν} = κ(T_{μν} − ½Tg_{μν}) | g^{μν}G_{μν} = R − 2R = −R ⇒ R = −κT ⇒ boxed form | ✔ |
| 36 | κ | κ = +8πG/c⁴ | ∇²Φ/c² = ½κρc² ⇒ ∇²Φ = ½κρc⁴ = 4πGρ ⇒ κ = 8πG/c⁴ | ✔ |
| 37 | κ numeric | 2.08×10⁻⁴³, 1/κ = 4.8×10⁴² N | 2.0766×10⁻⁴³, 4.8155×10⁴² | ✔ |
| 38 | Perfect fluid | T^{μν} = (ρ+p/c²)u^μu^ν − pη^{μν} | ∂_μT^{μ0} = 0 → ∂_tρ + ∇·(ρ**v**) = 0; ∂_μT^{μi} = 0 → ρDv_i/Dt = −∂_ip | ✔ |
| 39 | EH variation identity | δ(√−g R) = √−g G_{μν}δg^{μν} + ∂_λ(√−g v^λ), v^λ = g^{μν}δΓ^λ_{μν} − g^{λν}δΓ^μ_{μν} | exact symbolic 3D rational-metric test: `LHS - RHS = 0` | ✔ |
| 40 | Matter stress definition | T_{μν} = +(2/√−g) δS_m/δg^{μν} | correct sign in (+,−,−,−); cross-checked against ch2-6's T^{00} > 0 | ✔ |
| 41 | Action sign | α = −c⁴/16πG, S_EH = −(c⁴/16πG)∫(R−2λ)√−g d⁴x | α = −1/(2κ) from `e-stationary` with κ = +8πG/c⁴ | ✔ |
| 42 | Forward-quote clash | ch1.2 §8.1 previewed S = (1/2κ)∫R√−g d⁴x | the discrepancy is ⚑-flagged in place at ch3-6 line 878 and explained via g → −g | ✔ |
| 43 | Λ sign | Λ = −λ; G_{μν} − Λg_{μν} = κT_{μν} in this signature | consistent with ρ_vac = −λc²/8πG = +Λc²/8πG; (−,+,+,+) contrast flagged at line 1049 | ✔ |
| 44 | Λ numeric | ρ_vac = 5.9×10⁻²⁷ kg m⁻³, ≈3.5 H atoms m⁻³ | 5.886×10⁻²⁷ from the book's own intermediate; 5.894×10⁻²⁷ exact | ✔ |
| 45 | F = dA | reproduces ch2-6's F_{μν} | verified for general A_μ(x) | ✔ |
| 46 | d⋆F = μ₀⋆J | equivalent to ∂_μF^{μν} = μ₀j^ν | component-by-component ratio uniformly `[-6,-6,-6,-6]` (= 3! from the 3-form dualisation × ε^{0123} = −1) | ✔ |
| 47 | Holonomy | α = Δφ(1−cosθ₀) = 𝒜/a² | direct numerical parallel transport: 0.25867359398 vs 0.25867359399, ratio 0.99999999999 | ✔ |
| 48 | Frame-change term | the +Δφ "frame change at the pole" in `e-holo` | transport alone gives −Δφcosθ₀ = −0.84132640601; the pole term is required to reach Δφ(1−cosθ₀) | ✔ |
| 49 | Units | G and c explicit throughout Part III; SI in Part II | no natural-units slip found in either part | ✔ |
| 50 | Rapidity symbol | φ, never η | `\varphi` used for rapidity; η reserved for the metric | ✔ |

---

## §4 · Verification log — what came back clean

Scripts in `/tmp/bk/`. Everything below was computed, not recalled.

**Part II.**

- `v_p2.py` — Λᵀ η Λ = η for both the β-form and the rapidity form; β = tanh φ maps one to the other
  exactly; Λ(φ₁)Λ(φ₂) = Λ(φ₁+φ₂) exactly, so velocity addition is rapidity addition; u·u = c²;
  p·p = m²c²; E² − p²c² − m²c⁴ = 0 identically; Compton 1/E′ − 1/E = (1−cosθ)/(m_ec²) and
  λ′ − λ − (h/m_ec)(1−cosθ) = 0.
- `v_em.py`, `v_em2.py`, `em.py`, `em2.py` — F_{μν} built from A_μ(x) reproduces the book's E and B
  read-offs; F_{μν}F^{μν} = 2(B²−E²/c²); ε_{μνρσ}F^{μν}F^{ρσ} − (8/c)**E**·**B** = 0 with the book's
  ε_{0123} = +1; T^{μν} symmetric (residual 0), traceless (η_{μν}T^{μν} = 0), T^{00} = ε₀E²/2+B²/2μ₀,
  T^{0i} = S^i/c. ch2-6's boost transformation rules for **E** and **B** reproduced from F′ = ΛFΛᵀ.
- ch2-4's Levi-Civita-as-density discussion, its symmetric/antisymmetric counts n(n±1)/2, and the
  quotient theorem all check out as stated; ch2-5's Mandelstam s, invariant mass and mass-defect
  arithmetic all reproduce.

**Part III — geometry.**

- `gr.py` implements the book's Riemann and Ricci sign conventions *literally* and is the basis of
  every symbolic curvature result below. `grnum.py` (4th-order central differences) and a 60-digit
  mpmath rewrite handle the cases where symbolic evaluation on a generic 4-metric does not terminate.
- `v_conv.py` — 2-sphere: Γ^θ_{φφ} = −sinθcosθ, Γ^φ_{θφ} = cotθ, R_{θθ} = 1, R_{φφ} = sin²θ,
  **R = +2/a²**, G_{μν} = 0. Every one matches ch3-3 and ch3-4.
- `v_weak.py` — weak-field metric with the book's g₀₀ = 1 + 2Φ/c² and an *undetermined* spatial
  coefficient s: Γ^i_{00} = ∂_iΦ/c², R^i_{0j0} = Φ_{,ij}/c², R₀₀ = ∇²Φ/c², the last independent of s.
  This is the check the flagged historical signature slip would have failed.
- `v_sym.py` — all four Riemann symmetries on a deliberately generic Lorentzian 4-metric (eigenvalues
  −1.038, −0.977, −0.936, +1.032): residuals 4.0e−9, 0.0, 1.4e−17, 2.0e−9 against a curvature scale
  of 4.5e−2 — i.e. the finite-difference floor.
- `v_bianchi_mp.py` — second Bianchi identity and ∇^μG_{μν} = 0 on the same metric at 60 decimal
  digits:

  ```
  dps=60  h=1.0e-10
  max|R_abcd| = 0.04543139267    max|nabla_e R_abcd| = 0.1159654939
  2nd Bianchi  max|nabla_[e R_ab]cd| = 1.03717e-31
  max|G_mn| = 0.047082747
  nabla^mu G_{mu nu}  max| | = 3.49845e-32
  ```

  Thirty orders of magnitude below scale. Both identities hold in the book's conventions; neither
  was accepted on the book's word.
- `v_conbianchi.py` — the contracted Bianchi identity component by component:

  ```
  nu=0 :  -7.60117966771e-5     vs   -7.60117966771e-5     diff -2.768e-33
  nu=1 :  -0.111572595408       vs   -0.111572595408       diff  2.663e-32
  nu=2 :   0.0165875627982      vs    0.0165875627982      diff -3.498e-32
  nu=3 :   0.00520012184803     vs    0.00520012184803     diff -1.504e-32
  ```

  This is what makes ch3-6's cornering B = −A/2 (constraint C4) follow rather than be asserted.
- `v_count.py` — the 1/6/20/50/105 table by rank of the (S1)–(S4) constraint system, matching
  n²(n²−1)/12. ch3-4's *second* route to 20 (the 100 second derivatives of the metric minus the 80
  killed by normal coordinates) reproduces the same number, as the text claims.
- `v_misc.py` — Weyl tensor built by the book's trace-removal prescription has every trace vanishing
  (2.66e−15 against scale 3.76), and carries 20 − 10 = 10 components in n = 4.
- `v_hol.py` — sphere holonomy by direct numerical parallel transport (Rodrigues rotation, 2×10⁵
  steps per leg) around ch3-4 §1's three-leg loop with θ₀ = 0.7, Δφ = 1.1:

  ```
  measured rotation relative to the END frame : -0.8413264060154743
    ^ book's leg-1 (latitude) term -Delta_phi*cos theta0 = -0.8413264060129374
  total holonomy in the START frame  = 0.25867359398452583
  book  Delta_phi(1-cos theta0)      = 0.2586735939870627
  ratio = 0.9999999999901928
  ```

  Both the leg-by-leg decomposition and the +Δφ frame-change term at the pole are confirmed, and
  α = 𝒜/a² follows.
- ch3-2: charts/atlases, tangent vectors as derivations, the Lie bracket and the vanishing of
  [∂_μ,∂_ν] for coordinate fields all check out; ch3-3: both routes to the geodesic equation
  (extremal proper time, and parallel transport of the tangent) give the same Γ, and the polar and
  spherical worked examples reproduce (aside from Errors 1 and 2 above); ch3-4 §8's flat-cone
  discussion is correct — R = 0 with non-trivial holonomy.

**Part III — forms, action, field equations.**

- `v_dstar.py` — d⋆F for general A_μ(x), dualised back to a vector, against ∂_μF^{μν}: the ratio is
  the *same* constant (−6) in all four components, so d⋆F = μ₀⋆J is literally ch2-6's inhomogeneous
  pair. dF = 0 likewise reproduces the homogeneous pair. The Part II ↔ Part III seam is clean.
- `v_poincare.py`, `v_poincare2.py` — the homotopy construction of ch3-5 §4.2 verified at p = 1
  (the book's own formula f(x) = ∫₀¹ω_μ(tx)x^μ dt, giving df − ω = 0 identically), and the general-p
  operator at p = 2 and p = 3.
- `v_eh.py` — the Einstein–Hilbert variation identity, done exactly:

  ```
  LHS  delta(sqrt(-g) R)                              = 0.00490380265666887492326078377683
  RHS  sqrt(-g) G_mn delta g^mn + d_l( sqrt(-g) v^l ) = 0.00490380265666887492326078377683
  LHS - RHS                                           = 0
  ```

  Rational-function metrics, rational perturbation, rational evaluation point: the residual is
  **exactly zero**, not small. This covers δ√−g = −½√−g g_{μν}δg^{μν}, the Palatini identity, and the
  identification of the total-derivative piece with v^λ = g^{μν}δΓ^λ_{μν} − g^{λν}δΓ^μ_{μν}.
- The action-sign question that motivated this review resolves in the book's favour. In (+,−,−,−) the
  correct matter definition is T_{μν} = +(2/√−g)δS_m/δg^{μν}, which I cross-checked two ways: against
  a free scalar field, and against ch2-6's electromagnetic tensor, which must give
  T^{00} = ε₀E²/2 + B²/2μ₀ > 0 — it does. From that, α = −1/(2κ) = −c⁴/16πG and
  S_EH = −(c⁴/16πG)∫(R−2λ)√−g d⁴x, exactly as ch3-6 line 873 has it. The clash with ch1.2 §8.1's
  forward-quoted +1/(2κ) is not an error in ch3-6: it is ⚑-flagged in place at line 878 and explained
  by the opposite-signature convention.
- `v_misc.py` — perfect-fluid conservation: ∂_μT^{μ0} = 0 gives continuity and ∂_μT^{μi} = 0 gives
  Euler with the correct pressure sign (ρDv/Dt = −∇p), confirming the −pη^{μν} term is right in this
  signature. The trace-reversed equation follows from g^{μν}G_{μν} = −R, which is signature-dependent
  and correct here.
- ch3-6's constraint list (C1)–(C5), the ten-equations/four-identities count, the vacuum equation of
  state p = −ρc², the Gibbons–Hawking–York remark and the Ostrogradsky remark are all internally
  consistent, and the last two are ⚑-flagged as quoted.
- ch3-6 worked examples and problems: κ = 2.08×10⁻⁴³ and 1/κ = 4.8×10⁴² N reproduce;
  R = −8πGρ/c² for cold matter; ρ_vac = Λc²/8πG = 5.9×10⁻²⁷ kg m⁻³ ≈ 3.5 H atoms m⁻³;
  r = (3M_⊙/8πρ_vac)^{1/3} ≈ 3.4×10¹⁸ m ≈ 110 pc, matching the stated "about 3×10¹⁸ m, roughly 100
  parsecs". The Λ-restored Poisson equation ∇²Φ = 4πGρ − Λc² and the static-universe balance
  Λ = 4πGρ/c² both follow.

**Hypotheses.** Every hypothesis I could find used is also stated: torsion-freedom is used exactly
twice in Part III and named both times (ch3-4 `e-torsionfree1` in §4.1 and the T₆ term in §2.2);
metric compatibility is named where the Levi-Civita formula is derived; the coordinate-patch
restriction is stated in ch3-2 and used in ch3-3; the boundary term in the EH variation is discussed
rather than silently discarded (with the GHY remark attached); weak-field, static and slow-motion are
each named at the point of use in ch3-4 §4.3 and ch3-6 §5. I found no hypothesis used but unstated.

**⚑ marks.** Counts: ch2-1 20, ch2-2 12, ch2-3 6, ch2-4 1, ch2-5 8, ch2-6 7, ch3-1 10, ch3-2 3,
ch3-3 4, ch3-4 4, ch3-5 0, ch3-6 7. I checked every "we quote", "without proof", "will not develop",
"do not prove" and "asserted" occurrence in all twelve chapters against the flag rule. All of them
carry a ⚑ except the ones in `src/ch3-5.html`, which is the subject of Error 3 and gap G3. I found
**no falsely-marked derivation** — nothing carries a ⚑ that the book in fact proves.

---

## §5 · Things I could not verify

1. **Cross-part forward references.** Claims about Chapters 0.x, 1.x, 3.7, 3.8, 5.4, 6.1, 7.7 and
   Part VI were outside my scope, so pointers such as "Chapter 3.1's equation (3.1.14)", "Chapter 0.7
   §7.3", "Chapter 2.4 §7.2" and "Chapter 1.2 §8.1 previewed this action as…" were checked for
   internal *consistency* with what Part II/III say, not against those chapters' actual text. The one
   case where the forward quotation visibly disagrees (ch1.2's action sign) is ⚑-flagged in place, so
   whichever way that is reconciled, ch3-6 has already discharged its obligation.

2. **Equation-number cross-references.** The `<a class="eqref">` links carry no visible number in
   source; numbers are assigned by the build, which I was instructed not to read. I resolved
   `(3.4.13)` by counting `class="eq" id=` occurrences in `src/ch3-4.html` (13th = `e-riemcomp`,
   correct), but did not audit every numbered cross-reference this way.

3. **Riemann symmetries at finite-difference precision.** The S1 and S4 residuals (4.0e−9, 2.0e−9)
   sit at the differencing floor rather than at machine zero. The 60-digit mpmath rerun that drove
   the Bianchi residuals to 1e−31 was not repeated for S1–S4; I consider them established, but the
   S1/S4 evidence is 9 significant figures rather than 31.

4. **Ostrogradsky, Lovelock, Whitney, the Riemann-flat converse, Sylvester's law, ODE
   existence-uniqueness, the wave-equation solvability theorem, Birkhoff.** All quoted rather than
   derived, all correctly ⚑-flagged, none re-proved here — they are outside what sympy can settle and
   the book does not claim them as derived.

5. **The general-region Stokes decomposition** (ch3-5 §5.3). That a piecewise-smooth region admits a
   finite cell decomposition mapping to cubes is a point-set fact I did not attempt to verify; the
   book states the hypothesis honestly (see G3), it simply states it late.

6. **Prose-level physical claims** — the numerology of experimental precisions in ch2-3's muon and
   GPS notes, the Darwin field-momentum historical discussion in ch2-6, the equivalence-principle
   framing in ch3-1 §2. These are physics-of-record rather than mathematics and were read but not
   independently checked against sources.

7. **Figures and interactive elements.** Not rendered, not checked.

---

*Scratch scripts: `/tmp/bk/gr.py`, `grnum.py`, `em.py`, `em2.py`, `totxt.py`, `v_ch33.py`,
`v_ch33b.py`, `v_conv.py`, `v_weak.py`, `v_sym.py`, `v_bianchi_mp.py`, `v_conbianchi.py`,
`v_count.py`, `v_cyc.py`, `v_cyc4.py`, `v_hol.py`, `v_eh.py`, `v_em.py`, `v_em2.py`, `v_dstar.py`,
`v_poincare.py`, `v_poincare2.py`, `v_misc.py`, `v_p2.py`.*
