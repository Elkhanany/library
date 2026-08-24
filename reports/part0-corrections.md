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
