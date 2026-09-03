# Flow review — `src/ch4-5.html`, "The Spectral Theorem in Infinite Dimensions"

Read start to finish as a first read, then back over the places I stopped. Ten findings, ordered by
position. Nothing here is a break in the argument: the chapter's section seams are the strongest I
have read in this run, and every one of these is a stall — somewhere the reader has to scroll back or
read twice — rather than a place the thread is lost.

---

## 1 · §1.3 — the chapter's own opening does not name where it is going

> "What follows repairs this in three moves, and they are worth having in front of you as a list
> before any of them is built…"

**Failure mode 5** (a section that does not say where it is going).

The three moves end at "the sum $\sum_k\lambda_kP_k$ becomes an integral $\int\lambda\,\dd P(\lambda)$."
That is the whole of the destination as §1 states it: repair the eigenvalue theorem. Stone's theorem —
which is what makes time evolution a consequence of self-adjointness rather than a postulate, and is
the reason Chapter 4.6 can start — appears nowhere in §1.

It is named once, in the Where-we-are box: "Section 9 proves the half of Stone's theorem that makes
'time evolution is unitary' and 'the Hamiltonian is self-adjoint' the same statement." That is a good
sentence and it is the only one of its kind before §8. After it the chapter goes silent about §9 for
the whole of §§1–5 — roughly 11,000 words, nearly half the chapter. The next four mentions name §9 by
number and say nothing about what it delivers: "the recipe for building functions of an operator that
§9 needs" (§6 intro), "One more construction comes free, and §9 needs it" (§6.6), "which is the
observation §9 is built on" (§6.6 end), "The third depends on §9, which has not been proved yet"
(§8 intro). The first restatement of *content* after the route box is §8.3.

**What the reader needed:** a fourth item on §1.3's list, or one sentence closing it, saying that the
same machinery will make unitary time evolution and self-adjointness the same statement. As it
stands, a reader who reads the route box on Monday and §§2–5 on Wednesday has nothing carrying him
toward the payoff.

---

## 2 · §1.3 and the pause after §5 — what a projection-valued measure is *for* is never said before §6

> §1.3: "It does survive, with the sum replaced by an integral against a family of projections
> indexed by the real line."
>
> Pause marker after §5: "the checking is finished; what follows is the machinery it licenses"

**Failure mode 5** (a seam that does not say what is now in hand or where it is going).

Coming out of §5 I could say what a PVM *replaces*. I could not say what it *buys*. The purpose
sentence exists and it is excellent — it is the second sentence of §6: "the Born rule is a statement
about projections, and until a projection exists for a continuous observable there is no probability
to compute." But it sits *after* the reader has already decided whether to keep going. The pause
marker is a designated stopping point, and what it offers as a reason to return is "machinery".

**What the reader needed:** that §6 sentence, or its substance, in §1.3's third bullet and again at
the pause. The three replacements of §1.3 are described in terms of what they give up; the third one
is the only one whose gain (a probability for a continuous observable) is never stated at the point
where it is promised.

---

## 3 · §7.2 against §3.2 — momentum in a box "does have eigenvectors"

> §3.2: "Momentum on $[0,L]$ with the wavefunction pinned at both ends is symmetric and has no
> eigenvalues at all."
>
> §7.2, about 850 lines later: "On this interval momentum does have eigenvectors, and they are the
> Fourier modes"

**Failure mode 4** (a symbol — here, a whole worked counterexample — returns cold).

§3.2's counterexample is the most memorable thing in the quoted-theorem box; it is what the box uses
to prove that *self-adjoint* cannot be weakened to *symmetric*. When §7.2 asserts the opposite of it,
the reader stops to check whether he is being contradicted. He is not — §7.2 says "periodic
condition" and "which that section proved self-adjoint", and Chapter 4.4 §5.4 does genuinely
establish the periodic/pinned distinction — but the reader has to reconstruct that himself from two
different adjectives 850 lines apart.

**What the reader needed:** one clause naming §3.2's counterexample and saying that the difference is
periodic versus pinned. The chapter raised the collision; it should be the chapter that closes it.

---

## 4 · §4 intro — the plan promises three verifications; the section runs five subsections

> "Two of the three land here, and the third is set up here and finished there."

**Failure mode 5** (mild). §4 delivers Verification 1 (§4.1), a non-uniqueness demonstration (§4.2),
Verification 2 (§4.3), a numerical check (§4.4), and Verification 3's setup (§4.5). §4.2 is announced
back in §3.2 ("§4 will exhibit the same operator in two different ones"). §4.4 is announced nowhere.
A reader counting to three loses his place twice.

**What the reader needed:** the plan paragraph to name the two interpolations, so that arriving at
"§4.4 · The second verification, checked against arithmetic" does not read as a fourth verification.

---

## 5 · §4.3, and three more places — "nine chapters ago" points at three different chapters

> §4.3: "one line of algebra applied to a theorem the reader proved nine chapters ago" — Chapter 0.9
> (Plancherel).
>
> Plain terms 4.5.4: "the transform between position and wavelength that was built nine chapters ago"
> — Chapter 0.9.
>
> Plain terms 4.5.6: "the promise made nine chapters ago in the toolkit" — Chapter 0.5.
>
> Plain terms 4.5.9: "Nine chapters ago it was shown that every such rotation is an exponential of
> something, and that the something is a legitimate observable with the dimensions of energy" —
> Chapter 4.2 §7.3, which is three chapters back and which §9's own opening paragraph names.

**Failure mode 4.** The phrase is house idiom: in `ch4-2.html` and in `_throughline.html` it means
Chapter 0.5, consistently. Here it means Chapter 0.9 twice, Chapter 0.5 once, and Chapter 4.2 once.

This matters more than it looks because of *where* it is used. Three of the four are in the
"In plain terms" boxes, which are the one register that gives no chapter numbers at all — "the
toolkit", "nine chapters ago", "the previous chapter". The phrase is the reader's only handle in that
register, and pointing it at three different places inside one chapter takes the handle away.

**What the reader needed:** the idiom to keep one referent, or in the plain-terms boxes to be
replaced by something that survives the reader not counting.

---

## 6 · §5.1 → §6.1 — $\xi$ is silently reassigned

**Failure mode 4.** This is the sharpest working-memory hazard in the chapter.

$\xi$ is the generic point of the abstract measure space $X$ from §3.2 onward: "$(\hat U\hat A\hat
U^{-1}\Psi)(\xi)=g(\xi)\Psi(\xi)$", "$\{\xi:\abs{g(\xi)-\lambda}\lt\epsilon\}$". Then §5.1 takes it
over for something else entirely —

> "Writing $\xi=x/x_0$ turns [the oscillator Hamiltonian] into…"

— and holds that meaning through the whole of §5: roughly 300 lines, the longest unbroken run of the
symbol anywhere in the chapter, ending 44 lines before §6 at "its classical turning point sits at
$\xi=\sqrt{79}=8.89$."

Then §6.1's defining display reads

> "$g^{-1}(E)=\{\xi\in X:\ g(\xi)\in E\}$"

with no signal that the symbol has gone back. It reverses again in §6.3, §9.1 and §9.2, and reverses
a third time inside Problem 2's solution.

**What the reader needed:** a note at §5.1 that $\xi$ is being borrowed for the oscillator's
dimensionless coordinate, and a note at §6.1 that it is the abstract label again. The chapter is
careful about far smaller things than this — it names the dominating function on every one of its
five uses of dominated convergence — which makes the omission conspicuous.

---

## 7 · §6.3 — the chapter's promised equation arrives and the next sentence is bookkeeping

> $$\hat A \;=\; \int_{\sigma(\hat A)} \lambda \, \dd P(\lambda)$$
>
> followed immediately by: "The domain is not an extra stipulation."

**Failure mode 3** (a result is stated and the text moves on without saying what changed).

This display is promised three times before it arrives: in the Where-we-are box, in §1.3's third
bullet, and in §6's opening ("By the end you will have $\hat A=\int\lambda\,\dd P(\lambda)$…"). It is
the third form of Chapter 0.5's theorem, the one Chapter 0.5 said would survive. It arrives, and the
next words are a domain check.

It is not strictly unread — the two inline annotations gloss it, and §6.4's heading ("Chapter 0.5's
sum, recovered") supplies the beat one subsection later. But at the display itself nothing marks the
arrival, and I read past it and had to come back to confirm that that had been the payoff.

**What the reader needed:** one sentence at the display saying what has just changed — that Chapter
0.5's third form now exists for an operator with no eigenvectors — before the domain paragraph.

---

## 8 · §7 — $\ket p$ is promised, $\ket k$ is delivered, and the two meet at the end of §7.6

> §7 opening: "Every physics text writes $\ket x$ and $\ket p$… and writes
> $\avg{x|p}=\ee^{\ii px/\hbar}/\sqrt{2\pi\hbar}$."
>
> §7.6, four subsections later: "One piece of bookkeeping remains… Everything above was in the
> wavenumber $k$, and Part IV writes momentum $p=\hbar k$ with the constants visible."

**Failure mode 4.** §7.1 discusses $\ket p$. §7.2's heading is "Momentum, in a box", and its first
display switches to $k_n=2\pi n/L$ without comment. §7.4's summary sentence then reads "Every
equation containing $\ket x$ or $\ket k$" — the promised symbol quietly substituted in the section's
own headline claim. The reconciliation, when it comes, is clean and complete; it is just four
subsections late.

**What the reader needed:** a sentence at the top of §7.2 saying that the section works in wavenumber
throughout and restores the $\hbar$ at the end. Without it the reader spends §§7.2–7.5 unsure whether
the object he was promised has been dropped.

---

## 9 · §7.3 — "since a box does nothing for it"

> "Position needs the same treatment with a different replacement, since a box does nothing for it."

**Failure mode 1** (a dropped thread: the paragraph asserts a reason it does not give).

The reader has just spent the longest subsection in §7 being persuaded that a box is exactly what
rescues momentum. The single question he brings to §7.3 is why the same move fails for position, and
he gets six words of assertion at the head of the subsection and then a lattice.

**What the reader needed:** the reason. Confining the line to an interval leaves position still
multiplication by $x$ with continuous spectrum — bounding the space does nothing, so what has to be
discretised is the space itself rather than its extent. One clause. Its absence is the more noticeable
because §7.2 justified its own replacement in three sentences.

---

## 10 · §9.1 — three symbols go cold or change meaning in one paragraph

> "Let $\hat H$ be self-adjoint, and define $\hat U(t)=\ee^{-\ii\hat Ht/\hbar}$ by [e-fcalc], which is
> legitimate because $\lambda\mapsto\ee^{-\ii\lambda t/\hbar}$ is measurable and bounded. Work in the
> multiplication picture, where the operator is multiplication by $\ee^{-\ii g(\xi)t/\hbar}$…"

**Failure mode 4.** This is the worst stall in the chapter, and it is at the payoff.

Three things happen in that one sentence and the display after it:

- **$\hat U$ is overloaded.** From §3.2 through §6.6 $\hat U$ is the spectral-theorem unitary, and
  e-fcalc — the equation this very sentence points the reader at — reads
  $f(\hat A)=\hat U^{-1}M_{f\circ g}\hat U$ with that meaning. The same sentence gives $\hat U(t)$ a
  different meaning. The collision is never named.
- **"the multiplication picture" is the first $\hat U$**, used without being said.
- **$\Psi$ returns after roughly 5,000 words.** It was defined exactly once, as a trailing qualifier
  inside §6.2's display — "$\Psi=\hat U\psi$" — last used in §6.3, and it comes back in the
  strong-continuity display with no reminder, after §§6.4–6.6, the whole of §7 and the whole of §8.

The compounding is what does the damage. A reader who has been away from the multiplication picture
for two long sections needs to recover $\Psi$, and to recover it he needs $\hat U$, and $\hat U$ has
just been given to something else in the sentence that sent him looking. This is where I scrolled
furthest.

**What the reader needed:** at the head of §9.1, the reminder that $\Psi$ is $\psi$ seen through the
spectral unitary, and a distinguishing name for the evolution family. The mathematics of §9.1–9.2 is
four lines and is beautifully clean; the notation is what makes it expensive.

---

## Failure mode 6 — checked, and it holds

The clinical analogy is the familiar-ground box in §6.5 (survival time / continuous spectrum). I
checked it element by element, because the brief says this is where Chapter 4.1 went wrong.

| Analogy element | Counterpart | Holds? |
|---|---|---|
| $\Pr(T = 14.000\ldots\text{ months}) = 0$, for every value | $P(\{x_0\}) = 0$, for every point | yes |
| the distribution is not thereby empty | the theory is not thereby silent | yes |
| everything reported is an integral of a density over a region | $\int_a^b\abs\psi^2\dd x$ | yes |
| survival density | $\abs\psi^2$ as density w.r.t. Lebesgue measure | yes, for position |
| a distribution with an atom | point spectrum | yes; Worked example 2 builds the mixed case |
| — | $\mu_\psi$ is observable-dependent, no joint distribution | named as a place the parallel stops |
| — | projections do not commute; "no survival analysis in which the events fail to commute" | named as a place the parallel stops |

Both disanalogies are stated, in the box, before the reader can be misled by them. This is the
opposite of the Chapter 4.1 failure and it is worth saying so.

One scope point, not a break: "The measure $\mu_\psi$… $\abs\psi^2$ is its density with respect to
Lebesgue measure" is true for the observable whose $g$ is the identity, and the reader is two
paragraphs from the oscillator, whose $\mu_\psi$ is pure atoms and has no density. The box's own next
sentence corrects it ("a point spectrum is a distribution that is all atoms"), so the reader does
recover, but the sentence is written more generally than it is true.

---

## Reads unusually well — §3.1, "What a list of numbers has to become"

Three short paragraphs, no notation beyond $D$ and $\{1,\dots,n\}$, and they take the finite theorem
apart into three pieces, say which one cannot survive and why, and rebuild the list as a function
before the theorem is quoted:

> "Written that way, the operation $D$ performs is not 'attach a number to each direction' but
> **multiply by a function**, and multiplication by a function makes sense on any set at all, finite
> or not."

By the time §3.2's quoted box arrives, the theorem reads as forced rather than borrowed — which is
exactly what a quoted result needs, and it is achieved with no machinery at all. This is the
"classical simplicity" the reader says he is missing elsewhere, and the chapter can already do it.

Two more that work the same way, more briefly: §7.4's three-step procedure ("Replace the continuum…
Do the computation there… Rescale so that each term carries the spacing"), which is the whole of §7
compressed into something checkable; and §5.6's three-line collection of the verifications, whose
payoff sentence — "The operators differ in their measure and in nothing else that matters" — earns
the figure that follows it.

---

# Summary judgements

## Could a reader who understood Chapter 4.4 follow this one straight through?

**Yes.** None of the ten findings breaks the argument.

The structural work in this chapter is unusually good and it is what carries the reader across the
stalls. Every section opens with a route paragraph that says what it will do and what to hold on to,
and every section closes with a plain-terms box that says what is in hand. The three pause markers
sit at real breaks. The quoted results are marked where they arrive, with their hypotheses, with what
the mark covers and what it does not — and §5.6 does the rarest thing in the book, which is to say
out loud how far the verification reaches and where it stops.

The closest call is §9.1, where the notation stacks up at the exact moment the chapter's payoff
lands. A reader can recover there by scrolling to §6.2, and he will, but he pays for it — and he pays
for it while reading the section that is the chapter's reason for existing.

The parent's two watch items, answered directly:

- **Can the reader say what a PVM is for at the end of §5?** No. He can say what it replaces. The
  purpose sentence exists and is good, and it is the second sentence of §6 — one paragraph past the
  point where the chapter invites him to stop. Finding 2.
- **Has the chapter said it is heading somewhere before §9?** Once, on page one, in the route box.
  Then nothing for §§1–5, and four mentions by section number in §§6 and 8 that do not restate what
  §9 delivers. §1 — the chapter's own statement of what it is doing — does not mention it at all.
  Finding 1.

## Does it sound like the same hand as `src/ch3-6.html` and `src/ch4-2.html`?

**Yes.** Same architecture (Where we are → route → Conventions; Tools you'll need; ⚑ quoted-not-derived
boxes whose "the hypotheses are the content" paragraph does the real work; numbered In plain terms
boxes; Familiar ground; grind boxes; Worked examples; Your turn; the closing brick). Same vocabulary
of debt — bill, instalment, mark, spent, bought, brick, cornered. Same habit of naming what a result
costs at the moment it is used. Nothing in the chapter reads as a second voice.

Three tells, all mild, and only the third is unambiguously this chapter's:

1. **The "worth" construction, at roughly twice the rate.** Occurrences per 10,000 words: `ch3-6`
   8.2, `ch4-2` 7.0, `ch4-4` 11.0, **`ch4-5` 15.8** (`ch4-3` 14.1). In this chapter it almost always
   announces significance instead of demonstrating it — "worth slowing down over", "worth pausing
   on", "worth registering", "worth having explicitly", "worth saying why", "worth a clause", "worth
   the section". `ch3-6` in the same situation writes "Set $\lambda=0$ until §6" and "Everything
   needed for it is already in hand." This is the closest thing in the chapter to the reader's word
   *theatrical*, and it is a drift that begins in `ch4-3` rather than here.
2. **The section-opening formula is gone.** `ch4-2` opens 10 of its 12 sections with "Announce the
   destination." plus an italic mini-abstract; `ch3-6` uses "Here is where this section is going."
   `ch4-5` uses neither — but nor do `ch4-3` or `ch4-4`, so this is Part IV drift, not a foreign hand.
   It is still the visible difference from `ch4-2`.
3. **"nine chapters ago" detached from its referent.** In `ch4-2` and in `_throughline.html` the
   idiom means Chapter 0.5 and means it consistently. Here it means Chapter 0.9 twice, Chapter 0.5
   once, and Chapter 4.2 once. An inherited idiom used without checking where it points is the one
   tell that belongs to this chapter and not to its neighbours. It is finding 5.

---

## One note that is not a finding

§8.5's second bullet repeats §5.6 word for word — "need not be self-adjoint, need not be essentially
self-adjoint, and need not even be densely defined" — and the brick makes it a third time. §8.5 does
cite §5.6 in the next clause, so it is a deliberate callback rather than an oversight, and a checklist
is the right place to restate a prohibition. Recording it only because verbatim self-repetition at
700 lines' distance is part of what "dense" feels like from inside.
