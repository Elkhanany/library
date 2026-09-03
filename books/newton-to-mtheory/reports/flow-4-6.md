# Narrative-flow review — `src/ch4-6.html`, "The Schrödinger Equation"

Read linearly, first line to last, once. Fourteen places where I stalled, in order of appearance.
Weight varies a lot; I have said where an item is minor rather than dressing all fourteen alike.

Two things this chapter does *not* have, and both are worth saying before the list because they are
the failures I went looking for hardest and did not find. **There is no failure mode 2 in this
chapter.** Every display I can find is motivated before it arrives — including the awkward ones
(`e-gaugep`, `e-divid`, `e-kinav`), where the lead-in sentence states the purpose and the display
then does exactly that. And **the two extended analogies both hold** (§7.3 diffusion/tissue, §10.4
water waves); I checked them element by element and they check out. Detail under items 9 and 13.

---

## 1 · Front matter — the subtitle promises one thing and the Conventions block, three paragraphs later, says three

> *"The only physics added anywhere in this chapter is the choice of which operator the generator is,
> and that choice is marked where it is made."* (subtitle)

> *"Three results are quoted rather than derived, and each is marked where it arrives: … and de
> Broglie's relation for matter in §10.6."* (Conventions)

**Failure mode 1.** Stone–von Neumann is mathematics and can be excused from the word "physics". De
Broglie's relation cannot: §10.6 labels it *"Experimental input, not derived"* and puts Davisson and
Germer underneath it. So the count in the first sentence a reader reads is wrong by one, and it is
wrong in the direction that matters for a book whose whole method is marking what it assumes. The
brick at the end says "Three marks", correctly. The subtitle says one.

*What the reader needed:* the subtitle to scope its claim — one physical choice inside the
derivation, one experimental input where the numbers arrive — or to say "one choice and one
measurement." As it stands the reader arrives at §10.6 having been told there would be nothing there.

---

## 2 · §1.2 — the section is named for a trichotomy it does not state until its last sentence

> *"Before going on it is worth asking what the alternative would have looked like, because the
> answer is that there is no alternative."*

**Failure mode 5.** The heading is "There is no third option." Third of what? The reader has just
come off §1.1, whose live question is isometry-versus-unitary — a *two*-way distinction — so the
natural (wrong) reading is that §1.2 continues it. The actual three options are |λ|<1, |λ|=1, |λ|>1,
and they are named only in the closing sentence: *"A factor of modulus less than one is decay, a
factor of modulus greater than one is growth, and probability permits neither."* The reader carries
an unresolved "the alternative to *what*?" through the whole subsection.

There is a second, smaller cost. §1.2 sits between §1.1, which opens the isometry/unitary gap, and
§1.3, which closes it. It is a digression at the one point where a thread is deliberately left
hanging, and the reader has to hold the hanging thread across it.

*What the reader needed:* the three cases stated in the lead-in rather than the exit line.

---

## 3 · §1.4 — a pattern the reader is instructed to watch for, and told to expect twice, appears once with a flag

> *"That is a pattern worth registering, because the same argument appears twice more in this
> chapter: a group law turns a statement at one point into a statement everywhere."*

**Failure mode 1, minor.** This creates a reading obligation. §3.1 discharges half of it explicitly
(*"The group law does the work, in the same move §1.4 used"*). The second instance — §3.3's *"a state
that starts in dom(Ĥ) stays there for all time, so the equation holds along the whole trajectory once
it holds at the start"* — is the same shape but is nowhere marked as the second, and it runs on
commuting rather than on the group law, so a reader checking against the sentence above cannot
confirm it is the one meant. A reader who took the instruction seriously spends the rest of the
chapter half-looking for something that is never labelled.

*What the reader needed:* the second instance flagged where it occurs, in the same words the first
one got, or the count not promised.

---

## 4 · §3.1 — **the worst stall in the chapter.** The equation the chapter is named after arrives at the tail of a caveats paragraph and is never read

> *"Every step there is legitimate for a reason worth naming. The middle equality is the group law
> together with the fact that Û(t) is bounded, so it passes through the limit. The last equality is
> Chapter 4.5 §9.2 … Finally, Û(t) and Ĥ commute, because both are functions of the same self-adjoint
> operator in the sense of Chapter 4.5 §6.6, so Û(t)Ĥψ = ĤÛ(t)ψ. **Multiply by iℏ and write
> |ψ(t)⟩ = Û(t)|ψ(0)⟩. What is left is the equation this chapter is named after:**"*

**Failure mode 3.** Four separate things go wrong at this one seam, and they compound:

**(a) The instruction that produces the equation is the fifth sentence of a paragraph about domains,
boundedness and commuting.** The paragraph's announced job is bookkeeping ("Every step there is
legitimate for a reason worth naming"), and the arrival is smuggled into its last two clauses. A
reader tracking the paragraph's stated purpose has already downshifted.

**(b) Nothing reads the equation.** The box goes up and the very next words are *"and its solution,
which is the exponential we started from"*, then a paragraph about which forward pointers this pays.
No sentence says what the two sides are. The gloss the reader needs — the left side is a rate of
turning, iℏ converts a rate of turning into an energy, the right side is the energy operator applied
to the state — exists in this chapter, but it is in §6.1, three sections later, attached to the *PDE*
form: *"Read across it once. The left-hand side is a rate, with iℏ converting the rate at which a
phase turns into an energy…"* That is exactly the move §3.1 needed and did not make.

**(c) The chapter's own road-map says §3 does it.** The "Where we are" block: *"Section 3
differentiates and reads the equation."* It differentiates. It does not read.

**(d) The box is not new, and the text does not say so at the box.** `ch4-2.html` line 1125 already
carries the identical display, boxed, with the identical lead-in shape (*"gives the equation the next
chapter is named after"*). A reader who remembers Chapter 4.2 sees the same box again with no
acknowledgement that this time it has been earned rather than reached in finite dimensions; the
acknowledgement is there but it is in §3.2, a subsection later, and it is phrased as a debt being
settled rather than as the thing that just happened. A reader who does not remember 4.2 gets no
reading at all.

The emotional shape is the specific casualty. Three chapters of domains, spectra and self-adjointness
converge here, the chapter has been telling the reader since the subtitle that this is where the
payment falls, §3's own opening says *"All the work is done and this section collects the payment"* —
and then the payment is handed over inside a footnote about why a limit may be passed through a
bounded operator. Compare the same writer in `ch3-6.html`: *"Put that value of κ back into the boxed
result of §3, and there, at last, are the field equations of general relativity."* The house style
does mark arrivals. This one is unmarked.

*What the reader needed:* the derivation's housekeeping finished and closed, then the multiplication
by iℏ standing on its own; and immediately after the box, one sentence reading it — what the left
side is, what the right side is, what iℏ is doing between them — before any cross-reference is paid.

---

## 5 · §4.4 — the Coulomb Hamiltonian is written in position representation two sections before the position representation exists

> *"The Coulomb Hamiltonian −(ℏ²/2m)∇² − e²/4πε₀r has a ladder of negative eigenvalues accumulating
> at zero…"*

**Failure mode 4**, in its forward form: the reader has to go *ahead* rather than back. At this point
p̂ = −iℏ∇ has not been written (§5.2) and p̂² = −ℏ²∇² has not been computed (§6.1, `e-psquared`).
The chapter has been unusually strict about not spending what it has not earned — §2.5 stops to say
what an exponential of an unbounded operator even means — so the lapse is conspicuous here rather
than in a looser book. The reader either recognises the expression from elsewhere, which the chapter
elsewhere refuses to rely on, or stalls.

The same paragraph carries a second, smaller version of it: *"So §9.3 below applies to it word for
word."* §9.3 is five sections ahead and has not been characterised; the reader cannot evaluate the
claim, and cannot even tell whether it is load-bearing. It is also inserted between two sentences
that belong together (the spectrum, and *"which closes the oscillator's route before it opens"*).

*What the reader needed:* the Coulomb operator written abstractly here, or one clause saying that its
differential form is §6's and is being borrowed.

---

## 6 · §5.4 — the exponentiated commutator is displayed and never connected to the commutator

> *"Suppose they satisfy the exponentiated form of the canonical commutator,"* → display → *"Suppose
> further that the representation is **irreducible**…"*

**Failure mode 3.** The display Â(a)B̂(b) = e^{−iab/ℏ} B̂(b)Â(a) is stated and stepped over. Nothing
says why this is the exponentiated form of [x̂,p̂] = iℏ — where the e^{−iab/ℏ} comes from, or that it
is the group-level version of the same relation. Two paragraphs later the callout leans hard on
exactly that connection: *"The exponentiated form is essential and the commutator alone is not
enough."* A reader who could not read the display cannot feel the force of that sentence, and it is
the sentence the whole hypothesis discussion turns on. He is then asked to accept that momentum on a
half-line satisfies one form and not the other, which is a distinction between two things he has been
given only one of.

*What the reader needed:* one sentence between the display and "Suppose further" saying that this is
what [x̂,p̂] = iℏ becomes when both operators are exponentiated, so that the reader can see the two
forms as two statements of one relation and then be told they are not equivalent.

---

## 7 · §6.2 — the subsection ends with a second, different reason for the Laplacian, unsupported

> *"The kinetic term of the Schrödinger equation is a Laplacian, and the reason is the one that puts a
> Laplacian into Poisson's equation as well: a second derivative is what a rotationally symmetric
> quadratic form in ∇ has to be."*

**Failure mode 1.** The subsection has just given a clean and complete reason — kinetic energy is
multiplication by p²/2m in the momentum representation, and the transform turns multiplication by k
into differentiation. Then the last clause offers a *different* reason, from a different direction,
in a sentence that is neither derived nor pointed anywhere. The two are not reconciled and the reader
is left holding two explanations with no statement of how they relate, or which is the one to carry.
The section opened by saying the Laplacian *"deserves a sentence of explanation rather than being left
as the output of an algebraic substitution."* It gets two, and the second one is itself left as an
assertion.

*What the reader needed:* either the sentence to say how the symmetry argument and the Fourier
argument are the same argument, or the sentence to be somewhere it can be supported.

---

## 8 · §7.3 — σ₀ and σ(t) do the load-bearing work of the disanalogy 450 lines before either is defined

> *"A free quantum packet widens as σ(t) = √(σ₀² + (ℏt/2mσ₀)²), which §10 derives, and which grows
> **linearly** in t once t is large."*

**Failure mode 4.** First occurrence of σ₀ anywhere in the chapter (line 996); first definition at
line 1452 (*"a normal distribution of standard deviation σ₀"*). It is not defined in Chapter 4.5
either — I checked; the symbol does not occur there. So a reader meeting this line has no way to read
the formula, and the formula is the entire content of the paragraph: this is the middle of three
places where the clinical analogy is said to break, and the break is the difference between √t and t.
He can take the *conclusion* on trust, but he cannot check the sentence that follows and justifies it
(*"the spread in velocity that was fixed at the start"*) against anything.

Same paragraph, minor: *"so the packet drifts apart at constant rates"* — plural "rates" with no
antecedent set.

*What the reader needed:* four words saying σ₀ is the packet's starting width. Everything else in the
box is self-contained.

---

## 9 · §8.4 — the Liouville comparison, and the element with no counterpart

> *"Liouville's theorem says the density of representative points in phase space is carried along by
> the classical flow without being compressed or created, which makes classical probability conserved
> as an identity rather than an assumption. Unitarity is the Hilbert-space version of that sentence,
> and `e-current` is its local form."*

**Failure mode 6**, and the weakest item on this list — I include it because the brief asks for
element-by-element checking and this is the one comparison in the chapter where an element genuinely
has no counterpart. The map has three terms:

| classical | quantum | holds? |
|---|---|---|
| Liouville's theorem (flow preserves the measure) | unitarity (flow preserves the norm) | yes |
| conservation is an identity of the equations, not a postulate | same | yes — and this is the real point, and it lands |
| the phase-space continuity equation | ∂ρ/∂t + ∇·**J** = 0 | **no** |

The classical density is on phase space; ρ = |ψ|² is on configuration space, and its classical
counterpart is the *marginal* of the phase-space density over momenta, not the density itself. There
is no quantum joint position–momentum density for **J** to be the current of — which is, in a book
that has just spent §5.4 on why x̂ and p̂ cannot be simultaneously diagonalised, exactly the thing the
reader has been trained to notice. The comparison is two sentences and hedged ("the Hilbert-space
version of that sentence"), so this is not the Chapter 4.1 failure of an analogy closing a gap; it is
a slogan that a careful reader will try to cash and find one term short.

Minor and related: *"and `e-current` is its local form"* — the antecedent of "its" is ambiguous
between "unitarity" and "that sentence", and the two readings differ in exactly the way above.

**For contrast — the two analogies that do hold, checked term by term:**

*§7.3, diffusion in tissue.* Presented as a disanalogy list, which is the safe form. All three named
breaks are correct: (i) diffusion conserves ∫C dV, quantum conserves ∫|ψ|² dV and not ∫ψ dV — right,
and the observation that the two roles which coincide classically come apart here *is* the Born rule;
(ii) √(Dt) against linear-in-t, with the mechanism correctly attributed (repeated collisions, variance
adds / initial velocity spread, positions separate) — and the arithmetic matches: Δv = ℏ/2mσ₀ from
`e-packetk` gives exactly σ² = σ₀² + (Δv·t)²; (iii) information loss. I looked for a fourth unnamed
break and could not find one that the three do not already cover.

*§10.4, water waves.* Deep water v_p = 2v_g is right (ω = √(gk)); crests running forward through the
group in deep water is right; the free particle reversing it is right.

---

## 10 · §8.6 → §8.7 — the Ehrenfest subsection opens with a consequence of nothing named

> *"One consequence belongs in your hands now even though its proof belongs elsewhere."*

**Failure mode 1.** A consequence of what? §8.6 has just been about what Chapters 4.7 and 4.10 do with
**J**; §8.7 then produces Hamilton's equations for expectations, half of which follows from §8 and
half of which explicitly does not (*"the second needs machinery this chapter does not have"*). The
thread that makes this subsection belong here was laid in §4.3 — *"Section 8 below supplies the piece
of that argument which belongs in this chapter"* — but §8.7 never reaches back for it. The forward
pointer exists; the back-pointer does not, and it is the back-pointer the reader needs, because he is
four sections downstream and has been through the whole current derivation since.

*What the reader needed:* the first clause to say this is the classical-limit evidence §4.3 promised
and deferred, so that a subsection which is half off-topic for §8 has a reason to be in §8.

---

## 11 · §9.3 — the heading asserts what the subsection's last paragraph retracts, and §4.4's forward pointer is never collected

> Heading: *"Every solution is a superposition of these"*
>
> Middle: *"Every solvable problem in Chapters 4.7, 4.8 and 4.13 is that line plus a
> diagonalisation."*
>
> Last paragraph: *"The expansion is legitimate exactly when the spectrum is pure point and the
> eigenvectors are complete … and **fails** for a Hamiltonian with a continuous part."*

**Failure mode 5**, with a dropped thread (mode 1) inside it. Three problems, and they interlock:

- The heading over-claims and the closing paragraph takes it back. A reader who read the heading and
  the first two paragraphs has already filed a general result that the third paragraph conditions.
- The middle paragraph names **Chapter 4.13** — hydrogen — as an instance of the expansion, and §4.4
  has already told this same reader that hydrogen's *"bound states span the point-spectrum subspace
  and are not a basis of L²(ℝ³)"*. So he is holding a flat contradiction between two paragraphs of
  the same chapter, and neither one acknowledges the other.
- §4.4 pointed here explicitly: *"So §9.3 below applies to it word for word."* §9.3 never mentions
  hydrogen, or Coulomb, or Chapter 4.13 in that context — its examples of the failure are the step,
  the barrier and the free particle. The promise made in §4.4 is not collected at the address it
  names, and the one place in §9.3 where hydrogen *is* named is on the wrong side of the argument.

This is the second-worst stall in the chapter and the only one where the reader is likely to conclude
that the text has contradicted itself rather than that he has misread.

*What the reader needed:* the condition attached where the claim is first made rather than at the end;
and §9.3 to name hydrogen as the case §4.4 sent forward, on the side of the ledger §4.4 put it on.

---

## 12 · §10 — the section's road-map ends at §10.5, and then three subsections follow

> *"By the end we will have a formula for the width of a packet at any time and a number for how long
> an electron stays where you put it."*

**Failure mode 5.** Both promised objects are delivered by the end of §10.5. §10.6 (de Broglie,
marked experimental input), §10.7 (the numerical figure) and §10.8 (the convergence tests) then
follow, unannounced. This matters more than usual for §10.6 specifically, because it is one of the
chapter's three flagged assumptions and the reader has been told at the top of the section that the
section is finished before it arrives. §10 also has the chapter's only marked input that the subtitle
denied existed (item 1), so it lands twice unprepared.

*What the reader needed:* the section opening to name what is coming after the numbers — that the
experimental input those numbers rest on gets marked, and that the formula gets checked against a
direct integration.

---

## 13 · §10.4 — the crest passage is correct term for term; one pronoun is not

I checked this paragraph against the equations in front of it, clause by clause, because it is the
most picture-dependent stretch in the chapter. **It holds.** Recording that in full, because a
negative result here is worth as much as a finding:

- v_g = dω/dk at k₀ with ω = ℏk²/2m gives ℏk₀/m = p₀/m ✓ (and matches `e-packetrho`).
- v_p = ω/k = ℏk₀/2m, *"half as fast"* ✓.
- *"each crest drifts **backwards** at v_p − v_g = −ℏk₀/2m"* ✓ — sign and magnitude both right.
- *"a crest is continually born at the leading edge of the packet and dies at the trailing edge"* ✓ —
  this is the correct consequence of backward drift relative to the envelope, and it is the clause
  most likely to have been written the wrong way round. It is not.
- *"in deep water v_p = 2v_g, so crests there run forward through the group, and a free particle does
  the reverse"* ✓ on all three counts.
- §2.4 set this up in advance and correctly: *"Only the direction is being used here, and not the
  speed, which is E/p = p/2m rather than p/m; §10.4 is where that mismatch is taken up."* The debt is
  named there and paid here.

The one thing that stalls:

> *"**That factor of two** is a standing reminder that the wave and the particle are different
> objects."*

**Failure mode 4, minor.** There are two factors of two in the two preceding clauses, running in
opposite directions — the quantum one (v_p = v_g/2) and the deep-water one (v_p = 2v_g) — and "that
factor of two" sits immediately after the water one. The reader has to decide which is meant in a
paragraph whose entire point is that the two cases are reversed. It is the one sentence in an
otherwise exact passage where the referent has to be reconstructed.

---

## 14 · §10.7 figure caption — an unexplained sign reversal, offered as one of three things to watch

> *"In the free case the current is positive across the body of the packet and the packet spreads,
> though far out in the trailing tail, where the density has fallen to a few parts in a hundred
> thousand of its peak, the current turns negative."*

**Failure mode 3.** The statement is true, and I am glad it is there rather than airbrushed. But it is
stated and left. The reader has been given, in §8.3, *"the current has exactly the classical form,
density times velocity"*, and in §10.4, a packet whose centre moves right at v_g; he now watches a
right-moving free packet with a region of leftward current and is told to *watch* it. There is
nothing in the chapter that lets him reconcile the three, and the natural inference — that something
is wrong with §10.4, or with the integrator — is the wrong one.

*What the reader needed:* one clause saying that the spreading itself is a flow, so the local velocity
is v_g plus a term proportional to the displacement from the centre, which turns negative far enough
behind it. That is a statement about `e-jphase` and the chirp in the grind box, both of which are
already in the chapter.

---

# A stretch that reads unusually well

**§8.1 through §8.3, the probability current.** This is the chapter's method working at full
strength, and it is the section the writer should read back to himself before touching §3.

- §8.1 states the thing to be proved *and why the thing already proved is not it*: *"a global
  statement about a number is much weaker than the physical claim anyone actually wants, which is
  that probability does not vanish here and reappear there."* Then it names the constraint that makes
  it a real question rather than an exercise: *"Nothing may be chosen to make the equation come out:
  ρ = |ψ|² is not negotiable, so either a **J** exists that fits it or the claim of local conservation
  is false."* The reader now has stakes and knows what failure would look like.
- §8.2 runs five displays and every one of them is motivated before it arrives and read after it. The
  load-bearing step is *named as* load-bearing rather than left to be noticed: *"The conjugation used
  one property of V and it is the property the whole result rests on: V is **real**."* The divergence
  identity is checked rather than quoted, with a reason given for checking it. The final equality gets
  a one-line arithmetic gloss (z − z*) so that no reader is left wondering where the 2i went.
- §8.3 reads the result immediately — modulus and phase, **J** = ρ∇S/m — and then extracts the two
  consequences that make it worth having, including the one that overturns a natural picture (*"the
  shape of |ψ| says nothing about the flow"*). The figure exists to show exactly that and nothing else.
- §8.5 then shows what breaks if the load-bearing property fails, which retroactively justifies why
  §8.2 stopped to name it.

Second place, briefly: **§7.2**, which settles the chapter's most quotable claim in one display and
three sentences, with the moduli compared rather than the formulas. And **§6.1's** annotated display
plus *"Read across it once"* — which is, precisely, the move §3.1 owed the reader and did not make.

---

# Summary judgements

## Could a reader who understood Chapter 4.5 follow this one straight through?

**Yes.** There is no point at which it becomes impossible, and I want to be unambiguous about that
because the list above is long. The section seams are the strongest thing in the chapter: every §
opens by saying what it will produce and closes by saying what is now in hand, the three `pause`
markers are placed at genuine rests, and the "Where we are" route is accurate about §§1–2 and §§4–10.
A reader who has 4.5 can get from the first line to the last without going backwards.

Three places make him proceed on trust rather than on understanding, none fatal:

1. **§7.3**, where σ₀ is undefined (item 8) — he can accept the conclusion, not check it.
2. **§9.3**, where he is holding a contradiction with §4.4 about hydrogen (item 11) — this is the one
   place he is likely to stop and go back, and going back will not resolve it, because the two
   passages really do say different things.
3. **§5.4**, where the hypothesis discussion leans on a display he was not given the means to read
   (item 6).

And one place where he does not stall but *should have been made to stop and did not*: §3.1. The
chapter's central equation goes past him without a marker. That is not a comprehension failure; it is
the failure the doctor's first sentence is about.

## Does it sound like the same hand as `src/ch3-6.html` and `src/ch4-2.html`?

**Yes.** Same furniture, same structure, same instincts: the `where`/`tools` opening, the numbered
`In plain terms` boxes, the ⚑ warn callouts that name a thing as chosen or quoted at the place it
arrives, the `Familiar ground` box built on the reader's own clinical ground, the `pause` markers, the
`brick you just laid` close. Same sentence habits: short declaratives after a long one, "That is the
whole argument", the discipline of naming where an assumption fails rather than only where it holds.
Nothing reads as a second voice.

Three tells, in descending order of how much they matter:

**1. One tic has roughly doubled in density.** The construction *"X is worth Y-ing"* — "worth naming",
"worth registering", "worth having", "worth pausing on", "worth isolating", "worth installing",
"worth carrying forward" — runs at **13.2 per 10 000 words in 4.6**, against **6.5 in 3.6** and **5.1
in 4.2**. Thirty-three instances. This is the mechanism of "theatrical" in the doctor's sentence:
each one is the writer telling the reader that something deserves attention instead of writing the
thing so that it does. It is his own tic, at about two and a half times his own rate.

**2. The arrival is unmarked, and that is a departure from his own practice, not from his voice.**
`ch3-6` §5: *"Put that value of κ back into the boxed result of §3, and there, at last, are the field
equations of general relativity."* That is the same writer giving a central equation its moment, in
the chapter this one is structurally closest to. `ch4-6` §3.1 gives its central equation *"What is
left is the equation this chapter is named after"* — and gives it at the end of a paragraph about
domains. The hand is the same; the practice was not applied here.

**3. The subtitle overclaims against the chapter's own conventions block** (item 1). Neither
comparison chapter does this. `ch4-2`'s subtitle is *"A table of renamings, seven postulates, and
nothing else"* — a count, and the chapter delivers exactly that count. `ch3-6`'s subtitle promises
three derivations and a constant, and §§3–5 deliver three derivations and a constant. `ch4-6`'s
subtitle promises one added assumption and the chapter marks three, one of which is physics. In a book
whose credibility rests on its accounting, that is the tell most worth fixing.
