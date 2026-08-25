# Part IV — Quantum Mechanics: derivation plan

*Eleven chapters, three of them dedicated mathematics. This is the part the whole of Part 0 was a
down-payment on: `GAPS.md` G1 records seven separate promises, made in writing, that fall due here,
and Chapter 0.5 told the reader in its own words that "Chapter 4.2 becomes a translation exercise:
a table of renamings, not a new subject". That sentence is either honoured or the design of the
book fails retrospectively.*

*Everything below is **derived in the text**. Items marked ⚑ are the only permitted exceptions and
must be flagged in place. `MATHPLAN-3.md` §0's eight pacing rules are **binding here unchanged** and
are not restated; `PLAN-FORWARD.md` §2's items 9–11 are folded in below as items 9–11, and items
12–14 are new for this part.*

---

## 0 · Pacing

`MATHPLAN-3.md` §0 items 1–8 stand verbatim: announce the destination; one manipulation per line;
name the technique as you use it; say what was done after any non-obvious line; spell out index and
operator gymnastics; grind boxes hold length, never logic; recap after ten lines; prefer two
derivations of the important results. Read them before writing anything in this part.

Three additions carried in from `PLAN-FORWARD.md` §2, binding from here to the end of the book:

9. **Every new physical postulate is announced as a postulate, in its own box, before it is used.**
   Part III never had to do this — general relativity was cornered rather than posited. Quantum
   mechanics cannot be. The Born rule is not derivable and the book's credibility depends on saying
   so at the moment it enters rather than letting it seep in. §0.1 below is the complete list of
   postulates this part introduces and the section that announces each.

10. **A ⚑ from here on carries its hypotheses.** "Quoted" is not enough by itself. The adiabatic
    theorem without its gap condition, the spectral theorem without "self-adjoint, not merely
    symmetric", Gleason without "dimension at least three" — in each case the hypothesis *is* the
    content, and this part contains the two chapters (4.4, 4.10) where dropping one silently would
    do the most damage.

11. **Numerical confirmation, in the text, at least once per chapter.** Parts IV has more of this
    available than Part III, not less: a numerically integrated Schrödinger equation, a numerically
    diagonalised Hamiltonian, a golden rule checked against an exact two-level integration, a CHSH
    value read off a slider. §0.3 below assigns one to each chapter.

Three more, specific to this part:

12. **4.2 is a translation, and must read as one.** The chapter's spine is a two-column table of
    renamings with 0.5's theorem on the left and the physical statement on the right, and its only
    new content is the postulates. If a writing agent finds themselves re-proving that Hermitian
    operators have real eigenvalues, they have misread the brief. `PLAN-FORWARD.md` §5.2 makes the
    same point about the uncertainty relation in 4.7: **spend it, do not re-derive it.**

13. **Say out loud, each time, whether a step is a derivation or an identification.** "$p=\hbar k$"
    is not algebra; it is a physical identification with an experiment behind it. "$\hat H =
    \hat p^2/2m + V$" is not forced by anything so far; it is a choice that 4.7 §8 will show cannot
    be made consistently for every classical observable. The reader has been trained for
    twenty-eight chapters to ask which is which, and this is the part where the answer changes
    from sentence to sentence.

14. **Announce the two-chapter shape of 4.3 + 4.4 in advance, in 4.2's closing brick.** 0.4 built
    the space and 0.5 built the operators on it; 4.3 builds the space and 4.4 builds the operators
    on it. A reader who is told that the shape repeats will recognise it, and the recognition is
    worth more than the four pages it saves.

Every chapter is written **with its "In plain terms" boxes in place**, by the same author, in one
pass — `PLAIN-TERMS-PLAN.md` §7. Every box must be placeable on §2's table; Part IV's row reads
*"What state is this in stops having a single answer. The state is a direction in an abstract
space, measurement is a projection, and the mathematics was already built in Part 0."* The recurring
motif this part owns is **"falling apart into independent pieces"** — energy eigenstates, Fourier
modes, angular-momentum multiplets, occupation numbers are the same trick four more times, and the
boxes should say so in those words.

### 0.1 · The postulate ledger — every postulate this part introduces

Binding. Each is announced in a box, in the section named, **before** its first use; each carries a
⚑ as well as its box (see Conventions); each is repeated on the ledger in 4.11 §9 with an honest
statement of what it does and does not settle.

| P | Postulate | Announced | First used | Derivable? |
|---|---|---|---|---|
| **P1** | A pure state is a unit vector, defined up to phase, in a complex Hilbert space | 4.2 §3 | 4.2 §3 | No. Rays, not vectors: the global phase is unobservable and the *relative* phase is everything |
| **P2** | An observable is a **self-adjoint** operator on that space | 4.2 §4 | 4.2 §4 | No. Stated as *Hermitian* in 4.2 and **corrected to self-adjoint in 4.4 §4**, with the correction flagged in both places |
| **P3** | **The Born rule.** The probability of outcome $\lambda_k$ in state $\ket\psi$ is $\norm{P_k\ket\psi}^{2}$ | 4.2 §5 | 4.2 §5 | **No, and this is the one that matters.** `GAPS.md` G13 lists it as permanently open. Gleason is ⚑'d in the same box with its hypotheses, and is *not* presented as a derivation |
| **P4** | **The state update.** After an outcome, the state is $P_k\ket\psi/\norm{P_k\ket\psi}$ | 4.2 §6 | 4.2 §6 | No — and it is a *separate* assumption from P3, which is why it gets its own line. Say so; most texts merge them |
| **P5** | Time evolution is generated by a self-adjoint operator, and that operator is the energy | 4.2 §7 (stated), 4.5 §2 (half derived) | 4.5 | **Half.** That evolution is $\ee^{-\ii\hat Ht/\hbar}$ for *some* self-adjoint $\hat H$ follows from unitarity plus Stone (4.4 §9). That $\hat H$ is the energy is the postulate |
| **P6** | **Canonical quantisation:** $[\hat x_i,\hat p_j]=\ii\hbar\delta_{ij}$, $[\hat x_i,\hat x_j]=[\hat p_i,\hat p_j]=0$ | 4.2 §8 | 4.5, 4.6, 4.8 | No. 4.7 §8 then proves the sharper statement: the correspondence $\{\,,\}\to\frac{1}{\ii\hbar}[\,,]$ **cannot** be extended to all observables |
| **P7** | A composite system's space is the tensor product of the parts' | 4.2 §9 | 4.11 | No |
| **P8** | **Symmetrisation.** States of identical particles are totally symmetric or totally antisymmetric | 4.11 §3 | 4.11 §4 | No, not here. 5.5 derives *which*, from locality and Lorentz invariance; 4.11 must say that plainly and name it |
| **E1** | *Experimental input, not a postulate:* the electron carries $j=\half$ | 4.8 §6 | 4.8 §7 | No — a measurement (Stern–Gerlach). The *possibility* of $j=\half$ is derived in 4.8 §3 from the algebra alone; that nature uses it is data |

**Eight postulates and one measurement is the complete bill, and the reader should be told the
number.** Of the eight, P1 and P2 together are what 0.5 §6.5 called *"one postulate, not four"*;
P3 and P4 are what 0.5 did not have to state at all; and P5–P8 are dynamics, quantisation,
composition and identity, one each. Say the count out loud in 4.2 §1 and again in 4.11 §9, and each
time say which of Part 0's *theorems* it is not. That contrast is the payoff for nine chapters of
mathematics, and it is checkable.

### 0.2 · What Part IV owes — the debt map

`python3 debts.py 4` returns **242 sentences** in the written text that name a Part IV chapter.
**Regenerate this table after every batch.** It was accurate at 119 when written and went stale the moment
4.1, 4.2 and 4.3 were written, because those chapters cite each other and everything before them. Every row
below moved, and subtracting the three new chapters' contributions reproduces the original numbers exactly.
Every one is a requirement. Counts, and the collector:

| Ch | Debts | The heaviest creditors |
|---|---|---|
| 4.1 | 23 | 4.2 (12), 4.3 (6), 2.5 (5) |
| 4.2 | 33 | 0.5 (12), 4.3 (7), 0.4 (6), 4.1 (4) |
| 4.3 | 15 | 4.2 (6), 0.2 (2), 0.5 (2), 0.9 (2) |
| 4.4 | 25 | 4.2 (9), 4.3 (7), 0.5 (3), 0.9 (3) |
| 4.5 | 30 | 0.7 (5), 4.2 (5), 0.2 (4), 0.5 (4) |
| 4.6 | 17 | 0.8 (8), 1.3 (3), 0.5 (2), 4.2 (2) |
| 4.7 | 41 | 4.2 (13), 1.3 (9), 0.9 (6), 0.5 (4) |
| 4.8 | 16 | 4.2 (6), 1.4 (4), 0.5 (3), 1.3 (2) |
| 4.9 | 7 | 4.1 (2), 4.2 (2), 0.3 (1), 0.4 (1) |
| 4.10 | 10 | 4.2 (6), 1.3 (1), 2.5 (1), 4.1 (1) |
| 4.11 | 25 | 4.2 (19), 4.1 (4), 0.8 (1), 0.9 (1) |

**Run `python3 debts.py 4.N` and paste the output into the writing brief for chapter N.** It is the
chapter's requirements list, not background reading.

`GAPS.md` G1's seven promises split **three to 4.3** (the Lebesgue integral rebuilt "from scratch";
dominated convergence "proved properly"; the Fourier-completeness ⚑ of 0.9 §1.3) and **four to 4.4**
(the projection form "survives to infinite dimensions"; continuous spectra and projection-valued
measures — *"Chapter 4.4 pays this bill in full"*; unbounded operators, *"$\dv{}{x}$ being the
standard offender"*; and $\ee^{\ii kx}\notin L^{2}$ — *"that gap is real. Chapter 4.4 closes it"*).

**Note the wording of that last one.** 0.9 §5.3 says 4.4 *closes* the gap, and `GAPS.md` G11 says
4.4 makes only a partial payment with 5.4 completing it. Both can be true and the plan resolves it
explicitly: **4.4 closes the specific gap 0.9 named** — why every manipulation with $\ket x$ and
$\ket k$ is legitimate, via box normalisation and a stated limit that always works — and 5.4 builds
the general theory of distributions. 4.4 must not use the word "closes" about anything wider.

### 0.3 · The numerical confirmation each chapter carries

Per pacing item 11. One per chapter, in the running text, with the arithmetic visible:

| Ch | The confirmation |
|---|---|
| 4.1 | The Planck curve's peak at $\nu_{\max}/T=5.8789\times10^{10}\ \mathrm{Hz\,K^{-1}}$ and its integral giving $\sigma=5.6704\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}$, both from the same formula |
| 4.2 | Probabilities summing to $1$ to machine precision through a full Rabi cycle |
| 4.3 | $\norm{f-S_N}_2\to0$ like $N^{-1/2}$ for the square wave **while** the pointwise overshoot stays at $8.95\%$ of the jump — the two convergences visibly different |
| 4.4 | Parseval in the Hermite basis: $\sum_{n<20}\abs{c_n}^{2}=1.00000000$ for a test function |
| 4.5 | A split-operator integration conserving the norm to $4\times10^{-13}$ while $\avg{x}(t)$ tracks the classical trajectory to $2\times10^{-6}$ |
| 4.6 | The numerically diagonalised oscillator giving levels equally spaced to $10^{-10}$ |
| 4.7 | WKB against exact levels: **exact** for the oscillator, $18\%$ at $n=0$ and $0.17\%$ at $n=4$ for $V=x^{4}/4$ |
| 4.8 | $\ee^{-\ii\theta J_z}$ returning $-\hat I$ at $360^{\circ}$ and $+\hat I$ at $720^{\circ}$ for $j=\half$, against $+\hat I$ at $360^{\circ}$ for $j=1$ |
| 4.9 | The radial equation integrated numerically for $\ell=0,1,2,3$, giving $-\tfrac12 n^{-2}$ hartree with $\ell\le n-1$ falling out |
| 4.10 | The two-level system integrated exactly against first-order theory: ratio $0.970$ at $Vt/2=0.3$, which is $\sin^{2}(0.3)/0.3^{2}$ |
| 4.11 | CHSH read off the interactive: $2.8284$ at $(0^\circ,90^\circ,45^\circ,135^\circ)$, against $10^{5}$ hidden-variable runs that never exceed $2$ |

---

## Register

`CONVENTIONS.md`'s closing section, **Register, from Part IV onward**, is binding on every chapter in
this part and was written for it. Read it before writing a line. In short: the mathematics does not
soften, but the motive for each step goes in front of the step rather than behind it, connectives
replace clipped declaratives, the reader's daily quantitative fluency may be drawn on in the main
text where the mathematics is genuinely identical, and a hard step gets named as hard.

---

## Conventions (binding, extending `CONVENTIONS.md`)

`CONVENTIONS.md` governs in full: British spelling, second person, the forbidden hedges, the
per-chapter structure (`where` callout, one closing `brick` led by **Where this gets spent**, at
least one `familiar`, at least one `warn`, numbered `N.M · Title` sub-headings), and the ⚑ contract.
What follows is what Part IV adds.

- **$\hbar$ is written explicitly everywhere.** Part IV does **not** use natural units. 2.6 already
  told the reader that Part V switches to $\hbar=c=1$; that switch happens in 5.1 and not before.
  The same argument as Part III's refusal to geometrise: nothing is harder for a rusty reader than
  a vanished constant, and every dimensional check the reader can run is a check the book gets for
  free.
- **The $m$ collision, resolved once.** `CONVENTIONS.md` fixes $m$ as **rest mass**, always.
  Part IV therefore writes the magnetic quantum numbers as $m_\ell$, $m_s$, $m_j$ — **never a bare
  $m$** — and uses $m_e$ for the electron mass and $\mu$ for a reduced mass. Flag the collision in
  place at 4.8 §2, as 2.6 §2 flags the rapidity clash. This is the single most likely source of
  silent confusion in the part.
- **Inner product linear in the second slot**, as 0.5 §1 chose and said it was choosing, precisely
  so that $\avg{\phi|\psi}$ reads right-to-left as "amplitude to find $\psi$ in $\phi$". Restate
  this once, in 4.2 §2, because the Born rule is built on it.
- **Dirac notation as 0.5 §2.2 installed it.** Hats on operators ($\hat x$, $\hat H$), no hats on
  eigenvalues or classical quantities. $\hat I$ for the identity, matching 0.5.
- **Fourier convention: the symmetric one**, $\tilde f(k)=\frac{1}{\sqrt{2\pi}}\int f\ee^{-\ii kx}\dd x$,
  exactly as 0.9 §2.2 chose it and for the reason 0.9 gave — it is the unitary one. Momentum-space
  wavefunctions are $\tilde\psi(p)$ with $p=\hbar k$ and the $\sqrt\hbar$ written out.
- **Only these KaTeX macros exist** (`assets/book.js`): `\dd \ee \ii \dv \pdv \abs \norm \ket
  \bra \avg \half \R \C \vv`. There is **no** `\tr`, `\dom`, `\Q`, `\Z`, `\Im` or `\div`. Write
  $\operatorname{tr}$, $\operatorname{dom}$, $\mathbb{Q}$, $\mathbb{Z}$, $\operatorname{Im}$ and
  $\nabla\cdot$. A macro that does not exist produces a chapter that fails the build, and 4.3, 4.4
  and 4.11 each need three of these.
- **Reuse Part 0's symbols exactly where a debt is being collected.** The probability current is
  $\vv J$, because 0.7 §6 wrote $\pdv{\rho}{t}+\nabla\cdot\vv J=0$ with that symbol, and the reader
  must see the *same* equation rather than a cousin.
- **Signs.** $\ii\hbar\,\partial_t\ket\psi=\hat H\ket\psi$; $\hat p=-\ii\hbar\nabla$;
  $\hat U(t)=\ee^{-\ii\hat Ht/\hbar}$; $[\hat L_i,\hat L_j]=\ii\hbar\epsilon_{ijk}\hat L_k$;
  raising operator $\hat a^{\dagger}$, $\hat J_+$. State the sign convention loudly, once, in 4.5 §2,
  and note that the opposite time convention exists in some engineering literature.
- **Physical constants — the Part IV form of the $GM$ rule.** `CONVENTIONS.md` requires the
  *measured combination*, never a product of separately measured pieces. In Part IV that rule bites
  as follows, and it is not a nicety:
  - Since the 2019 SI redefinition, $h$, $c$, $e$ and $k_B$ are **exact by definition**;
    $\alpha^{-1}=137.035999177(21)$ and $m_e$ are **measured** (relative uncertainty $1.5\times10^{-10}$
    and $3.1\times10^{-10}$); and $\epsilon_0$ is *derived* from $\alpha$ by
    $\epsilon_0=e^{2}/(2\alpha hc)$.
  - **Therefore write the Coulomb combination as $\alpha\hbar c$, never as $e^{2}/4\pi\epsilon_0$
    reassembled from a tabulated $e$ and a tabulated $\epsilon_0$.** That reassembly is exactly the
    $G\times M_\odot$ mistake wearing electrical clothes.
  - **Use the measured $R_\infty hc = 13.605693122994(26)\ \mathrm{eV}$ for the Rydberg energy**, not
    $\tfrac12\alpha^{2}m_ec^{2}$ recomputed. $R_\infty$ is the most precisely measured constant in
    physics (relative uncertainty $1.1\times10^{-12}$); the reconstruction is two hundred times
    worse. Where 4.9 needs hydrogen specifically rather than infinite nuclear mass, use the reduced
    mass and get $-13.5983\ \mathrm{eV}$, and say which number is which.
  - $a_0=5.29177210544\times10^{-11}$ m; $m_ec^{2}=0.51099895069$ MeV;
    $\lambda_C=h/m_ec=2.42631023538$ pm.
- **Postulates carry a ⚑ as well as a box.** A postulate is by definition a result the book uses and
  does not derive, which is what the mark means; and `CONVENTIONS.md` is explicit that a chapter
  with no ⚑ is claiming to have built everything it spends. The box says what is being asserted;
  the mark says it was not earned. 4.2 therefore carries the largest flag count in the part and
  that is correct, not a defect.
- **The meaning of ⚑ does not change in Part IV.** `STATUS.md` records that from 5.8 the mark shifts
  register — from *"I chose not to prove this"* to *"nobody has proved this"*. Every flag in Part IV
  is still the first kind, with two honest exceptions that must be labelled as such in place: the
  Born rule (P3) and the measurement problem (4.11 §9). Say so where they appear.
- **Nothing in Part IV uses a contour integral.** `GAPS.md` G2 records that complex analysis has
  never been built and will not be until 5.4. See "What this part must not do".

---

# 4.1 · What Classical Physics Cannot Do

**What this chapter exists to do:** make four classical failures *quantitative*, so that
quantisation arrives as forced rather than proposed — and derive the Planck spectrum by a route
that needs no quantum statistics, because quantum statistics does not exist until 4.11.

**Sections (fixed — forward references point at these numbers):**

| § | Title |
|---|---|
| 1 | What a classical prediction of the blackbody spectrum actually is |
| 2 | Counting modes in a box |
| 3 | Rayleigh–Jeans, and a divergent integral |
| 4 | Einstein's A and B coefficients |
| 5 | The Planck spectrum, and what $h$ is |
| 6 | Light carries momentum in parcels: the photoelectric effect and Compton |
| 7 | Spectral lines, and why an orbiting electron is a catastrophe |
| 8 | Worked examples |
| 9 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Cavity radiation as a thermodynamic object: $u(\nu,T)$ depends on nothing but $\nu$ and $T$ | Kirchhoff's argument, given in full: two cavities at the same temperature joined through a filter | One page, and it is what makes the problem well posed. ⚑ the second law as the input |
| 2 | **Mode counting: $g(\nu)=8\pi\nu^{2}/c^{3}$ per unit volume** | standing waves in a box — **0.8** §7.6's continuum limit, now in three dimensions, with two polarisations | Verified. Count wavevectors in the positive octant of a sphere of radius $k$, divide by the cell $(\pi/L)^{3}$, double for polarisation, differentiate. **Every step on the page** — this closes the half of `GAPS.md` G3 that is pure counting |
| 3 | **Rayleigh–Jeans $u=8\pi\nu^{2}k_BT/c^{3}$** | item 2 × equipartition $k_BT$ per mode, which is **0.6** WE1's Boltzmann distribution with a quadratic Hamiltonian | Derive equipartition from 0.6, do not quote it |
| 4 | **The ultraviolet catastrophe is a divergent integral, not a metaphor** | $\int_0^\infty\nu^{2}\dd\nu=\infty$ | Say the number: a cavity at room temperature would hold infinite energy. This is the sentence the chapter is built around |
| 5 | Wien's displacement and the $T^{4}$ law as *experimental* constraints any correct formula must meet | ⚑ measured | Set the target before the derivation, so the reader can score it |
| 6 | **Detailed balance**, stated as the assumption it is | ⚑ with hypotheses named: a stationary state in which *each* microscopic process balances its own reverse, which is stronger than "the total rate is zero" | Per pacing item 10 |
| 7 | Einstein's three processes: absorption $B_{12}$, spontaneous emission $A_{21}$, **stimulated emission $B_{21}$** | posited as the only three rates linear in the level populations | The move worth naming: stimulated emission is *forced* by the argument, not added. It was not known when Einstein wrote it down |
| 8 | $N_2/N_1=\ee^{-h\nu/k_BT}$ | **0.6** WE1 | Non-degenerate levels; note the $g_1/g_2$ that would appear otherwise |
| 9 | **$B_{12}=B_{21}$** | require item 7's balance to survive $T\to\infty$, where $u\to\infty$ | One line, and it is the whole trick |
| 10 | **$A_{21}/B_{21}=8\pi h\nu^{3}/c^{3}$** | require the $h\nu\ll k_BT$ limit to reproduce item 3 | The Rayleigh–Jeans law is used as a *boundary condition*, which is why the classical failure had to come first |
| 11 | **The Planck spectrum** $\displaystyle u(\nu,T)=\frac{8\pi h\nu^{3}}{c^{3}}\frac{1}{\ee^{h\nu/k_BT}-1}$ | items 7–10 | Verified. **No Bose–Einstein statistics anywhere** — that is the point, and 4.11 §5 returns to derive the same formula the other way. `GAPS.md` G3 closed |
| 12 | Wien and Stefan–Boltzmann, **recovered with numbers** | differentiate and integrate item 11 | Verified: $\nu_{\max}/T=5.8789\times10^{10}$ Hz K$^{-1}$ from the root of $3(1-\ee^{-x})=x$ at $x=2.8214$; $\int_0^\infty x^{3}/(\ee^{x}-1)\dd x=\pi^{4}/15$ gives $\sigma=5.6704\times10^{-8}$ W m$^{-2}$K$^{-4}$. Arithmetic on the page |
| 13 | $h$ read off, and the two limits of item 11 | $h\nu\ll k_BT$ and $h\nu\gg k_BT$ | Say what $h$ *is* at this stage: a fitted constant with dimensions of action. Nothing more is claimed until 4.2 |
| 14 | Photoelectric effect: $K_{\max}=h\nu-\phi$, with a threshold and no intensity dependence | ⚑ the measurements | The classical prediction is stated and then contradicted, in that order |
| 15 | **Compton: $\Delta\lambda=(h/m_ec)(1-\cos\theta)$** | **2.5** §8, four-momentum conservation, unchanged | Verified symbolically. **This is 2.5's Worked example 1 re-used exactly as 2.5 promised**, and the promise is collected by name: *"Chapter 4.1 reuses Worked example 1 as evidence that photons carry momentum"*. $h/m_ec=2.42631$ pm |
| 16 | $p^{\mu}=\hbar k^{\mu}$ promoted from suspicion to law | items 14–15 + **2.5** §7.1 | Collects 2.5's four separate promises verbatim, including *"Chapter 4.1 supplies the missing constant"* |
| 17 | Hydrogen's spectrum as an empirical formula, $1/\lambda=R(1/n_1^{2}-1/n_2^{2})$ | ⚑ measured | Left unexplained on purpose. 4.9 §5 collects it |
| 18 | **A classical orbiting electron radiates and falls in, in $1.6\times10^{-11}$ s** | Larmor's formula ⚑, integrated | Do the integral and give the number. An atom that lasts $16$ picoseconds is a sharper statement than "classical physics fails" |

**Interactive (one):** the three spectra — Planck, Rayleigh–Jeans, Wien — on log–log axes with a
temperature slider, showing where each is right. **Test it must pass:** the displayed peak tracks
$\nu_{\max}=2.8214\,k_BT/h$ to three significant figures across the slider range, and the numerically
integrated area matches $\sigma T^{4}$ with $\sigma=5.6704\times10^{-8}$ to three figures.

**⚑ permitted in 4.1:** the second law (item 1); the measured Wien and Stefan–Boltzmann constants
used as targets (item 5); detailed balance, with its hypotheses named (item 6); the photoelectric
and Compton measurements (items 14–15); the empirical Rydberg formula (item 17); Larmor's radiation
formula (item 18). **Nothing else** — the Planck law is derived, and the mode count is derived.
**Seven.**

---

# 4.2 · The Linear Algebra of Quantum States ※

**What this chapter exists to do:** show that Chapter 0.5 was quantum mechanics with the physics
stripped off, and put the physics back — as a table of renamings plus seven postulates (P1–P7, as §0.1
lists them), and nothing else.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The claim, stated before it is earned |
| 2 | The table of renamings |
| 3 | States are unit rays |
| 4 | Observables are Hermitian operators |
| 5 | The Born rule |
| 6 | Measurement, and the state after it |
| 7 | Evolution has a Hermitian generator |
| 8 | Canonical quantisation |
| 9 | Two systems: the tensor product |
| 10 | Three two-state systems, in full |
| 11 | Worked examples |
| 12 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **The table of renamings** — the chapter's spine | **0.5** §§1–8, item by item: eigenvalue → outcome; Hermitian → observable; orthonormal basis → complete set of outcomes; $\abs{\avg{e_i,v}}^{2}$ → probability; $\sum_i\ket{e_i}\bra{e_i}=\hat I$ → probabilities sum to one; commuting operators → compatible measurements; $\ee^{\ii A}$ → symmetry | **Collects 0.5's own sentence**: *"Chapter 4.2 becomes a translation exercise: a table of renamings, not a new subject."* Build the table first and refer back to it for the rest of the chapter |
| 2 | Nothing in item 1 is a postulate | **0.5** §6.5's insight box, quoted | 0.5 said *"That is one postulate, not four. Everything else is renaming."* Collect it |
| 3 | **P1** — a state is a unit ray | ⚑ postulate box | The phase: global unobservable, relative everything. Give the two-slit argument for why in one paragraph |
| 4 | **P2** — an observable is a Hermitian operator | ⚑ postulate box | And flag *in place* that "Hermitian" will be sharpened to "self-adjoint" in 4.4 §4, and that the difference is physical, not pedantic. **Collects 0.5's promise** that *"an observable is a Hermitian operator is the one postulate that has to be made"* |
| 5 | **P3 — the Born rule** | ⚑ postulate box, and the chapter's most important paragraph | **It is not derivable.** Say it there. ⚑ Gleason's theorem in the same box **with its hypotheses**: it derives $\abs\psi^{2}$ from the assumption that probability is a countably additive measure on projections, in dimension $\ge3$ — which assumes most of what one wants explained. Not a derivation. `GAPS.md` G13 |
| 6 | **P4 — the state update**, as a *separate* postulate | ⚑ postulate box | Most books merge P3 and P4. Separating them is what lets 4.11 §9 say precisely which one decoherence addresses |
| 7 | Expectation value $\avg{\hat A}=\bra{\psi}\hat A\ket{\psi}$ and variance | items 1, 5 | Derived from P3, not postulated. Show the two-line calculation |
| 8 | **Quantum numbers, defined** | **0.5** §8's simultaneous diagonalisation | **Collects 0.5's promise by name**: *"Chapter 4.8 calls such a list the quantum numbers of the state"* — 4.2 defines the term, 4.8 spends it. Note the reassignment in place |
| 9 | **P5** — evolution has a Hermitian generator | ⚑ postulate box; **0.5** §7's $U=\ee^{\ii A}$ | State it here, derive the half that is derivable in 4.5 §2. **Collects 0.5's "Where this is spent" line** naming this exact equation |
| 10 | **P6 — $[\hat x,\hat p]=\ii\hbar$** | ⚑ postulate box; **1.3** §6.2's $\{q,p\}=1$ | **This is where 1.3's canonical-quantisation promises land, not 4.7.** 1.3 wrote *"Chapter 4.7 will take the classical structure you now own… and make the single substitution"* — but 4.5, 4.6 and 4.8 all need the commutator first. Resolution, and it must be executed in both places: **4.2 postulates the commutator and names 1.3; 4.7 §7 collects the general correspondence and proves it cannot be made exact.** Say in 4.2 §8 that the general question is deferred to 4.7 |
| 11 | **No finite-dimensional space carries $[\hat x,\hat p]=\ii\hbar$** | trace both sides: $\operatorname{tr}[\hat x,\hat p]=0$ but $\operatorname{tr}(\ii\hbar\hat I_n)=\ii\hbar n$ | Verified. **Three lines, and it forces the whole of 4.3 and 4.4.** Quantum mechanics is infinite-dimensional before any physics is done, and the reader can prove it here. This is the single best possible motivation for the two mathematics chapters and it belongs in the main text |
| 12 | **P7** — the tensor product | ⚑ postulate box; **0.4** §2 | Dimension multiplies, and the reason: a basis of pairs. Defer the consequences to 4.11 |
| 13 | The ammonia molecule, neutrino oscillation, the qubit | **0.5** §9, where all three were set up | **Collects 0.5's promise verbatim**: *"Chapter 4.2 will do all three, and the linear algebra will already be finished."* Do all three, and let the reader see that they are one calculation |
| 14 | Rabi oscillation between two levels, with the probabilities summing to one | item 13; **0.8** §6 | The numerical confirmation of §0.3. Note the exact solution and hold the driven case for 4.10 |
| 15 | The honest note about what everything rests on | **0.4** §7's ⚑ on the fundamental theorem of algebra | One paragraph. Every measurement postulate above descends from 0.5's spectral theorem, whose Step 1 is *"Because $V$ is complex, [0.4] supplies an eigenvalue"* — and that theorem is the one thing Part 0 imported. ⚑, naming **5.4** as where it becomes a corollary. `GAPS.md` G4 |
| 16 | Announce the shape of 4.3 and 4.4 | pacing item 14 | 0.4 built the space, 0.5 built the operators; 4.3 builds the space, 4.4 builds the operators. In the closing brick |

**Interactive (one):** a Bloch sphere for a two-state system with a Hamiltonian the reader sets —
watch the state precess, with $\abs{c_1}^{2}$ and $\abs{c_2}^{2}$ read out. **Test:**
$\abs{c_1}^{2}+\abs{c_2}^{2}=1$ to $10^{-12}$ at every frame, and the precession period matches
$2\pi\hbar/\Delta E$ to four figures.

**⚑ permitted in 4.2:** the seven postulate boxes P1–P7; Gleason's theorem
with its hypotheses; the fundamental theorem of algebra inherited from 0.4; the measured ammonia
inversion frequency and neutrino mixing parameters used as illustration. **Nothing else.** **Ten,
of which seven are postulates** — and 4.2 is the only chapter in the book permitted a count like
that, because it is the only chapter whose subject is the postulates.

---

# 4.3 · Function Spaces: Measure, L², and Completeness ※

**What this chapter exists to do:** rebuild the integral so that the space of states is actually a
space — closing 0.2's promise to *"throw away and rebuild the integral from scratch"* and 0.9's
completeness ⚑ in one chapter.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Why the Riemann integral has to go |
| 2 | Measure, with one thing quoted |
| 3 | The Lebesgue integral, built |
| 4 | Monotone and dominated convergence |
| 5 | $L^{2}$, and the functions that are not functions |
| 6 | Completeness: the theorem, and the failure it repairs |
| 7 | Orthonormal bases in infinite dimensions |
| 8 | The Fourier basis is a basis |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **The failure, exhibited:** the indicator of the rationals is not Riemann integrable | **0.2** §1.1, which already did this, calls the function $\chi$ and shows every partition can be tagged either way | **Collects 0.2's promise by name**: *"In Chapter 4.3 we will throw away and rebuild the integral from scratch (the Lebesgue integral), and the reason is visible already."* Do it in the first paragraph, and **use 0.2's own symbol $\chi$** rather than introducing $\chi_{\mathbb Q}$ |
| 2 | **Cauchy sequences, *defined here*** | **nowhere earlier — this is a hole nobody has recorded** | `PLAN-FORWARD.md` §5.3 lists "Cauchy sequences and convergence (**0.3**)" as a prerequisite of this chapter. **`grep` finds no occurrence of "Cauchy sequence" anywhere in the twenty-eight written chapters**; the only Cauchys in the book are Cauchy–Schwarz (0.5), the Cauchy distribution (0.9) and Cauchy's functional equation (2.2). The definition is one paragraph and 4.3 must give it, building on **0.3** §3's convergence tests. Do not cite it as already built |
| 3 | **The second failure, which is the one that matters:** a sequence of Riemann-integrable functions, Cauchy in the $L^{2}$ norm, whose limit is not Riemann integrable | **0.2** §1.1's own $f_n$ — the function equal to $1$ at $q_1,\ldots,q_n$ and $0$ elsewhere, which 0.2 constructed and then set aside | Use 0.2's sequence, not a new one. `PLAN-FORWARD.md` §3.1 is right that this is the payload: **the reader must see the hole before it is filled**, and 0.2 already dug it in front of them |
| 4 | $\sigma$-algebras, and Lebesgue measure on $\R$ | ⚑ the construction (outer measure, Carathéodory) — countable additivity, translation invariance and regularity are **quoted as a package** | This is the one substantial import in the chapter and it must be marked as such. Say precisely what is being assumed and what it buys |
| 5 | **Not every set is measurable** — the Vitali set | built, in a grind box: choice, translates, countable additivity, contradiction | Short, complete, and it makes item 4's flag feel like a real restriction rather than a formality |
| 6 | The Lebesgue integral: simple functions, then the sup | item 4 | Contrast the two pictures explicitly — Riemann slices the domain, Lebesgue slices the range. That one sentence is the whole idea |
| 7 | It agrees with Riemann where Riemann works | items 1, 6 | Otherwise the reader has to relearn Part 0 |
| 8 | **Monotone convergence**, derived | item 6 | |
| 9 | **Dominated convergence**, derived from item 8 via Fatou | item 8 | **Collects 0.2 §4.4's promise verbatim**: dominated convergence *"proved properly in Chapter 4.3"*. And go back and discharge the specific use 0.2 made of it — differentiating under the integral sign — by name |
| 10 | $L^{2}(\R)$ as an inner-product space; functions equal almost everywhere are one vector | **0.5** §1's axioms, checked one by one | **Collects 0.5's promise**: *"That row is the entire reason Chapter 4.3 is possible."* The quotient is the price of axiom (iii) and the reader should see why |
| 11 | Cauchy–Schwarz, Minkowski, and $L^{2}\not\subset L^{1}$ on $\R$ | **0.5** §1 unchanged | The theorems transfer without a word changed. Say so — it is the payoff of 0.5 having been abstract |
| 12 | **Completeness of $L^{2}$ (Riesz–Fischer)** ⚑, then made concrete | ⚑ the diagonal-subsequence proof; then *show* the reader the exact sequence from item 3 now converging, in $L^{2}$, to a limit that exists | `PLAN-FORWARD.md` §3.1's decision, executed: quote the theorem, exhibit the repair. The reader ends holding a flag they have watched do work |
| 13 | Separability; an orthonormal basis is countable | item 4's regularity, plus polynomials with rational coefficients | Needed before item 16 can even be stated |
| 14 | Bessel, Parseval, and the equivalence of four statements of completeness | **0.5** §2 | Prove the equivalence; it is what makes item 16 checkable |
| 15 | **Continuous functions are dense in $L^{2}$** | derived from the regularity quoted in item 4 | Do **not** flag this separately — say explicitly that it is being cashed out of item 4's package, so the reader can see the flag is doing exactly the work it claimed |
| 16 | **Fejér's theorem: the Cesàro means of a Fourier series converge uniformly for continuous $f$** | built, constructively, from the Fejér kernel — a positive kernel, integrating to one, concentrating at zero, which is **0.9** §5.2's delta-sequence argument re-used | The good route: Fejér is elementary, constructive, and reuses machinery the reader owns |
| 17 | **The Fourier basis is an orthonormal basis of $L^{2}$** | items 14, 15, 16 | Verified. **This closes `GAPS.md` G1's sixth promise and the ⚑ of 0.9 §1.3** — *"Both facts are proved in Chapter 4.3, where the space of square-integrable functions gets its proper name, a Hilbert space, and completeness stops being an assumption."* **Do not strike the flag in 0.9.** The book's convention, applied twice already at Chapter 0.7 §7.3 (Poincaré) and §7.1 (generalised Stokes), is that a ⚑ stays at the point of use and names the chapter that proves it; both are still flagged today and both were collected in 3.5. Record the payment in `GAPS.md` instead |
| 18 | $L^{2}$ convergence is not pointwise convergence | items 16–17; **0.9** §1.4's Gibbs example, revisited | Verified: $\norm{f-S_N}_2\sim N^{-1/2}$ for the square wave while the overshoot sits permanently at $8.95\%$ of the jump. **Two different convergences, one picture.** This is §0.3's numerical confirmation |
| 19 | Position and momentum representations are two bases for one space | item 17 and **0.9** §2.3 | **Collects 0.9's "Where this gets spent" line** naming 4.3 for exactly this |

**Interactive (one):** partial sums of a Fourier series with $N$ on a slider, plotting the function,
the partial sum, the $L^{2}$ error and the pointwise error together. **Test:** the $L^{2}$ error
falls like $N^{-1/2}$ over two decades of $N$ while the displayed maximum error stays at
$0.0895\times$ the jump — the two curves visibly doing different things.

**Three errors in this 4.3 plan, caught by the writing and verification agents. Recorded because the
same mistakes are easy to make again in 4.4:**

1. **Item 3 does not work as specified.** Chapter 0.2's $f_n$ differs from $f_m$ on a *finite* set, so
   $\lVert f_n-f_m\rVert_2=0$ and every $f_n$ is the same vector in $L^2$, namely zero — which the
   Riemann class already contains. It exhibits the seminorm failure and the non-closure failure but
   **not incompleteness**, so item 12's payoff would have had nothing behind it. The chapter as
   written uses 0.2's sequence for the two failures it genuinely shows, says out loud that it is too
   thin for the third, and then *thickens* 0.2's own enumeration into indicators of small intervals
   around each rational. That limit, $\mathbf 1_U$ with $\abs U\le\tfrac14$, is genuinely not
   Riemann integrable, and the reader still recognises 0.2's construction.
2. **Item 13's stated source is impossible.** No non-zero polynomial is in $L^2(\R)$, so polynomials
   with rational coefficients cannot be dense in it. That argument is Weierstrass on a compact
   interval, which is not this space. The chapter uses step functions with rational values on
   rational-endpoint intervals, out of the same regularity clause the plan wanted spent.
3. **Item 17's instruction to strike 0.9's flag contradicts the book's convention** — see the item's
   own row, now corrected.

**⚑ permitted in 4.3:** the construction of Lebesgue measure, quoted as a package (item 4); the
proof of Riesz–Fischer (item 12). **Nothing else.** **Two** — and it should be said in the closing
brick that a chapter this heavy carries two flags, because that is the claim the chapter is making.

---

# 4.4 · Operators in Infinite Dimensions ※

**What this chapter exists to do:** say exactly which of Chapter 0.5's theorems survive, which need
repair and which are false — and pay `GAPS.md` G1's remaining four promises, including the one 0.5
called "the bill".

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The four places Chapter 0.5 used finite dimension |
| 2 | Bounded, unbounded, and why the derivative cannot be tamed |
| 3 | Domains, and the adjoint's domain |
| 4 | Symmetric is not self-adjoint |
| 5 | Two cases in full: the interval, and the half-line |
| 6 | The spectrum, when there are no eigenvectors |
| 7 | The spectral theorem, in multiplication form |
| 8 | Checked three times |
| 9 | Stone's theorem |
| 10 | What $\ket x$ and $\ket p$ actually mean |
| 11 | Worked examples |
| 12 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The four failures named, one by one | **0.5**'s closing paragraph, quoted in full | 0.5 listed them: *"in the induction, in rank–nullity, in the interchange of sums, in the claim that an injective map is surjective."* Take them in that order and say what happens to each. **This is the collection point for 0.5's "Chapter 4.4 is where the bill comes due"** |
| 2 | **$\dv{}{x}$ is unbounded** | exhibit $\ee^{\ii kx}$ on a bounded interval: norm fixed, derivative norm $\to\infty$ | **Collects 0.6 §2's promise verbatim**: *"In infinite dimensions linear maps can be unbounded, $\dv{}{x}$ being the standard offender"* |
| 3 | **Unboundedness is not avoidable**: Hellinger–Toeplitz | ⚑ the closed graph theorem; derive Hellinger–Toeplitz from it in two lines | A symmetric operator defined on *all* of a Hilbert space is bounded. So an unbounded observable **must** have a restricted domain: the domain is forced, not chosen for convenience. This reframes the whole chapter and is worth its two lines |
| 4 | Domains; $\hat p$ on $L^{2}(\R)$ | item 3; **0.9** §2 | The domain of $\hat p$ is the functions whose derivative is in $L^{2}$, and it is dense. Say what "dense" is doing |
| 5 | **The adjoint, with its own domain** | **0.5** §4's definition, now read carefully | The definition of $\hat A^{\dagger}$ *determines* $\operatorname{dom}(\hat A^{\dagger})$, and there is no reason for it to equal $\operatorname{dom}(\hat A)$. This is the sentence the chapter turns on |
| 6 | **Symmetric ($\avg{\hat Au,v}=\avg{u,\hat Av}$ on $\operatorname{dom}\hat A$) vs self-adjoint ($\hat A=\hat A^{\dagger}$, *domains included*)** | items 4–5 | **P2 is corrected here.** Go back and say so: 4.2 §4 said "Hermitian" and it was not enough |
| 7 | **The boundary term is where the domain lives** | **0.2** §3.2's integration by parts, redone with the boundary term kept | **Collects 0.2's promise by name**: *"Chapter 4.4, where it makes $-\ii\hbar\partial_x$ Hermitian and thereby makes momentum an observable."* 0.2 waved the boundary term through; here it is the whole content |
| 8 | Deficiency indices, stated | ⚑ von Neumann's classification, with hypotheses | Then apply it by hand three times in item 9 — the flag is discharged into cases the reader checks |
| 9 | **$\hat p=-\ii\hbar\dv{}{x}$ on three domains** | solve $\hat p^{\dagger}f=\pm\ii f$, i.e. $f=\ee^{\mp x/\hbar}$, and ask which solutions are square-integrable | Verified. **On $\R$: $(0,0)$, essentially self-adjoint. On $[0,L]$: $(1,1)$, a genuine one-parameter $U(1)$ family $\psi(L)=\ee^{\ii\theta}\psi(0)$ — the Bloch phase, and a physical choice. On $[0,\infty)$: $(1,0)$, and therefore *no self-adjoint extension at all*: "the momentum of a particle on a half-line" is not an observable.** Three lines of algebra for a genuinely shocking conclusion |
| 10 | **The particle in a box: $-\dd^{2}/\dd x^{2}$ on $[0,L]$ has deficiency indices $(2,2)$, hence a $U(2)$ — *four-real-parameter* — family of self-adjoint extensions** | item 8 applied to the second derivative | **Correction to `PLAN-FORWARD.md` §3.1, which says "a one-parameter family". It is four.** Dirichlet, Neumann, periodic, antiperiodic and the two-parameter Robin family all sit inside $U(2)$. Work the Robin family $\psi'(0)=\alpha\psi(0)$, $\psi'(L)=-\alpha\psi(L)$ explicitly, get its transcendental spectrum, and show that **different extensions have different spectra** — so the boundary condition is physics and not bookkeeping. Verified numerically |
| 11 | The spectrum decomposed: point, continuous, residual | items 4–6 | And the fact 0.9 flagged: $\hat p$ has **no eigenvectors in the space** and a purely continuous spectrum. **Collects 0.9 §5.3** |
| 12 | **The spectral theorem, multiplication-operator form** ⚑ | ⚑, with hypotheses: every **self-adjoint** operator is unitarily equivalent to multiplication by a real function on some $L^{2}(\mu)$ | The one substantial flag in Part IV. State it as *the infinite-dimensional reading of 0.5's $A=UDU^{\dagger}$*, in exactly those words, and say that its proof (Cayley transform, continuous functional calculus, Riesz representation) is three chapters of analysis this book does not spend. `GAPS.md` G1's proposed outcome, executed |
| 13 | **Verification 1: $\hat x$** | already multiplication by $x$ on $L^{2}(\R,\dd x)$ | Trivial, and that is the point: the theorem's *statement* is that everything looks like this |
| 14 | **Verification 2: $\hat p$** | the Fourier transform of **0.9** §2.3, which 0.9 proved unitary | $\mathcal F\hat p\mathcal F^{-1}$ is multiplication by $\hbar k$. Verified. One line, and it uses a unitary the reader built |
| 15 | **Verification 3: $\hat H_{\text{osc}}$** | Hermite functions, **built complete here** | **The Hermite functions are complete, and it is derivable with what 4.3 built.** Proof: if $\avg{f,h_n}=0$ for all $n$ then $\int f(x)x^{n}\ee^{-x^{2}/2}\dd x=0$ for all $n$; expand $\ee^{-\ii kx}$ in its power series and interchange (**dominated convergence, 4.3 §4**, with dominating function $\abs f\ee^{-x^{2}/2}\ee^{\abs{kx}}$, integrable by Cauchy–Schwarz); so the Fourier transform of $f\ee^{-x^{2}/2}$ vanishes identically; so $f=0$ by **0.9** §2.3. **No complex analysis, no ⚑.** Then $\hat H_{\text{osc}}$ is multiplication by $(n+\half)\hbar\omega$ on $\ell^{2}$ |
| 16 | The three verifications, collected | items 13–15 | Say it plainly: the reader now holds a quoted theorem **and has checked it in every case the book will use it**. That is the standard `PLAN-FORWARD.md` §3 sets, met |
| 17 | The projection-valued measure form, and $\hat A=\int\lambda\,\dd P(\lambda)$ | item 12 | **Collects 0.5 §6.4's two promises by name**: the projection form *"is the one that survives to infinite dimensions"*, and *"the sum $\sum_k\lambda_kP_k$ becomes an integral $\int\lambda\,\dd P(\lambda)$… Chapter 4.4 pays this bill in full"* |
| 18 | **Stone, forward direction:** $\hat H$ self-adjoint $\Rightarrow$ $\ee^{-\ii\hat Ht/\hbar}$ unitary | item 12's functional calculus | Three lines. ⚑ **the converse** (every strongly continuous one-parameter unitary group has a self-adjoint generator), which is the hard half. **This is what makes "time evolution is unitary" and "the Hamiltonian is self-adjoint" the same statement** — the sentence 0.5 §7 has been pointing at |
| 19 | **What $\ket x$ and $\ket k$ mean** | items 11, 12; **0.9** §5.3 | The honest crutch first: **box normalisation, then the limit**, worked once in full so the reader has a procedure that always works. Then ⚑ Gelfand–Maurin and the rigged Hilbert space, with the concrete content stated — these are continuous functionals on a smaller space of well-behaved functions, and every manipulation using them abbreviates a wave-packet statement. **Collects 0.9's *"That gap is real. Chapter 4.4 closes it"*** — and says, in place, that the general theory of distributions is 5.4's. `GAPS.md` G11 |
| 20 | What is now safe to do, listed | the whole chapter | A closing checklist: insert a resolution of the identity; expand in eigenstates; write $\ee^{-\ii\hat Ht/\hbar}$; integrate by parts and drop the boundary term. Each with the condition under which it is legitimate. **This list is what the rest of Part IV stands on** |

**Interactive (one):** the spectrum of $-\dd^{2}/\dd x^{2}$ on $[0,L]$ as the Robin parameter
$\alpha$ is dialled — levels sliding continuously, and one dropping below zero as $\alpha$ goes
negative. **Test:** at $\alpha=0$ the levels read $n^{2}\pi^{2}\hbar^{2}/2mL^{2}$ to four significant
figures against the closed form; the level count below any fixed energy changes as $\alpha$ crosses
the value the transcendental equation predicts.

**⚑ permitted in 4.4:** the closed graph theorem (item 3); von Neumann's deficiency-index
classification, with hypotheses (item 8); the spectral theorem for unbounded self-adjoint operators,
in multiplication form, with hypotheses — then verified three times (item 12); the converse half of
Stone (item 18); Gelfand–Maurin / the rigged Hilbert space (item 19). **Nothing else** — and
specifically **not** Hermite completeness, which is built. **Five.**

---

# 4.5 · The Schrödinger Equation

**What this chapter exists to do:** get the equation from two things already built — a unitary flow
with a self-adjoint generator, and one physical identification — and show that normalisation is
preserved as a theorem rather than a hope.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | What time evolution has to be |
| 2 | Stone, and the generator |
| 3 | Which operator is the generator |
| 4 | The equation in the position representation |
| 5 | The probability current |
| 6 | Stationary states |
| 7 | A free packet: group velocity, and spreading |
| 8 | Schrödinger and Heisenberg are one change of basis |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Evolution must be linear, and must preserve $\norm\psi=1$ | P1, P3 | **Collects 0.5's promise verbatim**: *"$U(t)$ must be unitary because $\norm\psi^{2}=1$ is a total probability"* |
| 2 | **Unitary $\Rightarrow$ $\abs\lambda=1$, and there is no third option** | **0.5** §7 | **Collects 0.5's sentence**: *"If $\abs\lambda\lt1$ the state would fade away and probability would leak out of the universe."* |
| 3 | $U(t+s)=U(t)U(s)$, $U(0)=\hat I$, strong continuity | item 1 | The group law is where "no memory" enters. Name it |
| 4 | **$U(t)=\ee^{-\ii\hat Ht/\hbar}$ with $\hat H$ self-adjoint** | **4.4** §9 (Stone, converse half ⚑) | And therefore $\ii\hbar\,\partial_t\ket\psi=\hat H\ket\psi$. **Collects 0.1's forward pointer**, the first sentence in the book that named a Part IV chapter |
| 5 | Why $\hbar$ and why $\ii$ | dimensions; and item 2 | **Collects 0.7's promise by name**: *"the $\ii$ is what makes time evolution a rotation in the space of states rather than a contraction, which is exactly what conserving total probability requires"* — 0.7 said 4.5 would say what it is. Put the Schrödinger and diffusion equations side by side as 0.7 did |
| 6 | **$\hat H=\hat p^{2}/2m+V(\hat x)$ — an identification, not a derivation** | **1.3** §2.2's classical $H$; P6 | Say it is a choice, per pacing item 13, and name **4.7** §7 as where the choice is shown to be unextendable |
| 7 | $\hat p=-\ii\hbar\nabla$ in the position representation | P6, solved | **Collects 1.3's promise**: *"the operator $\hat p=-\ii\hbar\,\partial/\partial q$ is the standard realisation"*. Show it is *a* realisation and note Stone–von Neumann ⚑ for uniqueness, with hypotheses (irreducibility, finitely many degrees of freedom) — the hypothesis that fails in 5.3 |
| 8 | **$\ii\hbar\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+V\psi$** | items 4, 6, 7 | **Collects 0.7's promise** that the kinetic term is a Laplacian, and 0.8's that adding an $\ii$ to the wave equation gives this |
| 9 | **The probability current and $\pdv{\rho}{t}+\nabla\cdot\vv J=0$** | multiply by $\psi^{*}$, subtract the conjugate — every step shown | Verified. **The chapter's centre.** $\vv J=\frac{\hbar}{m}\operatorname{Im}(\psi^{*}\nabla\psi)$, written with **0.7**'s own symbol $\vv J$ so the reader sees the same equation, not a cousin. **Collects 0.7 §6 by name** — *"The continuity equation → Chapter 4.5 (probability current)"* — and makes "the wavefunction stays normalised" a theorem |
| 10 | Stationary states; $\hat H\psi=E\psi$ | separation of variables | **Collects 0.8's promise**: *"In Chapter 4.6 the eigenvectors of $\hat H$ are the stationary states"* — note the reassignment: 4.5 defines them, 4.6 finds them |
| 11 | The general solution as a superposition | **4.4** §7's spectral theorem | Every solvable problem in 4.6 and 4.9 is this one line plus a diagonalisation |
| 12 | **A Gaussian packet, in full** | **0.2** §4's Gaussian integral, **0.9** §3 | **Collects 0.2's promises by name** (normalising a wave packet; $\abs\psi^{2}\propto\ee^{-2ax^{2}}$; and *"quantum mechanics then contributes one physical identification, $b=p/\hbar$"*) |
| 13 | Group velocity $=p/m$; **spreading $\sigma(t)^{2}=\sigma_0^{2}+(\hbar t/2m\sigma_0)^{2}$** | **0.8** §7.6's dispersion; **0.9** §3 | Verified numerically to eight figures. Give the number for an electron localised to 1 nm: it doubles in width in $\sim2.7\times10^{-14}$ s |
| 14 | Ehrenfest, **stated and deferred** | item 9 | State the two relations, say they are proved in 4.7 §4, and do **not** prove them here. 1.1's promise names 4.7 |
| 15 | The Heisenberg picture, and the fact that it is a change of basis | **0.4** §4 | **Collects 0.4's promise verbatim**: *"why the Schrödinger and Heisenberg pictures look like different physics instead of different bases"* |

**Interactive (one):** a split-operator integration of the equation, with a potential the reader
picks (free, step, barrier, oscillator) and $\abs\psi^{2}$, $\operatorname{Re}\psi$ and $\vv J$
drawn together.
**Test:** the norm is conserved to $4\times10^{-13}$ over the full run; in the oscillator, $\avg x(t)$
tracks $x_0\cos\omega t$ to $2\times10^{-6}$; for the free packet the displayed width matches
item 13's formula to four figures.

**⚑ permitted in 4.5:** the converse half of Stone, cited from 4.4 rather than re-flagged as new;
de Broglie's $\lambda=h/p$ for **matter** as experimental input, naming Davisson–Germer; the
Stone–von Neumann uniqueness theorem, with hypotheses (item 7); the identification
$\hat H=\hat p^{2}/2m+V$, flagged as the choice it is (item 6). **Nothing else.** **Four.**

---

# 4.6 · Systems You Can Solve in One Dimension

**What this chapter exists to do:** solve the oscillator twice, because the second way — the ladder
— is the whole of Parts V and VII, and carry 0.8's eight promises across.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Bound states, and the boundary condition as a domain choice |
| 2 | The infinite well |
| 3 | The finite well, and tunnelling |
| 4 | The oscillator, the hard way |
| 5 | The oscillator, the ladder way |
| 6 | The wavefunctions, from $\hat a\ket0=0$ |
| 7 | The phase-space area, collected |
| 8 | Scattering: step, barrier, and what transmission means |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The boundary condition is a choice of self-adjoint extension | **4.4** §5 | Do not let the reader think $\psi(0)=\psi(L)=0$ is obvious. It is one point in a $U(2)$, and the physics of an infinite wall is what selects it |
| 2 | Infinite well: $E_n=n^{2}\pi^{2}\hbar^{2}/2mL^{2}$ | item 1; **0.8** §3 | And the zero-point energy read as uncertainty, using **0.9** §6 |
| 3 | Finite well: the transcendental matching condition, solved graphically | **0.8** §3; matching $\psi,\psi'$ | Derive the condition; count the bound states; show at least one always exists in one dimension |
| 4 | **Tunnelling**, with an amplitude and a number | item 3's exponential tails | Give the transmission through a 1 eV barrier 1 nm wide for a 0.5 eV electron. ⚑ the STM and $\alpha$-decay measurements it is compared against |
| 5 | The oscillator by series — **stated and not done** | | Say plainly that the differential-equation route exists, is standard, and is being skipped because the algebraic route is better teaching and is the one Parts V and VII use. `PLAN-FORWARD.md` §3.1's "never by series" decision, made visible |
| 6 | $\hat a=\sqrt{\frac{m\omega}{2\hbar}}\big(\hat x+\frac{\ii}{m\omega}\hat p\big)$, $\hat a^{\dagger}$ | **0.5** §4's adjoint; P6 | Motivate by factorising $\hat x^{2}+\hat p^{2}$ as far as commutativity permits, and let the leftover **be** the commutator. That is where the zero-point energy comes from and it should be visible at the moment of factorisation |
| 7 | **$[\hat a,\hat a^{\dagger}]=1$; $\hat H=\hbar\omega(\hat a^{\dagger}\hat a+\half)$** | item 6, expanded | Verified |
| 8 | **$[\hat N,\hat a^{\dagger}]=\hat a^{\dagger}$, $[\hat N,\hat a]=-\hat a$** — the ladder | item 7 | Verified. Name the technique: this is the same "commutator shifts the eigenvalue" move that 4.8 will run on $\hat J_\pm$ and 7.4 on the Virasoro modes |
| 9 | **The ladder terminates below**, because $\avg{\hat N}\ge0$ | item 7 and positivity of $\norm{\hat a\ket\psi}^{2}$ | The one step people skip. Do it: the spectrum is bounded below *because* a norm is non-negative |
| 10 | **$E_n=(n+\half)\hbar\omega$, from the algebra alone** | items 8–9 | Verified. **Collects 1.3's ⚑ by name** — *"which Chapter 4.6 will derive exactly, with ladder operators and no semiclassical approximation, and get precisely this answer"* — and 0.8's *"the $\tfrac12\hbar\omega$ that will not go away"* |
| 11 | $\psi_0\propto\ee^{-m\omega x^{2}/2\hbar}$ | solve $\hat a\psi_0=0$, a **first-order** equation | The whole point of the method: a second-order eigenvalue problem replaced by one first-order equation and an algebra |
| 12 | $\psi_n\propto(\hat a^{\dagger})^{n}\psi_0$, and these are the Hermite functions | item 11 | **Collects 0.5's promise**: *"The identical procedure with a weight $\ee^{-x^{2}}$ on the whole line produces the Hermite polynomials, which are the quantum harmonic oscillator states of Chapter 4.6."* Completeness is cited from **4.4** §8, not re-proved |
| 13 | $\avg{\hat x^{2}}=\avg{\hat p^{2}}/m^{2}\omega^{2}=(n+\half)\hbar/m\omega$; the uncertainty product is $(n+\half)\hbar$ | item 12 | Verified. The ground state saturates 0.9 §6.5's bound — the Gaussian, again |
| 14 | **The phase-space area is $(n+\half)h$** | item 10 and **0.8** §4.4's ellipse | Verified symbolically: $\oint p\,\dd q=2\pi E/\omega$. **Collects three promises at once** — 0.8's *"the area that Chapter 4.6 will quantise"*, 1.3 §4.4's Bohr–Sommerfeld ⚑, and 1.3's *"Three things to notice, all of which Chapter 4.6 will confirm by an exact operator calculation that uses none of this reasoning"* |
| 15 | Coherent states, briefly: $\hat a\ket\alpha=\alpha\ket\alpha$ | item 8 | A packet that does not spread, and the closest thing to a classical oscillator. Half a section; it earns its place by being the bridge to 5.3 |
| 16 | Scattering off a step and a barrier; $T+R=1$ from the current | **4.5** §5 | Use the probability current, not hand-waving. This is what 4.5 §5 was for |
| 17 | Where this goes | | **Collects 0.8's and 0.3's forward pointers by name**: one oscillator per field mode (5.3), one per string mode (7.4), and *"those quanta… are what we call particles"* |

**Interactive (one):** the ladder made operable — press $\hat a^{\dagger}$ or $\hat a$ and watch the
wavefunction climb or fall, with the energy, the classical turning points and the phase-space ellipse
drawn alongside. **Test:** the numerically diagonalised Hamiltonian's levels are equally spaced to
$10^{-10}$; the displayed $\avg{x^{2}}$ matches $(n+\half)\hbar/m\omega$ to four figures at every rung.

**⚑ permitted in 4.6:** the tunnelling measurements used for comparison (item 4); the vibrational
spectroscopy data quoted in the worked examples. **Nothing else** — every result in this chapter is
derived, and the closing brick should say so. **Two.**

---

# 4.7 · Symmetry, Commutators, and the Classical Limit

**What this chapter exists to do:** *spend* the uncertainty relation rather than re-derive it, and
then say honestly how classical mechanics emerges — including the theorem that says it cannot
emerge exactly. **This chapter carries 23 debts, the most in Part IV, and most of them can be paid
in a single sentence each, which is exactly the point.**

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | One substitution: $p=\hbar k$ |
| 2 | The general uncertainty relation, and what it is not |
| 3 | Compatible observables, and a complete set |
| 4 | The Heisenberg equation, and Ehrenfest |
| 5 | Symmetries, generators, and conserved quantities |
| 6 | The classical limit I: Hamilton–Jacobi |
| 7 | The classical limit II: WKB, and Bohr–Sommerfeld recovered |
| 8 | Why the correspondence cannot be exact |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **$\Delta x\,\Delta p\ge\hbar/2$, in one line** | **0.9** §6.4's bandwidth theorem, plus $p=\hbar k$ | **Collects six of 0.9's promises at once**, including *"All that quantum mechanics will add, in Chapter 4.7, is a single substitution: $p=\hbar k$"* and *"The bandwidth theorem → Chapter 4.7, which adds $p=\hbar k$ and nothing else."* **It must actually be one line.** If it takes a page the chapter has failed its brief |
| 2 | **$\Delta A\,\Delta B\ge\half\abs{\avg{[\hat A,\hat B]}}$** | **0.5** §1's Cauchy–Schwarz, applied to $(\hat A-\avg A)\ket\psi$ and $(\hat B-\avg B)\ket\psi$ | **Collects 0.5's four promises**, including *"Nothing is added in Chapter 4.7 except the physical meaning of the symbols."* Three lines |
| 3 | What the relation does **not** say | items 1–2 | **Collects 0.9's promise by name**: *"Measurement disturbance is a real and separate phenomenon with its own theorems, and Chapter 4.7 will keep the two apart."* It is a statement about the *spread of outcomes over an ensemble*, not about a microscope. Say so in a `warn` box |
| 4 | The dimensional consistency of every conjugate pair | **1.3** §2.1 | **Collects 1.3's promise**: *"$p_i$ is whatever pairs with $q^i$ so that $p_i\dd q^i$ has the dimensions of action"* |
| 5 | Compatible observables; the complete set of commuting observables | **0.5** §8, unchanged | **Collects 0.5's "the qualitative content of Chapter 4.7"** and hands the definition to 4.8 and 4.9 |
| 6 | **The Heisenberg equation** $\dv{\hat A}{t}=\frac{1}{\ii\hbar}[\hat A,\hat H]+\pdv{\hat A}{t}$ | **4.5** §8; **1.3** §6.1's classical version, term by term | **Collects 1.3's "the bracket goes to Chapter 4.7"**. Put the two equations side by side; the only difference is which bracket |
| 7 | **Ehrenfest:** $\dv{\avg{\hat x}}{t}=\frac{\avg{\hat p}}{m}$, $\dv{\avg{\hat p}}{t}=-\avg{\nabla V}$ | item 6 | Verified numerically. **Collects 1.1's promise by name**, including 1.1's own warning that *"read carefully that is not a fundamental law but a derived statement about expectation values"*. Then the crucial caveat: $\avg{\nabla V}\ne\nabla V(\avg x)$ unless $V$ is at most quadratic — which is why the oscillator is exactly classical in the mean and nothing else is |
| 8 | Symmetry $\Rightarrow$ unitary $\Rightarrow$ conserved observable | **1.4** §7; **0.5** §7 | **Collects 1.3's "The generators of §7 go to… Chapter 4.2 (observables generate unitaries)"** — note the reassignment: 4.2 states it, 4.7 proves it. Give translation, rotation and time as the three cases, as 1.4 §3 did |
| 9 | **Hamilton–Jacobi as the $\hbar\to0$ limit** | substitute $\psi=\ee^{\ii S/\hbar}$ into 4.5's equation | Verified symbolically: the exact result is $\partial_tS+\frac{(\partial_xS)^{2}}{2m}+V=\frac{\ii\hbar}{2m}\partial_x^{2}S$, and the right-hand side is the entire quantum content. **Collects 1.3 §8.2's ⚑ by name** — *"Hamilton–Jacobi goes to Chapter 4.7 as the classical limit of the Schrödinger equation — the last stop before the wavefunction"* |
| 10 | Reading the two real equations: Hamilton–Jacobi plus the continuity equation | split item 9 into $\abs\psi$ and phase | The phase is the classical action over $\hbar$, exactly as 1.3 promised. And the amplitude equation is **4.5** §5's current again |
| 11 | **WKB**, and the $\hbar$ in which it is an expansion | item 9, expanded in powers of $\hbar$ | Say what the small parameter really is: $\lambda$ varying slowly compared with itself, not "$\hbar$ small" |
| 12 | ⚑ **The connection formulae**, with hypotheses | ⚑: a linear turning point, isolated, with the Airy asymptotics — which need the stationary-phase method **5.4** builds | Flag it, name 5.4, and then discharge it numerically in item 13 |
| 13 | **Bohr–Sommerfeld $\oint p\,\dd q=(n+\half)h$, recovered — and tested** | items 11–12 | Verified. **Exact** for the oscillator, which is why 1.3 §4.4's semiclassical guess was right. For $V=x^{4}/4$: $18\%$ error at $n=0$, $1.3\%$ at $n=1$, $0.17\%$ at $n=4$. For $V=\abs x$: $9.5\%$ at $n=0$, $0.13\%$ at $n=4$. **Print the table.** It shows exactly what "semiclassical" means, and it collects 1.3's and 0.8's Bohr–Sommerfeld ⚑ from the other side |
| 14 | **Groenewold–van Hove: the correspondence cannot be exact** | ⚑ the general theorem, with hypotheses; **build the obstruction** | Verified. Classically $q^{2}p^{2}=\frac19\{q^{3},p^{3}\}=\frac13\{q^{2}p,qp^{2}\}$, so any quantisation respecting brackets must give the same operator both ways. With Weyl ordering the two routes differ by exactly $\tfrac13\hbar^{2}\hat I$. **Compute it, on the page.** ⚑ only the statement that no ordering rule whatsoever repairs it. **Collects 1.3's ⚑ for the third time** |
| 15 | What survives: the bracket correspondence to leading order in $\hbar$ | item 14 | So P6 is safe, and "canonical quantisation" is a procedure for a restricted class of observables, not a functor. Say it |

**Interactive (one):** WKB levels against exact levels for a potential the reader shapes, with
$\hbar$ on a slider. **Test:** for the oscillator the two agree to $10^{-6}$ at every $\hbar$; for
$V=x^{4}/4$ the relative error falls like $n^{-1}$ and matches the table in item 13 to two figures.

**⚑ permitted in 4.7:** the WKB connection formulae, with hypotheses, naming 5.4 (item 12); the
general Groenewold–van Hove no-go, with the concrete obstruction built rather than quoted (item 14);
the Stone–von Neumann theorem if it is cited again (cite 4.5, do not re-flag). **Nothing else.**
**Two, plus one citation.**

---

# 4.8 · Angular Momentum and Spin

**What this chapter exists to do:** build the reader's first Lie algebra from a commutator they can
compute, and find a representation with no classical counterpart at all.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The commutator, computed |
| 2 | What the algebra alone forces |
| 3 | Why $2j$ must be a whole number |
| 4 | The matrices for $j=\half$ and $j=1$ |
| 5 | Orbital angular momentum, and the spherical harmonics |
| 6 | Spin: the representation with no wavefunction |
| 7 | Turning a spinor through $720^{\circ}$ |
| 8 | Adding angular momenta |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | **$[\hat L_i,\hat L_j]=\ii\hbar\epsilon_{ijk}\hat L_k$** | $\hat{\vv L}=\hat{\vv r}\times\hat{\vv p}$ and P6 (**4.2** §8) | Verified. **Collects 1.3's and 1.4's five promises**, including 1.3's Problem 2 (*"say what both results become in Chapter 4.8"*) and 1.4's *"Chapter 4.8 finds the identical relation with commutators in place of brackets… and derives the entire quantum theory of angular momentum — including half-integer spin, which has no classical counterpart — from nothing but that algebra."* **The word "nothing but" is a contract: nothing else may be used in §§2–4** |
| 2 | $[\hat{\vv L}^{2},\hat L_z]=0$ | item 1 | Verified. So $\hat{\vv L}^{2}$ and $\hat L_z$ are a complete set for the algebra — **4.7** §3's definition, used |
| 3 | The **notation decision**, flagged in place | Conventions | $m_\ell$, $m_s$, $m_j$ — never a bare $m$, which is mass. Flag it here in a `warn` box, as 2.6 §2 flags the rapidity clash |
| 4 | $\hat J_\pm=\hat J_x\pm\ii\hat J_y$; $[\hat J_z,\hat J_\pm]=\pm\hbar\hat J_\pm$ | item 1 | **The same ladder move as 4.6 §5.** Say so explicitly — it is the second of three appearances and the reader should feel the pattern |
| 5 | $\hat J_\mp\hat J_\pm=\hat{\vv J}^{2}-\hat J_z^{2}\mp\hbar\hat J_z$ | item 4 | The identity that closes the ladder at both ends |
| 6 | **The ladder terminates at both ends** | $\norm{\hat J_\pm\ket{jm_j}}^{2}\ge0$ with item 5 | Same argument as 4.6 §5. Positivity of a norm, twice |
| 7 | **$2j$ is a non-negative integer; $m_j=-j,\dots,j$; $\hat{\vv J}^{2}=j(j+1)\hbar^{2}$; the multiplet has $2j+1$ states** | items 5–6: top and bottom must be joined by a whole number of steps | Verified for $j=\half,1,\tfrac32,2,\tfrac52$. **This is the chapter's theorem and it must be derived, not asserted.** Collects 1.3's promise that *"its magnitude takes the values $\sqrt{j(j+1)}\hbar$, that $j$ can be a half-integer, and hence that spin exists"* |
| 8 | Matrix elements $\hat J_\pm\ket{j,m_j}=\hbar\sqrt{j(j+1)-m_j(m_j\pm1)}\ket{j,m_j\pm1}$ | item 5 | Verified. Write out $j=\half$ (the Pauli matrices) and $j=1$ |
| 9 | **The Pauli matrices are $\hat{\vv S}=\tfrac\hbar2\vec\sigma$** | item 8 at $j=\half$ | And note that **0.5** WE2 already computed $\ee^{\ii\theta\sigma_x}$. **Collects 0.5's promise by name**: *"In Chapter 4.8, $\ee^{-\ii\theta\,\hat n\cdot\vec\sigma/2}$ is precisely the operator that rotates a spin-$\tfrac12$ state"* |
| 10 | **Orbital $\ell$ must be an integer** — the algebra does not know that | require single-valuedness of $\psi$ in $\varphi$ | The sharpest sentence available here: **the algebra permits half-integers and orbital motion does not realise them.** So the half-integer representations must belong to something with no wavefunction |
| 11 | **Spherical harmonics from the top state, by algebra** | solve $\hat L_+Y_\ell^{\ell}=0$: a **first-order** equation giving $Y_\ell^{\ell}\propto\sin^{\ell}\theta\,\ee^{\ii\ell\varphi}$, then lower with $\hat L_-$ | Verified symbolically for $\ell=0,1,2,3$: $\hat L_+Y_\ell^\ell=0$, $\hat L_zY_\ell^\ell=\ell\hbar Y_\ell^\ell$, $\hat{\vv L}^{2}Y_\ell^\ell=\ell(\ell+1)\hbar^{2}Y_\ell^\ell$; and lowering reproduces the standard $Y_\ell^{m_\ell}$ up to normalisation, checked to $\ell=2$. **No Legendre series anywhere.** `PLAN-FORWARD.md` §3.1's decision, executed, and it is the reason 4.9 fits in one chapter |
| 12 | Orthonormality and completeness of $\{Y_\ell^{m_\ell}\}$ on the sphere | cite **4.4** §7 | Do not re-prove |
| 13 | **E1: spin exists, and the electron has $j=\half$** | ⚑ experimental: Stern–Gerlach; the fine-structure doubling; the anomalous Zeeman effect | Announced in its own box per pacing item 9. Note that this is the one place in Part IV where nature chooses among possibilities the mathematics offered |
| 14 | ⚑ $g_e\approx2$ | ⚑ experimental here | **Name the three-stage debt in place:** measured here, derived from the Dirac equation in **5.5**, corrected to $g/2=1.00115965\ldots$ in **5.10**. A reader who is told the schedule will notice when it is kept |
| 15 | **A $360^{\circ}$ rotation multiplies a spin-$\half$ state by $-1$; $720^{\circ}$ returns it** | $\ee^{-\ii\theta\hat n\cdot\vec\sigma/2}=\cos\tfrac\theta2-\ii\sin\tfrac\theta2\,\hat n\cdot\vec\sigma$ | Verified: $\ee^{-\ii2\pi\hat J_z/\hbar}=-\hat I$ for $j=\half$ and $+\hat I$ for $j=1$. **Collects 0.5's "already visible coming"**. Then say what is and is not observable: the sign is invisible on its own state and visible in interference — ⚑ the neutron-interferometry measurement |
| 16 | Adding two angular momenta: $\hat{\vv J}=\hat{\vv J}_1+\hat{\vv J}_2$ satisfies item 1 | direct computation | One line, and it is why the whole apparatus applies again |
| 17 | **$j_1\otimes j_2=\bigoplus_{j=\abs{j_1-j_2}}^{j_1+j_2}j$**, with the dimension check | count $m$ values with multiplicity and peel off multiplets from the top | Verified: $\sum_j(2j+1)=(2j_1+1)(2j_2+1)$. Do $\half\otimes\half=0\oplus1$ in full — the singlet and triplet, which 4.11 needs |
| 18 | Clebsch–Gordan coefficients for the cases used | item 8's ladder, applied inside a fixed $j$ | ⚑ the general tables; derive $\half\otimes\half$ and $\ell\otimes\half$, which are the only two the book spends (4.10 §5, 4.11 §8) |
| 19 | $\hat{\vv L}\cdot\hat{\vv S}=\half(\hat{\vv J}^{2}-\hat{\vv L}^{2}-\hat{\vv S}^{2})$ | item 16 squared | Verified: $\tfrac{\hbar^{2}}2[j(j+1)-\ell(\ell+1)-\tfrac34]$, giving $\ell\hbar^{2}/2$ for $j=\ell+\half$ and $-(\ell+1)\hbar^{2}/2$ for $j=\ell-\half$. **Handed forward to 4.10 §5 explicitly** |
| 20 | Forward pointer to **6.1** and **6.2** | | This algebra is $\mathfrak{su}(2)$, and 6.1 will notice that boosts, rotations, $\ee^{\ii A}$ and Poisson generators were all the same structure. **Collects 3.9's line** that *"the $\mathfrak{su}(2)$ of Chapter 4.8 is the algebra §1.1 of this chapter used to state isotropy"* |

**Interactive (one):** a spin-$\half$ state on the Bloch sphere with a rotation angle the reader
drives past $360^{\circ}$, showing **the state's position and its amplitude's phase separately** —
the sphere returns at $360^{\circ}$ and the phase does not. **Test:**
$\avg{\psi_0|\psi(\theta)}=\cos(\theta/2)$ exactly, reading $-1$ at $360^{\circ}$ and $+1$ at
$720^{\circ}$, with the interference readout changing sign accordingly.

**⚑ permitted in 4.8:** E1, the experimental input that the electron carries $j=\half$ (item 13);
$g_e\approx2$, with 5.5 and 5.10 named (item 14); the neutron-interferometry measurement of the
$4\pi$ periodicity (item 15); the general Clebsch–Gordan tables, with the two cases used derived
(item 18). **Nothing else.** **Four.**

---

# 4.9 · The Hydrogen Atom

**What this chapter exists to do:** solve the one system whose exact solution built the subject —
and then explain a degeneracy nobody asked for, which is the quantum shadow of a closed classical
orbit.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Two bodies become one |
| 2 | Separation, and why the angular part is already finished |
| 3 | The radial equation |
| 4 | Factorising it: the ladder, a third time |
| 5 | The spectrum, and the number that started the subject |
| 6 | The degeneracy, and one factor too many |
| 7 | The Runge–Lenz vector, quantised |
| 8 | $SO(4)$, and the accident explained |
| 9 | Worked examples |
| 10 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | Reduced mass $\mu=m_em_p/(m_e+m_p)$ | **1.1** §6, unchanged | And the number: it moves $-13.6057$ eV to $-13.5983$ eV, a shift of $7.4$ meV, which is measurable. Say which of the two numbers is which |
| 2 | Separation of variables; the angular factor **is 4.8's** | **4.8** §5 | **The ordering argument, made visible.** One sentence: separating the angular part *is* the representation theory of $\mathfrak{su}(2)$, which is why 4.8 comes first. Under `PLAN.md`'s old ordering this chapter would have had to assert its own prerequisite |
| 3 | The radial equation for $u=rR$ | item 2 | With the effective potential $-\frac{e^{2}}{4\pi\epsilon_0 r}+\frac{\hbar^{2}\ell(\ell+1)}{2\mu r^{2}}$ — **written as $-\alpha\hbar c/r+\ldots$** per Conventions |
| 4 | The boundary condition at the origin, argued not assumed | **4.4** §5 | $u(0)=0$ is a self-adjointness requirement, not a convenience |
| 5 | **The factorisation** $\hat A_\ell=\dv{}{r}+\frac{\ell+1}{r}-\frac{1}{(\ell+1)a}$ | the same move as **4.6** §5 and **4.8** §4 | Verified symbolically: $\frac{\hbar^{2}}{2\mu}\hat A_\ell\hat A_\ell^{\dagger}=\hat H_\ell-E_{\ell+1}$ and $\frac{\hbar^{2}}{2\mu}\hat A_\ell^{\dagger}\hat A_\ell=\hat H_{\ell+1}-E_{\ell+1}$. **The third and last appearance of the ladder. Name it as such** |
| 6 | **$\hat H_\ell\ge E_{\ell+1}$, with equality iff $\hat A_\ell^{\dagger}u=0$** | item 5 and positivity of a norm — the same step as 4.6 §5 and 4.8 §2 | Gives $u\propto r^{\ell+1}\ee^{-r/(\ell+1)a}$ directly, from a first-order equation |
| 7 | **The intertwining $\hat H_{\ell+1}\hat A_\ell^{\dagger}=\hat A_\ell^{\dagger}\hat H_\ell$** | item 5 | Verified. So every level of $\hat H_{\ell+1}$ is a level of $\hat H_\ell$: **the $\ell$-channels share their spectra, and the energy cannot depend on $\ell$.** This is the algebraic statement of the degeneracy and it arrives before the group theory |
| 8 | **$E_n=-\dfrac{\mu(\alpha c)^{2}}{2n^{2}}=-\dfrac{13.606\ \mathrm{eV}}{n^{2}}$**, $n=\ell+1,\ell+2,\dots$, hence $\ell\le n-1$ | items 6–7 | Verified numerically by integrating the radial equation for $\ell=0,1,2,3$. **Collects 0.4's promise** that *"the same eigenvalue machinery solves a coupled-oscillator problem in Chapter 0.8 and a hydrogen atom in Chapter 4.9"*, and 4.1 item 17's empirical Rydberg formula |
| 9 | $a_0=\hbar/(\alpha m_ec)=52.918$ pm; $v_1/c=\alpha$ | item 8 | **The sentence 4.10 needs:** hydrogen is a system that is relativistic at the $1\%$ level, so corrections of relative order $\alpha^{2}=5.3\times10^{-5}$ are expected. **Collects 0.3's promise** that *"in hydrogen the electron's typical speed is $v\approx\alpha c$ (Chapter 4.9)"* |
| 10 | The radial functions and their nodes; $\avg r_{n\ell}=\frac{a_0}{2}(3n^{2}-\ell(\ell+1))$ | item 6, laddered | Verified symbolically for seven $(n,\ell)$ pairs. Note that $\avg r$ *does* depend on $\ell$ while $E$ does not — which sharpens the puzzle |
| 11 | **The degeneracy is $\sum_{\ell=0}^{n-1}(2\ell+1)=n^{2}$** | item 8 and **4.8** §7 | Verified. Derive the sum, do not quote it. With spin, $2n^{2}$ — and the periodic table's $2,8,18,32$ |
| 12 | **The puzzle stated sharply** | items 10–11 | Rotational symmetry explains the $(2\ell+1)$ and nothing else. Degeneracy across different $\ell$ needs a symmetry that is not rotation. **0.5 predicted this**: *"a degenerate energy level is one where the Hamiltonian alone does not tell you which state you are in"* |
| 13 | **The quantum Runge–Lenz vector** $\hat{\vv A}=\frac{1}{2\mu}(\hat{\vv p}\times\hat{\vv L}-\hat{\vv L}\times\hat{\vv p})-\dfrac{\alpha\hbar c}{r}\hat{\vv r}$ | **1.4** WE2's classical LRL vector, symmetrised | Say why the symmetrisation is needed — $\hat{\vv p}$ and $\hat{\vv L}$ do not commute — and that this is the first time in the book operator ordering has cost anything |
| 14 | **$[\hat H,\hat A_i]=0$; $\hat{\vv A}\cdot\hat{\vv L}=\hat{\vv L}\cdot\hat{\vv A}=0$; $\hat A^{2}=\frac{2\hat H}{\mu}(\hat{\vv L}^{2}+\hbar^{2})+(\alpha\hbar c)^{2}$** | item 13, computed | **All three verified symbolically.** Grind box for the algebra, statements outside. The middle one is why $\hat{\vv A}$ adds only two new labels, not three |
| 15 | **$[\hat L_i,\hat A_j]=\ii\hbar\epsilon_{ijk}\hat A_k$; $[\hat A_i,\hat A_j]=-\ii\hbar\frac{2\hat H}{\mu}\epsilon_{ijk}\hat L_k$** | item 13, computed | **Both verified symbolically.** The second is the one that matters: the commutator of two Runge–Lenz components is an angular momentum, *with a coefficient that depends on the energy* |
| 16 | **On a bound level, $\hat{\vv D}=\sqrt{-\mu/2\hat H}\,\hat{\vv A}$ closes $\mathfrak{so}(4)$** | item 15 with $\hat H<0$ | The rescaling is legitimate on a fixed eigenspace and illegitimate off it — say so, and say that this is why the argument gives the bound states and not the continuum |
| 17 | **$\hat{\vv I}=\half(\hat{\vv L}+\hat{\vv D})$, $\hat{\vv K}=\half(\hat{\vv L}-\hat{\vv D})$ are two commuting $\mathfrak{su}(2)$s** | item 16 | And $\hat{\vv I}^{2}=\hat{\vv K}^{2}$ because $\hat{\vv L}\cdot\hat{\vv D}=0$ — so one label $j$, not two |
| 18 | **$E=-\dfrac{\mu(\alpha c)^{2}}{2\hbar^{2}(2j+1)^{2}}$, so $n=2j+1$ — and the degeneracy is $(2j+1)^{2}=n^{2}$** | items 14, 17 | Verified symbolically. **The spectrum a second time, by pure algebra, with the degeneracy falling out as a dimension count.** Per `MATHPLAN-3.md` §0 item 8: two derivations of the important result, one showing where it comes from and one showing why it had to be that |
| 19 | $\ell$ runs $0\ldots n-1$ because $j\otimes j$ contains $\ell=0,\ldots,2j$ | **4.8** §8 | The range of $\ell$, recovered from representation theory. Nothing left unexplained |
| 20 | **The classical shadow** | **1.4** WE2 | The Runge–Lenz vector is conserved because the Kepler orbit closes; the extra degeneracy is that conservation law after quantisation. **Collects 1.4's ⚑ verbatim: *"And the payoff arrives in Chapter 4.9."*** Strike that flag in the same commit |
| 21 | What the model leaves out, listed honestly | | Fine structure (**4.10**), the Lamb shift (⚑, partly **5.10**), hyperfine structure (⚑), the proton's finite size (⚑). Give the size of each so the reader knows the accuracy of what they have derived |

**Interactive (one):** the orbital $\abs{\psi_{n\ell m_\ell}}^{2}$ in a cut plane with $n$, $\ell$,
$m_\ell$ selectors, beside a level diagram whose degeneracies are drawn as stacked states.
**Test:** the displayed $\avg r$ matches $\frac{a_0}{2}(3n^{2}-\ell(\ell+1))$ to three figures; the
level diagram's multiplicity at level $n$ counts $n^{2}$; the radial node count is $n-\ell-1$.

**⚑ permitted in 4.9:** the completeness of the bound states **together with the continuum**, cited
from 4.4 and flagged where the scattering states are named; the Lamb shift, hyperfine structure and
the proton radius (item 21), each with its size; the measured $R_\infty$ used for comparison.
**Nothing else** — the spectrum is derived twice and the degeneracy is explained. **Four.**

---

# 4.10 · Perturbation Theory and Transitions

**What this chapter exists to do:** build the approximation scheme the rest of the book runs on, in
the one setting where it can be checked exactly — and then say honestly that the series does not
converge.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | The setup, and what the small parameter is |
| 2 | First and second order |
| 3 | Degeneracy, and why the naive formula explodes |
| 4 | Fine structure I: the $p^{4}$ term |
| 5 | Fine structure II: spin–orbit, and the factor of two from Chapter 2.2 |
| 6 | Fine structure III: the Darwin term, and what it is waiting for |
| 7 | The variational principle |
| 8 | Time-dependent perturbation, and the interaction picture |
| 9 | Fermi's golden rule |
| 10 | The series does not converge |
| 11 | Worked examples |
| 12 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | $\hat H=\hat H_0+\lambda\hat V$, and the expansion in $\lambda$ | **0.3** §4's asymptotic series | State at the outset that $\lambda$ is a bookkeeping device and the real small parameter is $\abs{V_{ab}}/\Delta E$. Item 15 comes back to this |
| 2 | **$E_a^{(1)}=V_{aa}$** | expand and project onto $\ket a$ | Verified numerically |
| 3 | $\ket{a}^{(1)}=\sum_{b\ne a}\dfrac{V_{ba}}{E_a-E_b}\ket b$ | project onto $\ket b$ | Verified: overlap with the exact eigenvector is $1$ to ten decimal places at $\lambda=10^{-5}$ |
| 4 | **$E_a^{(2)}=\sum_{b\ne a}\dfrac{\abs{V_{ab}}^{2}}{E_a-E_b}$** | item 3 | Verified: the residual against exact diagonalisation scales as $\lambda^{3}$ over three decades. **The ground state always moves down** — say why, and note this is the same fact that makes the van der Waals force attractive |
| 5 | **Degenerate perturbation theory: diagonalise $\hat V$ inside the degenerate subspace** | items 3–4 break; **0.5** §6 applied to the block | Verified. **Collects 0.5's promise**: *"why 'lifting a degeneracy' — with a magnetic field, say — is such a common experimental move"*. And say what the right zeroth-order states are: the ones $\hat V$ chooses, not the ones you brought |
| 6 | **$\hat H_{\text{rel}}=-\hat p^{4}/8m^{3}c^{2}$** | **2.5** §3.1's expansion of $\sqrt{p^{2}c^{2}+m^{2}c^{4}}$, third term | **Collects 0.3 WE2 and 2.5 §3.3 by name** — 2.5 wrote *"Chapter 4.10 computes the full splitting; the point here is that the leading piece of it is a term in [the expansion] and nothing more exotic"* |
| 7 | **$\avg{\hat H_{\text{rel}}}=-\dfrac{E_n^{2}}{2mc^{2}}\Big(\dfrac{4n}{\ell+\half}-3\Big)$** | rewrite $\hat p^{4}=[2m(\hat H_0-V)]^{2}$ — the trick that avoids a fourth derivative — with $\avg{1/r}$ and $\avg{1/r^{2}}$ | Verified symbolically for five $(n,\ell)$ pairs against the closed form, using $\avg{1/r}=1/n^{2}a_0$ and $\avg{1/r^{2}}=1/[(\ell+\half)n^{3}a_0^{2}]$ (both verified). **The number: $-9.06\times10^{-4}$ eV for the ground state**, against 2.5's estimate of $\alpha^{2}\times13.6=7.2\times10^{-4}$ eV. Say that the estimate was right |
| 8 | The spin–orbit term $\dfrac{1}{2m^{2}c^{2}}\dfrac1r\dv{V}{r}\hat{\vv L}\cdot\hat{\vv S}$, **including the factor of $\half$** | the electron-frame field, **then** Thomas | **Derive the naive term first and get it wrong by two.** Then take the $\half$ from **2.2**'s boxed result $M=\exp(\phi_2K_y+\phi_1K_x+\tfrac12\phi_1\phi_2J_z+\cdots)$ — verified numerically: the $J_z$ coefficient of $\log(\ee^{\phi_2K_y}\ee^{\phi_1K_x})$ is $\tfrac12\phi_1\phi_2$ to ten figures. **Collects 2.2's promise verbatim**: *"this contributes a factor of $\tfrac12$ to the spin–orbit coupling in atomic fine structure. Without it, the predicted fine-structure splitting is wrong by a factor of two."* The ⚑ stays where 2.2 put it, on BCH; **no new flag** |
| 9 | $\avg{\hat{\vv L}\cdot\hat{\vv S}}$, and why $\ket{n\ell jm_j}$ is the right basis | **4.8** §8's $\hat{\vv L}\cdot\hat{\vv S}=\half(\hat{\vv J}^{2}-\hat{\vv L}^{2}-\hat{\vv S}^{2})$ | Degenerate perturbation theory choosing its own basis — item 5, in action, on the case that matters |
| 10 | ⚑ **The Darwin term** $\dfrac{\hbar^{2}}{8m^{2}c^{2}}\nabla^{2}V$ | ⚑ its coefficient, with the Zitterbewegung smearing given **explicitly as a heuristic and labelled as one** | It affects $\ell=0$ only. Name **5.5**: the Dirac equation produces all three terms at once, and that is the right way to see it |
| 11 | **$E_{n,j}=E_n\Big[1+\dfrac{\alpha^{2}}{n^{2}}\Big(\dfrac{n}{j+\half}-\dfrac34\Big)\Big]$** — the three terms combining into one that depends on $j$, not $\ell$ | items 7, 9, 10 | Verified. **The $2p_{3/2}$–$2p_{1/2}$ interval comes out $4.528\times10^{-5}$ eV $=10.949$ GHz against a measured $10.969$ GHz** — a $0.2\%$ residual which is the QED correction, ⚑ and named for 5.10. **Print both numbers.** This is the best "how good is it, and what is missing" moment in Part IV |
| 12 | The variational principle: $\avg{\hat H}\ge E_0$ for any trial state | **4.4** §7's spectral decomposition | Two lines. Then use it: a Gaussian trial on hydrogen gets $-11.5$ eV, and the reader sees a bound that is honest rather than lucky |
| 13 | The interaction picture and the Dyson series | items 1–4 in time; **1.3** §6.1 | **The survival-function identity, made explicit**: $S(t)=\exp\!\big(-\!\int_0^th\big)$ and the Dyson series are the same object, and **time-ordering is the only new ingredient**. `PLAN-FORWARD.md` §5.1(c)'s Familiar Ground row, landed. When 5.8 meets this again it must be a recognition |
| 14 | **Fermi's golden rule** $\Gamma=\frac{2\pi}{\hbar}\abs{V_{fi}}^{2}\rho(E_f)$ | first order in time; the $\sin^{2}$ kernel becoming $2\pi t\,\delta$ | Verified: $\int\frac{\sin^{2}(\Delta t/2)}{(\Delta/2)^{2}}\dd\Delta=2\pi t$ exactly (**0.9** §5's delta, used). Then **check it numerically**: a two-level system integrated exactly gives $0.970$ of the first-order prediction at $Vt/2=0.3$, which is exactly $\sin^{2}(0.3)/0.3^{2}$; and integrating over detuning reproduces the linear-in-$t$ rate to $0.6\%$. **Say what "linear in $t$" requires**: a continuum, and a time long compared with $1/\Delta E$ and short compared with the lifetime |
| 15 | **The series is asymptotic, not convergent** | **0.3** §4 | Verified. For $\hat H=\half(\hat p^{2}+\hat x^{2})+\lambda\hat x^{4}$ the coefficients are $\tfrac12,\tfrac34,-\tfrac{21}8,\tfrac{333}{16},-\tfrac{30885}{128},\ldots$ with $\abs{E_{n+1}/E_n}$ growing linearly in $n$ — factorial growth, zero radius of convergence. **And Dyson's argument, in miniature and completely accessible: for $\lambda<0$ the potential is unbounded below, so there is no ground state at all, so $E(\lambda)$ cannot be analytic at $\lambda=0$.** Show optimal truncation: at $\lambda=0.01$ the best is order 11 and gives $2\times10^{-11}$; at $\lambda=0.2$ the best is **order 1**. `GAPS.md` G12 pre-paid, and 5.11's shock set up |
| 16 | ⚑ **The adiabatic theorem**, with hypotheses | ⚑: a spectral gap that does not close, and evolution slow compared with $\hbar/\Delta E^{2}$ | **Collects 1.3's promise by name**: *"The modern statement is Chapter 4.10's adiabatic theorem: a quantum system stays in the $n$-th eigenstate under slow change, which is the same sentence with $J$ replaced by $n$"* — the quantum version of the adiabatic invariant. Per pacing item 10 the gap condition is stated, not waved at. Mention the Berry phase in one sentence and ⚑ it |

**Interactive (one):** a driven two-level system, exactly integrated, with drive strength and
detuning on sliders, plotted against the first-order prediction — so the reader can watch
perturbation theory work and then watch it fail. **Test:** at $Vt/2=0.3$ the ratio of exact to
first-order reads $0.970$; the exact curve returns to $P=1$ at the Rabi time while the first-order
curve passes $1$ and keeps going, visibly.

**⚑ permitted in 4.10:** the Darwin term's coefficient, with the heuristic labelled and 5.5 named
(item 10); the QED residual in the fine-structure interval, naming 5.10 (item 11); the adiabatic
theorem with its gap hypothesis (item 16); the Berry phase (item 16); the Bender–Wu asymptotic form
of the coefficients — the *divergence* is derived by Dyson's argument, only the growth *rate* is
quoted (item 15); the measured fine-structure interval. **Nothing else** — and specifically **not**
the Thomas factor, which is derived from 2.2. **Six.**

---

# 4.11 · Identical Particles, Entanglement, and Measurement

**What this chapter exists to do:** show what quantum mechanics says about *two* things, which is
where all the strangeness lives — and close Part IV by saying precisely what has and has not been
explained.

**Sections (fixed):**

| § | Title |
|---|---|
| 1 | Two particles |
| 2 | Identical, and what that costs |
| 3 | The symmetrisation postulate |
| 4 | Exchange, which is not a force |
| 5 | Occupation numbers, and the Planck law a second time |
| 6 | Density matrices, and the state of a part |
| 7 | Entanglement, stated precisely |
| 8 | Bell's inequality, derived and violated |
| 9 | What is settled, and what is not |
| 10 | Worked examples |
| 11 | Your turn |

### The numbered build

| # | Built | From | Note |
|---|---|---|---|
| 1 | The two-particle space $\mathcal H_1\otimes\mathcal H_2$; product states and the rest | P7 (**4.2** §9); **0.4** §2 | Count dimensions and note immediately that most states are not products. That single count is the chapter |
| 2 | The exchange operator $\hat P_{12}$; $\hat P_{12}^{2}=\hat I$, so eigenvalues $\pm1$ | item 1 | Derived. The two possibilities are forced by an algebraic fact, and only the *choice between them* is postulated |
| 3 | **P8 — symmetrisation** | ⚑ postulate box | And say exactly what is not being claimed: **which** sign goes with which spin is **not** derived here. ⚑ spin–statistics, naming **5.5**, and state the two computations 5.5 will do — a Dirac field quantised with commutators has a Hamiltonian unbounded below; a scalar quantised with anticommutators fails to commute at spacelike separation |
| 4 | Slater determinants; **the Pauli principle as a corollary, not a postulate** | items 2–3 | Two fermions in the same state give a vanishing vector. Derived in one line from P8 |
| 5 | **Exchange energy: an interaction that is not an interaction** | items 3–4 with a spin-independent Hamiltonian | Compute $\avg{(x_1-x_2)^{2}}$ for symmetric and antisymmetric states and get a difference with no term in the Hamiltonian responsible. **This is the most surprising consequence of P8 and it is a two-line calculation** |
| 6 | **Bose–Einstein and Fermi–Dirac occupation numbers** | the grand canonical sum over occupations, using **0.6** WE1's method with a second multiplier | Verified: $\avg n=1/(\ee^{\beta(\epsilon-\mu)}\mp1)$; both reduce to Boltzmann when $\ee^{\beta(\mu-\epsilon)}\ll1$. **`GAPS.md` G3's second half, closed** |
| 7 | **The Planck law, a second time** | item 6 with $\mu=0$ and **4.1** item 2's mode count | **Collect 4.1 explicitly**: the same formula, from a completely different argument, and neither used the other. Say which assumption each route made instead of the other |
| 8 | The density matrix $\hat\rho$; $\operatorname{tr}\hat\rho=1$, $\avg{\hat A}=\operatorname{tr}(\hat\rho\hat A)$ | **0.5** §1's trace inner product $\operatorname{tr}(A^{\dagger}B)$ | **Collects 0.9's promise by name**: *"Probability, variance, the CLT → Chapter 4.11 (density matrices and measurement statistics)"* |
| 9 | Pure vs mixed: $\operatorname{tr}\hat\rho^{2}=1$ or $<1$ | item 8 | And the crucial distinction the chapter turns on: a mixture is ignorance, a superposition is not |
| 10 | **The reduced density matrix**, by partial trace | items 1, 8 | Verified: for the singlet, $\hat\rho_A=\half\hat I$, $\operatorname{tr}\hat\rho_A^{2}=\half$, entropy $\ln2$. **A pure state of the pair whose parts are maximally uncertain** — that is entanglement, defined by a computation rather than a slogan |
| 11 | **The singlet's correlation $E(\hat a,\hat b)=-\cos\theta$** | **4.8** §4's Pauli matrices and §8's singlet | Verified to twelve figures at seven angles. **Do this by explicit computation with 4.8's matrices** — it is the chapter's one piece of real algebra and everything else rests on it |
| 12 | **The CHSH inequality $\abs S\le2$ for any local hidden-variable model** | four $\pm1$ assignments; $AB-AB'+A'B+A'B'=A(B-B')+A'(B+B')$, one bracket zero, the other $\pm2$ | Verified by exhaustion over all sixteen deterministic assignments: the value is always exactly $\pm2$, so any mixture obeys the bound. **State the hypotheses as pacing item 10 requires: locality, realism, and measurement independence** — and say that the last one is an assumption people do argue about |
| 13 | **Quantum mechanics gives $2\sqrt2$** | item 11 at $a=0^{\circ}$, $a'=90^{\circ}$, $b=45^{\circ}$, $b'=135^{\circ}$ | Verified: $S=-2.82842712$. **Get the angles right** — the commonly quoted $(0,90,45,-45)$ gives exactly zero with this sign convention, and the plan says so because it is the kind of slip that ships |
| 14 | **Tsirelson: quantum mechanics cannot exceed $2\sqrt2$ either** | $\hat{\mathcal B}^{2}=4\hat I+[\hat A,\hat A']\otimes[\hat B,\hat B']$ with $\norm{[\hat A,\hat A']}\le2$ | Verified: the operator identity holds exactly and the CHSH operator's eigenvalues are $\{-2\sqrt2,0,0,2\sqrt2\}$. **Derived, not flagged.** Quantum mechanics violates the classical bound and then stops at a bound of its own, and that second fact is as interesting as the first |
| 15 | ⚑ The experiments | ⚑ with hypotheses: Aspect 1982 and the 2015 loophole-free tests, with the detection and locality loopholes named and said to be closed | Per pacing item 10 |
| 16 | What no-signalling means, and why entanglement does not transmit anything | item 10: $\hat\rho_A$ is unchanged by anything done at $B$ | Compute it. This is the antidote to every popular account the reader has met |
| 17 | **Decoherence: what it explains** | build one explicit model — a two-level system coupled to $N$ environment spins — and watch the off-diagonal elements of $\hat\rho$ decay | ⚑ the general theory; build the one case. Give the timescale, and the number for a dust grain: coherence gone in $\sim10^{-31}$ s |
| 18 | **What decoherence does not explain** | item 17 against P3 | It explains why interference terms become unobservable. **It does not explain why the probabilities are $\abs\psi^{2}$, and it does not select an outcome.** `GAPS.md` G13. Say it plainly and without apology |
| 19 | **The postulate ledger, closed** | §0.1 | Reprint the table of P1–P8 and E1 with, for each, what was assumed, what was derived from it, and where (if anywhere) the assumption is discharged later — P8 in 5.5, P2's self-adjointness in 4.4, P5's half in 4.5. **Eight postulates and one measurement is what Part IV cost, against the twenty-odd theorems of Part 0 it renamed.** This is the closing brick of the part |
| 20 | The handoff to Part V | | Say what the reader now has that Part V needs: a Hilbert space, self-adjoint generators, $\mathfrak{su}(2)$, ladder operators, perturbation theory in an interaction picture, and identical particles. And say what breaks: fixed particle number, once $\Delta E\,\Delta t\gtrsim\hbar$ meets $E=mc^{2}$ |

**Interactive (one):** the CHSH experiment — four analyser angles on dials, the four correlations
and $S$ read out live, with the classical bound at $2$ and Tsirelson's at $2\sqrt2$ drawn as lines,
and a local-hidden-variable simulator running alongside. **Test:** at
$(0^{\circ},90^{\circ},45^{\circ},135^{\circ})$ the readout is $2.8284$; the quantum curve touches
$2\sqrt2$ and never exceeds it; the hidden-variable simulator over $10^{5}$ runs never exceeds $2$.

**⚑ permitted in 4.11:** P8, the symmetrisation postulate (item 3); the spin–statistics theorem,
naming 5.5 and stating its two computations (item 3); the Bell experiments with their loopholes
named (item 15); the general theory of decoherence, with one model built (item 17); the Born rule
and the measurement problem, restated as permanently open and labelled as the second kind of flag
(item 18). **Nothing else** — Tsirelson is derived and the CHSH bound is derived. **Five.**

---

## ⚑ budget for the part

| Ch | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 | 4.10 | 4.11 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ⚑ | 7 | 10 | 2 | 5 | 4 | 2 | 2 | 4 | 4 | 6 | 5 | **51** |

Of the 51, **eight are postulate boxes** (P1–P7 in 4.2, P8 in 4.11), **about a third are
experimental inputs**, and **exactly one is the substantial mathematical flag of the part** — the
spectral theorem for unbounded self-adjoint operators, discharged into three explicit verifications
in 4.4 §8. For comparison, Part III carries 29 flags across 6 chapters and Part II 54 across 6. A
count in the
fifties across eleven chapters, with the postulates marked, is the honest number.

**What Part IV closes in `GAPS.md`:** **G1** entirely (three promises in 4.3, four in 4.4, with the
residual flag verified three times); **G3** entirely (mode counting and Planck in 4.1, occupation
numbers in 4.11); **G12** in part (the divergence derived in 4.10 §10, leaving only 5.11's QED
instance). **What Part IV explicitly declines:** **G2** — no complex analysis, anywhere; **G4** —
the fundamental theorem of algebra is re-flagged in 4.2's closing brick and left for 5.4;
**G5** — constrained Hamiltonian systems are not Part IV's and are not mentioned; **G11** — the
specific gap 0.9 named is
closed in 4.4 §10, the general theory is 5.4's, and 4.4 must say which it is doing.

---

## What this part must not do

- **Not re-derive Part 0.** Not Cauchy–Schwarz, not the uncertainty relation, not the finite-dimensional
  spectral theorem, not Parseval, not the Fourier transform's unitarity, not simultaneous
  diagonalisation. Every one is done, and 4.2 and 4.7 exist to *spend* them. Repeating them would
  be the one thing this book has never done.
- **Not use a contour integral, a residue, or an analytic continuation.** `GAPS.md` G2: complex
  analysis is built in 5.4 and not before. Every result in this part is reachable without it,
  including Hermite completeness (4.4 item 15), which is the one place the temptation is real.
- **Not use natural units.** $\hbar$ is written out. The switch is 5.1's.
- **Not let the Born rule seep in.** It arrives in a box, in 4.2 §5, marked, with Gleason's
  hypotheses stated, and it is named again in 4.11 §9. It is never presented as following from
  anything.
- **Not solve the oscillator or hydrogen by power series.** The ladder does both, three times over,
  and the repetition is the teaching. `PLAN-FORWARD.md` §3.1.
- **Not schedule hydrogen before angular momentum**, and not let 4.9 quietly re-derive spherical
  harmonics. 4.9 §2's one-sentence statement of *why* the order is what it is has to be in the text.
- **Not merge P3 and P4**, and not merge "Hermitian" with "self-adjoint". Both merges are standard
  and both cost the book a distinction it later needs.
- **Not treat 4.3 as a measure theory course.** No Radon–Nikodym, no $L^{p}$ duality, no Riesz
  representation beyond what 4.4 cites. The chapter's job is: the integral, the convergence
  theorems, $L^{2}$, and the Fourier basis.
- **Not let 4.11 become an interpretations essay.** Copenhagen, many-worlds and Bohm get one
  paragraph between them, named and not adjudicated, and the chapter's weight stays on the two
  calculations — the reduced density matrix and CHSH.
- **Not quote a physical constant as a product of separately measured pieces.** See Conventions.

---

## Batch order

`PLAN-FORWARD.md` §11 gives F3 = 4.1+4.2, F4 = 4.3 alone, F5 = 4.4 alone, F6 = 4.5+4.6,
F7 = 4.7+4.8, F8 = 4.9+4.10, F9 = 4.11 + reunification. **One change is recommended.**

| Batch | Contents | Note |
|---|---|---|
| F3 | 4.1 + 4.2 | The crisis, and the translation of 0.5 |
| F4 | **4.3 alone** | The 3.3 of Part IV |
| F5 | **4.4 alone** | The 3.4 of Part IV — the chapter Part 0 has been writing cheques against since 0.2 |
| F6 | 4.5 + 4.6 | |
| F7 | 4.7 + 4.8 | |
| F8 | **4.9 alone** *(changed)* | It derives one spectrum twice and carries the $\mathfrak{so}(4)$ computation. Pairing it with 4.10 was the riskiest cell in `PLAN-FORWARD.md` §11 |
| F9 | **4.10 alone** *(changed)* | Sixteen build items, three fine-structure terms, two pictures of time-dependent theory and a divergent series. It is the largest chapter in the part |
| F10 | 4.11 + Part IV reunification pass | Per `PLAIN-TERMS-PLAN.md` §7 |

Cost: one extra batch. The alternative is a 25,000-word 4.10, which is the failure mode
`PLAN-FORWARD.md` §0 identifies by measurement.

**Before F3, and not during it:** run `python3 debts.py 4.N` for every N and put the output in that
chapter's brief; confirm `build.py`'s `PARTS` list matches this plan's eleven titles (it does, as of
this writing); and check that the Part IV forward references in Parts 0–III have already been
re-aimed — spot checks confirm 0.9 §5.3 now names 4.4 and 2.5 §3.3 now names 4.10, which are the two
that moved.

---

## Verification performed while this plan was written

Everything marked *Verified* above was checked in sympy, numpy or scipy before it was written down.
Specifically:

- **Ladder algebra.** $[\hat a,\hat a^{\dagger}]=1$; $[\hat N,\hat a^{\dagger}]=\hat a^{\dagger}$;
  $\hat H=\hbar\omega(\hat N+\half)$ giving $\{0.5,1.5,2.5,\ldots\}$ exactly on a 60-state
  truncation; $\avg{x^{2}}=\avg{p^{2}}=n+\half$ and the uncertainty product $(n+\half)\hbar$.
  $\oint p\,\dd q=2\pi E/\omega$ symbolically, giving $E_n=(n+\half)\hbar\omega$ from
  $\mathcal A=(n+\half)h$.
- **$\mathfrak{su}(2)$.** $[\hat J_i,\hat J_j]=\ii\hbar\epsilon_{ijk}\hat J_k$, $\hat{\vv J}^{2}=j(j+1)$,
  $[\hat{\vv J}^{2},\hat J_z]=0$ and $\dim=2j+1$, all checked for $j=\half,1,\tfrac32,2,\tfrac52$.
  $\ee^{-\ii2\pi\hat J_z/\hbar}=-\hat I$ for $j=\half$ and $+\hat I$ for $j=1$; the $720^{\circ}$
  return; $\ee^{-\ii\theta\hat n\cdot\vec\sigma/2}=\cos\tfrac\theta2-\ii\sin\tfrac\theta2\,\hat
  n\cdot\vec\sigma$.
  Spherical harmonics from $\hat L_+Y_\ell^\ell=0$ verified for $\ell=0..3$ and the lowered states
  matched against the standard $Y_\ell^{m_\ell}$ to $\ell=2$.
- **Hydrogen.** The radial equation integrated numerically for $\ell=0,1,2,3$, reproducing
  $-1/2n^{2}$ hartree with $\ell\le n-1$; $\sum_{\ell<n}(2\ell+1)=n^{2}$; $\avg{1/r}$, $\avg{1/r^{2}}$,
  $\avg{1/r^{3}}$ and $\avg r$ against their closed forms for seven $(n,\ell)$; the radial
  factorisation $\frac{\hbar^{2}}{2\mu}\hat A\hat A^{\dagger}=\hat H_\ell-E_{\ell+1}$, its adjoint
  partner, the annihilated ground state and the intertwining relation, all symbolically.
- **Runge–Lenz.** With $\hat{\vv A}$ Pauli-symmetrised, all five identities verified symbolically on
  a general test function: $[\hat H,\hat A_i]=0$; $\hat{\vv A}\cdot\hat{\vv L}=\hat{\vv L}\cdot\hat{\vv A}=0$;
  $\hat A^{2}=\frac{2\hat H}{m}(\hat{\vv L}^{2}+\hbar^{2})+k^{2}$;
  $[\hat L_i,\hat A_j]=\ii\hbar\epsilon_{ijk}\hat A_k$;
  $[\hat A_i,\hat A_j]=-\ii\hbar\frac{2\hat H}{m}\epsilon_{ijk}\hat L_k$. The
  $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ arithmetic then gives $E=-mk^{2}/2\hbar^{2}(2j+1)^{2}$ and
  degeneracy $(2j+1)^{2}=n^{2}$.
- **Perturbation theory.** $E^{(1)}=V_{aa}$ and $E^{(2)}=\sum_{b\ne a}\abs{V_{ab}}^{2}/(E_a-E_b)$
  against exact diagonalisation of a random $8\times8$ Hermitian pair: the residual scales as
  $\lambda^{3}$ across $\lambda=10^{-2},10^{-3},10^{-4}$; the first-order eigenvector overlaps the
  exact one to ten decimals; the degenerate case matches $E_0+\lambda\,\mathrm{eig}(V|_{\text{block}})$.
- **Fine structure and $\alpha$.** $\alpha=7.2973525643\times10^{-3}$, $\alpha^{-1}=137.035999178$,
  $\alpha^{2}=5.325\times10^{-5}$; $R_\infty hc=13.605693123$ eV recovered from
  $\tfrac12\alpha^{2}m_ec^{2}$ to eleven figures; $\avg{\hat H_{\text{rel}}}$ against
  $-\frac{E_n^{2}}{2mc^{2}}(\frac{4n}{\ell+1/2}-3)$ symbolically for five states, giving
  $-9.06\times10^{-4}$ eV at $n=1$ (2.5's estimate was $7\times10^{-4}$); the full $E_{n,j}$ giving a
  $2p_{3/2}$–$2p_{1/2}$ interval of $10.949$ GHz against a measured $10.969$ GHz. The Thomas $\half$
  extracted numerically from $\log(\ee^{\phi_2K_y}\ee^{\phi_1K_x})$ to ten figures.
- **Bell/CHSH.** $E(\hat a,\hat b)=-\cos\theta$ to twelve figures; the classical bound $\pm2$ by
  exhaustion over all sixteen deterministic assignments; $\abs S=2\sqrt2=2.82842712$ at
  $(0^{\circ},90^{\circ},45^{\circ},135^{\circ})$ and confirmed as the numerical optimum over 40
  restarts; $\hat{\mathcal B}^{2}=4\hat I+[\hat A,\hat A']\otimes[\hat B,\hat B']$ exactly, with
  eigenvalues $\{-2\sqrt2,0,0,2\sqrt2\}$; $\hat\rho_A=\half\hat I$ with entropy $\ln2$.
- **4.1's numbers.** $g(\nu)=8\pi\nu^{2}/c^{3}$ symbolically from the box count; the Rayleigh–Jeans
  limit of the Planck form; $\int\nu^{2}\dd\nu$ divergent; $\nu_{\max}/T=5.8789\times10^{10}$ Hz K$^{-1}$
  from $3(1-\ee^{-x})=x$; $\int x^{3}/(\ee^{x}-1)=\pi^{4}/15$ giving $\sigma=5.670374\times10^{-8}$
  against CODATA to eight figures; Wien's $b=2.8977720\times10^{-3}$ m K; Compton's
  $\Delta\lambda=(h/mc)(1-\cos\theta)$ symbolically from four-momentum conservation.
- **4.4's cases.** Deficiency indices of $-\ii\dv{}{x}$ on $\R$, $[0,L]$ and $[0,\infty)$ as
  $(0,0)$, $(1,1)$, $(1,0)$; the box Hamiltonian's $(2,2)$ and hence $U(2)$; Robin spectra computed
  for three values of $\alpha$ and confirmed distinct; the Hermite functions' Gram matrix equal to
  the identity to $10^{-8}$ for $M=40$; Parseval reaching $1.00000000$ by $M=20$;
  $\mathcal F\hat p\mathcal F^{-1}=\hbar k$ against a finite-difference derivative to $2\times10^{-4}$
  on a 4096-point grid.
- **4.5, 4.7 and 4.10 numerics.** Split-operator evolution conserving the norm to $3.7\times10^{-13}$,
  Ehrenfest residuals at the finite-difference floor, $\avg x(t)$ tracking $2\cos t$ to
  $1.6\times10^{-6}$, and free-packet spreading matching $\sigma_0^{2}+(\hbar t/2m\sigma_0)^{2}$
  exactly. WKB against exact levels for $\tfrac12x^{2}$ (exact), $x^{4}/4$ and $\abs x$. The
  Groenewold obstruction: $\tfrac19[\hat q^{3},\hat p^{3}]/\ii$ and
  $\tfrac13[\widehat{q^{2}p},\widehat{qp^{2}}]/\ii$ differing by exactly $\tfrac13\hbar^{2}\hat I$
  under Weyl ordering. The two-level system integrated at $10^{-11}$ tolerance against first-order
  theory and against the golden rule. Bender–Wu coefficients $\tfrac12,\tfrac34,-\tfrac{21}8,
  \tfrac{333}{16},-\tfrac{30885}{128}$ reproduced exactly, with linearly growing ratios.
- **4.3's numbers.** The Gibbs constant $\frac1\pi\int_0^\pi\frac{\sin t}{t}\dd t=0.5894899$, giving
  an $8.95\%$ overshoot; $\norm{f-S_N}_2\sim0.63N^{-1/2}$ for the square wave.

**The chapters must be checked again independently after they are written**, by an agent that did
not write them, per the standing rule in `reports/README.md`. Three of the errors caught in the last
build were in a plan, not in a chapter — and two of the corrections in this document
(`PLAN-FORWARD.md` §3.1's extension count, and the CHSH angles) are of exactly that kind.

---

## Corrections to `PLAN-FORWARD.md` and `GAPS.md` found while writing this plan

Recorded here because the standing rule is that plan errors are caught in plans. Each is already
applied above; each should also be struck in the source document.

1. **`PLAN-FORWARD.md` §3.1 and §5.3: the particle in a box does *not* have "a one-parameter family
   of self-adjoint extensions".** Its Hamiltonian has deficiency indices $(2,2)$ and therefore a
   $U(2)$ — **four-real-parameter** — family. The genuine one-parameter family belongs to the
   *momentum* operator on a finite interval, $\psi(L)=\ee^{\ii\theta}\psi(0)$. Both are worth
   working and 4.4 §5 works both, in that order; but the count as written is wrong and the wrong
   count would have shipped in a chapter whose whole subject is counting extensions.

2. **`PLAN-FORWARD.md` §5.3 lists "Cauchy sequences and convergence (0.3)" as a prerequisite of 4.3.
   The book has never defined a Cauchy sequence.** `grep` across all twenty-eight written chapters
   finds the phrase nowhere; the only Cauchys present are Cauchy–Schwarz (0.5 §1), the Cauchy
   distribution (0.9 §7.5) and Cauchy's functional equation (2.2 §2). 4.3 must define it — one
   paragraph, from 0.3 §3's convergence tests — and must not cite it as built. This is a new entry
   for `GAPS.md` §5, "machinery used before it was built", except that here it was never used
   either: it was *assumed available by a plan*, which is a failure mode that register does not
   currently catch.

3. **`PLAN-FORWARD.md` §3.1 routes 1.3's canonical-quantisation promises to 4.7; they must be
   collected in 4.2.** Nine of 4.7's twenty-three debts come from 1.3, and several of them —
   *"Chapter 4.7 will take the classical structure you now own, replace observables $f(q,p)$ by
   self-adjoint operators… and make the single substitution"*, and *"In Chapter 4.7 the operator
   conjugate to position is $\hat{\vv p}=-\ii\hbar\nabla$"* — name material that 4.5, 4.6 and 4.8
   all require first. `PLAN-FORWARD.md`'s own 4.8 row already assumes the fix (it lists the
   canonical commutators as coming from **4.2**), so the plan is internally inconsistent. Resolved
   above by splitting the collection: **4.2 §8 postulates the commutator and names 1.3; 4.7 §8 takes
   up the general correspondence and proves it cannot be exact.** Both chapters must say so.

4. **`GAPS.md` G11 and the text of 0.9 §5.3 disagree about who closes the plane-wave gap.** The
   written text says *"Chapter 4.4 closes it"*; the register says 4.4 makes a partial payment and
   5.4 completes. §0.2 above resolves it by scope rather than by softening either: 4.4 closes the
   gap 0.9 actually named, 5.4 builds the general theory, and 4.4 must not claim more.

5. **`PLAN-FORWARD.md` §11's batch F8 (4.9 + 4.10) is the riskiest cell in the Part IV schedule.**
   See "Batch order" above; the recommendation is to split it, at a cost of one batch.

---

## Where I am uncertain

Recorded so these read as judgements rather than findings.

1. **4.2's flag count is a genuine judgement call.** I have decided that a postulate carries a ⚑ as
   well as its box, on the grounds that `CONVENTIONS.md` defines the mark as "used but not derived",
   which a postulate is by construction. The consequence is that 4.2 carries ten flags — more than
   any chapter outside Parts I and II — and a reader skimming `GAPS.md` will see Part IV's most
   important chapter looking like its least rigorous. The alternative is that postulate boxes are
   *instead of* flags, and `GAPS.md` grows a separate postulate register. **I recommend the flags,
   and I recommend the decision be made explicitly rather than by whoever writes 4.2 first.**

2. **Whether 4.7 can really pay 23 debts in the space allotted.** Its brief says the uncertainty
   material takes twenty minutes and the chapter's real content is the classical limit. That is
   right in principle. But nine of the debts come from 1.3, several are about canonical
   quantisation, and I have re-routed those to 4.2 §8 — which means 4.2 must carry the collection
   even though 1.3's sentences say "Chapter 4.7". Either 4.2 §8 explicitly says "1.3 promised this
   to 4.7; the commutator is needed sooner, so it is here, and 4.7 takes up the general question",
   or three sentences in 1.3 get re-aimed. **I would re-aim 1.3, but that touches written text and
   the decision is not mine.**

3. **The Darwin term is the weakest link in 4.10.** Everything else in the fine-structure section is
   derived or is a flag with a named payer. The Darwin term is a flag with a heuristic attached, and
   heuristics are exactly what this book has spent thirty chapters not doing. The alternatives are
   worse — deriving it needs the Dirac equation, and omitting it makes $E_{n,j}$ wrong for $\ell=0$.
   **My recommendation is to keep it, label the smearing argument as a heuristic in the strongest
   terms available, and give the reader the arithmetic showing that it is the term that makes the
   $j$-dependence work.** But a reviewer may reasonably think it should be quoted with no
   story at all.

4. **I am not certain 4.11 fits.** It carries symmetrisation, exchange, quantum statistics, density
   matrices, entanglement, Bell, Tsirelson, decoherence, the postulate ledger and the handoff to
   Part V. That is more distinct ideas than any other chapter in the part, and its debt count (2) is
   deceptively low. The fallback, if it runs past 20,000 words: **move items 6 and 7 (occupation
   numbers and the second derivation of the Planck law) into 4.10's worked examples**, since the
   grand canonical sum needs nothing from the rest of 4.11 except P8. I would not move Bell.

5. **The $U(2)$ correction to `PLAN-FORWARD.md` §3.1 may make 4.4 §5 harder to teach, not easier.**
   Four parameters is the truth, but "the boundary condition is a physical choice" lands more
   cleanly with the one-parameter momentum case. **My recommendation is to lead with momentum on
   $[0,L]$ (a clean $U(1)$), then give the box Hamiltonian's $U(2)$ as the richer case and work only
   the Robin sub-family.** A writing agent who leads with the box will find the parameter counting
   fighting the pedagogy.

6. **Whether 4.1 should derive the Planck law Einstein's way *only*.** `PLAN-FORWARD.md` §3.1's
   argument is sound and I have followed it. But there is a cost the plan should acknowledge: the
   A/B argument produces the *form* of the spectrum from a boundary condition supplied by the
   classical theory it is replacing, which is a slightly uncomfortable logical shape, and a sharp
   reader may notice. 4.11 item 7's second derivation is what repairs it. **If the reunification
   pass finds that 4.1 reads as circular, the repair is to make 4.1 §5 say explicitly that the
   argument is fixing two constants in a form, not deriving a law from nothing, and to point
   forward to 4.11 by name.**
