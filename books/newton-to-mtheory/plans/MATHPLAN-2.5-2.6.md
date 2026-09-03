# Math plan — Chapters 2.5 and 2.6 (completing Part II)

Every item below is **derived in the text**, not quoted. Items marked ⚑ are the only
permitted exceptions and must be flagged in place.

## Chapter 2.5 — Relativistic Dynamics

**Inherited:** interval and $\eta_{\mu\nu}$ (2.3), proper time as path length (2.3),
tensor transformation law + the invariance theorem (2.4), Euler–Lagrange (1.2),
Noether (1.4), Taylor expansion (0.3).

| # | Object built | Derived from |
|---|---|---|
| 1 | $\dd t/\dd\tau=\gamma$ | definition of proper time (2.3) |
| 2 | Four-velocity $u^\mu=\gamma(c,\vv v)$ | differentiate $x^\mu$ by $\tau$, chain rule (0.6) |
| 3 | $u\!\cdot\! u=c^2$ | direct contraction with $\eta$ |
| 4 | Four-acceleration, and $u\!\cdot\! a=0$ | differentiate item 3 — acceleration is always "perpendicular" to velocity |
| 5 | Four-momentum $p^\mu=mu^\mu=(E/c,\vv p)$ | definition + item 2 |
| 6 | **Why $p^\mu$ is the right conserved quantity** | 2.4's theorem: conservation of a *four-vector* in one frame is conservation in all. Three-momentum alone fails this. This is the argument the chapter turns on. |
| 7 | $E=\gamma mc^2$, $E_0=mc^2$ | Taylor-expand item 5 and match the $\tfrac12mv^2$ term |
| 8 | $E^2=p^2c^2+m^2c^4$ | contract $p\!\cdot\! p=m^2c^2$ |
| 9 | Massless case $E=pc$, $v=c$ | set $m=0$ in item 8; derive $\vv v=\vv pc^2/E$ first |
| 10 | Relativistic Lagrangian $L=-mc^2\sqrt{1-\beta^2}$ | *require* Euler–Lagrange to give $\dot{\vv p}=\vv F$ with $\vv p=\gamma m\vv v$, then solve for $L$ |
| 11 | $S=-mc^2\!\int\!\dd\tau$ | rewrite item 10 — **the action is proper time**, closing 2.3's maximisation result |
| 12 | Why $\vv F=m\vv a$ fails | $\vv F$ and $\vv a$ are not parallel; derive longitudinal vs transverse response, then explain why the book refuses "relativistic mass" |
| 13 | Covariant force $\dd p^\mu/\dd\tau=f^\mu$, $f\!\cdot\! u=0$ | item 4 + item 5 |
| 14 | Wave four-vector $k^\mu=(\omega/c,\vv k)$; Doppler | boost $k^\mu$; include **transverse Doppler**, which is pure time dilation and has no classical analogue |
| 15 | Compton scattering | four-momentum conservation, squared to kill the recoil term — the cleanest worked use of item 8, and needed again in 4.1 |
| 16 | Pair-production threshold; Mandelstam $s$ | invariant mass of a system; centre-of-momentum frame (previews 5.7) |
| 17 | Mass defect / binding energy | item 7 applied to a bound system, with real nuclear numbers |

**Figure (one):** the **mass shell**. $E$ against $p$, with a rest-mass slider. The curve is the
hyperbola $E=\sqrt{p^2c^2+m^2c^4}$ — the same geometry as 2.3's invariant hyperbolae, now in
momentum space. As $m\to0$ it degenerates onto the asymptote $E=pc$. Overlay the Newtonian
$E=mc^2+p^2/2m$ and watch it hug the hyperbola near the origin and then diverge badly.

## Chapter 2.6 — Electromagnetism Is Relativity

**Inherited:** everything above, plus $\nabla\cdot,\nabla\times$ and the continuity equation
(0.7), field-version Euler–Lagrange (1.2 §8), the antisymmetric-tensor component count (2.4 §7),
and 2.1's unresolved crisis.

| # | Object built | Derived from |
|---|---|---|
| 1 | Four-current $j^\mu=(c\rho,\vv J)$ | require $\partial_\mu j^\mu=0$ to reproduce 0.7's continuity equation |
| 2 | Four-potential $A^\mu=(\phi/c,\vv A)$ | require $\vv E,\vv B$ in terms of $\phi,\vv A$ to be covariant |
| 3 | $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$, **all six components identified** | write the matrix out; three entries are $\vv E/c$, three are $\vv B$ — the count 2.4 predicted |
| 4 | **Maxwell's four equations become two** | $\partial_\mu F^{\mu\nu}=\mu_0 j^\nu$ (Gauss + Ampère) and $\partial_{[\lambda}F_{\mu\nu]}=0$ (no-monopoles + Faraday). Expand **every component explicitly** — this is the chapter's centrepiece and must not be waved through |
| 5 | Gauge invariance $A^\mu\to A^\mu+\partial^\mu\chi$ | substitute into item 3; connect to 1.2's total-derivative freedom |
| 6 | Lorenz gauge $\Rightarrow \Box A^\mu=\mu_0 j^\mu$ | choose $\partial_\mu A^\mu=0$; recover 2.1's wave equation, now manifestly covariant |
| 7 | Transformation of $\vv E$ and $\vv B$ under a boost | apply 2.4's tensor law to item 3. **What one observer calls magnetic, another calls partly electric** |
| 8 | **The wire** | a lab-neutral current-carrying wire, boosted to the test charge's frame: the two charge densities contract by *different* factors, the wire acquires net charge, and the magnetic force is re-described as electrostatic. Derived quantitatively, to leading order in the drift speed, with the force magnitudes shown to agree |
| 9 | Invariants $F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2/c^2)$ and $\propto\vv E\!\cdot\!\vv B$ | direct contraction; consequence — a light wave has $E\perp B$ and $E=cB$ in **every** frame |
| 10 | Lorentz force covariantly $\dd p^\mu/\dd\tau=qF^{\mu\nu}u_\nu$ | check components against the familiar $q(\vv E+\vv v\times\vv B)$; the time component gives the power |
| 11 | EM Lagrangian $\mathcal L=-\tfrac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu}-j_\mu A^\mu$ | vary it (1.2 §8) and **recover item 4**. This is the template Yang–Mills copies in 6.4 |
| 12 | Stress-energy $T^{\mu\nu}$, Poynting vector, field momentum $\vv g=\epsilon_0\vv E\times\vv B$ | Noether (1.4) applied to item 11 |
| 13 | **Newton's third law repaired** | 1.1 left two moving charges violating it. Show particles + field together conserve $p^\mu$: the missing momentum is *in the field*. Closes the longest-running open promise in the book |

**Figure (one):** **the wire**. Lab frame — equal and opposite line densities, zero net charge, a
test charge moving parallel feels a purely magnetic force. Boost slider to the test charge's rest
frame: the lattice and drift densities contract by different $\gamma$'s, a net charge density
appears, and the readout re-labels the force from magnetic to electric while the **total force is
shown to be unchanged**. That single figure is the chapter's thesis, measured rather than asserted.
