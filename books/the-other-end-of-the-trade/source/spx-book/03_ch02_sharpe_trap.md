# Chapter 2 — The Sharpe ratio trap
## Why mean and variance aren't enough

> **Core intuition.** A strategy can win 95% of the time and still lose money. A strategy with the same Sharpe as another can have catastrophically different worst-case behavior. Sharpe sees mean and variance; it ignores skew, kurtosis, and path. For options strategies — and short-vol strategies in particular — Sharpe is systematically misleading in a direction that flatters short-vol and penalizes long-vol/tail-hedge structures.

---

## 2.1 The pedagogical ladder

This chapter walks the reader through the reasoning chain explicitly:

1. A strategy can win often and still lose money.
2. This happens when small gains are frequent but rare losses are large.
3. That means mean, variance, skew, and kurtosis all matter.
4. Sharpe only sees mean/variance.
5. Short options are structurally short skew.
6. Therefore short-vol strategies can look better than they are.
7. Therefore every short-vol trade needs tail-loss and margin-path analysis.

Each step is developed in its own section.

---

## 2.2 Step 1: A strategy can win often and still lose money

### Toy example

Strategy: I sell you a coin flip with the following payoffs:
- 95% probability: I pay you $1
- 5% probability: you pay me $25

Win rate: 95%. Looks great, right?

Expected value per round: $0.95 × $1 - $0.05 × $25 = $0.95 - $1.25 = **-$0.30**.

Each round you lose 30 cents on average, despite winning 95% of the time. **Win rate is not edge.**

This is the simplest possible illustration of why the empirical "feel" of trading — "I won 19 trades in a row" — can systematically diverge from the actual P&L.

### A more realistic version

Sell a 90-delta short put for $0.50 of premium, max possible loss is $4.50 (if the stock goes to zero, simplified). You win the $0.50 about 90% of the time. Your "win rate" is 90%, which feels like edge. But:

- Win: 90% × $0.50 = +$0.45 per trade on average from wins
- Loss: 10% × E[loss given loss] = 10% × ~$2 (assuming average loss is partial) = -$0.20

Mean = +$0.25 per trade. So this one *does* have positive EV. But suppose the realized average loss given loss is $3 instead of $2 (because losses cluster in stress when IV expands): mean = +$0.45 - $0.30 = +$0.15. And if you can't hold to expiry due to margin (forced to close at MTM peak), realized loss given loss can be $4-4.50 even when terminal would have been $2: mean = +$0.45 - $0.40 = +$0.05.

The realized edge depends heavily on the loss distribution and the path, not just the win rate.

---

## 2.3 Step 2: Small frequent gains + rare large losses = negative skew

This is the structural shape of all premium-selling strategies. Let's make it precise.

### The shape

For a typical short-vol strategy:
- **70-90% of trades:** small positive return (the premium minus minor MTM)
- **5-20% of trades:** moderate negative return (the position moved against you, you closed for a loss)
- **1-5% of trades:** large negative return (a market shock blew through your strikes)

The mean of this distribution is the *premium* minus the *expected loss in tail*. If the premium is high enough, mean is positive. But the *median* and *mode* of the distribution are positive, while the mean can be barely positive or negative, because the tail dominates.

### The math

Skew is formally:
$$\text{Skew} = E\left[\left(\frac{R - \mu}{\sigma}\right)^3\right]$$

For a Gaussian, this is 0. For PUT index, it's roughly **-2.09**. For SPX index itself, it's about **-0.81**. For a short far-OTM put, it can be **-5 or worse**.

Negative skew means the distribution leans left — the left tail is much fatter than the right tail. Visually:

```
Normal distribution:        Short-vol distribution:
       _____                          _____
      /     \                        /  ___|___
     /       \                      /  |     \
    /         \                    /   |      \
___/           \___              _/____|_______\___
   left      right                left           right
                                  (long tail)
```

The bulk of the mass is on the right side (frequent small wins), but the left tail extends much further than the right tail (rare large losses). Mean shifts left; median stays right of zero.

### Why every short-option position has this shape

Sell an option, you collect premium up front (right tail capped). Maximum gain = premium. Maximum loss = much larger than premium (especially for puts on equity indices, where the underlying can drop 30%+ and you owe the difference between strike and spot).

**Asymmetric payoffs produce asymmetric distributions.** Capped gains and uncapped (or large) losses inevitably create negative skew. There is no way to construct a short-option position without negative skew.

### Misconception box

> **Misconception:** "If I use defined-risk spreads, I eliminate the skew problem."
>
> **Correction:** Spreads cap the loss but the cap is still much larger than the gain. A $1-credit / $9-max-loss put spread has -9× skew at a single-trade level. Aggregating across many trades, the skew narrows but doesn't disappear. The structural issue is asymmetric payoff, and spreads don't fix asymmetric payoff — they just bound the worst case.

---

## 2.4 Step 3: Mean, variance, skew, kurtosis all matter

A return distribution is fully described (more or less) by the first four moments:

| Moment | What it measures | Why it matters |
|---|---|---|
| **Mean (μ)** | Average outcome | The thing you're trying to maximize |
| **Variance (σ²)** | Spread around mean | How "uncertain" the outcome is |
| **Skew (γ₁)** | Asymmetry | Whether bad outcomes are bigger than good |
| **Kurtosis (γ₂)** | Tail fatness | How likely "extreme" events are |

For symmetric, thin-tailed (Gaussian) returns, mean and variance are sufficient. For non-Gaussian returns — which describes essentially every options strategy — all four matter.

### Why kurtosis matters

Kurtosis measures how often "rare" events happen. For a normal distribution, kurtosis = 3 (or "excess kurtosis" = 0). SPX daily returns have kurtosis around 18 — six times normal. PUT index has even higher.

This means "5-sigma events" — which Gaussian models say happen roughly once per 17,000 days (about once per 70 years) — actually happen every few years in financial markets.

### The 1987 example

October 19, 1987: SPX dropped 22.6% in one day. Pre-1987 Gaussian models said this was a ~25-sigma event with probability roughly 10⁻¹³⁷ — i.e., essentially impossible in the lifetime of the universe.

But it happened.

The lesson isn't that markets are mysterious; it's that the Gaussian assumption is *wrong*. Returns have fat tails. Kurtosis is high. "Once-per-100-years" events happen multiple times per career.

For options strategies, this matters a lot, because the tail of the loss distribution is where you actually lose serious money. Underestimating kurtosis = underestimating tail risk.

---

## 2.5 Step 4: Sharpe only sees mean and variance

The Sharpe ratio is defined as:
$$\text{SR} = \frac{E[R - r_f]}{\sigma_R} = \frac{\mu - r_f}{\sigma}$$

It uses the first moment (μ) in the numerator and the second moment (σ) in the denominator. **Skew and kurtosis appear nowhere.**

This means two strategies with identical Sharpe can have wildly different risk profiles:

### Worked example

Two strategies, both with $5/year mean return on $100 capital and $10 standard deviation. Both have Sharpe = 0.5.

**Strategy A (long equity):** roughly Gaussian. Worst year historically: -$25. Recovery time after worst year: ~3 years.

**Strategy B (short far-OTM puts):** 95% of years return between $4-7, but in 5% of years the strategy loses $50-100 in a single bad month. Same mean ($5), same standard deviation ($10), but max drawdown is 4× larger and recovery may be impossible (margin call, forced unwind, fund termination).

Sharpe says: equivalent. Reality: completely different.

### The Calmar ratio

A partial fix: use *drawdown* in the denominator instead of standard deviation.

$$\text{Calmar} = \frac{\mu}{\text{MaxDD}}$$

Calmar penalizes path-dependent strategies more honestly. SPX over 1990-2024 has Sharpe ~0.5 and Calmar ~0.18. PUT index has Sharpe ~0.65 and Calmar ~0.29 — better on both. But XIV (short-vol ETP, terminated 2018) had Sharpe ~1.5 and Calmar ~undefined (max DD ~96% destroyed the strategy).

The ranking by Calmar tells a more honest story than Sharpe does.

### The Sortino ratio

Another partial fix: only penalize downside volatility.

$$\text{Sortino} = \frac{\mu - r_f}{\sigma_\text{downside}}$$

Sortino captures one part of the skew problem: it doesn't penalize positive deviations. But it still doesn't capture kurtosis explicitly.

### Use multiple metrics

**Operational rule:** never evaluate a strategy on Sharpe alone. Always look at Sharpe **and** Sortino **and** Calmar **and** the actual path of returns through 2008, 2018, 2020, 2022. Different metrics highlight different problems.

---

## 2.6 Step 5: Short options are structurally short skew

Recap: short option = collect premium (capped right tail) in exchange for accepting potential larger loss (open left tail). The payoff is structurally asymmetric → distribution is structurally negatively skewed.

This is true for:
- Naked short puts
- Short calls
- Iron condors (short volatility on both sides)
- Strangles (shorter premium for same risk)
- Any "premium-selling" strategy

It's also true to lesser degrees for:
- Defined-risk spreads (skew bounded but still very negative)
- Calendar spreads (short front-month is the dominant Greek)
- Most "income" strategies

Short-vol = short skew. There is no way around this.

### The Jurek-Stafford insight

**Jurek & Stafford (2015)** asked: how much of hedge-fund alpha is just compensation for short-skew exposure? Their answer: most of it. Hedge fund index returns from 1996-2012 are statistically indistinguishable from mechanical SPX put-writing once you correctly price the downside-skewed payoffs. The 6-10% pre-fee "alphas" reported by traditional risk-factor models *vanish*.

This is a profound result. It says: if you account for the price of accepting negative skew, the entire hedge fund industry is just selling insurance, not generating alpha.

The implication for retail premium-selling: if institutional sophistication can't outperform mechanical put-writing on a skew-adjusted basis, retail certainly can't.

### Bakshi-Crosby-Gao 2024

Bakshi, Crosby, and Gao (2024, *Mathematical Finance*) extended Jurek-Stafford in a formal ambiguity-averse and downside-risk-averse decision framework. They show that the apparent attractiveness of naive short-vol strategies largely *disappears* once realistic crash-aversion is priced in.

In other words: even if VRP is real (and it is), a sufficiently risk-averse investor would not increase utility by harvesting it without significant tail hedging or sizing discipline.

### The size of the skew "tax"

How much should we discount short-vol Sharpe? Various approaches give:
- Compare PUT skew (-2.09) to SPX skew (-0.81): roughly 2.5× more negative skew → meaningful discount
- Apply a risk-aversion-adjusted Sharpe penalty: roughly 30-50% haircut
- Compare Calmar (which captures some of the path issue): PUT 0.29 vs SPX 0.18 = 60% premium, not the 30% Sharpe ratio premium

Operational rule of thumb: **mentally apply a 30-50% Sharpe haircut to any short-vol strategy before comparing it to long-only or trend-following.**

### Misconception box

> **Misconception:** "Sharpe is the standard performance metric, so it must be reliable."
>
> **Correction:** Sharpe is a *standard* metric, which is different from a *reliable* metric for all strategies. It's reasonable for roughly Gaussian payoffs. It's misleading for options strategies, especially short-vol. Standard ≠ correct.

---

## 2.7 Step 6: Short-vol strategies look better than they are

We've now built the case. Putting it together:

- Short-vol = negatively skewed payoff
- Sharpe ignores skew
- Therefore Sharpe systematically *over-rates* short-vol
- The over-rating bias is consistent — you'll always see short-vol with attractive Sharpe even when it's a bad allocation

This is not an indictment of VRP harvest as a strategy. VRP is real (Chapter 6). The point is that *the metric you use to evaluate strategies has to match the distribution shape of those strategies.* Sharpe doesn't match short-vol distribution shape. Calmar, Sortino, and explicit path/stress analysis match better.

### Implication for portfolio construction

If you allocate by Sharpe alone, you'll over-allocate to short-vol relative to a properly-risk-adjusted optimal portfolio. The fix isn't "don't trade short-vol" — it's "use better metrics."

**Operational tools for evaluating short-vol strategies:**

1. **Path simulation:** run the strategy through 2008, 2018, 2020, 2022 explicitly. What was max DD? How long was recovery?
2. **Stress P&L:** what's the loss in SPX -10/-20/-35? Plus VIX +10/+25/+50?
3. **Margin expansion:** under PM, what's the cushion needed to survive S2 (Chapter 14)?
4. **Conditional drawdown:** what's the average drawdown beyond the 95th percentile?
5. **Tail beta:** what's the strategy's beta to equity in the worst 5% of equity months?

Any short-vol allocation should be sized based on these, not on Sharpe.

---

## 2.8 Step 7: Every short-vol trade needs tail-loss and margin-path analysis

The conclusion of the ladder. Here's the operational framing:

### The five-question stress test

Before allocating to any short-vol strategy, answer:

1. **What's my tail loss?** Specifically, ES₉₅ (expected shortfall at 95th percentile) — average loss in the worst 5% of months.
2. **What's the margin expansion under stress?** Run the position through SPX -20/VIX +25 and see how broker margin requirements change.
3. **Can I hold to expiry?** If the position MTMs to -X% in 30 days, would I be force-closed?
4. **Is the premium adequate compensation for the skew?** Apply the 30-50% Sharpe haircut. Is the strategy still attractive?
5. **What's the kill criterion?** Specific, measurable, pre-committed.

If you can't answer all five before entering, the position is too big or you don't understand it well enough.

### A worked example of the stress test

XSP cash-secured ATM monthly put-write at 25% of $1M portfolio = $250k notional.

1. **Tail loss:** based on Bondarenko 2019 historical data, ES₉₅ for monthly returns of ATM PUT is roughly -8% in a single month. On $250k position, that's -$20k. In the worst 1% (S3 scenario), losses can reach -$100-150k.

2. **Margin expansion:** cash-secured (no margin), so this risk is bounded by the cash collateral. *If* you scale up to use margin, expansion can be 2-3× initial requirement under PM in stress.

3. **Hold to expiry:** yes for cash-secured. If on margin, force-close risk depends on cushion.

4. **Premium vs skew:** PUT index has -2.09 skew vs SPX -0.81. Apply 30-50% Sharpe haircut. Bondarenko Sharpe was 0.65; haircut to 0.32-0.45. Realistic retail Sharpe: 0.20-0.40 (with the haircut + retail friction).

5. **Kill criterion:** halt new sales when VIX/VIX3M > 1.05 for 3 days, reduce sizing 50% when realized vol > 30, close when sleeve drawdown > 20% PTP.

This kind of explicit walkthrough is what distinguishes "I think VRP is positive EV" (a memo claim) from "I can size this correctly" (an operational position).

---

## 2.9 Misconception box: defined-risk doesn't fix the Sharpe trap

> **Misconception:** "Iron condors are defined-risk, so the skew problem doesn't apply."
>
> **Correction:** Iron condors cap your loss per trade, but you take the same shape of negatively-skewed bet hundreds of times. The aggregate skew of a many-trade portfolio of condors is still very negative. Plus, condors have terrible tail behavior because both sides of the structure can be threatened in a single move. CBOE's CNDR index returned approximately 690% from 1986-2024 vs. ~5,500% for SPX TR — *empirical evidence* that systematic condors underperform massively over time. The defined-risk feature doesn't fix the structural skew issue.

---

## 2.10 Self-check

1. Define skew and kurtosis. Why does each matter for options strategies?
2. Why is win rate not the same as expected value? Construct a 95% win-rate strategy with negative EV.
3. State the Sharpe ratio formula. Why does it systematically over-rate short-vol strategies?
4. What's the Jurek-Stafford finding? Why is it so important for VRP harvest decisions?
5. Apply the 5-question stress test to a hypothetical 30-delta XSP weekly put-write strategy at 30% of portfolio. What's your sizing decision?
6. Why does CNDR underperform SPX so dramatically despite being "defined risk"?

---

## Where this fits

Chapter 0 gave us distributions. Chapter 1 gave us why edges exist. Chapter 2 gives us why Sharpe lies for short-vol. Chapter 3 will give us realistic retail expectations using the haircut framework. Chapter 4 will formalize the conviction framework that uses all of this.

Without Chapter 2, the rest of the book's evaluations of short-vol strategies would seem arbitrary — "why is Sharpe 0.65 PUT not equivalent to Sharpe 0.5 SPX?" Now you know.

[← Previous: Chapter 1 — Four sources](02_ch01_four_sources.md) | [Next: Chapter 3 — Retail haircut →](04_ch03_retail_haircut.md)
