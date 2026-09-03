# Corrections found while converting Part 0 to the plain-language register

Nine agents converted Chapters 0.1–0.9 in place. Converting a chapter means reading every sentence
of it closely, which is why register work keeps turning up content errors that eight earlier
verification passes did not. Every item below was reported by the converting agent, re-verified
independently before being touched, and fixed in a separate pass after the conversion had passed
`registercheck.py`.

Three of the fixes deliberately break a `registercheck.py` invariant, which is the correct behaviour:
the invariants exist to prove a *register* rewrite changed nothing but prose, and these are content
changes made afterwards, on purpose. They are marked **[invariant]**.

## Chapter 0.1 — What a Derivative Really Is

1. **The squeeze triangles.** "Inside the unit circle, compare the areas of a triangle, a circular
   sector, and a larger triangle." The third triangle is the tangent-line triangle of area
   $\tfrac12\tan h$, which necessarily lies *outside* the circle — that is exactly why its area
   exceeds the sector's. Rewritten to name all three areas and say which sits inside which.
2. **"Both go to zero at the same rate."** False wherever $f'(a)=0$: for $f(x)=x^2$ at $a=0$ the
   numerator is $h^2$ and dies strictly faster. What makes the limit exist is that the numerator is
   $O(h)$, no *slower* than the denominator. Corrected in the main text and, since the same wording
   had propagated there, in plain-terms box 0.1.1. **[invariant]**
3. **"Two chapters from here."** Plain box 0.1.5 promises the payoff — multiplying by $\ii$ is a
   rotation by 90° — two chapters on. The main text names the target correctly as Chapter 0.4, and
   `src/ch0-4.html` calls back to "Chapter 0.1's closing observation". That is three chapters on.
   **[invariant]**

## Chapter 0.2 — Integration and Accumulation

4. **Duplicate section number.** Two `<h3>`s were both numbered 1.1. The second is now 1.2, and the
   two live cross-references that meant the second one (the `fig-riemann` figcaption and §4.4's
   remark on odd moments) were repointed. **[invariant]**
5. **Wrong chapter for the propagator.** "(Chapter 5.6)" — 5.6 is *The Path Integral*; the propagator
   is 5.4, *Distributions, Contours, and the Propagator*. The chapter contradicted itself: its own
   grind box and closing brick both say 5.4.
6. **Wrong chapter for complex $b$.** "Chapter 0.4 makes that legitimate" — 0.4 is *Vector Spaces and
   Linear Maps* and contains no complex analysis. Repointed to 5.4, which is where contour
   integration is actually built, and which Chapter 0.9 already names as the only place in the book
   that uses it.

## Chapter 0.3 — Series, Approximation, Orders of Magnitude

7. **"Thirteen significant figures."** $a_e = 1.15965218059(13)\times10^{-3}$ carries twelve. The
   surrounding text was already self-consistent with twelve in two places, so "thirteen" was the
   outlier.

## Chapter 0.4 — Vector Spaces and Linear Maps

8. **"Shares not one entry with $ST$."** With $ST=\begin{pmatrix}3&6\\1&1\end{pmatrix}$ and
   $TS=\begin{pmatrix}5&-2\\1&-1\end{pmatrix}$ the $(2,1)$ entry is $1$ in both. Now "agrees in only
   one of its four entries". §6.1's parenthetical repeated the same overclaim and was fixed with it.
9. **"No entry of $A'$ even appears in $A$."** $A$ and $A'$ both contain $4$. The weaker positional
   claim — nothing stayed in its slot — is true and is what the text now says.

## Chapter 0.5 — Inner Products, Eigenvectors, and the Spectral Theorem

10. **Wrong sign on the phase.** The alternative Cauchy–Schwarz proof said to choose $\varphi$ as the
    argument of $\avg{u,v}$. With $\avg{u,v}=r\ee^{\ii\alpha}$ that gives $r\cos2\alpha$, not $r$.
    It must be *minus* the argument. Verified numerically: for a pair with overlap modulus $0.600$,
    $\varphi=+\arg$ gives $0.102$ and $\varphi=-\arg$ gives $0.600$. The conclusion was never in
    doubt; only the instruction was wrong.

## Chapter 0.6 — Multivariable Calculus

11. **The Higgs potential at the wrong point.** The §6.3 bullet on a vanishing Hessian eigenvalue
    cited the Higgs potential *at the symmetric point*. For $V=-\mu^2\abs\phi^2+\lambda\abs\phi^4$
    the Hessian at $\phi=0$ is $-2\mu^2\delta_{ij}$ — negative definite, a strict maximum, and the
    second-derivative test is not silent there. The zero eigenvalue lives at the broken minimum,
    along the Goldstone direction. The chapter said this correctly in two other places.

## Chapter 0.7 — Fields, Flux, and the Big Theorems

12. **A 3×3 Jacobian with eleven entries.** "three in the trace, three in the curl, and the remaining
    five" sums to 11. The trace is one number: $1+3+5=9$. The "remaining five" depended on the right
    decomposition, so only the first term was wrong.

## Chapter 0.8 — Differential Equations and the Oscillator

13. **"Hence, exactly."** $Q$ is *approximately* the number of radians in which the energy falls by
    $\ee$. Phase advances at $\omega_{\mathrm d}$, not $\omega_0$, so the true count is
    $Q\sqrt{1-1/4Q^2}$; and $E_0\ee^{-2\gamma t}$ is the cycle-averaged energy, not the instantaneous
    one. Correct to one part in $40{,}000$ at $Q=100$ and $13\%$ off at $Q=1$. Both approximations
    are now named, with their size.

## Chapter 0.9 — Fourier, Delta Functions, and Probability

14. **A contour argument attributed to a chapter with no contours.** Worked example 1 justified the
    imaginary contour shift by "the rectangle-contour argument of Chapter 0.4", which is *Vector
    Spaces and Linear Maps*. It also contradicted §7.5, which says Chapter 5.4 is the only place in
    the book that uses complex analysis. The step is now marked ⚑ — quoted here, built in 5.4 —
    which is what it always was. **[invariant]**
15. **A sign flip between a problem and its solution.** Problem 4(b) gives the amplitude as
    $a(t)=\ee^{-\ii\omega_0t}\ee^{-t/2\tau}$; the solution opened by asserting the carrier was
    $\ee^{+\ii\omega_0t}$. The solution now says which sign the problem gives, that it puts the line
    at $-\omega_0$, and that it is taking the other sign deliberately. No number changes.

## Pattern worth noting

Nine of the fifteen are **cross-references** or **arithmetic in prose about equations that are
themselves correct** — the two categories that survive a math review, because a math reviewer checks
the derivation and a language reviewer checks the sentence, and neither is looking at the seam
between them. Items 5, 6, 11, 12 and 14 were each contradicted *by the same chapter* somewhere else,
which suggests a cheap future check: extract every "Chapter N.M" claim and every count-of-things
claim, and look for a chapter that disagrees with itself.

---

# Second pass: `xrefcheck.py` over all thirty chapters

Writing the checker suggested by the pattern above and pointing it at the whole book found sixteen
more mis-aimed references. Three agents audited the 590 distinct (source, target) pairs; every
finding below was re-verified against the target chapter's own text before anything was edited.

None of these is a build error. Every one resolves to a chapter that exists. That is the point: the
reference is a promise about *subject matter*, and no build can check a promise.

## The √-g cluster — four references, one wrong belief

Four chapters send the reader to **3.3** for the invariant volume element. `src/ch3-3.html` contains
zero occurrences of `\sqrt{-g}` and the word "volume" appears in it not once; `src/ch3-5.html` has
twenty-three. Chapter 3.5 §6.2 boxes the result and says in place *"Chapter 0.6 §8.3 told you this
was coming"* — so 3.5 knew, and 0.6 did not.

| where | was | now |
|---|---|---|
| 0.6 §8.3 | "Chapter 3.3 will show it" | 3.5 §6.2 |
| 0.6 closing brick | "Chapter 3.3's $\sqrt{-g}\,\dd^4x$" | 3.5 |
| 0.4 closing brick | "Chapter 3.3, where $\sqrt{-g}$…" | 3.5 |
| 0.7 §3 | "Chapter 3.3 will prove the general formula" | 3.5 §6.4 |

`GAPS.md` §5 already recorded the last of these as *paid in 3.5 §6.4*. It never noticed that 0.7's
prose still named 3.3.

## The rest

- **1.2's ⚑ on the charged-particle Lagrangian** pointed at 2.6, which builds the *field* Lagrangian
  $-\tfrac1{4\mu_0}F_{\mu\nu}F^{\mu\nu}-j_\mu A^\mu$ and never writes
  $\half m\dot{\vv x}^2 - e\varphi + e\vv A\cdot\dot{\vv x}$. That Lagrangian appears in exactly one
  written chapter — 1.3 §9, which writes it and then derives the Lorentz force from it. The ⚑ now
  names 1.3 §9 and says what happens there, so it discharges one chapter later instead of never.
- **2.6's closing brick** sent gauge-bosons-as-string-excitations and the Born–Infeld action to 7.1,
  *Why Quantum Gravity Is Hard*. The other eleven promises naming 7.1 are uniformly about power
  counting and $\ell_P$. Repointed to 7.5 (the spectrum) and 7.7 (D-branes). This one had teeth
  beyond the reader: `debts.py` hands every promise to whoever writes the target chapter, so as it
  stood, 7.1's brief would have arrived carrying a requirement to derive Born–Infeld.
- **3.1** credited 2.2 with the horizon. 2.2 has no horizon; it has the hyperbola, in Problem 4 (not
  a worked example). The Rindler horizon is derived in 2.3's Problem 3, whose title is literally
  *"the accelerated worldline is a hyperbola, and it has a horizon"*. Both fixed.
- **3.2** opened §6 with *"Chapter 0.4 attached to every vector space its dual $V^*$… and proved that
  in $n$ dimensions the dual is also $n$-dimensional."* `src/ch0-4.html` contains no dual space, no
  covector, no linear functional. 0.6 §4 names $V^*$ and defers it; 2.4 §3 builds it. Neither proves
  the dimension — and 3.2 proves it itself four paragraphs later, so the sentence now says that
  instead of claiming it as inherited. A third sentence attributing the dual-basis condition to 0.4
  was fixed with it.
- **3.5 §8.2** said the ten Poincaré generators were what *"Chapter 2.2 obtained by demanding the
  interval be preserved"*. 2.2 mentions neither the Poincaré group nor translations. 2.3 §2 derives
  $\eta_{\mu\nu}\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma=\eta_{\rho\sigma}$ that way and counts six by
  hand in its Problem 4. The four translations appear nowhere in Part II, so the sentence
  over-claimed even against the right chapter. It now credits 2.3 with the six and says the four
  translations are new.
- **4.2** sent the barrier calculation to 4.5. `MATHPLAN-4.md` fixes 4.5's sections and none is a
  barrier; tunnelling is 4.6 §3 and §8. Untracked in `GAPS.md`, and already sitting in `debts.py 4.5`
  as a requirement. → 4.6.
- **4.2** cited 4.4 §9 twice, for two different things. §9 is Stone's theorem (correct); the
  half-line result is §5. → 4.4 §5.
- **1.1 and 1.2** each wobbled between 5.2 and 5.3 for "what Lorentz invariance demands of the
  Lagrangian". Split: Lorentz invariance and locality → 5.2, unitarity → 5.3, in both chapters.
- **0.9** called 5.10's subject renormalisation. 5.10 is *Regularisation*; renormalisation is 5.11,
  and the curriculum splits them deliberately. 0.9's own closing brick already said regularisation.
- **2.5** cited 1.2 §7 for the total-derivative freedom (it is Problem 4) and 2.1 §3 for
  $\omega/k=c$ from Maxwell (it is §2).

## One thing that was not a reference error

Chapter 1.3 invokes *"the inverse function theorem of Chapter 0.6"* twice, and the whole
Legendre-transform argument rests on it. Chapter 0.6 states only the **implicit** function theorem.
The right chapter was named; the theorem was simply never stated anywhere in the book. It is now
stated in 0.6 §8, where the Jacobian is introduced, carrying a ⚑ — the contraction-mapping proof
belongs to a real analysis course — and noting it is equivalent to the implicit function theorem
quoted in §7.

## What this suggests for the remaining thirty-seven chapters

`xrefcheck.py --all` should be run and scanned whenever a part is finished, not only when a
conversion happens to surface something. It costs one agent-hour per part. The failure mode it
catches is invisible to the build, invisible to a math review (which checks the derivation) and
invisible to a language review (which checks the sentence), because it lives in the seam between
them — and, through `debts.py`, a wrong target quietly rewrites a future chapter's brief.
