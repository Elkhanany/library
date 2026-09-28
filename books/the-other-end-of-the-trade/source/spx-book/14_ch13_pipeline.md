# Chapter 13 — The signal-to-trade pipeline
## From observation to position to invalidation

> **Core intuition.** Every action in your portfolio should pass through the same five-step grammar: observation → interpretation → trade implication → sizing → invalidation. This grammar is what makes "high-conviction trading" operational rather than aspirational. Most retail trading fails by skipping steps — observing and trading without explicit interpretation, sizing, or invalidation criteria.

---

## 13.1 The five steps

The pipeline:

$$\text{Observation} \rightarrow \text{Interpretation} \rightarrow \text{Trade implication} \rightarrow \text{Sizing} \rightarrow \text{Invalidation}$$

Each step is distinct and required:

| Step | Question answered | Output |
|---|---|---|
| **Observation** | What did I see? | Specific, measurable signal |
| **Interpretation** | What does it mean? | Mapping signal to regime / risk update |
| **Trade implication** | What action does it imply? | Specific position / non-position decision |
| **Sizing** | How much? | Position size derived from loss budget |
| **Invalidation** | What would prove me wrong? | Specific kill condition |

Skipping any step produces undisciplined trading.

---

## 13.2 Step 1: Observation

### What an observation is

A specific, *measurable* market state. Examples:
- "VIX/VIX3M ratio crossed 1.05 today"
- "21-day realized vol on SPX is 32% vs implied 26%"
- "TED spread widened from 25 bps to 95 bps over 5 days"
- "MTUM has underperformed SPX by 8% over the trailing 6 months"

### What an observation is NOT

- "The market feels overextended" (not measurable)
- "There's a lot of bearish news" (vague)
- "Twitter is bullish on AI again" (sentiment-narrative, not data)
- "I think we're due for a correction" (prediction, not observation)

The pipeline starts with measurable inputs only. If you can't define the threshold, the observation step has failed.

### Operational practice
Maintain a written list of observation triggers — the specific measurable conditions that earn an interpretation step. For most traders, ~5-10 triggers cover 95% of legitimate trade situations. The rest can be researched as ad-hoc situations require.

A reasonable trigger list:
- VIX/VIX3M ratio thresholds (filter)
- 21-day realized vs implied (filter)
- TED, MOVE, HY OAS thresholds (filter)
- Quarterly SPX vs bond divergence (overlay)
- FOMC schedule position (overlay)
- 24-month rolling factor Sharpe (factor tilt review)
- Sleeve drawdown thresholds (kill rule)
- Portfolio drawdown threshold (behavioral kill)

That's it. ~8 observation triggers cover the systematic decision space.

---

## 13.3 Step 2: Interpretation

### What interpretation does

Maps the observation to a regime / risk update. The interpretation is the bridge between data and action.

### Worked example
- **Observation:** "VIX/VIX3M = 1.10 for 3 consecutive closes"
- **Interpretation:** "Term structure is backwardated, indicating elevated near-term hedging demand. Historically, this regime is associated with higher realized vol, wider option spreads, and possible margin expansion under PM. Short-vol strategies face structural headwind during this regime."

The interpretation should:
1. Translate the observation into a regime characterization
2. Reference the body of evidence supporting the interpretation
3. Be specific about what's now elevated/diminished risk

### Common failures

**Over-interpretation:** "VIX backwardated = market about to crash." This is prediction dressed as interpretation. Backwardation indicates elevated near-term vol; *direction* is unpredictable.

**Under-interpretation:** "VIX backwardated, idk what to do." If you can't translate the signal to a regime characterization, the signal isn't useful.

**Narrative-interpretation:** "VIX backwardated because the AI bubble is popping." The narrative may or may not be true; the interpretation should be regime-based, not story-based.

### Operational practice
Each observation trigger has a written interpretation. When the trigger fires, you read the interpretation, you don't compose a new one. The discipline is in pre-committing what each signal means before it fires.

---

## 13.4 Step 3: Trade implication

### What the trade implication does

Translates the interpretation into a specific action (or non-action). This is where conviction analysis happens (Chapter 4).

### Worked example
Continuing from the VIX backwardation example:
- **Observation:** VIX/VIX3M = 1.10 for 3 days
- **Interpretation:** Backwardated, stress regime
- **Trade implication:**
  - Halt new short-vol entries (CARD 02 kill rule)
  - Reduce existing XSP put-write 50%
  - Maintain equity allocation (no rule for direct equity reduction at this filter level)
  - Maintain trend allocation (filter doesn't apply)
  - Consider modest equity beta reduction if other filters also fire

### The non-action implication

Sometimes the right trade implication is "do nothing new." Examples:
- Filter triggered but no existing position to modify
- Observation falls within normal-regime range
- Conviction score insufficient (< 0.3)
- Already implemented; no incremental action required

**"Do nothing" is a valid output of the pipeline.** Most observations should produce no incremental trade.

### Operational practice
When the conviction score is < 0.3, the trade implication is "no new position." Document the observation in the journal but don't act on it. Most days, most observations should not produce new trades. Selectivity is operational.

---

## 13.5 Step 4: Sizing

### What sizing does

Derives the specific position size from the loss budget.

### The sizing equation
$$n \leq \left\lfloor \frac{B_\text{exp}}{L_\text{max}} \right\rfloor$$

Where:
- $B_\text{exp}$ = explicit loss budget for this sleeve / trade (in dollars)
- $L_\text{max}$ = per-unit maximum reasonable loss in stress (in dollars)
- $n$ = maximum number of units (contracts, shares, etc.)

Floor-rounded to be conservative.

### Worked example
- Sleeve loss budget: 5% of $1M portfolio = $50,000
- Strategy: XSP ATM monthly put-write
- Per-contract S2 stress loss: $10,000 (Chapter 11, Example 10)
- $n \leq \lfloor 50,000 / 10,000 \rfloor = 5$

So 5 contracts is the max. Round down for buffer: 4 contracts.

### Stress test the sizing
After computing $n$, run S3 (worst-case) stress:
- 4 contracts × S3 loss/contract = 4 × $20,000 = $80,000 = 8% of portfolio

Is 8% recoverable? If yes (account survives operationally, no margin breach, no behavioral capitulation), sizing is OK. If no, reduce to 3 contracts and recompute S3.

### The portfolio constraint

Beyond per-sleeve sizing, the portfolio constraint:

$$\sum_{i} \text{ES}_{95,i} \leq B_\text{portfolio}$$

The sum of expected shortfalls across sleeves can't exceed the portfolio loss budget. Because correlations rise in stress (tail correlations approach 1.0 for premium-selling sleeves), this is binding more often than naive sleeve-level sizing suggests.

### Operational practice
Compute $n$ from the formula. Document the assumed $L_\text{max}$ for the sleeve. Stress-test against S3. If your intuition disagrees with the formula's $n$ (in either direction), check which is wrong — it's usually the intuition.

---

## 13.6 Step 5: Invalidation

### What invalidation does

Specifies the explicit conditions under which you'll close the position or revalidate the thesis.

### Two kinds of invalidation

**Trade-level invalidation:** when does THIS specific trade close?
- Time-based: "21 DTE, close and roll"
- Loss-based: "MTM down 3× initial premium, close"
- Profit-based: "MTM up 50% of initial premium, take profit"

**Strategy-level invalidation:** when does this *strategy* get suspended or reassessed?
- Filter-based: "VIX/VIX3M > 1.05 for 3 days, halt new entries"
- Performance-based: "Sleeve drawdown > 20% PTP, close and reassess"
- Evidence-based: "Academic consensus shifts (rare but possible)"

### Worked example
- Trade-level: "Close XSP put at 21 DTE or 50% profit, whichever first; otherwise hold to expiry"
- Strategy-level: "Halt new XSP put entries if VIX/VIX3M > 1.05 for 3 closes; reduce 50% of existing"
- Behavioral: "If sleeve drawdown > 20% PTP, full stop and 30-day cooling-off"

All three are specified before entering. The discipline is in pre-committing.

### Why pre-commitment matters

Behavioral economics (Thaler, Sunstein) shows that ex-ante decisions made in calm states are more rational than ex-post decisions made under stress. Stress activates loss-avoidance and confirmation biases that override consistent decision-making.

By writing down the invalidation criteria *before* the position is on, you're using your calm-state self to constrain your stress-state self. This is the operational meaning of "discipline."

### Operational practice
Every position has documented invalidation criteria. If you can't articulate what would prove you wrong, the trade isn't ready. Many bad trades fail this test because the entry was based on unfalsifiable narrative ("the market should rally") rather than testable hypothesis.

---

## 13.7 The full pipeline in action

Putting it together with a worked example:

### Scenario
You wake up, check market data. Notice that VIX is at 22 (up from 14 last week) and VIX/VIX3M = 1.04. SPX is down 3% on a weak jobs print.

### Pipeline execution

**Step 1: Observation**
- VIX rose 8 points over 5 days
- VIX/VIX3M = 1.04 (up from 0.85)
- This is the FIRST close above 1.00 (rule says wait 3 closes)
- 21-day realized vol on SPX = 18% (still below 22 implied)
- TED spread = 35 bps (normal)
- MOVE = 95 (normal)

**Step 2: Interpretation**
- Term structure tightening but not yet stress
- Realized vol still below implied (VRP still positive)
- Liquidity normal
- This is "elevated, not stress" — yellow zone, not red

**Step 3: Trade implication**
- Filter not yet triggered (need 3 consecutive closes)
- No new short-vol entries today (preemptive caution at 1 close)
- No reduction of existing positions
- No equity action
- Document and re-check tomorrow

**Step 4: Sizing**
- No new positions, so sizing N/A today
- Existing XSP positions unchanged
- Filter trigger has not occurred yet

**Step 5: Invalidation**
- If VIX/VIX3M crosses back below 1.00 on tomorrow's close → return to normal regime
- If VIX/VIX3M stays above 1.00 for 2 more closes → escalate to filter trigger and reduce 50%
- If realized vol crosses above implied → halt new entries even before VIX trigger

### Conclusion of the day's pipeline

**Result: no action today, plus pre-committed conditions for tomorrow.** This is what the pipeline produces in elevated-but-not-stress regimes. Most of the discipline shows up in the *non-actions* — not entering new positions because the filter is yellow.

---

## 13.8 The pipeline for a foundation allocation

The pipeline applies even to long-term allocations, just at slower frequency.

### Scenario: quarterly review of the trend allocation

**Step 1: Observation**
- DBMF YTD return: -2.1%
- BTOP50 YTD return: -0.8%
- DBMF tracking error to BTOP50: 1.3% annualized (within 4% threshold)
- Trailing 12-month: DBMF -3.2%, BTOP50 -1.5%

**Step 2: Interpretation**
- Trend in mid-drought
- DBMF tracking is acceptable
- 12-month underperformance is consistent with documented trend droughts (e.g., 2011-2018)
- This regime should reverse in next stress / trending event

**Step 3: Trade implication**
- Hold existing position
- Don't reduce (drought is not a kill criterion)
- Possibly add at next rebalance if other allocations have drifted (but not because of trend performance)

**Step 4: Sizing**
- No change

**Step 5: Invalidation**
- DBMF tracking > 4% annualized for 4 consecutive quarters → switch vehicle
- DBMF drawdown > 25% PTP → reassess (not auto-exit)
- 5+ year sustained negative absolute returns → reassess (would be unprecedented)

The discipline of running the pipeline even on calm-state allocations is what prevents impulsive exits during drawdowns.

---

## 13.9 Common pipeline failures

### Failure 1: Skipping interpretation
"VIX is up, sell calls." Why? What does "VIX up" mean about the regime? Without interpretation, the action is arbitrary.

### Failure 2: Skipping sizing
"This is a great trade, I'll go big." How big? Why? Without explicit sizing from a loss budget, you've abandoned the survivability discipline.

### Failure 3: Skipping invalidation
"If it works, great; if it doesn't, I'll figure out what to do." This guarantees stress-state decision-making. Pre-commit invalidation before entering.

### Failure 4: Re-running pipeline mid-trade with new biases
Entering a trade with one set of conditions, then under stress, re-running the pipeline with biased interpretation to justify holding. The original interpretation should govern unless objective conditions change. Rationalizing-as-you-go is the most subtle failure mode.

### Failure 5: Pipeline-without-checklist execution
Running the pipeline mentally without writing it down. Memory degrades; written records preserve the discipline. Even a brief journal entry per pipeline run is sufficient.

---

## 13.10 The pipeline at portfolio level

The pipeline scales from individual trades to portfolio-level decisions:

### Portfolio observation
Total portfolio drawdown reaches 18% PTP.

### Portfolio interpretation
Approaching the 25% behavioral kill threshold (Chapter 14). Combination of equity + short-vol losses indicates correlated stress regime.

### Portfolio trade implication
Reduce all leveraged exposure 25%. Halt new tactical positions. Maintain core foundation allocations.

### Portfolio sizing
Existing positions held except as filter rules dictate. New positions: zero.

### Portfolio invalidation
- 25% drawdown → full stop on tactical sleeves, 30-day cooling-off
- Foundation drawdown > 35% → revalidation of full thesis required

---

## 13.11 Misconception box

> **Misconception:** "The pipeline is bureaucratic; experienced traders don't need it."
>
> **Correction:** Experienced traders run the pipeline implicitly through pattern recognition. The pipeline framework just makes the implicit explicit. Beginners use it explicitly because their pattern recognition isn't formed yet. *Experienced traders who skip the pipeline produce experienced trader-style failures* — well-articulated rationalizations of stress-state decisions. The pipeline doesn't go away with experience; it goes from explicit document to internalized habit.

---

## 13.12 Self-check (chapter)

1. State the five steps of the pipeline. What question does each answer?
2. Take a recent trade you made. Walk it through the pipeline retroactively. Did each step actually occur, or were some skipped?
3. What's the difference between trade-level and strategy-level invalidation?
4. Why is "no action" a valid pipeline output?
5. What's the operational consequence of skipping the sizing step?
6. State the position sizing equation. Why is it floor-rounded?

---

## Where this fits

Chapter 11 walked through reasoning chains. Chapter 12 compressed strategies into operational cards. Chapter 13 gives the grammar that connects observations to actions. Chapter 14 (next) covers portfolio framework, capital allocation, kill criteria, and revalidation cadence — the longest-time-horizon view of the framework.

[← Previous: Chapter 12 — Setup cards](13_ch12_setup_cards.md) | [Next: Chapter 14 — Portfolio framework →](15_ch14_portfolio_kill.md)
