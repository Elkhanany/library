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

`python3 debts.py 4` returns **824 sentences** in the written text that name a Part IV chapter. The
per-chapter column below sums to more than that, because one sentence can name two chapters; the
column is the load on each chapter's writer, which is the number that matters when a brief is built.
**Regenerate this table after every batch.** It was accurate at 119 when written and went stale the moment
4.1, 4.2 and 4.3 were written, because those chapters cite each other and everything before them. Every row
below moved, and subtracting the three new chapters' contributions reproduces the original numbers exactly.
Every one is a requirement. Counts, and the collector:

| Ch | Debts | The heaviest creditors |
|---|---|---|
| 4.1 | 53 | ledger (27), 4.2 (12), 4.3 (6), 2.5 (5) |
| 4.2 | 140 | ledger (35), 4.6 (32), 4.4 (18), 0.5 (12) |
| 4.3 | 140 | 4.5 (58), ledger (34), 4.4 (23), 4.6 (7) |
| 4.4 | 121 | 4.5 (40), 4.7 (36), 4.6 (19), ledger (11) |
| 4.5 | 98 | 4.6 (40), ledger (15), 4.4 (14), 4.7 (10) |
| 4.6 | 83 | 4.7 (26), ledger (18), 4.2 (7), 0.7 (5) |
| 4.7 | 25 | 4.6 (15), 4.4 (3), 4.5 (2), 0.5 (1) |
| 4.8 | 40 | 0.8 (9), ledger (7), 4.6 (6), 1.3 (3) |
| 4.9 | 54 | 4.2 (10), ledger (9), 4.6 (7), 0.9 (6) |
| 4.10 | 29 | 4.6 (6), 4.7 (6), ledger (6), 4.2 (4) |
| 4.11 | 25 | 4.2 (6), ledger (6), 1.4 (3), 4.7 (3) |
| 4.12 | 12 | 1.4 (3), 4.2 (3), 4.6 (2), 0.5 (1) |
| 4.13 | 27 | 4.6 (8), 4.7 (4), 4.2 (3), 4.5 (3) |
| 4.14 | 2 | 1.4 (1), ledger (1) |
| 4.15 | 3 | 0.5 (1), 4.3 (1), ledger (1) |
| 4.16 | 6 | 4.7 (3), 4.6 (2), 2.5 (1) |
| 4.17 | 25 | 4.6 (8), 4.2 (6), 4.7 (4), ledger (3) |
| 4.18 | 16 | 4.1 (4), 4.2 (4), ledger (4), 4.7 (3) |
| 4.19 | 9 | 4.2 (5), ledger (3), 0.9 (1) |
| 4.20 | 20 | 4.2 (13), 4.6 (3), ledger (3), 0.8 (1) |

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
> **⚠ This table is on the pre-split numbering and has not been re-aimed.** The split moved every
> confirmation after 4.3: the split-operator run listed against 4.5 is the new **4.6**'s, the
> diagonalised oscillator against 4.6 is the new **4.8**'s, the WKB comparison against 4.7 is the
> new **4.10**'s, and the new 4.7 has no row at all. Take each chapter's confirmation from its own
> block below, which is current, and not from here.

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

> **Revised 26 August 2026.** Part IV was re-planned from eight unwritten chapters to seventeen, to
> cap each chapter at about six new objects. The reader, after reading 4.1–4.3: *"I value now slow
> (very slow one by one) pace than intense pace that feels like running around."* Chapters 4.1, 4.2
> and 4.3 carry twelve and thirteen objects each; the new chapters average 5.4 and none exceeds seven.
> The full reasoning, the promise triage and what the split cost are in `reports/part4-replan.md`.
> Chapters 4.1–4.3 keep their blocks below unchanged, since they are written.

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

**Sections (as written — this table was regenerated from the file after the chapter was written; the original was stale by one section for 4.5 and by three for 4.6)** (fixed — §9 is load-bearing):**

| § | Title |
|---|---|
| 1 | The half of the bill that is still unpaid |
| 2 | The spectrum, when there are no eigenvectors |
| 3 | The spectral theorem, in multiplication form |
| 4 | Checked three times |
| 5 | The Hermite functions are complete |
| 6 | The projection-valued measure, and the integral that replaces the sum |
| 7 | What $\ket x$ and $\ket p$ actually mean |
| 8 | What is now safe to do |
| 9 | Stone's theorem |
| 10 | Worked examples |
| 11 | Your turn |

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

**Sections (as written — this table was regenerated from the file after the chapter was written; the original was stale by one section for 4.5 and by three for 4.6)** (fixed — §2 is load-bearing):**

| § | Title |
|---|---|
| 1 | What time evolution has to be |
| 2 | Stone, and the generator |
| 3 | The equation |
| 4 | Which operator is the generator |
| 5 | Momentum in the position representation |
| 6 | The equation as a partial differential equation |
| 7 | What the $\ii$ is doing |
| 8 | The probability current |
| 9 | Stationary states, and the time-independent equation |
| 10 | A free packet: group velocity, and spreading |
| 11 | Worked examples |
| 12 | Your turn |

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

**Sections (as written — this table was regenerated from the file after the chapter was written; the original was stale by one section for 4.5 and by three for 4.6)** (fixed):**

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
| 7 | Scattering off a step: reflection above the barrier | **4.6** §8 | A classical particle with $E>V_0$ always transmits; this one does not. **Give the number** |
| 8 | **$T+R=1$ from the probability current** | **4.6** §8 | Use the current, not hand-waving. **This is what 4.6 §8 was for**, and the flux ratio is the only honest definition of $T$ — say why $\abs{t}^{2}$ alone is wrong when the two sides have different $k$ |
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
| 8 | $\psi_n\propto(\hat a^{\dagger})^{n}\psi_0$, and these are the Hermite functions | item 7 | **Collects 0.5's promise**: *"The identical procedure with a weight $\ee^{-x^{2}}$ on the whole line produces the Hermite polynomials, which are the quantum harmonic oscillator states of Chapter 4.6."* Completeness is **cited from 4.5 §4, not re-proved** — and 4.3's closing brick says exactly this will happen, so say that it has happened |
| 9 | $\avg{\hat x^{2}}=\avg{\hat p^{2}}/m^{2}\omega^{2}=(n+\half)\hbar/m\omega$; the uncertainty product is $(n+\half)\hbar$ | item 8 | Verified. The ground state saturates 0.9 §6.5's bound — the Gaussian, again. **Note in place that the general uncertainty relation is 4.9's**, and that this is an instance computed before the theorem, which is the order the book prefers |
| 10 | **The phase-space area is $(n+\half)h$** | item 6 and **0.8** §4.4's ellipse | Verified symbolically: $\oint p\,\dd q=2\pi E/\omega$. **Collects three promises at once** — 0.8's *"the area that Chapter 4.6 will quantise"*, 1.3 §4.4's Bohr–Sommerfeld ⚑, and 1.3's *"Three things to notice, all of which Chapter 4.6 will confirm by an exact operator calculation that uses none of this reasoning"*. Say that the *general* Bohr–Sommerfeld statement is **4.10** §6 and that this chapter has done the one case where it is exact |
| 11 | Coherent states: $\hat a\ket\alpha=\alpha\ket\alpha$ | item 4 | §7. A packet that does not spread, the closest thing to a classical oscillator, and a state that is not an energy eigenstate — which is worth saying out loud after six sections of eigenstates. It earns its place by being the bridge to 5.3 |
| 12 | Where this goes | | **Collects 0.8's and 0.3's forward pointers by name**: one oscillator per field mode (5.3), one per string mode (7.4), and *"those quanta… are what we call particles"* |

**Interactive (one — carried from old 4.6):** the ladder made operable — press $\hat a^{\dagger}$ or
$\hat a$ and watch the wavefunction climb or fall, with the energy, the classical turning points and
the phase-space ellipse drawn alongside. **Test:** the numerically diagonalised Hamiltonian's levels
are equally spaced to $10^{-10}$; the displayed $\avg{x^{2}}$ matches $(n+\half)\hbar/m\omega$ to
four figures at every rung.

**Numerical confirmation:** the numerically diagonalised oscillator on a 60-state truncation giving
$\{0.5,1.5,2.5,\dots\}$ exactly and levels equally spaced to $10^{-10}$.

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
| 2 | **$\Delta A\,\Delta B\ge\half\abs{\avg{[\hat A,\hat B]}}$** | **0.5** §1's Cauchy–Schwarz, applied to $(\hat A-\avg A)\ket\psi$ and $(\hat B-\avg B)\ket\psi$ | **Collects 0.5's four promises**, including *"Nothing is added in Chapter 4.7 except the physical meaning of the symbols."* Three lines. **Collects 4.2's** *"The second form is the one Chapter 4.7 needs, because it exhibits $\Delta A$ as the length of a vector"* — use 4.2's second form, not a fresh one |
| 3 | What the relation does **not** say | items 1–2 | **Collects 0.9's promise by name**: *"Measurement disturbance is a real and separate phenomenon with its own theorems, and Chapter 4.7 will keep the two apart."* It is a statement about the *spread of outcomes over an ensemble*, not about a microscope. Say so in a `warn` box — **and ⚑ the error–disturbance relations by name** (Ozawa; Busch–Lahti–Werner), because 0.9 said "with its own theorems" and naming none under-delivers while naming them unmarked would be an unflagged import. This flag is new in this re-plan and is the only one added anywhere in it |
| 4 | The dimensional consistency of every conjugate pair | **1.3** §2.1 | **Collects 1.3's promise**: *"$p_i$ is whatever pairs with $q^i$ so that $p_i\dd q^i$ has the dimensions of action"* |
| 5 | Compatible observables; the complete set of commuting observables | **0.5** §8 and **4.2** §4.3, unchanged | §3, the section 4.2 names. **Collects 0.5's "the qualitative content of Chapter 4.7"** and 4.2's *"Chapter 4.7 §3 asks how one knows a set is complete"* — answer that question, which is the one thing 4.2 did not: a set is complete when the common eigenspaces are one-dimensional, and in practice one shows it by exhibiting the count. Hand the definition to 4.11 and 4.13 |
| 6 | **The Heisenberg picture, and the fact that it is a change of basis** | **0.4** §4; **4.6** §2's $\hat U(t)$ | **Moved here from old 4.5 item 15.** It belongs beside the equation it generates. **Collects 0.4's promise verbatim**: *"why the Schrödinger and Heisenberg pictures look like different physics instead of different bases"* — 0.4 names Chapter 4.5 and must be re-aimed |
| 7 | **The Heisenberg equation** $\dv{\hat A}{t}=\frac{1}{\ii\hbar}[\hat A,\hat H]+\pdv{\hat A}{t}$ | item 6; **1.3** §6.1's classical version, term by term | **Collects 1.3's "the bracket goes to Chapter 4.7"**. Put the two equations side by side; the only difference is which bracket |
| 8 | **Ehrenfest:** $\dv{\avg{\hat x}}{t}=\frac{\avg{\hat p}}{m}$, $\dv{\avg{\hat p}}{t}=-\avg{\nabla V}$ | item 7 | Verified numerically. **Collects 1.1's promise by name**, including 1.1's own warning that *"read carefully that is not a fundamental law but a derived statement about expectation values"*. Then the crucial caveat: $\avg{\nabla V}\ne\nabla V(\avg x)$ unless $V$ is at most quadratic — which is why the oscillator is exactly classical in the mean and **nothing else is**. Point at 4.8's coherent state as the case where it is exact |
| 9 | Symmetry $\Rightarrow$ unitary $\Rightarrow$ conserved observable | **1.4** §7; **0.5** §7; **4.2** §7.4 | **Collects 1.3's "The generators of §7 go to… Chapter 4.2 (observables generate unitaries)"** — note the reassignment: 4.2 states it, this chapter proves it. Give translation, rotation and time as the three cases, as 1.4 §3 did. **Rotation is the one that matters**: it hands 4.11 its commutator, and the hand-off should be explicit |
| 10 | Where the classical limit begins, and where it is | | Half a page closing the chapter. Everything so far says the commutator *bounds*, *moves* and *generates*; what it does not yet say is what happens when $\hbar$ is small against the action in play. **That is 4.10, and 4.10 §8 will prove that the correspondence cannot be made exact** — announce both, because two written sentences of 4.2 name "§8" for the second and the reader should meet the claim before the proof |

**Interactive:** none of its own. One figure: the Cauchy–Schwarz triangle drawn as *lengths*, with
$\Delta A$ and $\Delta B$ as the two sides and $\half\abs{\avg{[\hat A,\hat B]}}$ as the projection —
the picture 4.2 §1.4 pointed at.

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
| 3 | Reading the two real equations: Hamilton–Jacobi plus the continuity equation | split item 2 into $\abs\psi$ and phase | The phase is the classical action over $\hbar$, exactly as 1.3 promised. And the amplitude equation is **4.6** §8's current again — say so with 4.6's own symbol $\vv J$ |
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
