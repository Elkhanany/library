# Chapter 0 — Primitives
## Distributions, tails, leverage, margin, path

> **Why this chapter exists.** Without these primitives, everything that follows is memorization. With them, you can reason. Most retail traders have a vague sense of "risk" but lack the vocabulary to talk about it precisely. By the end of this chapter you'll be able to read any other chapter in this book and follow the reasoning.

---

## 0.1 Return distributions

A **return distribution** is the set of possible outcomes from a strategy, weighted by their probabilities. Every strategy you trade has one, whether you describe it that way or not.

**Toy example.** I sell you a coin flip: heads you pay me $1, tails I pay you $1. The distribution is two outcomes: +$1 with probability 50%, -$1 with probability 50%. Boring but instructive.

Now consider selling a 30-delta put on SPX for $3 of premium. The distribution looks roughly like:
- "Win" (option expires worthless): roughly 70% probability, +$3 outcome
- "Small loss" (modest pullback): roughly 20% probability, -$2 to -$10
- "Medium loss" (correction): roughly 8% probability, -$10 to -$30
- "Tail loss" (crash): roughly 2% probability, -$30 to -$100+

**The key point.** Most of the time you win a little. Occasionally you lose a lot. This is what a "negatively skewed" distribution looks like, and it characterizes almost every short-vol strategy.

### Four numbers describe a distribution

For any return distribution, four numbers tell you most of what you need to know:

1. **Mean** (expected value): the average outcome
2. **Variance** (or standard deviation, σ): how spread out the outcomes are
3. **Skewness**: whether the distribution leans right (positive) or left (negative)
4. **Kurtosis**: how "fat" the tails are vs a normal distribution

A normal (Gaussian) distribution is fully described by mean and variance — its skew is 0 and its kurtosis is 3. Real financial returns almost never look normal. SPX daily returns have skew around -0.7 and kurtosis around 18 — far fatter tails than normal.

### Worked example: same Sharpe, different outcomes

Two strategies, both have mean return 5% and standard deviation 10%, so both have Sharpe ratio 0.5.

**Strategy A:** roughly normal returns. Worst month: -8%. You can plan around it.

**Strategy B:** wins 95% of months by 1%, loses 5% of months by 14% on average. Same mean, same standard deviation, same Sharpe. But the worst month is *much* worse than -8%, and the loss months cluster (when you lose, you often lose multiple in a row).

**Sharpe doesn't see the difference.** This is not a small problem; it's the central reason why naive risk metrics underestimate the danger of short-vol strategies. Chapter 2 develops this fully.

---

## 0.2 Skew and kurtosis: the third and fourth moments

**Skew** measures asymmetry. Negative skew means the left tail is longer/fatter — large losses are more common than the equivalent large gains. Positive skew is the opposite.

- **Lottery tickets:** positive skew (small probable losses, rare large gains)
- **Insurance selling:** negative skew (small probable gains, rare large losses)
- **Most short-vol strategies:** negative skew, often severe

**Kurtosis** measures tail fatness. High kurtosis means more outcomes far from the mean than a normal distribution would predict. Markets have high kurtosis — "rare" events happen more often than naive models suggest.

### Why this matters operationally

If you're selling premium, you're collecting a small expected gain in exchange for accepting negative skew and high kurtosis. The premium has to compensate for:
- The expected loss in the tail
- The illiquidity of unwinding the position in stress
- The path-dependent risk of margin breach before mean reversion

If the premium is too small to compensate for these (which is often true for retail-sized accounts), you have a strategy with a positive *median* outcome but a negative *mean* outcome. You win most of the time and lose money over the long run.

### Misconception box

> **Misconception:** "I win 80% of my trades, so I have edge."
>
> **Correction:** Win rate alone is meaningless. A coin flip with -$1/+$0.10 payoff has 0% edge but you can engineer high win rates with bad EV trivially. What matters is the full distribution: mean × probability vs loss magnitude × probability, including the tail.

---

## 0.3 Drawdown

**Drawdown** is the peak-to-trough loss in equity over a period.

Two kinds matter:
- **Maximum drawdown (MaxDD):** largest historical peak-to-trough loss
- **Conditional drawdown (CDaR-α):** average drawdown beyond the α percentile

For a strategy with 5% mean return and 10% volatility, naive Gaussian math says max drawdown over 10 years should be around 25%. In reality, fat-tailed strategies often see 40-50% drawdowns.

**The Calmar ratio** = annualized return / max drawdown. For SPX long-only over 1990-2024, return ~10% and max DD ~55% give Calmar ~0.18. For PUT index, return ~9.5% and max DD ~33% give Calmar ~0.29 — a meaningful improvement, though paid for in path dependency.

### Why drawdown matters more than volatility

Volatility is symmetric. Drawdown is one-sided. A strategy can have low volatility and a 40% max drawdown if it crashes occasionally. From a portfolio-survival standpoint, drawdown is the binding constraint, not volatility.

**The 2008 framing.** A strategy that loses 40% requires a 67% recovery to break even. A strategy that loses 60% requires a 150% recovery. The asymmetry of drawdown is a real cost; recovery time is non-linear in loss size.

---

## 0.4 Leverage

**Leverage** is the ratio of total exposure to capital. A $1M account holding $1.4M of SPX has 1.4× leverage.

There are three economically distinct ways to take leverage:
1. **Borrow to buy** (margin loan, box spread financing): explicit cost = interest rate
2. **Use futures** (ES, MES): implicit cost = the basis between spot and futures, roughly SOFR + 10-20 bps
3. **Use options for replication** (LEAPs, deep-ITM calls): implicit cost = embedded leverage drag, typically 50-150 bps annualized (Frazzini-Pedersen 2012, 2022)

The first two are usually cheap. The third is expensive *and* has path-dependent properties (Greeks, margin expansion, assignment risk).

### The leverage trap

A common retail error is to construct a complex options structure that achieves leveraged equity exposure, then mistakenly believe the structure has "edge" beyond simple leverage. The structure usually does add a small positive expected return (some VRP, some skew premium), but it also adds:
- Embedded leverage drag (the option market's price for embedded leverage)
- Path dependency (the structure can be force-liquidated even if the terminal payoff is fine)
- Operational complexity (rolls, assignments, margin expansion)

The net is usually that the structure offers no edge over simple ES futures or box-spread financing once these costs are counted. We'll demolish this carefully in Chapter 11 (worked examples) and Chapter 10 (rejected).

---

## 0.5 Margin and path dependency

**Margin** is the capital your broker requires to hold a position. Two main models:

- **Reg-T:** fixed percentage of position size, simple but capital-inefficient
- **Portfolio Margin (PM):** based on stress-tested theoretical losses (typically ±15% SPX move plus IV shifts)

Under PM, margin requirements *expand non-linearly* in stress. In March 2020, many PM accounts saw requirements double or triple in 1-3 days. Brokers also raised house requirements during the crisis. This combination is what creates *path-dependent* risk: even if your terminal payoff is acceptable, you can be forced to close the position before the path completes.

### The forced-liquidation trap

Path dependency is the single most underestimated risk in retail options structures. Consider a 1-year SPX put spread that's "defined-risk" with $30 max loss per contract. Sold for $5 premium, max risk is $25.

If SPX drops 25% in 30 days and IV doubles, the spread might mark to -$22 even though terminal payoff is unchanged. If the position is large enough that this MTM exceeds your margin cushion, you're force-liquidated at -$22 — locking in 88% of max loss instead of holding to expiry where the spread might recover to -$10 or -$5.

**Operational consequence.** "Defined risk" describes the *terminal* loss. It does not describe the *path* loss. Every options structure must be sized to survive the path, not just the terminal payoff.

### Misconception box

> **Misconception:** "Defined-risk spreads are safe because I know my max loss."
>
> **Correction:** Defined terminal loss does not eliminate (a) mark-to-market loss requiring margin, (b) liquidity risk on the spread, (c) margin expansion that exceeds your cushion. The 2018 and 2020 episodes are full of "defined-risk" trades that nonetheless force-liquidated.

---

## 0.6 Correlation and tail correlation

**Correlation** measures how two return series move together over a sample. SPX vs Treasury bonds had correlation of roughly -0.3 from 2000-2020, meaning they tended to diversify each other.

**Tail correlation** is correlation conditional on extreme events. SPX vs Treasury bonds had tail correlation closer to -0.6 in 2008 (bonds rallied sharply as stocks crashed) — but +0.5 in 2022 (both fell together). The tail correlation flips on regime.

### The diversification illusion

Most "diversifying" strategies have decent unconditional correlation to equities (say, 0.3-0.5) but their tail correlation jumps toward 1.0 in crashes. Examples:
- BAB / low-vol: ~0.5 unconditional, ~1.0 in 2008
- Quality factor: ~0.5 unconditional, ~0.8 in 2008
- Carry trades: ~0.0-0.3 unconditional, ~0.7 in liquidity events
- Index VRP (PUT): ~0.5 unconditional, ~1.0 in left tail

**The genuine tail-diversifiers are rare:**
- Trend-following: ~0.0 unconditional, *negative* in slow drawdowns (8 of 10 largest 60/40 drawdowns positive)
- Long Treasuries: regime-conditional (worked 2000-2020, broke in 2022)
- Deep-OTM tail puts: pay in left tail but bleed in normal regimes

This is why allocation by individual Sharpe is the wrong framework. Allocation has to be by *contribution to tail behavior* of the portfolio.

---

## 0.7 Path dependency and the difference between MTM and terminal P&L

A strategy is **path dependent** if its MTM trajectory matters as much as its terminal payoff. Most options strategies are path-dependent in some way.

**Examples of path-dependent risk:**
- Margin expansion forcing liquidation before mean reversion
- Assignment risk on short options before expiry
- Theta decay that can't be recovered if MTM deteriorates and you have to close
- Forced rolling that changes the strategy from what you intended

**Examples of non-path-dependent strategies:**
- Long stock with no margin
- Cash-secured short put held to expiry (no margin call possible)
- Box spread financing (no MTM risk)

**Operational implication.** Every strategy you consider must be evaluated under "can this be force-liquidated mid-path." If yes, you must size for the path, not the terminal. This typically means sizing 30-50% smaller than what the terminal payoff would suggest is acceptable.

---

## 0.8 Liquidity

**Liquidity** is the cost of getting into and out of a position. Three components:

1. **Bid-ask spread:** the immediate cost of executing
2. **Market impact:** how much your order moves the price
3. **Stress liquidity:** how spreads widen in volatile conditions

For SPX/XSP options, normal-condition spreads are tight (a few cents on liquid strikes). In stress, spreads can widen 10-50× — meaning the cost of unwinding a position right when you most need to is enormous.

**Govindaraj-Li-Zhao (2020)** documented pre-earnings single-name option bid-ask spreads averaging 31.7% of mid-quote. Academic backtests use mids; live P&L uses real fills. The gap between paper and reality is mostly here.

### Operational rule

For any options strategy, ask: *"Could I close this position in the worst conditions?"* If the answer requires the bid to be tight, the answer is "probably not." Size accordingly.

---

## 0.9 Signal vs strategy vs allocation

These are three different things and conflating them produces garbage thinking.

- **Signal:** an observation that updates probabilities (e.g., "VIX/VIX3M > 1.05")
- **Strategy:** a rule that translates signals into trades (e.g., "halt put-write when signal triggers")
- **Allocation:** how much capital each strategy gets (e.g., "10% of portfolio risk to put-write sleeve")

A signal isn't tradable. A strategy without an allocation is a backtest. An allocation without strategies is a portfolio policy.

When you read trading content and someone says "this is a great edge," ask: are they describing a signal, a strategy, or an allocation? Most "great edges" are signals dressed up as strategies, with no allocation discipline behind them.

---

## 0.10 Math you need to internalize

The book uses a small recurrent set of equations. Memorize the meaning, not just the form.

**Expected value:**
$$E[R] = pG - (1-p)L - c$$

where p is win probability, G is gain on win, L is loss on loss, c is friction (commissions, taxes, slippage).

**Sharpe ratio:**
$$\text{SR} = \frac{E[R - r_f]}{\sigma_R}$$

excess return per unit of volatility.

**Tail loss (Expected Shortfall):**
$$\text{ES}_\alpha = E[L \mid L > \text{VaR}_\alpha]$$

average loss conditional on being in the worst α tail.

**Retail-realism haircut:**
$$\text{SR}_\text{user} = \text{SR}_\text{paper} \times h_\text{index} \times h_\text{fund} \times h_\text{tax/exec}$$

each h is typically 0.7-0.9; cumulative haircut is often 0.3-0.5.

**Portfolio variance:**
$$\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$$

individual Sharpes don't aggregate; covariance dominates.

**Conviction threshold (introduced fully in Chapter 4):**
$$\text{Trade only if } \hat{\mu}_\text{net} - \lambda \cdot \text{ES}_{95} - \kappa \cdot C_\text{exec} > 0$$

expected return must beat tail-risk penalty plus execution cost.

These six equations recur throughout the book. Don't gloss over them — they're the language the rest of the framework is written in.

---

## 0.11 Self-check

Before moving to Chapter 1, can you answer these without flipping back?

1. What's the difference between mean, skew, and kurtosis? Why does skew matter for options strategies?
2. Why isn't a high win rate the same as positive expected value?
3. What is path dependency, and why does it make "defined-risk" trades not actually risk-defined?
4. What's the difference between unconditional correlation and tail correlation? Why does it matter for portfolio construction?
5. State the Sharpe ratio formula and explain why it's misleading for negatively-skewed strategies.
6. Why is a $1M account with $1.4M of SPX exposure via LEAPs riskier than $1.4M via ES futures, even though the delta exposure is the same?

If you can't answer all six, re-read the relevant section. The rest of the book assumes these are second nature.

---

## Where this fits

Chapter 1 will use these primitives to explain *why* edges exist in the first place — the four sources (risk premium, behavioral, institutional, microstructure). Chapter 2 will build on the distribution material to explain why Sharpe lies for short-vol. Chapter 3 will use the haircut equation to derive realistic retail expectations. Without Chapter 0, those chapters are claims; with Chapter 0, they're conclusions.

[← Back to Home](index.md) | [Next: Chapter 1 — Why edges exist →](02_ch01_four_sources.md)
