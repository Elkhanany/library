# Chapter 1 — Why edges exist
## The four sources of return predictability

> **Core intuition.** When practitioners say "edge," they usually mean one of four very different things. Mixing them is the single most common analytical error in trading literature, and it leads directly to over-allocating to overlays and under-allocating to genuine premia. The taxonomy in this chapter is the most important conceptual tool in the entire book.

---

## 1.1 The four sources

Every documented "edge" in financial markets traces back to one (or a combination) of four sources:

1. **Compensated risk premia** — payment for bearing risk that cannot be diversified away
2. **Behavioral / cognitive frictions** — payment for being on the right side of systematic mispricing
3. **Institutional frictions and constraints** — payment for accommodating predictable mandate-driven flow
4. **Microstructure and flow** — payment for providing liquidity at high frequencies

These four sources differ in *why* they pay, *how durably* they pay, and *who can capture them*. Understanding these differences is the difference between treating "ERP" and "OPEX-week tilt" as comparable allocations (wrong) and treating them as fundamentally different objects requiring different sizing, persistence assumptions, and kill criteria (right).

---

## 1.2 Source 1: Compensated risk premia

### Core intuition

The market pays you to take risks that other people would pay to avoid. Equities are riskier than bonds — they crash when consumption is already low (recessions). So equities trade at a discount to expected dividends, which means they offer a higher expected return. The premium is compensation for bearing the consumption risk.

### Toy example

Imagine an island economy with two assets:
- **Bond:** pays $100 every year, no matter what
- **Stock:** pays $120 in good years, $60 in bad years (50/50 odds → expected $90)

Naive analysis says nobody buys the stock — its expected payoff is $90 vs the bond's certain $100. But in reality the stock might trade at, say, $70 while the bond trades at $90. Why? Because bad years are *exactly when you most need cash* — your job income is also low, your household is stressed. The stock's bad-year payoff is "low quality" cash. People discount it more heavily than the bond's same-amount payoff. The result is a *risk premium*: an expected excess return for accepting bad-year risk.

### Formal object

For any compensated risk premium:
$$E[R_i] - r_f = \beta_i \cdot \pi$$

where $\beta_i$ is exposure to the priced risk factor and $\pi$ is the price of that risk. The key feature: **the premium can't be arbitraged away because the risk is real.** Anyone who bears it deserves the payment.

### What's in this category

- **Equity Risk Premium (ERP):** payment for consumption-correlated risk
- **Variance Risk Premium (VRP):** payment for taking the other side of investors who want to hedge volatility
- **Term premium:** payment for accepting interest rate risk on long bonds
- **Carry / commodity convenience yield:** payment for supplying storage / accepting mean-reversion risk
- **Trend-following (with caveats):** partly compensation for accepting tail risk in exchange for diversifying behavior

### Why this matters: persistence

**Risk premia are the most durable source of return.** They don't disappear when more capital chases them. The risk is the reason the premium exists; if more capital takes the risk, the premium might compress, but it can't go to zero (at zero, no one bears the risk and the market breaks down).

This is the strongest argument for anchoring a portfolio in risk premia: their persistence is more robust than behavioral or institutional edges.

### What it costs

Risk premia are **not free lunches.** In stress, they pay their cost. ERP is paid for in 30-50% drawdowns. VRP is paid for in crashes when implied vol explodes. Trend is paid for in long whipsaw periods. The premium *exists because* of these costs.

A common retail confusion: treating risk premia as if they were behavioral mispricings that should always pay. They don't. They pay on average across regimes; they hurt badly in specific regimes; the average is what compounds.

### Misconception box

> **Misconception:** "If VRP exists, every short option is positive EV."
>
> **Correction:** VRP is a long-run premium. Within any period, your specific option, your specific entry timing, your specific size, and your specific exit can produce negative EV even though the underlying premium is real. The premium is a population average; your individual trade lives in the tail of that distribution.

---

## 1.3 Source 2: Behavioral / cognitive frictions

### Core intuition

Investors systematically misprice information or extrapolate. Mispricings persist longer than efficient-market theory predicts because (a) limits to arbitrage prevent rational traders from fully correcting them, and (b) behavioral biases are remarkably stable over time — humans don't get less prone to recency bias just because they read about it.

### Toy example

A stock reports earnings 20% above consensus. Efficient markets say the stock should jump 20% immediately and stay there. Empirically, it jumps maybe 12% on the day, then drifts up another 4-5% over the following weeks. This is **post-earnings announcement drift (PEAD)**. The mechanism: investors under-react to surprising news because (a) their priors were anchored on the old number, (b) they wait to see if the surprise reverses, (c) institutional mandates limit their ability to act on single-name news quickly.

### Formal object

A behavioral edge typically takes the form:
$$\text{Pricing error}_t = \text{Belief}_t - \text{True value}_t \neq 0$$

with predictable decay:
$$\text{Pricing error}_{t+1} = \rho \cdot \text{Pricing error}_t + \epsilon_t$$

where ρ is between 0 and 1 — a fraction of the error persists into the next period, creating exploitable predictability.

### What's in this category

- **Momentum** (cross-sectional and time-series): under-reaction followed by over-reaction
- **Post-earnings drift (PEAD):** under-reaction to fundamental news
- **Value premium (partly):** over-extrapolation of growth in glamour stocks
- **Lottery demand / low-vol anomaly:** over-payment for high-beta lottery-like stocks
- **Seasonality effects** (Halloween, January): less-clear mechanisms but persistent patterns

### Why this matters: decay risk

**Behavioral edges decay when capital exploits them.** Once enough sophisticated investors learn about PEAD, they buy the post-earnings winners and the drift compresses. McLean & Pontiff (2016) document a 26-58% decline in factor returns post-publication, depending on the factor. Jensen-Kelly-Pedersen (2023) document ~47% post-publication decline across hundreds of factors.

The decay isn't to zero — institutional and behavioral frictions remain — but it's substantial. **Don't assume an edge that worked in 1990s data still works at the same magnitude today.**

### What it costs

Behavioral edges typically have lower drawdowns than risk premia (they're not insurance products), but they can have **catastrophic single-event losses** when the regime that supported them flips. Momentum lost -73% from March-May 2009. Value's 2010-2020 drawdown was the worst in modern history. The costs are different — episodic rather than systematic — but real.

### Misconception box

> **Misconception:** "I can extrapolate behavioral biases from psychology research and find new edges."
>
> **Correction:** Most behavioral biases that produce robust edges are well-documented; the academic literature has been mining this seam for 30 years. Novel "behavioral edges" usually fall into two categories: (a) already documented under different names, (b) not actually edges, just narratives. Be skeptical.

---

## 1.4 Source 3: Institutional frictions and constraints

### Core intuition

Predictable price pressure caused by mandates, leverage limits, accounting rules, or regulatory constraints. Big institutional investors don't trade like rational economic agents — they trade according to mandates that often produce predictable behavior. If you can identify the mandate-driven flow, you can position ahead of it.

### Toy example

Pension fund X has a 60/40 stock/bond mandate with quarterly rebalancing. In Q1 stocks went up 8%, bonds up 1%. The fund is now overweight stocks. By rule, on the last few days of Q1, the fund must *sell* stocks and *buy* bonds to return to 60/40. This selling is forced, predictable, and not driven by fundamental views. If you go *short* stocks and *long* bonds in the last week of Q1 (and reverse early Q2), you're providing the liquidity the fund needs. You earn a small premium for this service.

### Formal object

Institutional frictions create flow imbalances:
$$\Delta P_t = \alpha + \beta \cdot \text{Imbalance}_t + \epsilon_t$$

where Imbalance reflects mandate-driven buy/sell pressure. The premium is small per trade but mechanically repeating.

### What's in this category

- **Betting-Against-Beta (BAB):** leverage-constrained investors bid up high-beta stocks → low-beta outperforms
- **End-of-quarter rebalancing flows:** 60/40 mandates create predictable cross-asset flow
- **Demand-based option pricing:** asset managers' need for hedges pushes up put prices
- **Index reconstitution effects (largely dead now):** S&P 500 additions historically rallied
- **Forced liquidations / margin call cascades:** create predictable reversals once stress passes
- **Securities lending / short-borrow markets:** specials premium

### Why this matters: persistence vs regulatory risk

**Institutional frictions persist as long as the constraint persists.** They can disappear quickly when regulations or product structures change. The S&P 500 inclusion premium was a real ~7% effect in the 1990s; it's now <1% (Greenwood-Sammon 2024) because index funds got smarter about avoiding the obvious arbitrage.

This is different from risk premia (which persist as long as the risk is real) and from behavioral edges (which decay slowly). Institutional edges can vanish in a regulatory update.

### What it costs

The costs are usually small per trade and concentrated in stress periods (when the flow gets dislocated, the institutional player you're trading against may default). Trade slippage and execution costs are the main retail enemies because the per-trade edge is small.

### Misconception box

> **Misconception:** "If I find an institutional flow pattern, I can scale it."
>
> **Correction:** Institutional edges are typically capacity-constrained. The flow you're front-running is finite. As more capital tries to capture the same edge, the imbalance gets eaten before the mandate forces the trade. Most institutional edges work at small size and break at large size.

---

## 1.5 Source 4: Microstructure and flow

### Core intuition

Short-horizon predictability driven by order-flow imbalance, dealer hedging, or liquidity provision. The economic magnitudes are usually small per trade and dominated by transaction costs for retail; institutional players capture them as part of market-making activity.

### Toy example

A large mutual fund needs to buy 1M shares of XYZ over the trading day. Its algos break the order into hundreds of small pieces. Throughout the day there's persistent buying pressure. If you can detect this pressure and position ahead of it (long for an hour, then exit when the buying pressure abates), you earn a few cents per share. Repeated thousands of times across many names, this is high-frequency market making.

### Formal object

Microstructure edges live at the order-book level:
$$E[R_{t+\Delta t}] = f(\text{order flow imbalance}_t, \text{spread}_t, \text{dealer position}_t)$$

where Δt is seconds to minutes. The edge per "unit" is tiny (basis points or less) and only viable at scale with low transaction costs.

### What's in this category

- **Short-term reversal (1-5 day):** liquidity provision after sharp moves
- **Dealer gamma effects:** hedging flows around major strikes / OPEX
- **Intraday momentum / mean reversion:** order-flow patterns
- **Pin risk / OPEX dynamics:** options-related flows around expiry
- **Market-making spreads:** quoting and immediacy provision

### Why this matters: not retail tradable

**Microstructure edges are essentially institutional-only.** The edge per trade is usually 1-5 bps; retail commission and slippage costs alone exceed this. The infrastructure required (low-latency execution, order-book data, large account size for cross-margining) is institutional.

A retail trader trying to capture microstructure edges is playing on a field where every other participant has structural cost advantages and is taking your money on each trade.

### What it costs

The "cost" for retail is just the transaction friction. For institutions, the cost is the rare adverse selection event when the flow pattern reverses (e.g., the "buyer" you were front-running was actually informed, and the news drops).

### Misconception box

> **Misconception:** "GEX scalping is a retail edge — I can sell at the call wall and buy at the put wall."
>
> **Correction:** Public GEX models are model-dependent estimates of dealer position. The most cited models (SqueezeMetrics, SpotGamma) make assumptions about who is long/short which strikes that have not validated post-2022 with the rise of 0DTE options. Cboe's 2025 study estimated that 0DTE market-maker gamma hedging represents only ~0.2% of SPX daily liquidity. The dealer-gamma narrative was always overstated; specific level-trading rules are not retail edges. Use directional sign as low-confidence regime context only (Chapter 9).

---

## 1.6 Why this taxonomy matters operationally

The source determines:

| Source | Persistence | Capacity | Best implementation | Worst implementation |
|---|---|---|---|---|
| **Risk premium** | High (premium = risk is real) | Very high | Foundation sleeve | Naive sizing without crash awareness |
| **Behavioral** | Medium (decays with capital) | Medium | Factor tilt | Treating decayed effect as live |
| **Institutional** | Medium (regulatory dependence) | Low to medium | Tactical overlay | Scaling beyond capacity |
| **Microstructure** | High at institutional scale, ~zero at retail | Institutional-only | Don't | Anything retail |

**The operational rule.** When you see a new "edge," classify it first. If it's a risk premium, it can anchor a sleeve but must be sized for crash behavior. If it's behavioral, it's a tilt with decay risk. If it's institutional, it's a tactical overlay subject to capacity. If it's microstructure, you almost certainly can't trade it profitably.

This single classification step eliminates 80% of the noise in retail trading content.

---

## 1.7 Mixed-source edges

Some edges combine multiple sources. This is fine, but the analyst should be able to *decompose* them.

**Example: Trend-following.**
- Partly risk premium (compensation for accepting whipsaw risk)
- Partly behavioral (under-reaction to information)
- Partly institutional (commodity producer hedging needs)

The decomposition matters because the *behavioral* component is at risk of decay (already partly decayed), while the *risk premium* and *institutional* components are more durable. A pure-behavioral interpretation of trend would be more pessimistic about its forward returns than the academic mixed view.

**Example: VRP.**
- Mostly risk premium (compensation for accepting crash risk)
- Partly institutional (asset manager hedging demand)
- Small behavioral (retail call-buying during bull markets)

Most of VRP is real risk premium and won't decay. Some of it is institutional and might compress as hedging product structures evolve. A small behavioral component might decay further.

**Example: Momentum.**
- Mostly behavioral (under-reaction → over-reaction)
- Partly risk premium (accepting crash risk in V-shaped reversals)
- Small institutional (chase behavior by fund managers)

Most of momentum is behavioral and has decayed substantially post-publication. The crash-risk component is real and explains why momentum can lose -73% in a quarter.

---

## 1.8 The four sources and the five categories

Chapter 5 will introduce a five-category taxonomy: foundation premia, factor tilts, structural overlays, regime filters, and rejected. The mapping between sources and categories is:

| Source | Most common category |
|---|---|
| Risk premium | Foundation premium |
| Behavioral | Factor tilt |
| Institutional | Structural overlay |
| Microstructure | Regime filter or rejected |

This isn't deterministic — VRP is a risk premium *and* sometimes implemented as a tilt, BAB is institutional *and* often classified as a factor — but the rough mapping helps.

The key cognitive rule: **before you can know how to size and how to kill a strategy, you have to know what kind of edge it is.** That's why this chapter exists before any specific dossier.

---

## 1.9 Self-check

1. State the four sources of edges. For each, give one example you've encountered in trading content.
2. Why are risk premia more durable than behavioral edges?
3. Why are institutional edges typically capacity-constrained?
4. Why are microstructure edges essentially not retail-tradable?
5. Decompose "earnings vol harvest" into the four sources. What's the dominant component? (Hint: this is in Chapter 10.)
6. Take any "edge" you've recently considered allocating to. Classify it. What does the classification imply about persistence and sizing?

---

## Where this fits

Chapter 0 gave us the language to talk about distributions, tails, leverage, margin, path. Chapter 1 gives us the framework to talk about *why edges exist* in the first place. Chapter 2 will use Chapter 0's distribution material to explain why Sharpe systematically misleads on negatively-skewed strategies. Chapter 3 will use Chapter 1's source classification to explain why retail haircuts differ across edge types.

The reasoning chain: distributions → sources of edges → why Sharpe lies → realistic retail expectations → conviction framework → taxonomy → dossiers → operational. Skip ahead at your peril.

[← Previous: Chapter 0 — Primitives](01_ch00_primitives.md) | [Next: Chapter 2 — Sharpe trap →](03_ch02_sharpe_trap.md)
