# Part IV — re-plan: cap the objects, split the chapters

*A revision of `MATHPLAN-4.md` §§4.4–4.11. Chapters 4.1, 4.2 and 4.3 are written and are not
touched. Nothing here is applied: `MATHPLAN-4.md`, `build.py` and every chapter file are unchanged
on disk.*

**Read before this document:** `MATHPLAN-4.md` §0 (pacing, the postulate ledger, the debt map, the
numerical confirmations), its Register and Conventions sections, and its "What this part must not
do". All of those are **unchanged and still binding**. This document replaces only the eight
chapter sections 4.4–4.11, the ⚑ budget table, and the batch order.

---

## 0 · What counts as an object, and the measurement

The standard is `src/_ledger.html`'s own: **an object is a row of the Math Ledger** — a named thing
with a symbol or a statement, introduced for a stated reason, and spent somewhere later. It is not
a build item; the written chapters run about 0.7 ledger rows per build item, because several items
routinely assemble one object (4.1's five items on detailed balance and the three Einstein
processes produce two rows; 4.3's items 16 and 17 produce two).

Counting the written Part IV that way:

| Ch | Ledger rows | Words | Words per object |
|---|---|---|---|
| 4.1 | 12 | 18,450 | 1,538 |
| 4.2 | 13 | 23,714 | 1,824 |
| 4.3 | 13 | 23,718 | 1,824 |
| **Part IV so far** | **38** | **65,882** | **1,734** |

Against the book's own history — Part 0 at ~2,100 words per object, Parts I–III at ~2,800 — Part IV
is running at **62% of the book's established word budget per new idea, in chapters 40% longer than
the book's mean (16,817 words).** Both numbers move the wrong way at once. That is the "running
around", and it is arithmetic, not mood.

Counting the *planned* chapters 4.4–4.11 the same way gives **88 objects across 8 chapters** —
11.0 per chapter, which is worse than what is already on the page. At six per chapter that is
between 14 and 15 chapters; the fault lines fall where they fall and the answer below is **17**.
Where the extra three came from is stated in §2.

---

## 1 · The split, and the numbering

The rule the author set: **when a chapter splits, the first piece keeps its number and everything
downstream shifts.** Applied:

| Old chapter | Objects | New chapters | Objects each |
|---|---|---|---|
| 4.4 Operators in Infinite Dimensions | 12 | **4.4** Domains, and the Adjoint's Domain · **4.5** The Spectral Theorem in Infinite Dimensions | 6 · 6 |
| 4.5 The Schrödinger Equation | 8 | **4.6** The Schrödinger Equation *(not split)* | 7 |
| 4.6 Systems You Can Solve in One Dimension | 11 | **4.7** Wells, Barriers, and Tunnelling · **4.8** The Oscillator, and the Ladder | 6 · 6 |
| 4.7 Symmetry, Commutators, and the Classical Limit | 9 | **4.9** Commutators, Uncertainty, and Symmetry · **4.10** The Classical Limit | 5 · 5 |
| 4.8 Angular Momentum and Spin | 12 | **4.11** The Angular Momentum Algebra · **4.12** Spin, Orbitals, and Addition | 6 · 6 |
| 4.9 The Hydrogen Atom | 10 | **4.13** The Hydrogen Atom · **4.14** The Degeneracy, and $SO(4)$ | 6 · 4 |
| 4.10 Perturbation Theory and Transitions | 12 | **4.15** Perturbation Theory · **4.16** The Fine Structure of Hydrogen · **4.17** Transitions | 4 · 4 · 6 |
| 4.11 Identical Particles, Entanglement, and Measurement | 14 | **4.18** Identical Particles · **4.19** Density Matrices and Entanglement · **4.20** Bell, Decoherence, and What Is Settled | 5 · 5 · 4 |

**Part IV becomes 20 chapters: 4.1–4.3 as written, 4.4–4.20 as below.** Mean 5.4 objects per new
chapter; **no chapter above seven, and the only seven is 4.6**, whose seventh object — stationary
states — is three lines from 4.5's spectral theorem.

**The arithmetic of the second column against the fourth: 88 objects become 91.** One moves (the
Heisenberg picture, out of old 4.5 and into 4.9, beside the equation it generates) and **three are
added**: parity in 4.7, and the rotating-wave approximation and the selection rules in 4.17. The
last two are objects the written text already promised and the current plan has no build item for —
see Findings 4 and 5. Nothing is dropped anywhere.

**The remap table**, which is the whole of the mechanical work:

```
old 4.4 → 4.4 (+4.5)      old 4.8  → 4.11 (+4.12)
old 4.5 → 4.6             old 4.9  → 4.13 (+4.14)
old 4.6 → 4.7 (+4.8)      old 4.10 → 4.15 (+4.16, +4.17)
old 4.7 → 4.9 (+4.10)     old 4.11 → 4.18 (+4.19, +4.20)
```

### 1.1 · Section numbers were designed to survive

Ten written sentences name a **section** of an unwritten chapter, not just the chapter. The section
lists below were built backwards from those ten so that nine of them keep their section number and
change only the chapter number:

| Written promise names | Becomes | Section preserved? |
|---|---|---|
| 4.4 §4 (symmetric → self-adjoint), ×2 | 4.4 §4 | yes — *and the chapter number too* |
| 4.4 §5 (momentum on the half-line), ×2 | 4.4 §5 | yes — *and the chapter number too* |
| 4.4 §9 (Stone) | **4.5 §9** | yes |
| 4.5 §2 (the sign convention) | **4.6 §2** | yes |
| 4.7 §3 (how one knows a set is complete) | **4.9 §3** | yes |
| 4.7 §8 (the correspondence cannot be exact), ×2 | **4.10 §8** | yes |
| 4.11 §3 (P8) | **4.18 §3** | yes |
| 4.11 §5 (occupation numbers, Planck twice), ×2 | **4.18 §5** | yes |
| 4.11 §9 (what is settled), ×4 | **4.20 §9** | yes |
| 4.10 §8 (the interaction picture) | **4.17 §3** | **no** — the only one |

That was not free: 4.5's Stone section was moved *after* the $\ket x$/$\ket p$ section to land on §9,
and 4.20 was given nine numbered sections rather than seven. Both changes are improvements on their
own merits — Stone reads better as the hand-off to 4.6 than as a detour before it — but they were
chosen for this reason and a later editor should know that before renumbering anything.

---

## 2 · What the split costs, and what it does not

**Where the three extra chapters over the expected fourteen came from.** Old 4.10 and old 4.11 each
need three pieces, not two, and old 4.9 needs two. In each case a two-way cut leaves one side at
eight or nine objects:

- **old 4.10** cuts only at {expansion, degenerate, variational, asymptotic} = 4 · {the three
  fine-structure terms and their sum} = 4 · {interaction picture, Dyson series, rotating-wave,
  golden rule, selection rules, adiabatic} = 6, the last including the two items the old plan owed
  and did not have. Any merge is 8 or more, and the three fine-structure terms cannot be separated
  from the formula they add up to without splitting the derivation.
- **old 4.11** cuts only at {exchange, P8, Slater, exchange energy, occupation numbers} = 5 ·
  {density matrix, purity, reduced state, entanglement, no-signalling} = 5 · {singlet correlation,
  CHSH, Tsirelson, decoherence} = 4. Merging the last two gives 9.
- **old 4.9** is 10 objects; the $SO(4)$ material is a second, independent derivation of a spectrum
  already derived, which is exactly the seam the book uses at 4.3 → 4.4.

**The renumbering cost is paid in full at the first split.** Once *any* chapter before 4.11 splits,
every chapter after it shifts, and every written promise naming a shifted chapter needs its number
changed. So there is no saving in splitting less: the marginal cost of the ninth split is one
judgement pass over that chapter's own promises, not a new class of work. **Split as far as the
object count demands and no further** — which is what §1 does.

**Word count goes up, not down.** Seventeen chapters carry seventeen opening `where` callouts,
seventeen closing bricks, seventeen sets of worked examples and seventeen "Your turn" sections
against eight of each. At the observed overhead (about 2,200 words per chapter in Parts 0–III for
the frame alone, excluding worked examples) that is **roughly 20,000 extra words across the part**,
about 9%. It buys chapters of 9,000–12,000 words — one sitting each, at the book's own
2,000-words-per-object rate rather than 1,700.

**Interactives do not multiply.** `CONVENTIONS.md` requires a `where`, a `brick`, a `familiar` and
a `warn` per chapter; it does not require an interactive. `MATHPLAN-4.md`'s one-per-chapter rule was
its own. **Keep the eight interactives already specified, each in the chapter that owns it**, and
add three cheap ones (4.7, 4.15, 4.19) where a chapter would otherwise carry none of its own.
Nine of the seventeen chapters carry a figure and a numerical confirmation but no interactive, and
that is correct.

**The numerical confirmation does multiply** — pacing item 11 is per chapter and is worth keeping.
All seventeen are assigned below; nine are new and every one of them is computable from a
verification `MATHPLAN-4.md` already performed.

### 2.1 · The written chapters are not being split, and here is the alternative for them

4.1, 4.2 and 4.3 carry 12–13 objects each and are on the page. Splitting them would renumber the
whole part a second time and invalidate 30 more promises for no gain in content. **The right repair
for a written chapter is not a split but a marked sitting break**: a horizontal rule with one line
of text — *"a natural place to stop; §§5–8 are a second sitting"* — placed at 4.1 §5, 4.2 §7 and
4.3 §5, and reflected on the landing page as "three chapters, seven sittings". That is a
sixty-word edit per chapter, costs no numbering, and gives the reader the thing he actually asked
for, which is permission to stop. The new chapters do not need it because they are one sitting each
by construction.

---

# Deliverable 1 · The revised Part IV

---

# 4.4 · Domains, and the Adjoint's Domain ※

**What this chapter exists to do:** show that in infinite dimensions an operator is not a formula
but a formula *together with a domain*, and that the domain is forced rather than chosen — then
prove that "Hermitian" was not enough, on two operators the reader can check by hand.

**Objects introduced — six:**

1. **Bounded and unbounded operators**, $\norm{\hat A}=\sup\norm{\hat A\psi}/\norm\psi$, with
   $\dv{}{x}$ as the offender
2. **Hellinger–Toeplitz** ⚑ — a symmetric operator defined on all of a Hilbert space is bounded
3. **The domain of an operator**, and what *dense* is doing
4. **The adjoint, and its own domain** $\operatorname{dom}(\hat A^{\dagger})$
5. **Symmetric versus self-adjoint**, with the boundary term as the place the domain lives
6. **Deficiency indices** ⚑, and the family of self-adjoint extensions they count

**Sections (fixed — forward references point at these numbers, and §4 and §5 are load-bearing):**

| § | Title |
|---|---|
| 1 | The four places Chapter 0.5 used finite dimension |
| 2 | Bounded, unbounded, and why the derivative cannot be tamed |
| 3 | Domains, and the adjoint's domain |
| 4 | Symmetric is not self-adjoint |
| 5 | Two cases in full: the interval, and the half-line |
| 6 | Counting the extensions: deficiency indices |
| 7 | The particle in a box has four parameters, not one |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The four failures named, one by one | **0.5**'s closing paragraph, quoted in full | 0.5 listed them: *"in the induction, in rank–nullity, in the interchange of sums, in the claim that an injective map is surjective."* Take them in that order and say what happens to each — **and say in the same paragraph that the repair takes two chapters, this one for the domains and 4.5 for the spectrum.** This is the collection point for 0.5's *"Chapter 4.4 is where the bill comes due"*, and the sentence must be honoured across both chapters or the promise reads as half kept |
| 2 | **$\dv{}{x}$ is unbounded** | exhibit $\ee^{\ii kx}$ on a bounded interval: norm fixed, derivative norm $\to\infty$ | **Collects 0.6 §2's promise verbatim**: *"In infinite dimensions linear maps can be unbounded, $\dv{}{x}$ being the standard offender"* |
| 3 | **Unboundedness is not avoidable**: Hellinger–Toeplitz | ⚑ the closed graph theorem; derive Hellinger–Toeplitz from it in two lines | A symmetric operator defined on *all* of a Hilbert space is bounded. So an unbounded observable **must** have a restricted domain: the domain is forced, not chosen for convenience. This reframes the whole chapter and is worth its two lines |
| 4 | Domains; $\hat p$ on $L^{2}(\R)$ | item 3; **0.9** §2 | The domain of $\hat p$ is the functions whose derivative is in $L^{2}$, and it is dense. Say what "dense" is doing: it is what makes $\hat A^{\dagger}$ well defined at all, and 4.3 §7.4 already paid for it |
| 5 | **The adjoint, with its own domain** | **0.5** §4's definition, now read carefully | The definition of $\hat A^{\dagger}$ *determines* $\operatorname{dom}(\hat A^{\dagger})$, and there is no reason for it to equal $\operatorname{dom}(\hat A)$. This is the sentence the chapter turns on |
| 6 | **Symmetric ($\avg{\hat Au,v}=\avg{u,\hat Av}$ on $\operatorname{dom}\hat A$) vs self-adjoint ($\hat A=\hat A^{\dagger}$, *domains included*)** | items 4–5 | **P2 is corrected here, in §4, which is the section two written sentences of 4.2 name.** Go back and say so: 4.2 §4 said "Hermitian" and it was not enough |
| 7 | **The boundary term is where the domain lives** | **0.2** §3.2's integration by parts, redone with the boundary term kept | **Collects 0.2's promise by name**: *"Chapter 4.4, where it makes $-\ii\hbar\partial_x$ Hermitian and thereby makes momentum an observable."* 0.2 waved the boundary term through; here it is the whole content |
| 8 | **$\hat p=-\ii\hbar\dv{}{x}$ on three domains, worked before any theory of extensions** | require the boundary term of item 7 to vanish, and ask on which functions it does | §5, and it must come *before* item 9. **On $\R$: nothing to impose. On $[0,L]$: $\psi(L)=\ee^{\ii\theta}\psi(0)$, a one-parameter family, and the reader can see the whole family by hand. On $[0,\infty)$: the boundary term at $0$ cannot be killed without killing the operator.** The shocking conclusion arrives from integration by parts alone, with no imported classification — which is why this section is the one 4.2 points at twice |
| 9 | Deficiency indices, stated | ⚑ von Neumann's classification, with hypotheses | §6. The flag arrives *after* the reader has already seen the answer in the three cases, so it is discharged into arithmetic they have done. Solve $\hat p^{\dagger}f=\pm\ii f$, i.e. $f=\ee^{\mp x/\hbar}$, and ask which solutions are square-integrable: $(0,0)$ on $\R$, $(1,1)$ on $[0,L]$, $(1,0)$ on $[0,\infty)$ — matching item 8 exactly, three times |
| 10 | **The particle in a box: $-\dd^{2}/\dd x^{2}$ on $[0,L]$ has deficiency indices $(2,2)$, hence a $U(2)$ — *four-real-parameter* — family of self-adjoint extensions** | item 9 applied to the second derivative | §7. **Correction to `PLAN-FORWARD.md` §3.1 and §5.3, which say "a one-parameter family". It is four.** Dirichlet, Neumann, periodic, antiperiodic and the two-parameter Robin family all sit inside $U(2)$. Work the Robin family $\psi'(0)=\alpha\psi(0)$, $\psi'(L)=-\alpha\psi(L)$ explicitly, get its transcendental spectrum, and show that **different extensions have different spectra** — so the boundary condition is physics and not bookkeeping. Verified numerically. `MATHPLAN-4.md` §"Where I am uncertain" item 5 is executed here: **momentum first (§5, a clean $U(1)$), the box second (§7, the richer $U(2)$)** |
| 11 | What the chapter has and has not done, and what 4.5 owes | the whole chapter | Half a page. The reader now knows which operators are observables. They still do not know what the *values* are when there are no eigenvectors — and 4.5 is that. **Announce the two-chapter shape here as 4.2's closing brick announced 4.3+4.4**, in the same words, because the shape has repeated |

**Interactive (one — carried from old 4.4):** the spectrum of $-\dd^{2}/\dd x^{2}$ on $[0,L]$ as the
Robin parameter $\alpha$ is dialled — levels sliding continuously, one dropping below zero as
$\alpha$ goes negative. **Test:** at $\alpha=0$ the levels read $n^{2}\pi^{2}\hbar^{2}/2mL^{2}$ to
four significant figures against the closed form; the level count below any fixed energy changes as
$\alpha$ crosses the value the transcendental equation predicts.

**Numerical confirmation:** the Robin spectra for three values of $\alpha$, computed and confirmed
distinct, against the transcendental condition solved by Newton's method on the page. *(This is
`MATHPLAN-4.md`'s "4.4's cases" verification, reassigned; the Hermite/Parseval confirmation that
was old 4.4's goes to 4.5, where the Hermite functions are.)*

**⚑ permitted in 4.4:** the closed graph theorem (item 3); von Neumann's deficiency-index
classification, with hypotheses (item 9). **Nothing else.** **Two.**

---

# 4.5 · The Spectral Theorem in Infinite Dimensions ※

**What this chapter exists to do:** replace 0.5's $A=UDU^{\dagger}$ with the statement that survives,
verify it in every case the book will ever use it, and give $\ket x$ and $\ket p$ a meaning — paying
the four remaining promises of `GAPS.md` G1.

**Objects introduced — six:**

1. **The spectrum**, decomposed into point, continuous and residual — and an operator with **no
   eigenvectors in the space**
2. **The spectral theorem, multiplication-operator form** ⚑
3. **The Hermite functions, proved complete** — built, not quoted
4. **The projection-valued measure**, and $\hat A=\int\lambda\,\dd P(\lambda)$
5. **Box normalisation, $\ket x$ and $\ket p$**, with the rigged Hilbert space ⚑ behind them
6. **Stone's theorem** (forward direction built, converse ⚑)

**Sections (fixed — §9 is load-bearing):**

| § | Title |
|---|---|
| 1 | The spectrum, when there are no eigenvectors |
| 2 | The spectral theorem, in multiplication form |
| 3 | Checked three times |
| 4 | The Hermite functions are complete |
| 5 | The projection-valued measure, and the integral that replaces the sum |
| 6 | What $\ket x$ and $\ket p$ actually mean |
| 7 | What is now safe to do |
| 8 | Worked examples |
| 9 | Stone's theorem |
| 10 | Your turn |

**Note on the section order.** Stone sits at §9, after the checklist, because a written sentence in
4.2 names "Chapter 4.4 §9" for it and the number is worth preserving; it also reads better there,
as the hand-off to 4.6, than as an interruption between the functional calculus and $\ket x$. §7's
checklist is written to cover §9 as well, and says so. **If a later editor reorders, the promise in
4.2 must be re-aimed in the same commit.**

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The spectrum decomposed: point, continuous, residual | **4.4** §§3–4 | And the fact 0.9 flagged: $\hat p$ has **no eigenvectors in the space** and a purely continuous spectrum. **Collects 0.9 §5.3.** Define the spectrum by the failure of $(\hat A-\lambda)^{-1}$ to exist as a bounded everywhere-defined operator, and show that in finite dimensions this collapses to "eigenvalue" — so nothing has been redefined, only widened |
| 2 | **The spectral theorem, multiplication-operator form** ⚑ | ⚑, with hypotheses: every **self-adjoint** operator is unitarily equivalent to multiplication by a real function on some $L^{2}(\mu)$ | The one substantial mathematical flag of Part IV. State it as *the infinite-dimensional reading of 0.5's $A=UDU^{\dagger}$*, in exactly those words, and say that its proof (Cayley transform, continuous functional calculus, Riesz representation) is three chapters of analysis this book does not spend |
| 3 | **Verification 1: $\hat x$** | already multiplication by $x$ on $L^{2}(\R,\dd x)$ | Trivial, and that is the point: the theorem's *statement* is that everything looks like this |
| 4 | **Verification 2: $\hat p$** | the Fourier transform of **0.9** §2.3, which 0.9 proved unitary | $\mathcal F\hat p\mathcal F^{-1}$ is multiplication by $\hbar k$. Verified against a finite-difference derivative to $2\times10^{-4}$ on a 4096-point grid. One line, and it uses a unitary the reader built |
| 5 | **Verification 3: $\hat H_{\text{osc}}$**, on the Hermite functions | Hermite functions, **built complete here** | §4. **Derivable with what 4.3 built.** If $\avg{f,h_n}=0$ for all $n$ then $\int f(x)x^{n}\ee^{-x^{2}/2}\dd x=0$ for all $n$; expand $\ee^{-\ii kx}$ in its power series and interchange (**dominated convergence, 4.3 §4.3**, dominating function $\abs f\ee^{-x^{2}/2}\ee^{\abs{kx}}$, integrable by Cauchy–Schwarz); so the Fourier transform of $f\ee^{-x^{2}/2}$ vanishes identically; so $f=0$ by **0.9** §2.3. **No complex analysis, no ⚑.** Then $\hat H_{\text{osc}}$ is multiplication by $(n+\half)\hbar\omega$ on $\ell^{2}$. **This item collects 4.3's promise by name** — 4.3's closing brick says *"Chapter 4.4 also proves the Hermite functions complete, and that proof is statement (d) of §7.3 above run on an integral that only the dominated convergence of §4.3 licenses"* |
| 6 | The three verifications, collected | items 3–5 | Say it plainly: the reader now holds a quoted theorem **and has checked it in every case the book will use it**. That is the standard `PLAN-FORWARD.md` §3 sets, met. **This paragraph is the reason the flag in item 2 is honest, and it must not be cut for length** |
| 7 | The projection-valued measure form, and $\hat A=\int\lambda\,\dd P(\lambda)$ | item 2 | §5. **Collects 0.5 §6.4's two promises by name**: the projection form *"is the one that survives to infinite dimensions"*, and *"the sum $\sum_k\lambda_kP_k$ becomes an integral $\int\lambda\,\dd P(\lambda)$… Chapter 4.4 pays this bill in full"*. Both sentences name Chapter 4.4 and must be re-aimed to 4.5 — see Deliverable 2 |
| 8 | The Born rule for a continuous variable, restated | item 7; P3 | Half a page, and it closes a loop the reader will already have felt: 4.3 §5.3 said a vector of $L^{2}$ has no value anywhere, so $\abs{\psi(x_0)}^{2}$ is not a probability; item 7 says what $\int_a^b\abs\psi^{2}\dd x$ **is** — the expectation of the projection $P([a,b])$. No new postulate |
| 9 | **What $\ket x$ and $\ket k$ mean** | items 1, 7; **0.9** §5.3 | §6. The honest crutch first: **box normalisation, then the limit**, worked once in full so the reader has a procedure that always works. Then ⚑ Gelfand–Maurin and the rigged Hilbert space, with the concrete content stated — these are continuous functionals on a smaller space of well-behaved functions, and every manipulation using them abbreviates a wave-packet statement. **Collects 0.9's *"That gap is real. Chapter 4.4 closes it"*** and 0.9's delta row naming continuum normalisation $\avg{x|y}=\delta(x-y)$ — and says, in place, that the general theory of distributions is 5.4's, and that the word *closes* applies to the gap 0.9 named and to nothing wider. `GAPS.md` G11 |
| 10 | What is now safe to do, listed | the whole chapter | §7. A closing checklist: insert a resolution of the identity; expand in eigenstates; write $\ee^{-\ii\hat Ht/\hbar}$; integrate by parts and drop the boundary term. Each with the condition under which it is legitimate. **This list is what the rest of Part IV stands on.** It must include the exponential, which §9 licenses — say so forward, in one clause |
| 11 | **Stone, forward direction:** $\hat H$ self-adjoint $\Rightarrow$ $\ee^{-\ii\hat Ht/\hbar}$ unitary | item 2's functional calculus | §9. Three lines. ⚑ **the converse** (every strongly continuous one-parameter unitary group has a self-adjoint generator), which is the hard half. **This is what makes "time evolution is unitary" and "the Hamiltonian is self-adjoint" the same statement** — the sentence 0.5 §7 has been pointing at, and the sentence 4.2 names as *"quoted in Chapter 4.4 §9"* |

**Interactive:** none of its own. The chapter carries one figure that matters: the three
verifications side by side — $\hat x$, $\hat p$ and $\hat H_{\text{osc}}$ drawn as the same picture
in three different measures.

**Numerical confirmation:** Parseval in the Hermite basis — $\sum_{n<20}\abs{c_n}^{2}=1.00000000$
for a test function, with the Gram matrix equal to the identity to $10^{-8}$ at $M=40$. *(Carried
from old 4.4, where it was §0.3's entry.)*

**⚑ permitted in 4.5:** the spectral theorem for unbounded self-adjoint operators, in multiplication
form, with hypotheses — then verified three times (item 2); the converse half of Stone (item 11);
Gelfand–Maurin / the rigged Hilbert space (item 9). **Nothing else** — and specifically **not**
Hermite completeness, which is built. **Three.**

*(4.4 + 4.5 = five flags, exactly old 4.4's five. Nothing was added by splitting.)*

---

# 4.6 · The Schrödinger Equation

**What this chapter exists to do:** get the equation from two things already built — a unitary flow
with a self-adjoint generator, and one physical identification — and show that normalisation is
preserved as a theorem rather than a hope. **Not split**: items 1 to 9 are a single derivation
running from the group law to the continuity equation, and any cut inside it would leave a chapter
ending on an equation whose conservation law is in the next one.

**Objects introduced — seven (the seventh is three lines):**

1. **The one-parameter evolution group** $\hat U(t)$: the group law, and strong continuity
2. **The Schrödinger equation** $\ii\hbar\,\partial_t\ket\psi=\hat H\ket\psi$, and $\hat U=\ee^{-\ii\hat Ht/\hbar}$
3. **$\hat H=\hat p^{2}/2m+V(\hat x)$** — an identification, flagged as one
4. **$\hat p=-\ii\hbar\nabla$**, the position representation, with Stone–von Neumann ⚑ for uniqueness
5. **The probability current $\vv J$**, and $\pdv{\rho}{t}+\nabla\cdot\vv J=0$
6. **Stationary states** — *three lines from 4.5's spectral theorem*
7. **The Gaussian wave packet**: group velocity, and spreading

**Sections (fixed — §2 is load-bearing):**

| § | Title |
|---|---|
| 1 | What time evolution has to be |
| 2 | Stone, and the generator |
| 3 | Which operator is the generator |
| 4 | The equation in the position representation |
| 5 | The probability current |
| 6 | Stationary states |
| 7 | A free packet: group velocity, and spreading |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Evolution must be linear, and must preserve $\norm\psi=1$ | P1, P3 | **Collects 0.5's promise verbatim**: *"$U(t)$ must be unitary because $\norm\psi^{2}=1$ is a total probability"* |
| 2 | **Unitary $\Rightarrow$ $\abs\lambda=1$, and there is no third option** | **0.5** §7 | **Collects 0.5's sentence**: *"If $\abs{\lambda}\lt1$ the state would fade away and probability would leak out of the universe."* |
| 3 | $U(t+s)=U(t)U(s)$, $U(0)=\hat I$, strong continuity | item 1 | The group law is where "no memory" enters. Name it, and say which of the three assumptions 4.17 will have to give up |
| 4 | **$U(t)=\ee^{-\ii\hat Ht/\hbar}$ with $\hat H$ self-adjoint** | **4.5** §9 (Stone, converse half ⚑, cited not re-flagged) | And therefore $\ii\hbar\,\partial_t\ket\psi=\hat H\ket\psi$. **Collects 0.1's forward pointer**, the first sentence in the book that named a Part IV chapter. §2, and this is the section 4.2 names for the sign convention: **state the sign convention loudly here**, and note that the opposite time convention exists in some engineering literature |
| 5 | Why $\hbar$ and why $\ii$ | dimensions; and item 2 | **Collects 0.7's promise by name**: *"the $\ii$ is what makes time evolution a rotation in the space of states rather than a contraction, which is exactly what conserving total probability requires"* — 0.7 said this chapter would say what it is. Put the Schrödinger and diffusion equations side by side as 0.7 did |
| 6 | **$\hat H=\hat p^{2}/2m+V(\hat x)$ — an identification, not a derivation** | **1.3** §2.2's classical $H$; P6 | Say it is a choice, per pacing item 13, and name **4.10** §8 as where the choice is shown to be unextendable |
| 7 | $\hat p=-\ii\hbar\nabla$ in the position representation | P6, solved | **Collects 1.3's promise**: *"the operator $\hat p=-\ii\hbar\,\partial/\partial q$ is the standard realisation"* — 1.3 names Chapter 4.7 for it and it belongs here; see Deliverable 2. Show it is *a* realisation and note Stone–von Neumann ⚑ for uniqueness, with hypotheses (irreducibility, finitely many degrees of freedom) — the hypothesis that fails in 5.3 |
| 8 | **$\ii\hbar\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+V\psi$** | items 4, 6, 7 | **Collects 0.7's promise** that the kinetic term is a Laplacian, and 0.8's that adding an $\ii$ to the wave equation gives this |
| 9 | **The probability current and $\pdv{\rho}{t}+\nabla\cdot\vv J=0$** | multiply by $\psi^{*}$, subtract the conjugate — every step shown | Verified. **The chapter's centre.** $\vv J=\frac{\hbar}{m}\operatorname{Im}(\psi^{*}\nabla\psi)$, written with **0.7**'s own symbol $\vv J$ so the reader sees the same equation, not a cousin. **Collects 0.7 §6 by name** and makes "the wavefunction stays normalised" a theorem |
| 10 | Stationary states; $\hat H\psi=E\psi$ | separation of variables | Three lines. **Collects 0.8's promise**: *"In Chapter 4.6 the eigenvectors of $\hat H$ are the stationary states"* — note the reassignment in place: **this chapter defines them; 4.7 and 4.8 find them** |
| 11 | The general solution as a superposition | **4.5** §5's spectral decomposition | Every solvable problem in 4.7, 4.8 and 4.13 is this one line plus a diagonalisation |
| 12 | **A Gaussian packet, in full** | **0.2** §4's Gaussian integral, **0.9** §3 | **Collects 0.2's promises by name** (normalising a wave packet; $\abs\psi^{2}\propto\ee^{-2ax^{2}}$; and *"quantum mechanics then contributes one physical identification, $b=p/\hbar$"*) |
| 13 | Group velocity $=p/m$; **spreading $\sigma(t)^{2}=\sigma_0^{2}+(\hbar t/2m\sigma_0)^{2}$** | **0.8** §7.6's dispersion; **0.9** §3 | Verified numerically to eight figures. Give the number for an electron localised to 1 nm: it doubles in width in $\sim2.7\times10^{-14}$ s. ⚑ de Broglie's $\lambda=h/p$ for **matter** as experimental input, naming Davisson–Germer |
| 14 | Ehrenfest, **stated and deferred** | item 9 | State the two relations, say they are proved in **4.9** §4, and do **not** prove them here. 1.1's promise names 4.7 and must be re-aimed to 4.9 |

**Removed from this chapter:** old 4.5 item 15, *the Heisenberg picture and the fact that it is a
change of basis*, **moves to 4.9**, where the Heisenberg *equation* is derived. Keeping the picture
three chapters away from its equation was the one place old 4.5 and old 4.7 overlapped, and 0.4's
promise about the two pictures re-aims with it. Nothing is dropped.

**Interactive (one — carried from old 4.5):** a split-operator integration with a potential the
reader picks (free, step, barrier, oscillator) and $\abs\psi^{2}$, $\operatorname{Re}\psi$ and
$\vv J$ drawn together. **Test:** the norm is conserved to $4\times10^{-13}$ over the full run; in
the oscillator, $\avg x(t)$ tracks $x_0\cos\omega t$ to $2\times10^{-6}$; for the free packet the
displayed width matches item 13's formula to four figures.

**Numerical confirmation:** as the interactive's test — norm to $3.7\times10^{-13}$, $\avg x(t)$
tracking $2\cos t$ to $1.6\times10^{-6}$, free-packet spreading matching item 13 exactly.

**⚑ permitted in 4.6:** de Broglie's $\lambda=h/p$ for matter, naming Davisson–Germer (item 13);
the Stone–von Neumann uniqueness theorem, with hypotheses (item 7); the identification
$\hat H=\hat p^{2}/2m+V$, flagged as the choice it is (item 6). **Nothing else** — the converse of
Stone is **cited** from 4.5 and not re-flagged, which is one fewer than old 4.5's count and the
only place this re-plan reduces a flag. **Three.**

---

# 4.7 · Wells, Barriers, and Tunnelling

**What this chapter exists to do:** turn the equation into numbers on the four problems that are
exactly solvable with matching conditions, and show that the boundary condition is a choice the
reader watched being made in 4.4.

**Objects introduced — six:**

1. **The bound-state problem in one dimension**: matching $\psi$ and $\psi'$, as a domain condition
2. **Parity**, $\hat\Pi$, $\hat\Pi^{2}=\hat I$, and $[\hat\Pi,\hat H]=0$ for even $V$
3. **The infinite well**, $E_n=n^{2}\pi^{2}\hbar^{2}/2mL^{2}$
4. **The finite well**, and its transcendental condition
5. **Tunnelling**, and the transmission coefficient through a barrier
6. **Scattering states**, and $T+R=1$ from the current

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Bound states, and the boundary condition as a domain choice |
| 2 | Parity, and half the work |
| 3 | The infinite well |
| 4 | The finite well, and counting its bound states |
| 5 | The step, the barrier, and what transmission means |
| 6 | Tunnelling, with a number |
| 7 | Worked examples |
| 8 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The boundary condition is a choice of self-adjoint extension | **4.4** §7 | Do not let the reader think $\psi(0)=\psi(L)=0$ is obvious. It is one point in a $U(2)$, and the physics of an infinite wall is what selects it. **This item is why 4.4 comes before 4.7 and it must be one paragraph, not one clause** |
| 2 | **Matching $\psi$ and $\psi'$ at a finite step is the same statement** | item 1 | A jump in $\psi'$ costs a delta in $\psi''$, hence in $\hat H\psi$, hence leaves the domain. So the matching conditions are not a recipe: they are $\operatorname{dom}(\hat H)$ written out. And say what changes at an *infinite* step, where $\psi'$ may jump |
| 3 | **Parity** $\hat\Pi\psi(x)=\psi(-x)$; $\hat\Pi^{2}=\hat I$, so eigenvalues $\pm1$; $[\hat\Pi,\hat H]=0$ when $V$ is even | **4.2** §8's compatible observables | New object, and it earns its keep three times: it halves the finite-well algebra here, it kills half the fine-structure matrix elements in **4.16**, and it *is* the electric-dipole selection rule in **4.17**. Note the pattern: **a symmetry, a commuting observable, a label** — the same three-step move 4.11 will run on rotations |
| 4 | Infinite well: $E_n=n^{2}\pi^{2}\hbar^{2}/2mL^{2}$ | items 1–3; **0.8** §3 | And the zero-point energy read as uncertainty, using **0.9** §6. The ground state cannot have $E=0$ because $\psi\equiv0$ is not a state — say it that way, not by invoking a principle |
| 5 | Finite well: the transcendental matching condition, solved graphically | items 2–3; **0.8** §3 | Derive the condition; count the bound states; **show at least one always exists in one dimension**, which is false in three and is worth saying |
| 6 | The delta well, as the limit that has exactly one | item 5 with $V_0\to\infty$, $a\to0$, $V_0a$ fixed | Cheap, and it is the only bound-state problem in the book with a closed-form answer in one line: $E=-m\lambda^{2}/2\hbar^{2}$. Uses **0.9** §5's delta, which the reader owns |
| 7 | Scattering off a step: reflection above the barrier | **4.6** §5 | A classical particle with $E>V_0$ always transmits; this one does not. **Give the number** |
| 8 | **$T+R=1$ from the probability current** | **4.6** §5 | Use the current, not hand-waving. **This is what 4.6 §5 was for**, and the flux ratio is the only honest definition of $T$ — say why $\abs{t}^{2}$ alone is wrong when the two sides have different $k$ |
| 9 | **Tunnelling**, with an amplitude and a number | items 5, 8 | Give the transmission through a 1 eV barrier 1 nm wide for a 0.5 eV electron, computed exactly. ⚑ the STM and $\alpha$-decay measurements it is compared against. **Collects 4.2's promise**: *"the coupling is suppressed by three orders of magnitude rather than being zero is the quantitative content of tunnelling"*, and hand the exponential form forward to **4.10** §4 by name — 4.2 promises the WKB estimate to old 4.7 and it is now 4.10 |
| 10 | Resonant transmission: $T=1$ when $k'a=n\pi$ | item 9 | Half a page. A barrier that becomes perfectly transparent at particular energies, which is interference and nothing else — and it is the same condition as a bound state of the well, analytically continued. The reader should see the two problems as one |

**Interactive (one — new, and cheap):** a step/well/barrier with $V_0$, width and $E$ on sliders,
drawing $\abs\psi^{2}$, the incident/reflected/transmitted decomposition, and $T$ and $R$ read out.
**Test:** $T+R=1$ to $10^{-12}$ at every setting; $T$ matches the closed form to six figures; the
resonances land at $k'a=n\pi$.

**Numerical confirmation:** the finite well's transcendental roots against direct numerical
diagonalisation on a grid, agreeing to six figures for all bound states at three well depths; and
the 1 eV / 1 nm / 0.5 eV barrier computed by transfer matrix and by the closed form, agreeing to ten
figures.

**⚑ permitted in 4.7:** the STM and $\alpha$-decay measurements used for comparison (item 9).
**Nothing else.** **One.**

---

# 4.8 · The Oscillator, and the Ladder

**What this chapter exists to do:** solve the oscillator by algebra, because that method — not the
answer — is the whole of Parts V and VII, and carry 0.8's eight promises across.

**Objects introduced — six:**

1. **$\hat a$ and $\hat a^{\dagger}$**, and $[\hat a,\hat a^{\dagger}]=1$
2. **The number operator $\hat N$**, and the ladder $[\hat N,\hat a^{\dagger}]=\hat a^{\dagger}$
3. **$E_n=(n+\half)\hbar\omega$**, and the zero-point energy
4. **The oscillator eigenfunctions** $\psi_n\propto(\hat a^{\dagger})^{n}\psi_0$, which are the Hermite functions
5. **The phase-space area $(n+\half)h$**
6. **Coherent states**, $\hat a\ket\alpha=\alpha\ket\alpha$

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Two routes, and why only one is taken |
| 2 | Factorising $\hat x^{2}+\hat p^{2}$, and what the leftover is |
| 3 | The ladder |
| 4 | Why it stops |
| 5 | The wavefunctions, from $\hat a\ket0=0$ |
| 6 | The phase-space area, collected |
| 7 | Coherent states |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The oscillator by series — **stated and not done** | | §1. Say plainly that the differential-equation route exists, is standard, and is being skipped because the algebraic route is better teaching and is the one Parts V and VII use. `PLAN-FORWARD.md` §3.1's "never by series" decision, made visible. Half a page and no apology |
| 2 | $\hat a=\sqrt{\frac{m\omega}{2\hbar}}\big(\hat x+\frac{\ii}{m\omega}\hat p\big)$, $\hat a^{\dagger}$ | **0.5** §4's adjoint; P6 | Motivate by factorising $\hat x^{2}+\hat p^{2}$ as far as commutativity permits, and let the leftover **be** the commutator. That is where the zero-point energy comes from and it should be visible at the moment of factorisation |
| 3 | **$[\hat a,\hat a^{\dagger}]=1$; $\hat H=\hbar\omega(\hat a^{\dagger}\hat a+\half)$** | item 2, expanded | Verified |
| 4 | **$[\hat N,\hat a^{\dagger}]=\hat a^{\dagger}$, $[\hat N,\hat a]=-\hat a$** — the ladder | item 3 | Verified. Name the technique: this is the "commutator shifts the eigenvalue" move that **4.11** will run on $\hat J_\pm$, **4.13** on the radial $\hat A_\ell$, and 7.4 on the Virasoro modes. **Say that it appears three times in the next five chapters** — the reader who is told to expect it will recognise it |
| 5 | **The ladder terminates below**, because $\avg{\hat N}\ge0$ | item 3 and positivity of $\norm{\hat a\ket\psi}^{2}$ | The one step people skip. Do it: the spectrum is bounded below *because* a norm is non-negative |
| 6 | **$E_n=(n+\half)\hbar\omega$, from the algebra alone** | items 4–5 | Verified. **Collects 1.3's ⚑ by name** — *"which Chapter 4.6 will derive exactly, with ladder operators and no semiclassical approximation, and get precisely this answer"* — and 0.8's *"the $\tfrac12\hbar\omega$ that will not go away"* |
| 7 | $\psi_0\propto\ee^{-m\omega x^{2}/2\hbar}$ | solve $\hat a\psi_0=0$, a **first-order** equation | The whole point of the method: a second-order eigenvalue problem replaced by one first-order equation and an algebra |
| 8 | $\psi_n\propto(\hat a^{\dagger})^{n}\psi_0$, and these are the Hermite functions | item 7 | **Collects 0.5's promise**: *"The identical procedure with a weight $\ee^{-x^{2}}$ on the whole line produces the Hermite polynomials, which are the quantum harmonic oscillator states of Chapter 4.6."* Completeness is **cited from 4.5 §5, not re-proved** (§5.4 and §5.5; §5.6 says how far the verification reaches) — and 4.3's closing brick says exactly this will happen, so say that it has happened |
| 9 | $\avg{\hat x^{2}}=\avg{\hat p^{2}}/m^{2}\omega^{2}=(n+\half)\hbar/m\omega$; the uncertainty product is $(n+\half)\hbar$ | item 8 | Verified. The ground state saturates 0.9 §6.5's bound — the Gaussian, again. **Note in place that the general uncertainty relation is 4.9's**, and that this is an instance computed before the theorem, which is the order the book prefers |
| 10 | **The phase-space area is $(n+\half)h$** | item 6 and **0.8** §4.4's ellipse | Verified symbolically: $\oint p\,\dd q=2\pi E/\omega$. **Collects three promises at once** — 0.8's *"the area that Chapter 4.6 will quantise"*, 1.3 §4.4's Bohr–Sommerfeld ⚑, and 1.3's *"Three things to notice, all of which Chapter 4.6 will confirm by an exact operator calculation that uses none of this reasoning"*. Say that the *general* Bohr–Sommerfeld statement is **4.10** §6 and that this chapter has done the one case where it is exact |
| 11 | Coherent states: $\hat a\ket\alpha=\alpha\ket\alpha$ | item 4 | §7. A packet that does not spread, the closest thing to a classical oscillator, and a state that is not an energy eigenstate — which is worth saying out loud after six sections of eigenstates. It earns its place by being the bridge to 5.3 |
| 12 | Where this goes | | **Collects 0.8's and 0.3's forward pointers by name**: one oscillator per field mode (5.3), one per string mode (7.4), and *"those quanta… are what we call particles"* |

**Interactive (one — carried from old 4.6):** the ladder made operable — press $\hat a^{\dagger}$ or
$\hat a$ and watch the wavefunction climb or fall, with the energy, the classical turning points and
the phase-space ellipse drawn alongside. **Test:** the numerically diagonalised Hamiltonian's levels
are equally spaced to $10^{-10}$; the displayed $\avg{x^{2}}$ matches $(n+\half)\hbar/m\omega$ to
four figures at every rung.

**Numerical confirmation:** ~~the numerically diagonalised oscillator on a 60-state truncation~~ —
**this test was vacuous and 4.8's writer caught it.** Building $\hat H=\half(\hat X^{2}+\hat P^{2})$
out of truncated ladder matrices gives a matrix that is *identically diagonal* with entries
$n+\half$: the $\hat a^{2}$ and $\hat a^{\dagger2}$ pieces cancel exactly whatever the truncation, so
the check measures floating-point addition and nothing else (confirmed: max off-diagonal
$3.6\times10^{-15}$, and only the top state is wrong, $29.5$ against $59.5$). What 4.8 does instead is
a **position-space grid Hamiltonian** — a grid Laplacian plus $\half x^{2}$ — containing no ladder
operator, no Hermite function and no generating function. It returns the lowest sixteen levels
equally spaced to $6.2\times10^{-14}$. **The lesson generalises: a numerical check built out of the
same algebra as the result is not a check.**

**⚑ permitted in 4.8:** the vibrational spectroscopy data quoted in the worked examples.
**Nothing else** — every result in this chapter is derived, and the closing brick should say so.
**One.**

*(4.7 + 4.8 = two flags, exactly old 4.6's two.)*

---

# 4.9 · Commutators, Uncertainty, and Symmetry

**What this chapter exists to do:** *spend* the uncertainty relation rather than re-derive it — in
one line, as 0.9 promised — and then show that the same commutator that bounds a product of spreads
also generates the motion and the symmetries. **This chapter carries the largest single block of
debts in Part IV and most of them are paid in a sentence each, which is the point.**

**Objects introduced — five:**

1. **The general uncertainty relation** $\Delta A\,\Delta B\ge\half\abs{\avg{[\hat A,\hat B]}}$, and $\Delta x\,\Delta p\ge\hbar/2$ as its one-line instance
2. **The Heisenberg picture**, and the fact that it is a change of basis
3. **The Heisenberg equation** $\dv{\hat A}{t}=\frac{1}{\ii\hbar}[\hat A,\hat H]+\pdv{\hat A}{t}$
4. **Ehrenfest's theorem**, and the exact condition under which it looks classical
5. **Generators**: symmetry $\Rightarrow$ unitary $\Rightarrow$ conserved observable, in three cases

**Sections (fixed — §3 is load-bearing):**

| § | Title |
|---|---|
| 1 | One substitution: $p=\hbar k$ |
| 2 | The general relation, and what it is not |
| 3 | Compatible observables, and a complete set |
| 4 | The Heisenberg picture, and the Heisenberg equation |
| 5 | Ehrenfest, and the potentials for which it is exact |
| 6 | Symmetries, generators, and conserved quantities |
| 7 | Worked examples |
| 8 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **$\Delta x\,\Delta p\ge\hbar/2$, in one line** | **0.9** §6.4's bandwidth theorem, plus $p=\hbar k$ | **Collects six of 0.9's promises at once**, including *"All that quantum mechanics will add, in Chapter 4.7, is a single substitution: $p=\hbar k$"* and *"The bandwidth theorem → Chapter 4.7, which adds $p=\hbar k$ and nothing else."* **It must actually be one line.** If it takes a page the chapter has failed its brief |
| 2 | **$\Delta A\,\Delta B\ge\half\abs{\avg{[\hat A,\hat B]}}$** | **0.5** §1.4's Cauchy–Schwarz, applied to $(\hat A-\avg A)\ket\psi$ and $(\hat B-\avg B)\ket\psi$ | **Collects 0.5's four promises**, including *"Nothing is added in Chapter 4.7 except the physical meaning of the symbols."* Three lines. **Collects 4.2's** *"The second form is the one Chapter 4.7 needs, because it exhibits $\Delta A$ as the length of a vector"* — use 4.2's second form, not a fresh one |
| 3 | What the relation does **not** say | items 1–2 | **Collects 0.9's promise by name**: *"Measurement disturbance is a real and separate phenomenon with its own theorems, and Chapter 4.7 will keep the two apart."* It is a statement about the *spread of outcomes over an ensemble*, not about a microscope. Say so in a `warn` box — **and ⚑ the error–disturbance relations by name** (Ozawa; Busch–Lahti–Werner), because 0.9 said "with its own theorems" and naming none under-delivers while naming them unmarked would be an unflagged import. This flag is new in this re-plan and is the only one added anywhere in it |
| 4 | The dimensional consistency of every conjugate pair | **1.3** §2.1 | **Collects 1.3's promise**: *"$p_i$ is whatever pairs with $q^i$ so that $p_i\dd q^i$ has the dimensions of action"* |
| 5 | Compatible observables; the complete set of commuting observables | **0.5** §8 and **4.2** §4.3, unchanged | §3, the section 4.2 names. **Collects 0.5's "the qualitative content of Chapter 4.7"** and 4.2's *"Chapter 4.7 §3 asks how one knows a set is complete"* — answer that question, which is the one thing 4.2 did not: a set is complete when the common eigenspaces are one-dimensional, and in practice one shows it by exhibiting the count. Hand the definition to 4.11 and 4.13 |
| 6 | **The Heisenberg picture, and the fact that it is a change of basis** | **0.4** §4; **4.6** §2's $\hat U(t)$ | **Moved here from old 4.5 item 15.** It belongs beside the equation it generates. **Collects 0.4's promise verbatim**: *"why the Schrödinger and Heisenberg pictures look like different physics instead of different bases"* — 0.4 names Chapter 4.5 and must be re-aimed |
| 7 | **The Heisenberg equation** $\dv{\hat A}{t}=\frac{1}{\ii\hbar}[\hat A,\hat H]+\pdv{\hat A}{t}$ | item 6; **1.3** §6.1's classical version, term by term | **Collects 1.3's "the bracket goes to Chapter 4.7"**. Put the two equations side by side; the only difference is which bracket |
| 8 | **Ehrenfest:** $\dv{\avg{\hat x}}{t}=\frac{\avg{\hat p}}{m}$, $\dv{\avg{\hat p}}{t}=-\avg{\nabla V}$ | item 7 | Verified numerically. **Collects 1.1's promise by name**, including 1.1's own warning that *"read carefully that is not a fundamental law but a derived statement about expectation values"*. Then the crucial caveat: $\avg{\nabla V}\ne\nabla V(\avg x)$ unless $V$ is at most quadratic — which is why the oscillator is exactly classical in the mean and **nothing else is**. Point at 4.8's coherent state as the case where it is exact |
| 9 | Symmetry $\Rightarrow$ unitary $\Rightarrow$ conserved observable | **1.4** §7; **0.5** §7.1; **4.2** §7.5 | **Collects 1.3's "The generators of §7 go to… Chapter 4.2 (observables generate unitaries)"** — note the reassignment: 4.2 states it, this chapter proves it. Give translation, rotation and time as the three cases, as 1.4 §3 did. **Rotation is the one that matters**: it hands 4.11 its commutator, and the hand-off should be explicit |
| 10 | Where the classical limit begins, and where it is | | Half a page closing the chapter. Everything so far says the commutator *bounds*, *moves* and *generates*; what it does not yet say is what happens when $\hbar$ is small against the action in play. **That is 4.10, and 4.10 §8 will prove that the correspondence cannot be made exact** — announce both, because two written sentences of 4.2 name "§8" for the second and the reader should meet the claim before the proof |

**Interactive:** none of its own. One figure: the Cauchy–Schwarz triangle drawn as *lengths*, with
$\Delta A$ and $\Delta B$ as the two sides and $\half\abs{\avg{[\hat A,\hat B]}}$ as the projection —
the picture **0.5 §1.4**'s Cauchy–Schwarz and **4.2 §5.3**'s second form of $\Delta A$ point at.

**Numerical confirmation:** the Ehrenfest residuals at the finite-difference floor for a
split-operator run in a quartic potential, beside the same run in a quadratic one where they are
exactly zero — the two cases of item 8 measured against each other. And $\Delta x\,\Delta p$ for the
$n=3$ oscillator state reading $3.5\hbar$ to twelve figures, against $0.5\hbar$ for the Gaussian.

**⚑ permitted in 4.9:** the error–disturbance relations, named with their hypotheses and not proved
(item 3). **Nothing else** — everything else in this chapter is 0.5, 0.9, 1.3 and 4.2 spent.
**One.**

---

# 4.10 · The Classical Limit

**What this chapter exists to do:** say honestly how classical mechanics emerges, recover
Bohr–Sommerfeld from a real approximation scheme rather than a guess, and then prove the theorem
that says the correspondence cannot be exact.

**Objects introduced — five:**

1. **Hamilton–Jacobi as the $\hbar\to0$ limit**, and the one term that is the entire quantum content
2. **The WKB approximation**, and what its small parameter really is
3. **The connection formulae** ⚑
4. **Bohr–Sommerfeld $\oint p\,\dd q=(n+\half)h$**, recovered and *scored*
5. **The Groenewold–van Hove obstruction** ⚑, with the obstruction itself built

**Sections (fixed — §8 is load-bearing and named twice in 4.2):**

| § | Title |
|---|---|
| 1 | What "$\hbar\to0$" can and cannot mean |
| 2 | Hamilton–Jacobi, from the Schrödinger equation |
| 3 | The two real equations |
| 4 | WKB, and the small parameter |
| 5 | The connection formulae |
| 6 | Bohr–Sommerfeld, recovered and tested |
| 7 | Phase-space area, and the number of states |
| 8 | Why the correspondence cannot be exact |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | What the limit is a limit *in* | | §1, and it must come first. "$\hbar\to0$" is not a limit — $\hbar$ is a constant. The limit is in a *dimensionless ratio*: the action of the motion in units of $\hbar$, equivalently $\lambda$ varying slowly compared with itself. Say this before any algebra, because the rest of the chapter is otherwise a sequence of manipulations of a symbol that cannot vary |
| 2 | **Hamilton–Jacobi as the $\hbar\to0$ limit** | substitute $\psi=\ee^{\ii S/\hbar}$ into **4.6**'s equation | Verified symbolically: the exact result is $\partial_tS+\frac{(\partial_xS)^{2}}{2m}+V=\frac{\ii\hbar}{2m}\partial_x^{2}S$, and the right-hand side is the entire quantum content. **Collects 1.3 §8.2's ⚑ by name** — *"Hamilton–Jacobi goes to Chapter 4.7 as the classical limit of the Schrödinger equation — the last stop before the wavefunction"* |
| 3 | Reading the two real equations: Hamilton–Jacobi plus the continuity equation | split item 2 into $\abs\psi$ and phase | The phase is the classical action over $\hbar$, exactly as 1.3 promised. And the amplitude equation is **4.6** §5's current again — say so with 4.6's own symbol $\vv J$ |
| 4 | **WKB**, and the $\hbar$ in which it is an expansion | item 2, expanded in powers of $\hbar$ | Say what the small parameter really is (item 1), not "$\hbar$ small". Then **collect 4.2's tunnelling promise**: the exponential $\exp(-\frac1\hbar\int\abs p\dd x)$ is the suppression 4.7 §6 computed exactly for a rectangular barrier, and the two agree in the thick-barrier limit — **check that agreement numerically on the page**, because it is the only place in the book where an approximation and an exact answer for the same quantity sit side by side |
| 5 | ⚑ **The connection formulae**, with hypotheses | ⚑: a linear turning point, isolated, with the Airy asymptotics — which need the stationary-phase method **5.4** builds | Flag it, name 5.4, and then discharge it numerically in item 6 |
| 6 | **Bohr–Sommerfeld $\oint p\,\dd q=(n+\half)h$, recovered — and tested** | items 4–5 | Verified. **Exact** for the oscillator, which is why 1.3 §4.4's semiclassical guess was right. For $V=x^{4}/4$: $18\%$ error at $n=0$, $1.3\%$ at $n=1$, $0.17\%$ at $n=4$. For $V=\abs x$: $9.5\%$ at $n=0$, $0.13\%$ at $n=4$. **Print the table.** It shows exactly what "semiclassical" means, and it collects 1.3's and 0.8's Bohr–Sommerfeld ⚑ from the other side, and 1.3's *"⚑ Quoted, with the derivation deferred to Chapter 4.7"* |
| 7 | **A classical orbit of area $\mathcal A$ holds about $\mathcal A/h$ states** | item 6 | §7. **Collects 4.1's promise by name** — 4.1 §5 wrote *"Chapter 4.7 makes the statement precise by showing that a classical orbit enclosing area $\mathcal A$ in phase space corresponds to about $\mathcal A/h$ quantum states"* — and 4.1's *"It is the subject of Chapter 4.7"* about the dimensions of action. **Both re-aim to 4.10 and this is where they land.** Then say what it is for: it is the missing $\varsigma$ of 4.1 §3.1's classical partition function, supplied, and every density of states in Part V is this count |
| 8 | **Groenewold–van Hove: the correspondence cannot be exact** | ⚑ the general theorem, with hypotheses; **build the obstruction** | §8, the section 4.2 names twice. Verified. Classically $q^{2}p^{2}=\frac19\{q^{3},p^{3}\}=\frac13\{q^{2}p,qp^{2}\}$, so any quantisation respecting brackets must give the same operator both ways. With Weyl ordering the two routes differ by exactly $\tfrac13\hbar^{2}\hat I$. **Compute it, on the page.** ⚑ only the statement that no ordering rule whatsoever repairs it. **Collects 1.3's ⚑ for the third time**, and 4.2's two sentences: *"Section 8 postulates it for the single pair it needs, and Chapter 4.7 §8 proves that it cannot be extended consistently to all of them"* and *"What Chapter 4.7 §8 supplies is the sharper and more interesting statement, and that statement is negative"* |
| 9 | What survives: the bracket correspondence to leading order in $\hbar$ | item 8 | So P6 is safe, and "canonical quantisation" is a procedure for a restricted class of observables, not a functor. Say it. **And collect 2.2's promise** that *"classical mechanics is a limit of quantum mechanics (Chapter 4.7)"* — the limit exists, it is item 2, and item 8 says it is a limit and not a dictionary |

**Interactive (one — carried from old 4.7):** WKB levels against exact levels for a potential the
reader shapes, with the action-in-units-of-$\hbar$ on a slider. **Test:** for the oscillator the two
agree to $10^{-6}$ at every setting; for $V=x^{4}/4$ the relative error falls like $n^{-1}$ and
matches item 6's table to two figures.

**Numerical confirmation:** item 6's table — WKB against exact for $\tfrac12x^{2}$ (exact),
$x^{4}/4$ and $\abs x$ — together with the Groenewold obstruction computed as
$\tfrac19[\hat q^{3},\hat p^{3}]/\ii$ against $\tfrac13[\widehat{q^{2}p},\widehat{qp^{2}}]/\ii$,
differing by exactly $\tfrac13\hbar^{2}\hat I$ under Weyl ordering.

**⚑ permitted in 4.10:** the WKB connection formulae, with hypotheses, naming 5.4 (item 5); the
general Groenewold–van Hove no-go, with the concrete obstruction built rather than quoted (item 8).
**Nothing else** — Stone–von Neumann, if cited again, is cited from 4.6 and not re-flagged.
**Two.**

*(4.9 + 4.10 = three flags against old 4.7's two. The one addition is item 3's error–disturbance
relations, which 0.9 promised by name and the old plan left unmarked.)*

---

# 4.11 · The Angular Momentum Algebra

**What this chapter exists to do:** build the reader's first Lie algebra from a commutator they can
compute, and derive the entire spectrum from it with **nothing else** — which is a contract 1.4 wrote
into the text in those words.

**Objects introduced — six:**

1. **$[\hat L_i,\hat L_j]=\ii\hbar\epsilon_{ijk}\hat L_k$** — the algebra, computed not quoted
2. **The Casimir $\hat{\vv J}^{2}$**, and $[\hat{\vv J}^{2},\hat J_z]=0$
3. **$\hat J_\pm=\hat J_x\pm\ii\hat J_y$** — the ladder, a second time
4. **The multiplet:** $2j\in\mathbb Z_{\ge0}$, $m_j=-j,\dots,j$, $\hat{\vv J}^{2}=j(j+1)\hbar^{2}$, $2j+1$ states
5. **The matrix elements** $\hat J_\pm\ket{j,m_j}=\hbar\sqrt{j(j+1)-m_j(m_j\pm1)}\ket{j,m_j\pm1}$
6. **The Pauli matrices** $\vec\sigma$, as the $j=\half$ case — as algebra, before any physics

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The commutator, computed |
| 2 | A notation collision, resolved before it happens |
| 3 | What commutes with what |
| 4 | The ladder, a second time |
| 5 | Why it stops at both ends |
| 6 | $2j$ is a whole number |
| 7 | The matrices, written out |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **$[\hat L_i,\hat L_j]=\ii\hbar\epsilon_{ijk}\hat L_k$** | $\hat{\vv L}=\hat{\vv r}\times\hat{\vv p}$ and P6 (**4.2** §8) | Verified. **Collects 1.3's and 1.4's promises**, including 1.3's Problem 2 (*"say what both results become in Chapter 4.8"*) and 1.4's *"Chapter 4.8 finds the identical relation with commutators in place of brackets… and derives the entire quantum theory of angular momentum — including half-integer spin, which has no classical counterpart — from nothing but that algebra."* **The words "nothing but" are a contract: nothing outside the algebra may be used anywhere in this chapter.** Where 1.4's sentence also promises spin, say in place that the spin half of it is 4.12 |
| 2 | The **notation decision**, flagged in place | Conventions | §2. $m_\ell$, $m_s$, $m_j$ — never a bare $m$, which is mass. Flag it here in a `warn` box, as 2.6 §2 flags the rapidity clash. **This is the single most likely source of silent confusion in the part** and it belongs in its own numbered section, at the first use, not in a parenthesis |
| 3 | $[\hat{\vv L}^{2},\hat L_z]=0$ | item 1 | Verified. So $\hat{\vv L}^{2}$ and $\hat L_z$ are a complete set for the algebra — **4.9** §3's definition, used. **Collects 1.3's** *"Then show $\{\vv L^{2},L_{z}\}=0$, and say what both results become in Chapter 4.8"* |
| 4 | The algebra abstracted: $\hat{\vv J}$ is anything satisfying item 1 | items 1, 3 | One paragraph, and it is the move that makes the chapter general. From here on nothing is assumed about where $\hat{\vv J}$ came from — which is precisely what lets 4.12 find a representation with no wavefunction |
| 5 | $\hat J_\pm=\hat J_x\pm\ii\hat J_y$; $[\hat J_z,\hat J_\pm]=\pm\hbar\hat J_\pm$ | item 4 | **The same ladder move as 4.8 §3.** Say so explicitly — it is the second of three appearances and the reader was told in 4.8 to expect it |
| 6 | $\hat J_\mp\hat J_\pm=\hat{\vv J}^{2}-\hat J_z^{2}\mp\hbar\hat J_z$ | item 5 | The identity that closes the ladder at both ends |
| 7 | **The ladder terminates at both ends** | $\norm{\hat J_\pm\ket{jm_j}}^{2}\ge0$ with item 6 | Same argument as 4.8 §4. Positivity of a norm, twice — and this is the third time in three chapters that a spectrum has been bounded by a norm being non-negative. Name the pattern |
| 8 | **$2j$ is a non-negative integer; $m_j=-j,\dots,j$; $\hat{\vv J}^{2}=j(j+1)\hbar^{2}$; the multiplet has $2j+1$ states** | items 6–7: top and bottom must be joined by a whole number of steps | Verified for $j=\half,1,\tfrac32,2,\tfrac52$. **This is the chapter's theorem and it must be derived, not asserted.** Collects 1.3's promise that *"its magnitude takes the values $\sqrt{j(j+1)}\hbar$, that $j$ can be a half-integer, and hence that spin exists"* — derive the first two here and hand the third to 4.12 by name, in the same paragraph, so the promise is visibly not dropped |
| 9 | Matrix elements $\hat J_\pm\ket{j,m_j}=\hbar\sqrt{j(j+1)-m_j(m_j\pm1)}\ket{j,m_j\pm1}$ | item 6 | Verified. The phase convention (Condon–Shortley) is a choice; say that it is one |
| 10 | **The $j=\half$ matrices are $\tfrac12\vec\sigma$, and the $j=1$ matrices** | item 9 | Written out. **Still pure algebra: nothing yet says an electron is one of these.** And note that **0.5** WE2 already computed $\ee^{\ii\theta\sigma_x}$, so the exponential is not new either. **Collects 4.2's** *"Chapter 4.8 will describe electron spin with $2\times2$ matrices, and that is finite-dimensional"* — answer 4.2's objection here: these matrices carry no $[\hat x,\hat p]$, so 4.2 §8.4's theorem is not contradicted |
| 11 | What the algebra has **not** decided | items 8, 10 | Half a page closing the chapter. The algebra permits $j=\half$ and says nothing about whether nature uses it, and nothing about which physical system carries which $j$. **That is 4.12, and it is the one place in Part IV where nature chooses among possibilities the mathematics offered** — announce it |

**Interactive:** none of its own. One figure: the $2j+1$ rungs for $j=0,\half,1,\tfrac32,2$ drawn as
a lattice, with $\hat J_\pm$ as arrows and the two closure conditions marked where they bite.

**Numerical confirmation:** $[\hat J_i,\hat J_j]=\ii\hbar\epsilon_{ijk}\hat J_k$,
$\hat{\vv J}^{2}=j(j+1)$, $[\hat{\vv J}^{2},\hat J_z]=0$ and $\dim=2j+1$, all checked explicitly for
$j=\half,1,\tfrac32,2,\tfrac52$ with the matrices printed for the first two.

**⚑ permitted in 4.11:** **none.** Every result is derived from item 1, which is derived from P6.
`CONVENTIONS.md` says a chapter with no ⚑ is claiming to have built everything it spends; here that
claim is exactly 1.4's *"from nothing but that algebra"*, and the closing brick should say so in
those words. **Zero.**

---

# 4.12 · Spin, Orbitals, and Adding Angular Momenta

**What this chapter exists to do:** find out which of 4.11's representations nature uses, discover
one with no wavefunction at all, and learn to add two of them — which is what 4.13, 4.16 and 4.20
all need.

**Objects introduced — six (one of them a single quoted number):**

1. **Orbital angular momentum**: $\ell$ must be an integer, and the **spherical harmonics** $Y_\ell^{m_\ell}$, from the algebra
2. **Spin** (E1) — the electron carries $j=\half$, and there is no wavefunction behind it
3. **$g_e\approx2$** ⚑ — a measured number with a three-stage debt
4. **The rotation operator and the $720^{\circ}$ return**: $\ee^{-\ii\theta\hat n\cdot\vec\sigma/2}$
5. **Addition of angular momenta**, and $j_1\otimes j_2=\bigoplus_{j}\,j$ with its Clebsch–Gordan coefficients
6. **$\hat{\vv L}\cdot\hat{\vv S}=\half(\hat{\vv J}^{2}-\hat{\vv L}^{2}-\hat{\vv S}^{2})$**

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Orbital angular momentum, and why $\ell$ is an integer |
| 2 | The spherical harmonics, from the top state down |
| 3 | Spin: the representation with no wavefunction |
| 4 | Turning a spinor through $720^{\circ}$ |
| 5 | Adding two angular momenta |
| 6 | The two cases the book actually spends |
| 7 | Worked examples |
| 8 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **Orbital $\ell$ must be an integer** — the algebra does not know that | require single-valuedness of $\psi$ in $\varphi$ | The sharpest sentence available here: **the algebra permits half-integers and orbital motion does not realise them.** So the half-integer representations must belong to something with no wavefunction. Note honestly that single-valuedness is an assumption about the domain of $\hat L_z$ and not a theorem — **4.4** gave the reader the vocabulary to see that, and it costs one clause |
| 2 | **Spherical harmonics from the top state, by algebra** | solve $\hat L_+Y_\ell^{\ell}=0$: a **first-order** equation giving $Y_\ell^{\ell}\propto\sin^{\ell}\theta\,\ee^{\ii\ell\varphi}$, then lower with $\hat L_-$ using **4.11** §7 | Verified symbolically for $\ell=0,1,2,3$; lowering reproduces the standard $Y_\ell^{m_\ell}$ up to normalisation, checked to $\ell=2$. **No Legendre series anywhere.** `PLAN-FORWARD.md` §3.1's decision, executed, and it is the reason 4.13 fits in one chapter. **The same first-order trick as 4.8 §5** — third appearance of "annihilate the extreme state, then ladder down"; say so |
| 3 | Orthonormality and completeness of $\{Y_\ell^{m_\ell}\}$ on the sphere | cite **4.5** §2 | Do not re-prove. One sentence, and it is a use of the spectral theorem the reader has already checked three times |
| 4 | **E1: spin exists, and the electron has $j=\half$** | ⚑ experimental: Stern–Gerlach; the fine-structure doubling; the anomalous Zeeman effect | §3. Announced in its own box per pacing item 9. **Note that this is the one place in Part IV where nature chooses among possibilities the mathematics offered** — 4.11's closing brick promised this sentence. **Collects 4.2's** *"The measurement is that the electron carries half-integer angular momentum, which is Stern–Gerlach's, quoted in Chapter 4.8"* and 4.2's postulate-table row for E1 |
| 5 | $\hat{\vv S}=\tfrac\hbar2\vec\sigma$, and the three Stern–Gerlach measurements | item 4; **4.11** §7 | **Collects 4.2's** *"Chapter 4.8 measures exactly these with three Stern–Gerlach magnets in three orientations"* — the three components of the Bloch vector, measured. The 2×2 matrices were built in 4.11 with no physics; here they acquire a subject |
| 6 | ⚑ $g_e\approx2$ | ⚑ experimental here | **Name the three-stage debt in place:** measured here, derived from the Dirac equation in **5.5**, corrected to $g/2=1.00115965\ldots$ in **5.10**. A reader who is told the schedule will notice when it is kept. One paragraph |
| 7 | **A $360^{\circ}$ rotation multiplies a spin-$\half$ state by $-1$; $720^{\circ}$ returns it** | $\ee^{-\ii\theta\hat n\cdot\vec\sigma/2}=\cos\tfrac\theta2-\ii\sin\tfrac\theta2\,\hat n\cdot\vec\sigma$ | §4. Verified: $\ee^{-\ii2\pi\hat J_z/\hbar}=-\hat I$ for $j=\half$ and $+\hat I$ for $j=1$. **Collects 0.5's "already visible coming"** and 0.5's *"In Chapter 4.8, $\ee^{-\ii\theta\,\hat n\cdot\vec\sigma/2}$ is precisely the operator that rotates a spin-$\tfrac12$ state"*. Then say what is and is not observable: the sign is invisible on its own state and visible in interference — ⚑ the neutron-interferometry measurement |
| 8 | Adding two angular momenta: $\hat{\vv J}=\hat{\vv J}_1+\hat{\vv J}_2$ satisfies **4.11** item 1 | direct computation | One line, and it is why the whole apparatus applies again. The tensor product is P7 (**4.2** §9), used for the first time since it was postulated — say so |
| 9 | **$j_1\otimes j_2=\bigoplus_{j=\abs{j_1-j_2}}^{j_1+j_2}j$**, with the dimension check | count $m$ values with multiplicity and peel off multiplets from the top | Verified: $\sum_j(2j+1)=(2j_1+1)(2j_2+1)$. Do $\half\otimes\half=0\oplus1$ in full — the singlet and triplet, which **4.19** and **4.20** need |
| 10 | Clebsch–Gordan coefficients for the cases used | **4.11** §7's ladder, applied inside a fixed $j$ | ⚑ the general tables; derive $\half\otimes\half$ and $\ell\otimes\half$, which are the only two the book spends (**4.16** §3, **4.20** §1) |
| 11 | $\hat{\vv L}\cdot\hat{\vv S}=\half(\hat{\vv J}^{2}-\hat{\vv L}^{2}-\hat{\vv S}^{2})$ | item 8 squared | Verified: $\tfrac{\hbar^{2}}2[j(j+1)-\ell(\ell+1)-\tfrac34]$, giving $\ell\hbar^{2}/2$ for $j=\ell+\half$ and $-(\ell+1)\hbar^{2}/2$ for $j=\ell-\half$. **Handed forward to 4.16 §3 explicitly** |
| 12 | Forward pointer to **6.1** and **6.2** | | This algebra is $\mathfrak{su}(2)$, and 6.1 will notice that boosts, rotations, $\ee^{\ii A}$ and Poisson generators were all the same structure. **Collects 3.9's line** that *"the $\mathfrak{su}(2)$ of Chapter 4.8 is the algebra §1.1 of this chapter used to state isotropy"*, and 1.4's *"the reason quantum angular momentum is quantised in Chapter 4.8"* |

**Interactive (one — carried from old 4.8):** a spin-$\half$ state on the Bloch sphere with a
rotation angle the reader drives past $360^{\circ}$, showing **the state's position and its
amplitude's phase separately** — the sphere returns at $360^{\circ}$ and the phase does not.
**Test:** $\avg{\psi_0|\psi(\theta)}=\cos(\theta/2)$ exactly, reading $-1$ at $360^{\circ}$ and $+1$
at $720^{\circ}$, with the interference readout changing sign accordingly.

**Numerical confirmation:** $\ee^{-\ii\theta\hat J_z/\hbar}$ returning $-\hat I$ at $360^{\circ}$ and
$+\hat I$ at $720^{\circ}$ for $j=\half$, against $+\hat I$ at $360^{\circ}$ for $j=1$; and the
spherical harmonics from $\hat L_+Y_\ell^\ell=0$ checked against the standard forms for
$\ell=0,1,2,3$.

**⚑ permitted in 4.12:** E1, the experimental input that the electron carries $j=\half$ (item 4);
$g_e\approx2$, with 5.5 and 5.10 named (item 6); the neutron-interferometry measurement of the
$4\pi$ periodicity (item 7); the general Clebsch–Gordan tables, with the two cases used derived
(item 10). **Nothing else.** **Four.**

*(4.11 + 4.12 = four flags, exactly old 4.8's four, and all four are in the second piece — which is
why 4.11 can carry none.)*

---

# 4.13 · The Hydrogen Atom

**What this chapter exists to do:** solve the one system whose exact solution built the subject,
using the ladder for the third time — and end on a degeneracy that the symmetry used to derive it
cannot explain.

**Objects introduced — six:**

1. **The radial equation** for $u=rR$, and the effective potential
2. **The radial ladder** $\hat A_\ell=\dv{}{r}+\frac{\ell+1}{r}-\frac{1}{(\ell+1)a}$ — the factorisation
3. **$E_n=-\dfrac{\mu(\alpha c)^{2}}{2n^{2}}$**, the principal quantum number $n$, and $\ell\le n-1$
4. **$a_0$ and $v_1/c=\alpha$** — one line each, and the sentence 4.16 needs
5. **The radial functions**: nodes, and $\avg r_{n\ell}=\frac{a_0}{2}(3n^{2}-\ell(\ell+1))$
6. **The $n^{2}$ degeneracy**, and the puzzle it creates

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Two bodies become one |
| 2 | Separation, and why the angular part is already finished |
| 3 | The radial equation |
| 4 | Factorising it: the ladder, a third time |
| 5 | The spectrum, and the number that started the subject |
| 6 | The radial functions, and where the electron is |
| 7 | The degeneracy, and one factor too many |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Reduced mass $\mu=m_em_p/(m_e+m_p)$ | **1.1** §6, unchanged | And the number: it moves $-13.6057$ eV to $-13.5983$ eV, a shift of $7.4$ meV, which is measurable. Say which of the two numbers is which |
| 2 | Separation of variables; the angular factor **is 4.12's** | **4.12** §2 | **The ordering argument, made visible.** One sentence: separating the angular part *is* the representation theory of $\mathfrak{su}(2)$, which is why 4.11 and 4.12 come first. Under `PLAN.md`'s old ordering this chapter would have had to assert its own prerequisite. **Collects 0.4's promise** that *"the same eigenvalue machinery solves a coupled-oscillator problem in Chapter 0.8 and a hydrogen atom in Chapter 4.9"* |
| 3 | The radial equation for $u=rR$ | item 2 | With the effective potential $-\frac{\alpha\hbar c}{r}+\frac{\hbar^{2}\ell(\ell+1)}{2\mu r^{2}}$ — **written as $\alpha\hbar c$ and never as $e^{2}/4\pi\epsilon_0$ reassembled**, per Conventions |
| 4 | The boundary condition at the origin, argued not assumed | **4.4** §5 | $u(0)=0$ is a self-adjointness requirement, not a convenience. Two paragraphs, and it is 4.4's most direct dividend |
| 5 | **The factorisation** $\hat A_\ell=\dv{}{r}+\frac{\ell+1}{r}-\frac{1}{(\ell+1)a}$ | the same move as **4.8** §3 and **4.11** §4 | Verified symbolically: $\frac{\hbar^{2}}{2\mu}\hat A_\ell\hat A_\ell^{\dagger}=\hat H_\ell-E_{\ell+1}$ and $\frac{\hbar^{2}}{2\mu}\hat A_\ell^{\dagger}\hat A_\ell=\hat H_{\ell+1}-E_{\ell+1}$. **The third and last appearance of the ladder. Name it as such**, and point back at both earlier ones by chapter and section |
| 6 | **$\hat H_\ell\ge E_{\ell+1}$, with equality iff $\hat A_\ell^{\dagger}u=0$** | item 5 and positivity of a norm — the same step as 4.8 §4 and 4.11 §5 | Gives $u\propto r^{\ell+1}\ee^{-r/(\ell+1)a}$ directly, from a first-order equation. **Fourth time a spectrum is bounded by a norm being non-negative** |
| 7 | **The intertwining $\hat H_{\ell+1}\hat A_\ell^{\dagger}=\hat A_\ell^{\dagger}\hat H_\ell$** | item 5 | Verified. So every level of $\hat H_{\ell+1}$ is a level of $\hat H_\ell$: **the $\ell$-channels share their spectra, and the energy cannot depend on $\ell$.** This is the algebraic statement of the degeneracy and it arrives before the group theory |
| 8 | **$E_n=-\dfrac{\mu(\alpha c)^{2}}{2n^{2}}=-\dfrac{13.606\ \mathrm{eV}}{n^{2}}$**, $n=\ell+1,\ell+2,\dots$, hence $\ell\le n-1$ | items 6–7 | Verified numerically by integrating the radial equation for $\ell=0,1,2,3$. **Collects 4.1's promise by name**: *"Chapter 4.9 derives it, including the value of $R$, and that derivation is one of the three or four things quantum mechanics is believed for"*, and 4.1's *"Chapter 4.9 supplying the two integers"*. **Use the measured $R_\infty hc=13.605693122994$ eV ⚑ for comparison, not a reconstruction** |
| 9 | $a_0=\hbar/(\alpha m_ec)=52.918$ pm; $v_1/c=\alpha$ | item 8 | **The sentence 4.16 needs:** hydrogen is a system that is relativistic at the $1\%$ level, so corrections of relative order $\alpha^{2}=5.3\times10^{-5}$ are expected. **Collects 0.3's promise** that *"in hydrogen the electron's typical speed is $v\approx\alpha c$ (Chapter 4.9)"* |
| 10 | The radial functions and their nodes; $\avg r_{n\ell}=\frac{a_0}{2}(3n^{2}-\ell(\ell+1))$ | item 6, laddered | Verified symbolically for seven $(n,\ell)$ pairs. Note that $\avg r$ *does* depend on $\ell$ while $E$ does not — which sharpens the puzzle. **Also compute $\avg{1/r}=1/n^{2}a_0$, $\avg{1/r^{2}}=1/[(\ell+\half)n^{3}a_0^{2}]$ and $\avg{1/r^{3}}$ here, and say they are being computed for 4.16** — they are pure radial algebra and putting them in 4.16 would make that chapter carry a seventh object for no reason |
| 11 | **The degeneracy is $\sum_{\ell=0}^{n-1}(2\ell+1)=n^{2}$** | item 8 and **4.11** §6 | Verified. Derive the sum, do not quote it. With spin, $2n^{2}$ — and the periodic table's $2,8,18,32$ |
| 12 | **The puzzle stated sharply** | items 10–11 | §7, and it is the closing brick. Rotational symmetry explains the $(2\ell+1)$ and nothing else. Degeneracy across different $\ell$ needs a symmetry that is not rotation. **0.5 predicted this**: *"a degenerate energy level is one where the Hamiltonian alone does not tell you which state you are in"*. **Collects 4.2's** *"exactly what Chapter 4.9's degeneracies will need"* and *"the reason Chapter 4.9's hydrogen states need three labels"*. Then name 4.14 and say what it will produce: a conserved vector, and a spectrum derived a second time with the degeneracy falling out as a dimension count. **This is the same shape as 4.3's ending and 4.13's reader should be told it is** |

**Interactive (one — carried from old 4.9):** the orbital $\abs{\psi_{n\ell m_\ell}}^{2}$ in a cut
plane with $n$, $\ell$, $m_\ell$ selectors, beside a level diagram whose degeneracies are drawn as
stacked states. **Test:** the displayed $\avg r$ matches $\frac{a_0}{2}(3n^{2}-\ell(\ell+1))$ to
three figures; the level diagram's multiplicity at level $n$ counts $n^{2}$; the radial node count is
$n-\ell-1$.

**Numerical confirmation:** the radial equation integrated numerically for $\ell=0,1,2,3$, giving
$-\tfrac12 n^{-2}$ hartree with $\ell\le n-1$ falling out, and $\avg{1/r}$, $\avg{1/r^{2}}$,
$\avg{1/r^{3}}$, $\avg r$ against their closed forms for seven $(n,\ell)$ pairs.

**⚑ permitted in 4.13:** the completeness of the bound states **together with the continuum**, cited
from 4.5 and flagged where the scattering states are named; the measured $R_\infty$ used for
comparison. **Nothing else.** **Two.**

---

# 4.14 · The Degeneracy, and $SO(4)$

**What this chapter exists to do:** answer the question 4.13 ended on — find the conserved quantity
that rotation does not account for, and derive the spectrum a second time from an algebra, with the
degeneracy falling out as a dimension count.

**Objects introduced — four.** A low count and a long chapter: this is five symbolic identities and
a representation-theoretic argument, at about 2,500 words per object, which is the book's own rate
and the opposite of the failure this re-plan exists to fix.

1. **The quantum Runge–Lenz vector** $\hat{\vv A}$, and the ordering problem that forces its symmetrisation
2. **The closed algebra**: $[\hat L_i,\hat A_j]$, $[\hat A_i,\hat A_j]$, and the rescaled $\hat{\vv D}$
3. **$\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$**, and the two commuting $\hat{\vv I}$, $\hat{\vv K}$
4. **The spectrum, from the algebra alone**, with $n=2j+1$ and degeneracy $(2j+1)^{2}$

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The puzzle, restated, and what a symmetry would have to look like |
| 2 | The classical vector, and why the orbit closes |
| 3 | The quantum Runge–Lenz vector, and the first time ordering costs something |
| 4 | The algebra it closes |
| 5 | Two commuting $\mathfrak{su}(2)$s |
| 6 | The spectrum, a second time |
| 7 | What the model still leaves out |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | What would have to be true | **4.13** §7 | §1. Half a page. A degeneracy across different $\ell$ needs an operator that commutes with $\hat H$ and does **not** commute with $\hat{\vv L}^{2}$ — say that first, so the reader knows what is being looked for before it is produced. Per pacing item 1: announce the destination |
| 2 | **The classical Runge–Lenz vector, recalled** | **1.4** WE2 | Conserved because the Kepler orbit closes; points along the major axis; exists for $1/r$ and for nothing else. One page, and it is 1.4's own calculation, not a new one |
| 3 | **The quantum Runge–Lenz vector** $\hat{\vv A}=\frac{1}{2\mu}(\hat{\vv p}\times\hat{\vv L}-\hat{\vv L}\times\hat{\vv p})-\dfrac{\alpha\hbar c}{r}\hat{\vv r}$ | item 2, symmetrised | Say why the symmetrisation is needed — $\hat{\vv p}$ and $\hat{\vv L}$ do not commute — and that **this is the first time in the book operator ordering has cost anything**. Point back at **4.10** §8: ordering ambiguity is exactly what Groenewold–van Hove was about, and here is a case where a choice has to be made by hand |
| 4 | **$[\hat H,\hat A_i]=0$; $\hat{\vv A}\cdot\hat{\vv L}=\hat{\vv L}\cdot\hat{\vv A}=0$; $\hat A^{2}=\frac{2\hat H}{\mu}(\hat{\vv L}^{2}+\hbar^{2})+(\alpha\hbar c)^{2}$** | item 3, computed | **All three verified symbolically.** Grind box for the algebra, statements outside. The middle one is why $\hat{\vv A}$ adds only two new labels, not three |
| 5 | **$[\hat L_i,\hat A_j]=\ii\hbar\epsilon_{ijk}\hat A_k$; $[\hat A_i,\hat A_j]=-\ii\hbar\frac{2\hat H}{\mu}\epsilon_{ijk}\hat L_k$** | item 3, computed | **Both verified symbolically.** The second is the one that matters: the commutator of two Runge–Lenz components is an angular momentum, *with a coefficient that depends on the energy*. The first says $\hat{\vv A}$ is a vector under rotations, which is a statement the reader can now read off a commutator rather than being told |
| 6 | **On a bound level, $\hat{\vv D}=\sqrt{-\mu/2\hat H}\,\hat{\vv A}$ closes $\mathfrak{so}(4)$** | item 5 with $\hat H<0$ | The rescaling is legitimate on a fixed eigenspace and illegitimate off it — say so, and say that this is why the argument gives the bound states and not the continuum |
| 7 | **$\hat{\vv I}=\half(\hat{\vv L}+\hat{\vv D})$, $\hat{\vv K}=\half(\hat{\vv L}-\hat{\vv D})$ are two commuting $\mathfrak{su}(2)$s** | item 6 | And $\hat{\vv I}^{2}=\hat{\vv K}^{2}$ because $\hat{\vv L}\cdot\hat{\vv D}=0$ — so one label $j$, not two. **Everything here is 4.11 applied twice** and the reader should be told that no new representation theory is being used |
| 8 | **$E=-\dfrac{\mu(\alpha c)^{2}}{2\hbar^{2}(2j+1)^{2}}$, so $n=2j+1$ — and the degeneracy is $(2j+1)^{2}=n^{2}$** | items 4, 7 | Verified symbolically. **The spectrum a second time, by pure algebra, with the degeneracy falling out as a dimension count.** Per `MATHPLAN-3.md` §0 item 8: two derivations of the important result, one showing where it comes from and one showing why it had to be that |
| 9 | $\ell$ runs $0\ldots n-1$ because $j\otimes j$ contains $\ell=0,\ldots,2j$ | **4.12** §5 | The range of $\ell$, recovered from representation theory. Nothing left unexplained |
| 10 | **The classical shadow** | **1.4** WE2 | The Runge–Lenz vector is conserved because the Kepler orbit closes; the extra degeneracy is that conservation law after quantisation. **Collects 1.4's ⚑ verbatim: *"And the payoff arrives in Chapter 4.9."*** That sentence names 4.9 and must be re-aimed to 4.14; strike the flag in the same commit |
| 11 | What the model leaves out, listed honestly | | §7. Fine structure (**4.16**), the Lamb shift (⚑, partly **5.10**), hyperfine structure (⚑), the proton's finite size (⚑). Give the size of each so the reader knows the accuracy of what they have derived. **This closes the hydrogen pair and hands 4.16 its agenda** |
| 12 | Forward pointer to **6.1**, **6.2** | | $\mathfrak{so}(4)$, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, and the fact that this is the *second* accidental-looking coincidence of algebras the book has met — the first was 2.2's. 6.1 explains both |

**Interactive:** none of its own. One figure: the $n=3$ level drawn twice — once as
$\ell=0,1,2$ with $2\ell+1$ states each, once as a single $j=1$ pair of $\mathfrak{su}(2)$s with
$(2j+1)^{2}=9$ — the same nine states counted two ways.

**Numerical confirmation:** the five Runge–Lenz identities verified symbolically on a general test
function, and $\hat{\vv I}^{2}=\hat{\vv K}^{2}$ checked numerically on the $n=3$ eigenspace with the
degeneracy counted as $9$.

**⚑ permitted in 4.14:** the Lamb shift, hyperfine structure and the proton radius, each with its
size (item 11); and one methodological flag, that the Runge–Lenz symmetrisation is *a* choice whose
uniqueness is not proved here. **Nothing else** — the spectrum is derived and the degeneracy is
explained. **Two.**

*(4.13 + 4.14 = four flags, exactly old 4.9's four.)*

---

# 4.15 · Perturbation Theory

**What this chapter exists to do:** build the approximation scheme the rest of the book runs on, in
the one setting where it can be checked exactly against a diagonalisation — and then say honestly
that the series does not converge.

**Objects introduced — four:**

1. **The perturbation expansion**: $E_a^{(1)}=V_{aa}$, $\ket a^{(1)}$, $E_a^{(2)}$
2. **Degenerate perturbation theory**: diagonalise $\hat V$ inside the degenerate subspace
3. **The variational principle**, $\avg{\hat H}\ge E_0$
4. **The series is asymptotic, not convergent** — with Dyson's argument

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The setup, and what the small parameter really is |
| 2 | First and second order |
| 3 | Degeneracy, and why the naive formula explodes |
| 4 | The variational principle |
| 5 | The series does not converge |
| 6 | Worked examples |
| 7 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | $\hat H=\hat H_0+\lambda\hat V$, and the expansion in $\lambda$ | **0.3** §4's asymptotic series | State at the outset that $\lambda$ is a bookkeeping device and the real small parameter is $\abs{V_{ab}}/\Delta E$. Item 8 comes back to this. **Collects 4.3's** *"Chapter 4.10's perturbation series"*, whose first correction is an infinite sum over the unperturbed basis and therefore needs completeness — say which theorem is being spent |
| 2 | **$E_a^{(1)}=V_{aa}$** | expand and project onto $\ket a$ | Verified numerically |
| 3 | $\ket{a}^{(1)}=\sum_{b\ne a}\dfrac{V_{ba}}{E_a-E_b}\ket b$ | project onto $\ket b$ | Verified: overlap with the exact eigenvector is $1$ to ten decimal places at $\lambda=10^{-5}$ |
| 4 | **$E_a^{(2)}=\sum_{b\ne a}\dfrac{\abs{V_{ab}}^{2}}{E_a-E_b}$** | item 3 | Verified: the residual against exact diagonalisation scales as $\lambda^{3}$ over three decades. **The ground state always moves down** — say why, and note this is the same fact that makes the van der Waals force attractive |
| 5 | **Degenerate perturbation theory: diagonalise $\hat V$ inside the degenerate subspace** | items 3–4 break; **0.5** §6 applied to the block | Verified. **Collects 0.5's promise**: *"why 'lifting a degeneracy' — with a magnetic field, say — is such a common experimental move"*. **That sentence names Chapter 4.8 and has to be re-aimed here** — see Deliverable 2 and Finding 3. Say what the right zeroth-order states are: the ones $\hat V$ chooses, not the ones you brought |
| 6 | The Zeeman effect, worked | item 5; **4.12** §5 | The cheapest possible instance of item 5 and the one 0.5's sentence had in mind: $\hat V=-\vec\mu\cdot\vv B$ lifts the $(2\ell+1)$-fold degeneracy, the right basis is $\hat L_z$'s, and the splitting is linear in $B$. Half a section, and it means 4.16 can start straight into the relativistic term |
| 7 | The variational principle: $\avg{\hat H}\ge E_0$ for any trial state | **4.5** §5's spectral decomposition | §4. Two lines. Then use it: a Gaussian trial on hydrogen gets $-11.5$ eV against $-13.6$, and the reader sees a bound that is honest rather than lucky. Say what it is for in Part V and VII: it is the only method in the book that gives a *one-sided* error |
| 8 | **The series is asymptotic, not convergent** | **0.3** §4 | §5. Verified. For $\hat H=\half(\hat p^{2}+\hat x^{2})+\lambda\hat x^{4}$ the coefficients are $\tfrac12,\tfrac34,-\tfrac{21}8,\tfrac{333}{16},-\tfrac{30885}{128},\ldots$ with $\abs{E_{n+1}/E_n}$ growing linearly in $n$ — factorial growth, zero radius of convergence. **And Dyson's argument, in miniature and completely accessible: for $\lambda<0$ the potential is unbounded below, so there is no ground state at all, so $E(\lambda)$ cannot be analytic at $\lambda=0$.** Show optimal truncation: at $\lambda=0.01$ the best is order 11 and gives $2\times10^{-11}$; at $\lambda=0.2$ the best is **order 1**. `GAPS.md` G12 pre-paid, and 5.11's shock set up |

**Interactive (one — new, and cheap):** an $8\times8$ Hermitian $\hat H_0+\lambda\hat V$ with
$\lambda$ on a slider, plotting the exact eigenvalues against the first- and second-order curves, and
the residual on a log axis beside them. **Test:** the second-order residual falls as $\lambda^{3}$
over three decades; at a level crossing the non-degenerate formula visibly diverges and the
degenerate one does not.

**Numerical confirmation:** as the interactive's test, plus the Bender–Wu coefficients
$\tfrac12,\tfrac34,-\tfrac{21}8,\tfrac{333}{16},-\tfrac{30885}{128}$ reproduced exactly with
linearly growing ratios, and the optimal-truncation table.

**⚑ permitted in 4.15:** the Bender–Wu asymptotic form of the coefficients — the *divergence* is
derived by Dyson's argument, only the growth *rate* is quoted (item 8). **Nothing else.** **One.**

---

# 4.16 · The Fine Structure of Hydrogen

**What this chapter exists to do:** compute the three corrections of relative order $\alpha^{2}$,
watch them combine into a formula that depends on $j$ and not on $\ell$, and print the residual
against measurement so the reader can see exactly what is missing.

**Objects introduced — four:**

1. **The relativistic kinetic correction** $\hat H_{\text{rel}}=-\hat p^{4}/8m^{3}c^{2}$
2. **The spin–orbit term**, including the Thomas factor of $\half$
3. **The Darwin term** ⚑
4. **$E_{n,j}$** — the three combining into one formula that depends on $j$

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | What order to expect, and why |
| 2 | The $p^{4}$ term |
| 3 | Spin–orbit, and the factor of two from Chapter 2.2 |
| 4 | The Darwin term, and what it is waiting for |
| 5 | Three terms, one formula |
| 6 | How good it is, and what the residual is |
| 7 | Worked examples |
| 8 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The size of the correction, before computing it | **4.13** §5's $v_1/c=\alpha$ | §1. One paragraph. $\alpha^{2}\times13.6\ \mathrm{eV}=7.2\times10^{-4}$ eV is the answer's order of magnitude and the reader should hold it before the algebra starts. **Collects 2.5 §3.3's** *"the point here is that the leading piece of it is a term in the expansion and nothing more exotic"* |
| 2 | **$\hat H_{\text{rel}}=-\hat p^{4}/8m^{3}c^{2}$** | **2.5** §3.1's expansion of $\sqrt{p^{2}c^{2}+m^{2}c^{4}}$, third term | **Collects 0.3 WE2 and 2.5 §3.3 by name** — 2.5 wrote *"Chapter 4.10 computes the full splitting"*, which re-aims here |
| 3 | **$\avg{\hat H_{\text{rel}}}=-\dfrac{E_n^{2}}{2mc^{2}}\Big(\dfrac{4n}{\ell+\half}-3\Big)$** | rewrite $\hat p^{4}=[2m(\hat H_0-V)]^{2}$ — the trick that avoids a fourth derivative — with **4.13** §6's $\avg{1/r}$ and $\avg{1/r^{2}}$ | Verified symbolically for five $(n,\ell)$ pairs against the closed form. **The number: $-9.06\times10^{-4}$ eV for the ground state**, against 2.5's estimate of $7.2\times10^{-4}$ eV. Say that the estimate was right |
| 4 | The spin–orbit term $\dfrac{1}{2m^{2}c^{2}}\dfrac1r\dv{V}{r}\hat{\vv L}\cdot\hat{\vv S}$, **including the factor of $\half$** | the electron-frame field, **then** Thomas | §3. **Derive the naive term first and get it wrong by two.** Then take the $\half$ from **2.2**'s boxed result $M=\exp(\phi_2K_y+\phi_1K_x+\tfrac12\phi_1\phi_2J_z+\cdots)$ — verified numerically. **Collects 2.2's promise verbatim**: *"this contributes a factor of $\tfrac12$ to the spin–orbit coupling in atomic fine structure. Without it, the predicted fine-structure splitting is wrong by a factor of two."* The ⚑ stays where 2.2 put it, on BCH; **no new flag** |
| 5 | $\avg{\hat{\vv L}\cdot\hat{\vv S}}$, and why $\ket{n\ell jm_j}$ is the right basis | **4.12** §6's $\hat{\vv L}\cdot\hat{\vv S}=\half(\hat{\vv J}^{2}-\hat{\vv L}^{2}-\hat{\vv S}^{2})$; **4.15** §3 | Degenerate perturbation theory choosing its own basis — 4.15 item 5, in action, on the case that matters. **This is the payoff of splitting 4.15 from 4.16: the reader met the rule two chapters ago on a $2\times2$ block and meets it here on the case that decides the answer** |
| 6 | ⚑ **The Darwin term** $\dfrac{\hbar^{2}}{8m^{2}c^{2}}\nabla^{2}V$ | ⚑ its coefficient, with the Zitterbewegung smearing given **explicitly as a heuristic and labelled as one** | §4. It affects $\ell=0$ only, which is exactly the case parity (**4.7** §2) does not save you from. Name **5.5**: the Dirac equation produces all three terms at once, and that is the right way to see it. `MATHPLAN-4.md` §"Where I am uncertain" item 3 stands: keep it, label the heuristic in the strongest terms available, and give the arithmetic showing it is the term that makes the $j$-dependence work |
| 7 | **$E_{n,j}=E_n\Big[1+\dfrac{\alpha^{2}}{n^{2}}\Big(\dfrac{n}{j+\half}-\dfrac34\Big)\Big]$** | items 3, 5, 6 | §5. Verified. Three terms, each depending on $\ell$, summing to something that does not — say that this is not a coincidence and that 5.5 explains it |
| 8 | **How good it is** | item 7 | §6. **The $2p_{3/2}$–$2p_{1/2}$ interval comes out $4.528\times10^{-5}$ eV $=10.949$ GHz against a measured $10.969$ GHz** — a $0.2\%$ residual which is the QED correction, ⚑ and named for 5.10. **Print both numbers.** This is the best "how good is it, and what is missing" moment in Part IV and it deserves its own numbered section rather than a closing paragraph |

**Interactive:** none of its own. One figure: the $n=2$ level of hydrogen drawn four times — bare,
plus $p^{4}$, plus spin–orbit, plus Darwin — with the $\ell$-dependence visibly cancelling between
the third and fourth columns and the measured interval marked.

**Numerical confirmation:** $\avg{\hat H_{\text{rel}}}$ against the closed form symbolically for five
states, giving $-9.06\times10^{-4}$ eV at $n=1$; the Thomas $\half$ extracted numerically from
$\log(\ee^{\phi_2K_y}\ee^{\phi_1K_x})$ to ten figures; and the full $E_{n,j}$ giving $10.949$ GHz
against $10.969$ GHz measured.

**⚑ permitted in 4.16:** the Darwin term's coefficient, with the heuristic labelled and 5.5 named
(item 6); the QED residual in the fine-structure interval, naming 5.10 (item 8); the measured
fine-structure interval (item 8). **Nothing else** — and specifically **not** the Thomas factor,
which is derived from 2.2. **Three.**

---

# 4.17 · Transitions

**What this chapter exists to do:** do perturbation theory when the Hamiltonian depends on time —
which is where the group law fails and the exponential becomes a series — and get a transition
*rate*, checked against an exact integration.

**Objects introduced — six:**

1. **The interaction picture**
2. **The Dyson series, and time-ordering** — recognised as the survival function
3. **The rotating-wave approximation**, and the driven two-level system
4. **Fermi's golden rule** $\Gamma=\frac{2\pi}{\hbar}\abs{V_{fi}}^{2}\rho(E_f)$
5. **Selection rules**, from parity and from $\hat{\vv L}$
6. **The adiabatic theorem** ⚑, with its gap condition, and the Berry phase ⚑

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | When the group law fails |
| 2 | The interaction picture |
| 3 | The Dyson series, and a function you already know |
| 4 | A driven two-level system, exactly |
| 5 | First order, and the kernel that becomes a delta |
| 6 | Fermi's golden rule, and what "linear in $t$" requires |
| 7 | Which transitions happen at all |
| 8 | Slow change: the adiabatic theorem |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Where the group law fails | **4.6** §2's three assumptions | §1. $\hat U(t,s)\ne\hat U(t-s)$ once $\hat H$ depends on time, so $\ee^{-\ii\hat Ht/\hbar}$ is simply wrong. **Collects 4.2's** *"There $\hat H(t)$ depends on time, the group law fails, and $\ee^{-\ii\hat Ht/\hbar}$ is wrong. Chapter 4.10 §8 handles that case"* — this is the one written §-level promise in Part IV whose section number changes, from §8 to **4.17 §3** |
| 2 | The interaction picture | items in **4.15**; **4.9** §4's Heisenberg picture | §2. A third picture, and the reader has met two — say explicitly that it is neither, that it splits the evolution between states and operators, and that the split is a choice made to isolate $\hat V$ |
| 3 | **The Dyson series and time-ordering** | item 2 iterated | §3. **The survival-function identity, made explicit**: $S(t)=\exp\!\big(-\!\int_0^th\big)$ from a hazard model and the Dyson series are the same object, and **time-ordering is the only new ingredient**. `PLAN-FORWARD.md` §5.1(c)'s Familiar Ground row, landed. When 5.8 meets this again it must be a recognition, and the closing brick should say so by name |
| 4 | **The rotating-wave approximation, and the driven two-level system** | item 2; **4.2** §10's static two-state solution | §4. **New item — the current plan has none, and 4.2 promises this twice.** 4.2 wrote *"Chapter 4.10 shows that in a frame rotating with the drive the problem becomes [the static matrix] with $\delta=0$ and $\Delta=\hbar\Omega_R/2$"* and *"That reduction is Chapter 4.10's and is not derived here."* Derive it: go to the rotating frame, drop the counter-rotating term, say what is thrown away and when that is legitimate ($\Omega_R\ll\omega_0$), and recover 4.2's Rabi formula exactly. Then **integrate the full equation numerically and show the counter-rotating term's residue** — the Bloch–Siegert shift — so the approximation is scored rather than asserted |
| 5 | First order in time; the $\sin^{2}$ kernel | item 3 truncated | §5. And the fact 4.2's figure already showed the reader: **every detuned curve leaves the origin along the same parabola**, with the detuning absent from the leading term. **Collects 4.2's two sentences about exactly this**, which name it as what the transition rate is built on |
| 6 | **Fermi's golden rule** $\Gamma=\frac{2\pi}{\hbar}\abs{V_{fi}}^{2}\rho(E_f)$ | item 5; the $\sin^{2}$ kernel becoming $2\pi t\,\delta$ | §6. Verified: $\int\frac{\sin^{2}(\Delta t/2)}{(\Delta/2)^{2}}\dd\Delta=2\pi t$ exactly (**0.9** §5's delta, used). Then **check it numerically**: a two-level system integrated exactly gives $0.970$ of the first-order prediction at $Vt/2=0.3$, which is exactly $\sin^{2}(0.3)/0.3^{2}$; integrating over detuning reproduces the linear-in-$t$ rate to $0.6\%$. **Say what "linear in $t$" requires**: a continuum, and a time long compared with $1/\Delta E$ and short compared with the lifetime. The density of states $\rho(E_f)$ is **4.10** §7's phase-space count — point at it |
| 7 | **$B_{12}=B_{21}$, recovered** | item 6; **4.1** §5 | **New item — the current plan has none, and 4.1 promises it by name:** *"$B_{12}=B_{21}$ returns in Chapter 4.10 as the equality of two matrix elements that Hermiticity makes automatic."* Two lines: $\abs{V_{fi}}^{2}=\abs{V_{if}}^{2}$ because $\hat V$ is Hermitian, so absorption and stimulated emission have equal rate constants. **What 4.1 got from a thermodynamic limit, 4.17 gets from P2.** That is the same shape as 4.11's second Planck derivation and the two should be named together |
| 8 | **Selection rules** | **4.7** §2's parity; **4.12** §5's Clebsch–Gordan | §7. $\avg{f|\hat{\vv r}|i}$ vanishes unless $\Delta\ell=\pm1$ and $\Delta m_\ell=0,\pm1$ — parity kills the first, the $\ell\otimes1$ decomposition kills the second. **Two chapters' machinery spent in one page**, and it is why most transitions do not happen |
| 9 | ⚑ **The adiabatic theorem**, with hypotheses | ⚑: a spectral gap that does not close, and evolution slow compared with $\hbar/\Delta E^{2}$ | §8. **Collects 1.3's promise by name**: *"The modern statement is Chapter 4.10's adiabatic theorem: a quantum system stays in the $n$-th eigenstate under slow change, which is the same sentence with $J$ replaced by $n$"* — the quantum version of the adiabatic invariant. Per pacing item 10 the gap condition is stated, not waved at, and the reader is shown a level crossing where it fails. Mention the Berry phase in one sentence and ⚑ it |

**Interactive (one — carried from old 4.10):** a driven two-level system, exactly integrated, with
drive strength and detuning on sliders, plotted against the first-order prediction and against the
rotating-wave solution — so the reader can watch perturbation theory work, watch it fail, and watch
the RWA hold and then break. **Test:** at $Vt/2=0.3$ the ratio of exact to first-order reads
$0.970$; the exact curve returns to $P=1$ at the Rabi time while the first-order curve passes $1$ and
keeps going, visibly; the RWA curve tracks the exact one until $\Omega_R/\omega_0$ is pushed up.

**Numerical confirmation:** the two-level system integrated at $10^{-11}$ tolerance against
first-order theory (ratio $0.970$ at $Vt/2=0.3$) and against the golden rule (linear rate to $0.6\%$).

**⚑ permitted in 4.17:** the adiabatic theorem with its gap hypothesis (item 9); the Berry phase
(item 9). **Nothing else** — the rotating-wave approximation is derived *and scored*, not quoted.
**Two.**

*(4.15 + 4.16 + 4.17 = six flags, exactly old 4.10's six, and two build items that the old plan
owed and did not have are now placed.)*

---

# 4.18 · Identical Particles

**What this chapter exists to do:** show that "these two are the same kind of thing" is a statement
with arithmetic consequences — an exclusion principle, an energy with no term in the Hamiltonian
responsible, and the Planck law a second time from a completely different direction.

**Objects introduced — five:**

1. **The exchange operator $\hat P_{12}$**, and why its eigenvalues can only be $\pm1$
2. **P8, the symmetrisation postulate** ⚑
3. **Slater determinants**, and the Pauli principle **as a corollary**
4. **Exchange energy** — an interaction that is not an interaction
5. **Bose–Einstein and Fermi–Dirac occupation numbers**

**Sections (fixed — §3 and §5 are load-bearing):**

| § | Title |
|---|---|
| 1 | Two particles |
| 2 | Identical, and what that costs |
| 3 | The symmetrisation postulate |
| 4 | Exchange, which is not a force |
| 5 | Occupation numbers, and the Planck law a second time |
| 6 | Worked examples |
| 7 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The two-particle space $\mathcal H_1\otimes\mathcal H_2$; product states and the rest | P7 (**4.2** §9); **0.4** §2 | Count dimensions and note immediately that most states are not products. **That single count is the whole of what 4.19 needs from here** — 4.2's own sentence says so: *"The counting is what makes entanglement a fact about arithmetic rather than a mystery."* Do the count and hand it forward by name |
| 2 | The exchange operator $\hat P_{12}$; $\hat P_{12}^{2}=\hat I$, so eigenvalues $\pm1$ | item 1 | Derived. The two possibilities are forced by an algebraic fact, and only the *choice between them* is postulated. Same move as parity in **4.7** §2 — an involution, two eigenvalues, a label. Third time; name it |
| 3 | **P8 — symmetrisation** | ⚑ postulate box | §3, the section 4.2 names. And say exactly what is not being claimed: **which** sign goes with which spin is **not** derived here. ⚑ spin–statistics, naming **5.5**, and state the two computations 5.5 will do — a Dirac field quantised with commutators has a Hamiltonian unbounded below; a scalar quantised with anticommutators fails to commute at spacelike separation |
| 4 | Slater determinants; **the Pauli principle as a corollary, not a postulate** | items 2–3 | Two fermions in the same state give a vanishing vector. Derived in one line from P8. Then $2n^{2}$ per shell and the periodic table, which **4.13** §7 counted and could not yet justify |
| 5 | **Exchange energy: an interaction that is not an interaction** | items 3–4 with a spin-independent Hamiltonian | §4. Compute $\avg{(x_1-x_2)^{2}}$ for symmetric and antisymmetric states and get a difference with no term in the Hamiltonian responsible. **This is the most surprising consequence of P8 and it is a two-line calculation.** Then say where it goes: it is why ferromagnetism exists and why the covalent bond binds, and neither is a new force |
| 6 | **Bose–Einstein and Fermi–Dirac occupation numbers** | the grand canonical sum over occupations, using **0.6** WE1's method with a second multiplier | §5, the section 4.1 names twice. Verified: $\avg n=1/(\ee^{\beta(\epsilon-\mu)}\mp1)$; both reduce to Boltzmann when $\ee^{\beta(\mu-\epsilon)}\ll1$. **`GAPS.md` G3's second half, closed** |
| 7 | **The Planck law, a second time** | item 6 with $\mu=0$ and **4.1** §2's mode count | **Collect 4.1 explicitly**: the same formula, from a completely different argument, and neither used the other. 4.1 promised this four separate times — *"What repairs it. Chapter 4.11 §5 derives a second time and by a completely different route"* — and this is where the promise is kept. Say which assumption each route made instead of the other: 4.1 borrowed the classical limit as a boundary condition, this route borrows P8. **And say that 4.17 §7 did the same thing to $B_{12}=B_{21}$** — twice in three chapters, a result got from thermodynamics has been got again from a postulate, and that pattern is worth naming |
| 8 | What is still counted, and what is not | | Half a page. Fixed particle number is still assumed everywhere; a state with an indefinite number of particles has not been written down and cannot be until 5.3. **Collects 4.1's** *"there is no statistics of light in this book until Chapter 4.11"* — the statistics now exist; the field does not |

**Interactive:** none of its own. One figure: two wells and two particles, drawn three ways —
distinguishable, symmetric, antisymmetric — with $\avg{(x_1-x_2)^{2}}$ read out under each.

**Numerical confirmation:** $\avg n=1/(\ee^{\beta(\epsilon-\mu)}\mp1)$ evaluated against direct
summation over occupations for a small system, and the second Planck derivation reproducing 4.1's
$\sigma=5.6704\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}$ from a route that shares no step with it.

**⚑ permitted in 4.18:** P8, the symmetrisation postulate (item 3); the spin–statistics theorem,
naming 5.5 and stating its two computations (item 3). **Nothing else.** **Two.**

---

# 4.19 · Density Matrices and Entanglement

**What this chapter exists to do:** build the object that answers "what is the state of *this half*",
find that a pure state of a pair can have no answer for either part, and show by computation that
this transmits nothing.

**Objects introduced — five:**

1. **The density matrix** $\hat\rho$, with $\operatorname{tr}\hat\rho=1$ and $\avg{\hat A}=\operatorname{tr}(\hat\rho\hat A)$
2. **Pure versus mixed**, $\operatorname{tr}\hat\rho^{2}=1$ or $<1$
3. **The reduced density matrix**, by partial trace
4. **Entanglement**, defined by a computation — and the entropy $S=-\operatorname{tr}\hat\rho\ln\hat\rho$
5. **No-signalling**

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The question the state vector cannot answer |
| 2 | The density matrix |
| 3 | Ignorance and superposition are different |
| 4 | The state of a part |
| 5 | Entanglement, stated precisely |
| 6 | Nothing is transmitted |
| 7 | Worked examples |
| 8 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The question | **4.18** §1; **4.2** §9 | §1. Half a page and it must come first: given a pure state of two systems, what is the state of the first? For a product state the answer is obvious; for the singlet there is **no vector** that reproduces its statistics. **Collects 4.2's** *"That is why Chapter 4.11 has to build a different object, the density operator, to answer it"* |
| 2 | The density matrix $\hat\rho$; $\operatorname{tr}\hat\rho=1$, $\avg{\hat A}=\operatorname{tr}(\hat\rho\hat A)$ | **0.5** §1's trace inner product $\operatorname{tr}(A^{\dagger}B)$ | **Collects 0.9's promise by name**: *"Probability, variance, the CLT → Chapter 4.11 (density matrices and measurement statistics)"*. Note the macro name: there is no `\tr`, so write $\operatorname{tr}$ |
| 3 | Pure vs mixed: $\operatorname{tr}\hat\rho^{2}=1$ or $<1$ | item 2 | §3, and the crucial distinction the chapter turns on: a mixture is ignorance, a superposition is not. **Do it as a computation, not a slogan**: exhibit two $\hat\rho$ with the same diagonal, one pure and one mixed, and find the observable that separates them. **Collects 4.2's** *"It is built in Chapter 4.11, where the distinction is what decoherence is about"* — the distinction is built here; what decoherence does with it is 4.20 |
| 4 | The Bloch ball: mixtures are the interior | item 3; **4.2** §3's Bloch sphere | **Collects 4.2's** *"(States inside it exist and are mixtures, which is Chapter 4.11's density operator.)"* One paragraph, and it makes item 3 visible rather than algebraic |
| 5 | **The reduced density matrix**, by partial trace | items 1, 2 | §4. Verified: for the singlet, $\hat\rho_A=\half\hat I$, $\operatorname{tr}\hat\rho_A^{2}=\half$. Define the partial trace by what it must do — reproduce every expectation of every observable on $A$ alone — and then derive the formula, rather than defining the formula and checking |
| 6 | **Entanglement, defined**, and the entropy | item 5 | §5. A pure state of the pair is **entangled** exactly when $\operatorname{tr}\hat\rho_A^{2}<1$. **A pure state of the pair whose parts are maximally uncertain** — that is entanglement, defined by a computation rather than a slogan. Then $S=-\operatorname{tr}\hat\rho_A\ln\hat\rho_A=\ln2$ for the singlet, and note that $S_A=S_B$ always, which is a theorem and a surprise |
| 7 | **No-signalling** | item 5: $\hat\rho_A$ is unchanged by anything done at $B$ | §6. Compute it — including the case where $B$ measures and does not report. **This is the antidote to every popular account the reader has met**, and it must be arithmetic, not reassurance |
| 8 | What is still unanswered | | Half a page. The correlations are real, no signal passes, and nothing yet said rules out the parts having had definite values all along. **That is 4.20, and the reader should be told that the question is about to become a measurable number.** Same shape as 4.13 → 4.14 |

**Interactive (one — new, and cheap):** a two-qubit state on a slider from product to maximally
entangled, showing $\hat\rho_{AB}$, $\hat\rho_A$, $\operatorname{tr}\hat\rho_A^{2}$ and $S$ together,
with a "measure at B" button that visibly changes nothing on the left. **Test:**
$\operatorname{tr}\hat\rho_A^{2}$ runs from $1$ to $0.5$ and $S$ from $0$ to $\ln2=0.6931472$;
$\hat\rho_A$ is unchanged to $10^{-15}$ under every unitary applied at $B$.

**Numerical confirmation:** for the singlet, $\hat\rho_A=\half\hat I$,
$\operatorname{tr}\hat\rho_A^{2}=0.5$, $S=\ln2=0.6931472$; and $\hat\rho_A$ invariant to $10^{-15}$
under $10^{3}$ random unitaries applied at $B$.

**⚑ permitted in 4.19:** **none.** Everything is 0.5's trace inner product and 4.2's P7, computed.
**Zero.**

---

# 4.20 · Bell, Decoherence, and What Is Settled

**What this chapter exists to do:** turn "could they have had definite values all along" into a
number, measure it, find that quantum mechanics violates the classical bound and then stops at a
bound of its own — and close Part IV by saying precisely what has and has not been explained.

**Objects introduced — four:**

1. **The singlet correlation** $E(\hat a,\hat b)=-\cos\theta$
2. **The CHSH inequality** $\abs S\le2$, for any local hidden-variable model
3. **The Tsirelson bound** $2\sqrt2$ — derived, not quoted
4. **Decoherence**, built on one explicit model

**Sections (fixed — §9 is load-bearing and named four times in 4.2):**

| § | Title |
|---|---|
| 1 | The singlet, and its correlation |
| 2 | What a local hidden-variable model is, exactly |
| 3 | CHSH, derived |
| 4 | Quantum mechanics gives $2\sqrt2$ |
| 5 | Tsirelson: and no further |
| 6 | The experiments |
| 7 | Decoherence: what it explains |
| 8 | What it does not explain |
| 9 | What is settled, and what is not |
| 10 | Worked examples |
| 11 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **The singlet's correlation $E(\hat a,\hat b)=-\cos\theta$** | **4.12** §5's Pauli matrices and the singlet from $\half\otimes\half$ | §1. Verified to twelve figures at seven angles. **Do this by explicit computation with 4.12's matrices** — it is the chapter's one piece of real algebra and everything else rests on it |
| 2 | **What a local hidden-variable model is** | | §2. State the three hypotheses separately — locality, realism, and measurement independence — **before** any inequality, per pacing item 10. Say that the last one is an assumption people do argue about, and that the first two are the ones the reader's intuition supplies for free |
| 3 | **The CHSH inequality $\abs S\le2$** | four $\pm1$ assignments; $AB-AB'+A'B+A'B'=A(B-B')+A'(B+B')$, one bracket zero, the other $\pm2$ | §3. Verified by exhaustion over all sixteen deterministic assignments: the value is always exactly $\pm2$, so any mixture obeys the bound. **Collects 4.2's** *"The description 'each has a definite but unknown value, correlated at preparation' reproduces these particular numbers and is ruled out by measuring other observables, which is the content of Bell's inequality"* |
| 4 | **Quantum mechanics gives $2\sqrt2$** | item 1 at $a=0^{\circ}$, $a'=90^{\circ}$, $b=45^{\circ}$, $b'=135^{\circ}$ | §4. Verified: $S=-2.82842712$. **Get the angles right** — the commonly quoted $(0,90,45,-45)$ gives exactly zero with this sign convention, and the plan says so because it is the kind of slip that ships |
| 5 | **Tsirelson: quantum mechanics cannot exceed $2\sqrt2$ either** | $\hat{\mathcal B}^{2}=4\hat I+[\hat A,\hat A']\otimes[\hat B,\hat B']$ with $\norm{[\hat A,\hat A']}\le2$ | §5. Verified: the operator identity holds exactly and the CHSH operator's eigenvalues are $\{-2\sqrt2,0,0,2\sqrt2\}$. **Derived, not flagged.** Quantum mechanics violates the classical bound and then stops at a bound of its own, and that second fact is as interesting as the first |
| 6 | ⚑ The experiments | ⚑ with hypotheses: Aspect 1982 and the 2015 loophole-free tests, with the detection and locality loopholes named and said to be closed | §6. Per pacing item 10 |
| 7 | **Decoherence: what it explains** | build one explicit model — a two-level system coupled to $N$ environment spins — and watch the off-diagonal elements of $\hat\rho$ decay | §7. ⚑ the general theory; build the one case. Give the timescale, and the number for a dust grain: coherence gone in $\sim10^{-31}$ s. **This is 4.19's $\operatorname{tr}\hat\rho^{2}$ falling, watched happening** — and the reader should be told that is what they are looking at |
| 8 | **What decoherence does not explain** | item 7 against P3 and P4 | §8. It explains why interference terms become unobservable. **It does not explain why the probabilities are $\abs\psi^{2}$, and it does not select an outcome.** `GAPS.md` G13. Say it plainly and without apology. **Collects 4.2's four sentences that name §9 for exactly this**, including *"states precisely which part of the problem decoherence addresses and which part it does not touch"* — the separation of P3 from P4 is what makes that sentence sayable, and 4.2 said so twice |
| 9 | Interpretations, briefly and without adjudication | | Half a section. Copenhagen, many-worlds and Bohm get one paragraph between them, named and not adjudicated. **`MATHPLAN-4.md`'s "must not do" list is binding: this chapter does not become an interpretations essay**, and its weight stays on items 1–5 and 7 |
| 10 | **The postulate ledger, closed** | §0.1 | §9. Reprint the table of P1–P8 and E1 with, for each, what was assumed, what was derived from it, and where (if anywhere) the assumption is discharged later — P8 in 5.5, P2's self-adjointness in **4.4** §4, P5's half in **4.6** §2. **Eight postulates and one measurement is what Part IV cost, against the twenty-odd theorems of Part 0 it renamed.** This is the closing brick of the part. **Collects 4.2's** *"Nothing else in Part IV is asserted without being derived. Chapter 4.11 §9 puts the whole list back on one page"* — and that claim is now checkable against seventeen chapters' flag lists, so **check it and say the total** |
| 11 | The handoff to Part V | | Say what the reader now has that Part V needs: a Hilbert space with domains, self-adjoint generators, $\mathfrak{su}(2)$, ladder operators, an interaction picture, and identical particles. And say what breaks: fixed particle number, once $\Delta E\,\Delta t\gtrsim\hbar$ meets $E=mc^{2}$ |

**Interactive (one — carried from old 4.11):** the CHSH experiment — four analyser angles on dials,
the four correlations and $S$ read out live, with the classical bound at $2$ and Tsirelson's at
$2\sqrt2$ drawn as lines, and a local-hidden-variable simulator running alongside. **Test:** at
$(0^{\circ},90^{\circ},45^{\circ},135^{\circ})$ the readout is $2.8284$; the quantum curve touches
$2\sqrt2$ and never exceeds it; the hidden-variable simulator over $10^{5}$ runs never exceeds $2$.

**Numerical confirmation:** $E(\hat a,\hat b)=-\cos\theta$ to twelve figures; the classical bound
$\pm2$ by exhaustion over sixteen assignments; $\abs S=2\sqrt2=2.82842712$ confirmed as the numerical
optimum over 40 restarts; $\hat{\mathcal B}^{2}$'s eigenvalues $\{-2\sqrt2,0,0,2\sqrt2\}$.

**⚑ permitted in 4.20:** the Bell experiments with their loopholes named (item 6); the general theory
of decoherence, with one model built (item 7); the Born rule and the measurement problem, restated
as permanently open and labelled as the second kind of flag (item 8). **Nothing else** — Tsirelson
is derived and the CHSH bound is derived. **Three.**

*(4.18 + 4.19 + 4.20 = five flags, exactly old 4.11's five.)*

---

## ⚑ budget for the part

| Ch | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 | 4.10 | 4.11 | 4.12 | 4.13 | 4.14 | 4.15 | 4.16 | 4.17 | 4.18 | 4.19 | 4.20 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ⚑ | 7 | 10 | 2 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 0 | 4 | 2 | 2 | 1 | 3 | 2 | 2 | 0 | 3 | **51** |

**51, unchanged.** The arithmetic: 4.1–4.3 are written and carry 19; the old plan gave 4.4–4.11
thirty-two, and the seventeen new chapters carry thirty-two. Two changes cancel: **one flag is added**
(4.9's error–disturbance relations, which 0.9 promised "with its own theorems" and the old plan left
unnamed and unmarked) and **one is removed** (old 4.5 counted the converse of Stone even while
saying it was cited rather than re-flagged; 4.6 cites and does not count it).

Three chapters now carry **zero** flags — 4.11, 4.19, and nothing else — and in each case that is a
claim the chapter is making out loud: the angular-momentum spectrum comes from the algebra and
nothing else, which is the contract 1.4 wrote; the density matrix is 0.5's trace inner product and
4.2's P7, computed. Both closing bricks should say so.

Of the 51, **eight are postulate boxes** (P1–P7 in 4.2, P8 in 4.18), about a third are experimental
inputs, and **exactly one is the substantial mathematical flag of the part** — the spectral theorem
for unbounded self-adjoint operators, now in 4.5 §2 and discharged into three explicit verifications
in 4.5 §§3–4.

---

## Batch order

The batches do not double. Sixteen chapters at 9,000–12,000 words pair naturally where the old
plan's twenty-thousand-word chapters could not.

| Batch | Contents | Note |
|---|---|---|
| F5 | **4.4 + 4.5** | The two halves of one repair; one agent, because item 1 of 4.4 and item 1 of 4.5 are the same sentence split |
| F6 | 4.6 + 4.7 | The equation, then the first systems it solves |
| F7 | 4.8 + 4.9 | The ladder, then the commutator that generates it |
| F8 | 4.10 + 4.11 | |
| F9 | 4.12 + 4.13 | Spin and addition, then the atom that needs both |
| F10 | **4.14 alone** | Five symbolic identities and a representation-theoretic argument. It is the 3.4 of this stretch |
| F11 | 4.15 + 4.16 | The tool, then the case that decides it |
| F12 | 4.17 + 4.18 | |
| F13 | 4.19 + 4.20 + Part IV reunification pass | Per `PLAIN-TERMS-PLAN.md` §7 |

**Nine batches against `MATHPLAN-4.md`'s six remaining (F5–F10).** Three extra batches, against
seventeen chapters instead of eight — which is the real saving of the split: the *batch* got bigger
in chapter count and smaller in words per chapter, which is the direction that has worked.

**Before F5, and not during it:** apply the remap of Deliverable 2 in one commit, regenerate
`python3 debts.py 4.N` for every N in 4..20, and confirm `build.py`'s `PARTS` list matches the
twenty titles above.

---

# Deliverable 2 · The promise triage

`python3 debts.py 4.4` … `4.11` returns **171** sentences. Every one is accounted for below. The
counts in each block sum to that block's total, and the blocks sum to 171.

## Summary

| Category | What has to happen | Count |
|---|---|---|
| **A** | **Lands correctly. No edit at all** — chapter number *and* section number both survive | **6** |
| **B** | Chapter number changes, one-to-one, no judgement — the chapter did not split | 28 |
| **C** | Chapter number changes, and **which piece** of a split chapter is a judgement | 114 |
| **D** | The sentence must be **widened** to name two chapters, because it describes work now done by both | 13 |
| **E** | The sentence must be **split** — different clauses point at different chapters | 6 |
| **F** | **Cross-subject re-aim** — the named material left the old chapter entirely | 4 |
| | **Total** | **171** |

**165 of 171 need an edit.** That is the honest number, and it is larger than "only the ones whose
material moved into the second piece", because the shift renumbers every chapter after the first
split whether it split or not. **See Finding 1: the rule as stated understates the bill by about a
factor of eight, and the bill is still worth paying.**

What makes it affordable is that **114 of the 165 are one substitution each with a decided answer**
— the table below decides them — **28 are a blind find-and-replace**, and only **23 (categories D,
E, F) need a sentence rewritten**. Twenty-three sentence rewrites across twenty-eight written
chapters is one afternoon. The reading pass the author feared is a reading pass over twenty-three
sentences, not 171.

---

## Block 1 — the 25 promises naming Chapter 4.4

New targets: **4.4** (domains, the adjoint, symmetric ≠ self-adjoint, extensions) · **4.5** (the
spectrum, the spectral theorem, Hermite completeness, PVM, $\ket x$/$\ket p$, Stone).

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **A** | ch0-2 | 2 | integration by parts, and the boundary term that "makes $-\ii\hbar\partial_x$ Hermitian and thereby makes momentum an observable" | **4.4** — no edit |
| **A** | ch0-6 | 1 | "$\dv{}{x}$ being the standard offender" | **4.4** — no edit |
| **A** | ch4-2 | 3 | "Chapter 4.4 §4 makes the correction"; "Chapter 4.4 §4 will sharpen it to self-adjoint"; "Chapter 4.4 §5 shows that $-\ii\hbar\dv{}{x}$ on the half-line … has no self-adjoint extension" | **4.4 §4**, **4.4 §5** — *no edit; the section list was designed to preserve these* |
| **C** | ch0-5 | 2 | the projection form "survives to infinite dimensions"; "$\sum_k\lambda_kP_k$ becomes $\int\lambda\,\dd P(\lambda)$ … pays this bill in full" | **4.5** (item 7) |
| **C** | ch0-9 | 3 | "that one change is the difficulty Chapter 4.4 has to work to make legitimate" ($\ee^{\ii kx}\notin L^{2}$); "That gap is real. Chapter 4.4 closes it"; "the delta → 4.4 (continuum normalisation $\avg{x\vert y}=\delta(x-y)$)" | **4.5 §6** (item 9) |
| **C** | ch4-2 | 1 | "Stone's theorem, quoted in Chapter 4.4 §9" | **4.5 §9** — *section preserved by design* |
| **C** | ch4-3 | 4 | "$\ket x$ … Chapter 4.4 says what it is instead"; "Chapter 4.4's spectral theorem"; "closes the specific gap Chapter 0.9 named … box normalisation and a limit that always works"; "Chapter 4.4 also proves the Hermite functions complete" | **4.5** (items 9, 2, 9, 5) |
| **D** | ch0-5 | 1 | "Quantum mechanics happens in infinite dimensions. Chapter 4.4 is where the bill comes due." | **"Chapters 4.4 and 4.5"** — the bill is now paid over two chapters and 4.4 item 1 says so |
| **D** | ch4-2 | 4 | "a space of functions that Chapter 4.3 builds and Chapter 4.4 supplies operators for"; "Everything in §§1–3 … is on credit until then. Chapter 4.4 builds the operators on it."; "Chapter 4.3 builds the space and Chapter 4.4 builds the operators on it" (×2) | **"Chapters 4.4 and 4.5"** |
| **D** | ch4-3 | 2 | "This chapter builds the space and Chapter 4.4 builds the operators on it"; "Sections 6 and 7 supply replacements for as much of that as this chapter needs, and Chapter 4.4 handles the rest" | **"Chapters 4.4 and 4.5"** |
| **E** | ch4-2 | 1 | the closing-brick list: "Chapter 4.4 supplies domains, the difference between symmetric and self-adjoint, spectra with no eigenvectors in the space, the spectral theorem in the form that survives, Stone's theorem for §7.3, and the meaning of $\ket x$ and $\ket p$" | **split**: domains and symmetric/self-adjoint → **4.4**; the remaining four → **4.5** |
| **E** | ch4-3 | 1 | "Where this gets spent. Chapter 4.4 takes the space built here and puts operators on it … domains, the difference between symmetric and self-adjoint, spectra with no eigenvectors in the space, and the precise meaning of $\ket x$ and $\ket p$" | **split**: first two → **4.4**; last two → **4.5** |
| | | **25** | | |

**6 of the 25 need no edit.** They are the only six in the whole of Part IV, and they exist because
4.4 kept its number *and* because §4 and §5 were pinned. That is the entire dividend of the
"first piece keeps its number" rule, measured.

---

## Block 2 — the 30 promises naming Chapter 4.5 → **4.6**

The chapter does not split, so this block is a find-and-replace with two exceptions.

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **B** | ch0-1 | 1 | "In Chapter 4.5 the fundamental law of quantum mechanics will turn out to be $\ii\hbar\dv{}{t}\ket\psi=\hat H\ket\psi$" | **4.6** |
| **B** | ch0-2 | 4 | the Gaussian integral, the wave packet's normalisation, $\abs\psi^{2}\propto\ee^{-2ax^{2}}$, and "$b=p/\hbar$" | **4.6** (item 12) |
| **B** | ch0-5 | 4 | $U(t)$ must be unitary; "probability would leak out of the universe"; $\ee^{-\ii\hat Ht/\hbar}$; "$\ee^{\ii A}$ goes to Chapter 4.5" | **4.6** (items 1–4) |
| **B** | ch0-7 | 5 | probability in quantum mechanics; Schrödinger beside diffusion; "the $\ii$ … makes time evolution a rotation"; the continuity equation → probability current; the Laplacian as the kinetic term | **4.6** (items 5, 8, 9) |
| **B** | ch0-8 | 1 | "adding an $\ii$ turns [the wave equation] into the Schrödinger equation" | **4.6** (item 8) |
| **B** | ch0-9 | 3 | the symmetric convention is "the property Chapter 4.5 needs"; moving a wavefunction between representations; "the Fourier basis and Plancherel → … Chapter 4.5" | **4.6** |
| **B** | ch1-1 | 1 | "$\hat H$ generates time evolution through $\ii\hbar\partial_t\ket\psi=\hat H\ket\psi$" | **4.6** |
| **B** | ch1-3 | 2 | evolution generated by $\ee^{-\ii\hat Ht/\hbar}$; "phase space and Liouville go to Chapter 4.5" | **4.6** |
| **B** | ch4-2 | 5 | "Chapter 4.5 takes [the Schrödinger equation] seriously"; "§2 states the sign convention loudly"; "supplies the standard realisation $\hat p=-\ii\hbar\nabla$"; "the machinery … is Chapter 4.5's wave packets"; "turns into a differential equation and solves it" | **4.6**; the second becomes **4.6 §2** — *section preserved by design* |
| **B** | ch4-3 | 2 | "Chapter 4.5's time evolution" needs the limit to exist in the space; $\ee^{-\ii\hat Ht/\hbar}$ maps states to states | **4.6** |
| **C** | ch4-3 | 1 | "The travelling bump … is a particle escaping to infinity, and Chapter 4.5 has to handle exactly this when a state is not bound" | **4.6** — the free packet does handle it. **Add a clause naming 4.7** for genuine scattering states, or the promise reads as only half kept |
| **F** | ch0-4 | 1 | "why the Schrödinger and Heisenberg pictures look like different physics instead of different bases (Chapter 4.5)" | **4.9** — the Heisenberg picture moved to sit beside the Heisenberg equation |
| | | **30** | | |

---

## Block 3 — the 17 promises naming Chapter 4.6

New targets: **4.7** (wells, barriers, tunnelling) · **4.8** (the oscillator and the ladder).
**Fourteen of seventeen are about the oscillator.**

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **C** | ch0-3 | 1 | "Chapter 4.6, the quantum oscillator and its ladder operators" | **4.8** |
| **C** | ch0-5 | 1 | "the Hermite polynomials, which are the quantum harmonic oscillator states of Chapter 4.6" | **4.8** (item 8) |
| **C** | ch0-8 | 7 | $E_n=(n+\half)\hbar\omega$ and $\mathcal A_n=(n+\half)h$; "derives this properly with ladder operators"; "do the single-oscillator calculation once, then attach a copy to every mode"; "the particle content of quantum field theory comes out of the ladder operators"; "the area that Chapter 4.6 will quantise"; "energy eigenstates are the same construction for $\hat H$"; "the harmonic oscillator → Chapter 4.6 (ladder operators, and the $\tfrac12\hbar\omega$ that will not go away)" | **4.8** |
| **C** | ch1-3 | 3 | "⚑ Quoted forward to Chapter 4.6"; "which Chapter 4.6 will derive exactly, with ladder operators"; "all of which Chapter 4.6 will confirm by an exact operator calculation" | **4.8** (items 6, 10) |
| **C** | ch4-2 | 1 | "Chapter 4.6 diagonalises the oscillator" | **4.8** |
| **C** | ch4-3 | 1 | "after which Chapter 4.6 expands in them freely" | **4.8** (item 8) |
| **C** | ch4-2 | 1 | "Nothing in P1 to P5 requires a state to get from one place to another through the intervening places, and Chapter 4.6 computes $\Delta$ for a barrier" | **4.7** (item 9) |
| **D** | ch0-5 | 1 | "the spectral theorem goes to … Chapter 4.6, where solving a system means diagonalising its Hamiltonian" | **"Chapters 4.7 and 4.8"** |
| **D** | ch0-8 | 1 | "In Chapter 4.6 the eigenvectors of $\hat H$ are the stationary states" | **"Chapter 4.6 defines them; 4.7 and 4.8 find them"** — the reassignment note the old plan already required, now spanning three chapters |
| | | **17** | | |

---

## Block 4 — the 41 promises naming Chapter 4.7

New targets: **4.9** (commutators, uncertainty, symmetry) · **4.10** (the classical limit).
**Twenty-nine of forty-one are the uncertainty relation and its neighbours**, which is why 4.9
keeps the lower number.

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **C** | ch0-4 | 2 | "$[\hat x,\hat p]=\ii\hbar$ is the uncertainty principle"; "non-commutativity → Chapter 4.7 (uncertainty)" | **4.9** |
| **C** | ch0-5 | 4 | "this inequality is the uncertainty principle"; "nothing is added in Chapter 4.7 except the physical meaning of the symbols"; "that is the qualitative content of Chapter 4.7"; "Cauchy–Schwarz goes to Chapter 4.7" | **4.9** (item 2) |
| **C** | ch0-9 | 6 | "Chapter 4.7 will add exactly one thing: $p=\hbar k$"; the general relation "as Chapter 0.5's insight box already promised"; "the one Chapter 4.7 needs"; "a single substitution: $p=\hbar k$"; "measurement disturbance … Chapter 4.7 will keep the two apart"; "the bandwidth theorem → Chapter 4.7" | **4.9** (items 1, 2, 3) |
| **C** | ch1-1 | 1 | "Ehrenfest's relation $\dd\avg{\hat{\vv p}}/\dd t=-\avg{\nabla V}$ (Chapter 4.7)" | **4.9** (item 8) |
| **C** | ch1-3 | 4 | "spend one line doing the substitution"; "$p_i\dd q^i$ has the dimensions of action"; "the smallest allowed area is $h/2$"; "the bracket goes to Chapter 4.7 … and becomes the Heisenberg equation" | **4.9** (items 4, 7) |
| **C** | ch4-2 | 9 | Cauchy–Schwarz "cashed as the uncertainty principle"; the two renaming-table rows ending "the qualitative half of Chapter 4.7"; "Chapter 4.7 supplies the quantitative version"; "Chapter 4.7 §3 asks how one knows a set is complete"; "the second form is the one Chapter 4.7 needs"; "Chapter 1.3 §6.4 … named Chapter 4.7 as where it would be taken seriously"; "because Chapters 4.5, 4.6 and 4.8 all need it before Chapter 4.7 arrives" (×2) | **4.9**; the §3 one becomes **4.9 §3** — *section preserved by design*. **The last two also carry a plural list — see Block 9** |
| **C** | ch4-3 | 3 | $L^{2}\not\subset L^{1}$ and "a normalised state can have no mean position" (×2); "the physical reading is worth having now rather than in Chapter 4.7" | **4.9** |
| **C** | ch1-3 | 2 | "⚑ Quoted, with the derivation deferred to Chapter 4.7" (Bohr–Sommerfeld); "Hamilton–Jacobi goes to Chapter 4.7 as the classical limit … the last stop before the wavefunction" | **4.10** (items 6, 2) |
| **C** | ch2-2 | 1 | "classical mechanics is a limit of quantum mechanics (Chapter 4.7)" | **4.10** (item 9) |
| **C** | ch4-1 | 2 | "It is the subject of Chapter 4.7" (the dimensions of action); "a classical orbit enclosing area $\mathcal A$ corresponds to about $\mathcal A/h$ quantum states" | **4.10 §7** (item 7) |
| **C** | ch4-2 | 3 | "Chapter 4.7 §8 proves that it cannot be extended consistently to all of them"; "what Chapter 4.7 §8 supplies … is negative"; "Chapter 4.7's WKB approximation computes the suppression" | **4.10**; the first two become **4.10 §8** — *section preserved by design* |
| **E** | ch1-3 | 1 | "the fundamental brackets … from which the uncertainty principle follows in three lines (Chapter 4.7) and for which $\hat p=-\ii\hbar\,\partial/\partial q$ is the standard realisation" | **split**: uncertainty → **4.9**; the realisation → **4.6** |
| **E** | ch4-2 | 1 | "Chapter 4.7 applies Cauchy–Schwarz … and gets the uncertainty principle with nothing added, then proves that P6 cannot be extended to every observable" | **split**: **4.9** then **4.10** |
| **F** | ch1-3 | 1 | "In Chapter 4.7 the operator conjugate to position is $\hat{\vv p}=-\ii\hbar\nabla$" | **4.6** (item 7) — the realisation is the Schrödinger chapter's |
| **F** | ch1-3 | 1 | "Canonical quantisation, in one line. Chapter 4.7 will take the classical structure you now own … and make the single substitution" | **4.2 §8** — already collected there in the written text. **4.9 must say so in place**, or this sentence gets re-aimed to 4.2; `MATHPLAN-4.md` §"Where I am uncertain" item 2 left this open and it should now be closed in favour of re-aiming, because 4.2 is written and says the right thing |
| | | **41** | | |

---

## Block 5 — the 16 promises naming Chapter 4.8

New targets: **4.11** (the algebra) · **4.12** (spin, orbitals, addition).

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **C** | ch0-5 | 1 | "Chapter 4.8 calls such a list the quantum numbers of the state" | **4.11** — *and note that 4.2 already defined the term; 4.11 spends it* |
| **C** | ch1-3 | 1 | "then show $\{\vv L^{2},L_z\}=0$, and say what both results become in Chapter 4.8" | **4.11** (items 1, 3) |
| **C** | ch1-4 | 1 | "the reason quantum angular momentum is quantised in Chapter 4.8" | **4.11** (item 8) |
| **C** | ch3-9 | 1 | "the $\mathfrak{su}(2)$ of Chapter 4.8 is the algebra §1.1 of this chapter used to state isotropy" | **4.11** |
| **C** | ch4-2 | 3 | "Chapter 0.5's insight box promised the term to Chapter 4.8"; "Chapter 4.8 will describe electron spin with $2\times2$ matrices, and that is finite-dimensional"; "Chapter 4.8 spends §4.3's quantum numbers on angular momentum" | **4.11** (items 10, 11) — the finite-dimension objection is answered in 4.11 item 10 |
| **C** | ch0-5 | 1 | "$\ee^{-\ii\theta\,\hat n\cdot\vec\sigma/2}$ is precisely the operator that rotates a spin-$\tfrac12$ state" | **4.12 §4** (item 7) |
| **C** | ch1-4 | 1 | "Chapter 4.8 turns it into the whole theory of spin" | **4.12** |
| **C** | ch4-2 | 3 | "the electron carries half-integer angular momentum, which is Stern–Gerlach's, quoted in Chapter 4.8"; the postulate table's "E1 … Chapter 4.8"; "Chapter 4.8 measures exactly these with three Stern–Gerlach magnets" | **4.12 §3** (items 4, 5) |
| **D** | ch1-3 | 1 | "derives … that its magnitude takes the values $\sqrt{j(j+1)}\hbar$, that $j$ can be a half-integer, and hence that spin exists" | **"Chapters 4.11 and 4.12"** — the first two clauses are 4.11's theorem, the third is 4.12's measurement |
| **D** | ch1-4 | 2 | "derives the entire quantum theory of angular momentum from nothing but that algebra, including half-integer spin, which has no classical counterpart"; "Chapter 4.8 finds §7's bracket algebra again with commutators, which is where spin comes from" | **"Chapters 4.11 and 4.12"** — and the phrase **"from nothing but that algebra"** is what licenses 4.11 carrying zero flags, so it must survive the edit verbatim |
| **F** | ch0-5 | 1 | "why 'lifting a degeneracy' — with a magnetic field, say — is such a common experimental move. Chapter 4.8." | **4.15 §3** — degenerate perturbation theory, with the Zeeman effect worked as 4.15 item 6. **This promise is mis-aimed in the current plan too: 0.5 names 4.8 and old 4.10 item 5 collects it. See Finding 3** |
| | | **16** | | |

---

## Block 6 — the 7 promises naming Chapter 4.9

New targets: **4.13** (the atom) · **4.14** (the degeneracy and $SO(4)$).

| Cat | Where | n | The promise | New target |
|---|---|---|---|---|
| **C** | ch0-3 | 1 | "in hydrogen the electron's typical speed is $v\approx\alpha c$ (Chapter 4.9)" | **4.13** (item 9) |
| **C** | ch0-4 | 1 | "the same eigenvalue machinery solves a coupled-oscillator problem in Chapter 0.8 and a hydrogen atom in Chapter 4.9" | **4.13** (item 2) |
| **C** | ch4-1 | 2 | "Chapter 4.9 derives it, including the value of $R$"; "Chapter 4.9 supplying the two integers" | **4.13** (item 8) |
| **C** | ch4-2 | 2 | "exactly what Chapter 4.9's degeneracies will need"; "the reason Chapter 4.9's hydrogen states need three labels" | **4.13** (item 12) |
| **C** | ch1-4 | 1 | "⚑ And the payoff arrives in Chapter 4.9." (the Laplace–Runge–Lenz vector) | **4.14** (item 10) — *and the flag is struck in the same commit* |
| | | **7** | | |

---

## Block 7 — the 10 promises naming Chapter 4.10

New targets: **4.15** (perturbation theory) · **4.16** (fine structure) · **4.17** (transitions).

| Cat | Where | n | The promise | New target |
|---|---|---|---|---|
| **C** | ch4-3 | 1 | "Chapter 4.10's perturbation series, whose first correction is an infinite sum over the unperturbed basis" | **4.15** (item 1) |
| **C** | ch2-5 | 1 | "one of the three contributions to the fine structure … Chapter 4.10 computes the full splitting" | **4.16** (items 2–3) |
| **C** | ch1-3 | 1 | "the modern statement is Chapter 4.10's adiabatic theorem" | **4.17 §8** (item 9) |
| **C** | ch4-1 | 1 | "$B_{12}=B_{21}$ returns in Chapter 4.10 as the equality of two matrix elements that Hermiticity makes automatic" | **4.17** (item 7) — **which the current plan has no build item for. See Finding 4** |
| **C** | ch4-2 | 6 | "Chapter 4.10 §8 handles that case … a time-ordered series"; "the seed of the transition-rate formula Chapter 4.10 derives"; "in a frame rotating with the drive the problem becomes … with $\delta=0$"; "that reduction is Chapter 4.10's and is not derived here"; "every detuned curve leaves the origin along the same parabola … is what Chapter 4.10's transition rate is built on" (×2) | **4.17** (items 1, 4, 5). The first becomes **4.17 §3** — **the only §-number in Part IV that changes**. Two of the six name the rotating-frame reduction, **which the current plan has no build item for. See Finding 5** |
| | | **10** | | |

---

## Block 8 — the 25 promises naming Chapter 4.11

New targets: **4.18** (identical particles) · **4.19** (density matrices, entanglement) · **4.20**
(Bell, decoherence, what is settled).

| Cat | Where | n | The promise (grouped) | New target |
|---|---|---|---|---|
| **C** | ch4-1 | 4 | "no statistics of light in this book until Chapter 4.11"; "used again in Chapter 4.11 for occupation numbers"; "Chapter 4.11 §5 derives [the Planck law] a second time"; "Chapter 4.11 §5 does it again from the other end and closes that loop" | **4.18 §5** (items 6, 7) — *section preserved by design* |
| **C** | ch4-2 | 3 | "the eighth is the symmetrisation of identical-particle states, which arrives in Chapter 4.11"; the postulate table's "P8 … Chapter 4.11"; "that restriction is P8 … stated in Chapter 4.11 §3" | **4.18 §3** (item 3) — *section preserved by design* |
| **C** | ch0-9 | 1 | "probability, variance, the CLT → Chapter 4.11 (density matrices and measurement statistics)" | **4.19** (item 2) |
| **C** | ch4-2 | 3 | "the counting is … the whole of what Chapter 4.11 needs from this chapter"; "that is why Chapter 4.11 has to build a different object, the density operator"; "(states inside it exist and are mixtures, which is Chapter 4.11's density operator)" | **4.19** (items 1, 4) |
| **C** | ch0-8 | 1 | "Chapter 4.11 is about exactly where that seam is" (where the randomness enters) | **4.20 §9** |
| **C** | ch4-2 | 10 | "Chapter 4.11 returns to what it costs"; "Chapter 4.11 §9 puts the whole list back on one page" ; "Chapter 4.11 §9 returns to what that costs"; "the separation is what lets Chapter 4.11 say precisely which of the two decoherence addresses"; "Chapter 4.11 §9 needs the separation"; "runs into Chapter 4.11's inequalities"; "Chapter 4.11 §9 states which of these decoherence answers"; "that is Chapter 4.11's subject, and it is not available by adjusting $\hat H$"; "what Chapter 4.11 measures with Bell's inequality"; "Chapter 4.11 returns to P3, P4 and P7 together" | **4.20**; the four naming §9 become **4.20 §9** — *section preserved by design, which is why 4.20 has nine numbered sections* |
| **E** | ch4-2 | 2 | "it is built in Chapter 4.11, where the distinction is what decoherence is about"; "Chapter 4.11 builds the density operator to answer 'what is the first system's state' and then measures the inequality" | **split**: built in **4.19**, spent in **4.20** |
| **D** | ch4-2 | 1 | "which one nature uses is a physical question, and its answer is the source of every effect in Chapter 4.11" | **"Chapters 4.18 to 4.20"** |
| | | **25** | | |

---

## Block 9 — what `debts.py` does not see, and which must be remapped in the same commit

The 171 are the sentences matching `Chapter 4\.N`. They are not the whole surface.

| Where | Count | What | Why `debts.py` misses it |
|---|---|---|---|
| `src/ch*.html` | **15 mentions in 8 sentences** | *"Chapters 4.5, 4.6 and 4.8 all need it"* (ch4-2, ×2); *"Chapters 4.8 and 4.9 spend it"* (ch4-2); *"Chapters 4.5 to 4.7"* (ch4-3); *"Chapters 4.7 and 4.8"* (ch0-5); *"Chapters 0.8, 4.6, 5.3, 7.4"* (ch0-1, ch0-3); *"Chapters 0.9, 4.6 and 5.3"* (ch0-8) | The regex is `Chapter 4\.N`; the plural **"Chapters"** does not match. **These are invisible to the census as well as the per-chapter report** |
| `src/_ledger.html` | **84** | every "Spent in" cell naming 4.4–4.11 — e.g. *"4.5 ($\ee^{-\ii\hat Ht/\hbar}$)"*, *"4.7 — Cauchy–Schwarz becomes the Heisenberg…"*, *"4.11 (density matrices)"*. By target: 4.4 ×17, 4.5 ×18, 4.6 ×9, 4.7 ×15, 4.8 ×7, 4.9 ×5, 4.10 ×4, 4.11 ×9 | The ledger writes bare numbers, never "Chapter N.M", and `debts.py` only globs `src/ch*.html` |
| `GAPS.md`, `STATUS.md` | ~50 | the registers | Not globbed |
| `build.py` `PARTS` | 8 rows → 17 | the authoritative curriculum: index hub, navigation, progress count | — |
| `MATHPLAN-4.md`, `PLAN-FORWARD.md` §§3.1, 5.3, 11 | — | the plans themselves | — |

**Total remapping surface: 171 + 15 + 84 + ~50 ≈ 320 references**, of which the 84 ledger cells are
the ones most likely to be forgotten, because nothing in the toolchain looks at them.

**Recommendation, and it is cheap:** before the remap, widen `debts.py`'s pattern to
`Chapters? ((?:\d\.\d+)(?:\s*(?:,|and|to)\s*\d\.\d+)*)` and add `src/_*.html` to its glob. That is a
two-line change and it turns a 320-reference hand search into a script. **`xrefcheck.py` should
then be extended to fail the build on any reference to a chapter number not in `build.py`'s `PARTS`**
— which would have caught this class of error before it was ever a reading pass.

---

# Deliverable 3 · Specification for the Part IV Bird's Eye View

*A standalone page, `src/_birdseye-4.html`, sitting between the Part III end matter and Chapter 4.1
on the landing page. Not a chapter: no number, no entry in `build.py`'s `PARTS`, no effect on any
promise. Roughly 1,200–1,600 words — shorter than the shortest chapter in the book by a factor of
four, and it must stay that way.*

**What it is for.** The reader is about to meet twenty chapters. Schwichtenberg's device works
because it lets you hold the destination in your head while the machinery goes past; the failure it
prevents is the one this reader named — "running around" — which is not caused by any single chapter
being hard but by not knowing which of the hard things are the point.

**What it must cover, in this order:**

1. **The one sentence.** *Quantum mechanics replaces "the system is in state $s$" with "the system
   is a direction in a space of possibilities, and every question you can ask is a projection onto
   some other direction."* Everything else in the part is that sentence made precise or made
   computable.
2. **Why a space at all** — because four measurements in the 1900s could not be fitted by any theory
   in which a system has one value at a time, and because a three-line trace argument shows the
   space must be infinite-dimensional before any physics is done. Name 4.1 and 4.2. Two paragraphs.
3. **The four things that are assumed** — states are rays; observables are self-adjoint operators;
   the Born rule; the state update — and the count: **eight postulates and one measurement, and the
   reader will be told when each arrives and when each is spent.** Say that P3 is the one nobody has
   derived and that the part ends by saying so again. This is the paragraph that buys the most
   trust, and it is the one most easily cut for length. Do not cut it.
4. **What gets computed with it** — one atom's spectrum from an algebra, one oscillator's from a
   ladder, one correlation that no classical model can produce. Name the numbers: $-13.6$ eV,
   $(n+\half)\hbar\omega$, $2\sqrt2$.
5. **The map of the twenty chapters as four movements**, one sentence each: *the failures*
   (4.1–4.2), *the space and the operators on it* (4.3–4.5), *solving things* (4.6–4.17), *two
   things instead of one* (4.18–4.20). A reader who knows there are four movements will not feel
   lost inside the third.
6. **The recurring motif, named once**: everything in this part falls apart into independent pieces
   — energy eigenstates, Fourier modes, angular-momentum multiplets, occupation numbers. Four names
   for one trick. `MATHPLAN-4.md` §0 already says this is Part IV's motif; the Bird's Eye View is
   where the reader should meet it first.

**The two or three equations that earn a place — exactly three, and no others:**

| Equation | Why it, and not something else |
|---|---|
| $\ii\hbar\,\dv{}{t}\ket\psi=\hat H\ket\psi$ | The law. Every chapter from 4.6 on is this equation solved, approximated, or generalised. The reader has already seen it in 0.1 and 0.5 and will recognise it, which is the point |
| $\Pr(\lambda_k)=\norm{\hat P_k\ket\psi}^{2}$ | The rule connecting the mathematics to a number a machine reads. It is also the one thing in the part that is not derived, so it earns its place twice |
| $[\hat x,\hat p]=\ii\hbar$ | The single line that forces the infinite-dimensional space, the uncertainty relation, the ladder, the angular-momentum spectrum and the classical limit's failure. If only two equations survive an edit, this is not the one to cut |

**What it must not do:**

- **No derivation. Not one line of algebra with a "so" in front of it.** If a step is being justified,
  it belongs in a chapter.
- **No new notation.** Dirac brackets may appear because 0.5 built them; $\hat P_k$, $\hat H$ and
  $\hbar$ may appear because 0.5, 1.3 and 4.1 built them. Nothing else. No $L^{2}$, no
  $\mathfrak{su}(2)$, no $\hat\rho$, no $\ket{j,m_j}$.
- **No ⚑, and no `GAPS.md` entry.** Nothing on this page is used by anything, so nothing on it can be
  an unmarked import. Say in one line that the part's flags are counted in the chapters and totalled
  at the end.
- **No interpretations.** Not one sentence about what the wavefunction "really is". 4.20 §9 is where
  that is handled, honestly and briefly, and the Bird's Eye View may point at it and must not
  anticipate it.
- **No promises.** This page must not add a single forward reference of the kind `debts.py` counts.
  It names chapters as a map, in the form "Chapters 4.3 to 4.5 build the space", and never in the
  form "Chapter 4.7 will prove". A page written to relieve the promise-tracking burden must not add
  to it.
- **It is not a summary of the part and must not be readable as one.** A reader who reads only this
  page should be able to say what quantum mechanics claims and should *not* be able to say why any
  of it is true. That asymmetry is the whole design.

**Where it is linked from:** the landing page, before 4.1; and one line in 4.1's opening `where`
callout — *"if you would rather see the whole thing first, the bird's eye view is one page and has
no algebra in it."* Nowhere else, and no chapter may cite it as a source.

**If it works, do the same for Parts V–VII**, and consider one retrofitted for Part 0, which is the
other place the reader has the least idea where he is going.

---

# What I believe is wrong in the current plan

Recorded per the standing rule that plan errors are caught in plans. Eight have been caught this way
across the build; these are five more, plus two judgement calls.

**1 · The "first piece keeps its number" rule does not do what the brief says it does — it saves
6 promises, not 148.** The brief says *"a promise naming 4.7 still lands on a chapter about the
right subject unless the specific material it names moved into the second piece — and those are the
only ones needing re-aiming."* That is true only for the **first** chapter that splits. A shift
renumbers every chapter after it, split or not, so a promise naming old 4.5 lands on new 4.5, which
is the second half of old 4.4 — an operator-theory chapter — and is not merely inexact but wrong.
Measured: **165 of 171 need an edit; only the 6 in Block 1 category A do not.** The rule is still
the right rule, because it puts the six where they are cheapest to keep and it makes the other 165 a
decided table rather than an open question — but the number in the brief is off by a factor of about
eight and the schedule should be set from the real one. **The corollary is useful: the renumbering
cost is paid in full at the first split, so there is no reason to split conservatively.**

**2 · Nothing in the toolchain sees the ledger, and the ledger holds 84 references to 4.4–4.11.**
`debts.py` globs `src/ch*.html` and matches `Chapter 4\.N`. `src/_ledger.html` writes bare numbers
("4.11 (density matrices)") and is not globbed; `_throughline.html`, `GAPS.md` and `STATUS.md` are
not globbed either. It also misses the plural form — *"Chapters 4.5, 4.6 and 4.8"* — which occurs
15 times in 8 sentences of written text and is invisible to both the report and the census.
**The census figure of 242 for Part IV is therefore an undercount**, and any renumbering driven from
it will leave the ledger stale. Two-line fix in `debts.py`; a check in `xrefcheck.py` that fails the
build on a chapter number absent from `build.py`'s `PARTS` would make the class of error impossible.

**3 · A promise is already mis-aimed inside the current plan.** Chapter 0.5 writes *"why 'lifting a
degeneracy' — with a magnetic field, say — is such a common experimental move. Chapter 4.8."*
`MATHPLAN-4.md`'s 4.10 item 5 says it collects that promise. Both cannot be right: 4.8 is angular
momentum and 4.10 is perturbation theory, and the sentence is about degenerate perturbation theory.
This would have shipped as a chapter naming a promise it does not carry. **Resolution: it belongs to
the degenerate-perturbation chapter (new 4.15), and 0.5's sentence must be re-aimed there** — which
is why 4.15 gets a new build item working the Zeeman effect explicitly, so the promise lands on
something visible.

**4 · Chapter 4.1 makes a promise to 4.10 that the current plan has no build item for.** 4.1's
closing brick says *"$B_{12}=B_{21}$ returns in Chapter 4.10 as the equality of two matrix elements
that Hermiticity makes automatic."* None of old 4.10's sixteen build items does this. It is two
lines from Fermi's golden rule and it is a genuinely good moment — a thermodynamic argument from
4.1 recovered from P2 — so the omission is a loss, not just a bookkeeping error. **Placed as 4.17
item 7.**

**5 · Chapter 4.2 promises the rotating-frame reduction to 4.10 twice, and the current plan has no
build item for that either.** 4.2 writes *"Chapter 4.10 shows that in a frame rotating with the
drive the problem becomes [the static two-state matrix] with $\delta=0$ and $\Delta=\hbar\Omega_R/2$"*
and, separately, *"That reduction is Chapter 4.10's and is not derived here."* Old 4.10's interactive
assumes a driven two-level system exists; no item derives it. This is the sharper of the two
omissions, because 4.2 explicitly declined to derive something on the strength of a later chapter
doing it. **Placed as 4.17 item 4, with the counter-rotating term's residue computed so the
approximation is scored rather than asserted.**

**6 · The uncertainty chapter has an unnamed, unmarked import.** 0.9 promises that *"measurement
disturbance is a real and separate phenomenon with its own theorems, and Chapter 4.7 will keep the
two apart."* Old 4.7 item 3 keeps them apart but names no theorem and carries no ⚑ — so either the
promise's "with its own theorems" is not kept, or theorems are gestured at without a mark, which is
exactly the failure `CONVENTIONS.md`'s ⚑ contract exists to prevent and which the Part 0 review
found eight times. **Fixed by naming the error–disturbance relations and flagging them (4.9 item 3).
This is the only flag added anywhere in this re-plan, and it is paid for by 4.6 no longer counting
the Stone converse it explicitly cites rather than re-flags.**

**7 · Two judgement calls I am recording rather than deciding.**

- **The order of new 4.7 and 4.8 (wells before oscillator) is not forced.** I chose wells first
  because it spends 4.4's $U(2)$ result while it is fresh, gives a concrete win immediately after
  the Schrödinger equation, and puts the oscillator's ladder three chapters from the angular-momentum
  ladder rather than five. The opposite order is defensible — the oscillator needs no boundary
  conditions at all — and **it makes no difference to the promise triage**, because both numbers
  differ from 4.6 either way. If the author's instinct is oscillator-first, take it; only the two
  chapters' §-lists and item 1 of each change.
- **4.14 at four objects is the thinnest chapter in the part.** It is four objects and roughly
  10,000 words, which is the book's own words-per-object rate and the *opposite* of the failure this
  re-plan exists to fix — but it will read as a short chapter about one calculation, and a reader
  who wanted hydrogen finished in one sitting may feel it as an epilogue rather than a chapter. The
  alternative is a ten-object 4.13, which is what the brief forbids. **I would keep the split and
  make 4.14's opening say plainly that it exists to answer one question 4.13 could not.**

**8 · One thing in `MATHPLAN-4.md` that this re-plan does *not* fix, and should be decided
separately.** Its §"Where I am uncertain" item 1 leaves open whether a postulate box carries a ⚑ as
well. That decision drives 10 of the part's 51 flags and it is now 10 of 51 across twenty chapters
rather than eleven, which makes 4.2 look even more like an outlier on any per-chapter flag chart.
**The decision should be made explicitly before F5** — the re-plan assumes the existing answer (yes,
a postulate carries a flag) and the ⚑ budget above is computed on it.

---

*Written against `MATHPLAN-4.md` (2026-08-25), `src/_ledger.html`, `PLAN-FORWARD.md` §§3.1, 5, 11,
`CONVENTIONS.md`, `src/ch4-3.html`, and `python3 debts.py 4.4` … `4.11` run 2026-08-26. Nothing on
disk was modified.*
