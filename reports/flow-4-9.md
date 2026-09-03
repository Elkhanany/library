# Narrative-flow review — `src/ch4-9.html`, "Commutators, Uncertainty, and Symmetry"

Read start to finish, in order, as a first read. Twenty-four entries, ordered by position in the
chapter — twenty-three stalls carrying one of the brief's six modes, plus one assessment (item 10)
that answers a question rather than reporting a stall.

By mode: **1** — 6 · **2** — 0 · **3** — 2 · **4** — 6 · **5** — 7 · **6** — 2.

This chapter is a collection, and the two things a collection can do wrong are both present: the
largest payoff arrives already paid, and one section hands the reader a bibliography where it
promised a proof. Neither is fatal. Both are locatable to a paragraph.

---

## 1 · "Where we are", first and third paragraphs — **mode 5**

> "Six results built elsewhere meet in this chapter, and all six were built with this meeting in
> mind."

and, four sentences later,

> "Section 1 is the shortest in the chapter and it pays six of Chapter 0.9's promises with one
> multiplication."

Two different sixes in one box. The first is six results from six different chapters — 0.9, 0.5, 4.2,
1.3, 1.4, 4.6 — and the reader has just been handed the list. The second is six promises all made by
Chapter 0.9. Reading forward, the two fuse: the reader takes the route paragraph to be saying that
§1 discharges the six-item list he was given a moment ago. §1 discharges one of them. He works this
out somewhere in §2 and has to re-read the box.

**What the reader needed:** the second six not to be a six, or the first list not to be counted.

---

## 2 · "Where we are", route paragraph — **mode 5**

> "Section 6 runs the symmetry chain in full for translation, rotation and time, and hands Chapter
> 4.11 the one commutator its entire chapter is built on. Sections 7 and 8 are worked examples and
> problems."

The route stops there. §6.5 (a symmetry with no generator) and §6.6 (what the commutator has *not*
told us, and the hand-off to Chapter 4.10's no-go theorem) get no notice. §6.6 is the chapter's
closing argument — it is where the chapter says what it has not done and why the next one is needed,
and it is the paragraph the whole book's forward structure runs through. A reader budgeting his
evening from the route budgets for a chapter that ends on the rotation table.

**What the reader needed:** that §6 ends by naming what is missing, and that the missing thing is the
classical limit.

---

## 3 · Conventions paragraph — **mode 5**, minor

> "**One thing is quoted rather than derived**, and it carries the chapter's single mark, in §2.6:
> the error–disturbance relations, a pair of named theorems about apparatus rather than about
> states"

One thing, immediately glossed as a pair. §2.6 does reconcile this later ("Both relations above are
covered by this box's mark, and it is the only one in the chapter"), but the reader meets the
mismatch first and carries it for two sections. The same construction — a count followed by a list
that disagrees with it — tripped this reader in Chapter 4.7's conventions paragraph.

**What the reader needed:** the count and the list to agree at first reading, or the reconciliation
in the same sentence.

---

## 4 · §1 as a whole, and equation `e-dxdp` — **mode 3**, and the chapter's central problem

> "That is the whole of it, and the promise Chapter 0.9 made is now discharged in the form it was
> made. **The inequality was never quantum.**"

This is the anticlimax, and it has a mechanical cause that a linear reader finds and a checker cannot.

**The debt was discharged one chapter ago, and the reader was told so.** Chapter 4.8 §6.1 — in the
chapter he finished last night — says: *"Chapter 0.9 §6's bandwidth theorem bounds the product of a
function's width and its transform's width from below, and Chapter 4.6 §10.2 turned that into
$\Delta x\,\Delta p\ge\hbar/2$ using the single substitution $p=\hbar k$."* He has already seen the
inequality stated, already been told which chapter made the substitution, and already watched the
oscillator ground state sit exactly on the bound with numbers attached. Chapter 4.8's closing brick
then hands off to *"Chapter 4.9 §2"* — not §1. Nothing prepared him for §1 to exist.

So §1 opens by telling him three times, before the line arrives, that it is about to pay a three-part
debt: the subtitle ("makes the substitution in a line"), the route paragraph ("pays six of Chapter
0.9's promises with one multiplication"), and §1's own opening ("This section has one line of
mathematics in it, and the line is a multiplication. That is not brevity for its own sake"). Three
pre-emptive defences against an objection he has not made, for a payment he believes he already
received. His reaction is not "at last" but "wait — didn't I have this?"

It gets worse when he tries to reconcile the two accounts. §1.2 credits Chapter 4.6 **§5.5** and
**§10.6**. Chapter 4.8 credited Chapter 4.6 **§10.2**. He cannot line them up without leaving the
book.

**And `e-dxdp` is glossed only about where it came from.** Every sentence after the display is about
provenance: never quantum, the mystery is in the substitution, arithmetic you did in Part 0. Nothing
says what he can now *see*. There is no scale, no instance, no number anywhere near the most
anticipated equation in the chapter — the first number attached to it arrives in §2.7, many pages
later, and is about oscillator eigenstates. The display that has been waiting three parts is the one
major display in the chapter with no instance beside it.

**What the reader needed:** to be told, before §1 begins, that he has met this result already and
what §1 adds that Chapter 4.6 did not — and, after the display, one sentence saying what the
inequality now forbids in the world rather than where it came from.

---

## 5 · §1.3 and In plain terms 4.9.1 — **mode 1**, and a flat contradiction

§1.3, third paragraph:

> "Whether the *inequality* holds for those other pairs is a separate question, and a more delicate
> one than it looks."

In plain terms 4.9.1, one screen later, closing sentence:

> "So the same bound applies to an angle and its angular momentum, in the same form, with the same
> constant, without any adjustment. That is not luck. It is what 'conjugate' was defined to mean."

§2.5 then calls precisely that statement *"the naive reading of §1.3"* and says *"That statement is
false."* Worked example 2 exhibits a state where the left-hand side is exactly zero, and its repair is
to replace the angle — which is an adjustment.

The plain-terms box is the box this reader reads for the takeaway. It drops the caveat raised in the
paragraph directly above it and states, as the section's summary, the thing the next section calls
false. He recovers at §2.5, but he spends the intervening pages holding a wrong result confidently.

**What the reader needed:** the plain-terms box to carry the same qualification the main text raised
three paragraphs earlier — that what is paid here is the dimensional half only.

---

## 6 · §2.3 onward: $\Delta A$ against $\Delta\hat A$ — **mode 4**, and the chapter's worst notation trap

> "abbreviating $\Delta\hat A=\hat A-a$ and $\Delta\hat B=\hat B-b$"

$\Delta A$ has meant a standard deviation since the Conventions paragraph. $\Delta\hat A$ is now an
operator. They differ by one hat and they appear inside the same display — `e-schrod` carries
$(\Delta A)^{2}(\Delta B)^{2}$ on the left and $\{\Delta\hat A,\Delta\hat B\}$ on the right.

The Conventions paragraph makes this actively worse: *"Hats stay on operators and come off their
values."* Applied here, that rule says $\Delta A$ is the value of $\Delta\hat A$ — which is zero.
$\Delta A$ is not the expectation of $\Delta\hat A$; it is the norm of $\Delta\hat A\ket\psi$. The
chapter's own stated convention hands the reader the wrong object, once, silently, at the exact point
the notation is introduced.

The pair then recurs at long range with no reminder: the figure caption, Worked example 1(a),
Problem 1(a) ("the covariance $\tfrac12\avg{\{\Delta\hat x,\Delta\hat p\}}$"), Problem 2(d), where
$(\Delta x)^{2}$ and $\avg{\{\Delta\hat x,\Delta\hat p\}}$ sit in one equation.

**What the reader needed:** one sentence at `e-fgop` saying that $\Delta A$ is not $\avg{\Delta\hat A}$
and stating which of the two the hat distinguishes.

---

## 7 · §2.4 — **mode 5**

> "The figure below is the geometry of that difference."

The figure is not below. Between that sentence and the figure sit §2.5 (two hypotheses and a domain
argument), §2.6 (a full-page warn box carrying two imported theorems), and §2.7 (two numerical
checks) — about a hundred and thirty lines. The reader either scrolls now and loses all three, or
holds an unresolved pointer through the densest run in the chapter.

**What the reader needed:** to be told the figure comes after the caveats, or not to be pointed at it
until it is in view.

---

## 8 · §2.5, third paragraph — **mode 1**

> "The other hypothesis fails in the most quoted example after position and momentum."

Paragraph one is the domain hypothesis. Paragraph two opens "A second hypothesis is easier to miss"
and spends a paragraph on the existence of moments. Paragraph three says "the other hypothesis" and
means the *first* one. "The other" reads as "the one not yet discussed", and both have been
discussed. He re-reads two paragraphs to find out which is meant, and the answer is confirmed only in
Worked example 2(b), at the end of the chapter, where the failing step is identified as `e-fgop`.

**What the reader needed:** the hypothesis named rather than ordinalised, since the two are not
adjacent any more.

---

## 9 · §2.6, the Ozawa relation — **mode 3**

> "What holds instead carries two extra terms,
> $\varepsilon(A)\eta(B)+\varepsilon(A)\,\Delta B+\Delta A\,\eta(B)\ge\tfrac12\abs{\avg{[\hat A,\hat B]}}$,
> in which $\Delta A$ and $\Delta B$ are the very spreads of `e-robertson`."

The result is stated with its hypotheses and the text moves straight to Busch–Lahti–Werner. Nothing
says what the two extra terms *do*. This is the chapter's single quoted import, the one thing it
takes on trust, and it is the display in the chapter that most needs a gloss — because a reader who
cannot read the corrected relation cannot tell why the naive one failed.

**What the reader needed:** what the extra terms buy — that a measurement can be very accurate on $A$
without forcing a large disturbance of $B$, provided the state's own spreads are wide, which is
exactly what the naive product got wrong.

---

## 10 · §2.6 as a whole — the brief's direct question

The box's first paragraph is excellent and it does its job completely. *"No system in that ensemble is
measured twice"* is the sentence that settles it, and *"It is a constraint on what can be prepared"*
is the sentence he will carry.

But the box promises a two-way separation and delivers a three-way one. The title says "what the
relation does not say, and the theorems that say the other thing" — *the* other thing, singular.
Paragraph two says *"Measurement disturbance is real, it is a different quantity, and it has theorems
of its own."* Then two theorems arrive that disagree with each other: under Ozawa's definitions the
naive Heisenberg product is *false*, and under Busch–Lahti–Werner's it is *true after all*. The
closing paragraph handles this correctly — "They bound different quantities" — but never gives the
reader a way to tell them apart in the wild.

So: coming out of §2.6 he knows preparation is not disturbance, cleanly and permanently. He does not
know which of the two disturbance theorems he is looking at when he next meets a claim, and given
that the box exists because "this is where most of the damage in popular accounts is done", the
diagnostic is the thing it was for.

**What the reader needed:** one sentence saying which question each definition answers, in the form
he would recognise a claim by — calibration against sharp reference states, or error in the one input
state at hand.

---

## 11 · §2.7 figure caption, right panel — **mode 4**

> "the picture is drawn with that radius scaled to one. The *horizontal* coordinate is the covariance
> $\tfrac12\avg{\{\Delta\hat A,\Delta\hat B\}}$ and the *vertical* coordinate is
> $\tfrac12\abs{\avg{[\hat A,\hat B]}}$"

The drawn axes are those quantities *divided by* $\Delta A\,\Delta B$ — the plotting code labels them
"covariance / Dx Dp" and "half commutator / Dx Dp", and the caption's own "scaled to one" says as
much. But the sentence naming the coordinates names the unnormalised quantities. Taken literally, the
Gaussian ground state has vertical coordinate $\hbar/2$ against a circle of radius one, and cannot be
"at the top of the circle" as the caption then says it is. He tries the caption's worked instance and
it does not close.

**What the reader needed:** the normalisation carried into the sentence that names the coordinates,
not left in the sentence before it.

---

## 12 · §2.7 familiar-ground box — **mode 6**

The map, element by element:

- $\Delta A$ ↔ sample standard deviation over $N$ patients. **Holds**, and the box is right that it is
  the same arithmetic.
- ensemble of identically prepared systems ↔ a cohort. **Does not hold**, and the box says so itself
  and uses the failure — this is the analogy working properly.
- hidden variable ↔ unmeasured covariate. **Holds**, and is named.
- *"a better preparation could in principle narrow both marginals at once, exactly as identifying a
  covariate narrows a response distribution."* **Does not hold**, and this one is not flagged.

Identifying a covariate does not narrow a response distribution. It narrows the *conditional*
distribution inside a stratum; the marginal is untouched, and no patient changes. On the physics side,
preparation is an intervention — a different preparation produces a genuinely different ensemble with
a genuinely different marginal. The element with no counterpart is the intervention itself: there is
nothing you *do* on the clinical side, and "exactly as" claims a correspondence the map does not have.

The conclusion the box draws is correct and the box is honest about the limits of what it proves. It
is the bridge sentence that will not bear weight, and this reader is the one person guaranteed to lean
on it.

**What the reader needed:** the clinical side of that clause to be stratification and not narrowing,
so the disanalogy — that a preparation is an act and a covariate is a discovery — is visible rather
than papered over.

---

## 13 · §3.3, the theorem statement — **mode 4**

> "*...has all its common eigenspaces one-dimensional if and only if every observable that commutes
> with all of them is a function of them.*"

"A function of them" is the operative phrase in both directions of the proof and in every later use
of the criterion, and its meaning is entirely in a citation ("in the sense of Chapter 0.5 §7") that
arrives three sentences *after* the theorem, inside the forward proof, as
$\hat C=\sum c(a_{1},\dots,a_{m})\hat P_{(a)}$. A function of an operator is not the ordinary meaning
of "function", and the reader meets the theorem's load-bearing term with nothing to hold.

**What the reader needed:** what "a function of" means for operators, before the theorem that turns on
it — the spectral sum, not the address of the chapter that built it.

---

## 14 · §3.4, opening — **mode 1**

> "The theorem is what makes the criterion trustworthy, and the following is what anyone actually
> does with it. Since the joint eigenvectors form a basis, a set is complete exactly when the
> *number of distinct eigenvalue tuples equals the dimension of the space*."

The count criterion follows from the *definition* (one-dimensional common eigenspaces) plus the basis
property. §3.3's maximality theorem is not used to get it and is not used again. A reader who has just
worked through both directions of §3.3 is told on the next page that the theorem underwrites the
practical test, and then watches the practical test be derived without it.

**What the reader needed:** what §3.3 buys that §3.4 could not get on its own — or, if it buys
nothing operational, to be told that its job is to make the definition safe rather than to power the
count.

---

## 15 · §3.5, closing paragraph — **mode 1**

> "One caution carries forward unchanged, and Chapter 4.2 §4.3 stated it with a figure to go with it.
> The theorem promises that a common eigenbasis *exists*. It does not promise that a numerical
> eigensolver hands you that one"

The heading is "What the criterion becomes in infinite dimensions". This paragraph is about a
finite-dimensional numerical hazard — a solver returning an arbitrary basis inside a degenerate
eigenspace. It has nothing to do with infinite dimensions, nothing to do with the paragraph above it,
and it is the third topic under a two-topic heading. This is the paragraph where §3 most reads as an
inventory rather than an argument.

**What the reader needed:** to be told this is a separate caution being parked before §4 begins, not a
consequence of the infinite-dimensional discussion.

---

## 16 · §3, section end — **mode 5**

§3 is the only body section with no pause brick after it and no closing statement of what is now in
hand in the main text. It ends on the eigensolver caution, then a plain-terms box, then §4 begins. The
other seams are excellent — §1→§2 ("It is worth saying what has *not* been proved by that line,
because §2 exists to prove it") is the best seam in the chapter, and the pause bricks after §2, §4 and
§5 all name what is coming. §3 gets neither.

**What the reader needed:** what he now holds — a test he can run, and where it will be run — before
the chapter changes subject from a single instant to time.

---

## 17 · §4.3, `e-heisderiv` → `e-heis` — **mode 1**

> "The first two terms combine, because $\hat H\hat A-\hat A\hat H$ is the commutator by definition,
> and a $\hat U\hat U^{\dagger}=\hat I$ can be inserted between the operator and the Hamiltonian to
> convert each factor separately into its Heisenberg form."

Two things stop him. The operations are given in the wrong order — the insertion has to happen before
anything can be read off as a commutator, and the sentence puts it second, as an afterthought. And the
sign is not accounted for: what the two terms give is $\tfrac{\ii}{\hbar}[\hat H,\hat A]_{H}$, and the
display carries $\tfrac{1}{\ii\hbar}[\hat A_{H},\hat H]$ — two flips, neither mentioned. He puts a
pencil to it, gets there, and loses a minute in the one section where the chapter is doing fresh work.

**What the reader needed:** the insertion first, and one clause acknowledging that both the bracket
order and the $\ii$ move to the other side.

---

## 18 · §5.1, `e-ophamilton` → `e-ehrenfest` — **mode 4**

> "Everything needed is already in `e-ophamilton`. Neither $\hat x$ nor $\hat p$ carries an explicit
> time, so the last term is absent, and taking expectations of those two operator identities gives
> **Ehrenfest's relations**"

`e-ophamilton` is one-dimensional: $\hat x$, $\hat p$, $V'(\hat x_{H})$. `e-ehrenfest` is three-
dimensional: $\hat{\vv x}$, $\hat{\vv p}$, $\nabla V$. The dimension changes silently across a step the
text says is nothing but taking expectations, and $\hat{\vv x}$ and $\nabla V$ appear here for the
first time in the chapter. The whole of §4 was scalar.

**What the reader needed:** that the promotion to three dimensions is componentwise and free, said
where it happens.

---

## 19 · §5.3 warn box — **mode 6**, minor, inside the chapter's best analogy

> "That is false for any function with curvature, for exactly the reason a skewed dose–response curve
> has a mean response that is not the response at the mean dose."

The analogy itself maps cleanly on all four elements — $V'$ ↔ the response curve, the packet's spread
in $x$ ↔ the spread of doses, $\avg{V'(\hat x)}$ ↔ the mean response, $V'(\avg{\hat x})$ ↔ the response
at the mean dose — and it is the best clinical bridge in the chapter. One word is wrong. Skewness is a
property of the *dose distribution*; what breaks the substitution is curvature of the *curve*. A
perfectly symmetric spread of doses over a curved response fails just as badly. The sentence says
"curvature" and then names skew, in the one analogy this reader will check hardest.

**What the reader needed:** the same property named twice — curvature on both sides of the bridge.

---

## 20 · §6.1 — **mode 5**, and the point where the chapter becomes an inventory

§6's opening promises:

> "**Chapter 4.2 states the correspondence; this section proves it**"

§6.1 then delivers the proof as five bullets, and every one of them is a citation: "Chapter 4.2 §7.2
showed", "Stone's theorem produces", "Chapter 4.2's second postulate requires, in the corrected form
Chapter 4.4 §4.2 gave it", "Chapter 4.2 §7.5 expanded", "by `e-conserved`". Nothing is shown. The
reader was promised a proof and handed a bibliography with five entries.

**This is where the thread stops and the inventory starts.** It is not §2's long run of caveats —
those are announced ("Then we spend rather longer on what the result means") and each earns itself. It
is not §3.4's three examples — those are instances he can check. It is §6.1, because it is the one
place the chapter says it is about to *do* something and instead lists where it was already done.
Everything after it recovers — §6.2 and §6.3 are among the best passages in the chapter, precisely
because they compute — but the recovery is his, not the text's.

There is a second, smaller thing in bullet one. "A map preserving all probabilities preserves all
norms" is a compression, and the text honestly flags that linearity is assumed rather than derived. It
never says what is being assumed away. The antiunitary alternative is not exotic here: parity arrives
in §6.5 and time reversal is coming.

**What the reader needed:** at least one link shown rather than cited — the chain is the section's
whole content — and, at the linearity bullet, what the excluded alternative is.

---

## 21 · §6.3, the sign sentence — **mode 1**, and the worst line-level stall in the chapter

> "...the survivors are $[\hat y\hat p_{z},\hat z\hat p_{x}]=\hat y[\hat p_{z},\hat z]\hat p_{x}
> =-\ii\hbar\,\hat y\hat p_{x}$ and $[\hat z\hat p_{y},\hat x\hat p_{z}]=\hat x[\hat z,\hat p_{z}]\hat p_{y}
> =+\ii\hbar\,\hat x\hat p_{y}$, **both entering with a plus sign once the two minus signs in the
> expansion have been multiplied together.**"

The first survivor carries no minus sign in the expansion at all — it is the leading term,
$[\hat y\hat p_{z},\hat z\hat p_{x}]$, and it enters with a plus because it always did. Only the
fourth term, $[\hat z\hat p_{y},\hat x\hat p_{z}]$, picks up two minus signs and multiplies them
together. The stated reason accounts for one of the two survivors and is offered as the reason for
both.

The answer is right — the sum is $\ii\hbar(\hat x\hat p_{y}-\hat y\hat p_{x})=\ii\hbar\hat L_{z}$ —
and both survivors do enter positively. But this is the computation the text has just called the one
that "buys the whole of Chapter 4.11", and it is therefore the one place in the chapter where a reader
will check every sign by hand. He checks, finds the explanation does not fit the first term, and has
to reconstruct the expansion himself to convince himself the result stands.

**What the reader needed:** the four terms and their signs written out, or the sentence to describe
only the term it describes.

---

## 22 · §6.3, "Two consequences" — **mode 5**, minor

> "Two consequences, and then the hand-off. First, feeding `e-Lalg` into `e-robertson` gives..."

The next paragraph opens "That is the third of §2.7's checks, and it can be run now that the
commutator exists." That paragraph *is* the second consequence, but it opens as a continuation of the
first, and the word "Second" never comes. He reads to the end of §6.3 looking for it.

---

## 23 · §6.5, $\hat\Pi$ — **mode 4**, minor

> "since $\hat\Pi^{2}=\hat I$ leaves it only two eigenvalues"

Parity is introduced two sentences earlier as "the map $\psi(x)\mapsto\psi(-x)$" and is never given a
symbol. $\hat\Pi$ appears once, at the end of the paragraph, unnamed. Chapter 4.7 §2 presumably named
it; this chapter does not, and this is its only appearance here.

---

## 24 · $\hat T$, three meanings — **mode 4**

$\hat T(a)$ is the translation family (§6.2). $\hat T=\hat p^{2}/2m$ is kinetic energy (Problem 3c).
$\hat T=\hat Z_{1}+\hat Z_{2}$ is the total which-state observable (Problem 4). Each is defined where
it is used, and no single use is wrong. But it is one letter carrying three jobs inside one chapter,
for a reader the brief describes as short of working memory for unfamiliar notation, and the three
uses are close enough together that Problem 3's $\hat T$ and Problem 4's $\hat T$ sit on adjacent
pages. The same is true of $a$ — $\avg{\hat A}$ in §2.3, the translation distance in §6.2, the complex
Gaussian width in Problem 1, the eigenvalue index in §3.

**What the reader needed:** one of the three renamed, most cheaply the translation family, which is
used in one subsection and one table row.

---

# What did not go wrong

**Mode 2 is clean.** Every one of the chapter's twenty-five numbered displays is set up before it
arrives. `e-leibniz` is the closest to an exception — its lead-in describes the derivation before the
purpose — and even there "One rule does almost all of the work" comes first. For a chapter with this
many equations, that is a real result and it is worth saying so rather than padding the list above.

**The three parallel cases in §6 do not go flat, and the design is why.** §6.2 (translation) does the
full construction: unitarity, the group law, strong continuity in one line, then differentiation to
the generator. §6.3 (rotation) is the longest and carries five distinct beats — the generator, the
algebra, the correspondence predicting something it was never postulated for, the uncertainty
consequence, the numerical check, the hand-off. §6.4 (time) is one paragraph and *announces itself as
free*: "The third case needs no work, because Chapter 4.6 did it before the pattern was visible." The
flat case is last and is labelled flat. That is the right order and it should be kept.

**The seams are mostly excellent.** §1→§2 ("§2 exists to prove it"), the three pause bricks, and §3's
opening ("Section 2 asked what happens when a commutator is large. This section asks what happens when
it is zero") are all doing exactly what the brief's mode 5 asks for.

---

# A stretch that reads unusually well

**§5.3 through §5.5**, the whole run from the warning box to the two-potential table. It is the only
place in the chapter that does the full arc in one movement: a claim, a distinction stated as two
labelled alternatives (a) and (b) that differ by one symbol, a mechanism for the gap (the Taylor
term, controlled by $V'''$ and $(\Delta x)^{2}$), a consequence that closes the question ("That is
three potentials and no more"), and then a measurement that separates the physics from the arithmetic:

> "Those residuals belong to the integrator rather than to the theorem, and here is how you know:
> halving $\dd t$ divides them by four, three times running, which is the second-order error of the
> splitting doing what second-order errors do. The theorem is exact and the arithmetic is not."

That sentence is the best in the chapter. It teaches a habit rather than a fact, and it is the one
place a reader learns *how to tell* rather than *what is true*. The closing move of §5.4 — that
exactness in the mean is a weak property, because an oscillator eigenstate satisfies the classical
equation with both sides zero forever — is the second best, because it takes away something the reader
was about to over-claim.

Two runners-up worth naming: **§4.2**, for "The claim has consequences you can check rather than
admire", and **Worked example 2**, which locates a failing step, computes the boundary term the
failure leaves behind, and repairs the statement — four moves, in order, with nothing skipped. It is
the chapter's best piece of technical writing and it is the only place the angle debt raised in §1.3
is actually paid.

---

# Summary judgements

## Could a reader who understood Chapter 4.8 follow this one straight through?

**Yes.** There is no point where it becomes impossible. The chapter's dependencies are almost all on
chapters more than one back — 0.5, 0.9, 1.3, 1.4, 4.2, 4.6 — and it restates enough of each for the
sentences to mean something; §1.1's recap of the bandwidth theorem and §4.4's term-by-term comparison
with the classical equation of motion are both models of how to do it. Every stall above is local and
recoverable.

The one place he is at risk of walking away *confidently wrong* rather than merely stalled is In plain
terms 4.9.1 (finding 5): the box states as the section's takeaway a claim that §2.5 calls false. He
recovers, because §2.5 names it explicitly as "the naive reading of §1.3" — but a reader who reads the
plain-terms boxes as summaries and skims between them, which is what those boxes are for, carries the
wrong statement from §1 to §2.5 with nothing warning him.

## Does it sound like the same hand as `src/ch3-6.html` and `src/ch4-2.html`?

**Yes.** All the house apparatus is present and used the same way: the eyebrow/title/thesis-subtitle
opening, the "Where we are" box with a route paragraph and a Conventions paragraph, the "Tools you'll
need" address list, ⚑ for quoted-not-derived and ⚠ for a trap, numbered "In plain terms" boxes,
"Familiar ground", the closing brick. The sentence rhythm matches — short declarative followed by a
qualifying clause, and the habit of saying what is *not* being claimed ("rather than" runs 47 times
here against 59 in 4.2 and 28 in 3.6, all in range).

**One tell, and it is a matter of degree rather than of voice.** The construction "an earlier chapter
promised this, and here it is" runs about twenty-five times — roughly one every seven hundred words.
"In advance" appears 8 times against 5 in 4.2 and 0 in 3.6; "said so / in those words / said in as
many words" appears 6 times against 2 and 0. The chapter is about discharging debts, so some of the
elevation is the subject rather than the writer. But past a point it stops being emphasis and becomes
the chapter's only mode of introducing a result: almost every payoff here is framed as the settling of
an account rather than as something the reader now knows. That is the same hand, writing under a
structural load the other two chapters do not carry — 3.6 corners one equation three ways, 4.2 lays out
a table of renamings, and both have a spine that is theirs. This one's spine is other chapters'
promises, and the prose has taken the shape of a ledger.
