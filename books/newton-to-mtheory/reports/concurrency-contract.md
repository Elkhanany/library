# Writing chapters concurrently: what you may assume about a chapter that does not exist yet

Chapters 4.5, 4.6 and 4.7 are being written at the same time, by three agents who cannot see each
other's work. Each depends on the one before it. This document is what makes that safe, and it is
binding on all three.

## The rule

**You may rely on a concurrent chapter's *results*, at the section numbers `MATHPLAN-4.md` fixes.
You may not quote its prose, name its worked examples, or describe how it argues.**

`MATHPLAN-4.md` fixes, for every chapter, the section list and the numbered build items. Those are
contracts, not sketches. A result the plan assigns to 4.5 §7 will be in 4.5 §7. What the plan does
not fix — the wording, the order of paragraphs inside a section, which example is Worked example 2,
the exact phrasing of a plain-terms box — does not exist yet and cannot be referred to.

So this is allowed:

> The spectral theorem of Chapter 4.5 §3 says an observable is unitarily equivalent to multiplication
> by a real function, and that is what we use here.

And this is not:

> As Chapter 4.5 puts it, "the spectrum is what the eigenvalues become when they run out".

The second sentence invents a quotation. It will not survive, and worse, it will read as though it
did — which is exactly how a book acquires a second voice.

## The one exception, and it runs backwards

You may quote **any chapter already written** (0.1 through 4.4) as freely as usual, verbatim, because
those files exist and you can read them. The concurrency restriction applies only forward, to 4.5,
4.6 and 4.7 in whichever of them is not yours.

## What each chapter may assume

**Everyone may assume Chapter 4.4**, which is written: an operator is a formula together with a
domain; the domain is forced by Hellinger–Toeplitz; symmetric is not self-adjoint; and 4.4 §5 works
$\hat p$ on three intervals by hand. Read `src/ch4-4.html`.

### If you are writing 4.5

Nothing upstream is concurrent. You are the foundation of this batch and everything below leans on
you. Two consequences:

- **Hold the section numbers exactly as `MATHPLAN-4.md` fixes them.** 4.6 is being written against
  them right now, and §9 in particular — Stone's theorem — is named by a written sentence in 4.2 and
  was pinned through the whole Part IV renumbering.
- Your §11 closing brick should say what 4.6 takes from you, in the plan's terms.

### If you are writing 4.6

You may assume from **4.5**, and nothing else about it:

| result | where the plan puts it |
|---|---|
| the spectrum, and that an observable can have no eigenvectors in the space | 4.5 §2 |
| the spectral theorem in multiplication-operator form ⚑ | 4.5 §3 |
| the projection-valued measure, $\hat A=\int\lambda\,\dd P(\lambda)$ | 4.5 §6 |
| box normalisation, and the meaning of $\ket x$ and $\ket p$ | 4.5 §7 |
| **Stone's theorem**, forward direction built, converse ⚑ | **4.5 §9** |

Stone's theorem is the hinge of your chapter: it is what turns "evolution is a strongly continuous
one-parameter unitary group" into "there is a self-adjoint $\hat H$ with $\hat U=\ee^{-\ii\hat Ht/\hbar}$".
Cite it at §9 and state it in your own words.

### If you are writing 4.7

You may assume from **4.6**, and nothing else about it:

| result | where the plan puts it |
|---|---|
| the Schrödinger equation $\ii\hbar\,\partial_t\ket\psi=\hat H\ket\psi$ | 4.6 §3 |
| $\hat H=\hat p^{2}/2m+V(\hat x)$, flagged as an identification | 4.6 §4 |
| $\hat p=-\ii\hbar\nabla$ in the position representation | 4.6 §5 |
| the probability current and $\partial_t\rho+\nabla\cdot\vv J=0$ | 4.6 §8 |
| stationary states, and the time-independent equation | 4.6 §9 |

You may also assume from **4.5** §3 the spectral theorem, in the same terms 4.6 gets it.

Your $T+R=1$ argument leans on 4.6 §8's current. Derive the current's *form* for your own scattering
states rather than importing a formula you cannot see.

## When your chapter refers forward

Chapters after yours are not being written now and are pure plan. Refer to them exactly as the book
already does — by chapter and, where `MATHPLAN-4.md` fixes one, by section — and never in a way that
promises wording. `python3 debts.py <N.M>` on your own chapter shows you the form these take.

## What happens afterwards

A reconciliation pass reads the three chapters together and fixes the seams: a result cited at a
section number that moved, a term defined twice, a hand-off that does not meet. That pass exists, so
you do not need to hedge. Write as though the chapter beside you will deliver exactly what the plan
says, because it is being held to the same contract you are.
