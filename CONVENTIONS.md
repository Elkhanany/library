# Part II conventions — fixed across all six chapters. Do not deviate.

- **Signature (+,−,−,−)**: `\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)`. Timelike separations have
  $\Delta s^2 \gt 0$. (Chosen because Parts V–VII are particle physics, where this is standard.
  Say so once, in 2.3, and note the other convention exists.)
- **Coordinates** $x^\mu=(ct,x,y,z)$, so $x^0=ct$. Greek indices $\mu,\nu,\rho,\sigma = 0\ldots3$;
  Latin $i,j,k=1\ldots3$. Einstein summation over one up + one down index.
- $\beta = v/c$, $\gamma = (1-\beta^2)^{-1/2}$. Rapidity $\phi$ with $\tanh\phi=\beta$
  (use $\phi$ for rapidity throughout; never $\eta$, which is the metric).
- **Interval** $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$.
  **Proper time** $c^2\dd\tau^2 = \dd s^2$.
- **Boost along $x$** (standard configuration, $S'$ moving at $+v$):
  $ct' = \gamma(ct - \beta x)$, $x' = \gamma(x - \beta ct)$, $y'=y$, $z'=z$.
- **Four-velocity** $u^\mu = \dd x^\mu/\dd\tau$, so $u\cdot u = c^2$.
  **Four-momentum** $p^\mu = mu^\mu = (E/c,\ \vv p)$, so $p\cdot p = m^2c^2$.
- $m$ ALWAYS means **rest mass**. The book does not use "relativistic mass"; 2.5 explains why
  in one paragraph and then never mentions it again.
- **Electromagnetism**: $A^\mu = (\phi/c,\ \vv A)$, $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$.
  $\partial_\mu = \pdv{}{x^\mu}$ (lower index — it is a covector, per 0.6).
- **Units**: SI throughout Part II, with $c$ written explicitly. Note in 2.6 that Part V switches to
  natural units ($\hbar=c=1$, Heaviside–Lorentz) and why.
- **Cross-part links**: forward-reference by chapter number only (e.g. "Chapter 3.3"), and link with
  `<a href="ch3-3.html">` only if that file exists in `src/`; otherwise write the reference as plain
  text so no dead links ship.

---

# Book-wide conventions, fixed by the review of August 2026

The five-agent review over Parts 0–III found that most drift was vocabulary rather than physics.
These are now binding for every chapter, written and unwritten.

## Spelling and naming

- **British spelling.** `-ise`, `-isation` throughout: *linearise, quantise, renormalise,
  normalise, generalise, diagonalise, parametrise*. (The book had 482 British forms against 40
  American, all of the latter in Parts 0–I; they are now regularised.)
- **energy–momentum tensor**, en-dash, never "stress-energy". Chapters 3.4 and 3.6 cite 2.6 by that
  name and a reader following the pointer must find the same object.
- **Minkowski spacetime**, one word, one object. Never "Minkowski space".
- **Worked example N**, lowercase *e*, in the label and in every reference to it.
- **one-form** spelled out; every higher degree in numerals — `$2$-form`, `$3$-form`.
- **Rapidity is $\phi$** in Part II, where the scalar potential has not yet appeared, and
  **$\varphi$** from Chapter 2.6 onward, where it has. The clash is flagged in place at 2.6 §2.
- A **local inertial frame** is a region; **locally inertial coordinates** are the coordinates
  adapted to it. Fixed in 3.4 §6 and used consistently after.
- In the plain-terms boxes, $\Gamma$ is **the comparison coefficients**, named in full at 3.3.5.

## Structure, per chapter

Every chapter carries, without exception:

- an opening `where` callout, and exactly one closing `brick` whose last paragraph is led by the
  bolded **Where this gets spent.**
- at least one `familiar` callout. This is the device that connects new machinery to something the
  reader already knows, and it is the highest-value device in the book for this reader; Part II
  went six chapters without one and that was a defect, not a style.
- at least one `warn` callout, opening with ⚠ or ⚑. The title is free — *"⚠ The belief this section
  exists to prevent"* is as good as *"⚠ Why this isn't obvious"*, and bespoke titles are now the
  pattern rather than the exception.
- numbered sub-headings, `N.M · Title`, restarting inside each `<h2>`.

## The ⚑ contract

⚑ marks a result the book **uses but does not derive**. It is not decoration and it is not a
severity rating: a chapter with no ⚑ is claiming to have built everything it spends, and that claim
must be true. The review found eight unmarked imports in Part 0 alone — Heine–Cantor, Fubini,
Liouville on antiderivatives, the fundamental theorem of algebra, the implicit function theorem,
Picard–Lindelöf, generalised Stokes, the Poincaré lemma — several announcing themselves in words
while carrying no mark. Every one is now flagged, and `GAPS.md` is the standing register.

Forbidden, everywhere: *it can be shown*, *one can show*, *it turns out that*, *obviously*,
*clearly*, *of course*, *simply*, *just*, *trivially* — with two exceptions that are technical
terms rather than hedges, *simply connected* and *simply false*.

Address the reader in the **second person**. Never "the reader".

## Referring to sections and chapters

- **`§N` mid-sentence, `Section N` sentence-initially.** Part III already does this; Parts 0 and I
  open sentences with `§N`. The rule, not the count, is what is binding from here.
- **Link a chapter once, in the `Tools you'll need` line; plain text thereafter.** Every chapter
  already follows this. Never link a chapter that does not yet exist in `src/`.
- **Cite the statement, not the step it is read off from.** A result derived over four equations is
  cited at the one that states it.

## Two decisions the review asked for, made

- **Local `c = 1` is permitted inside a figure or a problem, where it is declared at the point of
  use** — "in units where $c=1$", "inside this figure only". Seven places in Part II already do this
  and all seven declare it. The convention above ("SI throughout Part II, with $c$ written
  explicitly") governs the running text, not a self-contained figure.
- **"is just X" stays where its job is to deflate intimidating notation** ("a Hermitian matrix is
  just a symmetric matrix with complex entries") and **goes where the thing being deflated is
  something the book worked for**. A result that cost three pages is not "just" anything.

## Physical constants

Use the **measured combination**, not a product of separately measured pieces. $GM_{\odot} =
1.32712440018\times10^{20}\ \mathrm{m^{3}s^{-2}}$ is known to ten significant figures; $G$ alone is
known to five, and $M_{\odot}$ is derived from the two. Writing $G\times M_{\odot}$ discards five
digits. It shifts Mercury's precession by 0.01″ and the solar light deflection by 0.0004″ — small,
but these are precisely the numbers a reader checks against a measurement, and the book's whole
claim is that its arithmetic can be reproduced.

The same applies to $GM_{\oplus} = 3.986004418\times10^{14}\ \mathrm{m^{3}s^{-2}}$.

---

# Register, from Part IV onward

Set by the reader, 22 August 2026, after twenty-eight chapters: *"the language remains fairly dry.
I am OK with that, but just slightly make it more approachable — run it through the lens of an
oncologist with a robust mathematical background at this point, but still building these concepts
from scratch."*

Read that carefully. It is **not** a request to soften the mathematics, add analogies, or merge the
main text into the warm register of the plain-terms boxes. Those boxes exist precisely so the main
text does not have to do that job, and the two-register structure stays. What changes is the
sentence-level texture of the derivations, in four specific ways.

**1 · Say why before what.** The dry failure mode is a correct step with its motive withheld until
after it lands. *"Differentiate under the integral sign"* becomes *"We want the derivative of the
whole integral, and the only thing in it that depends on the parameter is the integrand — so
differentiate under the sign."* Same step, same rigour, one clause of motive in front. This is the
single highest-yield change and it costs almost nothing in length.

**2 · Connectives, not asyndeton.** *because, so that, which means, and therefore, the reason is.*
Twenty-eight chapters of clipped declaratives read as a wall even when every sentence is clear. Let
a thought finish before the next begins. One long connected sentence often beats three short ones.

**3 · Address a colleague who does quantitative work daily.** He fits survival models, reads
Kaplan–Meier curves, thinks in hazard ratios and confidence intervals, and reasons about
dose–response every week. That fluency is a resource the main text may draw on directly, not only
inside a `familiar` callout — *"the same structure as a hazard that varies with time"* can sit in a
derivation where it is exactly right. **Only where the mathematics is genuinely identical**, and say
what breaks when it is not. A loose clinical analogy is worse here than no analogy, because he will
check it against what he knows.

**4 · Name the difficulty out loud when there is one.** *"This is the step where the finite-dimensional
argument stops working, and it is worth slowing down."* Not reassurance and not apology — an honest
signal about terrain, which a reader building from scratch has no other way to get.

## What does not change

- Nothing asserted that is not derived. The ⚑ contract is untouched.
- No hedges: the forbidden list stands — *obviously, clearly, of course, simply, just, it turns out
  that, it can be shown*.
- No chattiness. No *let's*, no exclamation marks, no rhetorical questions, no *imagine that*.
- Second person, as before. Not *we* as a stand-in for *you*, though *we* for genuinely shared work
  — "we now have two routes and they must agree" — is fine and always was.
- Grind boxes stay terse. They hold algebra; warmth there is noise.
- The plain-terms boxes keep their own voice, unchanged, and their own specification.

**The test.** Read a section aloud. If it sounds like a competent colleague working through
something at a whiteboard with you, it is right. If it sounds like a reference manual, apply items
1 and 2. If it sounds like a popular-science article, you have gone too far — go back.
