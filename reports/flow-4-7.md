# Narrative-flow review — `src/ch4-7.html`, "Wells, Barriers, and Tunnelling"

Read start to finish, in order, as a first read. Fifteen places where I stalled, ordered by position
in the chapter. Modes are the brief's six.

---

## 1 · "Where we are", Conventions paragraph — **mode 5**

> "One result is quoted rather than derived, and it is experimental: the scanning tunnelling
> microscope and $\alpha$-decay measurements that §6.5 compares this chapter's exponential against."

Two things go wrong in one sentence. "One result" is followed by two measurements — STM *and* alpha
decay — and a reader who is being told in advance exactly how many unearned things the chapter
contains notices that the count and the list disagree. And the address is wrong: the marked box sits
in §6.4, not §6.5. The closing brick has it right ("The single flag in this chapter is experimental
and is raised in §6.4"), so the reader who checks finds the chapter disagreeing with itself about
where its own one flag is.

Related, same paragraph: the route runs "Section 1 … Section 6" and stops. Sections 7 and 8 exist and
are a fifth of the chapter. The route also does not mention §6.5 at all, which is where the chapter's
best result lives — the poles of $t$ being the bound states. A reader budgeting his evening from the
route paragraph budgets for the wrong chapter.

**What the reader needed:** the right subsection number, a consistent count of the flagged results,
and to be told that the barrier section ends by identifying scattering and binding as one function.

---

## 2 · §1.1 — **mode 5**

> "Two words in the paragraph above are doing hidden work and both need unpacking before anything can
> be solved. The first is *acceptable*. … The second is $\hat H$ itself."

The second word is given an address — "§1.3 below is where that answer comes from." The first is not.
Its answer is in §3.2, four hundred lines later, under a heading ("Where quantisation actually
happens") that does not use the word. The reader is told two debts are outstanding and given a due
date for one of them, so he carries the other open for three sections.

**What the reader needed:** where *acceptable* gets settled, in the same sentence that raises it.

---

## 3 · §1.3 — **mode 4**

> "There is a second way of saying the same thing which is worth having, because §4.6 needs it and
> because it makes the mechanism visible."

At this point the chapter has said "Chapter 4.6" ten times, and will say it twenty-five times in all.
It is the chapter the reader has just finished. A bare "§4.6" arriving in §1.3 reads, on first pass,
as that chapter — which is impossible, since a chapter already read cannot need something derived
here, and the reader loses a beat working that out. This is the only forward use of a bare
"§*n*.*m*" in the chapter that collides with the previous chapter's number; the four later uses of
"§4.6" all come after §4.6 exists and read cleanly.

**What the reader needed:** that this points forward inside the present chapter, and to what — the
delta well.

---

## 4 · §1.6 — **mode 5.** This is where the patience runs out.

> "The set of $u$ for which $v\mapsto\avg{u,(\hat H_{0}+V)v}$ extends continuously is the same as the
> set for which $v\mapsto\avg{u,\hat H_{0}v}$ does."

§1 opens by promising three things: the derivation, the one place it stops working, and the infinite
well selected out of the four-parameter family. All three are delivered by the end of §1.5. The warn
callout then closes the section rhetorically — "The rule that survives all three is the one that
produced [the matching condition] in the first place." §1.6 arrives *after* that closure, is not in
§1's opening promise, and is the most abstract prose in the chapter: two paragraphs of adjoint-domain
bookkeeping, the second of which is the sentence above, with no physical anchor and no worked
consequence anywhere later in the chapter. The reader has now read six subsections and a long callout
and has not yet seen a single energy level.

To answer the question directly: **§§1.1–1.5 earn the delay and §1.6 does not.** 1.2 supplies the two
shapes ($k$ and $\kappa$) that are the chapter's whole vocabulary. 1.3 is three paragraphs and is the
promised derivation. 1.4 is one paragraph. 1.5 is the payoff and is the best writing in the chapter
(see below). It is 1.6 that breaks the reader's patience, and it breaks it in the worst possible
place — one subsection short of the first solved problem.

**What the reader needed:** either §1's opening promise should have said §1.6 was coming and what it
buys, or the reader should have been told he may take it on trust and read on. As it stands nothing
tells him that skipping it costs him nothing, and nothing later in the chapter uses it except by
citation.

---

## 5 · §4.4, closing sentence — **mode 5 (low)**

> "Two dimensions sits between the two and always binds, for a reason that is not visible from this
> argument."

A claim with no reason and no address, in a chapter that is otherwise scrupulous about saying where
every loose end is picked up — §4.4's own preceding sentences send the reader to Chapter 4.13 for the
three-dimensional case. This one goes nowhere. It reads as a fact the writer wanted on the record
rather than a fact the reader can do anything with.

**What the reader needed:** either where the two-dimensional result is established, or the honest
statement that it is outside the book.

---

## 6 · §4.3 → §4.5, Figure 1 — **mode 5**

The only sentence in the body that sends the reader to this figure is at the end of §4.3:

> "There is a figure below on which that can be watched happening."

The figure then lands at the end of §4.5, with §4.4 (three dimensions, the threshold, the radial
argument) and the whole of §4.5 (three-depth table, then the grid-diagonalisation check) in between.
By the time the figure appears, the "that" it was going to show — new branches arriving as $z_0$
crosses multiples of $\pi/2$ — is two subsections cold, and the paragraph the reader has just
finished is about a $48\,000$-point tridiagonal matrix. Nothing at the figure's own position tells
him to touch it. The caption does the work the body should have done, and captions are what a reader
skips when he is tired, which at §4.5 of this chapter he is.

Second, smaller problem in the same figure: the preset button labelled **"one state"** carries
`class="on"` at load, but the slider's default is $z_0 = 2.561584$ — which is the first row of the
table two paragraphs above, and which has **two** bound states. So the first thing the reader sees is
a highlighted button whose label contradicts the readout directly underneath it, in a figure whose
caption says "The readouts are the test."

**What the reader needed:** an instruction at the figure, not two subsections before it; and a preset
label that matches what is on screen when the page loads.

---

## 7 · §5.2 — **mode 4**

> "The scattering solutions below are those two components, and the right way to hold them is as
> labels on pieces of a spectral measure rather than as vectors."

The densest sentence in §5, and it arrives while the reader is still waiting to find out what
transmission means. The phrase "pieces of a spectral measure" is carried entirely by Chapter 4.5;
nothing in this chapter unpacks it, and — this is the point — nothing in this chapter *uses* it.
Everything §5 and §6 actually do rests on the sentence before it (the preimage has two components,
one moving each way), which is genuinely needed and which §5.3 and Problem 2(d) both cash. The
spectral-measure clause is a debt being paid to the previous chapter in the middle of a paragraph the
reader is depending on for orientation.

**What the reader needed:** to be told that this clause is the formal statement and that nothing
below turns on it, so he can let it go past.

---

## 8 · §6.2, the transmission amplitude — **mode 3**

> "Note that $T=\abs t^{2}$ here with no correction factor … Taking the modulus squared of
> [$1/t = \ee^{\ii kw}[\cosh\kappa w + \tfrac{\ii}{2}(\kappa/k-k/\kappa)\sinh\kappa w]$] and
> simplifying, as the grind box does at the end, gives the result this chapter exists for."

The chapter's central algebraic result is displayed and the only thing said about it at the point of
arrival is an instruction to square it. Its structure is never read. It carries an explicit phase
factor $\ee^{\ii kw}$ and a complex bracket, i.e. the transmitted wave comes out phase-shifted, and
that phase is physical — Worked example 3(c) says so outright ("The transmitted phase does care, and
that is where the difference survives"), and §6.5 needs the bracket, not the modulus, to find the
poles. None of that is signalled here. Every other display in the chapter is read; this one is
consumed.

**What the reader needed:** one sentence on what the amplitude says over and above its modulus,
since two later passages depend on exactly that.

---

## 9 · §6.3, the labelled result — **mode 3 (low)**

The annotated display carries two different kinds of statement under one equation number: the result
$1/T = 1 + [\ldots]\sinh^2(\kappa w)$, and then, aligned on the same equals column, a *definition*,
$1/\kappa = \hbar/\sqrt{2m(V_0-E)}$. Aligned that way it reads as a second line of one equation
rather than as a reminder. And it is a reminder — $\kappa$ was defined in its own display two
subsections earlier.

**What the reader needed:** to be able to tell, from the layout alone, which line is the answer.

---

## 10 · §6.4, "Familiar ground" callout — **mode 6.** The analogy has one element with no counterpart.

The map is built carefully. $I = I_0\ee^{-\mu d}$ ↔ $T \simeq 16\epsilon(1-\epsilon)\ee^{-2\kappa w}$;
$\mu$ ↔ $2\kappa$; $d$ ↔ $w$; half-value layer $\ln2/\mu$ ↔ $\ln 2/2\kappa$. Three elements are then
explicitly withdrawn — no absorption, the coefficient depends on the particle, no resonance — and all
three withdrawals are correct and useful. The failure is in what the callout *grants*:

> "the logarithm of the fraction getting through is linear in the thickness, **half-value layers stack
> multiplicatively**, and a modest change in thickness is a large change in what emerges. If you are
> used to thinking in half-value layers you can think in them here, with $\ln 2/2\kappa$ playing the
> part."

Two paragraphs later:

> "Attenuation removes photons from the beam, one at a time and independently, **which is why the
> exponential is a product of independent survival probabilities across successive slabs.** Nothing of
> the kind happens in the barrier."

The reason half-value layers stack in radiology is independence across successive slabs. The callout
grants the stacking and then, as its first withdrawal, denies the mechanism that licenses it — without
saying what supplies the property instead. And the gap is not cosmetic. A radiologist's HVL intuition
is that slabs *compose*: two 1-HVL slabs equal one 2-HVL slab, whether or not they are pushed
together. That is exactly what does not hold here. Two barriers of width $w$ with a gap between them
do not transmit $T(w)^2$ — they resonate, which is the same interference the callout's own third
withdrawal describes for a single barrier. What actually carries across is far narrower: the width
appears linearly in one exponent, so *doubling one barrier* squares the transmission. That is a
statement about one wall, not about stacking.

This is the element to fix, and it is the one a clinical reader will lean on hardest, because HVL is
the piece of the analogy he already owns.

**What the reader needed:** what licenses thinking in half-value layers here, given that independence
does not — and the limit of the licence, which is that it is about widening one barrier and not about
putting two in a row.

---

## 11 · §6.4, same callout — **mode 4 (low)**

> "Section 6.6 shows that a barrier the particle has enough energy to cross becomes perfectly
> transparent at particular widths and energies."

It is §6.5. §6.6 is "What goes forward". Combined with finding 1 (the opening pointing at §6.5 for
what is in §6.4), the chapter's internal section pointers around §6 are off by one in both
directions, which is worse than either alone: a reader who finds one of them wrong stops trusting all
of them.

---

## 12 · §6.5 — **mode 4. This is the worst stall in the chapter.**

> "Continue [$1/t = \ee^{\ii kw}[\ldots]$] to negative energy, where $k=\ii\kappa$ and the particle
> would be bound, and ask where the transmission amplitude $t$ becomes infinite."

$\kappa$ has meant one thing continuously since its own boxed definition in §6.1: the decay constant
*inside* the barrier, $\sqrt{2m(V_0-E)}/\hbar$. The reader has used it in §6.3's three readings, in
§6.4's number ($\kappa w = 3.6226$ decay lengths), in the half-value-layer analogy ($\ln2/2\kappa$),
in the STM box, and in the width table. It is the most heavily loaded symbol in the chapter.

In the subordinate clause above it silently becomes something else — the decay constant *outside*, of
a bound state. And the display that follows,

> $\cot(qw) = (q^2 - \kappa^2)/2q\kappa$,

then contains that new $\kappa$ alongside $q$ = the wavenumber *inside*. That is §4's convention with
the letters swapped relative to everything §6 has done: §4 had $k$ inside and $\kappa$ outside; §6.1
through §6.4 had $k$ outside and $\kappa$ inside. The very next sentence asks the reader to compare
the display with §4's conditions — which is to ask him to hold both conventions at once, at the exact
moment the roles have been exchanged without notice.

Worse, $\kappa$ carries *two* meanings inside this one subsection: three paragraphs earlier it was
still the interior constant, analytically continued ("Put $\kappa=-\ii q$"). So the reader who scrolls
back to check finds the symbol used both ways on the same screen.

This is where I actually stopped and went back, and it is the one place in the chapter where going
back is not optional — the payoff (poles of $t$ are exactly the bound states, both parities) is the
chapter's best result and Problem 4(d) depends on it.

**What the reader needed:** to be told that the letters exchange roles because the region that decays
has moved from inside the wall to outside the well, and which convention the pole equation is written
in.

---

## 13 · §6.5, Figure 2 — **mode 5**

No sentence anywhere in the chapter refers to this figure. Not in §5, where half its content lives
(the $T+R-1$ readout, the behaviour above the top, the step-like reflection); not in §6.3, §6.4 or
§6.5, which supply every number it is preset to. It simply appears after the pole paragraph.

That is a waste of a good figure, and the waste is measurable: all three presets are anchored to
numbers in the text — "the worked barrier" is exactly §6.4's $1\ \mathrm{eV}$, $1\ \mathrm{nm}$,
$0.5\ \mathrm{eV}$; "a well" is exactly §6.5's $3\ \mathrm{eV}$, $0.6\ \mathrm{nm}$ well at its first
resonance — and none of those three passages says so. The caption is excellent and tells the reader
precisely what to do ("Drag the height negative to turn the barrier into a well, where the resonances
become dense and the fringes on the left almost vanish at each of them"), but it is doing work no
sentence in the body has asked for. Compare finding 6: figure 1 has one pointer in the wrong place;
figure 2 has none at all.

**What the reader needed:** at §6.4's number, that he can watch this number being computed live; and
at §5.5, that the conservation law he was just handed is checked in front of him further down.

---

## 14 · Worked example 1(a) — **mode 4**

> "Write $\kappa=\sqrt{-2mE}/\hbar$ and $q=m\lambda/\hbar^{2}$, so that $q$ is the $\kappa$ a single
> well would have."

$q$ was given to the reader in §6.5 as the wavenumber *inside* a barrier the particle can cross,
$\sqrt{2m(E-V_0)}/\hbar$; it is used in that sense through §6.5, in the resonance condition $qw=n\pi$,
in figure 2's readout, and again in Problem 4(d) — which comes *after* this worked example. Here it
is an inverse decay length instead. The definition is given locally and even glossed helpfully, so
this is not unreachable; it is expensive. The reader is asked to hold two meanings for one letter
across a hundred lines and then to switch back.

**What the reader needed:** either a different letter, or a note that $q$ is being reused because
this example does not need §6.5's.

---

## 15 · Worked example 2(a) — **mode 1. This is where the problems stop feeling different.**

> "On the right the energy is below the potential and the region is infinite, so §4.2's argument
> applies and only the decaying exponential survives. … Matching value and slope at the origin gives
> $A+B=C$ and $\ii k(A-B)=-\kappa C$."

This is the ninth value-and-slope match in the chapter and the second on this exact potential, and it
is done at full length from scratch. The reader cannot say why it is being solved again rather than
transported, because the chapter has twice just shown him that transporting works: §6.5 gets the whole
above-the-top barrier by continuing one formula ("Nothing in the derivation required $E$ to be below
$V_0$"), and Worked example 3(d) gets the delta well's bound state by continuing $t$. The same move is
available here in one line — the step result $r=(k-k')/(k+k')$ with $k'\to\ii\kappa$ *is*
$(k-\ii\kappa)/(k+\ii\kappa)$, which is what part (a) spends a paragraph deriving. Doing it the long
way, immediately after teaching the short way, is what makes the fatigue land.

**Where exactly the reader stops seeing the difference:** he *notices* the repetition earlier, at
§5.3 — "Solve them the way §4.2's were solved, by removing the overall scale" — but that is a
deliberate, cheap signpost and §5.4 pays for it within a paragraph. He *stops being able to justify*
the repetition at Worked example 2(a). Everything before it is well managed: §4 announces "the answer
stops being a formula", §5 announces "the question worth asking changes shape", §6.1 is literally
titled "the one change from §5" and names it in one sentence, and §6.2 moves the elimination into a
grind box precisely because it is grind. The chapter handles its five main matching problems with more
care than most books manage. It then spends that credit in §7, where three more full-length matching
problems arrive with the differentiator stated only in the italic problem line and never in the
answer. (For the record: §7 and §8 opening without a lead-in paragraph is the book's form —
`ch3-6.html` §8 and §9 and `ch4-2.html` §11 and §12 do the same — so that is not the issue. The issue
is that this chapter's §7 is three more of the same calculation and the others' are not.)

**What the reader needed:** at the top of part (a), why this one is worked rather than continued.

---

## A stretch that reads unusually well

**§1.5, "Which member of the family an impenetrable wall is."**

> "Now let $V_{0}$ grow with $E$ held fixed. The decay length $1/\kappa$ shrinks to zero, so the
> exterior wavefunction is crushed against the wall, and continuity of $u$ forces the interior value
> at the wall down with it. The slope does not go to zero at the same rate. In the exterior the slope
> is $-\kappa$ times the value, so as the value falls like $1/\kappa$ the slope stays finite. That is
> Dirichlet and it is nothing else: the value vanishes, the slope survives."

Five sentences, one moving part, and a conclusion the reader can see rather than accept. It settles a
question the previous chapter opened, it settles it with a limit he can picture, and the last clause
gives him something small enough to carry. This is the paragraph that justifies §1's whole length, and
it is the one place where the chapter's stated reason for existing — a boundary condition is a choice,
and here is which choice — becomes a physical picture instead of an argument. Worked example 2(d)
later reruns the same limit with the arithmetic supplied, and that pairing works.

Second mention: the warning callout after §5.5, on why $\abs t^2$ is not a probability. It states the
error, gives two numbers showing how large it is ($1.402$, $2.649$), and then explains why the error
is easy to miss — that it vanishes in every barrier problem, which is what people practise on. Naming
the conditions under which a mistake hides is rarer and more useful than naming the mistake.

---

## Summary judgements

**Could a reader who understood Chapter 4.6 follow this one straight through?**

**Yes** — but with one qualification and one near-miss.

The qualification is §1.6. It is followable, but it is where a reader reading after clinic puts the
chapter down, because it is the seventh block of preliminary and nothing tells him it is optional. He
loses nothing by skipping it; the chapter never uses it again except by citation. It does not make the
chapter impossible, it makes it easy to abandon, which for this reader is the same outcome by a
different route.

The near-miss is §6.5, finding 12. That is the one place where following the argument requires
scrolling back, because the chapter's most heavily used symbol changes referent inside a subordinate
clause and the display that follows silently adopts §4's convention with §6's letters. He can recover
— the comparison with §4's two conditions is spelled out and the arithmetic checks — but he recovers
by rereading, not by reading. Everything else in the chapter can be read forward once.

**Does it sound like the same hand as `src/ch3-6.html` and `src/ch4-2.html`?**

**Yes.** The furniture matches almost exactly — plain-terms boxes, warn callouts, one familiar-ground
callout, one closing brick, pause rules, a grind box, worked examples then problems with solutions
folded into `<details>`, verification passages that name a method sharing no algebra with the result.
The second-person address (31 uses of "you") tracks `ch4-2` (27) rather than `ch3-6` (2), so that is a
Part IV property, not a defect. The habit of naming what a section will hand you before it starts, of
saying which results are quoted rather than derived, and of closing by saying where each thing gets
spent, is all intact.

Two tells, both small:

1. **The roadmap form changed.** `ch4-2` opens all ten sections with "Announce the destination." plus
   an italicised, set-off, first-person-plural roadmap; `ch3-6` uses "Here is where this section is
   going." plus the same italic form in its two most argumentative sections. `ch4-7` inherits
   `ch3-6`'s trigger phrase but uses it once, without italics, and then switches to "By the end of
   this section you will have…" three times — a construction that appears nowhere in either
   comparison chapter. The habit survived; the shape of it did not.

2. **"Worth" has become a tic.** 34 distinct "worth …" constructions in 24,700 words — *worth having*
   (4), *worth watching* (3), *worth saying* (3), *worth knowing*, *worth carrying*, *worth naming*,
   *worth isolating*, *worth pausing over*, *worth real money*, *worth tabulating rather than
   asserting*. That is 1.54 per thousand words against 0.69 in `ch4-2` and 0.89 in `ch3-6`, both of
   which are the same writer using the same device sparingly. In a chapter that is mostly calculation
   the phrase is doing a real job — it is the flag that says *stop, this one matters* — but at 34 uses
   it stops flagging anything, and the four or five places where it marks something genuinely load-
   bearing (§1.3's "it is worth stating the conclusion in the form used in every problem below",
   §6.4's "worth tabulating rather than asserting") no longer stand out from the rest.

Neither tell suggests a second voice. Both suggest one voice under the strain of the longest chapter
in the part.
