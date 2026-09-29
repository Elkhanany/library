# Chapter 11 — Worked examples
## Ten reasoning chains end-to-end

> **Why this chapter is the most important.** Worked examples are the strongest pedagogical tool because they show the full reasoning path, not just the conclusion. Each example walks through the actual arithmetic of decision-making — distributions, Greeks, margin, conviction score, kill rule. By the end you should be able to apply the same chain to any new strategy you encounter.

---

## How to read these

Each worked example follows the same template:
1. **The question** — a specific operational decision
2. **Setup** — the relevant numbers
3. **Walkthrough** — the reasoning chain step-by-step
4. **Conclusion** — sized position or rejection
5. **What this teaches** — generalizable principle

Don't skim. The whole point is the granular reasoning.

---

## Example 1: The Sharpe trap in action

### Question
A friend pitches you a strategy: "It's a short-vol strategy with Sharpe 0.85 over 10 years. Better than SPX. Should you allocate?"

### Setup
- Pitched Sharpe: 0.85
- Strategy: systematic short far-OTM puts on SPX
- Backtest period: 2014-2023
- "Annual return 11%, vol 13%"

### Walkthrough

**Step 1: Apply the Sharpe haircut for skew (Chapter 2).**
Far-OTM puts have skew well below -3.0 (PUT index, ATM, has -2.09). Apply 30-50% Sharpe haircut for skew tax: 0.85 × 0.65 = 0.55. That's the skew-adjusted equivalent.

**Step 2: Apply the retail haircut for implementation (Chapter 3).**
The pitch is academic-style; live retail will see 0.6-0.7× this number. 0.55 × 0.65 = 0.36.

**Step 3: Check the backtest period.**
2014-2023 includes very few stress events (one quick March 2020 spike, no extended bear market). The dataset doesn't reflect the full distribution of regimes. **A short-vol Sharpe based on a benign decade is unreliable.**

**Step 4: Project tail behavior.**
Far-OTM puts have asymmetric crash exposure. Run mental stress test:
- SPX -10/VIX +10: estimated -8 to -15% sleeve loss
- SPX -20/VIX +25: estimated -25 to -40% sleeve loss
- SPX -35/VIX +50: estimated -55 to -85% sleeve loss

The strategy hasn't been tested in any of these. The backtest is silent on real tail behavior.

**Step 5: Compare to the simpler alternative.**
SPX over the same 2014-2023 period: ~12% annual return, vol ~16%, Sharpe ~0.65, with full liquidity, tax efficiency, and known tail behavior.

After haircuts, the candidate strategy's realistic Sharpe (~0.36) is materially worse than just holding SPX (~0.5 retail-adjusted).

**Step 6: Score the conviction (Chapter 4).**
- E (evidence): backtest on benign period only. Score ~0.30
- M (mechanism): far-OTM put-write is risk premium for catastrophic risk; mechanism real but harvested only with patience. Score ~0.50
- R (regime): assumes calm regime continues. Score ~0.40
- X (execution): far-OTM SPX options have wider spreads. Score ~0.55
- S (sizing): tail loss is 2-5x premium; survivability is unclear without more data. Score ~0.30

C = 0.30 × 0.50 × 0.40 × 0.55 × 0.30 = **0.010**

### Conclusion
Don't allocate. The Sharpe pitch is misleading because it ignores skew, applies no retail haircut, and uses a backtest period that doesn't include any real stress. After the conviction analysis, this strategy doesn't pass admission.

### What this teaches
**Pitched Sharpes are paper Sharpes.** The translation from "Sharpe 0.85 in a 10-year backtest" to "realistic retail user-account expectation" is roughly 0.36 — a 58% discount. This is the typical haircut for short-vol strategies, and the gap is *systematic*, not pessimistic.

---

## Example 2: VRP harvest at $1M portfolio, calm regime

### Question
You have a $1M portfolio. VIX is at 14, term structure is contango (VIX/VIX3M = 0.85), realized vol is 12%. You want to add VRP harvest. How much, and how?

### Setup
- $1M portfolio
- VIX 14, contango
- Considering 15% allocation to XSP cash-secured ATM monthly puts
- Goal: capture index VRP

### Walkthrough

**Step 1: Choose the right VRP variant (Chapter 6).**
Of the put-write variants, ATM monthly cash-secured XSP is the closest to academic VRP with reasonable retail implementation. Eliminates margin risk; gets 1256 tax treatment.

**Step 2: Position size.**
15% of $1M = $150k notional. XSP at 600 means each contract represents $60k notional ($600 × 100). Each ATM put is fully cash-secured at the strike: ~$60k of cash collateral per contract.

So 15% allocation = approximately **2-3 contracts** of XSP ATM monthly puts (total cash collateral $120-180k).

**Step 3: Project the typical month P&L.**
ATM XSP monthly put trades at roughly 2-3% of strike price = $12-18 of premium per contract. For 3 contracts: $36-54 of premium for the month, or $3,600-5,400 absolute. As % of portfolio: 0.36-0.54%/month, ~4.5-6.5%/year gross.

After haircuts: realistic 2-4%/year net contribution.

**Step 4: Stress test.**
- S1 (SPX -10, VIX +10): ATM puts likely deep ITM, MTM loss ~$3,000/contract = $9,000 (0.9% of portfolio)
- S2 (SPX -20, VIX +25): ATM puts deep ITM, MTM loss ~$8,000-12,000/contract = $24,000-36,000 (2.4-3.6% portfolio)
- S3 (SPX -35, VIX +50): ATM puts very deep ITM, MTM loss ~$15,000-20,000/contract = $45,000-60,000 (4.5-6% portfolio)

Cash-secured: no margin breach, no force-liquidation. Maximum loss bounded by collateral = $180,000 (worst case all assigned at zero, which doesn't happen with index).

**Step 5: Conviction score.**
- E: 0.85 (T1: Bondarenko, Carr-Wu)
- M: 0.90 (clear risk premium mechanism)
- R: 0.85 (calm regime, contango)
- X: 0.90 (XSP liquid)
- S: 0.85 (cash-secured eliminates margin path risk)

C = 0.85 × 0.90 × 0.85 × 0.90 × 0.85 = **0.50**

High conviction. Allocate.

### Conclusion
Sell 2-3 contracts of XSP ATM monthly puts (cash-secured). Expected monthly premium: ~$36-54. Worst-case monthly MTM in S3: ~5% of portfolio. Kill criteria: VIX/VIX3M > 1.05 for 3 days → halt new sales.

### What this teaches
**The conviction framework formalizes intuition.** Each domain scores around 0.85-0.90 because the strategy is strong across all dimensions. The product (~0.50) gates this as high conviction. If any single domain were weak (e.g., S = 0.4 because oversized), the product would collapse below 0.30.

---

## Example 3: VRP harvest in stress regime

### Question
Same portfolio, but now: VIX is 28, backwardated 5 days (VIX/VIX3M = 1.10), realized vol = 32%. The stress just hit yesterday. Should you allocate to VRP harvest now?

### Setup
- $1M portfolio
- VIX 28, backwardated
- Realized vol 32%
- "VRP looks elevated; this should be a great time to sell premium"

### Walkthrough

**Step 1: Check the filters (Chapter 9).**
- VIX/VIX3M > 1.05 for 3 days: ✗ (kill criterion triggered)
- 21-day realized > implied: ✗ (negative VRP regime)

**Both filters say HALT new entries.**

**Step 2: But isn't elevated VIX a great time to sell premium?**

This is the most common retail misconception around VRP. Elevated VIX tempts the trader because premiums are richer. But:
- Realized vol is even higher (32% > implied 28%)
- Forward distribution is wider than implied
- Margin expansion under PM has already triggered
- Path of MTM losses through this regime is severe
- Even cash-secured positions face large MTM drawdowns

The right framing: **VRP exists when implied > realized. Negative VRP (realized > implied) is the opposite of the structural premium.** Selling premium in negative VRP is doing the wrong thing.

**Step 3: Conviction score.**
- E: 0.85 (evidence unchanged)
- M: 0.90 (mechanism unchanged)
- R: **0.15** (regime is exactly opposite of supportive)
- X: 0.65 (spreads wider)
- S: **0.35** (much harder to size for survivability when realized > implied)

C = 0.85 × 0.90 × 0.15 × 0.65 × 0.35 = **0.026**

### Conclusion
**Do not enter new positions.** Existing positions: reduce sizing 50% via buying back half, or close entirely if MTM is acceptable. Wait for filter conditions to normalize before re-entering.

### What this teaches
**The conviction framework correctly turns OFF in adverse regimes.** Same strategy, same evidence, same mechanism — but R (regime) crashing the score means the trade is wrong now even if it's right on average. This is what "selectivity" looks like operationally.

The reviewer's framing applies: "skipping entire weeks when criteria weren't met" — high-conviction trading is mostly *not* trading.

---

## Example 4: Trend-following allocation timing

### Question
You're considering adding trend-following via DBMF. Trend has been in a multi-year drought (2023-2024 returns flat to slightly negative). Should you allocate now?

### Setup
- Portfolio currently 70% equities, 30% bonds. Want to add trend.
- DBMF has been flat for 18 months
- "Trend is broken, why allocate?"

### Walkthrough

**Step 1: Check evidence (Chapter 1, 6).**
- Hurst-Ooi-Pedersen 2017: 140 years, every decade positive
- Multiple replications across asset classes
- Mechanism: behavioral under-reaction + hedger compensation + liquidity provision
- T1 evidence

**Step 2: Why is trend in a drought?**
Trend has structural droughts during chop / mean-reverting regimes. 2011-2018 was the worst trend drought in modern history (~7 years). Trend doesn't "break" — it goes through extended periods where the underlying signals don't align across asset classes.

**Step 3: The bear case for waiting.**
"Wait until trend works again, then allocate." But:
- You can't time the regime turn
- Trend tends to recover in the same events that hurt other assets (2008, 2020, 2022)
- The recovery is fast — by the time trend "works" you've missed the entry
- Allocating during a drought is uncomfortable but historically a good entry

**Step 4: Position size and structure.**
- 10-15% allocation to DBMF (single vehicle, transparent, lower fees)
- Build over 3 months (avoid lump-sum entry timing risk)
- Don't try to time the regime turn

**Step 5: Conviction score.**
- E: 0.90 (T1, 140 years)
- M: 0.85 (multi-source mechanism)
- R: 0.55 (drought regime; not supportive but not adverse)
- X: 0.95 (DBMF easy to buy)
- S: 0.90 (10-15% well within survivability; positive crash skew)

C = 0.90 × 0.85 × 0.55 × 0.95 × 0.90 = **0.36**

Medium conviction. The regime score is the binding constraint.

### Conclusion
Allocate 10-15% to DBMF, but build over 3 months rather than lump-sum. The medium-conviction score reflects that timing is suboptimal but the structural case is strong. Hold across cycles; don't auto-exit during droughts. Kill criterion: DBMF tracking error to BTOP50 > 4% annualized for 4 quarters.

### What this teaches
**Medium conviction (0.3-0.5) means scale modestly with operational adjustments.** Not zero, not full size. The regime score caught that we're in a drought; the operational response is to phase the entry.

---

## Example 5: FOMC even-week overlay implementation

### Question
You have a 60% equity allocation. Cieslak says equity premium is concentrated in even weeks. Should you reduce equity in odd weeks?

### Setup
- 60% equity allocation, $600k of $1M portfolio
- Considering: 60% in even weeks, 45% in odd weeks (-25% reduction)
- Implementation: SPY (taxable account considerations)

### Walkthrough

**Step 1: Check evidence (Chapter 8).**
- Cieslak-Morse-Vissing-Jorgensen 2019: original 1994-~2014
- T2 evidence (replicated but OOS limited post-2019, 2022 hiking cycle uncertain)

**Step 2: Mechanism plausibility.**
The Fed put / forward guidance mechanism is plausible. But could decay similarly to pre-FOMC drift (which decayed post-2015). T2, not T1.

**Step 3: Implementation cost.**
Trading SPY in/out every 1.5 weeks generates:
- Bid-ask: minimal for SPY (0.01% spread)
- Slippage: minimal
- **Tax cost**: HUGE. Every sell triggers gain/loss recognition. In a taxable account this is a tax-acceleration disaster.

**Step 4: The tax-aware framing.**
- In a tax-deferred account (IRA, 401k): implementation cost is small. Worth doing.
- In a taxable account: tax acceleration on rotating SPY can cost 20-40 bps annually, which exceeds the expected 10-30 bps of cycle alpha.

**Step 5: The right operational form.**
Don't rotate the existing SPY position. Instead:
- For new contributions / rebalances, time them to even-week starts
- Modulate via futures sizing (ES, MES) since 1256 treatment doesn't trigger short-term gain on rolls
- Or use leveraged ETF on margin only during even weeks

The simplest implementation: time discretionary buys/sells to land in even weeks. Not full rotation.

**Step 6: Conviction score.**
- E: 0.50 (T2)
- M: 0.65 (mechanism plausible but decay risk)
- R: 0.65 (cycle effect should still be roughly intact)
- X: **0.40 in taxable, 0.85 in tax-deferred** (this is the binding constraint)
- S: 0.85 (modulation, not new sleeve)

C (taxable): 0.50 × 0.65 × 0.65 × 0.40 × 0.85 = **0.072**
C (tax-deferred): 0.50 × 0.65 × 0.65 × 0.85 × 0.85 = **0.153**

Both are below the 0.3 threshold.

### Conclusion
Don't run a separate FOMC rotation strategy. The expected alpha doesn't survive implementation costs even in tax-deferred accounts at retail scale. Use awareness to time discretionary entries (favor even-week starts), but don't build a system around it.

### What this teaches
**Implementation costs determine whether overlays are worth running.** A 10-30 bps overlay drowned by 20-40 bps of tax friction is negative-EV. The framework correctly identifies this through the X score.

---

## Example 6: EOQ rebalancing direction (with sign)

### Question
Q1 ends in 5 days. SPX is up 9% for the quarter; 10-year Treasury is down 1%. Should you trade the EOQ rebalance? Which direction?

### Setup
- Q1 SPX +9%, ZN -1%
- Divergence: ~10% (SPX outperformed bonds by 10%)
- Considering EOQ rebalancing trade

### Walkthrough

**Step 1: Check the divergence threshold.**
Rule from Chapter 8: divergence > 1.5% required. 10% qualifies.

**Step 2: Get the direction right (this is the corrected sign).**

> Stocks outperformed bonds → 60/40 funds are now overweight stocks → rebalancers will SELL stocks, BUY bonds → front-running means doing the same thing → SHORT ES, LONG ZN

The reviewer of v1 caught this sign in the original framework. **Restating clearly: if equities outperformed bonds during the quarter, you go SHORT equities and LONG bonds.**

**Step 3: Position size.**
First few quarters of personal data: 0.5% of portfolio at risk per leg. $1M portfolio = $5,000 risk per leg.

For ES (priced ~5800 × $50 multiplier = $290k notional), 0.5% portfolio risk with a 1% adverse move = 1 contract.
For ZN (priced ~110 × $1000 = $110k notional), similar sizing = 1 contract.

So: short 1 ES contract, long 1 ZN contract for first few quarters.

**Step 4: Timing.**
- Enter T-5 trading days of quarter end
- Exit T+1 to T+3 of new quarter (give the rebalancers time to execute)

**Step 5: Conviction score.**
- E: 0.55 (T2, recent paper, strong but not multi-decade-replicated)
- M: 0.75 (institutional flow mechanism is solid)
- R: 0.85 (large divergence supports trade)
- X: 0.80 (futures liquid; spread between ES and ZN clean)
- S: 0.80 (small size for first few quarters)

C = 0.55 × 0.75 × 0.85 × 0.80 × 0.80 = **0.224**

Below threshold for high conviction; medium-conviction range. **Test sizing for first 4 quarters.**

### Conclusion
Take the trade at small size (1 ES short / 1 ZN long for $1M portfolio). Track personal P&L for 4 quarters. After 4 quarters, evaluate: if hit rate > 55% AND net P&L > 0, increase size. If hit rate < 50% OR net P&L negative, suspend.

### What this teaches
**Untested live strategies start small.** The conviction framework reflects the genuine uncertainty about retail replication of a recent academic paper. Size grows with personal evidence, not paper claims.

---

## Example 7: VIX filter triggering during open VRP position

### Question
You have 3 contracts of XSP ATM monthly puts on (cash-secured, full size). VIX/VIX3M just crossed 1.05 for the third consecutive close. What do you do?

### Setup
- 3 XSP ATM puts, 22 days to expiry
- Currently each MTM at -$8 (SPX has dropped 4%)
- Total MTM loss: -$2,400
- Filter triggered

### Walkthrough

**Step 1: What does the kill rule say?**
From Chapter 9: VIX/VIX3M > 1.05 for 3 closes → halt new sales; reduce existing premium-selling sleeve sizing 50%.

**"Reduce 50%" means close half of existing positions, not just stop new entries.**

**Step 2: How to close.**
3 contracts → close 1.5, which means close 1 (rounded down conservatively) or 2 (rounded up aggressively). Conservative is closer to the rule.

Cost: buy back 1 contract at current price (e.g., $13 per contract for $1,300 to close). MTM loss locked in: ~$8 per contract × 100 = -$800 on the closed contract.

**Step 3: But it's MTM loss; if I hold I might recover.**

Critical operational point: **the kill rule is pre-committed.** It exists because in stress, your behavioral intuition tells you to hold and hope. The rule overrides intuition because:
- Stress regimes can deepen (March 2020 went from VIX 28 → 82 in 8 days)
- The rule is calibrated to cumulative outcomes, not individual trades
- Following the rule is what allows the strategy to compound across many cycles

If you override the rule once, you'll override it every time. Discipline only exists if it's binding in stress.

**Step 4: After closing.**
- Halt new entries until VIX/VIX3M < 1.00 for 5 closes
- Phased re-entry: 25% → 50% → 100% over 3 weeks
- During the halt period, lost VRP premium is opportunity cost (~0.3% portfolio over the typical halt duration)

**Step 5: Conviction score for the halt action itself.**
- E: 0.90 (filter rules T1-T2)
- M: 0.85 (clear stress mechanism)
- R: 0.95 (filter triggered)
- X: 0.85 (close a contract is easy)
- S: 0.95 (preserves portfolio survivability)

C = 0.90 × 0.85 × 0.95 × 0.85 × 0.95 = **0.59**

High conviction in the halt action.

### Conclusion
Buy back 1 of the 3 contracts. Halt new entries. Wait for filter normalization. Don't override the rule.

### What this teaches
**Pre-committed kill rules exist to override behavioral intuition.** In stress, your intuition will say "hold and hope." The rule says "trim and survive." Long-run compounding requires the rule to win these arguments. The conviction score for *following the rule* is high (0.59) — this is what good operational discipline scores.

---

## Example 8: Earnings short-vol on a single name

### Question
NVDA reports earnings tomorrow. IV is at 75% vs 35% historical average. The vol crush could be 30+ vol points. Should you sell premium?

### Setup
- NVDA at $850, earnings tomorrow
- ATM 3-day call: $35 (IV 75)
- ATM 3-day put: $32 (IV 75)
- 1-2 day expected move ~$45 (5.3%)

### Walkthrough

**Step 1: Source classification.**
This is single-name earnings short-vol — explicitly rejected category at retail (Chapter 10).

**Step 2: Adams-Neururer 2020 finding.**
At single-name retail level, naive earnings short-vol has *negative mean despite positive median*. Most of the time you make small premium; occasionally you lose much more.

**Step 3: Distribution analysis.**
- Most likely outcome: earnings beat, stock moves $30, you keep most premium (~+$30 per side)
- Tail outcome: guidance cut, stock drops 12%, you lose $80+ on the put side
- Expected gain per side: ~+$15 in win cases × 75% probability = +$11
- Expected loss per side: ~-$60 in loss cases × 25% probability = -$15
- Net expected: -$4 per side, **negative EV**

This matches the Adams-Neururer empirical finding.

**Step 4: But isn't NVDA's IV elevated indicating market doesn't expect a beat?**

The "IV is high" framing assumes you have edge in predicting whether the move exceeds implied. You don't have systematic edge there. Adams-Neururer's negative-mean finding is the average across many such "elevated IV" earnings events.

**Step 5: The cross-sectional version.**

If you ran this on 200+ names simultaneously (Cao-Han-Tong-Zhan 2022 institutional version), the cross-sectional dispersion provides edge. On a single name, you don't get that diversification.

**Step 6: Conviction score.**
- E: 0.30 (T3 at retail single-name level)
- M: 0.40 (mechanism real but heavily skewed against retail single-name)
- R: 0.50 (no specific regime support)
- X: 0.70 (NVDA options liquid)
- S: 0.30 (single-name tail risk huge relative to premium)

C = 0.30 × 0.40 × 0.50 × 0.70 × 0.30 = **0.013**

Effectively zero conviction.

### Conclusion
Don't sell premium on the NVDA print. If you must trade, prefer a calendar spread (long-dated long, short-dated short) to capture the vol crush with bounded downside. But the conviction even on calendar spreads at single-name level is medium at best.

### What this teaches
**The conviction framework correctly identifies retail-level rejected strategies even when the narrative is compelling.** "Vol is at 75 vs historical 35" is a compelling pitch. The framework catches that:
1. Single-name earnings short-vol is negative-mean for retail (Adams-Neururer)
2. The "edge" comes from cross-sectional dispersion, not single-name pricing
3. Tail risk dominates the small premium

---

## Example 9: The put-spread + LEAP combination

### Question
A "professional-style" trader pitches: "Sell 1-year SPX 4400/4200 put spreads to fund 2-year SPX 5000 LEAP calls. The premium pays for the LEAP. You get leveraged equity exposure with VRP edge." Should you do this?

### Setup (illustrative)
- SPX at 5000
- Sell 1-yr 4400/4200 put spread: collect $42 (max risk $158)
- Buy 2-yr 5000 LEAP call: cost $400
- Net: pay $358 ($400 - $42 short put net) for ~0.50 delta of LEAP exposure on $5000 SPX

### Walkthrough

**Step 1: Decompose the structure.**

Long LEAP call:
- Delta ~0.50
- Cost ~$400 = 8% of SPX notional
- Embedded financing: 50-150 bps annualized leverage drag

Short put spread:
- Theta: positive
- Vega: negative
- Bounded loss
- Delta: roughly +0.10

Combined structure:
- Total delta: ~0.60
- Cost: $358 net
- Implied leverage: ~ 60% of $5000 / $358 = 8.4× capital efficiency

**Step 2: Compare to ES futures.**
ES at SPX 5000: $250,000 notional per contract. Margin requirement ~$15,000. Implicit financing: ~SOFR + 10-20 bps ≈ 4.6-4.7% annualized.

For comparable delta exposure:
- ES futures: 1 contract gives 1.0 delta on $250k. For 0.60 effective delta on $250k, that's $150k notional ≈ 0.6 contracts ≈ $9,000 margin.
- Put-spread + LEAP: $358 capital outlay for 0.60 delta on $5,000 ≈ $3,000 of effective notional exposure.

Wait — these aren't comparable scales. Let me redo with the same effective notional:

For $250k notional equivalent (1 ES contract):
- ES: $9,000 margin, 4.6% financing = ~$11,500/year cost
- LEAP + put spread (scaled to $250k effective): roughly $18,000 capital outlay (estimating)

The LEAP-based structure costs roughly 50-100% MORE than ES futures for the same exposure, due to embedded leverage drag.

**Step 3: Where's the "VRP edge"?**
The short put spread captures roughly $42 of premium minus expected losses. After:
- 60-70% probability the spread expires worthless: +$42
- 25-30% probability partial loss: -$30 to -$80
- 5-10% probability full loss: -$158

Expected value: ~+$15 to +$20 per spread, before friction. After execution: ~+$10. **As a fraction of the $358 capital outlay, that's 2.8% additional yield.**

But the LEAP carries 50-150 bps of financing drag. Net "edge" over simple leverage: -50 bps to +180 bps. Within noise.

**Step 4: Path properties.**

Under SPX -20/VIX +25:
- ES futures: lose ~20% × $250k = $50k. Margin requirement ~triples but cushion is clear.
- LEAP + put spread: LEAP loses ~80% of value (delta + vega both bad), short put spread loses near max ($150). Total loss: $320 + $116 = $436 vs $358 outlay. Position essentially destroyed; force-close likely.

ES handles stress much better. The LEAP structure has worse path properties.

**Step 5: Conviction score for the LEAP structure.**
- E: 0.30 (no real "edge" beyond leverage)
- M: 0.30 (the "VRP edge" claim is wrong)
- R: regime-independent (it's just leverage)
- X: 0.50 (multi-leg, complex roll)
- S: 0.30 (worse path than alternatives)

C = 0.30 × 0.30 × 0.60 × 0.50 × 0.30 = **0.008**

Effectively zero conviction.

### Conclusion
Don't do the put-spread + LEAP combo. If you want leveraged equity exposure:
1. ES futures: best for active traders, 1256 tax, clean financing
2. 2× ETFs (SSO): for passive holders, 0.85% expense
3. Box-spread financing + SPY: for sophisticated PM accounts

All three give equivalent or better economic exposure with less complexity and better path properties. The LEAP + put-spread structure is leverage with extra steps, dressed as edge.

### What this teaches
**Decomposition kills false-edge claims.** When you actually walk through the Greeks, financing, and path properties, "edges" that depend on complexity often vanish. The simple alternatives (futures, leveraged ETFs) usually win on operational realism.

---

## Example 10: Position sizing from stress loss

### Question
You want to add a new short-vol strategy (XSP put-write) to your portfolio. Your max acceptable monthly loss on this sleeve in S2 (SPX -20, VIX +25) is 5% of total portfolio. How big can the position be?

### Setup
- Total portfolio: $1M
- Max acceptable S2 loss on this sleeve: 5% = $50k
- Strategy: XSP ATM monthly puts (cash-secured)

### Walkthrough

**Step 1: Estimate S2 P&L per contract.**
ATM XSP put with strike around current price 600. In S2, SPX drops 20%, so XSP drops to 480. The put is deep ITM at intrinsic $120.

If sold for $12 of premium initially, MTM loss at S2: ~$108 per contract.

**Step 2: Compute max contracts.**
Max loss per contract: ~$10,800 (×100 multiplier).

Max contracts: $50,000 / $10,800 ≈ **4.6 contracts**

**Round down to 4 contracts** for buffer.

**Step 3: Verify with S3 stress.**
S3: SPX -35, VIX +50. XSP at 390, put intrinsic $210.

Per-contract MTM loss: ~$200 × 100 = $20,000.

For 4 contracts: $80,000 = 8% of portfolio. **This exceeds the S2 budget but should still be recoverable.**

If 8% is acceptable as S3, sizing is OK. If 8% causes operational issues (margin breach, behavioral capitulation), reduce to 3 contracts.

**Step 4: Verify cash collateral.**
Each contract requires ~$58k of cash collateral (XSP 580 strike × 100). 4 contracts = $232k = 23% of portfolio in cash collateral.

Operationally feasible: reduces effective portfolio exposure but eliminates margin path risk.

**Step 5: The full sizing equation.**
The reviewer's framework:

$$n \leq \left\lfloor \frac{B_\text{exp}}{L_\text{max}} \right\rfloor$$

where $B_\text{exp}$ is the explicit loss budget and $L_\text{max}$ is the per-unit max loss.

Here: $B_\text{exp} = 50,000$, $L_\text{max} = 10,800$. n ≤ 4.6, so n = 4.

**Step 6: Conviction score.**
- E: 0.85 (T1 evidence)
- M: 0.90 (clear mechanism)
- R: assumed calm
- X: 0.90 (XSP liquid)
- S: 0.90 (sized to budget, cash-secured)

C = 0.85 × 0.90 × 0.85 × 0.90 × 0.90 = **0.53**

High conviction. Allocate.

### Conclusion
Sell 4 contracts of XSP ATM monthly puts. Max S2 loss: ~$43k (4.3% portfolio). Max S3 loss: ~$80k (8% portfolio). Cash collateral required: ~$232k. Kill criteria as in Example 7.

### What this teaches
**Position sizing should be derived from explicit loss budgets, not from intuition.** The equation $n \leq \lfloor B_\text{exp} / L_\text{max} \rfloor$ converts subjective risk tolerance into objective contract count. This is the operational meaning of "size for survivability."

---

## What these examples collectively teach

1. **Pitched Sharpes are paper Sharpes.** Apply haircuts before evaluating.
2. **The conviction framework correctly turns OFF in adverse regimes.** Selectivity is mostly *not* trading.
3. **Kill rules exist to override behavioral intuition.** Pre-commit them.
4. **Decomposition kills false-edge claims.** Walk through Greeks, financing, path.
5. **Position sizing comes from explicit loss budgets, not intuition.**
6. **Multi-domain analysis surfaces issues that single-dimensional analysis misses.**
7. **The simpler alternative usually wins.** Futures and ETFs beat complex options structures more often than not.

These are the operational principles distilled into reasoning chains. When you encounter a new strategy, run it through the same kind of analysis.

---

## Self-check (chapter)

1. Take a strategy you've recently considered. Walk through Examples 1-10 mentally — which one most resembles your situation? What does the analysis say?
2. State the position sizing equation. What inputs does it require?
3. Why does the conviction score for "following the kill rule" tend to be high in stress?
4. What's the difference between Sharpe haircut and conviction score?
5. Why do simpler alternatives (futures, ETFs) usually beat complex options structures?
6. If a strategy passes the conviction score (C ≥ 0.5) but stress P&L exceeds your loss budget, what do you do?

---

## Where this fits

Chapter 11 is the operational heart of the textbook — the chapter where concept becomes judgment. Chapters 12-14 give you the operational tools: setup cards (one-page references for tradeable strategies), the signal-to-trade pipeline (the grammar for how observations become positions), and the portfolio framework + kill criteria (when to suspend, revalidate, or rebuild).

Chapter 15 is reference: glossary, reading list, math summary card.

[← Previous: Chapter 10 — Rejected](11_ch10_rejected.md) | [Next: Chapter 12 — Setup cards →](13_ch12_setup_cards.md)
