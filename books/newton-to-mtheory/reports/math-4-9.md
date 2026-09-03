# Mathematics review — Chapter 4.9, *Commutators, Uncertainty, and Symmetry*

Independent re-derivation of `src/ch4-9.html` (≈13,400 words of prose by `registercheck`'s count,
1,690 lines including the figure script). Every derivation below was done from scratch before the
page was consulted: Robertson and Schrödinger by hand, the Heisenberg equation from
$\hat U^{\dagger}\hat A\hat U$ and the product rule, Ehrenfest from that, the CSCO theorem both
directions. Every printed number was recomputed — the oscillator moments in `mpmath` at 45 digits,
the angular-momentum algebra in a normal-ordering Weyl-algebra engine written for this review (not
`sympy`'s operator module), the random-pair and Mandelstam–Tamm surveys in fresh `numpy`, and §5.5's
whole table in an independently written split-operator integrator. **All eight entries of §5.5's
table reproduce**, including `1.665772` to six decimals, the bit-for-bit zero, and the factor-of-four
convergence.

**Counts: 2 BLOCKER, 5 MAJOR, 17 MINOR.**

Scratch work in `…/scratchpad/mr49/{a_osc,b_misc,c_sym,d_ehren,e_ehren2,f_random,g_variants,h_final,i_probs,j_num,ov,ov2}.py`.
Nothing in the repository was edited.

---

## What came out clean

Recorded because a review that lists only defects has not said where the chapter is load-bearing.

* **§2's derivation is correct and complete, and it proves both forms.** Cauchy–Schwarz on
  `e-fg`; `e-fgop` by Hermiticity; the Hermitian/anti-Hermitian split `e-split`; `e-modsq`;
  `e-robertson` by dropping a non-negative term; `e-schrod` by keeping it. Every step re-derived
  independently and every step is right, including the sign and factor conventions
  ($[\Delta\hat A,\Delta\hat B]=[\hat A,\hat B]$ because numbers commute; anticommutator Hermitian
  so real; commutator anti-Hermitian so imaginary). The chapter is precise about which form is which
  — it derives Robertson at `e-robertson` and Schrödinger at `e-schrod`, calls the second "the
  sharper form", and never conflates them. `e-modsq` was checked over 200,000 random cases: worst
  residual $4.3\times10^{-14}$.
* **§1's "one line" is genuinely valid, not merely short.** Chapter 0.9 §6.4 does prove
  $\Delta x\,\Delta k\ge\tfrac12$ for a normalised $f$ with finite widths — I read the proof; §6.1
  reduces to $\avg x=\avg k=0$ without loss, §6.2 puts both spreads on the same axis, §6.3 is
  Cauchy–Schwarz on $(xf,f')$, §6.4 bounds $|I|$ by $|\mathrm{Re}\,I|=\tfrac12$. The substitution is
  legitimate and is **not** a change of variable that alters what $\Delta$ means: 4.6 §5.5
  establishes that the position↔momentum map is 0.9's Fourier transform with $k=p/\hbar$ and is
  *unitary*, so the measured momentum density is the wavenumber density re-expressed; $\Delta$ stays
  the standard deviation of a probability density in both cases, and $k\mapsto\hbar k$ being affine
  multiplies a standard deviation by $\hbar$ exactly. Nothing is smuggled.
* **The ⚑ budget is met exactly.** One ⚑ in the file (line 295), and it is the error–disturbance box.
  Both theorems in it are correctly stated with their hypotheses: Ozawa's three-term relation
  $\varepsilon(A)\eta(B)+\varepsilon(A)\Delta B+\Delta A\,\eta(B)\ge\tfrac12\abs{\avg{[\hat A,\hat B]}}$
  with the indirect-measurement model and rms definitions, correctly labelled state-dependent, and
  correctly noting the naive product is *false*; and Busch–Lahti–Werner's calibration-error result
  $\ge\hbar/2$ for the canonical pair. The reason the box exists is real: Chapter 0.9's ⚠ box says in
  as many words "Measurement disturbance is a real and separate phenomenon with its own theorems, and
  Chapter 4.9 will keep the two apart." That promise is paid, with names, and naming none of them
  would indeed have been an under-delivery.
* **§3.3's theorem is correctly stated and correctly proved, both directions.** Forward: $\hat C$
  commuting maps each one-dimensional joint eigenspace to itself, so is diagonal in the joint basis.
  Reverse: $\ket u\bra u$ commutes with every $\hat A_i$ (Hermiticity gives the left-multiplication
  half), and is not constant on a $W$ of dimension $\ge2$. §3.4's counting criterion follows exactly
  ($\sum_{\text{tuples}}\dim=n$, so all dimensions one $\iff$ tuple count $=n$), and its two examples
  are right, including the restriction of $\{\hat J^2,\hat J_z\}$ to *a single multiplet* — where the
  count $2j+1$ works — rather than to the whole space, where it would not. $\sum_{\ell=0}^{n-1}(2\ell+1)=n^2$ ✓.
  The joint eigenbasis for $m>2$ operators is covered by 0.5 §8.2's closing Remark, so §3.3 is not an
  unmarked import (see MINOR 17 for a defect in that Remark itself).
* **§4.3's differentiation is right, sign for sign.** $\dot{\hat A}_H = \tfrac{\ii}{\hbar}\hat U^\dagger\hat H\hat A\hat U-\tfrac{\ii}{\hbar}\hat U^\dagger\hat A\hat H\hat U+\hat U^\dagger(\partial_t\hat A)\hat U$,
  and inserting $\hat U\hat U^\dagger$ converts it to $\tfrac{1}{\ii\hbar}[\hat A_H,\hat H]+(\partial_t\hat A)_H$
  exactly, with $\hat H_H=\hat H$ for a time-independent Hamiltonian. `\dv` and `\pdv` both render in
  that one display (checked in the built page).
* **§4.4's term-by-term comparison with Chapter 1.3 §6.1 is honest.** I read 1.3 §6.1: it derives
  $\dv{f}{t}=\{f,H\}+\pdv{f}{t}$, calls it "the equation of motion for every observable of every
  Hamiltonian system", and notes it contains Hamilton's equations as $f=q^i$, $f=p_i$ — all three
  claims quoted accurately. The four-bullet comparison is exact and the fourth bullet ("the only
  difference anywhere is which bracket") is true of the two displays as written.
* **§4.6 and its two commutators.** $[\hat x,\hat p^2]=2\ii\hbar\hat p$ and $[\hat p,V]=-\ii\hbar V'$
  both verified symbolically; `e-ophamilton` follows exactly, with the $\ii\hbar$'s cancelling as
  claimed.
* **§5.5 is the best thing in the chapter and it is fully reproducible.** See the table at the end:
  every entry reproduces in an integrator sharing no code with theirs, the quadratic column's zero is
  bit-for-bit (`numpy.all(a==b)` is `True` at all 6001 samples), and the quartic gap `1.665772` is
  unmoved across four halvings of $\dd t$ while the Ehrenfest residuals fall by 4.000, 3.998, 3.984.
  The mean gap is 0.617952 ("0.62"), $\abs{\avg x-1.3\cos t}=2.608\times10^{-7}$ ("$2.6\times10^{-7}$"),
  and the packet width really does breathe (0.6000 → 0.8333) as the text claims.
* **§6.2 and §6.3's generators.** The translation family is checked for unitarity *and surjectivity*
  and for strong continuity by the correct density argument (4.3 §8.1's construction does deliver
  compactly supported continuous functions, so the citation is sound). The sign works out:
  $-\tfrac{\ii}{\hbar}\hat G\psi=-\psi'$ gives $\hat G=-\ii\hbar\partial_x$ ✓. $R^{-1}(\theta)\vv r$
  is written correctly, and $y\partial_x\psi-x\partial_y\psi=-\tfrac{\ii}{\hbar}\hat L_z\psi$ ✓.
* **The Worked examples and Problems compute correctly.** Every part of Worked examples 1–3 and
  Problems 1–4 was recomputed (symbolically where possible, numerically otherwise) and every stated
  answer is right — including the $\ii\hbar$ defect, the $\sin\hat\varphi$ repair, the chirped
  Gaussian's three numbers and its position on the unit circle, the oscillator's Heisenberg solution
  and its $2\omega$ breathing, the virial theorem in one and three dimensions, and all four parts of
  the two-qubit problem ($[\hat Z_1,\hat S]\ket{01}=-2\ket{10}$ ✓). **No blocker and no false clause
  in §7 or §8.** After 4.4's problem and 4.7's two worked-example blockers, this is worth saying.
* **Conventions.** One ⚑, one ⚠, one `familiar`, one `where`, one `brick`, six `plain`. `\ann` used
  exactly twice. No `\dv[...]`/`\pdv[...]`. No American spellings. No forbidden hedges (the two hits
  for "just" are both temporal — "has just been obtained", "the brick you just laid"). `tagcheck`
  clean. `registercheck --new` passes all four targets. Every `eqref` resolves. Every linked chapter
  exists; the nine unwritten ones are plain text. **Rendered at 1280/1000/900/760 px: column 704 px,
  zero overflowing displays, tables or solution blocks.**

---

## BLOCKER

### B1 — §2's `familiar` box (and the closing brick) assert a floor that does not exist for a general pair, contradicting §3.1 and §6.3 of this chapter

Line 411–412, and again at line 1512:

```
Equation [e-robertson] says no preparation does:
the product has a floor that no state gets under, so there is no experiment to design and no
covariate to go looking for. That much is proved here.
```

```
What is proved here is that no preparation narrows both spreads at once
```

The box is written about a generic pair — "two correlated readings", "a true pair of values
$(A,B)$". For a generic pair there is **no state-independent floor**. `e-robertson` bounds
$\Delta A\,\Delta B$ by $\tfrac12\abs{\avg{[\hat A,\hat B]}}$ *evaluated in the same state*, and that
number can be zero in a state where the operator $[\hat A,\hat B]$ is not.

The chapter says so itself, three times, and each time in stronger language than the box:

* §3.1: "$\avg{[\hat A,\hat B]}$ can vanish in a state even when the operator $[\hat A,\hat B]$ does
  not. In that state the bound has fallen silent while the prohibition still stands."
* §6.3, with a number I reproduced exactly: the spin-1 middle state has
  $\Delta L_x\,\Delta L_y=1.000000000000000\,\hbar^{2}$ **against a bound of exactly zero**.
* plain-terms 4.9.2: "when the right-hand side happens to vanish in some particular state, the
  theorem has not announced that both quantities are sharp. It has fallen silent."

And a two-line counterexample settles it: take $\hat A=\hat\sigma_x$ and
$\hat B=\hat\sigma_x+\epsilon\hat\sigma_z$, which do not commute
($[\hat A,\hat B]=-2\ii\epsilon\hat\sigma_y$). In the state $\ket{+}$, $\Delta A=0$ and
$\Delta B=\epsilon$: **both spreads are as narrow as you like, simultaneously**, for a genuinely
non-commuting pair. "No preparation narrows both spreads at once" is false as written.

*What it should say.* Scope the claim to the pair that has a state-independent floor. Something like:
*"For position and momentum the commutator is $\ii\hbar$ in every state, so the floor is $\hbar/2$
whatever you prepare: there is no experiment to design and no covariate to go looking for. For a
general pair the floor is itself a property of the state, and §6.3 exhibits a case where it is zero
and the theorem says nothing."* The brick's sentence needs the same scoping.

### B2 — §2's `familiar` box reinstates by implication the very claim the next paragraph disowns, on a premise that is false

Lines 407–410:

```
Here the covariate story runs into something the arithmetic forbids. If each system
carried a true pair of values $(A,B)$ that you merely failed to record, then a better preparation
could in principle narrow both marginals at once, exactly as identifying a covariate narrows a
response distribution.
```

Read the paragraph as a logician would. It asserts *hidden pair $\Rightarrow$ both marginals can be
narrowed*; the next sentence asserts *both marginals cannot be narrowed*; modus tollens gives *no
hidden pair* — which is precisely the strong claim the following paragraph then disowns ("The
stronger statement, that there is no joint distribution underneath at all, is not proved by this
inequality and should not be claimed from it"). The retraction is therefore incomplete: the strong
claim is no longer asserted, but the chapter still hands the reader a valid route to it and then
tells them not to walk down it.

Worse, the premise is not merely unproved, it is **false**. A hidden joint distribution does not
entail that arbitrary sub-ensembles of it are preparable. Bohmian mechanics is the standing
existence proof: every system carries a definite pair $(x,v)$, and no preparation narrows both
spreads, because the equilibrium distribution is what constrains which sub-ensembles exist. The
implication needs the extra premise *every sub-ensemble is itself a quantum state* — which is the
completeness assumption at issue, not a consequence of the inequality.

This is exactly the reasoning the writer says it rejected. Its own stated rationale for the
retraction — a floor on a product of spreads does not contradict a hidden joint distribution with
correct marginals — is the refutation of the surviving sentence.

*What it should say.* Delete the conditional and state the operational half directly, with no
inference about what underlies it: *"The covariate story predicts that a better preparation would
narrow both. For position and momentum no preparation does, and that is proved here. It does not
follow that there is no joint distribution underneath — a floor on a product of spreads is
consistent with one — and that stronger claim belongs to Chapters 4.11 and 4.20."*

---

## MAJOR

### M1 — §4 never mentions domains, and the moving domain is exactly what Chapters 4.4 and 4.5 were spent on

`grep -i domain src/ch4-9.html` returns ten hits. Not one of them is in §4.1, §4.2 or §4.3. The
chapter that makes a set piece of the domain hypothesis in §2.5, and whose Worked example 2 exists to
exhibit a domain failure, builds the entire Heisenberg picture without a word about domains.

Three things are being passed over:

1. `e-hpic` defines $\hat A_H(t)=\hat U^\dagger(t)\hat A\hat U(t)$ with no domain. For unbounded
   $\hat A$ the operator is defined on $\operatorname{dom}(\hat A_H(t))=\hat U(t)^\dagger\operatorname{dom}(\hat A)$,
   **which moves with $t$**. That is what makes $\hat A_H(t)$ a genuinely different operator at each
   time in 4.4 §3.1's sense ("Two operators are the same operator when the formulae agree *and* the
   domains agree").
2. §4.3 differentiates the product $\hat U^\dagger\hat A\hat U$ "with the product rule". For
   unbounded $\hat A$ and $\hat H$ this is a strong derivative on vectors in a common invariant
   dense domain, not an operator-norm derivative, and the ingredient it uses
   ($\dv{\hat U}{t}=-\tfrac{\ii}{\hbar}\hat H\hat U$, 4.6 §3.1) is itself stated by 4.6 only on
   $\operatorname{dom}(\hat H)$ and only in the strong sense.
3. §4.2's "So `e-hpic` is a similarity transformation **and nothing else**" is the sentence that
   does the papering over. It is right about the algebra and silent about the one thing the algebra
   does not carry.

The results are all correct. What is missing is one sentence in §4.1 or §4.2 — *"the domain moves
with the operator, $\operatorname{dom}(\hat A_H(t))=\hat U^\dagger(t)\operatorname{dom}(\hat A)$,
and the differentiation of §4.3 is in the strong sense on vectors that stay in it"* — plus the
matching qualifier on "nothing else". As it stands, a reader who has just finished Chapter 4.4 is
being shown the one manoeuvre that chapter warned about, framed as costless.

### M2 — §4.2 gets spectrum-invariance from determinant, trace and eigenvalues, none of which exists for the operators in question

Lines 647–652:

```
Everything invariant under [e-hpic] is a fact about the observable rather than about the picture,
and Chapter 0.4 §5 and §6 identified the determinant and the trace as two such invariants, with
Chapter 0.5 adding the eigenvalues. So the spectrum of $\hat A_{H}(t)$ equals the spectrum of
$\hat A$ at every time.
```

Chapter 0.4 §5 is "The determinant, as signed volume" and §6 is "Trace, and the identity that
matters" — finite-dimensional matrix facts. $\hat x$, $\hat p$ and $\hat H$ have neither a
determinant nor a trace. And 0.5's contribution is *eigenvalues*, which the operators here do not
have: 4.5 §2.5 (which this very chapter cites at §3.5 for exactly this point — "an observable in
infinite dimensions may have no eigenvectors at all") shows $\hat x$ has spectrum $\R$ and no
eigenvectors whatever. The premises of the argument are void for every observable in Part IV, and
the conclusion is then stated about the *spectrum*, a word 0.4 and 0.5 never defined.

The conclusion is true, and the book already owns the one-line proof: by 4.5 §2.1's widened
definition, $\lambda$ is in the resolvent set of $\hat A_H$ iff $\hat A_H-\lambda=\hat U^\dagger(\hat A-\lambda)\hat U$
has a bounded everywhere-defined inverse, and $\hat U^\dagger(\hat A-\lambda)^{-1}\hat U$ is one
exactly when $(\hat A-\lambda)^{-1}$ is. Replace the det/trace sentence with that.

### M3 — §6.5: "there is no one-parameter family of which [parity] is a member" is false

Lines 1104–1107:

```
It is unitary, it is self-adjoint, and it
commutes with $\hat H$ whenever $V$ is even. But there is no one-parameter family of which it is a
member, so Stone has nothing to act on and there is no generator.
```

Every unitary involution sits inside a strongly continuous one-parameter unitary group. Write
$\hat P_-$ for the projection onto odd functions. Then $\epsilon\mapsto\ee^{\ii\pi\epsilon\hat P_-}$
is strongly continuous (the generator is bounded), obeys the group law, and at $\epsilon=1$ gives
$\hat I+(\ee^{\ii\pi}-1)\hat P_-=\hat I-2\hat P_-=\hat\Pi$. Stone has plenty to act on and hands
back the generator $-\pi\hbar\hat P_-$. So the stated reason for the section's conclusion is wrong.

The conclusion is right and the honest reason is geometric, not spectral: the reflection
$\vv r\mapsto-\vv r$ has determinant $-1$, and the component of $O(3)$ it lives in is not the one
containing the identity, so **no family of spatial transformations** connects parity to the
identity. A group manufactured algebraically from $\hat\Pi$ itself has a generator that is a function
of $\hat\Pi$, so it supplies no new conserved quantity — which is what the section actually wants to
say, and what the rest of the paragraph then says correctly.

### M4 — the plain-terms box and the closing brick drop the linearity assumption that §6.1 discloses

§6.1 is exemplary about this:

```
Linearity is assumed rather than derived at this link, exactly as Chapter 4.2 §7.1 assumed
it, and every family in this section is visibly linear, so the assumption is discharged case by case
instead of in general.
```

I checked 4.2 §7.1 and it does assume linearity as a physical requirement, and 4.2 §7.2's theorem is
"linear **and** norm-preserving $\Rightarrow$ unitary". So §6.1's disclosure is accurate.

The two summaries then delete it. Plain-terms 4.9.6: *"Preserving predictions means preserving
lengths, **which forces** the transformation to be a rotation of the space of states."* The brick:
*"**Symmetry forces unitarity** by Chapter 4.2 §7.2."* Both read as a proved implication. §6's own
headline compounds it: *"**Chapter 4.2 states the correspondence; this section proves it**"*, when
the section assumes one hypothesis and quotes another (Stone's converse, a ⚑ standing at 4.5 §9.3).

This matters more than a wording slip because the brick is the chapter's ledger, and the ledger is
where a later chapter goes to find out what it may rely on. Add "for a linear symmetry" to both.

**On the decision not to mention the antiunitary alternative: I judge it correct.** Under the ⚑
contract, saying anything about what happens when linearity is dropped requires either a proof of
Wigner's theorem or a second mark, and the budget is one. Every family in §6 is manifestly linear, so
the assumption is genuinely discharged where it is used, and §6.1 says so in plain words. The cost —
that a reader may take linearity for a formality — is paid by §6.1's disclosure and would be
entirely unpaid if M4 were left standing.

### M5 — the seam with Chapter 4.5: 4.5's own brick asserts, as a description of *this* chapter's theorem, exactly what this chapter refuses

`src/ch4-5.html` line 2267, in the closing brick's "Where this gets spent":

```
Chapter 4.9's uncertainty relation is the statement that two observables
have two spectral measures with no joint distribution beneath them, which §6.5's familiar-ground box
named and did not develop.
```

and 4.5 §6.5's familiar-ground box itself: *"the same state gives different distributions for
position and for momentum, **with no joint distribution underneath them from which both could be
recovered**. Chapter 4.9 turns that into the uncertainty relation…"*

Chapter 4.9 now says: *"The stronger statement, that there is no joint distribution underneath at
all, is not proved by this inequality and should not be claimed from it."* A reader following 4.5's
pointer arrives at a flat contradiction of what they were promised.

**4.9 is right and 4.5 is the side that must move.** The Robertson inequality constrains two
marginals; a joint distribution reproducing both marginals is not excluded by any bound on the
product of their spreads (the Wigner function reproduces both marginals for every state — what fails
is its non-negativity, and that is a different theorem). 4.5's two sentences assert an unproved
result, unflagged, and route the debt to a chapter that correctly declines it. The fix on 4.5's side:
the brick sentence should read *"Chapter 4.9's uncertainty relation says that no preparation narrows
both spreads below the floor; that no joint distribution lies beneath the two spectral measures is
Chapters 4.11's and 4.20's"*, and §6.5's box should point forward rather than assert.

One thing 4.9 should change at the same seam: its `familiar` box says "Chapter 4.5 §6.5's
familiar-ground box **named** it". 4.5 did not name it, it asserted it. Under-describing a live
contradiction as a naming leaves the seam unrepaired from both sides.

---

## MINOR

**m1 — §5.4, plain 4.9.5 and the brick: "three potentials and no more" undercounts the quadratics.**
$V'''\equiv0\iff V=ax^{2}+bx+c$. With $a<0$ that is the repulsive quadratic — the parabolic barrier —
which is neither free, nor a uniform field, nor the harmonic oscillator, and for which Ehrenfest's
classical reading is likewise exact. Say "the quadratics" and list four cases, or add the qualifier.
(The book never uses a parabolic barrier elsewhere, so nothing downstream is broken.)

**m2 — §4.5: "every moment … so the entire probability distribution … is frozen" leans on the moment
problem.** Constant moments do not in general determine a constant distribution for an unbounded
observable. The book has the one-line argument already: $[\hat A,\hat H]=0$ makes $\hat A$'s spectral
projections commute with $\hat U(t)$, so $\norm{P_A(E)\psi(t)}^{2}$ is constant for every Borel $E$
— 4.5 §6 supplies the projections and §3.5 of this chapter already cites them.

**m3 — §2.5 mis-cites 4.4 §2.1.** *"For bounded operators, which by Chapter 4.4 §2.1 are defined on
the whole space…"*. 4.4 §2.1 defines boundedness *for an operator on a subspace* $\mathcal D$ and
proves bounded $\iff$ continuous. It never says bounded operators are defined everywhere; the fact
4.4 does have (line 22) runs the other way — a symmetric operator defined on the whole space is
bounded. What makes the sentence true is continuous extension from a dense domain, which the book
has not stated. Cite §2.1 for continuity and say the extension explicitly, or drop the citation.

**m4 — §2.5's "second hypothesis" is not independent of the first.** The first hypothesis, as stated,
already presupposes that $\Delta\hat A\ket\psi$ and $\Delta\hat B\ket\psi$ exist, hence that
$\avg{\hat A}$ and $\avg{\hat B}$ do. The paragraph is worth keeping — the physical reading is the
point, and it *is* correctly derived: any $\psi\in L^{2}\setminus L^{1}$ automatically has
$\avg{x^{2}}=\infty$, since $\int\abs\psi\le\sqrt\pi(1+\avg{x^{2}})^{1/2}$ by Cauchy–Schwarz against
$(1+x^{2})^{-1/2}$, so 4.3 §5.5 really does deliver states with no $\Delta x$ — but "a second
hypothesis" should be "a second thing the first hypothesis quietly requires". Relatedly, the third
paragraph opens "The other hypothesis fails…" meaning the *first*, two paragraphs back; name it.

**m5 — §4.4 mis-cites 1.3 §6.4.** *"Chapter 1.3 §6.4 announced it in advance and named this chapter
as where it would be taken seriously."* 1.3 §6.4's insight box names **Chapter 4.2 §8** for the
substitution ("Chapter 4.2 §8 will take the classical structure you now own…"); it names 4.9 only for
the uncertainty principle. What does name 4.9 for the substitution is 1.3's §1 opening and its
closing brick ("The bracket goes to Chapter 4.9, which replaces it by $\tfrac1{\ii\hbar}[\;,\;]$").
The claim is substantively true of Chapter 1.3 and false of §6.4. (4.2 §8's ⚑ box makes the same
error; this is inherited, not invented.)

**m6 — §6.1: "what Chapter 1.3 promised would be repeated here word for word."** 1.3's brick routes
§7's generators to *Chapter 4.2* ("The generators of §7 go to … Chapter 4.2 (observables generate
unitaries)"), and 4.2 §7.5 already claimed this promise in the identical words. Two chapters cannot
both be the one 1.3 promised, and 1.3 names 4.2. Cite 1.4 §7 (which the sentence also does, and
correctly) and drop the 1.3 clause, or say "repeated a second time, with the generator's existence
now supplied".

**m7 — Problem 2(d) mis-cites 4.6 §10.4.** *"the reason Chapter 4.6 §10.4 found the oscillator
packet's width unchanging."* 4.6 §10.4 is "Reading the answer" and concerns the *free* packet
spreading. The oscillator run — displaced to $x_0=2$, $\sigma_0=1/\sqrt2$, width held to
$3.5\times10^{-7}$ — is 4.6 **§10.8**.

**m8 — Problem 2(d) mis-cites its own §4.5.** *"since §4.5 makes a stationary state's distributions
constant."* §4.5 shows that a *conserved observable*'s distribution is constant in any state. That
*every* observable's distribution is constant in a *stationary state* is 4.6 §9.2 — which this
chapter's own Problem 3(a) cites correctly. Point 2(d) at 3(a).

**m9 — Worked example 2 mis-describes 4.4 §5.4.** *"on the periodic domain Chapter 4.4 §5.4
selected"* and *"which Chapter 4.4 §5.4 fixed as the periodic functions"*. 4.4 §5.4's headline
result is the opposite: "**Momentum on a bounded interval is not one observable but a circle of
them**", the self-adjoint domains being $\mathcal D_\theta=\{v:v(L)=\ee^{\ii\theta}v(0)\}$.
Periodicity is $\theta=0$, which this example *chooses* (rightly — single-valuedness on the circle
forces it). Nothing in the example depends on the choice: I checked that the boundary term
$[\bar u v]_0^{2\pi}=1$ and the defect $\ii\hbar$ come out the same for every $\theta$. Say "the
$\theta=0$ member of the circle Chapter 4.4 §5.4 found".

**m10 — the "where" callout over-attributes.** *"Section 1 … pays six of Chapter 0.9's promises with
one multiplication."* `python3 debts.py 4.9` lists exactly six promises from ch0-9, and two of them
are not §1's: "That is exactly why Chapter 4.9 will be able to state the general uncertainty relation
as $\Delta A\Delta B\ge\tfrac12\abs{\avg{[A,B]}}$" is paid by §2, and "Measurement disturbance … and
Chapter 4.9 will keep the two apart" is paid by §2.6. Say "six of Chapter 0.9's promises, four of
them here and the rest in §2".

**m11 — §5.5 is not reproducible from what is printed.** The paragraph names the integrator (4.6
§10.7's split-operator), the grid (4096 on $[-20,20]$), the step ($10^{-3}$), the run ($t=6$), and the
initial state — but not the finite-difference stencil used for $\dv{}{t}$, and the first two rows
depend on it by five orders of magnitude. With 4.6 §10.7's ordering
($\ee^{-\ii V\dd t/2}\ee^{-\ii T\dd t}\ee^{-\ii V\dd t/2}$), the means follow velocity-Verlet exactly,
so a **two-point** centred difference makes row 1 vanish to $1.0\times10^{-12}$; only a **four-point**
(fourth-order) stencil gives the printed $2.2\times10^{-7}$ and $1.0\times10^{-6}$. I recovered the
table only after trying five estimators. One clause — "the time derivatives are fourth-order centred
differences of the recorded series" — makes the whole table checkable. (The book's own standard:
"the book's whole claim is that its arithmetic can be reproduced".)

**m12 — §5.5's diagnosis of the residual is one step looser than its test.** "halving $\dd t$ divides
them by four … **which is the second-order error of the splitting** doing what second-order errors
do." The fourfold test establishes only $O(\dd t^{2})$, and there are two $O(\dd t^{2})$ sources
here. With the four-point stencil the residual is exactly $\tfrac{\dd t^{2}}{6}\max\abs{\dddot{\avg p}}$:
$\tfrac{10^{-6}}{6}\times1.3=2.17\times10^{-7}$, which is the printed $2.2\times10^{-7}$ to three
figures. That is the splitting's second-order error read through the stencil, not the splitting
failing to solve the equation — a two-point difference of the same series gives $10^{-12}$. The
conclusion ("the residuals belong to the integrator rather than to the theorem") is safe; the
attribution is not quite.

**m13 — §2.7's $10^{-41}$ residuals are not independently reproducible.** My own 45-digit
Gauss–Legendre evaluation of the same integrals gives departures of $4.4\times10^{-47}$ ($n=0$),
$1.8\times10^{-46}$ ($n=1$) and exactly $0$ ($n=3$). The quoted $1.1\times10^{-41}$ and
$9.2\times10^{-41}$ are plausible for 40-digit working precision but depend on the quadrature.
The 12-figure values `0.500000000000` and `3.500000000000` are exact and reproduce.

**m14 — the figure script's header comment conflicts with 0.5 §1.4's definition of angle.**
`/* … the cosine of the angle between them is (1/2)/(3/2) = 1/3. */` For the $n=1$ state
$\avg{f,g}=\ii/2$ exactly (I computed it), so 0.5 §1.4's
$\cos\theta=\mathrm{Re}\avg{u,v}/\norm u\norm v$ is **zero**: the two vectors are orthogonal in the
book's own sense, and the drawn $70.5^\circ$ is the angle in the real plane spanned by the projection
and the leftover. The caption handles this correctly ("The drawing is the real plane spanned by the
projection and the leftover"); only the comment misstates it. Everything drawn is right:
$\Delta x=\Delta p=1.2247$, projection $0.40825$, ratio exactly $1/3$, product $1.500$, all verified.

**m15 — §3.3's "a function of the $\hat A_i$ in the sense of Chapter 0.5 §7."** 0.5 §7 defines
$f(A)=\sum_k f(\lambda_k)P_k$ for **one** operator. The plural object $\sum_a c(a)\hat P_{(a)}$ is a
natural extension (and in finite dimensions is genuinely a polynomial in the $\hat A_i$), but §7 as
written does not cover it. One clause of extension, or a different citation.

**m16 — Worked example 3(d)'s "run the same relation backwards" is a new argument, not a re-reading.**
$\tau_A\Delta E\ge\hbar/2$ is a statement about an observable $A$ and its rate of change; reading it
as "a state that lives for $\tau$ cannot have energy sharper than $\hbar/2\tau$" needs an
identification of the lifetime with some $\tau_A$. The hedges ("about", "order of magnitude") and the
deferral to 4.17 carry it, but "the same relation backwards" claims more than a re-reading.

**m17 — cross-chapter, surfaced by §3.3.** 0.5 §8.2's closing Remark, which is what licenses §3's
joint eigenbasis for $m>2$ operators, ends: *"refining the decomposition until no eigenspace has
dimension greater than one."* That is false for a commuting set that is not complete — which is
exactly what §3.3's second half and Problem 4(b) are about ($\{\hat T\}$ on two qubits leaves a
two-dimensional joint eigenspace no refinement by functions of $\hat T$ can cut). The Remark's
*conclusion* (a common eigenbasis exists) is right; the stopping condition is not. Worth fixing in
0.5 since §3 now leans on that Remark.

Two smaller notes, not worth numbering: §6.3's "both entering with a plus sign once the two minus
signs in the expansion have been multiplied together" describes the fourth term of the expansion
only — the first survivor is the $++$ term and has no minus signs to multiply (the four signs are
$+,-,-,+$ and the survivors are the two $+$ terms; verified symbolically). And plain-terms 4.9.3's
"three numbers in a bracket with nothing hidden behind them" is an unlucky echo of hidden-variable
language in a chapter that has just carefully declined that claim; it means "the three labels are the
whole content", which §3 does prove.

---

## Every number I reproduced independently

$\hbar=m=\omega=1$ throughout unless stated. "Mine" is computed from scratch; no code or intermediate
value was taken from the chapter or its figure script.

| § | Quantity | Chapter | Mine | Verdict |
|---|---|---|---|---|
| 2.7, brick | $\Delta x\,\Delta p$, oscillator $n=0$ | $0.500000000000$ | $0.5$ (45 dps; dev $4.4\times10^{-47}$) | ✓ |
| 2.7, brick | $\Delta x\,\Delta p$, oscillator $n=3$ | $3.500000000000$ | $3.5$ (dev $0$) | ✓ |
| 2.7 | ratio $n{=}3$ to $n{=}0$ | "seven times above" | $7.000000$ | ✓ |
| 2.7 | departures at 40 digits | $1.1\times10^{-41}$, $9.2\times10^{-41}$ | $\le1.8\times10^{-46}$ at 45 dps | order only (m13) |
| 2.7 | infinite-well ground state $\Delta x\Delta p/\hbar$ (4.7 §3.5) | $0.567862$ | $0.5678618084$ | ✓ |
| 2.7 | random pairs, min Robertson slack | $7.8\times10^{-10}$ | $5.9\times10^{-10}$, 0 violations / 200 000 | ✓ (order) |
| 2.7 | min sharper-form slack | $-3.0\times10^{-14}$ | $-2.1\times10^{-14}$; exactly tight in $d{=}2$ ($\max\abs{}=1.4\times10^{-14}$) | ✓ |
| 2.7 | worst residual of `e-modsq` | $2.5\times10^{-14}$ | $4.3\times10^{-14}$ over 200 000 | ✓ (order) |
| fig | $\Delta x=\Delta p$, $n=1$ | $1.2247$ | $1.2247448714=\sqrt{3/2}$ | ✓ |
| fig | $\abs{\avg{f,g}}$, $n=1$ | $0.500$ | $\avg{f,g}=\ii/2$ exactly | ✓ |
| fig | projection $\abs{\avg{f,g}}/\Delta x$ | $0.4082$ | $0.4082482905$ | ✓ |
| fig | projection $/\Delta p$ | $1/3$ | $0.3333333333$ | ✓ |
| fig | $\Delta x\,\Delta p$, $n=1$ | $1.500$ | $1.5$ | ✓ |
| fig | chirp point $(\beta/\alpha=1)$ | $(c,1)/\sqrt{1+c^2}$ | $(0.707107,0.707107)$ numerically | ✓ |
| fig | chirp point $(\beta/\alpha=2)$ | " | $(0.894427,0.447214)$ | ✓ |
| 4.6 | $[\hat x,\hat p^{2}]$ | $2\ii\hbar\hat p$ | Weyl algebra: difference $=0$ | ✓ |
| 4.6 | $[\hat p,V(\hat x)]$ | $-\ii\hbar V'$ | product rule, exact | ✓ |
| 5.5 | $\max\abs{\dv{}{t}\avg{\hat x}-\avg{\hat p}}$, $V=x^2/2$ | $2.2\times10^{-7}$ | $2.1667\times10^{-7}$ | ✓ |
| 5.5 | same, $V=x^4/4$ | $1.0\times10^{-6}$ | $1.0249\times10^{-6}$ | ✓ |
| 5.5 | $\max\abs{\dv{}{t}\avg{\hat p}+\avg{V'}}$, $V=x^2/2$ | $1.1\times10^{-7}$ | $1.0833\times10^{-7}$ | ✓ |
| 5.5 | same, $V=x^4/4$ | $3.1\times10^{-6}$ | $3.0857\times10^{-6}$ | ✓ |
| 5.5 | $\max\abs{\avg{V'}-V'(\avg{\hat x})}$, $V=x^2/2$ | $0$, bit for bit | `all(a==b)` True, all 6001 samples | ✓ |
| 5.5 | same, $V=x^4/4$ | $1.665772$ | $1.665772$ | ✓ |
| 5.5 | $\max\abs{\dv{}{t}\avg{\hat p}+V'(\avg{\hat x})}$, quartic | $1.665771$ | $1.665771$ | ✓ |
| 5.5 | mean gap over the run, quartic | $0.62$ | $0.617952$ | ✓ |
| 5.5 | $\max\abs{\avg{\hat x}-1.3\cos t}$, quadratic | $2.6\times10^{-7}$ | $2.608\times10^{-7}$ | ✓ |
| 5.5 | residual ratio per halving of $\dd t$ | "divides by four, three times" | 4.000, 3.998, 3.984 / 4.000, 4.000, 4.000 | ✓ |
| 5.5 | gap unmoved by $\dd t$ | "does not move" | $1.665772$ at all four $\dd t$ | ✓ |
| 5.5 | quartic force scale (context) | "of order one" | $\max\abs{\avg{V'}}=3.601$ | ✓ |
| 5.5 | quadratic packet "breathing" | "width breathing the whole time" | $\Delta x$: $0.6000\to0.8333$ | ✓ |
| 6.3 | $[\hat L_x,\hat L_y]-\ii\hbar\hat L_z$ | $0$ | $0$, and both cyclic images, in the Weyl algebra | ✓ |
| 6.3 | $[\hat y\hat p_z,\hat z\hat p_x]$ | $-\ii\hbar\,\hat y\hat p_x$ | identical | ✓ |
| 6.3 | $[\hat z\hat p_y,\hat x\hat p_z]$ | $+\ii\hbar\,\hat x\hat p_y$ | identical | ✓ |
| 6.3 | the two vanishing terms | $0$ | $0$ | ✓ |
| 6.3 | spin-1 top state $\Delta L_x\Delta L_y$ | $0.500000000000000\,\hbar^2$ | $0.500000000000000$ | ✓ |
| 6.3 | its bound $\tfrac\hbar2\abs{\avg{\hat L_z}}$ | $0.500000000000000\,\hbar^2$ | $0.500000000000000$ | ✓ |
| 6.3 | spin-1 middle state $\Delta L_x\Delta L_y$ | $1.0\,\hbar^2$ | $1.000000000000000$, bound $0$ | ✓ |
| WE2 | $\Delta\varphi$ on the circle | $\pi/\sqrt3=1.8138$ | $1.8137994$ | ✓ |
| WE2 | $\avg{\hat\varphi^{2}}$ | $4\pi^{2}/3$ | $13.159473$ | ✓ |
| WE2 | $\avg{\hat L_z\psi_m,\hat\varphi\psi_m}$ | $\pi m\hbar$ | identical | ✓ |
| WE2 | $\avg{\psi_m,\hat L_z\hat\varphi\psi_m}$ | $\pi m\hbar-\ii\hbar$ | identical | ✓ |
| WE2 | the defect | $\ii\hbar$ | $\ii\hbar$, boundary term $[\bar uv]_0^{2\pi}=1$ | ✓ |
| WE2 | $[\sin\hat\varphi,\hat L_z]$ | $\ii\hbar\cos\hat\varphi$ | identical | ✓ |
| WE3 | $\hbar/(2\times1\ \mathrm{eV})$ | $3.29\times10^{-16}$ s | $3.29106\times10^{-16}$ s | ✓ |
| WE3 | Mandelstam–Tamm, min slack | $2.7\times10^{-10}$ | $1.2\times10^{-9}$, 0 violations / 200 000 | ✓ (order) |
| WE3 | $(\ket0+\ii\ket1)/\sqrt2$ saturation | $\tau_A\Delta E=\hbar/2$ | $0.5000000000$ exactly, with $\hat A=\hat\sigma_x$ | ✓ |
| WE1 | minimiser width / spread | $\Delta x=\sqrt{\hbar/2\mu}$, $\Delta p=\sqrt{\mu\hbar/2}$ | identical; product $\hbar/2$ for every $\mu$ | ✓ |
| P1 | $(\Delta x)^2,\ (\Delta p)^2,\ \mathrm{cov}$ | $\tfrac1{4\alpha},\ \tfrac{\hbar^{2}(\alpha^{2}+\beta^{2})}{\alpha},\ \tfrac{\hbar\beta}{2\alpha}$ | all three, symbolically and numerically | ✓ |
| P1 | sharper form tight | equality | slack $\le4.4\times10^{-16}$ at three $(\alpha,\beta)$ | ✓ |
| P1 | $\Delta x\Delta p$ | $\tfrac\hbar2\sqrt{1+(\beta/\alpha)^{2}}$ | identical | ✓ |
| P2 | $[\hat x_H(t),\hat p_H(t)]$ | $\ii\hbar$ | $\ii\hbar\cdot1$, symbolically for all $t$ | ✓ |
| P2 | cross term of $(\Delta x(t))^{2}$ | $\tfrac{\sin2\omega t}{2m\omega}\avg{\{\Delta\hat x,\Delta\hat p\}}$ | identical | ✓ |
| P2 | constant-width condition | $\mathrm{cov}=0$, $(\Delta p)^2=m^2\omega^2(\Delta x)^2$ | gives $(\Delta x)^2$, $t$-free | ✓ |
| P3 | $[\hat x\hat p,\hat H]$ | $\ii\hbar(\hat p^{2}/m-\hat xV')$ | identical, Weyl algebra | ✓ |
| P3 | virial, $V=-k/r$ | $E=-\avg{\hat T}$, $\avg{\hat V}=2E$ | Euler degree $-1$: identical | ✓ |
| P4 | $\hat T$ spectrum | $2,0,0,-2$ | $\{-2,0,0,2\}$ | ✓ |
| P4 | $[\hat T,\hat S]$, $\hat S^{2}$, $\hat S^{\dagger}$ | $0$, $\hat I$, $\hat S$ | $0$, $I$, symmetric | ✓ |
| P4 | $[\hat Z_1,\hat S]\ket{01}$ | $-2\ket{10}$ | $-2\ket{10}$ | ✓ |
| 3.4 | hydrogen count | $\sum_{\ell=0}^{n-1}(2\ell+1)=n^{2}$ | identical | ✓ |
| render | column width / display overflow | fits 704 px | column $704$ px; **0** overflows at 1280/1000/900/760 px | ✓ |
