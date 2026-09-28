# Chapter 8 — Structural / tactical overlays
## FOMC cycle, EOQ rebalancing, OPEX, Halloween

> **Core intuition.** Overlays are calendar or flow-based effects that *modulate* exposure to other premia rather than serving as standalone strategies. The economic magnitudes are typically small (10-40 bps annualized), so implementation must be cheap. They're best expressed as sizing modulation of existing positions, not as separate sleeves.

---

## 8.1 What overlays are and aren't

### Definition
An overlay is a rule that systematically scales exposure up or down based on calendar date, regime indicator, or institutional flow pattern. It doesn't generate return on its own; it *modulates* the return on other strategies.

### Why this matters
A common retail error is treating overlays as standalone strategies. Examples:
- "I'll trade SPX only on FOMC even-weeks" → too restrictive, transaction costs eat the small premium
- "I'll trade the EOQ rebalance every quarter" → small premium per trade, only ~4 trades/year
- "I'll sell premium specifically on OPEX week" → narrow window, post-0DTE the effect is diluted

Better framing:
- "I'll modulate equity sizing across FOMC cycle weeks" → uses existing positions
- "I'll add small tactical positions in EOQ when divergence is extreme" → augments existing portfolio
- "I'll be aware of OPEX dynamics but not trade specifically around them" → context, not strategy

The overlay improves portfolio Sharpe by 0.05-0.20 *if implemented cheaply*. Implemented expensively, it's negative.

---

## 8.2 Cieslak FOMC even-week cycle

### Core intuition
Cieslak-Morse-Vissing-Jorgensen (2019) showed that since 1994, **the entire equity premium has been earned in even weeks** (week 0 of the FOMC cycle, plus weeks 2, 4, 6 since the cycle is 6 weeks). Odd weeks have produced near-zero or negative returns. The mechanism is the "Fed put" — Fed reaction function reduces tail risk during expected announcement windows.

### Toy example
FOMC meets every 6 weeks. "Week 0" is the meeting week. "Week 1" is the week after. Etc. Cieslak et al. found:
- Week 0: ~14 bps/day average return
- Weeks 2, 4: ~11 bps/day
- Weeks 1, 3, 5: ~0 bps/day

If you held equity only during even weeks (3 out of every 6 weeks), you captured most of the long-run equity premium with half the time exposure.

### Formal object
Even-week return in cycle time:
$$E[R_t \mid t \in \{w_0, w_2, w_4\}] \gg E[R_t \mid t \in \{w_1, w_3, w_5\}]$$

### Evidence
- Cieslak-Morse-Vissing-Jorgensen (2019, *JF*) — original paper
- Sample: 1994-~2014 in their analysis
- **Important caveat (reviewer corrected):** post-2019, post-COVID, post-2022 hiking cycle, OOS replication is limited. Some practitioner replications suggest the effect held through 2019; data through the 2022-2024 aggressive hiking cycle is thin and possibly disrupted.

### Why it exists
Institutional/structural (Source 3): Fed policy reaction function reduces equity tail risk during expected announcement windows. The "Fed put" creates asymmetric upside vs downside in even weeks.

### Retail implementation
- **Vehicle:** ETF rotation (full SPY in even weeks, reduced in odd weeks). No derivatives unless overlay capital >$200k.
- **Sizing rule:**
  - Week 0, 2, 4: equity exposure at 1.0× baseline
  - Weeks 1, 3, 5: reduce equity exposure 20-30%
- **Transaction cost discipline:** if costs exceed 100 bps annualized, simplify (just reduce in week 1, not all odd weeks)

### Failure mode
- The effect could decay with publication and Fed transparency reforms (similar to pre-FOMC drift, which decayed post-2015)
- The aggressive 2022-2024 hiking cycle may have disrupted the pattern
- OOS evidence is thinner than the original paper suggests

### Decision rule (today)
Implement modestly. **Treat as T2 overlay, not structural certainty.** Reduce equity 20-30% in odd weeks via ETF rotation; full exposure in even weeks. Track personal performance vs static-allocation baseline; suspend if 2-year rolling odd-week return ≥ even-week return.

### Misconception box
> **Misconception:** "FOMC cycle is robust because it has clear Fed-policy mechanism."
>
> **Correction:** Mechanism plausibility doesn't guarantee persistence. Pre-FOMC drift had a clear mechanism and decayed post-2015 due to Fed transparency reforms. FOMC even-week cycle could decay similarly. Use it but don't bet the portfolio on it.

### Self-check
1. State the Cieslak finding.
2. What's the implementation rule?
3. Why is the OOS evidence concern important?

---

## 8.3 End-of-quarter rebalancing flow

### Core intuition
60/40 pension funds, target-date funds, and similar mandates rebalance toward target weights at quarter-end. If equities outperformed bonds during the quarter, the fund is now over-weight stocks and rebalancers will *sell* equities, *buy* bonds. The reverse if equities under-performed. Front-running this flow earns a small premium.

### Toy example
Q1 2024: SPX +10%, 10-year Treasury -1%. A 60/40 fund that started the quarter at 60/40 is now at ~63/37. To return to 60/40, the fund must sell ~3% of stocks and buy ~3% of bonds. Aggregated across $5T in 60/40 mandates, that's ~$150B of expected stock selling and bond buying in the last week of March.

### Formal object
$$\text{Imbalance}_t = w_t - w^* = \text{drift from target weight}$$

When stocks outperformed, $w_t^{\text{stocks}} > w^*$ → rebalancers sell stocks. Front-runner: short ES / long ZN.

### Evidence
- Etula-Rinne-Suominen-Vaittinen (2020, *RFS*) "Dash for Cash"
- NBER WP 33554 (2024) "The Unintended Consequences of Rebalancing" — predictable next-day equity-return effects of ~17 bps when stocks are overweight, larger effects with extreme divergence

### Why it exists
Institutional friction (Source 3). Mandate-driven flow is mechanical and not driven by fundamental views. The premium compensates the front-runner for providing liquidity.

### Retail implementation
- **Signal:** SPX-bond divergence > ±1.5% over the quarter
- **Direction (corrected from v1!):**
  - Stocks OUTPERFORMED bonds → SHORT ES / LONG ZN (rebalancers will sell stocks, buy bonds)
  - Stocks UNDERPERFORMED bonds → LONG ES / SHORT ZN (rebalancers will buy stocks, sell bonds)
- **Timing:** enter T-5 trading days of quarter, exit T+1 to T+3 of new quarter
- **Sizing:** very small until you have personal data — 0.5% of portfolio at risk per trade for first 8 quarters

### The sign correction (important)
The reviewer of v1 caught a sign error in the original framework. **Restating clearly:**

> **If equities outperformed bonds in the quarter, you go short equities and long bonds.** This is because the rebalancers will sell their equity overweight to buy the bond underweight — front-running their flow means doing the same thing they're about to do.

This is the most important mechanical correction in the document; I want to flag it explicitly.

### Failure mode
- Effect requires meaningful divergence (>1.5%); skip flat quarters
- Flow is sometimes preempted by other market participants
- Recent paper, retail-replication is **untested**

### Decision rule (today)
**Treat as T2, "promising, replication required."** Tiny size for the first 8 quarters of personal data. Don't size up until you have statistical confidence in your own execution.

Kill criteria:
- After 4 quarters, hit rate < 50% OR net P&L negative → suspend
- Quarterly divergence < 1.5% → skip the trade

### Misconception box
> **Misconception:** "I can size this big because the academic Sharpe is good."
>
> **Correction:** The NBER 2024 paper is recent. Live retail replication is untested. There's a significant gap between "academic effect exists" and "I can capture it after slippage and execution." Size like a research project, not a foundation strategy.

### Self-check
1. State the EOQ rebalancing direction rule. Don't get the sign wrong.
2. What's the divergence threshold for entering?
3. Why should retail position size be tiny initially?

---

## 8.4 OPEX-week tilt

### Core intuition
The third Friday of each month is monthly options expiration ("OPEX"). Stivers-Sun (2013) documented a ~30 bps/week excess return on option-active large caps during OPEX week. Mechanism unclear, possibly related to dealer hedging into expiry.

### Toy example
Hold SPY only during the week of monthly OPEX (3rd Friday of the month). Historically, this captured ~30 bps/week of excess return concentrated in option-heavy large caps.

### Evidence
- Stivers-Sun (2013, *JBF*) — original SPY OPEX-week strategy
- **Decay caveat:** post-2022 with the explosion of weekly and 0DTE options, the importance of monthly third-Friday expiration has diluted significantly. Not retested rigorously in the post-0DTE regime.

### Why it exists
Microstructure / institutional (Sources 3, 4). Dealer hedging into expiry creates flow patterns; option-related rebalancing concentrates around OPEX.

### Retail implementation
- Don't allocate explicitly. Awareness only.
- If implementing, be aware that the post-0DTE regime may have already eroded the effect

### Failure mode
- Post-0DTE dilution
- Effect may already be priced in
- Small per-trade premium dominated by retail transaction costs

### Decision rule (today)
**Don't trade specifically around OPEX.** Use awareness to avoid getting caught in dealer-hedging-driven moves around expiry, but don't size positions to capture the effect.

### Self-check
1. Why has the OPEX effect likely diluted post-2022?
2. What's the operational implication?

---

## 8.5 Halloween / Sell-in-May

### Core intuition
"Sell in May and go away" — equities have historically had higher returns in November-April than May-October. The pattern persists across 36+ countries despite no clean mechanism.

### Toy example
SPX 1950-2024:
- November-April average return: ~7%
- May-October average return: ~2%

The 5% gap is large, persistent, and global. Yet no satisfying causal mechanism exists.

### Evidence
- Bouman-Jacobsen (2002, *AER*) — original: 36 of 37 countries show effect
- Jacobsen-Zhang (2021, *IRFA*) — 109 markets, 323 years aggregate, 82 of 109 show effect

### Why it exists
**No clean mechanism.** Possibilities:
- Tax timing (year-end harvest, January reinvest)
- Summer vacation reduced participation
- Seasonal mood (SAD)

The empirical persistence is striking despite unclear mechanism, which is itself a flag — either we're missing the mechanism, or it's sample-specific bias.

### Retail implementation
- Soft tilt at most. Reducing equity exposure 10-20% in May-October has small positive expected effect.
- Not enough to justify trading costs unless implemented at the rebalancing level

### Decision rule (today)
**Soft tilt only.** If you rebalance annually, time the rebalance to add equity in November and reduce in May. Don't run a separate strategy for it.

### Self-check
1. State the Halloween effect.
2. Why is the lack of mechanism concerning?
3. What's the operational implementation?

---

## 8.6 Turn-of-month

### Core intuition
The first 4-5 trading days of a month show modestly positive average returns, attributed to month-end pension contributions and 401k deposits being deployed in early days.

### Evidence
Modest empirical pattern; persistence narrowing as cash flow patterns change.

### Decision rule (today)
**Marginal.** Don't allocate against this. Useful only as a soft consideration when timing larger discretionary entries — if you have a discretionary buy decision, prefer the first week of the month over the last.

---

## 8.7 Aggregate overlay allocation

### Combined effect
Adding all overlays:
- FOMC even-week tilt: +0.10-0.30 Sharpe (with caveats)
- EOQ rebalancing: +0.05-0.15 Sharpe (untested live)
- OPEX: ~0
- Halloween: +0.05-0.10 Sharpe (rebalance timing)
- Turn-of-month: ~0

Net realistic addition to portfolio Sharpe: 0.10-0.30 if all implemented well, near zero or negative if implemented expensively.

### Operational principle
Overlays are *cheap* tilts. The moment you're paying meaningful transaction costs, taxes, or attention to capture them, they're not worth it. The right framing:
- FOMC cycle: built into your equity rebalancing rules, no separate execution
- EOQ rebalancing: a small tactical sleeve at <0.5% NAV per trade
- Halloween: timing of your annual rebalance
- OPEX: awareness only
- Turn-of-month: awareness only

If any overlay requires extensive operational infrastructure, it's miscategorized.

---

## 8.8 Misconception box (chapter level)

> **Misconception:** "Multiple overlays can stack to add 0.5+ Sharpe."
>
> **Correction:** Overlays are cheap to add but cheap to overstate. The aggregate addition is 0.10-0.30 Sharpe, and that's optimistic. They don't cleanly stack because (a) they overlap (FOMC cycle and Halloween both affect equity timing), (b) they have shared regime sensitivities, (c) implementation costs eat the small premiums. **Don't build a portfolio around overlays.**

---

## 8.9 Self-check (chapter)

1. State the five overlays. Which has the largest expected Sharpe contribution?
2. Get the EOQ rebalancing direction right: stocks outperform bonds → which way is the trade?
3. Why is the OPEX effect likely diluting post-2022?
4. Apply the conviction score (Chapter 4) to a hypothetical "trade FOMC even-weeks" strategy. What's the binding constraint?
5. Why are overlays "modulators" rather than "standalone strategies"?

---

## Where this fits

Chapter 6 covered foundation premia. Chapter 7 covered factor tilts. Chapter 8 covers structural overlays. Chapter 9 covers regime filters. Chapter 10 covers rejected/non-retail.

Overlays are the smallest contributors to portfolio Sharpe but the most operationally seductive — they have specific calendar dates and clear stories. Discipline yourself to treat them as small tilts, not foundation strategies.

[← Previous: Chapter 7 — Factor tilts](08_ch07_factor_tilts.md) | [Next: Chapter 9 — Regime filters →](10_ch09_filters.md)
