# Corrections found while converting Part III, 4.1 and 4.2

Eleven chapters, 163,688 words of main prose — the largest batch, and the one that finishes the
book's conversion. Forty-two items were reported by the eleven converting agents. Every one was
re-verified independently before anything was touched. **Twenty-three were fixed, one was a false
positive worth recording, and the rest were notational quibbles left alone.**

Two fixes deliberately break a `registercheck.py` invariant, which is correct — the invariants prove
a *register* rewrite changed nothing but prose, and these are content changes made afterwards, on
purpose. Marked **[invariant]**.

## Wrong sign, wrong word, wrong count

1. **3.1 §2 — the electron's charge-to-mass ratio lost its minus sign.** Printed as
   $1.759\times10^{11}\ \mathrm{C\,kg^{-1}}$ in a list that is otherwise signed, and the §8.1 table
   gives $-1.7588\times10^{11}$ with relative acceleration $-1836$. The two passages disagreed.
2. **3.1 §4.5 — "It is exactly right in three."** The volume ratio computed two lines below is
   $1-\tfrac34K^2t^4+\tfrac14K^3t^6$, and the bolded sentence that follows correctly says "keeps its
   volume **to second order in time**". "Exactly" overstates what the same paragraph derives.
3. **3.1, plain box 3.1.2 — "four orders of magnitude."** Excluding the neutron, which the sentence
   handles separately, the span is $1.76\times10^{11}$ to $4.82\times10^{7}$: a factor of 1836, or
   3.26 orders. **[invariant]**
4. **3.4 §3 — "Three separately non-tensorial objects"** followed by a list of four:
   $\partial\Gamma$ in two orderings *and* $\Gamma\Gamma$ in two orderings. Now four.
5. **3.5, Worked example 1 — "the terms quadratic in $t$ cancel."** Each product is (linear in $t$)
   × (constant), so no quadratic term exists at all. The cancellation itself is correct and is
   between the linear terms.
6. **3.9 §7.3 — "Twenty-five chapters."** Parts IV, V and VI are $11+11+8=30$. The same figure
   appears in plain box 3.9.7. **[invariant]**
7. **4.1, Problem 1(d) — the wrong one of two ingredients.** The solution says the divergence comes
   from a mode count that grows without bound and an energy per mode that does not fall, "and only
   the **second** of those is dimension-dependent." Part (b) states outright that equipartition is
   dimension-independent, and part (a) shows the mode count $g_d(\nu)=dC_d\nu^{d-1}/c^d$ *is*
   $d$-dependent. For the stated conclusion — that the diagnosis was correctly aimed at
   equipartition — it has to be the **first**.
8. **4.2 §3.4 — "§11's Problem 1."** Problem 1 is in §12; §11 is *Worked examples*.

## Claims that were true of a different object

9. **3.4 §6.2 — the Weyl tensor's conformal invariance stated for the wrong index placement.** The
   box names $C_{\rho\sigma\mu\nu}$, all indices down, and says it "is unchanged when the metric is
   multiplied by an arbitrary positive function of position." Under $g\to\Omega^2g$ the invariant
   object is the mixed form $C^{\rho}{}_{\sigma\mu\nu}$; the fully lowered form picks up $\Omega^2$.
   The conclusion drawn — that it records the shape of the light cones and not the scale of anything
   — is right either way. Now says "in the mixed form".
10. **3.8 §7.5 — a time given a distance's units.** "The characteristic time … for Rindler is $c/a$,
    and Chapter 3.1 §6.1 already noted it is about a light-year for $a=g$." $c/g\approx0.97$
    **year**; the light-year is $c^2/g\approx0.97$ ly, which is what 3.1 §6.1 actually says and is
    where the horizon sits. Both are now named, correctly.
11. **3.2, Worked example 1 — "on the equator the Jacobian is $\mathrm{diag}(-1,+1)$."** From the
    formulas two lines above, on $u^2+v^2=1$ it is
    $\begin{pmatrix}-\cos2\phi&-\sin2\phi\\-\sin2\phi&\cos2\phi\end{pmatrix}$ — a reflection with
    determinant $-1$, but equal to $\mathrm{diag}(-1,+1)$ only at $v=0$. The conclusion drawn is
    sound; the matrix was the value at one point.
12. **3.9 §1.1 — the wrong counterexample.** "A cone is homogeneous along its axis without being
    isotropic" is offered as *homogeneous but not isotropic*. A cone away from its apex is flat — as
    this book itself uses it in §2.4 and 3.3's Problem 1 — so locally it *is* isotropic; and it is
    not homogeneous in §1.1's own sense, because the length of the geodesic circle around the apex
    fixes $r$ intrinsically. Replaced with the infinite cylinder, which is the standard example and
    is genuinely homogeneous along its axis and anisotropic.

## Chapters that contradicted themselves

13. **3.2 §8.4 said the non-coordinate basis "produced centrifugal and Coriolis terms out of the
    labelling."** Worked example 2, four hundred lines later, says the opposite and is the one that
    is right: even in the coordinate basis the free-particle equation is $\ddot r-r\dot\theta^2=0$,
    and $\partial_r,\partial_\theta$ commute, so the extra term survives the change of basis. The
    real source is the connection. §8.4 now says the basis is what made the elementary calculation
    awkward, and points at Worked example 2 for the rest.
14. **3.6 — the sign traps could not agree how many there are.** The chapter opening announces
    **two**; §5's ⚠ box calls $g_{00}$ "the second of the two", promotes 3.4's Riemann convention to
    first, and refers to a **third** the opening never announced; §6.1's box is titled "The third
    sign trap". The opening now announces three. Both later boxes are ⚠ callouts, hence invariants,
    and are now correct as they stand.
15. **3.5, "Where we are" — "Chapter 0.7 §7.4 proved two vector identities by grinding through
    components."** The proofs are §7.1 and §7.2; §7.4 is the section that asserts the two are the
    same statement, $\dd^2=0$. The chapter's own tools paragraph and §3.2 both get this right, so
    the box was the outlier. Its two *other* citations of §7.4 are correct and were left.

## Numbers

16. **3.7 §8.3 — "A $20\%$ error in $\Delta\varphi$ would be four arcseconds per century, a hundred
    times the precision §8.5 claims."** $20\%$ of $42.98''$ is $8.6''$, which is 215× the $\pm0.04''$
    precision. The $4''$ and the "hundred times" agree with each other and correspond to $\approx
    9\%$, so the percentage was the outlier. Now $10\%$.
17. **3.8 §4.2 — "to the digit, the value Einstein published in 1911."** The chapter computes
    $0.8756''$ with modern solar constants; Einstein's 1911 number used the constants of his day and
    is usually quoted near $0.83''$. The *prediction* is his; the digits are not. The false precision
    is gone and the reason is named.
18. **4.1 §7.4** — $r_0^3$ listed as $1.481845\times10^{-31}$ and then multiplied as $1.481847$. The
    true value is $1.4818453\times10^{-31}$, so the list was right. Does not move $t_{\rm fall}$.
19. **4.1, Worked example 2** — $\Delta\lambda$ at $45^\circ$ listed as $0.7107$ pm;
    $2.4263102(1-\cos45^\circ)=0.710650$. Dependent entries unaffected.
20. **4.2** — $L_{\rm osc}$'s constant printed as $2.4797$ in `e-Losc` and used as $2.4795$ in
    Problem 4(a). $\pi/1.26693=2.47969$, so the equation was right.

## Two the agents fixed in passing, both dropped words in the original

21. **3.3 §5** read *"It does not be a tensor itself, which is the surprise."* A dropped word; the
    intended claim is unambiguous from §5.3(a).
22. **3.9's tools paragraph** carried a duplicated fragment, *"and for the radiation"*, immediately
    before the clause it duplicates.
23. **3.5 §1.1** contained an abandoned self-correction — a wrong expression for $\dd\lambda$
    followed by "more carefully" and the right one. The false start carried no claim and is gone.
24. **4.2 §7.3** stated "and is the unique solution with $\hat U(0)=\hat I$" twice, verbatim, in one
    sentence.

## One false positive, recorded so nobody re-spends the hour

**`fig-half`'s caption in 3.8 is correct.** It was flagged for using two incompatible coefficients:
"the second-order term in $GM/c^2b$, equal to $1.18\,GM/c^2b$", and then a gap growing "from six
parts in a million at the solar limb to seven percent at $24\,r_s$", which needs $\approx3$.

These are two different quantities. The first is the residual in the *ratio*
$\alpha_{\rm space}/\alpha_{\rm time}$ against $v^2/c^2$: $1.18\times2.122\times10^{-6}=2.5\times
10^{-6}$, matching the $2.6\times10^{-6}$ the caption states one clause earlier. The second is the
gap between the integrated $\alpha$ and the closed form, whose second-order coefficient is
$15\pi/16=2.945$: at the limb $6.25\times10^{-6}$ — "six parts in a million" — and at $24\,r_s$,
$6.1\%$. Both are right. Only "seven percent" rounds generously.

## Left alone deliberately

Notational quibbles, all recorded in the agents' reports and none of them false as printed: 3.5 §5.4
reuses $p$ for the dimension of a region rather than the degree of a form (unannounced, but every
reading is correct); 3.4 §5.2 calls the Levi-Civita symbol an array rather than a density, which the
book flags itself in 2.4 §8.1; 3.4 §1's holonomy-is-a-rotation claim is exact for the Riemannian
2-sphere it is run on and loose in Lorentzian signature; 3.2 §2.1's "no compact manifold is covered
by one chart" needs $n\ge1$; 3.6's Problem 4(b) draws a conclusion about galaxies from a 100 pc
crossover, which is directionally right for a stronger reason than the one computed.

## Where the errors were, across all three batches

| batch | items | cross-refs & section numbers | counts stated in prose | arithmetic | logic |
|---|---|---|---|---|---|
| Part 0 | 15 | 5 | 3 | 2 | 5 |
| 1.4 + Part II | 17 | 5 | 4 | 4 | 4 |
| Part III + 4.1–4.2 | 23 | 3 | 5 | 5 | 10 |

Fifty-five corrections across 383,000 words, none of which a build error could catch, and almost
none of which changes a final answer. That is the signature of the class: they survive because the
derivation is right and the sentence about it is wrong, and no reviewer looks at both at once.
