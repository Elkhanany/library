# Section 7 · Theory
*The math that justifies hedging.*

Up to this point we've described what the dealer does. The question this section answers is **why their delta-hedging strategy is the unique correct strategy**, and what mathematical structure their hedging P&L actually has. This is the most technical section in the document, but it is also the one that justifies every claim that follows.

The derivation proceeds in five steps. Each one builds on the previous, and each is doing a specific piece of intellectual work:

1. **Step 1** — assume the underlying follows geometric Brownian motion (the GBM model)
2. **Step 2** — apply Itô's lemma to derive how the option value changes
3. **Step 3** — construct the delta-hedged portfolio and observe it has no stochastic component
4. **Step 4** — invoke no-arbitrage: a locally risk-free portfolio must earn the risk-free rate
5. **Step 5** — derive the Black-Scholes-Merton PDE; this is the consistency condition

Then we derive the gamma-theta P&L decomposition that we previewed in Section 5C and that drives everything in the dealer-mechanics framework. And finally we connect the option-replication mathematics to variance swaps and VIX construction — the bridge to Section 9.

This section is dense. If math is not your native language, read it slowly, accept the steps one at a time, and pay particular attention to the plain-English unpacking that follows each formula. The intellectual payoff is large: by the end of Section 7B, you will understand that **every delta-hedged option position is, fundamentally, a bet on realized volatility against implied volatility**, and nothing else. This single insight reorganizes how to think about every options strategy.

---

## 7A · The PDE: why dealer hedging works at all

### Step 1 — Geometric Brownian Motion (the model)

Black and Scholes (1973) and independently Merton (1973) assumed the underlying asset follows a **geometric Brownian motion**:

```
dS = μS·dt + σS·dW
```

In words: in a small instant of time dt, the price S changes by an amount that has a deterministic component (μS·dt — the **drift**) and a random component (σS·dW — the **diffusion**). The randomness is captured by dW, an infinitesimal increment of a standard Brownian motion. By construction, dW is normally distributed with mean zero and variance dt. Multiplying by σS scales the noise by the current price and the volatility, making volatility "percent per unit time" rather than "dollars per unit time" — which is what we want, because we observe that volatility scales with price level (a $1,000 stock has bigger dollar moves than a $10 stock at the same volatility).

This is the **central modeling assumption** of the entire Black-Scholes framework. Prices wiggle proportionally to themselves, and the log-returns are Gaussian in continuous time. The model is wrong (real returns have fat tails, as we established in Section 1A), but it is wrong in ways that can be corrected at the margins without rebuilding the whole framework. For our purposes — establishing the rationale for why dealers hedge the way they do — GBM is fine.

A subtle clarification: the parameter μ here is the *instantaneous expected return* in simple-return space, not log-return space. By Itô's formula (which we're about to derive), the expected log-return is μ − ½σ² — that's the variance drag we discussed in Section 1B. The two parameters live in different return conventions; both are valid; you just have to know which one you're using.

### Step 2 — Itô's lemma (how the option value moves)

The option value V is a function of S and t: V(S, t). When S moves, V moves. The textbook chain rule would say dV = (∂V/∂S) × dS, but **that is wrong here**, because S is stochastic. Itô's lemma — the chain rule for Brownian motion — gives us the correct expansion:

```
dV = (∂V/∂t)·dt + (∂V/∂S)·dS + ½·(∂²V/∂S²)·σ²S²·dt
```

Why the extra term? Because (dS)² is not zero. For ordinary smooth functions, (dx)² = O(dt²), which we drop in the limit. For Brownian motion, the variance of dS over interval dt is σ²S²·dt — same order as dt itself, which we **must** keep. The ½(∂²V/∂S²)σ²S²·dt term is **gamma showing up explicitly**: it's the quadratic variation contribution that makes options different from linear instruments.

This is the central technical insight of stochastic calculus. The second derivative matters when the underlying is stochastic; it doesn't when the underlying is deterministic. Every "interesting" property of options derives from this single mathematical fact.

Substituting the Greek notation ∂V/∂S = Δ, ∂²V/∂S² = Γ, ∂V/∂t = Θ:

```
dV = Θ·dt + Δ·dS + ½·Γ·σ²S²·dt
```

Read this: the change in option value over a small time interval has three components — a time-decay piece (Θ·dt), a directional piece (Δ·dS, which moves with the underlying), and a curvature piece (½·Γ·σ²S²·dt, which is always positive for long-option positions and reflects the convexity benefit).

### Step 3 — The replicating portfolio

Consider a portfolio Π that holds the option and a short position of Δ shares (the delta hedge):

```
Π = V − Δ·S
```

In a small interval, its value changes by:

```
dΠ = dV − Δ·dS = (Θ + ½·Γ·σ²S²)·dt + Δ·dS − Δ·dS = (Θ + ½·Γ·σ²S²)·dt
```

Look at what just happened. **The dS terms canceled.** The portfolio change has no stochastic component — it is locally risk-free. That is what delta hedging accomplishes: it removes the dW term, leaving only the deterministic dt terms.

This is the mathematical statement of what we said informally in Section 6D: a delta-hedged book is, at the instant of hedge, locally directionless. The dW noise from the underlying has been hedged away. The remaining motion of the portfolio is entirely deterministic — driven by theta and gamma alone, at first order.

### Step 4 — No-arbitrage closure

A locally risk-free portfolio must earn the risk-free rate, otherwise there is free money. This is the **no-arbitrage condition** — the most consequential single principle in derivatives pricing. So:

```
dΠ = r·Π·dt
```

The portfolio earns the risk-free rate r on its current value. Combining this with the Step 3 expression:

```
(Θ + ½·Γ·σ²S²)·dt = r·(V − Δ·S)·dt
```

Cancel dt from both sides and rearrange:

```
Θ + ½·Γ·σ²S² = r·V − r·Δ·S
```

Or, written with all derivatives expanded back out:

```
∂V/∂t + r·S·∂V/∂S + ½·σ²·S²·∂²V/∂S² = r·V
```

### Step 5 — The Black-Scholes-Merton PDE

```
∂V/∂t + r·S·∂V/∂S + ½·σ²·S²·∂²V/∂S² = r·V
```

This is the celebrated **Black-Scholes-Merton partial differential equation**. (Robert Merton received the 1997 Nobel Memorial Prize in Economics for this work, jointly with Myron Scholes; Fischer Black, who would have shared the prize, had died in 1995.)

### What this PDE is really telling you

The PDE is not a pricing formula. It is a **consistency condition**: any option price function V(S, t) that doesn't satisfy this equation creates an arbitrage. Solving the PDE with boundary condition V(S, T) = max(S − K, 0) (the payoff of a call at expiration) gives the Black-Scholes call formula:

```
C = S·e^(-qT)·N(d1) − K·e^(-rT)·N(d2)
```

with d1 and d2 as defined in Section 5C. But more profoundly, the PDE encodes the **recipe** by which a dealer can replicate the option using only the underlying and cash. The dealer is not "pricing the option" in some metaphysical sense — the dealer is **manufacturing** the option through dynamic hedging.

This is the deepest insight in the entire framework. An option payoff that looks like it requires unusual cleverness to construct (an asymmetric, convex payoff) can in fact be constructed from a simple time-varying position in the underlying plus cash. The cost of constructing this is exactly the Black-Scholes price — no more, no less, under the model's assumptions. Any deviation from this price creates an arbitrage.

The practical implication: when you buy an option, what you're buying is the right to a payoff that the dealer is going to construct for you through their hedging activity. The premium you pay is the cost of the construction kit plus the dealer's margin plus their compensation for taking residual risks the model doesn't capture (jump risk, transaction costs, fat tails). The variance risk premium we discussed in Section 5E is the cumulative spread between what dealers charge and what the model says is fair — the structural compensation they require to be in this business.

### The hedging P&L: gamma vs theta — the punchline

Now we exploit the PDE to get the most important formula in this entire document. Suppose the dealer delta-hedges continuously but realized volatility (σ_R) differs from the volatility used to price the option (σ_I, the implied vol at entry). Their actual P&L over an interval dt is approximately:

```
dΠ ≈ ½·Γ·S²·[(dS/S)² − σ_I²·dt]
```

Read that as: **over each interval, the delta-hedged dealer earns gamma times the difference between realized squared return and implied variance.** This is the entire economic content of a delta-hedged option position.

If you are *long* the option (long gamma) and realized volatility *exceeds* implied, you make money. Every wiggle in spot lets you scalp gamma — buy low, sell high in your hedge — at a rate that, in aggregate, exceeds the theta you're paying.

If you are *long* the option and realized falls *short* of implied, you lose. You bought too much vol.

If you are *short* the option (short gamma — the dealer's typical position), the signs flip. You earn the implied vol (the theta you collect) and pay the realized vol (the rebalancing losses). A short-gamma dealer **wants quiet markets**. A long-gamma dealer **wants moves**.

> **Under the standard delta-hedged framework, an option position is, at first order, a bet on realized vs. implied volatility — the dominant P&L driver in the absence of large vega or skew dynamics.**

This is the punchline of the gamma-vs-theta decomposition. Strike selection affects the size of gamma; expiration selection affects the speed of gamma; the IV at entry sets the implied side of the bet — and to first order, the resulting P&L is a function of whether realized exceeded implied.

**The honest caveats.** The "nothing more, nothing less" framing skips several real-world second-order effects that matter in practice:

- **Vega risk on IV moves.** A delta-hedged position is *not* vega-neutral. If implied vol changes between entry and exit, that mark-to-market vega P&L is a separate component on top of the gamma-vs-realized term. For long-dated options with large vega, this can dominate.
- **Discrete hedging.** The decomposition above assumes continuous rebalancing. Real hedging happens discretely, and the *path* of spot between rebalances introduces variance around the theoretical gamma-scalping P&L. Two traders running the same position with different hedge frequencies will realize different P&L from the same realized vs. implied gap.
- **Skew and surface dynamics.** Options that sit on a steep part of the surface accrue P&L from vanna and volga as spot and vol co-move — terms that aren't captured by the simple γ × (RV² − IV²) decomposition.
- **Transaction costs.** Hedging is not free. The gamma-scalping P&L is *gross*; net P&L can be meaningfully smaller, especially in less liquid underlyings or on short-DTE options where rebalancing is frequent.

For most retail-scale, short-to-medium DTE, large-cap-underlying delta-hedged positions, the first-order realized-vs-implied framing captures the bulk of P&L variability. For longer-dated positions, exotic surface trades, or low-liquidity underlyings, the second-order terms matter and should be modeled explicitly.

[INTERACTIVE: realized-vs-implied]

[INTERACTIVE: hedging-friction-simulator]

### Why the dealer feedback loop is built into the math

This is also the punchline for why aggregate dealer positioning moves the market. Suppose dealers are collectively short gamma in aggregate. They are mechanically losing money to volatility — and the more volatility there is, the more they lose. To minimize losses they hedge aggressively, which means buying as the market rises and selling as it falls. **That hedging creates volatility**, which makes them lose more, which makes them hedge more.

The feedback loop is mathematically built into the gamma-theta decomposition we just derived. It is not a story or a metaphor. It falls out of the PDE. Section 8B will formalize this into the effective-volatility equation that quantifies how dealer feedback amplifies (or dampens) underlying volatility depending on the sign of aggregate dealer gamma.

### The variance swap connection

Integrating dΠ ≈ ½ΓS²·[(dS/S)² − σ_I²·dt] over the life of the option and weighting by 1/S² gives, almost exactly, the payoff of a **variance swap**. This is not coincidence — it's the foundation of model-free variance replication and the reason VIX (Section 9A) is constructed as a weighted strip of options with 1/K² weights.

Specifically, Demeterfi, Derman, Kamal, and Zou's 1999 Goldman Sachs paper ("More Than You Ever Wanted to Know About Volatility Swaps") showed that a portfolio of options weighted by ΔK/K² across all strikes, when dynamically delta-hedged, replicates the payoff of a variance swap. The intuition: weighting by 1/K² creates a "gamma flat" portfolio (constant gamma per dollar of spot move regardless of where spot is), which is exactly the property required to replicate realized variance.

This is the mathematical thread connecting dealer hedging to VIX. VIX is, fundamentally, the cost of replicating variance through delta-hedged options. Every option you trade contributes some amount of replicated variance to the dealer's book; aggregate dealer gamma is, essentially, the aggregate variance replication exposure of the entire options ecosystem. Section 9A returns to this connection in detail.

---

## 7B · Second-order Greeks in context

Gamma told us how delta changes when spot moves. But delta also changes when implied volatility moves (no spot move required) and when time passes (no spot move, no vol move). These derivatives — **Vanna** and **Charm** — generate predictable hedging flows that are largely invisible to retail and relentless on a calendar-time schedule. Understanding them is the difference between knowing dealers hedge and knowing *when* they hedge.

This section provides fully worked examples with dollar arithmetic for the two most important higher-order Greek flows: post-FOMC vanna unwinds, and the charm-driven Monday gap.

### Vanna recap: ∂Δ/∂σ

We covered Vanna formally in Section 5D. The closed form is:

```
Vanna = ∂Δ/∂σ = ∂ν/∂S = −e^(-qT)·φ(d1)·d2/σ
```

The intuition: implied volatility affects the option's pricing density. Higher IV puts more probability mass in the tails. For an OTM call, this raises delta. For an OTM put (negative delta), it pulls delta toward zero in magnitude.

**Vanna is large and negative for OTM puts.** When VIX spikes, OTM put deltas become more negative in magnitude. A dealer short these puts (because customers were buying protection) becomes effectively *longer* the underlying through the option leg. To remain delta-neutral, the dealer must sell more of the underlying.

Conversely: when IV crashes (typical post-event behavior), OTM put deltas decay toward zero. The dealer's effective long exposure from the puts evaporates. They were holding extra long shares against the short puts; now they have too many shares and must sell some back.

### Worked example: post-FOMC vanna unwind with full arithmetic

Make this concrete. Suppose SPX is 4,500. A dealer is short 5,000 SPX OTM puts at strike 4,400, against an institutional hedger who bought protection ahead of the FOMC meeting. The contracts have thirty days to expiration. Pre-FOMC, the IV at that strike is 25%.

**Initial setup (pre-FOMC):**
- 5,000 short contracts at K=4400, S=4500, IV=25%, T=30 days, r=4%, q=1.5%
- Put delta at this strike: approximately **−0.36** (BSM with these parameters)
- Dealer's effective delta exposure from the put leg: 5,000 × 100 × 0.36 = **+180,000 share-equivalents long**
- Hedge: dealer is short 180,000 SPX share-equivalents (via ES futures or SPY)

Net delta zero.

**FOMC announcement lands. IV at the put strike crushes from 25% to 18%.**

Vanna at this strike is approximately **−0.005 per vol point**:

```
ΔΔ_put = Vanna × Δσ = (−0.005) × (−7 vol points) = +0.035
```

The put delta moves from −0.36 to approximately −0.325. The dealer's effective long exposure from the puts drops from 180,000 to:

```
5,000 × 100 × 0.325 = 162,500 share-equivalents long
```

That's a drop of about **17,500 share-equivalents long**.

**The dealer is now over-hedged by 17,500 short shares.** To re-flatten, they buy 17,500 SPX-equivalents.

Across the entire dealer community, the aggregate flow scales proportionally. A 500,000-contract aggregate put book produces several hundred million to over a billion dollars of mechanical buying flow in the hour after the announcement.

**The aggregate is the post-FOMC ramp that has nothing to do with anyone reading the dot plot favorably.** It is dealers reversing their pre-event hedges into the vol crush. The rally is mechanical, not interpretive.

> *Numbers computed at stated parameters using a standard BSM calculator. Vanna and delta vary continuously with all inputs; verify with your own calculator. The orders of magnitude — tens of thousands of share-equivalents per 5,000-contract book — are the load-bearing point.*

This is the standard FOMC pattern: vol bids up into the event (because hedgers position), IV crushes after the event regardless of direction (because the event is now in the past), and dealers buy back hedge stock as their put deltas decay. The most you'll typically see this contribute to the SPX move post-FOMC is 0.3-0.5%, but it operates with high reliability across years.

### Charm recap: ∂Δ/∂t

Charm is the rate of change of delta with respect to time. Even with spot and IV frozen, delta drifts because the option's effective probability of finishing ITM evolves as the expiration window shrinks. The Black-Scholes formula for call charm:

```
Charm_call = −e^(-qT)·φ(d1)·[2(r−q)T − d2·σ√T] / (2T·σ√T)
```

Charm is small far from expiration and grows like 1/T as expiration approaches. It also operates on **calendar time** — including weekends, even though markets are closed. This is the technical reason for the empirical regularity of Monday gaps and the "charm bid" into OPEX Fridays.

### Worked example: the charm weekend gap with full arithmetic

Charm scales with 1/T and runs on calendar time, not trading time. A 30-DTE OTM put with delta −0.25 on Friday at 4:00 PM ET has its remaining T measured in calendar days. Friday close to Monday open is 65.5 hours of calendar elapse — roughly 9% of the option's remaining life — even though markets were open for zero of those hours.

**Setup:** 100,000 SPX OTM put contracts (a typical institutional book) at K = SPX × 0.97, S = SPX, T = 30 calendar days. Initial put delta: −0.25. Dealer is short these puts, so their effective long-stock exposure is:

```
100,000 × 100 × 0.25 = 2,500,000 share-equivalents long
```

The dealer is hedged with 2,500,000 SPX-equivalents short in ES or SPY.

**Friday 4 PM → Monday 9:30 AM. Spot is identical to Friday's close (no overnight news). T has shrunk from 30 days to 27.3 calendar days (Friday 4 PM = T₀; Monday 9:30 AM = T₀ + 65.5 hours = T₀ + 2.73 calendar days).**

For our −0.25 delta put, charm is approximately −0.004 per calendar day (computed from Black-Scholes at these parameters). Over 2.73 calendar days, the delta drifts:

```
ΔΔ_put = Charm × ΔT = (−0.004) × 2.73 = −0.011
```

Toward zero. So the put delta on Monday morning is approximately:

```
−0.25 + 0.011 = −0.239
```

The dealer's effective long exposure from the puts drops from 2,500,000 to:

```
100,000 × 100 × 0.239 = 2,390,000 share-equivalents long
```

A reduction of about 110,000 share-equivalents long.

**On Monday morning, the dealer is now over-hedged by 110,000 short shares** (because they hadn't unwound any of the 2,500,000 short hedge over the weekend, while the put deltas decayed in their favor). To re-flatten, the dealer buys 110,000 SPX-equivalents.

This is small per-contract but a dealer carrying 100,000 such put contracts opens Monday over-hedged by enough share-equivalents to push the SPX morning open up by a few basis points to a tenth of a percent. Aggregated across the entire dealer community, the buying flow becomes meaningful.

These 100,000-share-equivalent flows of mechanical buy-flow hit the tape in the first 30 minutes of Monday trading and explain a meaningful chunk of the **"Monday gap-up" anomaly** that's been documented in SPX since the 1990s. **The bull doesn't show up on Monday; the hedger does.**

### A note on calendar vs trading time

There's a subtle technical issue worth noting. Some option pricing models use calendar time for charm calculations (T measured in 365-day years), while others use trading time (T measured in 252-day years). The choice affects the magnitude of weekend charm — calendar-time models predict larger weekend charm drift than trading-time models.

Empirically, the Monday-gap-up anomaly is more consistent with calendar-time charm decay than trading-time, which is why most dealer risk systems use calendar-time conventions for short-dated positions. This is a pedantic detail, but it's the kind of pedantic detail that separates dealers who correctly anticipate Monday morning flows from those who don't.

### Vomma, Speed, Color, Veta, Zomma

The Greek menagerie keeps going. We touched on each in Section 5D; here is the operational summary of when each matters:

**Vomma (Volga)** — the second derivative of value with respect to vol. Vega convexity. Matters most for vol-of-vol risk and VIX options. Played a major role in Volmageddon (Section 8C) — short VIX wing positioning had massively negative vomma, and as VIX spiked, the convex losses overwhelmed the linear vega losses.

**Speed** — the third derivative of value with respect to spot (∂Γ/∂S). In 0DTE options, speed is enormous near the strike and explains why a 1% move can flip a position from heavily long to heavily short gamma within minutes. This is the source of the "gamma flipping" intraday character that makes 0DTE risk management qualitatively different from longer-dated risk management.

**Color** — the rate at which gamma decays over time (∂Γ/∂t). For ATM options, color is positive near expiration: gamma compresses *into* the ATM strike as expiration approaches. By the final hour of OPEX Friday, virtually all the dealer gamma is concentrated within ±$5-10 of spot. This is the mathematical source of pin risk (Section 5F) — the gamma concentration is what creates the gravitational pull toward strikes.

**Veta** — the rate at which vega decays over time (∂ν/∂t). Mostly relevant for managing the time decay of long-dated positions where vega is the dominant exposure. A vol-targeting fund running long VIX call positions for crash insurance worries about veta in a way that retail traders rarely do.

**Zomma** — the rate at which gamma changes with respect to vol (∂Γ/∂σ). Shows up in risk management of large vega positions and in vol surface dynamics.

For our purposes — understanding aggregate dealer flow analysis — Vanna and Charm cover roughly 95% of the dealer-relevant higher-order dynamics. The rest get bookkeeping attention from risk managers but rarely move the broad tape on their own. If you understand vanna and charm, you understand most of what's published about "dealer flows" with any analytical rigor; the rest is mostly noise.

[INTERACTIVE: higher-order-greeks]

### What to look for as you slide

Gamma peaks sharply at-the-money. Crank the days-to-expiry slider down and watch the peak grow — that's the 1/√T divergence in action. Vanna changes sign at-the-money: positive on the OTM-call side, negative on the OTM-put side. This sign asymmetry is what makes vanna flow direction-dependent. Charm is largest near the money and grows aggressively as expiry approaches — it is the mathematics of "pinning."

The joint surface visualization is what risk managers actually look at. A position isn't risky just because of any single Greek's value — it's risky because of how all the Greeks evolve jointly as conditions change. A short straddle two days before expiration isn't dangerous because of gamma alone; it's dangerous because gamma, vanna, charm, and vomma are all simultaneously at their peak magnitudes, and any combination of spot move + IV move + time passing activates all of them against the position at once.
