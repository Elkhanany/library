# Chapter 14 — Portfolio framework, kill criteria, revalidation
## The longest-time-horizon view

> **Core intuition.** Individual strategies don't survive on individual Sharpes — they survive because the *portfolio* survives. This chapter is about capital allocation across sleeves, the kill criteria that protect the portfolio when individual strategies fail, the behavioral safeguards that protect the portfolio when *you* fail, and the revalidation cadence that prevents the framework itself from going stale.

---

## 14.1 The reference allocation

A reasonable default for a $1M portfolio committed to the framework in this book:

| Sleeve | Capital allocation | Risk allocation | Vehicle | Category |
|---|---|---|---|---|
| Core equity (ERP) | 50-55% | 50-55% | SPY/VTI + QUAL/MTUM tilts | Foundation |
| VRP harvest | 10-15% | 10-15% | XSP cash-secured monthly puts | Foundation |
| Trend-following | 10-15% | 12-18% | DBMF or KMLM | Foundation |
| Cross-asset carry | 0-10% | 0-10% | Limited retail vehicles | Foundation |
| Tactical / overlays | 5-10% | 5-10% | EOQ rebalance, tactical equity sizing | Overlay |
| Cash buffer | 5-15% | 0% | Money market / T-bills | Liquidity |

**Notes.**
- "Capital allocation" is dollars. "Risk allocation" weights by vol — trend has higher vol per dollar than equity, so the same dollars give more risk.
- The cash buffer isn't dead capital. It's the optionality to buy stress, meet margin calls without forced liquidation, and absorb a tactical sleeve drawdown without compromising foundation.
- Cross-asset carry is optional given retail vehicle limitations.

### Why this allocation
- 70-80% in foundation premia (durable risk premia)
- 5-10% in overlays (modest enhancement, not a foundation)
- 10-15% in cash buffer (insurance against forced liquidation)
- Factor tilts live *inside* the equity sleeve, not as a separate line

---

## 14.2 Risk budget framework

### The principle
Allocate by *risk contribution*, not dollar weight. A 15% allocation to trend may contribute 18-20% of portfolio risk; a 15% allocation to long bonds may contribute 8-10%. The dollar weights mean nothing without the risk weights.

### The math
Portfolio variance:
$$\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$$

Risk contribution of sleeve $i$:
$$RC_i = w_i \cdot \frac{\partial \sigma_p}{\partial w_i} = w_i \cdot \frac{(\Sigma w)_i}{\sigma_p}$$

In practice: estimate the volatility and correlation of each sleeve's returns. Compute risk contribution. Adjust dollar weights so risk contributions match your target.

### The simpler heuristic
For most retail portfolios, target equal risk contributions across foundation sleeves. If equity vol is 16%, trend vol is 12%, VRP vol is 10%, you need *more dollars* in trend and VRP than in equity to equalize risk contribution.

But equal risk contribution often produces too little equity exposure. A pragmatic target:
- Equity ~ 50% of portfolio risk
- VRP, trend, carry combined ~ 30% of portfolio risk
- Tactical/overlays ~ 10%
- Cash ~ 0% (definitionally)

### Position sizing from stress loss
A more direct sizing rule, used by Ahmed's previous SPXW framework:

$$n \leq \left\lfloor \frac{B_\text{exp}}{L_\text{max}} \right\rfloor$$

where $B_\text{exp}$ is the expected loss budget for the period and $L_\text{max}$ is the maximum loss per trade (or per position). This translates a *budget* into a *contract count*. It's mechanical and bypasses intuition-based sizing.

The same logic at the sleeve level: if your S2 stress P&L on the sleeve is -X% of NAV, and your budget is -Y% NAV, then the sleeve size = Y / X × current sleeve size. Mechanical resizing on stress.

---

## 14.3 Stress testing the portfolio

### The four scenarios
Test the full portfolio under:

- **S1 (mild):** SPX -10%, VIX +10
- **S2 (moderate):** SPX -20%, VIX +25
- **S3 (severe):** SPX -35%, VIX +50
- **S4 (1987-style gap):** overnight -22%, VIX +80

### Worked example
$1M portfolio in the reference allocation:

| Sleeve | $ | S1 P&L | S2 P&L | S3 P&L | S4 P&L |
|---|---|---|---|---|---|
| Core equity | $550k | -55k | -110k | -193k | -121k |
| VRP harvest | $125k | -25k | -50k | -110k | -80k |
| Trend | $125k | flat | +10k | +30k | +5k |
| Carry | $50k | -3k | -8k | -15k | -10k |
| Tactical | $75k | -3k | -8k | -15k | -10k |
| Cash | $75k | 0 | 0 | 0 | 0 |
| **Total** | **$1M** | **-86k (-9%)** | **-166k (-17%)** | **-303k (-30%)** | **-216k (-22%)** |

### What "survivable" means
- **S1 survivable:** absolutely. -9% is a normal year.
- **S2 survivable:** yes. -17% is painful but not catastrophic; recovery is feasible in 2-3 years.
- **S3 survivable:** yes, with discipline. -30% is severe. Don't add risk, don't capitulate, hold the foundation.
- **S4 survivable:** yes. -22% with overnight gap is recoverable; the cash buffer prevents force-liquidation.

If your stress P&L makes any of these "borderline" or "no" — your sleeves are too big or your tactical bets are too big. Resize.

### The gut check
The **single most important question:** if the portfolio is at S3 (-30%) and another -10% happens tomorrow, are you still rational? Or do you panic-exit?

If you panic-exit, your *behavioral* sizing is wrong even if your *mathematical* sizing is fine. Reduce by 25% from what the math says is acceptable.

---

## 14.4 Kill criteria at multiple levels

Kill criteria operate at three levels. All three must exist.

### Level 1: Per-strategy kill criteria
Each strategy has its own kill rules. Examples from previous chapters:

- **VRP harvest:** halt new sales when VIX/VIX3M > 1.05 for 3 days; reduce 50% when realized vol > 30; close when sleeve drawdown > 20% PTP
- **Trend:** vehicle drawdown > 25% PTP; tracking error > 4% annualized
- **EOQ rebalance:** suspend if 4-quarter hit rate < 50%
- **Factor tilts:** 24-month rolling Sharpe < 0 → reduce 50%

### Level 2: Sleeve kill criteria
Each *category* has its own kill rules, in case multiple strategies in the category fail simultaneously:

- **Foundation:** if 2 of 4 foundation sleeves trigger their per-strategy kill, reduce all foundation sleeves 25%
- **Factor tilts:** if 3 of 5 factors are in deep drawdown, suspend new factor allocations for 6 months
- **Overlays:** if aggregate overlay P&L is negative for 2 years, simplify (drop the costliest overlays)
- **Tactical:** sleeve drawdown > 30% → suspend all tactical for 3 months

### Level 3: Portfolio kill criteria (behavioral)
The most important. If the *portfolio* exceeds certain thresholds, automatic actions take effect regardless of individual strategy logic:

- **Portfolio drawdown > 25% PTP:** halt all *discretionary* tactical activity for 30 days. Foundation sleeves continue mechanically; tactical bets are frozen.
- **Personal behavioral state degraded:** if you've been making impulse decisions, sleeping poorly, or trading outside written rules — halt new entries for 1 week minimum.
- **Account margin cushion < 30%:** force-deleverage by closing the smallest tactical positions first.

### The behavioral cooling-off period
The 25% drawdown / 30-day cool-off is not optional. It's the single most valuable behavioral safeguard in the framework. Reasons:

1. Drawdowns produce sub-optimal decision-making. The 30-day cool-off forces decisions to be made later, when emotional state is better.
2. Forced halt prevents revenge trading and "make it back" behavior.
3. The mechanical foundation continues running, so you don't sacrifice the long-term anchor — only the discretionary overlay.
4. Knowing the cool-off exists *in advance* makes the drawdown less catastrophic psychologically. You have a rule to point at.

This is the structural defense against the behavioral haircut from Chapter 3.

---

## 14.5 Monitoring cadence

### Daily (5-15 min)
- Position file: are positions where they should be?
- Filter check: VIX/VIX3M, realized vol, MOVE
- Account margin cushion

### Weekly (30-60 min)
- Per-strategy P&L vs benchmark
- Filter regime state (Chapter 9 score)
- Pipeline review: are observations being interpreted into trades correctly?

### Monthly (2-4 hours)
- Sleeve P&L attribution
- Compare actual to expected (is the haircut tracking? Is anything drifting badly?)
- Adjust regime sizing if persistent regime change
- Review the strategy diary

### Quarterly (4-8 hours)
- Full portfolio rebalance
- Review per-strategy kill criteria — any close to triggering?
- Update setup cards (Chapter 12) for any meaningful changes
- Honest review: are the strategies actually doing what they're supposed to?

### Annually (1-2 days)
- Full portfolio review
- Compare realized to expected on every sleeve
- Decide on persistence: any sleeve in 2+ years of drawdown that should be revalidated?

### Every 5 years
- **Thesis revalidation.** This is the one most people skip and shouldn't.

---

## 14.6 The five-year revalidation

Every 5 years, the entire framework should be re-examined:

1. **Are the foundation premia still real?** Has new evidence emerged that ERP, VRP, trend, or carry has structurally changed?
2. **Have any factors decayed below your threshold?** Quality, momentum, value, low-vol — any of these should be replaced or removed?
3. **Have any overlays decayed?** FOMC cycle? OPEX? EOQ?
4. **Have any rejected strategies been re-validated?** Sometimes the literature reverses (intangibles-adjusted value 2024 example).
5. **Are the kill criteria still calibrated correctly?** Maybe the 25% drawdown threshold should be 20%, or 30%.
6. **Is the conviction score still working?** Are high-C trades actually outperforming low-C trades in your account?

### Why this matters
Without revalidation, the framework calcifies. Pre-FOMC drift was a real edge until 2015; it's not now. People who didn't revalidate continued allocating to it long after it stopped working. Same risk applies to any edge in this book.

The 5-year cadence is roughly the pace at which structural market changes accumulate enough to matter without being dominated by short-term noise.

### What revalidation looks like in practice
- Read the most recent academic literature on each foundation premium
- Track 5-year rolling Sharpes against the longer-term expectation
- Test alternative implementations (e.g., does AVUV outperform IVE for the value tilt?)
- Revisit assumptions about haircuts and execution costs
- Update the framework document (this book) where evidence has changed

If revalidation reveals that 2 of 4 foundation premia have meaningfully changed, the framework needs serious revision, not a tweak. Be honest with yourself.

---

## 14.7 Behavioral safeguards (the structural fix to Chapter 3)

Chapter 3 documented that the behavioral haircut is large. Chapter 14 specifies the structural defenses.

### The non-negotiable safeguards
1. **Written rules for entry, exit, sizing.** Every strategy has a setup card (Chapter 12).
2. **Pre-committed kill criteria at three levels** (this chapter).
3. **Monthly strategy diary.** Documenting what you actually did vs the rules.
4. **Quarterly variance review.** If your account is consistently 200+ bps behind benchmarks, the gap is behavioral.
5. **25% drawdown / 30-day cool-off.** The single most important safeguard.

### Optional but recommended
- **Mechanical execution where possible.** Scheduled rebalances. Conditional orders.
- **Trading partner / spouse review.** Someone else seeing the trades reduces ego-driven decisions.
- **Time delay on large new positions.** "If I still want this trade in 24 hours, I'll do it." Most impulse trades fail this test.
- **Capacity discipline.** Don't trade beyond your operational capacity (e.g., 68 trades in a day exceeds operational capacity for any retail trader; the historical evidence is that this overtrading destroys returns).

### What good looks like
A trader following the framework should have:
- ~85-95% of variance in P&L explained by the *intended* strategies
- ~5-15% variance from execution friction and minor errors
- Near-zero variance from "trades I didn't plan to make"

If the third bucket is large, behavioral discipline isn't working. Add safeguards.

---

## 14.8 The selectivity principle (key)

One of the highest-yield insights from your previous portfolio analysis: **selectivity beats activity.**

The 68-trades-in-a-day data point is the most informative single observation about overtrading destroying returns. The BTF-style bot strategy that succeeded was successful because of *extreme selectivity* — entire weeks skipped when criteria weren't met.

### What selectivity looks like
- Most days, no new positions
- Most weeks, 1-3 new positions across the entire portfolio
- Most months, 4-8 positions with explicit conviction scores
- Most quarters, 1-2 deep dives that produce thesis changes

### The bias toward action
Retail traders bias toward action because action *feels* productive. Doing nothing feels lazy or "missing opportunity." The data systematically rewards the opposite: doing nothing is the highest-EV move on most days.

### The pipeline applied to selectivity
The signal-to-trade pipeline (Chapter 13) imposes selectivity by structure. Most observations don't pass interpretation. Most interpretations don't pass conviction. Most conviction-passing ideas don't pass sizing. The trades that *do* exist have all four gates clear, which is why they should be larger and more durable than the trades you'd otherwise make.

---

## 14.9 What this chapter is really about

Three things:

1. **Capital allocation across sleeves** that respects risk contribution and stress survivability.
2. **Multi-level kill criteria** that protect the portfolio when individual strategies, sleeves, or your behavior fails.
3. **Revalidation cadence** that keeps the framework alive across 5+ year horizons.

Without these, individual strategy success is irrelevant — the portfolio dies in stress, or the framework decays, or you behavioral-haircut your way into mediocrity.

The structure here is the *deliverable* of the entire book. Foundation, factors, overlays, filters, conviction, taxonomy — they're all upstream of this. The portfolio framework is where the abstract becomes the actual.

---

## 14.10 Self-check (chapter)

1. State the reference allocation. What's the rationale for each sleeve?
2. Compute risk contribution: if equity vol is 16%, trend vol is 12%, and you allocate 60/40 dollars, what's the approximate risk contribution of each? (Assume zero correlation for simplicity.)
3. State the three levels of kill criteria. Why do you need all three?
4. Why is the 25% drawdown / 30-day cool-off the single most important safeguard?
5. Walk through the monitoring cadence. What's the longest-frequency review and why?
6. State the selectivity principle. Why does it beat activity?

---

## Where this fits

Chapters 0-5 built the conceptual framework. Chapters 6-10 populated the framework with specific edges. Chapters 11-13 made it operational. Chapter 14 is the highest-time-horizon view: capital allocation, kill criteria, revalidation cadence, behavioral safeguards.

Chapter 15 (next) is reference material — glossary, reading list, math summary card. After Chapter 14, you've absorbed the framework. Chapter 15 is for looking up specifics later.

[← Previous: Chapter 13 — Pipeline](14_ch13_pipeline.md) | [Next: Chapter 15 — Reference →](16_ch15_reference.md)
