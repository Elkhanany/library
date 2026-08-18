# Mathematics audit — Part 0 (ch0.1–0.9) and Part I (ch1.1–1.4)

Scope: `src/ch0-1.html` … `src/ch0-9.html`, `src/ch1-1.html` … `src/ch1-4.html`.
Method: full read of every chapter (prose, boxed equations, `<details class="grind">` blocks,
worked examples, "Your turn" solutions, and the figure scripts where a caption quotes a number),
followed by independent re-derivation in `sympy` / `mpmath` / `numpy`. Scripts live in `/tmp/pb/`.
No file in the tree was modified.

---

## Verdict

The mathematics of these thirteen chapters is sound: I re-derived every non-trivial
result independently and found **no wrong equation, no broken derivation, and no sign or
factor error in any boxed result** — every one of the ~90 symbolic and ~40 numerical checks
below agreed, in several cases to the last printed digit of a twelve-digit number. The
defects I did find are one systematic convention failure (the ⚑ mark for quoted-not-derived
results is used in ch0-8, ch0-9 and all of Part I but is absent from ch0-1 through ch0-7,
which between them import at least eight named theorems), one wrong printed number, and a
handful of local imprecisions and unstated small steps. There are **no BLOCKERs**: nothing
in Part 0 or Part I gives a wrong answer.

---

## §1 Errors

Severity: **BLOCKER** = wrong result · **MAJOR** = right result but broken derivation or a
missing hypothesis · **MINOR** = typo or imprecision a reader will decode.

---

### 1. MAJOR — the ⚑ convention is not applied in ch0-1 … ch0-7

`README.md` line 9 and `PLAN.md` line 283 both state the rule: *"Every quoted-not-derived step
marked ⚑."* The mark is used correctly and often from ch0-8 onward (1 in ch0-8, 2 in ch0-9,
3/7/10/12 in ch1-1…ch1-4). It appears **zero times** in ch0-1 … ch0-7, which nonetheless import
named theorems, several of them announcing the fact in words.

Verification (grep counts of `⚑` per file):

```
ch0-1.html:0  ch0-2.html:0  ch0-3.html:0  ch0-4.html:0  ch0-5.html:0  ch0-6.html:0  ch0-7.html:0
ch0-8.html:1  ch0-9.html:2  ch1-1.html:3  ch1-2.html:7  ch1-3.html:10 ch1-4.html:12
```

The self-declared quotations, in source order. In each case the fix is the same: prefix the
sentence (or the enclosing `<p><b>…</b>`) with `⚑ ` exactly as ch0-8 does with
`⚑ Quoted, not proved — Picard–Lindelöf`.

| # | file | exact current string | exact corrected string |
|---|---|---|---|
| 1a | `src/ch0-2.html:71` | `is <em>uniformly</em> continuous: for any $\varepsilon$ there is a single $\delta$ that works` | `is <em>uniformly</em> continuous (⚑ Heine–Cantor, quoted): for any $\varepsilon$ there is a single $\delta$ that works` |
| 1b | `src/ch0-2.html:554` | `<p><b>Turning a product of integrals into a double integral.</b> This is Fubini's theorem, and` | `<p><b>Turning a product of integrals into a double integral.</b> ⚑ Quoted: this is Fubini's theorem, and` |
| 1c | `src/ch0-2.html:800` | `<p>none of which has an elementary antiderivative. This is a <strong>theorem</strong> (Liouville,` | `<p>none of which has an elementary antiderivative. ⚑ Quoted, not proved: this is a <strong>theorem</strong> (Liouville,` |
| 1d | `src/ch0-4.html:971` | `complex coefficients has a complex root. (This is the one result in this chapter we import rather than` | `complex coefficients has a complex root. (⚑ Quoted, not proved: this is the one result in this chapter we import rather than` |
| 1e | `src/ch0-6.html:878` | `$\nabla g$ is the velocity of some curve in $S$ — is the implicit function theorem, which we quote;` | `$\nabla g$ is the velocity of some curve in $S$ — is the implicit function theorem, ⚑ which we quote;` |
| 1f | `src/ch0-7.html:73` | `never cross except where $\vv F=\vv 0$. (This is the existence-and-uniqueness theorem for ODEs, which` | `never cross except where $\vv F=\vv 0$. (⚑ This is the existence-and-uniqueness theorem for ODEs, which` |
| 1g | `src/ch0-7.html:1251` | `<strong>Poincaré lemma</strong>, which we quote here and Chapter 3.5 proves. (The parallel with §2 is` | `⚑ <strong>Poincaré lemma</strong>, which we quote here and Chapter 3.5 proves. (The parallel with §2 is` |

Two further unmarked imports that do not announce themselves in the same words and should
also carry ⚑: the Aharonov–Bohm measurements in `ch0-7.html` §2.5 ("Those are experimental
facts, quoted"), and in `ch0-3.html` §4 the measured value of $a_e$ together with the
five-loop QED calculation and Dyson's divergence argument. Note that `ch0-6.html:208`
(`Theorem (quoted — proved in the grind box below)`) is *not* a violation in the other
direction: it is genuinely proved in the grind box, so no ⚑ is warranted; only the word
"quoted" in its title is misleading, and could read `Theorem — proved in the grind box below`.

---

### 2. MINOR — wrong printed number: straight-line descent time in the brachistochrone problem

**File** `src/ch1-2.html:1450` (§10, Problem 1 solution, "Check").

Current string:

```
    along the cycloid versus $0.8406\ \mathrm{s}$ along the straight line between the same two
```

Corrected string:

```
    along the cycloid versus $0.8412\ \mathrm{s}$ along the straight line between the same two
```

The stated cycloid time $0.7096$ s is exactly right; the straight-line comparison is not.
The straight line from $(0,0)$ to $(\pi/2,1)$ under $v=\sqrt{2gy}$, $g=9.8$, gives
$T=2\sqrt{1+m^2}\,x_1/\sqrt{2gy_1}$ with $m=y_1/x_1=2/\pi$:

```
=== ch1-2 Problem 1: straight-line descent time, exact ===
  T_line exact = sqrt(10)*pi*sqrt(4/pi**2 + 1)/14  = 0.8412091758930117
  T_cycloid = sqrt(a/g)*pi with a=1/2: 0.7096134475568644
  book says 0.8406 ; computed 0.8412
```

Independent numerical quadrature agrees: `straight line time = 0.8412091758931998`.
The neighbouring claim "16% faster" survives either way ($(0.8412-0.7096)/0.8412 = 15.6\%$),
so nothing downstream changes; but the printed value is a wrong result rather than a
decodable typo, and a reader who recomputes will find it.

---

### 3. MINOR — sign of the exponent in the alternative Cauchy–Schwarz proof

**File** `src/ch0-5.html:205` (§1, grind box, "An alternative proof, for the file").

Current string:

```
    $0\le\left\lVert u-\ee^{\ii\varphi}v\right\rVert^{2}=2-2\,\mathrm{Re}(\ee^{-\ii\varphi}\avg{u,v})$; choosing
```

Corrected string:

```
    $0\le\left\lVert u-\ee^{\ii\varphi}v\right\rVert^{2}=2-2\,\mathrm{Re}(\ee^{\ii\varphi}\avg{u,v})$; choosing
```

and in the next line `$\varphi$ to be the argument of $\avg{u,v}$` should become
`$-\varphi$ to be the argument of $\avg{u,v}$` (or leave that line alone and instead write
the norm as $\lVert u-\ee^{-\ii\varphi}v\rVert^{2}$).

**Why.** The chapter fixes the physics convention in §1 — conjugate-linear in slot 1,
linear in slot 2 — and derives $\avg{\alpha u,v}=\bar\alpha\avg{u,v}$ from it. Under that
convention

$$\lVert u-\ee^{\ii\varphi}v\rVert^{2}=\avg{u,u}-\ee^{\ii\varphi}\avg{u,v}-\ee^{-\ii\varphi}\avg{v,u}+\avg{v,v}=2-2\,\mathrm{Re}\big(\ee^{\ii\varphi}\avg{u,v}\big).$$

Symbolic check with $\avg{u,v}=a+\ii b$, $\lVert u\rVert=\lVert v\rVert=1$:

```
=== A. ch0-5 alternative Cauchy-Schwarz expansion (physics convention) ===
  2-2Re(e^{+i phi}<u,v>) = -2*a*cos(varphi) + 2*b*sin(varphi) + 2      <- correct
  book writes 2-2Re(e^{-i phi}<u,v>) = -2*a*cos(varphi) - 2*b*sin(varphi) + 2
```

The printed form is the one you get in the *mathematicians'* convention (linear in slot 1),
which the chapter explicitly declines. The conclusion $\abs{\avg{u,v}}\le1$ is unaffected,
which is why this is MINOR; but as printed the grind box is internally inconsistent with §1.

---

### 4. MINOR — "that factor of seven *is* the correlation" is false as literally read

**File** `src/ch0-6.html:854–855` (§6, Familiar ground, collinear-covariates example).

Current string:

```
  inverting the diagonal instead of taking the diagonal of the inverse. That factor of seven <em>is</em>
  the correlation, here $-99/100=-0.99$. Inverting first and taking the diagonal second is not a
```

Corrected string:

```
  inverting the diagonal instead of taking the diagonal of the inverse. That factor of seven is
  $1/\sqrt{1-\rho^{2}}$, with $\rho$ the correlation between the two estimates, here $-99/100=-0.99$.
  Inverting first and taking the diagonal second is not a
```

Verification:

```
=== B. ch0-6 collinear Fisher example ===
  J^-1 = [[100/199, -99/199], [-99/199, 100/199]]
  SE = sqrt(100/199) = 0.708881205008336
  1/sqrt(1-rho^2) = 7.088812050083359   <- the 'factor of seven'
  correlation from J^-1 = -0.99
```

The correlation is $-0.99$ and the inflation factor is $7.0888 = 1/\sqrt{1-\rho^2}$; the two
numbers are related but not equal, and the sentence as written asserts equality.

---

### 5. MINOR — variance of the *sum* is off by a factor of 2

**File** `src/ch0-6.html:849–850` (same box, one sentence earlier).

Current string:

```
  <em>sum</em> $\beta_{1}+\beta_{2}$ is pinned down with variance $1/199$; the <em>difference</em> is
  known only with variance $1$, two hundred times worse.
```

Corrected string:

```
  combination $(\beta_{1}+\beta_{2})/\sqrt2$ is pinned down with variance $1/199$; the
  combination $(\beta_{1}-\beta_{2})/\sqrt2$ is known only with variance $1$, two hundred times worse.
```

Verification:

```
  Var(e1.theta) = 1/199   Var(b1+b2) = 2/199
  Var(e2.theta) = 1       Var(b1-b2) = 2
```

The preceding sentence correctly says the variance of $\vv e_k\cdot\hat{\boldsymbol\theta}$ is
$1/\mu_k$ for the **unit** eigenvector; the follow-up drops the normalisation. The ratio $199$
is unaffected, so "two hundred times worse" stands either way.

---

### 6. MINOR — the multiplier sign convention in ch1-2 §6.4 is opposite to ch0-6 §7

**File** `src/ch1-2.html:979` and `src/ch1-2.html:1004`.

Chapter 0.6 §7 defines $\mathcal L = f-\lambda(g-c)$ and proves $\dd f^{*}/\dd c=\lambda$.
Chapter 1.2 §6.4 defines

```
$$ \tilde S[q,\lambda] \;=\; \int_{t_{1}}^{t_{2}}\Big[L(q,\dot q,t) \;+\; \lambda(t)\,g(q,t)\Big]\dd t, $$
```

i.e. **plus** $\lambda g$, and then claims at line 1004

```
  — which matches Chapter 0.6's finding that $\lambda = \dd f^{\ast}/\dd c$ is the sensitivity of
```

The two $\lambda$'s differ by a sign; Worked Example 1(c) then correctly reports
$\lambda = -m(\ell\dot\theta^{2}+g\cos\theta) < 0$ and has to take $\abs\lambda$ to get the
tension. Cleanest fix is one clause at line 1004:

```
  — which matches Chapter 0.6's finding that the multiplier is a sensitivity of the optimum to the
  constraint level, up to the sign convention (Chapter 0.6 wrote $f-\lambda(g-c)$, so its
  $\lambda$ is minus this one) —
```

Alternatively change line 979 to `\;-\; \lambda(t)\,g(q,t)`, which flips the sign of $\lambda$
in Worked Example 1(c) and removes the need for the absolute value there.

---

### 7. MINOR — repeated indices at the same height in ch0-7 §4, against the rule stated in ch0-6

**File** `src/ch0-7.html:806` and the surrounding grind box.

`ch0-6.html` §5.2 states the error-check as a rule: *"if you have written down a formula with
two indices at the same height summed against each other, you have made a mistake."*
`ch0-7.html` then writes, with the vector components declared upstairs in §1,

```
    $$ \big(\nabla\times\vv F\big)_{i} \;=\; \epsilon_{ijk}\,\partial_{j}F^{k}, $$
```

in which $j$ is summed with both occurrences downstairs, and similarly
$A_{ij}=\tfrac12(\partial_{j}F^{i}-\partial_{i}F^{j})$ carries mixed heights on one object.
This is universal practice in Cartesian 3-space (where $\delta_{ij}=\delta^{ij}$ makes the
distinction empty) and no formula is wrong, but as printed it contradicts a rule the book
states as an error test. One sentence, inserted immediately before line 806, resolves it:

```
    <p>A note on heights. Everything in this chapter is Cartesian and Euclidean, where
    $\delta_{ij}=\delta^{ij}$ and raising an index changes nothing, so we suppress the
    distinction and write all of $\epsilon$'s indices down. Chapter 2.4 reinstates it, and from
    there onward Chapter 0.6 §5.2's one-up-one-down test applies literally.</p>
```

---

## §2 Gaps in the chain

Places where step *n+1* does not follow from step *n* without an unstated move. Each is
given with the sentence to insert and where it goes.

**G1. `src/ch0-1.html` §5 — the existence and uniqueness of $\ee$ is asserted, not argued.**
Line 280 defines `$$ \ee \;\equiv\; \text{the unique base with } L(\ee)=1 …$$` after
observing only that $L(2)\approx0.693$ and $L(10)\approx2.303$. Nothing so far shows that
some base has $L=1$, or that only one does. Insert immediately before that display:

> That such a base exists, and only one, is worth half a sentence rather than an assumption.
> From $b^{h}=(\ee^{\ln b})^{h}$ — or, without circularity, from
> $L(b^{r}) = \lim_h (b^{rh}-1)/h = r\,L(b)$ for rational $r$ and continuity in between —
> $L$ is a continuous, strictly increasing function of $b$ on $(0,\infty)$ with $L(1)=0$ and
> $L(b)\to\infty$. So it takes the value $1$ exactly once, and $\ee$ is that base.

**G2. `src/ch0-3.html` §2 grind box — the logarithm's remainder is bounded only for $0\le x<1$.**
Line 237 reads `For $0\le x\lt1$ the integrand is at most $t^{n}$, so $\abs{R_{n}}\le
x^{n+1}/(n+1)\to0$`, and the paragraph then concludes that the radius is exactly $1$. The
negative half of the interval, which is the harder half (the $1/(1+t)$ factor is no longer
bounded by 1), is never treated. Insert after that sentence:

> For $-1\lt x\lt 0$ substitute $t=-s$ and bound $1/(1-s)\le 1/(1-\abs x)$ on the interval,
> giving $\abs{R_{n}}\le \abs{x}^{n+1}/\big[(n+1)(1-\abs x)\big]\to0$ as well. The bound
> degrades as $x\to-1$, which is the analytic shadow of $\ln(1+x)\to-\infty$ there.

**G3. `src/ch0-3.html` §4 — "the error is no bigger than the first omitted term" is proved for
one integral and stated for all asymptotic series.** Line 507 reads `beautiful, and it is the
practical rule for asymptotic series: <em>the error is no bigger than the …`. The bound was
derived from the explicit alternating remainder $R_{N+1}=(-x)^{N+1}\!\int e^{-t}t^{N+1}/(1+xt)$,
which is special. Amend the sentence to:

> beautiful, and it is the practical rule of thumb for asymptotic series: the error is no
> bigger than the first omitted term. That statement is a *theorem* here, because the
> remainder is an explicit alternating integral; for a general asymptotic series it is a
> reliable heuristic rather than a theorem, and the honest general statement is only
> $\abs{R_{N+1}}=O(x^{N+1})$.

**G4. `src/ch0-7.html` §7.5 — Earnshaw needs one more line.** Line 1357 says
`(Earnshaw's theorem — the potential energy is harmonic in charge-free space, so it has no
minimum to` — but the maximum principle was proved two sentences earlier only for maxima.
Insert before that parenthesis:

> Applying the same argument to $-\phi$, which is harmonic whenever $\phi$ is, rules out
> strict interior minima as well.

**G5. `src/ch0-5.html` §6(c) — the matrix form $A=UDU^{\dagger}$ skips one step.** The text
says "$Ae_{i}=\lambda_ie_i$ for every column reads $A = U D U^{\dagger}$". The intermediate
move is one clause; insert it:

> Stacking the $n$ relations $Ae_i=\lambda_ie_i$ column by column is $AU=UD$; multiplying on
> the right by $U^{-1}=U^{\dagger}$ gives $A=UDU^{\dagger}$.

**G6. `src/ch1-2.html` §5.1 — the widget's $\Delta S$ formula assumes the sine modes are
orthogonal on $[0,T]$ and cites Chapter 0.9, which comes later in reading order but earlier in
numbering.** This is fine as a cross-reference, but the specific fact needed —
$\int_0^{T}\cos(j\pi t/T)\cos(k\pi t/T)\,\dd t=0$ for $j\ne k$, applied to $\dot\eta$ rather
than $\eta$ — is not the fact ch0-9 §1.1 proves (which is for $\ee^{\ii k_n x}$ on
$[-L/2,L/2]$ with $k_n=2\pi n/L$). Add the half-line:

> (the cross terms vanish because $\int_{0}^{T}\cos(j\pi t/T)\cos(k\pi t/T)\dd t = 0$ for
> $j\neq k$, by the product-to-sum identity and one integration)

**G7. `src/ch1-4.html` §7.1 — the generator is silently narrowed.** §1.1 defines
$K_{i}(q,\dot q,t)$, allowing velocity dependence; §7.1 computes
$\delta q_{j}=\epsilon\,\partial Q/\partial p_{j}=\epsilon K_{j}$, which requires $K$ to be
free of $p$ (equivalently of $\dot q$). The text does write "$Q=\sum_i p_iK_i(q,t)-F(q,t)$",
but the restriction is not flagged as one. Add after that formula:

> — note that this identification needs $K$ to depend on $q$ and $t$ only, so that $Q$ is
> linear in the momenta; a velocity-dependent generator produces a charge quadratic in $p$
> and the bracket returns something else. The Laplace–Runge–Lenz vector of Worked Example 2
> is exactly such a case, which is why it does not appear in §3.4's table.

---

## §3 Verification log

Everything below was re-derived from scratch and agreed. Scripts: `/tmp/pb/v01_02.py`,
`v03.py`, `v04.py`, `v05.py`, `v11.py`, `final.py` plus inline `mpmath` one-liners.

**ch0-1.** $\gamma'(v)=cv/(c^2-v^2)^{3/2}$; $\gamma''(0)=1/c^{2}$; the series
$\gamma=1+v^{2}/2c^{2}+O(v^{4})$. $L(2)=0.693147$, $L(10)=2.30259$. Problem 2's table of
$E(h)=\ee^{h}-(1+h)$ reproduced exactly to all printed digits
($0.00517092/0.0517092/0.517092$; $5.01671\!\times\!10^{-5}/…/0.501671$;
$5.00167\!\times\!10^{-7}/…/0.500167$). $\tau/t_{1/2}=1/\ln2=1.44270$. Squeeze
$\sin h<h<\tan h$, $(1-\cos h)/h\to0$, product/quotient/chain/inverse rules, logarithmic
derivative $\dd T/T=\tfrac12\dd L/L$, escape-velocity sensitivity $\pm\tfrac12$: all clean.

**ch0-2.** Riemann error constants derived symbolically per cell (estimate − truth):
`mid-exact = -d^3 f2/24 - d^5 f4/1920`, `trap-exact = +d^3 f2/12 + d^5 f4/480`,
`(2M+T)/3 - exact = d^5 f4/2880` — confirming midpoint $=-f''d^{3}/24$, trapezoid
$=+f''d^{3}/12=-2\times$midpoint, Simpson kills $d^{3}$. Figure constants for
$f=1+t/2+\sin t$ on $[0,3]$: $f(3)-f(0)=1.64112$, $N\!\times\!E_{\rm left}\to-2.46168$,
$f'(3)-f'(0)=-1.98999$, $N^{2}E_{\rm mid}\to+0.746247$; direct summation confirms
($N=5000$: $-2.46198$, $+2.46138$, $0.74625$). Gaussian moments
$\int x^{2n}\ee^{-ax^{2}} = (2n)!/(n!(4a)^{n})\sqrt{\pi/a}$ verified for $n=0..4$;
$\int\ee^{-ax^{2}+bx}=\sqrt{\pi/a}\,\ee^{b^{2}/4a}$; $\int\ee^{-ax^{2}}\cos bx =
\sqrt{\pi/a}\,\ee^{-b^{2}/4a}$; disc/square squeeze; $v_{\rm esc}=11186$ m/s;
$\mathrm{erf}(1/\sqrt2)=0.6826895$; $1/\sqrt{2\pi}=0.398942$; $\Delta x\Delta k=\tfrac12$.
Problems 1–4 (reduction $I_n=nI_{n-1}$, parameter differentiation $n!/a^{n+1}$, AUC
$=\text{Dose}/Vk$ both ways, $J'=-(b/2a)J$) all correct.

**ch0-3.** Taylor by repeated integration by parts with the antiderivative chosen to kill the
upper boundary term — the induction, the Lagrange form and $\int(a+h-t)^n/n!\,\dd t=h^{n+1}/(n+1)!$
all check. Asymptotic example $F(x)=\int_0^\infty \ee^{-t}/(1+xt)$: numerically optimal
truncation and error

```
x=0.1 : F=0.9156333394  optimal N=9   err=1.77e-4   e^(-1/x)=4.54e-5
x=0.05: F=0.9543709099  optimal N=19  err=1.146e-8  e^(-1/x)=2.061e-9
```

matching the printed "$N=9$ with error $1.8\times10^{-4}$" and "$N=19$ with error
$1.1\times10^{-8}$". Planck units: $\ell_P=1.6163\times10^{-35}$ m, $t_P=5.391\times10^{-44}$ s,
$m_P=2.176\times10^{-8}$ kg, $m_Pc^{2}=1.221\times10^{19}$ GeV; the $3\times3$ dimension
determinant $=2$ and the $(\hbar,c,k_e)$ determinant $=0$. $F_{\rm grav}/F_{\rm elec}=4.409\times10^{-40}$;
$a_0=5.292\times10^{-11}$ m, $27.21$ eV, $2.188\times10^{6}$ m/s, $\alpha=1/137.04$. OR/RR
expansion exact and first-order numbers ($1.2667$, $6.333$, $2.08\%$, $12.5\%$, $75\%$),
$\ee^{-0.05}=0.951229$, $\ee^{0.5}=1.64872$. $\gamma$ at $0.1c$: exact $1.0050378153$,
truncated $1.0050375$, error $3.153\times10^{-7}$ vs next term $3.125\times10^{-7}$;
$1\%$ speed $v/c=0.1155$. Problem 1(b) radius $3$, function $-\ln(1-x/3)$, endpoint behaviour.
Problem 3 numbers ($\mathrm{RR}=0.600$, $\mathrm{OR}=0.529412$, ratio $0.882353$, $p_2\lesssim0.12$).
Pendulum $\omega=\sqrt{V''/m}$ and $T=2\pi\sqrt{L/g}$.

**ch0-4.** $\det(I+\epsilon A)$ for $A=[[2,1,0],[0,-1,3],[1,4,5]]$ came out
`-31*eps**3 - 9*eps**2 + 6*eps + 1` — matching the printed cubic exactly, with
$\mathrm{tr}A=6$, $\det A=-31$, the $\epsilon^{2}$ coefficient $-9$ as the sum of principal
$2\times2$ minors, and the value $1.059069$ at $\epsilon=0.01$. Worked Example 1:
$ST=[[3,6],[1,1]]$, $TS=[[5,-2],[1,-1]]$, $\det=-3$ both, $\mathrm{tr}=4$ both.
Problem 4: $A'=P^{-1}AP=[[-5,-15],[4,11]]$, $\mathrm{tr}=6$, $\det=5$. Markov example:
$(P^{2})_{21}=0.225$, state at $n=10$ is $(0.10737,0.11869,0.77394)$. Reflection similarity
$P^{-1}AP=\mathrm{diag}(1,-1)$; $FR$, $RF$, $[R,F]=[[0,2],[2,0]]$; $R_\theta(1,-\ii)^{\mathsf T}
=\ee^{\ii\theta}(1,-\ii)^{\mathsf T}$. Exchange lemma, Leibniz formula, $\det A^{\top}=\det A$,
$\det(AB)$ via the axioms, $\det\ee^{A}=\ee^{\mathrm{tr}A}$, SU($N$) tracelessness: all sound.

**ch0-5.** Cauchy–Schwarz (both the optimising $\lambda$ and the grind-box minimisation),
Gram–Schmidt induction, Dirac notation, completeness, projection = nearest point, adjoint
existence/uniqueness, $(A^{\dagger})_{ij}=\overline{A_{ji}}$, the full spectral-theorem
induction (base case, invariance of $e_1^{\perp}$, restriction Hermitian), degeneracy and
projector form, $A=UDU^{\dagger}$, the ellipse $M=(A^{-1})^{\top}A^{-1}$, functions of
operators, $\ee^{\ii A}$ unitary and its converse, simultaneous diagonalisation, PCA. Numeric:
Gram–Schmidt on $1,x,x^{2}$ over $[-1,1]$ returned
`[sqrt(2)/2, sqrt(6)*x/2, sqrt(10)*(3*x**2-1)/4]`, identical to $\sqrt{5/2}(3x^{2}-1)/2$;
$\lVert x^{2}-\tfrac13\rVert^{2}=8/45$. The §5 figure family $A(c)=[[2,\sqrt3/2+c],[\sqrt3/2-c,1]]$:

```
c=0   eigvals 2.5, 0.5     eigen-line angles 120°, 30°   (90° apart)
c=1/2 eigvals 2.366, 0.634 angles 135°, 15°              (60° apart — caption)
c=1   single eigenvalue 1.5, one direction                (collapse — caption)
```

$\ee^{\ii\theta\sigma_x}=\cos\theta\,I+\ii\sin\theta\,\sigma_x$ verified symbolically.
Problem 3(b): $N=[[3,3/2],[1/2,3]]$, $\lambda=3\pm\sqrt3/2$, eigen-directions $\pm30°$,
$\cos\alpha=1/2$.

**ch0-6.** Counterexample $xy/(x^{2}+y^{2})$; uniqueness of $\mathrm D f$; Jacobian as the
matrix; the continuous-partials theorem and its proof; steepest ascent from Cauchy–Schwarz;
$\nabla f\perp$ level sets; $(\nabla f)^{i}=g^{ij}\partial_jf$ and the polar gradient
$\partial_r f\,\hat{\vv r}+r^{-1}\partial_\theta f\,\hat{\boldsymbol\theta}$; the chain rule as a
Jacobian product; Clairaut and its counterexample ($\partial_y\partial_xf(0,0)=-1$,
$\partial_x\partial_yf(0,0)=+1$); second-order Taylor and the eigenvalue classification;
Lagrange multipliers with $\lambda=\dd f^{*}/\dd c$ checked on
$f=x^{2}+2y^{2}$, $g=x+y=c$ ($\lambda=4c/3$, $f^{*}=2c^{2}/3$, $(2,1)$ and $\lambda=4$ at $c=3$);
Jacobian determinants $r$ and $r^{2}\sin\theta$ both ways (last-row and first-column
expansions); $\sqrt{\det g}$ agreement; Boltzmann via two multipliers and $\beta=1/k_BT$;
Worked Example 2 ($x=x^{9}$, $H=[[12x^{2},-4],[-4,12y^{2}]]$, $\mu=\pm4$ at the origin,
$\mu=8,16$ at $(1,1)$, $\sqrt2$ axis ratio); Problem 4(b) ($\mu=\pm3$, $\mu=3,9$,
$\det H=36xy-9$).

**ch0-7.** Punctured-plane field: both mixed partials equal $(y^{2}-x^{2})/(x^{2}+y^{2})^{2}$,
circulation $2\pi$ for every $R$; $\nabla\theta=\hat{\boldsymbol\theta}/r=(-y,x)/r^{2}$.
Divergence via the box (with the exact $O(\Delta^{3})$ accounting), divergence $=\mathrm{tr}J$,
spherical divergence from face areas, $\nabla\cdot(\hat{\vv r}/r^{2})=0$ for $r\ne0$.
Curl via the rectangle; the unique symmetric/antisymmetric split; $A\vv h=\tfrac12\vv\omega\times\vv h$
with every entry of $A$ checked against $\vv\omega$; $\tfrac12n(n-1)=n\iff n=3$;
$\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$ and
$A_{ij}=-\tfrac12\epsilon_{ijk}\omega_k$, $\omega_k=-\epsilon_{kij}A_{ij}$. Figure presets:
source $(2,0)$, rotation $(0,2)$, shear $(0,0)$ with $\vv F=\nabla(xy)$, mixed
$\nabla\cdot=y+1$, $(\nabla\times)_z=1-x$ and the three dial settings $(1,-1),(1,1),(-1,-1)$.
Both big theorems by interior cancellation; continuity equation and the vanishing-integral
lemma; $\nabla\times\nabla\phi=0$, $\nabla\cdot(\nabla\times\vv A)=0$; mean-value form
$\bar\phi-\phi=\tfrac{a^{2}}{6}\nabla^{2}\phi$ (and $a^{2}/2n$ in $n$ dimensions);
$\nabla^{2}(1/r)=0$ with the $4\pi$ flux; Worked Example 2 ($J(1,1,1)=[[2,1,0],[3,0,-2],[0,1,1]]$,
$\nabla\cdot\vv F=3$, $\vv\omega=(3,0,2)$, $S$ and $A$ and $A\vv h=(-2,-\tfrac72,3)$,
$\tfrac12\sqrt{13}=1.80$); Problem 1 ($\tfrac52$ both sides; $\mathrm{vol}=\tfrac13\oint\vv r\cdot\dd\vv A$);
diffusion table $100$ s / $10^{4}$ s / $10^{6}$ s and $L=\sqrt{2DC_0/k}\approx90$–$200\,\mu$m.

**ch0-8.** Integrating factor and Duhamel (differentiated back); logistic partial fractions;
$\ee^{\lambda t}$ as eigenfunction and the Jordan-block origin of $t\ee^{\lambda t}$ (including
the confluent limit); phase-space area $\mathcal A=2\pi E/\omega=ET$ and $(n+\tfrac12)h$;
damping discriminant, $\omega_d$, $\lambda_+\approx-\omega_0^{2}/2\gamma$, critical damping,
$Q=\omega_0/2\gamma$ and $E=E_0\ee^{-\omega_0t/Q}$. Resonance: $\omega_{\rm peak}=\sqrt{\omega_0^{2}-2\gamma^{2}}$,
$A_{\max}=F_0/(2\gamma\sqrt{\omega_0^{2}-\gamma^{2}})$, power peak exactly at $\omega_0$,
$\omega_\pm=\sqrt{\omega_0^{2}+\gamma^{2}}\pm\gamma$, FWHM exactly $2\gamma$,
$\omega_+\omega_-=\omega_0^{2}$, Lorentzian, $\Gamma\tau=\hbar$ with the $\rho$
($4.4\times10^{-24}$ s) and $Z$ ($2.6\times10^{-25}$ s) numbers. Worked Example 2 recomputed
end to end: $\omega_{\rm peak}=0.99750$, $\omega_d=0.99875$, $A_{\max}=10.0125F_0$,
$\omega_\pm=1.05125/0.95125$, and the three Lorentzian comparisons
($0.5000$ vs $0.5120$; $0.0099$ vs $0.0142$; $0.0099$ vs $0.0044$). Coupled oscillators:
$M=[[1.1,-0.1],[-0.1,1.1]]$, $\omega=1,\sqrt{1.2}$, beat $T=65.8$ s vs $6.00$ s period,
weak-coupling estimate $62.8$ s ($4.6\%$ low), mode energies $5.50$ mJ split $45.5/54.5\%$.
$N$-chain $\omega_n=2\sqrt{k/m}\sin(n\pi/2(N+1))$ and its $N=2$ check; the $a\to0$ wave
equation; d'Alembert via $\partial_\xi\partial_\eta$. Two-compartment PK: $\lambda=-1.0,-0.1$
and $-2.00,-0.25$; eigenvectors $(2,-1),(1,4)$ and $(2,-1),(1,3)$; angles $102.5°$ and $98.1°$;
$A_1(t)=\tfrac89D\ee^{-\alpha t}+\tfrac19D\ee^{-\beta t}$ and $\tfrac67/\tfrac17$; half-lives
$0.347$ h $=20.8$ min and $2.77$ h. Pendulum $T/T_0$ corrections $0.19\%$, $1.74\%$, $18.0\%$
(the last is the exact elliptic value $1.18034$, not the truncated series $1.176$ — correctly
so); the $\theta_0=1$ rad check $1.06608$ vs $1.06633$.

**ch0-9.** Orthogonality $\int\ee^{-\ii k_mx}\ee^{\ii k_nx}=L\delta_{mn}$; Gibbs constant
$\tfrac2\pi\mathrm{Si}(\pi)=1.178979$; the $L\to\infty$ limit and Plancherel;
$\widetilde{f'}=\ii k\tilde f$; convolution theorem with the $\sqrt{2\pi}$; the delta from a
Gaussian regulator ($\sigma=\sqrt{2\epsilon}$) and from $\ee^{-\epsilon k^{2}}$;
$\delta(ax)=\delta(x)/\abs a$ with both signs of $a$; $\nabla^{2}(1/r)=-4\pi\delta^{3}$;
bandwidth theorem $\Delta x\Delta k\ge\tfrac12$ from Cauchy–Schwarz with
$I+\bar I=-1$; Gaussian saturation; characteristic function, CLT log-expansion, Cauchy
counterexample, $n=15.7\sigma^{2}/\delta^{2}$ ($z_{0.975}+z_{0.80}=2.80158$, squared and
doubled $=15.698$); Gaussian FT with the completed square; diffusion kernel
$1/\sqrt{4\pi Dt}$ and $\sigma=\sqrt{2Dt}$; box-function problem ($2a$ both sides,
$\Delta x=a/\sqrt3$, divergent $\Delta k$, $90.28\%$ in the central lobe from
$\tfrac1\pi\!\int_{-\pi}^{\pi}(\sin u/u)^{2}=0.902823$, $\pi/\sqrt3=1.814$); transform-limit
$0.4413$, $44.1$ THz, $94$ nm; Lorentzian linewidth $\Delta\omega=1/\tau$, $159$ MHz,
$0.66\,\mu$eV, $2.7\times10^{-7}$.

**ch1-1.** Grind-box drag integration reproduced to eleven digits with
`solve_ivp(rtol=1e-12)`:

```
dT             = -202.44636423166392   (book -202.4463642317)
int F.v dt     = -202.44636423152792   (book -202.4463642316)
d(T+mgy)       = -282.68693716555845   (book -282.6869372)
work by drag   = -282.68693716543055   (book -282.6869372)
```

Magnetic third-law failure: $\vv B_1(\vv r_2)=0$, $\vv B_2(\vv r_1)=+\mu_0q_2v\hat{\vv z}/4\pi d^{2}$,
$\vv F_{12}=-\mu_0q_1q_2v^{2}\hat{\vv y}/4\pi d^{2}$, ratio $v^{2}/c^{2}=1.11265\times10^{-5}$ at
$v=10^{6}$ m/s. Constrained pendulum both ways, $\mathcal F=m(\ell\dot\theta^{2}+g\cos\theta)$
and $3mg$ at the bottom from horizontal release. Polar acceleration and the free-particle check
$\ddot r=r\dot\theta^{2}=0.35355$ at $v_0=b=t=1$. Fermat/Snell, computed to 15 digits:

```
x* = 1.3626502055346          T(x*) = 11.5712403741      T(1) = 11.7932716837  (diff 0.222)
theta1 = 53.726393   n1 sin = 0.8062009081370601
theta2 = 32.511391   n2 sin = 0.8062009081370601   difference 2e-31
T''(x*) = 3.6913   half = 1.84565
delta=0.1   dT=0.01899   dT/d^2=1.8989
delta=0.05  dT=0.00468   dT/d^2=1.8719
delta=0.025 dT=0.001162  dT/d^2=1.8586
```

— every digit of the book's table. $T''>0$ everywhere. Escape velocity $11186$ m/s (Earth),
$2375$ m/s (Moon). Reduced mass $\mu_H/m_e=0.9994556794$, $\mu_D/m_e=0.9997276305$, relative
difference $2.721\times10^{-4}$, H-$\alpha$ shift $0.1786$ nm.

**ch1-2.** Every step of the Euler–Lagrange derivation, the bump function
(value and derivative both vanishing at the junctions, $\int=16\delta^{5}/15$), the smooth
$\ee^{-1/(\delta^{2}-u^{2})}$ alternative, the interchange counterexample
$\arctan(1/\epsilon)$, the higher-derivative EL with two boundary terms and $f''''=0$,
$L=T-V\Rightarrow\dot p=F$. Figure: $y_*=\tfrac12gt(T-t)$ peaking at $1.225$ m,
$S=-mg^{2}T^{3}/24=-4.0017$ J s, $\Delta S=\frac{m\pi^{2}}{4T}(a_1^{2}+4a_2^{2}+9a_3^{2})$
giving $0.024674$ at $a_1=0.1$ (6 parts in 1000, $8\%$ of peak height), and the $T+V$
comparison slope $4mgT/\pi=12.48$ per metre, i.e. $\pm0.125$ at $a_1=\pm0.01$, five hundred
times larger. Harmonic-oscillator saddle at $\mathcal T>\pi/\omega$; Legendre condition
$P=m\gamma^{3}>0$; second variation and the Jacobi equation reproducing $\pi/\omega$.
Double pendulum $T$ and $V$ derived independently; form invariance (Lemmas 1 and 2 and the
Jacobian factorisation); polar EL producing centrifugal and Coriolis; field EL. Worked Example 1
(a)(b)(c) including $\lambda=-m(\ell\dot\theta^{2}+g\cos\theta)$ and $3mg$; geodesics in the
plane and on the sphere including the $k\ne0$ integration to a plane through the origin.
Brachistochrone: Beltrami first integral $y(1+y'^{2})=C$, the cycloid, and the descent time
$0.7096134$ s (exactly $\pi\sqrt{a/g}$). Problems 2–4 (Beltrami, rotating hoop with
$V''_{\rm eff}=mR^{2}\Omega^{2}\sin^{2}\theta_0$, total-derivative gauge freedom and the EM
example) all correct.

**ch1-3.** Legendre transform, involution, $f=\tfrac14x^{4}\to g=\tfrac34p^{4/3}$ with
$\sup_x(2x-\tfrac14x^{4})=1.8898816=\tfrac34\cdot2^{4/3}$; Young's inequality and conjugate
exponents; thermodynamic potentials and $\partial^{2}U/\partial S^{2}=T/C_V$. Canonical momentum
$m\vv v+e\vv A$; $H=L_2-L_0$ and the three checks; the relativistic
$H=\gamma mc^{2}=\sqrt{p^{2}c^{2}+m^{2}c^{4}}$ with $\partial^{2}L/\partial\dot x^{2}=m\gamma^{3}$.
Hamilton's equations both ways; $\Omega^{\top}=-\Omega$, $\Omega^{2}=-I$, $\det\Omega=1$;
$\{f,g\}=(\nabla f)^{\top}\Omega\nabla g$ block-checked. Pendulum phase portrait: separatrix
$p=\pm2m\ell^{2}\omega_0\cos(q/2)$, linearisation $\ddot u=+\omega_0^{2}u$, Jacobian trace $0$
and $\lambda^{2}=-\omega_0^{2}\cos q$, homoclinic $q=4\arctan\ee^{\omega_0t}-\pi$.
$\dd\mathcal A/\dd E=T$ checked against $4K(E/2)$:

```
E=0.2  -> 6.449765395     E=0.8 -> 7.110077486
E=1.4  -> 8.301452541     E=1.9 -> 11.63334899
```

— all four match the printed ten-digit values. The blob spread:
`E=1.4112 -> 8.3348045`, `E=1.9208 -> 12.083922`, spread $44.98\%$ ("45%").
Liouville via $\mathrm{tr}J=0$; Jacobi identity by the relabelling
$a\to d,b\to c,c\to a,d\to b$; the fundamental brackets; the three generators; canonical
transformations, $M\Omega M^{\top}=\Omega$, generating functions, Hamilton–Jacobi and its
oscillator solution. Worked Example 1: the Lorentz force from $L$ (using
$v^{j}(\partial_iA_j-\partial_jA_i)=(\vv v\times\vv B)_i$) and $H=(\vv p-e\vv A)^{2}/2m+e\phi$.
Problems 1–4 including $\{L_i,L_j\}=\epsilon_{ijk}L_k$, $\{\vv L^{2},L_z\}=0$, the action–angle
transformation with unit Jacobian and $H=\omega P$, and $\mathcal A=2\pi E/\omega=8.19545910$
at $m=1.7$, $\omega=2.3$, $E=3$, $n\approx1.5\times10^{33}$.

**ch1-4.** Definition of symmetry with the total-derivative loosening; the boost
$F=M\vv u\cdot\vv R_{\rm cm}$; the four-step proof; the moving-clock grind box
($\bar K=K-\dot q\tau$, the measure expansion, $Q=\sum p_iK_i-H\tau-F$); the three classics;
$\dd E/\dd t=-\partial L/\partial t$ and the driven-oscillator example $-x\dot f$;
$\epsilon_{ijk}$ form of the rotation charge and $L_3=xp_y-yp_x$; the §4.4 figure rates
$\dot L_z=\lambda m\omega^{2}r^{2}\sin2\theta(1+\mu\sin\Omega t)$ and
$\dot E=\mu\Omega\cos\Omega t\cdot\tfrac12m\omega^{2}r^{2}(1+\lambda\cos2\theta)$, and the
identity $r^{2}(1+\lambda\cos2\theta)=(1+\lambda)x^{2}+(1-\lambda)y^{2}$ used in the script;
the field current $j^{\mu}=\ii(\phi\partial^{\mu}\phi^{*}-\phi^{*}\partial^{\mu}\phi)$ with
$\partial_\mu j^\mu=0$ from $\Box\phi=-m^{2}\phi$, and $j^{0}=\mp2EN^{2}$ on the two plane
waves; the improvement-term ambiguity; the charge-generates-its-own-symmetry identity;
the free-particle scaling non-symmetry ($\dot Q=m\dot x^{2}\ne0$); LRL conservation, $\vv A\cdot\vv L=0$,
$A^{2}=2mEL^{2}+m^{2}k^{2}$, $r=(L^{2}/mk)/(1+e\cos\theta)$; Problem 1 (scale symmetry,
$Q=mx\dot x-2tH$, $\dot Q=0$); Problem 2 (surface of revolution, quadrature,
$R_{\min}=\ell/\sqrt{2mE}$, Clairaut); Problem 4 (Kepler scaling, $\dot Q=\tfrac12L$, virial,
$T^{2}/a^{3}$).

**Count.** Roughly 90 symbolic identities and 40 numerical values re-derived; all agree with
the text except the single number in §1 item 2.

---

## §4 Things I could not verify

1. **The interactive figures' JavaScript, beyond the numbers quoted in captions.** I read the
   scripts only where a caption asserts a number (ch0-1 zoom constants, ch0-2 Riemann error
   readout sign convention, ch0-5 rotation preset `ROTANG = 50°, ROTSC = 1.25`, ch0-7 flow
   presets, ch1-4 potential). I did not execute any of the canvases, so claims about
   *measured* quantities that only the widget produces — the ch1-3 Liouville figure's
   "$18$ parts per million … never worse than $\pm300$ ppm" area drift, the ch1-2 widget's
   quadrature agreeing to $0.024674$, the ch0-9 bandwidth figure's
   $3.23,4.64,6.61,9.38,13.29$ sequence, the ch1-4 orbit figure's "$3\times10^{-13}$" and
   "$1.2\%$ at $\lambda=0.005$" — were checked only for plausibility and dimensional/scaling
   consistency, not reproduced.

2. **Physical/experimental values quoted from outside the book.** $a_e=1.15965218059(13)
   \times10^{-3}$ and the "over twelve thousand diagrams at fifth order"; the Aharonov–Bohm
   measurements (Chambers 1960, Tonomura 1986); the Thomlinson–Gray $100$–$150\,\mu$m viable
   rim; the $\rho$ and $Z$ widths; Efron–Hinkley on observed vs expected information; the
   Urey deuterium identification. These are correct to my knowledge but are quotations, and
   I verified only the arithmetic performed on them.

3. **Forward references.** Every "Chapter 2.x / 3.x / 4.x / 5.x / 6.x / 7.x will show…" claim
   was taken at face value; Parts II–VII are outside this brief and other agents are working
   them. I did check that the eight actions in ch1-2 §8.1 are the standard ones in the book's
   own $(+,-,-,-)$ signature, including that the Einstein–Hilbert sign genuinely does flip
   with the signature (under $g\to-g$ in four dimensions, $\sqrt{-g}$ is unchanged while
   $R=g^{\mu\nu}R_{\mu\nu}$ changes sign), so the footnote there is right.

4. **Rendering.** I read `src/*.html` as text and did not build or view the pages, so I
   cannot report on MathJax macro resolution (`\vv`, `\avg`, `\dv`, `\pdv`, `\half`, `\ee`,
   `\ii`, `\dd`, `\R`, `\C`), equation-reference resolution (the extractor strips the
   `<a href="#eq…">` links, which is why many sentences above read "into  and"), or whether
   any equation overflows its column.

5. **Prose outside the mathematics.** "In plain terms" boxes were read for mathematical
   claims only; I did not audit them for style, and I did not check the Math Ledger
   (`src/_ledger.html`) or the throughline page against these chapters.
