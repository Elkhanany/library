# Independent verification — `src/ch3-9.html`, "Cosmology, and a Loose Thread"

*Verifier: an agent that did not write the chapter. Every tensor was recomputed from the metric with
a Christoffel/Riemann/Ricci/Einstein library written for this audit (`[∇_μ,∇_ν]V^ρ = R^ρ_{σμν}V^σ`,
`R_{μν}=R^λ_{μλν}`, signature `(+,−,−,−)`, `x⁰=ct`). Every printed number was recomputed in
numpy/scipy from the constants the chapter states. No result below was recalled.*

---

## Verdict

The physics core is correct and, in the places that matter most, exactly correct: the thirteen FLRW
Christoffels, $G_{00}$, $G_{rr}$, Friedmann I with every factor of $c$, the acceleration equation and
its dependence on substituting Friedmann I, the coefficient **and sign** of
$-8\pi Ga^{2}/3c^{2}$ in the Bianchi combination, $\nabla_\mu T^{\mu\nu}=0$, the constant-curvature
ODE and its integration constant, $\rho\propto a^{-3(1+w)}$, all three $a(t)$, the Einstein-static
solution and its $\ddot\varepsilon=+\Lambda c^{2}\varepsilon$ instability including the claimed
identical vanishing at $O(\varepsilon^0)$ and $O(\varepsilon^1)$, the null-geodesic redshift, the
radiation-era Kretschmann scalar $\tfrac32(ct)^{-4}$, and all three worked constructions (closed-dust
cycloid, $\sinh^{2/3}$, de Sitter static patch) reproduce with residual **exactly zero** in sympy.
Four defects are substantive: the chapter's own thesis in §6.3 runs Noether's theorem backwards and
leaves uncollected the converse the book proved in 1.4 §7.2; §4.4 invokes the $t_0<1/H_0$ bound on a
universe whose $p\ge0$ hypothesis it violates; the §4.5 figure caption tells the reader to do
something and predicts the wrong result; and one printed intermediate in Worked example 2 is
arithmetically wrong (0.5325 for 0.5586).
Everything else is minor: sixteen items, mostly miscitation and ⚑ scope, none of which propagates
into a wrong physical result.

**Counts: 0 BLOCKER · 4 MAJOR · 16 MINOR.**

---

## §1 Errors

### MAJOR 1 — §4.4 applies the age bound to a universe that violates its stated hypothesis

**Current string** (unique, `src/ch3-9.html`):

```
comfortably inside the bound $1/H_{0}=14.5\ \mathrm{Gyr}$ that
```

**Corrected string:**

```
below $1/H_{0}=14.5\ \mathrm{Gyr}$ — a coincidence rather than a guarantee, because
```

…and continue `<a class="eqref" href="#e-agebound"></a>` with new text rather than the word
"guaranteed", e.g.:

> …below $1/H_{0}=14.5\ \mathrm{Gyr}$ — a coincidence rather than a guarantee, because
> <a class="eqref" href="#e-agebound"></a> assumed $p\ge0$ and this universe is $68.5\%$
> cosmological term, for which $p\lt0$. Push $\Omega_{\Lambda}$ above $0.737$ at fixed flatness and
> $t_{0}$ exceeds $1/H_{0}$: the bound is real, and this universe is not one of the universes it
> covers.

**Why.** §3.2 derives the bound with the hypothesis stated in its own words:

```
For any fluid with $\rho\gt0$ and $p\ge0$, <a class="eqref" href="#e-friedII"></a> gives
$\ddot a\lt0$
```

The concordance model has $\Omega_{\Lambda}=0.685$, i.e. $p=-\rho_{\Lambda}c^{2}<0$, so $\ddot a>0$
today (the chapter itself computes that the expansion has been accelerating since $z=0.63$). The
bound is therefore not available. It is also not *nearly* available — it fails at realistic parameter
values:

```
  Om=0.315, OL=0.685:  H0 t0 = 0.9510   ->  t0 < 1/H0
  Om=0.2,   OL=0.8:    H0 t0 = 1.0760   ->  t0 > 1/H0
  Om=0.1,   OL=0.9:    H0 t0 = 1.2779   ->  t0 > 1/H0
  Om=0.05,  OL=0.95:   H0 t0 = 1.4899   ->  t0 > 1/H0

  H0 t0 = 1 exactly at Om = 0.2629, OL = 0.7371
```

(from $H_{0}t_{0}=\tfrac{2}{3\sqrt{\Omega_\Lambda}}\,\mathrm{arsinh}\sqrt{\Omega_\Lambda/\Omega_m}$,
the chapter's own <a href="#e-age">(e-age)</a>.)
The margin between the measured $\Omega_{m}=0.315$ and the failure point $0.263$ is about seven
standard deviations of the quoted $\pm0.007$ — but a bound is not a hypothesis test, and the chapter
says "guaranteed".

The same overreach appears one section earlier and should be repaired with it. Current (line 498,
single line, unique):

```
bracket, is the argument that a universe of ordinary matter has a beginning, and §4.4 puts a number on
```

Corrected (the trailing `it.</p>` on the next line becomes part of the replacement):

```
bracket, is the argument that a universe of ordinary matter has a beginning. Section 4.4 computes
the age of the real one, which contains a fluid this argument excludes, and gets an answer that
happens to satisfy the bound anyway.</p>
```

---

### MAJOR 2 — §6.3 runs Noether's theorem in the direction it does not run, and the book's own converse goes uncollected

**Current string** (unique):

```
So there is no conserved total energy of an expanding universe, and the reason is that a
```

with its continuation `theorem handed no hypothesis returns no conclusion.</strong></p>`.

**Corrected string:**

```
So no conserved energy can be produced this way. And the theorem runs backwards as well, which
is what turns that into a negative result rather than a shrug: Chapter 1.4 §7.2 proved the
converse — a conserved $Q$ with no explicit time dependence satisfies $\{Q,H\}=0$ and therefore
<em>is</em> a symmetry, viewed as a generator. A conserved energy would generate a
time-translation symmetry, that symmetry would be a timelike Killing vector, and §6.2 proved
there is none. <strong>So there is no conserved total energy of an expanding universe, and it is
the converse, not the failure of the forward theorem, that says so.</strong>
```

**Why the current text does not follow.** The chain as printed is:

1. Noether: (continuous symmetry) ⟹ (conserved charge).
2. In curved spacetime the symmetry is a timelike Killing vector (3.5 §9).
3. FLRW has none (§6.2, and §6.2 *is* a valid proof — see the verification log).
4. ∴ "there is no conserved total energy".

Step 4 does not follow from 1–3. Denying the antecedent of an implication licenses nothing about the
consequent; the honest conclusion of 1–3 is "this construction yields nothing", which is exactly what
the chapter's own next clause says ("a theorem handed no hypothesis returns no conclusion") — and
that clause is *weaker* than the sentence it is offered as the reason for. §6.5 then leans on the
strong reading explicitly:

```
<em>"Energy is always conserved, you have to look harder"</em> is false, because §6.2 is a proof
and not an admission of ignorance.
```

which requires the converse and does not have it.

The book has the missing piece and this chapter never picks it up. `src/ch1-4.html` §7.2, *"The
converse, and why it is not decorative"*:

> Suppose $Q$ is conserved and has no explicit time dependence. Then $0=\dv{Q}{t}=\{Q,H\}$, and
> therefore the transformation $Q$ generates does this to the Hamiltonian: $\delta H=\epsilon\{H,Q\}
> =-\epsilon\{Q,H\}=0$. … So $Q$ is not merely *produced* by a symmetry; $Q$ **is** a symmetry,
> viewed as a generator. **There is nothing left to prove in either direction.**

With §7.2 in hand the argument closes. Without it, the chapter's thesis section asks the reader to
supply the move the book promises never to make them supply. The `Tools you'll need` line should gain
`§7.2 for the converse` alongside its existing `<a href="ch1-4.html">Chapter 1.4</a> §4.3, the honest
note, and §1 for Noether's theorem itself`.

*Scope note, worth one sentence in the text.* §7.2's converse is a statement about a Hamiltonian
system on phase space. Carrying it to "the total energy of the universe" is a further step the book
does not take (it has no Hamiltonian formulation of GR). §6.5's tiers do the honest work — tier two's
"there is no boundary term to collect" and tier three's "not asymptotically anything" are what
actually rule out a global energy — so the §6.3 sentence should point at them rather than claim more
than §6.2 delivers.

---

### MAJOR 3 — §4.5 figure caption predicts the wrong curve for the slider setting it names

**Current string** (unique):

```
Now pull $\Omega_{\Lambda}$ to zero: the late curve straightens onto the $\tfrac23$ guide and stays
```

**Corrected string:**

```
Now press <b>matter only, critical</b>, which sets $\Omega_{\text{m}}=1$: the late curve straightens onto the $\tfrac23$ guide and stays
```

and the following sentence, currently `there forever. Push $\Omega_{\text{m}}$ above $1$ with
$\Omega_{\Lambda}=0$ and the curve`, should gain the missing case:

```
there forever. Press <b>no $\Lambda$</b> instead, which leaves $\Omega_{\text{m}}=0.315$ and
therefore $\Omega_{k}=0.685$: the late slope does <em>not</em> settle on $\tfrac23$ but climbs
towards $1$, because §4.3's curvature term falls only as $a^{-2}$ and outlasts matter. Push
$\Omega_{\text{m}}$ above $1$ with $\Omega_{\Lambda}=0$ and the curve
```

**Why.** The caption says three lines earlier that $\Omega_{k}$ is *computed*, not set
(`$\Omega_{k}=1-\Omega_{\text{r}}-\Omega_{\text{m}}-\Omega_{\Lambda}$ computed rather than set`), and
the `no Λ` button is `setAll(0.315, 0.000)` — an **open** universe with $\Omega_{k}=0.685$, whose late
behaviour is $a\propto t$, not $t^{2/3}$. I re-ran the figure's own integrator (same $H_0$, same
radiation head, same trapezoid, same $\pm0.05$ log-slope estimator):

```
Omega_L = 0, Omega_m = 0.315 (Ok=0.685 computed):
   a=1     slope=0.8036
   a=2     slope=0.8521
   a=5     slope=0.9085
   a=8     slope=0.9312

Omega_m=1, Omega_L=0 (Einstein-de Sitter):
   a=1     slope=0.6666      a=2  slope=0.6666
   a=5     slope=0.6666      a=8  slope=0.6666
```

So "straightens onto the $\tfrac23$ guide and stays there forever" is a true description of the
**matter only, critical** preset and a false description of the **no Λ** preset. The caption also
opens with "Nothing is drawn by hand", which makes the mis-prediction worse: the reader will do the
thing and see the other thing.

*Everything else in that caption checks out*, from the same integrator:
`slope=0.5003` at $a=10^{-6}$ ("reads $0.500$ to three figures" ✓), `0.6654` at $a=0.1$ ("settles
near $0.66$, approaching $\tfrac23$ from below" ✓), `0.6528` at $a=10^{-2}$ (the familiar-callout's
"reads $0.653$ rather than $0.667$" ✓), and the $\Omega_{m}=2$, $\Omega_{\Lambda}=0$ run halts at
$a/a_{0}=1.98$, i.e. the $a_{\max}=2a_{0}$ that Problem 1(d) derives ✓. Slope at $a=1$ is `0.9506`
and crosses $1$ at $a\approx1.2$, so "near the present it climbs past $1$" is fair.

---

### MAJOR 4 — Worked example 2(d): the printed integrand at $z'=1$ is wrong

**Current string** (unique):

```
0.685\big)^{-1/2}=0.5325
```

**Corrected string:**

```
0.685\big)^{-1/2}=0.5586
```

**Why.**

```
  0.315*8+0.685 = 3.205      sqrt = 1.7902513789968157
  (0.315*8+0.685)**-0.5      = 0.5585807734779455
  what would give 0.5325?  1/0.5325^2 = 3.5266  (not 3.205)
```

The value 0.5325 corresponds to no combination of the chapter's own parameters. It does not
propagate — the final integral is computed elsewhere — but a chapter whose stated discipline is
"every number gets its arithmetic on the page" (MATHPLAN §0 item 9) cannot print an arithmetic step
that is wrong.

---

### MINOR 5 — §2.4 attributes the three-torus to a chapter that used the cone, and calls the cone the torus's two-dimensional version

**Current strings** (both unique):

```
The counterexample is Chapter 3.4 §8's, one dimension up.
```
```
version, a cone, and observed that flatness away from the apex did not make it a plane
```

**Corrected:**

```
The counterexample is one Chapter 3.4 §8 pointed here for.
```
```
version of the same mismatch, a cone, and observed that flatness away from the apex did not make it a plane
```

**Why.** `src/ch3-4.html` §8's counterexample is the cone, not a torus, and it forwards the closed-flat
case here rather than supplying it:

> The topological caveat is not a technicality. Chapter 3.3's Problem 1 built a cone, whose
> curvature vanishes at every point away from the apex … **Chapter 3.9 meets the same distinction on
> cosmological scales, where a universe can be flat everywhere and still closed.**

And a cone is not a two-dimensional three-torus. They are different objects with different defects:
the cone is flat only away from an apex, carries a conical deficit ($2\pi kR$ circumference), and its
punctured region fails to be simply connected; the flat 3-torus is complete, everywhere flat,
compact, and fails only because non-contractible loops exist. `src/ch3-3.html` Problem 1(c) is
$f(u)=ku$, the cone — correctly cited — but it is not the object the paragraph is drawing a parallel
to.

---

### MINOR 6 — "the fourth time" contradicts Chapter 3.5's explicit count

**Current strings** (both unique):

```
it is the fourth time this book has
```
```
is the fourth appearance in this book of a local fact failing to determine a global one
```

**Corrected:** `the fifth time this book has` / `is the fifth appearance in this book of a local fact
failing to determine a global one`.

**Why.** `src/ch3-5.html` §4.3 counts four **before** this chapter and then says this chapter is the
next one:

> the same distinction has now appeared **four times** in this book — the curl-free field with a
> non-zero circulation, the divergence-free field with no potential, Chapter 3.4 §8's cone that is
> flat everywhere and yet not a plane, and [the angle one-form] … **Chapter 3.9 meets it once more**,
> on a universe that can be flat everywhere and still closed.

Four + once more = five.

---

### MINOR 7 — the radiation equation of state is cited to Chapter 3.6 §1.3 three times; it is §1.4

**Current strings:**

```
equation of state $p=\rho c^{2}/3$;
```
(in the `Tools you'll need` line, where the preceding clause correctly cites §1.3 for the perfect
fluid — split the citation)

```
<b>Radiation</b> has $w=1/3$, which that same section derived from the tracelessness of the
```

```
tracelessness of $T^{\mu\nu}_{\text{EM}}$, 3.6 §1.3
```

**Corrected:** in the Tools line, `…$-pg^{\mu\nu}$ and §1.4 for the radiation equation of state
$p=\rho c^{2}/3$;`; in §4.1, `which Chapter 3.6 §1.4 derived from the tracelessness of the`; in the
table, `tracelessness of $T^{\mu\nu}_{\text{EM}}$, 3.6 §1.4`.

**Why.** `src/ch3-6.html` §1.3 is *"Dust, and then a fluid with pressure"* and ends before the
radiation result. The derivation is §1.4(iii), *"Three consequences worth naming before we start"*:

> **(iii) A gas of radiation has a fixed pressure.** Chapter 2.6 §10 built the electromagnetic
> energy–momentum tensor and its closing summary recorded that it is traceless … $p=\rho c^{2}/3$ …
> which is derived rather than quoted: the equation of state of light follows from the tracelessness
> of its stress tensor and from nothing else.

(The attribution of the traceless $T^{\mu\nu}_{\rm EM}$ to Chapter 2.6 is right — 3.6 says §10 of 2.6.)

---

### MINOR 8 — §5.5's density contrast for a human body is an order of magnitude out

**Current string** (unique):

```
the Solar System, vastly more; of your body, about $10^{30}$ times.
```

**Corrected:** `the Solar System, vastly more; of your body, about $10^{29}$ times.`

**Why.** With the chapter's own $\rho_{c,0}=8.53\times10^{-27}\ \mathrm{kg\,m^{-3}}$ and a body
density of $10^{3}\ \mathrm{kg\,m^{-3}}$:

```
  body density 1000 / rho_c = 1.17191e+29
```

---

### MINOR 9 — $z\approx1100$ is used twice and never flagged

The last-scattering redshift is quoted at line 1089 (`the microwave background, at $z\approx1100$`)
and line 1411 (`$z\approx1100$, that is $a/a_{0}=1/1101$`), and is load-bearing for §6.4's headline
"$99.91\%$ of the energy … has gone" and for Worked example 1(c)'s horizon angle. It is not derived
anywhere in this book — it needs recombination physics (Saha) that Part IV has not reached — and it
carries no ⚑. Under the ⚑ contract ("a chapter with no ⚑ is claiming to have built everything it
spends, and that claim must be true") it needs one. Simplest repair: add
`$z\approx1100$ ⚑, which is a measurement of when the plasma recombined and is not derived here` at
first use, or fold it into the §4.4 concordance callout, which is already ⚑.

---

### MINOR 10 — Birkhoff's "interior counterpart" is attributed to a section that does not contain it, and is not flagged

**Current string** (unique):

```
and its interior counterpart says a spherical shell
```

`src/ch3-7.html` §4 proves only the exterior statement; the words *interior*, *shell* and *cavity* do
not occur anywhere in that chapter. The interior result (the vacuum region inside a spherical shell
is flat) is a genuine additional theorem. Either flag it — `⚑ its interior counterpart, quoted, says
a spherical shell` — or drop the GR half and lean on the Newtonian statement the same paragraph
correctly cites (`Chapter 0.7 §8`, whose Worked example does derive "a hollow shell, having no
enclosed charge, exerts no force anywhere inside it. That is Newton's shell theorem").

---

### MINOR 11 — Worked example 2(d)'s integral is 0.765, not 0.766

**Current string** (unique): `numerically the integral is $0.766$, so`

Recomputed with scipy `quad`, using exactly the chapter's integrand:

```
  int_0^1: 0.764679    Om(1+z)^3+OL (chapter's stated integrand)
  int_0^1: 0.764584    + radiation
  int_0^1: 0.764117    + radiation + Ok=0.001
```

So `0.765`. Downstream: $d=0.765\times4.448=3.40$ Gpc $=11.09$ Gly (printed 3.41 / 11.1, both fine
after rounding), and $\dot d=0.765\,c$ — the two later occurrences of `0.766` should move with it.

---

### MINOR 12 — Worked example 1(c) describes the wrong integration range for the 0.28 Gpc

**Current string** (unique, line 1760):

```
being the recent $\Lambda$ era. The same integral run only as far as last scattering gives the
```

The displayed integral immediately above runs in $z$ from $0$ to $\infty$; "run only as far as last
scattering" in that variable means $\int_{0}^{1100}$, which is the **13.9 Gpc** the sentence then
contrasts against. The 0.28 Gpc is $\int_{1100}^{\infty}$ (equivalently $\int_{0}^{t_{\rm ls}}c\,\dd
t/a$). Suggested: `The same integral with its lower limit moved to last scattering gives the`.

Both numbers are right:

```
  comoving particle horizon at z=1100 [Gpc]     = 0.278265   printed 0.278
  comoving distance to z=1100 [Gpc]             = 13.8661    printed 13.87
  recomputed theta [deg]                        = 1.14981    printed 1.15
```

---

### MINOR 13 — §6.4's "no local energy density for gravity" argument drops a hypothesis

**Current string** (unique):

```
Any candidate local energy density built from the metric and its first derivatives is therefore zero
```

**Corrected:**

```
Any candidate local energy density built from the metric and its first derivatives, and required to
vanish in flat spacetime, is therefore zero
```

**Why.** At the chosen event the locally inertial coordinates give $g=\eta$, $\partial g=0$, so a
candidate $f(g,\partial g)$ takes the value $f(\eta,0)$ — a *constant*, not automatically zero. It is
zero only because one demands that an energy density of the gravitational field vanish where there is
no gravitational field. That is a physical requirement and the chapter's own discipline says to name
it. The conclusion is correct as it stands.

---

### MINOR 14 — the closing brick's ⚑ sits in front of results this chapter derived

**Current string** (unique):

```
unchanged. ⚑ With the measured parameters the universe is $13.8\ \mathrm{Gyr}$ old, began
```

The $13.8\ \mathrm{Gyr}$ and $z=0.63$ are *derived* in §4.4 from the quoted inputs; only the inputs
are quoted. Suggested: `unchanged. With the ⚑ measured parameters the universe is $13.8\
\mathrm{Gyr}$ old, began` — moving the flag onto the parameters, which is where the debt is.

---

### MINOR 15 — §5.5's ⚑ spans a clause the book derived

**Current string** (unique):

```
orbits and galaxies do not grow. ⚑ The cosmological term does exert a small outward tendency on a bound
```

The flagged sentence's second half (`Chapter 3.6's Problem 4(b) computed where it starts to matter —
around $100\ \mathrm{pc}$`) is derived, and I confirmed it in `src/ch3-6.html` Problem 4(b)
("about $3\times10^{18}\ \mathrm{m}$, roughly $100$ parsecs"). Only the first clause — that $\Lambda$
perturbs a bound orbit at all, which needs Schwarzschild–de Sitter and is nowhere in the book — is
unpaid. Re-scope the flag to that clause.

---

### MINOR 16 — §3.5's "not remotely long enough" leaves out the move that makes it true

**Current string** (unique):

```
$200\ \mathrm{Gyr}$ — long, and not remotely long enough, since the universe is a fifteenth of that
```

The supporting clause reads, on a first pass, as an argument for the opposite conclusion: if the
instability takes 200 Gyr to develop and the universe is 13.8 Gyr old, the instability has *not* had
time. The operative point is that the Einstein universe was proposed as an **eternal** one, for which
any finite e-folding time is fatal, and 200 Gyr is fifteen universe-ages, which is nothing on that
scale. One clause fixes it, e.g. `— long, and not remotely long enough for a universe that was
supposed to last forever, since`.

The arithmetic in that passage is right: $\ln(10^{9})=20.72$, so $\approx20\tau$; $\tau=10.08$ Gyr,
so $20\tau=202$ Gyr; $13.80/202=1/14.6$.

---

### MINOR 17 — §5.1 writes $h\nu=p_{\mu}u^{\mu}$ as an equality where Chapter 3.8 was careful to write $\propto$

`src/ch3-8.html` §5.1 writes `$h\nu(r)\;\propto\;p_{\mu}u^{\mu}$`, because $p^{\mu}=\dd
x^{\mu}/\dd\lambda$ fixes the four-momentum only up to the affine parameter's normalisation. §5.1
here defines $p^{\mu}=\dd x^{\mu}/\dd\lambda$ and then writes `$h\nu \;=\; p_{\mu}u^{\mu}$`. Nothing
downstream uses more than the proportionality, so no result changes; either restore `\propto` or add
"with $\lambda$ normalised so that $p^{0}=E/c$".

---

### MINOR 18 — Problem 1(d) points at "the definition below (e-omegasum)"; the definition is above it

`by the definition below <a class="eqref" href="#e-omegasum"></a>` — $\Omega_{k}\equiv-kc^{2}/a^{2}H^{2}$
is defined in the sentence that *introduces* that equation, not after it. Read `at` for `below`.

---

### MINOR 19 — §6.5's "three claims … Each can now be checked" does not map onto Chapter 1.4's three

`src/ch1-4.html` §4.3's three ⚑ claims are (1) no time-translation symmetry ⟹ no total energy, (2)
the local statement survives but cannot be integrated, (3) asymptotically flat spacetimes have an ADM
mass. §6.5's three tiers are (1) the local statement, (2) why it cannot be added up, (3) ADM. So
1.4's claim (1) is answered in §6.2–6.3 rather than in the tier list, and 1.4's claim (2) is split
across two tiers. The sentence `Each can now be checked` should say which tier answers which claim,
or say that the first was settled in §6.2.

---

### MINOR 20 — "Twenty-five chapters" is not a number either plan supports

**Current string** (unique): `Twenty-five chapters, after nine spent`

`PLAN.md` gives Part IV 8 ch, Part V 9 ch, Part VI 7 ch → **24**. `PLAN-FORWARD.md` §§5–7 give 11, 11
and 8 → **30**. The claim is checkable only once those parts exist; flagging it now so it does not
ossify.

---

## §2 Gaps in the chain

### G1 — the converse of Noether's theorem (see MAJOR 2)

**Where it goes:** §6.3, immediately before the sentence beginning `So there is no conserved total
energy`. **Line to insert:**

> And the implication runs the other way too, which is what makes this a negative result rather than
> a silence. Chapter 1.4 §7.2 proved the converse: a conserved $Q$ with no explicit time dependence
> satisfies $\{Q,H\}=0$, and the transformation $Q$ generates therefore leaves $H$ alone — so $Q$ is
> not merely produced by a symmetry, it *is* one. A conserved energy would generate a
> time-translation symmetry; that symmetry would be a timelike Killing vector; §6.2 proved there is
> none. The absence is therefore established and not merely unproved.

Add `§7.2 for the converse` to the `Chapter 1.4` entry in `Tools you'll need`.

### G2 — §2.1 asserts that the time dependence factors out as a single $a^{2}(t)$

The line `by homogeneity, the same geometry on every slice up to an overall time-dependent factor` is
supported only by the sentence after (e-split), which argues that a non-scale difference between
slices would define a position-dependent quantity. That is a good heuristic and it is doing real
work; one line makes it a step.

**Where it goes:** §2.1, after `and there are no position-dependent quantities here.` **Line to
insert:**

> Concretely: §2.2 shows each slice is a three-geometry of constant curvature $K$, and §2.3 shows
> that any two such geometries with the same sign of $K$ differ only by an overall constant factor.
> The slice at time $t$ is therefore the slice at time $t_{0}$ rescaled, and $a^{2}(t)$ is the ratio.

### G3 — the $K>0$ chart stops at $r=1/\sqrt K$ and nothing says so

$\ee^{-2\beta}=1-Kr^{2}$ vanishes at $r=K^{-1/2}$, so (e-flrwspatial) is a chart on half a
three-sphere and the label $r$ turns round at the equator. §2.3 asserts that the $k=+1$ slices *are*
three-spheres without ever noting that the coordinate the derivation produced does not cover one.
Given that Chapter 3.8 spent a whole section on exactly the distinction between a chart failing and a
geometry failing, this is the one place in the chapter where the reader has been trained to expect
the remark and does not get it.

**Where it goes:** §2.3, after `for $k=+1$ the slices are three-spheres and $a$ is their radius`.
**Line to insert:**

> One coordinate caution, of the kind Chapter 3.8 §6 taught you to expect. For $k=+1$ the factor
> $1-r^{2}$ vanishes at $r=1$, where the areal label has reached the largest sphere and starts
> shrinking again; the substitution $r=\sin\chi$ covers the whole three-sphere with $\chi\in[0,\pi]$
> and shows that nothing happens to the geometry there. The chart gives out; the sphere does not.

### G4 — §6.2 proves the theorem for dust and states it for "an expanding universe containing matter"

Step 2 restricts to dust (`Take the dust case, which is the universe from $z\approx3400$ until
recently`) and the QED line correctly says `every Killing vector of an expanding **dust** universe is
spacelike`. §6.3 then says `Section 6.2 proved there is none` for the general case, and the warn
callout generalises in words (`What kills it is expanding while containing something that dilutes`)
without a computation. The general case is easy and the chapter already has the ingredient.

**Where it goes:** §6.2, at the end of Step 2. **Line to insert:**

> For a mixture the same conclusion follows from the same scalar: by
> <a class="eqref" href="#e-Rtrace"></a>, $R$ is constant in time only if $\rho-3p/c^{2}$ is, and by
> <a class="eqref" href="#e-rhoscale"></a> a sum of fluids with different $w$ has
> $\rho-3p/c^{2}=\sum_{i}(1-3w_{i})\rho_{i,0}(a/a_{0})^{-3(1+w_{i})}$, which is constant while $a$
> changes only if every $w_{i}=-1$. That is the exception the callout below names, and there are no
> others.

### G5 — the ⚑ debt on $z\approx1100$ (see MINOR 9)

**Where it goes:** §5.1, at the first use. **Line to insert:** `⚑ that the microwave background was
released at $z\approx1100$ is a measurement of when hydrogen recombined, and this book does not
compute it.`

---

## §3 Numerical audit

Constants used are the chapter's own where it states them ($G=6.674\times10^{-11}$,
$1\,\mathrm{Mpc}=3.0857\times10^{22}$ m, $1\,\mathrm{Gyr}=3.156\times10^{16}$ s,
$c=2.99792458\times10^{8}$, $\hbar=1.054572\times10^{-34}$,
$GM_{\odot}=1.32712440018\times10^{20}$, $GM_{\oplus}=3.986004418\times10^{14}$,
$m_{p}=1.673\times10^{-27}$).

| quantity | printed | recomputed | inputs used | agrees? |
|---|---|---|---|---|
| $H_{0}$ in $\mathrm{s^{-1}}$ | $2.184\times10^{-18}$ | $2.18427\times10^{-18}$ | $67.4$ km/s/Mpc, Mpc | ✓ |
| $1/H_{0}$ | $4.578\times10^{17}$ s; $14.51$ Gyr | $4.57819\times10^{17}$; $14.506$ | above, Gyr | ✓ |
| $3H_{0}^{2}$ | $1.431\times10^{-35}$ | $1.43131\times10^{-35}$ | $H_{0}$ | ✓ |
| $8\pi G$ | $1.677\times10^{-9}$ | $1.67736\times10^{-9}$ | $G$ | ✓ |
| $\rho_{c,0}$ | $8.53\times10^{-27}$ kg m$^{-3}$ | $8.5331\times10^{-27}$ | above | ✓ |
| $\rho_{c,0}$ in H atoms m$^{-3}$ | $5.1$ | $5.10$ | $m_{p}$ | ✓ |
| $a/a_{0}$ at r–m equality | $2.9\times10^{-4}$ | $2.9206\times10^{-4}$ | $\Omega_{r}/\Omega_{m}$ | ✓ |
| $z_{\rm eq}$ | $\approx3400$ | $3422.9$ | $\Omega_{r}=9.2\times10^{-5}$, $\Omega_{m}=0.315$ | ✓ (to the stated "≈") |
| $a/a_{0}$ at m–$\Lambda$ equality | $0.77$ | $0.7719$ | $\Omega_{m},\Omega_{\Lambda}$ | ✓ |
| $z$ at m–$\Lambda$ equality | $0.30$ | $0.2956$ | as above | ✓ |
| $a/a_{0}$ at acceleration onset | $0.61$ | $0.6126$ | $(\Omega_m/2\Omega_\Lambda)^{1/3}$ | ✓ |
| **$z$ at acceleration onset** | **$0.63$** | **$0.6323$** | as above | **✓** |
| $\sqrt{\Omega_\Lambda/\Omega_m}$ | $1.475$ | $1.47465$ | $\Omega$'s | ✓ |
| $\mathrm{arsinh}(1.475)$; ln arg | $1.181$; $3.257$ | $1.18062$; $3.2564$ | — | ✓ |
| $\sqrt{\Omega_\Lambda}$ | $0.828$ | $0.82765$ | — | ✓ |
| **age $t_{0}$, $H_{0}=67.4$** | **$4.35\times10^{17}$ s $=13.8$ Gyr** | **$4.3538\times10^{17}$; $13.795$** | (e-age), $\Omega_m,\Omega_\Lambda,H_0$ | **✓** |
| age, exact 4-component integral | — | $13.782$ Gyr | + $\Omega_r,\Omega_k$ | ✓ (consistent) |
| **age, $H_{0}=73.0$** | **$12.7$ Gyr** | **$12.737$** | same $\Omega$'s, $H_0=73.0$ | **✓** |
| $H_{0}$ tension in $\sigma$ | "about five times" | $5.6/\sqrt{0.5^2+1^2}=5.01$ | $67.4\pm0.5$, $73.0\pm1.0$ | ✓ |
| $c/H_{0}$ | $1.37\times10^{26}$ m $=4.45$ Gpc | $1.37251\times10^{26}$; $4.448$ | $c,H_0$ | ✓ |
| $\sqrt{\Lambda}$ | $1.05\times10^{-26}$ m$^{-1}$ | $1.04881\times10^{-26}$ | $\Lambda=1.1\times10^{-52}$ | ✓ |
| **Einstein-static $\tau=1/c\sqrt\Lambda$** | **$3.2\times10^{17}$ s $\approx10$ Gyr** | **$3.180\times10^{17}$ s $=10.08$ Gyr** | $c,\Lambda$ | **✓** (chapter prints "≈10"; 10.1 is the two-figure value) |
| $20\tau$ | $200$ Gyr | $201.5$ | $\tau$ | ✓ |
| CMB energy density $u_{0}$ | $4.1\times10^{-14}$ J m$^{-3}$ | $4.140\times10^{-14}$ | $\Omega_\gamma=5.4\times10^{-5}$, $\rho_c$ | ✓ (cross-check $aT^{4}$ at 2.7255 K: $4.175\times10^{-14}$) |
| energy in comoving box at $z=1100$ | $4.5\times10^{-11}$ J | $4.558\times10^{-11}$ | $1101\,u_0$ | ✓ |
| fraction of CMB energy lost | $99.91\%$ | $99.9092\%$ | $1-1/1101$ | ✓ |
| $r_{s}(M_\odot)$ | $2953$ m | $2953.25$ | $GM_\odot$, $c$ | ✓ (matches ch3-7) |
| $A=4\pi r_{s}^{2}$ | $1.096\times10^{8}$ m² | $1.0960\times10^{8}$ | $r_s$ | ✓ |
| $\ell_{P}^{2}=\hbar G/c^{3}$ | $2.612\times10^{-70}$ m² | $2.61216\times10^{-70}$ | $\hbar,G,c$ | ✓ |
| **$S_\odot/k_{B}=A/4\ell_{P}^{2}$** | **$1.05\times10^{77}$** | **$1.04894\times10^{77}$** | above | **✓** |
| $M_{\odot}=GM_\odot/G$ | $1.99\times10^{30}$ kg | $1.9885\times10^{30}$ | $GM_\odot,G$ | ✓ |
| protons in $M_\odot$ | $1.19\times10^{57}$ | $1.18858\times10^{57}$ | $m_p$ | ✓ |
| $S/k_{B}$ per nucleon | "about $10^{20}$" | $8.8\times10^{19}$ | above | ✓ |
| $t_{P}=\sqrt{\hbar G/c^{5}}$ | $5.4\times10^{-44}$ s | $5.391\times10^{-44}$ | $\hbar,G,c$ | ✓ |
| $\ell_{P}$ | $1.6\times10^{-35}$ m | $1.6162\times10^{-35}$ | — | ✓ |
| Earth-surface curvature | $1.7\times10^{-23}$ m$^{-2}$ | $1.715\times10^{-23}$ | $GM_\oplus$, $R_\oplus=6.371\times10^{6}$ | ✓ (matches ch3-4 §4.5) |
| curvature radius | $2\times10^{11}$ m | $2.41\times10^{11}$ | above | ✓ at one figure |
| $(1.7\times10^{-23})(5.3\times10^{-11})^{2}$ | $4.8\times10^{-44}$ | $4.7753\times10^{-44}$ | as printed | ✓ |
| $Gm_{p}^{2}$ | $1.87\times10^{-64}$ | $1.86801\times10^{-64}$ | $G,m_p$ | ✓ |
| $e^{2}/4\pi\epsilon_{0}$ | $2.31\times10^{-28}$ | $2.30668\times10^{-28}$ | $e$, $8.988\times10^{9}$ | ✓ |
| gravity/EM for two protons | $8.1\times10^{-37}$ | $8.098\times10^{-37}$ | above | ✓ |
| **body density / $\rho_c$** | **$10^{30}$** | **$1.17\times10^{29}$** | $10^{3}$ kg m$^{-3}$, $\rho_c$ | **✗ MINOR 8** |
| **particle-horizon integral** | **$3.18\,c/H_{0}$** | **$3.17998$** | $\Omega_r,\Omega_m,\Omega_\Lambda$ | **✓** |
| $d_{\rm ph}$ | $14.1$ Gpc $=46$ Gly | $14.144$ Gpc $=46.13$ Gly | above | ✓ |
| $3ct_{0}$ | $41$ Gly | $41.39$ | $t_0=13.80$ | ✓ |
| horizon at last scattering | $0.28$ / $0.278$ Gpc | $0.27827$ | $\int_{1100}^{\infty}$ | ✓ |
| comoving distance to last scattering | $13.9$ / $13.87$ Gpc | $13.8661$ | $\int_{0}^{1100}$ | ✓ |
| horizon angle | $0.020$ rad $=1.15^{\circ}$ | $0.020043$ rad $=1.1484^{\circ}$ | ratio above | ✓ |
| $H_{\Lambda}=H_{0}\sqrt{\Omega_\Lambda}$ | $1.808\times10^{-18}$ | $1.80780\times10^{-18}$ | $H_0,\Omega_\Lambda$ | ✓ |
| de Sitter event horizon | $5.4$ Gpc $=17.5$ Gly | $5.374$ Gpc $=17.53$ Gly | $c/H_\Lambda$ | ✓ |
| event horizon with matter | $16.7$ Gly | $16.679$ | $\int_{-1}^{0}\dd z/E$ | ✓ |
| **WE2 integrand at $z'=1$** | **$0.5325$** | **$0.55858$** | $(0.315\cdot8+0.685)^{-1/2}$ | **✗ MAJOR 4** |
| WE2 integral $0\to1$ | $0.766$ | $0.76468$ | $\Omega_m,\Omega_\Lambda$ | ✗ MINOR 11 (last digit) |
| WE2 $d$ | $3.41$ Gpc $=11.1$ Gly | $3.401$ Gpc $=11.09$ Gly | above | ✓ after rounding |
| WE2 $\sinh^{2}$, $\sinh$, arsinh | $0.2719$, $0.5214$, $0.5004$ | $0.271825$, $0.521369$, $0.500243$ | $\Omega_\Lambda/\Omega_m$, $a/a_0=\frac12$ | ✓ |
| WE2 $t(z=1)$ | $1.845\times10^{17}$ s $=5.85$ Gyr | $1.84475\times10^{17}$; $5.845$ | $H_\Lambda$ | ✓ |
| WE2 lookback; fraction | $7.95$ Gyr; $42\%$ | $7.950$; $42.4\%$ | $t_0-t$ | ✓ |
| WE2 $z$ where $\dot d=c$ | $\approx1.5$ | $1.482$ | integral $=1$ | ✓ |
| WE2 integral to $z=7$ | $1.98$ | $1.98068$ | as above | ✓ |
| P1(d) lifetime $2\pi/H_{0}$ | $91$ Gyr | $91.13$ | $2\pi\times14.506$ | ✓ |
| P1(d) present age $(\pi/2-1)/H_{0}$ | $0.571\times14.51=8.3$ Gyr | $0.5708\times14.506=8.28$ | — | ✓ |
| P2(d) peculiar velocity at $10a_{0}$ | $37$ km s$^{-1}$ | $37$ | $370/10$ | ✓ |
| figure slope at $a=10^{-2}$ | $0.653$ | $0.6528$ | figure's own integrator | ✓ |
| figure slope at $a=10^{-6}$ | $0.500$ | $0.5003$ | as above | ✓ |
| **figure late slope, $\Omega_\Lambda\to0$** | **$\to2/3$** | **$0.908$ at $a=5$, $\to1$** | $\Omega_m=0.315$, $\Omega_k=0.685$ | **✗ MAJOR 3** |

Every number in the table depends on the chapter's own stated inputs, and every disagreement above
is in the input-independent arithmetic rather than in a convention.

---

## §4 Verification log — what came back clean

**Tensors, computed from the metric with nothing assumed.**

The FLRW connection reproduced exactly, and the count is right:

```
  Gam^0_{rr}   = a a'/(1-k r^2)        Gam^0_{thth} = r^2 a a'
  Gam^0_{phph} = r^2 a a' sin^2(th)    Gam^r_{0r} = Gam^th_{0th} = Gam^ph_{0ph} = a'/a
  Gam^r_{rr}   = k r/(1-k r^2)         Gam^r_{thth} = -r(1-k r^2)
  Gam^r_{phph} = -r(1-k r^2) sin^2(th) Gam^th_{rth} = Gam^ph_{rph} = 1/r
  Gam^th_{phph} = -sin(th)cos(th)      Gam^ph_{thph} = cot(th)
COUNT (symmetric pairs once) = 13
```

Grind box B's "**Thirteen** non-zero components, counting each symmetric pair once" ✓. Its two
pause-worthy remarks check too: no $\Gamma^{i}{}_{00}$ appears at all (§5.3's "comoving worldlines are
geodesics"), and $-(a'/a)g_{rr}=aa'/(1-kr^{2})=\Gamma^{0}{}_{rr}$, so $\Gamma^{0}{}_{ij}=-(a'/a)g_{ij}$ ✓.

Ricci, scalar and Einstein tensor all match grind box B term for term:

```
  R_{00} = -3 a''/a
  R_{rr} = (2k + a a'' + 2 a'^2)/(1-k r^2)
  R_{thth} = r^2 (2k + a a'' + 2 a'^2)      R_{phph} = R_{thth} sin^2
  R      = -6 (a a'' + a'^2 + k)/a^2
  G_{00} = 3(k + a'^2)/a^2
  G_{rr} = -(k + 2 a a'' + a'^2)/(1-k r^2)
  G_{thth}, G_{phph} = same bracket times -r^2, -r^2 sin^2
```

off-diagonal Ricci identically zero ✓.

**Friedmann I, with every factor of $c$.** $T_{00}=\rho c^{2}$, $T_{rr}=pa^{2}/(1-kr^{2})$,
$u_{\mu}u^{\mu}=c^{2}$ all confirmed. $G_{00}=\kappa T_{00}$ gives
$3(k+a'^{2})/a^{2}=8\pi G\rho/c^{2}$; multiplying by $c^{2}/3$ and using $a'=\dot a/c$ (so
$c^{2}a'^{2}=\dot a^{2}$) gives $(\dot a/a)^{2}=8\pi G\rho/3-kc^{2}/a^{2}$ exactly. This is the place
the brief warned a factor of $c$ goes missing, and it does not: the chapter's $a'\equiv\dd
a/\dd x^{0}=\dot a/c$ is used consistently in (e-G00), (e-eq11), (e-eq11b), grind box C and (e-fluid).

**The $11$ component needs Friedmann I.** Verified as an algebraic identity, not a remark:

```
target11 - (2a*II + I) = 0
```

i.e. the $rr$ field equation is exactly $2a\,\mathrm{II}+\mathrm{I}=0$, so it yields $\mathrm{II}$
(the acceleration equation) only after $\mathrm{I}$ is subtracted. The chapter's claim
"**The substitution was not optional**" is a theorem, not rhetoric.

**The Bianchi combination — constant and sign.**

```
dI/dx0 - 2a' II  =  8 pi G a (c^2(-a rho' - 3 rho a') - 3 p a')/(3 c^4)
ratio to fluid eq = -8*pi*G*a(x0)**2/(3*c**2)
claimed          = -8*pi*G*a(x0)**2/(3*c**2)
MATCH: True
```

Exactly $-\tfrac{8\pi Ga^{2}}{3c^{2}}$ times $\rho'+3(a'/a)(\rho+p/c^{2})$, sign included. Grind box
C's four lines were each checked by hand against this and each is right.

**$\nabla_{\mu}T^{\mu\nu}=0$.**

```
  nabla_mu T^{mu 0}  = (c^2 a rho' + 3 c^2 rho a' + 3 p a')/a
  nabla_mu T^{mu r}  = 0     nabla_mu T^{mu th} = 0     nabla_mu T^{mu ph} = 0
  nu=0 divided by fluid eq: c**2
```

So the $\nu=0$ component is $c^{2}\times$ the fluid equation and the spatial components vanish
identically — both claims in grind box C's parenthetical and in §6.5's tier one ✓.

**The constant-curvature classification.** The three-geometry's connection and Ricci reproduce grind
box A exactly ($\tilde R_{rr}=2\beta'/r$, $\tilde R_{\theta\theta}=\ee^{-2\beta}(r\beta'+\ee^{2\beta}-1)$).
The ODE $\ee^{-2\beta}\beta'=Kr$ is what (e-ricciiso) reduces to; sympy's own `dsolve` returns
$\beta=\tfrac12\ln\!\big(-1/(C_{1}+Kr^{2})\big)$, i.e. $\ee^{-2\beta}=-Kr^{2}-C_{1}$, which is the
chapter's (e-betasol) with $C_{1}=2C$ — so the integration is honest and complete, not a guess
verified after the fact. The integration constant is disposed of legitimately: regularity at $r=0$ is
a physical demand (a deficit there would make one point special in a space assumed to have none), it
is stated as such, and it fixes $-2C=1$ uniquely. The result satisfies the full four-index condition,
with the trig simplified properly:

```
3-geom: R_ijkl = K(g_ik g_jl - g_il g_jk)  ->  violations: []
Ricci scalar: 6*K
R_{ii} - 2K g_{ii} = 0 for all i
```

so grind box A's consistency check and its parenthetical claim ($\tilde R=6K$, full four-index
condition) are both true. The $\theta\theta$ arithmetic in the grind box ($\beta'=Kr/(1-Kr^2)$,
$\ee^{2\beta}-1=Kr^{2}/(1-Kr^{2})$, product $=2Kr^{2}$) is right line by line.

**The Einstein static universe, by perturbing — the chapter really does integrate.** Chapter 3.6
Problem 4(d) promised in writing that "Chapter 3.9 §3 shows the same thing by integrating the
equations rather than arguing from them", and it does. All three claims confirmed symbolically, with
$a=a_{E}(1+\varepsilon)$, $\rho_{m}=2\rho_\Lambda(a_E/a)^3$, $p=-\rho_\Lambda c^{2}$:

```
acceleration eq expanded in eps:
   order e^0: 0
   order e^1: eps'' - 8 pi G rho_L eps / c^2   ->  eps'' = Lambda eps  (primes)
                                              ->  eps.. = Lambda c^2 eps  (dots)   [PLUS sign]
Friedmann I orders (k=+1, a_E = 1/sqrt(Lambda)):
   e^0: 0
   e^1: 0                       <-- vanishes IDENTICALLY, as claimed
   e^2: c^2 eps'^2/(8 pi G rho_L) - eps^2   ->  eps.^2 = Lambda c^2 eps^2
```

So: $\rho_{m}=2\rho_\Lambda$ from the vanishing bracket ✓; $k=+1$ forced (the left side is $0$ and
$8\pi G\rho_\Lambda>0$, so $kc^{2}/a^{2}>0$) ✓; $a_{E}=c/\sqrt{8\pi G\rho_\Lambda}=1/\sqrt\Lambda$ ✓;
$\ddot\varepsilon=+\Lambda c^{2}\varepsilon$ ✓; the $O(\varepsilon^{0})$ **and** $O(\varepsilon^{1})$
terms of Friedmann I vanish identically ✓; and the insight-callout's second-order result
$\dot\varepsilon^{2}=\Lambda c^{2}\varepsilon^{2}$ is exactly right and is exactly what
$\varepsilon\propto\ee^{t/\tau}$ with $\tau=1/c\sqrt\Lambda$ satisfies ✓. The stated first-order
coefficient $-3\rho_{m}+2(\rho_{m}+\rho_\Lambda)=-\rho_{m}+2\rho_\Lambda$ is right.

**$\rho\propto a^{-3(1+w)}$ and the three $a(t)$.** The separation, the exponent
$(3+3w)/2$, and $a\propto t^{2/[3(1+w)]}$ all check; $w=0\Rightarrow t^{2/3}$,
$w=\tfrac13\Rightarrow t^{1/2}$, $w=1\Rightarrow t^{1/3}$, and $w=-1$ correctly handled separately
with $H_\Lambda=\sqrt{8\pi G\rho_\Lambda/3}=c\sqrt{\Lambda/3}$ ✓.

**Cosmological redshift from a null geodesic.** Every step reproduces: $\Gamma^{0}{}_{00}=
\Gamma^{0}{}_{0i}=0$ from the computed connection; $\Gamma^{0}{}_{ij}p^{i}p^{j}=-(a'/a)g_{ij}p^ip^j$;
the null condition gives $g_{ij}p^ip^j=-(p^{0})^{2}$; hence $\dd p^{0}/\dd\lambda=-(a'/a)(p^{0})^{2}$
and, after the chain-rule trade, $p^{0}\propto1/a$ ✓. The second route (crest counting) genuinely
shares no step with the first, as claimed. **Nothing about the source's motion is assumed** — the
derivation assumes only that emitter and observer are comoving ($u^{\mu}=(c,0,0,0)$ at both ends),
and §5.2's warn callout states that hypothesis explicitly and correctly contrasts it with the Doppler
and gravitational cases.

**Kretschmann scalar in the radiation era.**

```
Kretschmann (general k): 12((k + a'^2)^2 + a^2 a''^2)/a^4
Kretschmann (k=0):       12[(a''/a)^2 + (a'/a)^4]
radiation era a ~ (x0)^{1/2}:  K = 3/(2 x0^4)
chapter claims 3/2 (ct)^-4:    difference = 0
```

Exactly the chapter's $K=\tfrac32(ct)^{-4}$ ✓, and it is not constant, so §6.2's Step 2 stands for the
radiation era as claimed.

**Trace of the field equation.** $g^{\mu\nu}G_{\mu\nu}=-R$, $T=\rho c^{2}-3p$, hence
$R=-\tfrac{8\pi G}{c^{2}}(\rho-3p/c^{2})$ — and I confirmed this is what my computed $R$ becomes
on-shell:

```
R on-shell = 8 pi G(-c^2 rho + 3 p)/c^4     target = -8 pi G (rho - 3p/c^2)/c^2     MATCH: True
```

$R=0$ for radiation ✓; $R=-4\Lambda$ for pure $\Lambda$ ✓ (Problem 3(c)'s
$-32\pi G\rho_\Lambda/c^{2}$ ✓).

**§6.2's proof is valid.** Step 1 ($\mathcal{L}_\xi g=0\Rightarrow\xi^{\mu}\partial_\mu S=0$ for every
scalar built covariantly from $g$) is correct; Step 3's division by $\dd R/\dd x^{0}\neq0$ is licensed
by the dust monotonicity; and $\xi^{0}=0$ with $g_{0i}=0$ and a negative-definite spatial block gives
$\xi\cdot\xi<0$, spacelike by 2.3 §4's classification ✓. The Lie-derivative expansion quoted from 3.5
§8.1 matches that file verbatim, and (e-Ltime)'s $\partial_{0}(-a^{2}\tilde g_{ij})=-2aa'\tilde
g_{ij}$ is right. The de Sitter exception is real, is correctly identified as the one place Step 2
fails, and Problem 3 exhibits it. The chapter is right to say the exception is worth more than the
theorem.

**The three worked constructions, residuals exactly zero.**

```
PROBLEM 3 — de Sitter static patch
  static pullback - FLRW radial part: 0
  angular: rbar^2 = e^{2Ht} r^2 : 0
  book's dtbar formula matches: 0        book's drbar formula matches: 0
  g_tbar tbar = f c^2, root at rbar = ±c/H

PROBLEM 1 — closed dust cycloid
  residual  adot^2 - (C/a - c^2) = 0
  a_max = a(eta=pi) = C/c^2               lifetime t(2pi) = pi C/c^3

WORKED EXAMPLE — sinh^{2/3} for flat matter+Lambda
  residual with C = 8 pi G rho_m0 a0^3/3, H_L = sqrt(8 pi G rho_L/3): 0
```

Problem 1(d)'s chain ($\Omega_k=-1\Rightarrow a_{0}=c/H_{0}$, $C=2H_{0}^{2}a_{0}^{3}$,
$a_{\max}=2a_{0}$, lifetime $2\pi/H_{0}$, $\eta=\pi/2$ now, $t_{0}=(\pi/2-1)/H_{0}$) is right at every
step, and the figure's `closed, recollapsing` preset independently halts at $a/a_{0}=1.98$, which is
the same $a_{\max}=2a_{0}$. Problem 2's $Q=-a^{2}u^{X}$, $|p|=m|Q|/a$ and the $v\to c$ match are all
correct. Problem 4's Newtonian Friedmann, the $2\mathcal{E}=-kc^{2}$ identification, the missing
pressure term and the sign error for $w=-1$ all check.

**Hypotheses.** The cosmological principle is stated as an assumption and never as a theorem (§1.1,
§1.2's ⚑ callout, §1.3, and the plain-terms box all say so, and §1.1 correctly notes that isotropy
about every point implies homogeneity but not conversely). Comoving coordinates are fixed by the
matter's own four-velocity and the chapter says what fixes them and why the privileged slicing
belongs to a solution rather than to the theory (§1.3). The perfect fluid is written in the comoving
frame and the frame is named, with the normalisation checked against $g_{00}=1$. The perturbative
order in §3.5 is stated and the expansion used ($(1+\varepsilon)^{-3}\approx1-3\varepsilon$) is
adequate for the first-order result it is used for. §5.2's warn callout is the model of the practice
the book wants: three shift mechanisms, each with its hypotheses, and an explicit statement that
route (a) of 3.8 §5.1 is *unavailable* here for the reason §6 is about.

**⚑ discipline, mostly right.** All twelve flags were read in place. The $H_{0}$ tension is presented
as an open disagreement with both explanations named and neither preferred ("either one of the
measurements has a systematic error nobody has found, or the model … is wrong somewhere. Both remain
live"), the TRGB value near 70 is included, and the arithmetic is repeated with both values — this is
exactly what MATHPLAN item 11 asked for and it is not smoothed over. Inflation, nucleosynthesis,
structure formation and dark matter are named and pointed at in a single ⚑ callout that says
explicitly "none of them is derived here", and none is quietly developed or quietly asserted
elsewhere in the chapter; the four appear only as labels attached to results the chapter *did* derive
($n\ge1$ removes the horizon; $a\propto t^{1/2}$ sets nucleosynthesis rates; $10^{-5}$ perturbations
on FLRW; $\Omega_{m}\approx0.26$). $S=A/4$ is flagged twice and its debt stated precisely (what is
owed, why GR's own answer is zero, who collects). The three defects in flag placement are MINORs 9,
14 and 15.

**Promises and citations.** All three collected promises are verbatim-accurate:

- `src/ch1-1.html` §2 ("Energy"): "in an expanding universe the laws *are* time-dependent, and the
  energy of the cosmological photon gas is correspondingly *not* conserved … A quantity whose
  conservation you have been taught is absolute turns out to be contingent on a symmetry that the
  universe does not exactly possess." — quoted correctly in both the `where` callout and §6.3.
- `src/ch1-4.html` §4.3 ("An expanding universe: no conserved total energy"): "Chapter 3.5 makes this
  precise: the symmetries of a spacetime are its *Killing vector fields*, a conserved energy requires
  a timelike one, and the expanding solutions of Chapter 3.9 do not have one." — quoted correctly.
- `src/ch3-5.html` closing brick: "Chapter 3.9 uses the absence of a timelike Killing vector to
  explain why energy is not conserved in an expanding universe, collecting Chapter 1.4 §4.3's honest
  note." — quoted correctly, and §3.5's §9 really does prove the four-line result the chapter says it
  proves (§9.1 "The four-line derivation", §9.2 "The same result as Noether's theorem").

Also verified as landing where claimed: 3.2 §1.1's "a question to be answered rather than assumed"
(exact), 3.6 §4.5's Gibbons–Hawking–York quotation (exact, with a legitimate ellipsis), 3.6 §6.3 and
Problem 4(d)'s "shows the same thing by integrating the equations rather than arguing from them"
(exact), 3.6 §5.5's "a gas of light gravitates twice as strongly … Chapter 3.9 needs that" and its
$\nabla^{2}\Phi=4\pi G(\rho+3p/c^{2})$, 3.6 §6.1(iii)'s "its density is constant … because $\lambda$
is a constant", 3.6 §7.2's constraint-versus-evolution count, 3.6 Problem 4(b)'s ~100 pc, 3.5 §8.1's
Lie-derivative formula and practical test, 3.5 §6.4's divergence identity, 3.5 §4.3's forward
pointer, 3.4 §5.2's Riemann count, 3.4 §5.3's locally inertial coordinates, 3.4 §4.5's
$1.7\times10^{-23}\ \mathrm{m^{-2}}$, 3.4 §8's ⚑ converse, 3.3's Problem 1 cone, 3.7's
$r_{s}=2953$ m, 3.7 §§1–5, 3.8 §1.1, §5.1's contraction rule, §6.4's invariant, §7.1's tortoise
coordinate, §8.2's Planck-length statement, 2.3 §4's causal classification, 2.5 §7's Doppler, 0.2
§5's improper integrals, 0.5 §6 and §8, 0.6's Problem 3 ("$S_{\max}=\ln N$ is Boltzmann's
$S=k_{B}\ln W$"), 0.7 §8's shell theorem, 0.8 §2.1's separation of variables, 1.2 §5's
$\ee^{\ii S/\hbar}$ and its forward pointer to 5.8, 1.4 §§1–3 and §4.3, GAPS.md §6's
"one deliberate loose thread", and PLAN-FORWARD §4.2's flat-spacetime announcement. The three
miscitations found are MINORs 5, 7 and 10.

**Structure and style.** One `where`, one `brick` whose last paragraph is led by the bolded
**Where this gets spent.**, two `familiar`, six `warn` (each opening ⚑ or ⚠), two `insight`, seven
`plain`; nine `<h2>` matching MATHPLAN's fixed section list exactly; numbered `N.M` sub-headings
throughout. No forbidden hedge appears (the three hits for "just" are "nothing adjusted", "can be
justified" and the standard brick title). "The reader" appears zero times. No "stress-energy", no
"Minkowski space". No dangling `eqref`: every `#e-…` target exists, and every `<a href="chN-M.html">`
points at a file present in `src/`. Chapters 4.8, 5.8, 7.1, 7.8 and 7.9 are correctly plain text.

---

## §5 Things I could not verify

1. **Future-chapter numbering.** `Chapter 7.9` (entropy count), `Chapter 7.8` (cosmological constant)
   and `Chapter 5.8` (path integral for fields) are consistent with `GAPS.md`, `MATHPLAN-3.7-3.9.md`
   and `src/ch1-4.html`/`src/ch1-2.html` respectively, but `PLAN.md` gives Part VII only eight
   chapters (no 7.9) and `PLAN-FORWARD.md` puts the path integral at 5.6 with 5.8 as the Feynman
   rules. This chapter follows the newer documents and the existing chapters; the inconsistency is
   book-wide, not local. Same for "Twenty-five chapters" (MINOR 20).

2. **The de Sitter static-patch claim about *which* Killing vector.** I verified the coordinate
   transformation, the metric, $\xi\cdot\xi=fc^{2}$ and its null surface at $\bar r=c/H$ exactly. I
   did **not** verify the stronger implicit claim that this is the *only* region of de Sitter with a
   timelike Killing vector, nor the claim that "Minkowski spacetime and the Einstein static universe
   … are the other exceptions" is an exhaustive list. Both are true as far as I know, and the
   Einstein-static case is consistent with §6.2's mechanism (nothing dilutes, so no scalar varies),
   but exhaustiveness is not established in the chapter and I did not establish it.

3. **The observational inputs**, by construction: $T_{\rm CMB}=2.7255$ K, the $10^{-5}$ isotropy, the
   $370\ \mathrm{km\,s^{-1}}$ dipole, the ~100 Mpc homogeneity scale, the Planck and SH0ES $H_{0}$
   values and their uncertainties, $\Omega_{k}=0.001\pm0.002$, the split of $\Omega_{m}$ into 0.05
   baryons and 0.26 dark matter, the globular-cluster ages, the electron $g-2$ agreement to
   $10^{-13}$, and the SZ-based isotropy-from-elsewhere argument. All are ⚑ or attributed. I checked
   only their *internal* consistency, which holds: $\Omega_{\gamma}=5.4\times10^{-5}$ reproduces
   $aT^{4}$ at 2.7255 K to 1%; $\Omega_{r}/\Omega_{\gamma}=1.70$ is the standard neutrino factor;
   $\Lambda=1.1\times10^{-52}\ \mathrm{m^{-2}}$ reproduces $\Omega_{\Lambda}=0.685$ at $H_{0}=67.4$
   ($1.09\times10^{-52}$ computed).

4. **The interactive's rendering.** I re-ran the figure's numerical scheme (solver, radiation head,
   log-linear interpolation, slope estimator) and its four presets in Python, which is what MAJOR 3
   rests on. I did not run the drawing code, so claims about axes, guides and readout formatting are
   unchecked.

5. **The $\Lambda$ value's flag status on re-use.** §3.5 and §7.3(iv) use
   $\Lambda\approx1.1\times10^{-52}\ \mathrm{m^{-2}}$ without a local ⚑, attributing it to Chapter
   3.6 §6.3, where it *is* flagged ("⚑ Two numbers, quoted as observations"). Whether the book's
   contract requires a re-flag on re-use is a policy question `CONVENTIONS.md` does not settle, so I
   have not filed it as an error.

6. **Whether §7.2's account of the string-theory entropy count is accurate in detail** — the brane
   counting, weak-to-strong-coupling continuation, and "the factor of four included and nothing
   adjusted". It is ⚑ and explicitly outside the book; I did not check it against the literature.
