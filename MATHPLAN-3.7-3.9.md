# Chapters 3.7 – 3.9: derivation plan

*Part III, completed. Three chapters, none of them a dedicated mathematics chapter — every tool
they need already exists, which is the point. This is where Part III gets paid.*

*Everything below is **derived in the text**. Items marked ⚑ are the only permitted exceptions and
must be flagged in place. `MATHPLAN-3.md` §0's eight pacing rules are binding here unchanged; three
additions are in §0 below.*

---

## 0 · Pacing — three additions for these three chapters

`MATHPLAN-3.md` §0 items 1–8 stand. What is different about 3.7–3.9 is that the reader has arrived
somewhere they have been walking towards for eight chapters, and the failure mode changes with it.
In 3.3 and 3.4 the risk was that the machinery was opaque. Here the machinery is built and the risk
is the opposite: that the famous results arrive so fast the reader does not notice they have
personally derived them.

9. **Every number gets its arithmetic on the page.** 43 arcseconds and 1.75 arcseconds are the two
   most famous numbers in general relativity and the reader must produce both, from constants they
   can look up, with the unit conversions visible. A result quoted to three figures with the
   substitution hidden is worth less here than anywhere else in the book.

10. **Say which chapter each tool comes from, at the moment it is used.** These chapters spend the
    whole of Part III. Every time a Killing vector, a Christoffel symbol or the vacuum field
    equation is picked up, name its supplier in the same sentence. This is the payoff structure the
    book has been building and it only works if it is visible.

11. **Distinguish "the coordinates fail" from "the geometry fails", relentlessly.** It is the single
    most-misunderstood idea in this part of physics, the reader has met the machinery to settle it
    (charts in 3.2, invariants in 3.4), and 3.8 exists largely to make the distinction impossible to
    miss.

---

## Conventions

Unchanged from `MATHPLAN-3.md`, with two notes.

- **$G$ and $c$ stay explicit through all three chapters.** `MATHPLAN-3.md` said "through 3.7, then
  note the convention for 3.8"; that was written when Part III was eight chapters. Revised: keep
  them everywhere. The Schwarzschild radius is written $r_{s}=2GM/c^{2}$, never $2M$. Where a
  formula is unbearable, define a dimensionless ratio and say so.
- **Use the standard gravitational parameter $GM$, never $G\times M$.** $GM_{\odot}=
  1.32712440018\times10^{20}\ \mathrm{m^{3}s^{-2}}$ is known to ten significant figures; $G$ alone
  is known to five, and $M_{\odot}$ is *derived* from $GM_{\odot}$ and $G$. Multiplying them back
  together throws away five digits and shifts Mercury's precession by 0.01″ and the solar deflection
  by 0.0004″ — small, but both land on numbers the reader is checking against a measurement. This
  plan's first draft made exactly that error in two places and both writing agents caught it.
  Where the book needs a mass in kilograms for something else, say which quantity is the measured
  one.
- **$x^{0}=ct$** as everywhere else, so $g_{00}$ multiplies $(\dd x^{0})^{2}=c^{2}\dd t^{2}$ and the
  weak-field form $g_{00}\simeq 1+2\Phi/c^{2}$ of 3.6 applies directly. This matters: it is how the
  integration constant is fixed in 3.7 §3.4, and it is where a signature slip would show up.

---

# 3.7 · Schwarzschild: The Solution and Its Orbits

*Solve Einstein's equations for the first time. Then find the orbit Newton has no name for.*

**What this chapter exists to do:** produce an exact solution, in full, with no step taken on
authority — and then extract from it a prediction that is not a small correction to Newton but a
qualitatively new fact, namely that below a certain radius **no circular orbit exists at all**.

**Sections (fixed — forward references point at these numbers):**

| § | Title |
|---|---|
| 1 | What "spherically symmetric and static" buys |
| 2 | The ansatz, and why it has only two unknown functions |
| 3 | Solving $R_{\mu\nu}=0$ |
| 4 | Birkhoff's theorem, and what it says about a collapsing star |
| 5 | Two Killing vectors, two conserved quantities |
| 6 | The effective potential |
| 7 | The innermost stable circular orbit |
| 8 | The orbit equation, and perihelion precession |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Spherical symmetry stated as a statement about Killing vectors, not about pictures: three spacelike Killing fields with the algebra of rotations | **3.5** §8. Static = a timelike Killing field, plus invariance under $t\to-t$ | Say explicitly that *static* is stronger than *stationary*, and that the difference will matter in 3.8 |
| 2 | The metric reduces to $\dd s^{2}=A(r)c^{2}\dd t^{2}-B(r)\dd r^{2}-r^{2}\dd\Omega^{2}$ | item 1; the definition of $r$ as *the areal radius*, i.e. the label for which the sphere at $r$ has area $4\pi r^{2}$ | **The areal-radius definition is the load-bearing move and is a choice.** Say so. $r$ is not "the distance to the centre" and 3.8 §6 will show that reading it that way is what makes the horizon look catastrophic |
| 3 | $\Gamma^{\lambda}{}_{\mu\nu}$ for that metric | **3.3** §7 | Grind box. **Nine** non-zero components — $\Gamma^{0}{}_{01},\Gamma^{1}{}_{00},\Gamma^{1}{}_{11},\Gamma^{1}{}_{22},\Gamma^{1}{}_{33},\Gamma^{2}{}_{12},\Gamma^{2}{}_{33},\Gamma^{3}{}_{13},\Gamma^{3}{}_{23}$ — list them |
| 4 | $R_{\mu\nu}$, diagonal, four equations of which three are independent | **3.4** §6 | Grind box, but the *count* stays in the main text: four functions' worth of equations, two unknowns, and the system is consistent — that is not automatic and is worth a sentence |
| 5 | **$B R_{00}/c^{2}+A R_{11}=0$ collapses to $(AB)'=0$** | item 4 | The whole solution turns on this one line. Verified: the combination is exactly $A B'/(rB)+A'/r$, which is $(AB)'/(rB)$. Show it |
| 6 | $AB=1$ | item 5 plus asymptotic flatness: $A,B\to1$ as $r\to\infty$ | Name the physical input. The constant is fixed by a boundary condition, not by algebra |
| 7 | **$R_{22}=0$ becomes $-rA'-A+1=0$, i.e. $(rA)'=1$** | item 4 with $B=1/A$ | Verified. A first-order linear ODE the reader solved in **0.8** §2. One integration |
| 8 | $A=1+C_{1}/r$ | item 7 | |
| 9 | **$C_{1}=-2GM/c^{2}$**, giving $\displaystyle \dd s^{2}=\Big(1-\frac{2GM}{c^{2}r}\Big)c^{2}\dd t^{2}-\frac{\dd r^{2}}{1-\dfrac{2GM}{c^{2}r}}-r^{2}\dd\Omega^{2}$ | match $g_{00}=1+2\Phi/c^{2}$ with $\Phi=-GM/r$ at large $r$ — **3.6** §7's Newtonian limit | The mass enters as an integration constant fixed by a limit. That is worth naming: nothing in $R_{\mu\nu}=0$ knows about mass |
| 10 | $r_{s}=2GM/c^{2}$; numbers for the Sun (2.95 km), the Earth (8.9 mm), and a $10^{9}M_{\odot}$ hole | item 9 | Put the Earth's 8.9 mm in the main text. It is the number that makes the horizon feel like a real length rather than a symbol |
| 11 | **Birkhoff:** dropping *static* and keeping only spherical symmetry returns the same solution | redo items 3–9 with $A(t,r)$, $B(t,r)$; the $R_{01}$ equation forces $\dot B=0$ and the rest follows | Grind box for the algebra, statement and consequence in the main text: **a spherically symmetric star cannot radiate gravitationally**, and the field outside a pulsating star is static. This also collects 3.4's remark that Ricci-flat is not flat |
| 12 | $E\equiv c^{2}A\,\dd t/\dd\tau$ and $L\equiv r^{2}\dd\varphi/\dd\tau$ conserved | **3.5** §9 (Killing $\Rightarrow$ conserved), applied to the two Killing fields of item 1 | **This is the promise 3.5 §9 made twice and it must be collected by name.** Note the equatorial reduction $\theta=\pi/2$ is legitimate by symmetry, and say why |
| 13 | $\displaystyle\Big(\dv{r}{\tau}\Big)^{2}=\frac{E^{2}}{c^{2}}-\Big(1-\frac{2GM}{c^{2}r}\Big)\Big(c^{2}+\frac{L^{2}}{r^{2}}\Big)$ | normalisation $g_{\mu\nu}u^{\mu}u^{\nu}=c^{2}$ (**2.5**, **3.3**) with item 12 | One line of algebra, fully shown. This is the whole of orbital GR |
| 14 | The effective potential, and the **one new term**: $-GML^{2}/(c^{2}r^{3})$ | item 13, expanded and compared term by term with the Newtonian $-GM/r+L^{2}/2r^{2}$ | Table the comparison. Newtonian barrier, then the GR term that beats it at small $r$. This is where the interactive earns its place |
| 15 | Circular orbits at $\displaystyle r_{\pm}=\frac{L\big(Lc\pm\sqrt{L^{2}c^{2}-12G^{2}M^{2}}\big)}{2GMc}$ | $\dd V/\dd r=0$; the numerator is the quadratic $c^{2}r_{s}r^{2}-2L^{2}r+3r_{s}L^{2}$ | Verified |
| 16 | **No circular orbit exists at all unless $L\ge 2\sqrt3\,GM/c$** | the discriminant of item 15 | Verified. **This is the qualitatively new fact and it should be stated as one**: in Newtonian gravity there is a circular orbit at every radius, and here there is a floor |
| 17 | **The ISCO at $r=6GM/c^{2}=3r_{s}$** | the two roots merging when the discriminant vanishes | Verified. Give the number for a $10 M_{\odot}$ hole (88.6 km) and note this is what sets the inner edge of an accretion disc — the observational hook |
| 18 | The orbit equation $\displaystyle\dv[2]{u}{\varphi}+u=\frac{GM}{L^{2}}+\frac{3GM}{c^{2}}u^{2}$, $u=1/r$ | item 13, differentiated, with $\dd/\dd\tau=(L/r^{2})\dd/\dd\varphi$ | Derive the Newtonian version *first*, in the main text, and show it gives a closed ellipse — the reader met this in **1.4** WE2 (the LRL vector). The GR term is then visibly the only new thing |
| 19 | **$\omega^{2}=1-6G^{2}M^{2}/(c^{2}L^{2})$**, so the orbit closes late | linearise the $u^{2}$ term about the circular value | Verified. Say clearly that this is perturbative and what the small parameter is |
| 20 | **$\Delta\varphi=6\pi GM/(c^{2}p)$ per orbit**, $p=a(1-e^{2})$ | item 19 expanded to first order, with $L^{2}=GMp$ at leading order | Verified. Flag ⚑ that $L^{2}=GMp$ is the Newtonian relation, which is consistent at this order — and say why using it is legitimate |
| 21 | **Mercury: 42.99″ per century** | item 20 with $a=5.7909\times10^{10}$ m, $e=0.20563$, $P=87.969$ d | Verified: **42.98″** against an observed residual of $42.98\pm0.04$. **Every conversion on the page** — radians per orbit, orbits per century, arcseconds. ⚑ the observed residual, which is a measurement |
| 22 | Why Mercury and not the Earth | $\Delta\varphi\propto 1/p$ and orbits per century $\propto P^{-1}$ | One line; it explains the whole history of the problem |

**Interactive (one, and it must earn it):** the effective potential with $L$ on a slider. Newtonian
and GR curves on the same axes. As $L$ falls the two extrema approach; at $L=2\sqrt3\,GM/c$ they
merge and below it the barrier is *gone* and the curve runs monotonically inward. That is a fact
about a function that a static figure cannot show, and it is the chapter's thesis.

**⚑ permitted in 3.7:** the observed Mercury residual; the Eötvös-type inputs already flagged in
3.1; the Newtonian $L^{2}=GMp$ used at leading order in item 20. **Nothing else.** Birkhoff is
derived, not quoted.

---

# 3.8 · Light, Redshift, and What a Horizon Is

*Collect the factor of two Chapter 3.1 confessed. Then take the horizon apart.*

**What this chapter exists to do:** two things the reader has been promised. First, the missing half
of the light deflection, identified as spatial curvature — a debt 3.1 §7.3 called "the register of
debts" and named in writing. Second, the demonstration that $r=r_{s}$ is a failure of a chart and
not of a spacetime, which is the payoff for 3.2's insistence that a manifold is not its coordinates.

**Sections (fixed — forward references point at these numbers):**

| § | Title |
|---|---|
| 1 | Null geodesics, and what changes |
| 2 | The photon sphere |
| 3 | Deflection: the integral, done |
| 4 | Where the missing half was |
| 5 | Gravitational redshift, three ways |
| 6 | The horizon is not where the metric blows up |
| 7 | Eddington–Finkelstein, and crossing |
| 8 | What is actually singular |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The null normalisation $g_{\mu\nu}u^{\mu}u^{\nu}=0$ and the loss of proper time as a parameter | **3.3** §8 | Say plainly what breaks: $\tau$ is not available, an affine parameter is, and $E$ and $L$ individually lose meaning while the ratio $b=L/E$ survives. **This is the same "only the ratio is physical" move as the impact parameter in scattering** |
| 2 | $\displaystyle\Big(\dv{r}{\lambda}\Big)^{2}=\frac{1}{b^{2}}-\frac{1}{r^{2}}\Big(1-\frac{2GM}{c^{2}r}\Big)$, with $b$ the impact parameter | 3.7 item 13 with $c^{2}\to0$ on the right | Show the limit being taken, one line |
| 3 | **The photon sphere at $r=3GM/c^{2}$** | maximise the null effective potential | An unstable circular orbit *for light*, with no Newtonian counterpart at all. Give $b_{\text{crit}}=3\sqrt3\,GM/c^{2}$ and note this is the black-hole "shadow" radius that was imaged |
| 4 | The orbit equation $\displaystyle\dv[2]{u}{\varphi}+u=\frac{3GM}{c^{2}}u^{2}$ | item 2, differentiated | The Newtonian source term is *gone*: light in the zeroth approximation travels in a straight line, $u=\sin\varphi/b$, and the reader should check that this is a straight line in polar coordinates |
| 5 | First-order solution $\displaystyle u=\frac{\sin\varphi}{b}+\frac{3GM}{2c^{2}b^{2}}\Big(1+\tfrac13\cos2\varphi\Big)$ | perturbation about item 4's straight line | Verified: substituting gives residual exactly zero. Grind box for the trig, statement in the text |
| 6 | **Deflection $\displaystyle\alpha=\frac{4GM}{c^{2}b}$** | asymptotes of item 5 at $u\to0$ | Verified |
| 7 | **1.75″ grazing the Sun** | item 6 with $b=R_{\odot}=6.957\times10^{8}$ m | Verified: **1.7512″**. Arithmetic on the page |
| 8 | **The missing half, identified** | compare with 3.1 §7's cabin calculation, which used only $g_{00}$ | **The chapter's central payoff.** Redo the deflection keeping only the $g_{00}$ term and get exactly $2GM/c^{2}b=0.876''$ — Einstein's 1911 value. The other half comes from $g_{rr}$: *space is curved too, and a light ray samples both*. A massive slow particle spends its "motion" almost entirely in the time direction and barely notices the spatial curvature; light divides its motion equally, and gets both halves. **This is the sentence 3.1 promised.** ⚑ the 1919 and modern VLBI measurements |
| 9 | Lensing: multiple images as the conjugate-point phenomenon | item 6, plus **1.2** §5.1 and **2.3** §6.2 on conjugate points | Collects two chapters' promises by name. Keep it qualitative and say so — the lens equation is stated, ⚑, not derived |
| 10 | **Redshift from the metric alone**: $\displaystyle\frac{\nu_{\infty}}{\nu_{\text{em}}}=\sqrt{1-\frac{2GM}{c^{2}r}}$ | the timelike Killing vector of 3.7 §5 — $E$ is conserved along the photon's path while the *locally measured* frequency is not | **Three ways, per `MATHPLAN-3.md` §0 item 8:** (a) conserved $E$ against local proper time; (b) the static-observer argument from $\dd\tau=\sqrt{g_{00}}\,\dd t$; (c) the equivalence-principle cabin from 3.1 §6, recovered as the weak-field limit. Show all three agree |
| 11 | GPS, properly | item 10 combined with the special-relativistic time dilation of **2.2**, in **one metric** rather than two separate small effects | Collects 3.1 §7.2's explicit promise. The numbers: $+45.7\ \mu$s/day gravitational, $-7.2\ \mu$s/day kinematic, $+38.5\ \mu$s/day net. Say why adding is legitimate here — both are $O(10^{-10})$, the cross term is $O(10^{-20})$ |
| 12 | $g_{00}\to0$ and $g_{rr}\to\infty$ at $r=r_{s}$ | inspection | Then **stop and ask the right question**: is that a fact about the spacetime or about the labels? The reader has the tools (3.2 §2, 3.4 §5) and should be asked to guess before being told |
| 13 | **Radial infall reaches $r_{s}$ in finite proper time** but takes infinite coordinate $t$ | integrate item 2's timelike counterpart, twice, once in $\tau$ and once in $t$ | Both integrals in a grind box; the *contrast* in the main text. This is the sharpest possible statement that the two disagree, and only one of them is about the traveller |
| 14 | **The Kretschmann scalar $\displaystyle K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=\frac{48G^{2}M^{2}}{c^{4}r^{6}}$** | **3.4** §5, computed for the Schwarzschild metric | Verified. Grind box for the computation. Then the two evaluations that settle everything: $K(r_{s})=3c^{8}/4G^{4}M^{4}$, **finite**; $K\to\infty$ only as $r\to0$. An invariant cannot be argued with — that is what "invariant" has meant since 2.3 |
| 15 | Tidal force at the horizon $\propto M^{-2}$ | item 14, or the geodesic deviation of **3.4** §7 | Collects 3.1 §7.4's scaling remark by name: a bigger hole is *gentler* at its edge, and for a supermassive hole nothing locally remarkable happens at crossing |
| 16 | **Eddington–Finkelstein coordinates**: $v=ct+r_{*}$, with $r_{*}=r+r_{s}\ln\lvert r/r_{s}-1\rvert$ | constructed, not quoted — build $r_{*}$ by integrating the radial null condition, then define $v$ so that infalling rays are straight lines | The metric becomes $\dd s^{2}=(1-r_{s}/r)\dd v^{2}-2\,\dd v\,\dd r-r^{2}\dd\Omega^{2}$: **manifestly regular at $r_{s}$, degenerate nowhere except $r=0$**. Show the determinant. This is a change of chart, exactly the operation 3.2 §2 defined |
| 17 | The horizon as a **one-way surface**: the light cones tip | item 16; compute the two radial null directions in $(v,r)$ and show that inside $r_{s}$ both have $\dd r<0$ | Do this by calculation, not by picture. The picture then illustrates a result rather than substituting for one |
| 18 | Why the Rindler horizon of **2.3** Problem 3 was the same kind of object | compare: a coordinate-dependent horizon in flat spacetime, removable by a change of chart | Collects 2.3's promise by name. **And then the honest difference:** the Rindler horizon is observer-dependent and Schwarzschild's is not, because the latter is where a *global* causal structure changes, not where one observer's chart gives out. ⚑ the general definition of an event horizon as the boundary of the causal past of future null infinity, which needs machinery this book does not build |
| 19 | $r=0$ is a genuine curvature singularity, and general relativity does not predict what happens there | item 14 | End the chapter here, plainly. ⚑ the singularity theorems, stated with their hypotheses named (**`GAPS.md` §3.6**: energy conditions), not waved at |

**Interactive (one):** the light-cone tipping diagram in Eddington–Finkelstein coordinates — drag a
radius and watch the two null directions rotate, crossing over at $r_{s}$. It shows the one thing
that is genuinely hard to state in words, and it is a *computed* figure, not a drawn one.

**⚑ permitted in 3.8:** the 1919/VLBI deflection measurements; the lens equation; the general
definition of an event horizon; the singularity theorems. **Nothing else.**

---

# 3.9 · Cosmology, and a Loose Thread

*Put the largest possible source on the right-hand side. Then leave one number deliberately unpaid.*

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The cosmological principle as an assumption, and its evidence |
| 2 | The FLRW metric |
| 3 | The Friedmann equations |
| 4 | The three fluids, and what each does to $a(t)$ |
| 5 | Redshift, distance, and what "expanding" does not mean |
| 6 | Energy is not conserved, and why that is Noether rather than a paradox |
| 7 | The loose thread |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Homogeneity and isotropy stated as Killing-vector conditions | **3.5** §8 | ⚑ the observational evidence (CMB isotropy to $10^{-5}$, galaxy surveys). Say clearly that this is an assumption supported by evidence, not a theorem |
| 2 | **The FLRW metric** $\displaystyle\dd s^{2}=c^{2}\dd t^{2}-a^{2}(t)\Big[\frac{\dd r^{2}}{1-kr^{2}}+r^{2}\dd\Omega^{2}\Big]$ | item 1; the three maximally symmetric 3-geometries | Derive the $k$-classification rather than listing it, using the constant-curvature condition from **3.4** §8 |
| 3 | $G_{\mu\nu}$ for FLRW | **3.4** §6, **3.6** §2 | Grind box. Verified: $G_{00}=3(k+a'^{2})/a^{2}$ in units $x^{0}=ct$ |
| 4 | **Friedmann I:** $\displaystyle\Big(\frac{\dot a}{a}\Big)^{2}=\frac{8\pi G\rho}{3}-\frac{kc^{2}}{a^{2}}$ | item 3 with $G_{\mu\nu}=\kappa T_{\mu\nu}$, $\kappa=8\pi G/c^{4}$, perfect fluid from **3.6** §1.3 | Verified in the book's conventions |
| 5 | **Friedmann II** (acceleration) and the fluid equation | the $11$ component; and $\nabla_{\mu}T^{\mu\nu}=0$ | Show that only two of the three are independent — the same "the Bianchi identity already knew" structure as 3.6 |
| 6 | $\rho\propto a^{-3}$ (dust), $a^{-4}$ (radiation), $a^{0}$ ($\Lambda$) | item 5 with $p=0$, $\rho c^{2}/3$, $-\rho c^{2}$ | **Collects 3.6 §1.3's promise** that a gas of light gravitates twice as strongly, and its remark that radiation's extra factor of $a$ is the redshift |
| 7 | $a(t)\propto t^{2/3}$, $t^{1/2}$, $\ee^{Ht}$ | item 4 for each fluid alone | Separable first-order ODEs — **0.8** §2.1 |
| 8 | **The Einstein static universe is unstable** | perturb the $\Lambda$-balanced solution of item 4 | **Collects 3.6 §11's promise by name** — 3.6 argued it from the equations' form, and this integrates them. The pencil on its point |
| 9 | Cosmological redshift $1+z=a_{0}/a_{\text{em}}$ | null geodesics in FLRW — **3.3** §8 | And then say what expansion is *not*: galaxies are not moving through space, and the balloon analogy breaks precisely where the rubber suggests a surrounding volume. Name the break |
| 10 | **Energy is not conserved in an expanding universe** | there is **no timelike Killing vector**, so **3.5** §9 has nothing to work with, so **1.4**'s Noether theorem yields no conserved energy | **The chapter's thesis and the collection point for three separate promises** — 1.1 §5, 1.4 §4.3's "honest note", and 3.5 §9. Present it as a *consequence of a theorem the reader proved*, not as a curiosity. The photon gas loses energy and nothing catches it |
| 11 | ⚑ The concordance parameters | quoted: $H_{0}$, $\Omega_{m}$, $\Omega_{\Lambda}$, with uncertainties, and the $H_{0}$ tension stated as an open disagreement rather than smoothed over | |
| 12 | **The loose thread:** $S=A/4$ in Planck units | ⚑, deliberately | The one number in this book left unpaid on purpose. Say exactly what is owed and where it is collected (**7.9**), and that the derivation needs string theory. `GAPS.md` §6 lists it as the book's one deliberate loose thread |
| 13 | The closing statement of Part III | | Per `PLAN-FORWARD.md` §4.2: tell the reader **now** that Parts IV–VI are done on flat spacetime, that gravity does not reappear until 7.1, and that this is not a cheat but the actual state of physics. This is the one place it can be said before it happens |

---

## What this batch must not do

- **Not renumber anything else.** The split of the old 3.7 into 3.7 and 3.8 pushes cosmology to 3.9
  and nothing further. Every existing reference has been remapped; see the commit that accompanies
  this plan.
- **Not use geometrised units**, even where the algebra is ugly. See Conventions.
- **Not draw the horizon before computing it.** §17 of 3.8 exists so that the famous picture is a
  consequence.
- **Not let 3.9 become a cosmology course.** Inflation, structure formation, nucleosynthesis and
  dark matter are named as existing and pointed at, not developed. The chapter's job is the
  Friedmann equations and the Noether argument.

## Verification required before this batch ships

Every item marked *Verified* above was checked symbolically in sympy while this plan was written:
the Ricci tensor for the general static ansatz, the $(AB)'=0$ collapse, the $(rA)'=1$ integration,
the circular-orbit quadratic and its discriminant, the ISCO at $6GM/c^{2}$, the precession formula
and Mercury's 42.98″, the first-order null solution's exactly-zero residual, the $4GM/c^{2}b$
deflection and its 1.7512″, the Kretschmann scalar $48G^{2}M^{2}/c^{4}r^{6}$ and its finiteness at
$r_{s}$, and $G_{00}$ for FLRW giving Friedmann I.

**The chapters must be checked again independently after they are written**, by an agent that did
not write them, per the standing rule in `reports/README.md`. Three of the errors caught in this
build were in a plan, not in a chapter.
