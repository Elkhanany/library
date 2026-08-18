# Language and editorial consistency audit

*25 chapters, `src/ch0-1.html` … `src/ch3-6.html`. Read in book order; mechanical checks by grep and
scripted extraction over the HTML sources only. No files were edited.*

---

## Verdict

The book's editorial machinery is in far better shape than a 25-chapter, multi-agent build has any
right to be: the chapter template is honoured 25/25, all 190 internal chapter links resolve, all 74
cross-chapter equation citations point inside their target chapter's range, there are zero broken
`eqref` anchors, zero exclamation marks in prose, and the 187 "In plain terms" boxes are numbered
correctly against the section each one closes without a single mismatch. What has drifted is almost
entirely at the level of vocabulary and of devices that were established early and then quietly
lapsed: the ⚑ mark is never used in Part 0 even where the text says out loud that it is quoting a
theorem, the `⚠ Why this isn't obvious` box disappears after Chapter 3.2, the Familiar Ground box
disappears for the whole of Part II, and British/American spelling is split down a Part 0/I versus
Part II/III line. Three cross-references are genuinely wrong and will send a reader to the wrong
place — those are the only findings that damage the reader's trust rather than merely the book's
tidiness.

---

## §1 Canonical terminology table

| Object | Names used | Where | Recommended canonical form |
|---|---|---|---|
| $T^{\mu\nu}$ | "stress-energy tensor" (2); "energy–momentum tensor" (10, en-dash); "energy-momentum tensor" (3, hyphen) | stress-energy: `ch2-6` §10.1 heading + §12. energy–momentum: `ch1-4` ×3, `ch2-5`, `ch3-4`, `ch3-6` ×5. energy-momentum: `ch0-7` ×3 | **energy–momentum tensor** (en-dash). This is the majority form *and* the form 3.4 and 3.6 use when they cite 2.6 — so 2.6's own section heading is the outlier. |
| $\omega_\mu$ / $\mathrm dx^\mu$ basis object | "covector" (68); "one-form" (31); "covariant vector" (2); "linear functional" (7, abstract-algebra sense) | covector dominates 2.4, 3.2, 3.3; one-form dominates 3.5 (18 v 3) and 0.6 (5 v 4) | **covector** in index/tensor contexts, **one-form** only inside the graded $p$-form calculus of 3.5. Synonymy is already introduced correctly and once, at `ch2-4.html:319` ("Definition — covariant vector (one-form, covector)") and `ch0-6.html:457`. No change needed to the introductions; see finding 22 for the residual `one-form` / `$1$-form` split. |
| $\phi$ with $\tanh\phi=\beta$ | "rapidity" (39); "hyperbolic angle" (3); "boost parameter" (1) | rapidity: 2.2, 2.3, 2.4, 2.5. hyperbolic angle: `ch2-3` §3.2 and §11 (deliberate, introduced at `ch2-3.html:440` under the heading "The rapidity is the angle"). boost parameter: `ch2-1.html:171` | **rapidity**. The "hyperbolic angle" synonym is correctly introduced once and flagged. `ch2-1`'s "boost parameter" means the Galilean boost *velocity* and predates rapidity — reword rather than rename (finding 18). |
| $\Gamma^\lambda{}_{\mu\nu}$ | "Christoffel symbols" (33); "connection coefficients" (12); "Levi-Civita connection" (2) | Christoffel: 3.3–3.6. connection coefficients: 3.3, 3.4, 3.6 | **Christoffel symbols** for the metric-derived object; keep "connection coefficients" only where the point is that a general connection is meant. Current usage already roughly follows this; no fix required. |
| $\Gamma$, in the plain-terms voice | "comparison rule" (3.3 boxes); "comparison coefficients" (3.4, 3.5 boxes); "the coefficients" (bare, 3.3) | `ch3-3` boxes 3.3.4–3.3.8; `ch3-4` boxes 3.4.3/3.4.7/3.4.8; `ch3-5` boxes 3.5.2/3.5.6 | **comparison coefficients**, introduced by that full name in `ch3-3`'s box 3.3.5 and used unchanged thereafter (finding 25). |
| The locally flat patch | "local inertial frame" (6); "locally inertial coordinates" (6) | local inertial frame: `ch3-1` ×4, `ch3-4`:958, `ch3-6`:1030. locally inertial coordinates: `ch3-4`:961 + 1194, `ch3-6` ×4 | Keep both but split the sense explicitly: **local inertial frame** = the physical region, **locally inertial coordinates** = the chart. `ch3-4` uses both within three lines of each other without saying they differ (finding 19). |
| $\eta_{\mu\nu}$ / $g_{\mu\nu}$ | "metric", "metric tensor" (10), "line element" (3), "the interval" | metric everywhere; metric tensor scattered; line element `ch2-3`, `ch3-3` ×2 | **metric** for the tensor, **line element** for $\mathrm ds^2$ written out, **the interval** for $\Delta s^2$. Current usage is already clean — no fix. |
| $F^{\mu\nu}$ | "field tensor" (15) | 2.3, 2.4, 2.6, 3.5 | **field tensor**. Fully consistent; "field strength tensor" and "Faraday tensor" appear nowhere. |
| $j^\mu$ | "four-current" (5) | 2.3, 2.6 | **four-current**. Consistent. |
| $R$ | "Ricci scalar" (10) | 3.4, 3.6 | **Ricci scalar**. `PLAN.md` says "scalar curvature"; the book has settled on Ricci scalar and should keep it — the plan is the outlier. |
| Four-index vectors | "four-vector" (106); "four vector" (1, unhyphenated) | `ch1-2.html:921` reads "four vector equations", which parses as *four equations* — a false positive, not a drift | **four-vector**. No fix. |
| $\mathbb{M}^4$ | "Minkowski space" (3); "Minkowski spacetime" (1) | space: `ch2-3`:1645, `ch3-3`:106. spacetime: `ch3-2`:13 | **Minkowski spacetime** (finding 23). |

---

## §2 Findings

### BLOCKER

**1 · ⚑ is never used in Part 0, in five places where the text openly says it is quoting.**
`README.md` states the rule as "Every quoted-not-derived step marked ⚑." Chapters 0.8 and 0.9 obey it
(Picard–Lindelöf, Fourier completeness, the CLT sketch all carry ⚑). Chapters 0.6 and 0.7 do not,
even though their prose is explicit. The five sites:

| File:line | Current string (unique) | Theorem quoted |
|---|---|---|
| `src/ch0-6.html:209` | `We are quoting the theorem rather than deriving it in the flow of the argument only` | continuous partials ⇒ differentiable |
| `src/ch0-6.html:878` | `is the implicit function theorem, which we quote;` | implicit function theorem |
| `src/ch0-7.html:74` | `we quote here and Chapter 0.8 states properly.)` | Picard–Lindelöf |
| `src/ch0-7.html:1020` | `We are quoting the general form, not deriving it: the machinery needed to define` | generalised Stokes |
| `src/ch0-7.html:1251` | `Poincaré lemma, which we quote here and Chapter 3.5 proves.` | Poincaré lemma |

Not a simple string swap. Each needs a ⚑ inserted at the head of the sentence, matching the house
pattern used from 1.1 onward — e.g. `ch0-7.html:1251` becomes
`Poincaré lemma. ⚑ Quoted here; Chapter 3.5 proves it.` Only `ch0-6.html:209` is arguably exempt,
because the theorem *is* proved in the grind box immediately below, in which case the sentence should
say so rather than say "we are quoting" (see finding 15).
*Why:* this is the book's foundational promise, and a reader who has learned to scan for ⚑ will read
Part 0 as fully derived when it is not.

**2 · `src/ch2-1.html:234` — cross-reference to a section that does not exist.**
Current: `$\epsilon_{0}$ and $\mu_{0}$ are measured, and §2.4 says exactly how.`
Replace: `$\epsilon_{0}$ and $\mu_{0}$ are measured, and §2.3 says exactly how.`
*Why:* Chapter 2.1 §2 has subsections 2.1, 2.2, 2.3 only. The permittivity and permeability
measurements are at lines 371–390, inside §2.3 ("Put the numbers in").

**3 · `src/ch0-7.html:1094` — cross-reference to the wrong section.**
Current: `here for the same reason as in Chapter 0.2 §6: the integrand and its $t$-derivative are continuous`
Replace: `here for the same reason as in Chapter 0.2 §4.4: the integrand and its $t$-derivative are continuous`
*Why:* Chapter 0.2 §6 is "Worked examples". Differentiating under the integral sign is §4.4, with the
hypotheses spelled out in its grind box ("when you may differentiate under the integral sign, and
when you may not", `ch0-2.html:660`).

**4 · `src/ch3-6.html:1254` — cites the wrong equation number, off by one.**
Current: `which is positive and is Chapter 2.6's (2.6.81).`
Replace: `which is positive and is Chapter 2.6's (2.6.82).`
*Why:* (2.6.81) is the intermediate step $F^{0\lambda}F_\lambda{}^0 = E^2/c^2$. The energy density
$\epsilon_0E^2/2 + B^2/2\mu_0$ that the sentence is comparing against is (2.6.82), id `e-T00`.

### MAJOR

**5 · `src/ch2-6.html:1558` — the one place the energy–momentum tensor is named "stress-energy".**
Current: `10.1 · The stress-energy tensor, from Noether`
Replace: `10.1 · The energy–momentum tensor, from Noether`
Also `src/ch2-6.html:2274`: `And the stress-energy tensor, whose $T^{00}$ is` →
`And the energy–momentum tensor, whose $T^{00}$ is`.
*Why:* `ch3-4.html:1173` and `ch3-6.html:59` both say "Chapter 2.6 built the energy–momentum tensor".
A reader following that pointer into 2.6 finds a section heading naming a different object.

**6 · `src/ch0-7.html` ×3 — en-dash/hyphen split on the same term.**
Current: `energy-momentum tensor` (line 1170), `energy-momentum conservation`, `energy-momentum`
Replace: `energy–momentum` (en-dash) in all three.
*Why:* every other chapter uses the en-dash; 0.7 is the only hyphen user.

**7 · `⚠ Why this isn't obvious` is absent from the last four chapters.**
Present in 21 of 25 chapters (1–4 per chapter, 25 boxes total, last at `ch3-2.html`). Zero in
`ch3-3.html`, `ch3-4.html`, `ch3-5.html`, `ch3-6.html`. Those chapters still carry `warn` boxes
(3.3 ×2, 3.4 ×2, 3.6 ×8) but under bespoke titles ("⚠ The belief this section exists to prevent",
"⚠ Read this against §2"). `ch3-5.html` has **no `warn` box at all** — the only chapter in the book.
Not a string swap: either retitle one box per chapter to the standard form, or accept the bespoke
titles as the new pattern and say so in `CONVENTIONS.md`. Whichever is chosen, 3.5 needs at least one
`warn`.
*Why:* `PLAN.md` §2 names this as one of two recurring devices; a reader who has met it 25 times will
notice its disappearance exactly where the material gets hardest.

**8 · The `familiar` callout is absent from Chapter 1.4 and all six chapters of Part II.**
Distribution: one per chapter in 0.1–1.3; **zero** in 1.4, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6; back to one
or two per chapter in 3.1–3.6. Seven consecutive chapters with none.
Not a string swap — this needs authoring, not editing. The obvious candidates already exist in the
prose and are currently unmarked: 2.5's rest-energy bookkeeping, 2.6's "magnetism is electrostatics
in a moving frame" (`ch2-6.html:1117`), 2.2's muon flux.
*Why:* `PLAN.md` §2 item 3 makes Familiar Ground a per-chapter obligation of the math doctrine, and
the reader is a physician for whom it is the highest-value device in the book.

**9 · British/American spelling splits along a Part 0–I / Part II–III line — 35 instances.**
The book is British: 482 `-ise` forms against 40 `-ize`, and Parts II and III are 100 % `-ise`. Every
American form is in Part 0 or Part I. Straight swaps, all unique enough to grep:

| File:line | Current | Replace |
|---|---|---|
| `ch0-1.html:14` | `does not generalize.` | `does not generalise.` |
| `ch0-1.html:361, 419, 433, 496` | `linearization` | `linearisation` |
| `ch0-1.html:526` | `the form that generalizes:` | `the form that generalises:` |
| `ch0-2.html:145, 1059` | `linearization` | `linearisation` |
| `ch0-2.html:183, 754, 1085` | `renormalization` / `Renormalization` | `renormalisation` / `Renormalisation` |
| `ch0-2.html:918` | `dimensional regularization` | `dimensional regularisation` |
| `ch0-2.html:1088` | `linearizing is quadratic` | `linearising is quadratic` |
| `ch0-3.html:26` | `linearization, higher derivatives` | `linearisation, higher derivatives` |
| `ch0-3.html:216` | `will ever have to linearize:` | `will ever have to linearise:` |
| `ch0-3.html:1045` | `renormalization group.` | `renormalisation group.` |
| `ch0-4.html:12` | `we linearize everything` | `we linearise everything` |
| `ch0-4.html:28, 1077` | `linearization` | `linearisation` |
| `ch0-7.html:140, 736` | `linearization` | `linearisation` |
| `ch1-1.html:297` | `under the name renormalization` | `under the name renormalisation` |
| `ch1-2.html:264` | `3.2 · Move two: linearize the integrand` | `3.2 · Move two: linearise the integrand` |
| `ch1-2.html:835, 949, 1316, 1488` | `generalized` | `generalised` |
| `ch1-2.html:1608` | `differentiate under the integral, linearize,` | `differentiate under the integral, linearise,` |
| `ch1-3.html:27` | `the one that quantizes` | `the one that quantises` |
| `ch1-3.html:396` | `form in the generalized velocities` | `form in the generalised velocities` |
| `ch1-3.html:1220` | `Canonical quantization, in one line` | `Canonical quantisation, in one line` |
| `ch1-4.html:1021` | `invariant under it, quantize.` | `invariant under it, quantise.` |
| `ch1-4.html:1052, 1333` | `quantization` | `quantisation` |

*Why:* "linearisation" is the book's own name for its most-emphasised idea, and Chapter 0.1 — which
coins it — spells it the opposite way from Chapters 0.8, 3.1 and 3.4, which cite it.

**10 · `src/ch2-2.html:1066` — `brick` class used for a mid-chapter forward-pointer box.**
Current: `<div class="callout brick">` with `<span class="ct">Two forward pointers, flagged ⚑</span>`
Replace: `<div class="callout warn">` with the same title.
*Why:* `brick` is the chapter-closing summary class, used exactly once per chapter in the other 24
chapters and always as the last block. Every other ⚑-titled callout in the book (20 of 20) is `warn`.
This box sits at §7 of a nine-section chapter and is styled as a chapter conclusion.

**11 · `src/ch3-5.html:656` — the general-$p$ Poincaré lemma is asserted, not derived, and not flagged.**
Current: `The verification is the four lines of the main text with more indices, and rather than sketch it`
Replace: prefix the claim sentence with the standard mark, e.g.
`⚑ The verification is the four lines of the main text with more indices; rather than sketch it`
*Why:* the homotopy formula $\mathrm d(K\omega)+K(\mathrm d\omega)=\omega$ for general $p$ is stated
and used, with only the $p=2$ case done explicitly. Chapter 3.5 currently carries zero ⚑ marks, and
this is the one place it needs one.

**12 · Sub-section headings are unnumbered in four chapters and numbered in the other twenty-one.**
`ch0-1.html` (5/5 unnumbered), `ch0-3.html` (16/16), `ch0-4.html` (14/14), `ch0-5.html` (20/20) use
bare `<h3>` titles. Every chapter from 0.6 onward uses `N.M · Title`. Two single stragglers:
`ch0-2.html:61` (`What "the limit exists" is doing here`) and `ch0-8.html:67`
(`Initial conditions, and the mathematical content of determinism`).
Not a string swap — 57 headings need numbers assigned in order within their parent `<h2>`.
*Why:* the book makes 1387 `§N.M` references. No reference currently points into an unnumbered
subsection, so nothing is broken today, but any future "Chapter 0.4 §6.1" would be unresolvable, and
the sidebar TOC (`assets/book.js` `buildTOC`) renders these four chapters visibly differently.

**13 · `Worked Example N` (capital E) versus `Worked example N` — 32 against 55.**
The box label is *always* lowercase (`Worked example 1 — …`, 50 boxes). Cross-references are split:
`ch2-1`, `ch2-3`, `ch1-2`, `ch2-5`, `ch2-6`, `ch3-1` use lowercase; `ch0-3`, `ch0-6`, `ch0-9`,
`ch1-3`, `ch1-4`, `ch3-2`, `ch3-3` (×6), `ch3-4` (×5), `ch3-6` use capital.
Global replace `Worked Example ` → `Worked example ` (32 sites). Safe: no box label uses the capital.
*Why:* the label and the reference to it should read the same.

### MINOR

**14 · Hedging phrases the house style forbids.** Each is a short local rewrite:

| File:line | Current string | Suggested replacement |
|---|---|---|
| `ch0-6.html:984` | `The minimum of $x$ on it is obviously at the origin.` | `The minimum of $x$ on it is at the origin.` |
| `ch0-6.html:1286` | `should of course get the same answer)` | `should get the same answer)` |
| `ch2-2.html:689` | `matching the traveller's own clock, obviously, since it is his` | `matching the traveller's own clock, since it is his` |
| `ch1-4.html:566` | `is not conserved — of course not, something` | `is not conserved, and it should not be: something` |
| `ch2-4.html:371` | `which is, of course, the change in $f$` | `which is the change in $f$` |
| `ch2-6.html:154` | `and one simply adds their four-currents` | `and one adds their four-currents` |
| `ch2-6.html:311` | `each entry simply picks up $\eta_{\mu\mu}\eta_{\nu\nu}$` | `each entry picks up $\eta_{\mu\mu}\eta_{\nu\nu}$` |
| `ch3-3.html:927` | `The derivative terms simply collect:` | `The derivative terms collect:` |
| `ch3-3.html:1262` | `simply appeared, because only the symmetric` | `appeared, because only the symmetric` |
| `ch0-8.html:1697` | `So the wave equation is simply` | `So the wave equation is` |
| `ch0-6.html:980` | `Drop it and the method can simply be` | `Drop it and the method can be` |
| `ch0-5.html:842` | `simply hands you several basis vectors` | `hands you several basis vectors` |
| `ch0-1.html:57` | `the number simply converges.` | `the number converges.` |
| `ch3-4.html:3` | `It turns out to measure the tide.` | `It measures the tide.` |
| `ch3-3.html:503` | `It turns out not to` | `It does not` |
| `ch3-3.html:1613` | `governed by it turns out to be Chapter 3.1's tidal equation` | `governed by it is Chapter 3.1's tidal equation` |
| `ch3-5.html:1576` | `where it turns out to separate the two halves` | `where it separates the two halves` |
| `ch3-6.html:424` | `it turns out to be a total derivative` | `it is a total derivative` |
| `ch3-2.html:287` | `and it turns out to have precisely $n$ independent components` | `and it has precisely $n$ independent components` |
| `ch2-2.html:568` | `Velocity, it turns out, is simply` | `Velocity is` |

*Why:* all are on the explicit prohibition list. Note the ~50 remaining hits of "simply" are the
technical term "simply connected" or the emphatic negation "simply false / simply does not apply",
neither of which is the forbidden hedge — leave those alone.

**15 · `src/ch0-6.html:209` — the sentence contradicts the grind box directly beneath it.**
Current: `We are quoting the theorem rather than deriving it in the flow of the argument only`
Replace: `We state the theorem here rather than deriving it in the flow of the argument only`
*Why:* the same paragraph ends "but it is written out below, because this book does not say 'it can
be shown'", and the grind box at line 212 proves it. It is not quoted; it is deferred.

**16 · `src/ch2-6.html:719` and `src/ch2-6.html:1529` — the only two `warn` boxes with no ⚠/⚑ prefix.**
Current titles: `Where gauge freedom is going` and `A note on units, before Part V`
Replace: `⚠ Where gauge freedom is going` and `⚠ A note on units, before Part V`
*Why:* 83 of 85 `warn` boxes open with ⚠ or ⚑. These two are styled amber but carry no marker.

**17 · Three third-person references to "the reader", against second-person address everywhere else.**

| File:line | Current | Replace |
|---|---|---|
| `ch2-4.html:972` | `And the reader who has been kept waiting since Chapter 0.7 §4.4 should now be doing the arithmetic` | `And if you have been kept waiting since Chapter 0.7 §4.4, you should now be doing the arithmetic` |
| `ch3-3.html:268` | `it is worth stating them now so that the reader knows what is coming` | `it is worth stating them now so that you know what is coming` |
| `ch3-4.html:250` | `so the plan comes first and the reader should be able to` | `so the plan comes first and you should be able to` |

**18 · `src/ch2-1.html:171` — "boost parameter" collides with the rapidity vocabulary of 2.2–2.5.**
Current: `and the boost parameter must be constant for the argument of §1.3 to go through`
Replace: `and the boost velocity must be constant for the argument of §1.3 to go through`
*Why:* this means the Galilean relative velocity $v$, but "boost parameter" is the standard synonym
for rapidity, which the book introduces one chapter later.

**19 · `src/ch3-4.html:958` / `:961` — "local inertial frame" and "Locally inertial coordinates" three lines apart, undistinguished.**
Not a string swap. Add one clause at line 958 fixing the two senses, e.g.
`…which also settles what a "local inertial frame" is — a region — and what the "locally inertial
coordinates" adapted to it are.` Then the six later uses in `ch3-6` read correctly.

**20 · `src/ch2-6.html:187–211` — $\phi$ is introduced as the electric scalar potential with no note that it carried rapidity in 2.2–2.5.**
Not a string swap. Add one sentence after `ch2-6.html:211`
(`A^{\mu} \equiv (\phi/c,\ \vv A)`), in the style the book already uses at `ch2-6.html:1348`
("an unfortunate clash of symbols that the whole subject lives with") and `ch2-3.html:238`.
*Why:* `CONVENTIONS.md` mandates both $\phi$ = rapidity and $A^\mu=(\phi/c,\vv A)$. The book flags
its other symbol clashes explicitly; this one, the sharpest, goes unremarked.

**21 · Two "simply" in `plain` boxes, which the plain-terms spec bans by name.**
`PLAIN-TERMS-PLAN.md` §3 "Don't" lists *simply*, *just*, *of course*.

| File:line | Current | Replace |
|---|---|---|
| `ch2-4.html:463` | `the covector simply counts how many of its sheets` | `the covector counts how many of its sheets` |
| `ch2-4.html:796` | `Complex tensors are simply layered combinations` | `Complex tensors are layered combinations` |

(The third hit, `ch3-4.html:489` "the long computation just finished", is temporal and fine. Overall
the 187 plain boxes are clean — 0 display equations, 0 boxes over two inline symbols, 0 exclamations.)

**22 · `src/ch3-5.html` mixes spelled-out and numeral form degrees.**
`one-form` (18) alongside `$1$-form` (8); `two-form` (4) alongside `$2$-form` (15). Pick one rule.
Recommended, because it matches the rest of the book and the graded calculus equally well: spell out
**one-form** (the object is named that way in 0.6, 2.4, 3.2), and use numerals for every other degree
— so replace the eight `$1$-form` in `ch3-5.html` (lines 165, 552, 593, 756, 863, 1627, 1714, 1799)
and the one in `ch2-6.html:572` with `one-form`, and replace `two-form` at `ch3-5.html:207, 306, 316,
1808` with `$2$-form`.

**23 · `src/ch3-3.html:106` and `src/ch2-3.html:1645` — "Minkowski space" against `ch3-2.html:13`'s "Minkowski spacetime".**
Replace `Minkowski space` with `Minkowski spacetime` at both sites.
*Why:* the book is otherwise scrupulous about "spacetime" as one word and one object.

**24 · `src/ch1-1.html` — the only chapter whose closing brick has no labelled "Where this gets spent."**
24 of 25 bricks contain the bolded run `Where this gets spent.`; `ch1-1.html` does not.
Not a string swap: the *content* is present, woven into the prose (each of the four failures already
names its answering chapter). The fix is to split the last third of that brick out under the standard
bold lead so the chapter closes the way the other 24 do.

**25 · Plain-terms name for $\Gamma$ shifts between chapters.**
`ch3-3` boxes call it "the comparison rule" and then "the coefficients"; `ch3-4` and `ch3-5` boxes
call it "the comparison coefficients". Not a string swap: introduce the full phrase once, in
`ch3-3.html:658` (box 3.3.5, currently "The coefficients do not respond to relabelling…"),
and use "the comparison coefficients" from there on.
*Why:* `PLAIN-TERMS-PLAN.md` §2 requires recurring motifs to be named "by the same words each time".

**26 · `src/ch1-2.html:589` — lone lowercase problem reference.**
Current: `problem 4 shows you may add any total time derivative`
Replace: `Problem 4 shows you may add any total time derivative`
*Why:* the other 177 references are capitalised.

**27 · `src/ch3-6.html:1225` — "the source-free Lagrangian density as (2.6.72)" describes an equation that has the source term in it.**
Current: `Chapter 2.6 §9 gave the source-free Lagrangian density as (2.6.72)`
Replace: `Chapter 2.6 §9 gave the electromagnetic Lagrangian density as (2.6.72), whose source-free part is`
*Why:* (2.6.72) is $\mathcal L_{\text{EM}} = -F_{\mu\nu}F^{\mu\nu}/4\mu_0 - j_\mu A^\mu$; the second
term is exactly the source coupling.

**28 · `src/ch3-5.html:1247` — the citation for metric compatibility points at a derivation step rather than the statement.**
Current: `recorded there as (3.3.38), says $\nabla_{\lambda}g_{\mu\nu}=0$`
Replace: `imposed there in §7.1 as $\nabla_{\lambda}g_{\mu\nu}=0$ and used in the form (3.3.41)`
*Why:* (3.3.38) is $\mathrm d/\mathrm d\lambda(g_{\mu\nu}V^\mu W^\nu) = (u^\rho\nabla_\rho
g_{\mu\nu})V^\mu W^\nu$ — the step from which compatibility is *read off*. The statement itself
appears only inline in §7.1 prose; the numbered form is (3.3.41).

---

## §3 Patterns, not instances

**A · The devices were established early and lapse late; nobody re-read Part 0 after the rules were
finalised.** Three independent symptoms point at the same cause. The ⚑ mark is absent from Part 0's
quoted theorems but present from 1.1 onward (finding 1). `-ize` spellings are confined entirely to
Part 0 and Part I (finding 9). Sub-section numbering is absent from 0.1, 0.3, 0.4, 0.5 and present
everywhere else (finding 12). The right remedy is one back-fill pass over 0.1–0.7 against the
conventions as they now stand, rather than 40 individual fixes.

**B · The reverse also happens: devices established early are dropped at the far end.**
`⚠ Why this isn't obvious` stops at 3.2; `familiar` stops for the whole of Part II. These are
opposite failures with the same root — the house style lives in `CONVENTIONS.md`, which is scoped
"fixed across all six chapters" of Part II only. A one-page global style sheet covering the callout
taxonomy, the ⚑ rule, spelling, and the section-reference format would prevent recurrence better
than any of the individual fixes above.

**C · "is just X" as a diminisher, ~90 occurrences book-wide.** Distinct from the forbidden hedge
"just do X", and mostly doing useful work ("a Hermitian matrix is just a symmetric matrix",
"here it is just the chain rule"). But the density is high enough that a reader meets it every two or
three pages. Rather than 90 edits, adopt a rule: keep it where the sentence's job is to *deflate* a
piece of intimidating notation; cut it where the thing being deflated is a result the book worked
for. Roughly a third of the instances are the second kind.

**D · Sentence-initial section references are split between `§N` (58) and `Section N` (86), and the
split is chronological, not grammatical.** Part 0 and Part I open sentences with `§N`; Part III
opens them with `Section N` (3.3–3.6 alone account for 55 of the 86). Both forms appear
sentence-initially inside the same chapters. Adopt one rule — "`§N` mid-sentence, `Section N`
sentence-initially" is the more readable and is what Part III already does — and sweep once.

**E · `insight` is a catch-all carrying five different rhetorical jobs.** Of 156 boxes: 119 genuine
insights, 15 `Definition — …`, 8 `Theorem/Lemma/Claim`, 9 `Recap — what went in, what came out`, and
5 `Where we are going` (which duplicates the `where` class's job). This is not wrong — the styling
is neutral enough to carry it — but a `def` variant and a `recap` variant would let the sidebar TOC
and any future index distinguish a definition from an aside, and would cost one CSS rule each.

**F · Cross-chapter references are linked opportunistically, not by rule.** Every chapter mentions
several *existing* chapters in prose without linking them (e.g. `ch3-3.html` mentions Chapter 3.1
six times and never links it; `ch2-4.html` mentions eleven existing chapters unlinked). The de facto
pattern is "link in the `Tools you'll need` line, plain text thereafter", which is defensible and
which every chapter follows — but Parts II and III never forward-link even to files that exist
(`ch2-1` and `ch2-2` link forward to `ch2-4`; no Part III chapter links forward at all, and
`ch3-6.html` has zero inbound links from anywhere). Decide the rule and state it in `CONVENTIONS.md`;
do not hand-fix 200 sites.

**G · `c = 1` is adopted locally in Part II in seven places, each honestly declared, against
`CONVENTIONS.md`'s "SI throughout Part II, with $c$ written explicitly".** `ch2-3.html:635, 881, 940,
1367, 1447, 1562` and `ch2-5.html:745`. Every one says so at the point of use ("in units where
$c=1$", "Inside this figure only"), so nothing is misleading. Either amend the convention to permit
declared local unit choices in problems and figures, or convert those seven. This is a decision, not
a defect.

---

## §4 What is already good

The chapter template is honoured without exception: all 25 chapters open with `eyebrow → h1 →
subtitle → where` callout at line 4 → `Tools you'll need` paragraph, carry `N · Worked examples` and
`N · Your turn` as their last two `<h2>`s, and close with a single `brick` callout as the final
block. `<h2>` numbering is a correct 1..N sequence in all 25.

Cross-reference integrity is genuinely strong. All 190 `<a href="chN-M.html">` targets exist; zero
broken `eqref` anchors across 1,378 numbered equations; all 74 cross-chapter equation citations fall
inside their target chapter's equation count, and every one I opened matched its claim except the
single off-by-one in finding 4. Every "Chapter N.M" mentioned in prose exists in `PLAN.md`'s
curriculum, and no reference to an unwritten chapter is a link. I spot-checked 34 "as Chapter X §Y
proved/showed/gave" claims by opening the target section; 31 were exactly right, and the three that
were not are findings 2, 3 and 4.

The ⚑ system, from Chapter 1.1 onward, is used with more care than the brief assumed: it correctly
covers quoted mathematics, quoted experimental numbers, and results promised forward, and 20 of 20
⚑-titled callouts sit in the `warn` class. I found no false flag — no ⚑ marking something the book
had in fact derived.

The "In plain terms" apparatus is the cleanest thing in the repository. 187 boxes, every one numbered
`chapter.section`, and every number matching the section it actually closes — 0 mismatches. Zero
display equations, zero boxes carrying more than two inline symbols, and only two uses of a banned
word across roughly 40,000 words.

Prose discipline holds where it matters most: not one exclamation mark in prose anywhere in the book,
"it can be shown" appears zero times, and the recurring labels (`Grind box —`, `Solution`,
`Worked example N`, `Problem N`, `Where we are`, `Tools you'll need`, `The brick you just laid`) are
identical across all 25 chapters.
