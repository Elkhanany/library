# Part II conventions — fixed across all six chapters. Do not deviate.

- **Signature (+,−,−,−)**: `\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)`. Timelike separations have
  $\Delta s^2 \gt 0$. (Chosen because Parts V–VII are particle physics, where this is standard.
  Say so once, in 2.3, and note the other convention exists.)
- **Coordinates** $x^\mu=(ct,x,y,z)$, so $x^0=ct$. Greek indices $\mu,\nu,\rho,\sigma = 0\ldots3$;
  Latin $i,j,k=1\ldots3$. Einstein summation over one up + one down index.
- $\beta = v/c$, $\gamma = (1-\beta^2)^{-1/2}$. Rapidity $\phi$ with $\tanh\phi=\beta$
  (use $\phi$ for rapidity throughout; never $\eta$, which is the metric).
- **Interval** $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$.
  **Proper time** $c^2\dd\tau^2 = \dd s^2$.
- **Boost along $x$** (standard configuration, $S'$ moving at $+v$):
  $ct' = \gamma(ct - \beta x)$, $x' = \gamma(x - \beta ct)$, $y'=y$, $z'=z$.
- **Four-velocity** $u^\mu = \dd x^\mu/\dd\tau$, so $u\cdot u = c^2$.
  **Four-momentum** $p^\mu = mu^\mu = (E/c,\ \vv p)$, so $p\cdot p = m^2c^2$.
- $m$ ALWAYS means **rest mass**. The book does not use "relativistic mass"; 2.5 explains why
  in one paragraph and then never mentions it again.
- **Electromagnetism**: $A^\mu = (\phi/c,\ \vv A)$, $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$.
  $\partial_\mu = \pdv{}{x^\mu}$ (lower index — it is a covector, per 0.6).
- **Units**: SI throughout Part II, with $c$ written explicitly. Note in 2.6 that Part V switches to
  natural units ($\hbar=c=1$, Heaviside–Lorentz) and why.
- **Cross-part links**: forward-reference by chapter number only (e.g. "Chapter 3.3"), and link with
  `<a href="ch3-3.html">` only if that file exists in `src/`; otherwise write the reference as plain
  text so no dead links ship.
