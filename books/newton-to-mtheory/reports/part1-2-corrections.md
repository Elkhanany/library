# Corrections found while converting Chapter 1.4 and Part II

Seven chapters, 112,531 words of main prose. Every item below was reported by the converting agent,
re-verified independently before being touched, and fixed after the conversion had passed
`registercheck.py`. Two of the fixes deliberately break a registercheck invariant, which is correct:
the invariants prove a *register* rewrite changed nothing but prose, and these are content changes
made afterwards, on purpose. They are marked **[invariant]**.

Seventeen items. Four of them are arithmetic that had survived every previous pass because the
*final* answer in each case was right, or because nothing downstream depended on the number.

## Chapter 1.4 — Noether's Theorem

1. **An off-by-one section reference inside the chapter.** §2.1 says the fixed-$t$ variation "is
   precisely why §2.4, where the transformation moves $t$ as well, needs extra care." §2.4 is *Step 4
   — recognise a total derivative and compare*. The section where the transformation moves $t$ is
   §2.5. `xrefcheck.py` does not catch this class: it validates chapter-level and `eqref` targets,
   not in-chapter `§n.m` prose references.

## Chapter 2.1 — The Crisis of 1900

2. **The 1887 precision of $c$ was overstated as a limitation.** The text said a direct timing
   measurement "would have to resolve one part in $10^{4}$ of a quantity that in 1887 was itself
   known to only about one part in $10^{3}$." The best absolute determination then was Michelson's
   own 1879 figure, $299\,910\pm50\ \mathrm{km\,s^{-1}}$, which is about **two parts in $10^{4}$** —
   an order of magnitude better than claimed. The argument survives and is in fact sharper stated
   correctly: the difference he needed to see was *smaller than the error bar on the whole*, which is
   why he abandoned timing for interference.

3. **A measurement attributed to the wrong experimenter.** "$f=0.437$, and Fizeau measured about
   $0.44$." The figure $0.434\pm0.02$ is **Michelson's 1886 repetition**, not Fizeau's 1851 original,
   which agreed with Fresnel only to within a few per cent. Now says which is which.

4. **Two more citations of "Chapter 2.1 §3" for the wave equation**, this time in `src/ch4-1.html`
   (the transverse-mode counting for the Rayleigh–Jeans derivation). Maxwell produces the wave
   equation in 2.1 **§2**; §3 is *The question nobody could answer*. Fixed in 4.1. This is the third
   and fourth instance of the same mis-citation — 2.5 carried it too and was fixed in the previous
   batch.

## Chapter 2.2 — The Lorentz Transformation, Derived

5. **A satellite number computed at the wrong speed.** §2.5 fixes $v=30\ \mathrm{km\,s^{-1}}$ (the
   Earth's orbital speed), gets $3.3\times10^{-13}\ \mathrm{s}$ of simultaneity error at
   $x=1\ \mathrm{m}$, then says that scaling $x$ to $2\times10^{7}\ \mathrm{m}$ "becomes
   $0.9\ \mathrm{\mu s}$, that is $260\ \mathrm{m}$ of light travel." Scaling $x$ alone gives
   $6.7\ \mathrm{\mu s}$ and $2.0\ \mathrm{km}$. The quoted pair is internally consistent with each
   other but requires $v\approx3.9\ \mathrm{km\,s^{-1}}$ — a GPS satellite's own orbital speed,
   silently substituted mid-sentence. Corrected to $6.7\ \mathrm{\mu s}$ and $2.0\ \mathrm{km}$,
   which makes the point harder rather than softer.

6. **A counting argument that cited a step the chapter never takes.** "Four unknowns. We have three
   conditions, and the fourth is fixed by the fact that an overall rescaling of both frames is not a
   physical transformation." No rescaling argument appears anywhere in the chapter. What actually
   happens is that condition (ii) supplies **two** equations rather than one, because the light pulse
   can be sent in either direction along $x$ and both directions must work — which is exactly what
   §2.2 then does, at `e-Dis` and `e-Eis`. The preamble now says that, and now describes the
   derivation the reader is about to watch.

## Chapter 2.3 — Minkowski Geometry

7. **"The four families they fall into"** introduces a list of **three** bullets ($k>0$, $k<0$,
   $k=0$). Now three.
8. **"Three extra maps… which turn out to be parity and time reversal"** names two things for three.
   The third is the two applied together, which the grind box's own four sign choices make explicit.
9. **Problem 3(a) uses $k$ for the semi-axis rather than the interval.** The accelerated worldline
   sits on $c^2t^2-x^2=-(c^2/a)^2$, so $k=-(c^2/a)^2$ and it is $\sqrt{-k}$ that equals $c^2/a$. The
   solution said "$k=c^2/a$", which contradicts §3's own definition of $k$ two sections earlier.
10. **"The middle case has swollen"** — the three cases are *before, after, simultaneous*, and the
    one that swells is the third, not the middle.

## Chapter 2.4 — Tensors, Honestly

11. **A term count off by a factor of sixteen.** Problem 3's solution says relabelling
    $S^{\mu\nu}A_{\mu\nu}$ "leaves the same $256$ terms in a different order." A double sum over two
    four-valued indices has $16$ terms — which is the $n^2$ the same paragraph claims two sentences
    later. $256=4^4$ is the entry count of a rank-4 array, used correctly for
    $\epsilon_{\mu\nu\rho\sigma}$ in §8.1 and evidently carried over from there.
12. **An over-determination count that does not check.** The ⚠ box said decreeing $N^\mu=(1,0,0,0)$
    in every frame makes "four independent statements where the geometry permitted only one, and the
    extra three are false." Against the chapter's own example the decree conflicts with the predicted
    $(\gamma,-\gamma\beta,0,0)$ in **two** components, not three. Rewritten so the claim is
    checkable: fixing four components in one frame uses up every freedom the object has, and the
    decree then contradicts the transformation law in two of four components in a boosted frame, and
    in *something* in every frame but the original.
13. **Plain-terms box 2.4.8 said the same sentence twice** in consecutive paragraphs — "Each of these
    rules follows directly from what the objects actually are, rather than being imposed for the sake
    of tidiness", then "Each of these rules follows from what the objects are rather than from a
    taste for tidiness". An editing artifact. The first is deleted; the second continues into "and
    each can be re-derived from the transformation law in a line", so it is the one that earns its
    place. **[invariant]**

## Chapter 2.5 — Relativistic Dynamics

14. **A factor of $c$ inside a single definition.** §8.2 defines
    $\vv\beta_{\text{cm}}=\vv P c/P^{0} = c\sum_i\vv p_i/\sum_i E_i$. Since $P^0=\sum_i E_i/c$, the
    left expression evaluates to $c^2\sum\vv p_i/\sum E_i$, which is a velocity, not a $\beta$. The
    two halves of one equation disagree with each other. The right-hand form is correct and is what
    the rest of the section uses, so nothing downstream is affected — which is precisely why it
    survived. Now $\vv P/P^{0}$.

## Chapter 2.6 — The Field Lagrangian

15. **"Four vector equations, twelve-odd scalar equations."** Maxwell's four expand to **eight**
    scalars: $1+3+1+3$. The chapter's own covariant count agrees — §3.2 establishes that
    $\partial_\mu F^{\mu\nu}=\mu_0 j^\nu$ is four and $\partial_{[\lambda}F_{\mu\nu]}=0$ is four —
    so the chapter contradicted itself in the space of one section. Also "four vector equations" is
    loose, since two of the four are scalar equations. Now "Four equations, eight scalar equations".
16. **An unclosed `<p>` in the §5 grind box**, present in the pristine original. HTML5 closes it
    implicitly at the next `<p>`, so it rendered correctly and no check caught it. Closed.

## And one that turned into a check

17. `tagcheck.py` caught a `<` that a browser reads as a tag. It did **not** catch an unclosed block
    element, because the parser recovers silently and the page renders correctly. Item 16 was found
    only because the converting agent counted `<p>` opens against closes as a private self-check.
    That count now lives in `tagcheck.py`, over twenty-three element types. The whole corpus balances
    exactly, so the check can be enforcing rather than advisory from the start — and reintroducing
    item 16's missing `</p>` makes it fire, which is how I know it works.

## Pattern, again

Of seventeen items, **five are cross-references or section numbers** and **four are counts stated in
prose about equations that are themselves correct**. Both categories survive a mathematics review,
which checks the derivation, and a language review, which checks the sentence — because they live in
the seam. The previous batch reached the same conclusion from a different starting point, which is
now enough evidence to make it a standing check rather than an observation.
