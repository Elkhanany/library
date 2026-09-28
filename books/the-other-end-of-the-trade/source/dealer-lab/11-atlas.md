# Section 11 · Strategy Atlas
*Every play from Long Call to Double Diagonal.*

Every options strategy you'll see referenced in retail content or institutional desks reduces to a specific combination of the four primitives from Section 5A: long call, short call, long put, short put. This section catalogues approximately 58 named strategies organized by tier (Novice / Intermediate / Advanced / Expert) and category (Basic / Income / Credit Spreads / Neutral / Calendar / Debit Spreads / Directional / Naked / Ratio / Ladders / Synthetic / Arbitrage / Other).

For each strategy I provide: leg construction, market thesis, max profit / loss, breakeven, net Greeks at entry, dealer-side analysis (who takes the other side and why), regime fit, common variations, failure modes, and a concrete worked example with actual strike / premium / P&L numbers.

The treatment is reference-grade. Read it as a lookup, not a narrative.

---

## 11.0 · Strategy selection by purpose

The 58 strategies catalogued in this section are vehicles, not edges. The question that should drive selection isn't "which strategy do I know?" — it's "**what am I trying to express, and which structure expresses it most cleanly given current conditions?**"

This subsection is the decision-tree front door to the atlas. Read this before opening any strategy card.

### The four-question filter

Before selecting any structure, answer four questions in writing:

1. **Direction.** Bullish, bearish, or neutral (range-bound / no view)?
2. **Conviction time-horizon.** Days, weeks, or months?
3. **IV regime.** Cheap (IV percentile < 30), normal (30-70), or rich (> 70)?
4. **Catalyst.** Catalyst-driven (earnings, FOMC, FDA) or trend/structure-driven?

These four answers narrow the universe from 58 strategies to typically 1-3 candidates.

### The selection matrix

| Direction | IV regime | Catalyst | Preferred structures |
|---|---|---|---|
| **Bullish** | Cheap | Trend | Long call, call debit spread, shares + LEAP (PMCC) |
| **Bullish** | Cheap | Catalyst (positive) | Long call, call debit spread, call ratio backspread |
| **Bullish** | Normal | Trend | Call debit spread, shares, put credit spread |
| **Bullish** | Rich | Trend | **Put credit spread** (preferred over long call when IV is rich), short cash-secured put on XSP |
| **Bullish** | Rich | Catalyst (positive) | Diagonal call spread, put credit spread; avoid long calls (vol crush risk) |
| **Bearish** | Cheap | Trend | Long put, put debit spread |
| **Bearish** | Normal | Trend | Put debit spread, bear call spread |
| **Bearish** | Rich | Trend | **Bear call spread** (preferred), put debit spread |
| **Bearish** | Rich | Catalyst (negative) | Diagonal put spread, bear call spread; avoid long puts |
| **Neutral / range** | Cheap | None | Long calendar / diagonal, long strangle (range expected to break) |
| **Neutral / range** | Normal | None | Iron condor (with extreme selectivity per 11A), credit spreads either side |
| **Neutral / range** | Rich | None | Iron condor or iron butterfly at extreme IV percentile; short strangle if margin permits |
| **Long vol** (move expected, direction unknown) | Cheap | Imminent catalyst | **Long straddle / strangle**, ratio backspread |
| **Long vol** | Rich | Imminent catalyst | Calendar / diagonal (long forward vol while short event vol) |
| **Short vol** (no move expected) | Rich | None | Iron condor at extreme IV percentile, short strangle, calendar |

### Worked examples of the matrix

**Example 1.** SPX at 6,000, composite signal +45, VIX 14 (IV percentile 25%), Stage 2 confirmed, no imminent catalyst.

- Direction: bullish (composite +45)
- Horizon: 2-week swing
- IV regime: cheap
- Catalyst: none (trend-driven)

→ Matrix says: long call, call debit spread, shares + LEAP. **Preferred: call debit spread** for defined risk and capital efficiency given the modest IV.

**Example 2.** NVDA at $700, earnings in 4 days, IV percentile 92%, momentum signal firing on screen.

- Direction: bullish
- Horizon: through earnings
- IV regime: rich (very)
- Catalyst: imminent earnings

→ Matrix says: diagonal call spread or put credit spread; avoid long calls. **Preferred: diagonal call spread** — long back-month, short front-month at strike near the implied move boundary. Captures the IV crush post-earnings while maintaining bullish exposure.

**Example 3.** SPY at $580, VIX 28 (IV percentile 85%), composite signal +10, ADX 30 (extended trend).

- Direction: neutral (composite weak)
- Horizon: 3-week
- IV regime: rich
- Catalyst: none

→ Matrix says: iron condor or iron butterfly at extreme IV percentile, short strangle. **Preferred: defined-risk iron condor** because composite +10 isn't strong enough to take direction, but IV is rich enough to justify short vol. *Critical:* size very small per the CNDR-index empirical underperformance evidence — this should be 0.25% of portfolio risk, not 1%.

**Example 4.** AAPL at $230, FDA-equivalent event in 7 days (this is a product-launch scenario), IV percentile 70%, the screener flags constructive momentum.

- Direction: bullish (momentum)
- Horizon: through event
- IV regime: elevated
- Catalyst: imminent event

→ Matrix says: diagonal call spread (long back, short front near implied move) or put credit spread. **Preferred: depends on Greeks budget.** If you want max post-event upside, long call spread sized small to absorb IV crush. If you want event-vol mispricing, diagonal.

### Three principles that override the matrix

1. **Defined risk over naked risk for single-name event-week positions.** Always. The matrix may suggest a long call or short put, but if the position is on a single name through a catalyst, the structure should be defined-risk. Spread it.

2. **When in doubt, simpler structure.** A two-leg debit spread you understand executes better than a four-leg structure you sort-of-understand. Complexity has its own friction.

3. **Match instrument to size and tax bracket.** XSP for retail swings on index; SPX for size; Mag-7 single-names for momentum plays; everything else only if liquidity is verified.

### The structure-is-not-the-thesis principle

Every strategy in the atlas requires a market thesis (Section 10A.5), a regime check (Section 10A dashboard + 10F composite), a conviction score (Section 12B), explicit sizing (Section 12C), and pre-committed kill conditions. The structure expresses the thesis; it doesn't constitute it.

Picking iron condors because they have "high probability of profit" without understanding the regime is how retail traders lose money systematically over long horizons (Section 8B CNDR empirical evidence). Picking long straddles before earnings without surface analysis is how event-vol traders give the entire risk premium back to the dealer.

**The work that produces edge is in the four-question filter. The structure is just the wrapper.**

[INTERACTIVE: strategy-selection-tree]

---

## Novice tier — Basic structures

### Long Call

**Legs:** Buy 1 call at strike K.

**Thesis:** Strong upward move expected; IV cheap relative to forecast.

**Max profit / loss:** Unbounded / Premium paid. **Breakeven:** K + premium paid.

**Net Greeks:** Δ positive, Γ positive, Θ negative, ν positive.

**Dealer-side view:** The dealer who sold this call is short call, short delta, short gamma, long theta. They buy shares immediately to hedge the delta and continue re-hedging as spot moves. Your long-call position is, structurally, paying the dealer to manufacture upside convexity for you out of the underlying.

**Regime fit:** Best in low-IV regimes where you have a directional thesis that exceeds the implied move. Worst in high-IV regimes where you're paying inflated premium that decays quickly.

**Failure modes:** IV crush after expected catalyst arrives (you're right on direction but lose on vega); time decay accelerating in the final two weeks; underlying moves the wrong direction.

**Worked example:** SPX 6,000. Buy 1 SPX 6,050 call, 30 DTE, IV 18%, premium $35.00. Cost = $3,500. Breakeven SPX 6,085. If SPX rallies to 6,150 by expiration: payoff = $10,000 − $3,500 = $6,500 profit. If SPX stays at 6,000 by expiration: total loss = $3,500.

### Long Put

**Legs:** Buy 1 put at strike K.

**Thesis:** Strong downward move expected; or hedge for existing long stock.

**Max profit / loss:** K minus premium (S → 0) / Premium paid. **Breakeven:** K − premium paid.

**Net Greeks:** Δ negative, Γ positive, Θ negative, ν positive.

**Regime fit:** Best as a hedge in mid-IV regimes; standalone, as a directional bet, requires significant downside conviction to overcome the negative drift baked into option premium structures.

**Failure modes:** Equity skew means OTM puts are typically expensive relative to OTM calls; structural mean reversion in calm regimes; equity drift over multi-week horizons works against you.

**Worked example:** SPX 6,000. Buy 1 SPX 5,950 put, 30 DTE, IV 22% (higher than ATM call due to skew), premium $35.00. Cost = $3,500. Breakeven SPX 5,915. If SPX falls to 5,800: payoff = $15,000 − $3,500 = $11,500 profit.

### Covered Call

**Legs:** Long 100 shares + short 1 call at strike K above current spot.

**Thesis:** Own the stock anyway; willing to sell at strike for premium income.

**Max profit / loss:** (K − cost basis) + premium received / **(cost basis − premium received) per share if the underlying goes to zero** — bounded but potentially enormous in absolute dollars (a 100-share SPY position has ~$58,000 of downside before the premium offset). Calling this "limited risk" relative to naked short is fair; treating it as a small-risk position is not.

**Net Greeks:** Δ positive (less than +1.0 from the short call), Γ negative, Θ positive, ν negative.

**Dealer-side view:** The dealer is long the call you sold. They are long delta, long gamma, short theta. They sell shares as the underlying rises to hedge their growing delta — the same hedging that, on aggregate, contributes to the positive-GEX mean-reverting character we discussed in Section 8B.

**Regime fit:** Best in sideways or slowly rising markets. Worst in strong bull markets where you cap your upside far below where the stock actually goes.

**Eligible underlyings:** Single-name equities and ETFs that you can own as shares (SPY, QQQ, IWM, AAPL, NVDA, etc.). **Not available on cash-settled indices** — you cannot run a covered call on SPX, XSP, NDX, or RUT because there are no shares to own. The cash-settled-index equivalent for "I'm willing to sell at a higher level" is a *cash-secured short call* (naked call against cash collateral), which has unbounded loss and is a fundamentally different risk profile from a covered call. Do not conflate them.

**Worked example:** Own 100 shares SPY at $580. Sell 1 SPY 595 call, 30 DTE, premium $4.50. Credit = $450. If SPY closes at $590: keep shares + keep $450 premium. If SPY closes at $605: stock called away at $595 = $1,500 stock gain + $450 premium = $1,950 profit (vs $2,500 if you'd held without selling the call).

### Cash-Secured Put

**Legs:** Short 1 put at strike K, with cash equal to K × 100 set aside.

**Thesis:** Willing buyer at K. Get paid to wait.

**Max profit / loss:** Premium received / **(K − premium) per share if the underlying goes to zero** — bounded but very large in absolute dollars. A 570-strike SPY cash-secured put has a notional max loss near $57,000 per contract; the loss is *capped*, not *small*. "Defined risk" is a relative claim against naked-call exposure, not a license to size as if the position were tiny. See Section 12C for sizing.

**Net Greeks:** Identical to short put — Δ positive, Γ negative, Θ positive, ν negative.

**Regime fit:** Best in sideways or slowly rising markets where the put expires worthless. The canonical VRP-harvest vehicle when run systematically on XSP. Worst in strong downward moves where the put is exercised and you're long underwater stock.

**Failure modes:** Identical payoff to covered call (put-call parity from Section 5F), so the same failure modes apply. Common sizing trap: traders see "bounded loss" and size by the credit collected (e.g., "I collected $400, so my risk is $400") rather than by the actual loss-to-stop distance. The right size anchor is the notional or the loss at your *stop level*, not the option premium.

**Worked example:** Want to own SPY at $570 (currently $580). Sell 1 SPY 570 put, 30 DTE, premium $4.00. Receive $400 credit. Set aside $57,000 cash as collateral. If SPY closes above $570: keep $400 premium, do nothing. If SPY closes at $565: assigned 100 SPY shares at $570 (cost $57,000) but received $400 in premium = net effective purchase price $569.

**Critical reminder:** For US retail traders, do this on **XSP, not SPY**, to capture the 1256 60/40 tax treatment (Section 3C). The pre-tax math is identical; the after-tax math is dramatically better on XSP.

### Protective Put

**Legs:** Long 100 shares + long 1 put at strike K below current spot.

**Thesis:** Long stock you can't or won't sell; buy insurance against a defined loss.

**Max profit / loss:** Unbounded upside (minus put premium) / (cost basis − K) + put premium.

**Regime fit:** Best when you have asymmetric concerns about a specific event (earnings, FOMC, geopolitical) and want capped downside. Worst as a continuous overlay — the cost of rolling puts over long horizons is significant.

**Worked example:** Long 100 SPY at $580. Buy 1 SPY 560 put, 60 DTE, premium $6.00. Cost = $600 for downside insurance. If SPY falls to $540: stock loss = $4,000, put value at expiration = $2,000. Net loss = $2,000 + $600 premium = $2,600 (instead of $4,000 unhedged).

---

## Intermediate tier — Credit Spreads

### Bull Put Spread (vertical put credit spread)

**Legs:** Short 1 put at higher strike K1, long 1 put at lower strike K2 (K2 < K1).

**Thesis:** Moderately bullish/neutral. Defined-risk version of short put.

**Max profit / loss:** Net credit / (K1 − K2) − net credit. **Breakeven:** K1 − net credit.

**Net Greeks:** Δ positive, Γ negative, Θ positive, ν negative.

**Regime fit:** Best in moderately rising or flat markets above K1. The defined-risk feature means you can size them in margin accounts without the unbounded loss exposure of naked puts.

**Failure modes:** Wing breaks when underlying drops below K2. The "defined risk" frame can lull traders into over-sizing — net loss per spread is bounded but per dollar of credit collected, the loss-to-credit ratio is often 3-5×.

**Worked example:** SPX 6,000, 30 DTE. Sell 5,900 put for $20, buy 5,850 put for $10. Net credit = $10 ($1,000 per contract). Max risk = 50 − 10 = $40 (×100 = $4,000). If SPX > 5,900 at expiration: keep $1,000. If SPX < 5,850 at expiration: lose $4,000. Loss-to-credit ratio = 4:1.

### Bear Call Spread (vertical call credit spread)

**Legs:** Short 1 call at lower strike K1, long 1 call at higher strike K2 (K2 > K1).

**Thesis:** Moderately bearish/neutral. Defined-risk version of short call.

**Max profit / loss:** Net credit / (K2 − K1) − net credit. **Breakeven:** K1 + net credit.

**Net Greeks:** Δ negative, Γ negative, Θ positive, ν negative.

**Regime fit:** Best in moderately falling or flat markets below K1. Often paired with a bull put spread to form an iron condor.

**Worked example:** SPX 6,000, 30 DTE. Sell 6,100 call for $15, buy 6,150 call for $7. Net credit = $8 ($800 per contract). Max risk = 50 − 8 = $42 (×100 = $4,200).

---

## Intermediate tier — Neutral structures

### Iron Condor

**Legs:** Short put credit spread + short call credit spread, with the short put strike below current spot and the short call strike above. Long 1 put at lower strike, short 1 put at next-higher strike, short 1 call at next-higher strike (still above spot), long 1 call at highest strike.

**Thesis:** Stock stays inside the inner wings until expiration. Pure short-vol bet.

**Max profit / loss:** Total credit received / (wing width) − credit.

**Net Greeks:** Δ ≈ 0 (balanced), Γ negative, Θ positive, ν negative.

**Regime fit:** Best when expected realized vol is meaningfully below implied vol. Worst when underlying breaks out of the inner wings. The CNDR (Cboe S&P 500 Iron Condor) benchmark index has materially underperformed SPX since inception. Consistent underperformance across the available CNDR benchmark history (1986 backtest start; live 2007-present) strongly suggests the structure is unattractive for most retail implementations, though results vary with transaction-cost assumptions, sizing rules, and comparison period. The PUT Index by contrast — which sells systematic ATM cash-secured puts rather than condors — has historically delivered competitive risk-adjusted returns (Bondarenko 2019), so the lesson is specifically about iron condor structure, not about systematic premium selling in general.

[INTERACTIVE: cndr-vs-spx-historical]

**Worked example:** SPX 6,000, 45 DTE. Sell 5,800/5,750 put spread for $8 net credit. Sell 6,200/6,250 call spread for $7 net credit. Total credit = $15 ($1,500). Max risk = 50 − 15 = $35 (×100 = $3,500). Wins if SPX between 5,785 and 6,215 at expiration.

### Iron Butterfly

**Legs:** Short straddle at center strike K + long puts and calls at protective wings at K ± W.

**Thesis:** Very confident stock pins the middle strike. Larger credit than condor, narrower profit zone.

**Net Greeks:** Δ ≈ 0 at K, Γ negative (more negative than iron condor), Θ positive (higher than IC), ν negative.

**Regime fit:** Most aggressive premium-selling structure. Best when you have very specific reason to expect pinning at K.

### Long Call Butterfly

**Legs:** Long 1 call at lower strike K1, short 2 calls at middle strike K2, long 1 call at higher strike K3, with K2 = (K1 + K3)/2.

**Thesis:** Stock pins the body strike K2. Defined risk, cheap to enter, paper-thin win zone.

**Max profit / loss:** (K2 − K1) − cost / cost (premium paid).

**Net Greeks:** Δ ≈ 0 near body strike, Γ negative (peaks at K2), Θ positive (peaks at K2), ν negative.

**Worked example:** SPX 6,000, 30 DTE. Buy 5,950 call for $80, sell 2 × 6,000 calls for $50 each ($100 total), buy 6,050 call for $30. Net cost = $80 − $100 + $30 = $10 ($1,000 debit). Max profit at K2=6,000: $5,000 − $1,000 = $4,000.

### Long Put Butterfly

Same as call butterfly but using puts. Identical to call butterfly by put-call parity.

---

## Intermediate tier — Calendar Spreads

### Calendar Call Spread

**Legs:** Long 1 call with later expiration, short 1 call with earlier expiration, both at same strike K.

**Thesis:** Long forward volatility. Profits if stock pins near strike at near expiry AND forward IV rises.

**Net Greeks at entry:** Δ ≈ 0 (both legs ATM), Γ mixed (short near gamma, long far gamma; net positive), Θ positive (collecting near theta), ν positive (long forward vol).

**Regime fit:** Best when near-term IV is high relative to forward IV (term structure in backwardation) and you expect mean reversion. Worst in trending markets that move significantly through the strike.

**Worked example:** SPX 6,000. Sell 6,000 call expiring in 7 days for $25, buy 6,000 call expiring in 30 days for $40. Net debit = $15 ($1,500). If SPX is at 6,000 at the 7-day expiry: short leg expires worthless ($25 profit), long leg has ~21 days remaining and is worth perhaps $35 — net P&L approximately $20 ($25 short premium − $5 long decay) = $2,000.

### Calendar Put Spread

Same forward-vol structure using puts (often when put skew is richer).

### Diagonal Call Spread

**Legs:** Long 1 call with later expiration at one strike, short 1 call with earlier expiration at *different* strike. Typically: long far ITM call, short near OTM call (a "poor man's covered call").

**Net Greeks:** Δ positive, Γ mixed, Θ positive near leg, ν positive (long forward vol).

**Worked example:** SPX 6,000. Buy 5,700 LEAP call (1 year out, deep ITM) for $400. Sell 6,050 call expiring in 30 days for $25. Each month, collect ~$25 in premium against the LEAP cost. After 16 monthly rolls, premiums collected = $400 = full LEAP cost basis.

### Diagonal Put Spread

Mirror of diagonal call spread on the put side.

---

## Intermediate tier — Debit Spreads

### Bull Call Spread (vertical call debit spread)

**Legs:** Long 1 call at lower strike K1, short 1 call at higher strike K2.

**Thesis:** Moderately bullish. Cheaper than long call — gives up upside above K2.

**Max profit / loss:** (K2 − K1) − net debit / net debit.

**Net Greeks:** Δ positive, Γ ± (depends on spot), Θ negative, ν + / −.

**Worked example:** SPX 6,000. Buy 6,000 call for $35, sell 6,100 call for $15. Net debit = $20 ($2,000). Max profit = $100 − $20 = $80 ($8,000) if SPX ≥ 6,100 at expiration. Max loss = $2,000.

### Bear Put Spread

Mirror — long higher put, short lower put. Same risk/reward structure.

---

## Intermediate tier — Directional structures

### Long Straddle

**Legs:** Long 1 call + long 1 put, both at same strike K (typically ATM).

**Thesis:** Big move expected, direction unknown. Pure long volatility.

**Max profit / loss:** Unbounded / Total debit paid.

**Net Greeks:** Δ ≈ 0 at K, Γ very positive, Θ very negative (paying time decay on two long options), ν very positive.

**Regime fit:** Best when realized vol exceeds implied at entry; worst in calm regimes.

**Worked example:** SPX 6,000, 30 DTE. Buy ATM straddle for $80 (call $40 + put $40). Total debit = $80 ($8,000). Breakeven up = 6,080; down = 5,920.

### Long Strangle

Long OTM call + long OTM put. Cheaper than straddle, needs bigger move to break even.

### Inverse Iron Butterfly / Inverse Iron Condor

Inverse of credit-spread neutral structures — defined-risk long-vol bets. Pay debit, profit on movement away from body.

### Collar

**Legs:** Long 100 shares + long 1 protective put + short 1 covered call. Often structured zero-cost.

**Thesis:** Long stock with both downside protection AND capped upside. The "JPM Hedged Equity Fund" collar is this on SPX.

**Net Greeks:** Δ positive (less than +1.0), Γ ≈ 0, Θ ≈ 0, ν ≈ 0 (the long put vega offsets short call vega).

**Worked example:** Own 100 SPY at $580. Buy 1 SPY 560 put for $5. Sell 1 SPY 600 call for $5. Zero net cost. Upside capped at $600; downside capped at $560.

---

## Advanced tier — Naked structures

### Short Put (Naked)

Same payoff as cash-secured put but using margin (lower buying-power requirement). Subject to margin expansion in stress (Section 3C). Reg-T margin requirement is approximately 20% of strike value − OTM amount.

### Short Call (Naked)

Pure short volatility, no upside protection. Requires significant margin and explicit broker approval. **Max loss unbounded.** Rarely retail-appropriate.

**Worked example:** Avoid. Use defined-risk call credit spread (bear call spread) instead.

---

## Advanced tier — Neutral structures

### Short Straddle

Short 1 call + short 1 put, both at same strike K. Maximum credit, maximum risk. **Pure short volatility with unbounded loss.** Catastrophically dangerous in stress.

### Short Strangle

Short 1 OTM call + short 1 OTM put. Wider, higher-probability version of short straddle. Common VRP harvest vehicle. When used systematically with cash-secured collateral (XSP strangles), can be operationally viable.

**Worked example:** SPX 6,000, 45 DTE. Sell 5,900 put for $30, sell 6,100 call for $30. Total credit = $60 ($6,000). Wins if SPX between 5,840 and 6,160 at expiration. Probability of profit ≈ 70%, loss-to-credit ratio if either tail is hit can be 5-10×.

### Long Call Condor / Long Put Condor

Same payoff shape as iron condor, all calls or all puts. Used when puts are illiquid or skew makes one type preferable.

---

## Advanced tier — Ratio Spreads

### Call Ratio Backspread

**Legs:** Short 1 ITM/ATM call, long 2 (or 3) OTM calls.

**Thesis:** Bullish but with little downside (often zero-cost or small credit). Profits big on a strong rally.

**Max profit / loss:** Unbounded upside / Limited (typically the difference between strikes minus net credit).

**Worked example:** SPX 6,000. Sell 1 × 6,000 call for $40. Buy 2 × 6,100 calls for $20 each ($40 total). Net cost = $0. If SPX explodes to 6,400: short call loss = $40,000, long calls gain = $60,000 = $20,000 profit.

### Put Ratio Backspread

Mirror — bearish backspread. Profits big on a crash. Effective tail-hedge structure.

### Broken Wing Butterflies (call/put)

Butterfly with one wing wider than the other — eliminates one side's tail risk. Often opened for a credit.

---

## Advanced tier — Income variants

### Covered Short Straddle

**Legs:** Long 100 shares + short 1 ATM straddle. Heavy income on a stock you want to own. Highly negative gamma — double assignment exposure. Effectively two short-put-equivalent positions through put-call parity.

### Covered Short Strangle

Long 100 shares + short 1 OTM strangle (short OTM put + short OTM call, different strikes). Modest income with less assignment pressure than the covered short straddle above — the OTM strikes give the underlying room to move before either short leg goes ITM.

---

## Advanced tier — Other directional structures

### Bull/Bear Call/Put Ladders

Three-strike asymmetric structures. Premium income with capped profit zone and uncapped risk on one side. **Bull Call Ladder:** Long K1, short K2, short K3 — unbounded loss above K3.

### Jade Lizard

**Legs:** Short 1 OTM put + short 1 OTM call credit spread (long call further OTM).

**Thesis:** *Provided* total credit ≥ call-spread width → **zero upside risk**. All risk is on the downside. The "credit ≥ width" condition is the defining feature of the structure — if your credit is less than the call-spread width, you have a regular short-put + short-call-spread combo, not a Jade Lizard, and you have risk on both sides.

**Worked example:** SPX 6,000. Sell 5,950 put for $42. Sell 6,080 call for $18. Buy 6,110 call for $9. Net credit = $42 + $18 − $9 = $51 ($5,100 per contract). Call-spread width = 6,110 − 6,080 = $30. Credit $51 ≥ width $30 → **zero upside risk verified**: at any SPX print at or above 6,110, the call spread is worth its full $30 width, but the $51 credit you collected exceeds that, so you keep at least $51 − $30 = $21 (i.e., $2,100). The entire risk is on the put side: if SPX prints below 5,950 at expiration, you're assigned long stock at 5,950 minus the $51 credit = effective basis 5,899.

**Common arithmetic trap.** Many published "Jade Lizard" examples (and trading-platform builders) quote a call-spread width *larger* than the credit, then still call the structure a Jade Lizard. It isn't. Always verify credit ≥ width before relying on the no-upside-risk property.

### Reverse Jade Lizard

Mirror — short OTM call + short OTM put credit spread. No downside risk if credit ≥ put-spread width.

### Call/Put Ratio Spreads (debit version)

Long 1 ITM + short 2 OTM. Modest directional bet with premium income, but uncapped risk if underlying moves through the short strikes.

---

## Expert tier — Synthetic and Arbitrage

### Long/Short Synthetic Future

**Legs:** Long call + short put (long synthetic) or short call + long put (short synthetic), both at same strike.

**Net Greeks:** Δ ≈ ±1.0, Γ ≈ 0, Θ ≈ 0, ν ≈ 0 (all option Greeks cancel out by put-call parity).

**Use case:** When borrow on the underlying is hard or expensive (short squeeze in single stock), the synthetic can be cheaper than the literal stock.

### Synthetic Put

Short 100 shares + long 1 call at same strike. Replicates a long put. Used when listed puts are illiquid or expensive.

### Long/Short Combo

Combo = synthetic long or short stock. Used as half of a put-call parity arbitrage trade.

### Strip / Strap

Asymmetric straddle ratios. Strip = 1 call + 2 puts (bearish bias). Strap = 2 calls + 1 put (bullish bias). Long convexity in both directions with asymmetric weight.

### Long/Short Guts

Long/short ITM call + ITM put. Same vol exposure as straddle but more capital-intensive.

### Double Diagonal

Two diagonal calendars combined — one on the call side and one on the put side, at different strikes. Income from near shorts + forward vol via far longs.

### Box Spread — synthetic loan / borrow

**Legs:** Long call K_low + short call K_high + short put K_low + long put K_high. All four options at the same expiration, same underlying. The combination locks in a payoff equal to the width (K_high − K_low) at expiration, regardless of where the underlying prints.

**Net Greeks:** Δ ≈ 0, Γ ≈ 0, Θ ≈ 0, ν ≈ 0. By put-call parity, the box is *deterministic* — every Greek cancels.

**Use case:** **The box spread is a synthetic loan.** If you *sell* the box (collect the net credit upfront, owe the width at expiration), you've borrowed money at an implied interest rate equal to the gap between the net credit and the width, annualized over the days to expiration. If you *buy* the box (pay the net debit upfront, receive the width at expiration), you've lent money at that same implied rate.

For SPX, where boxes get tax-advantaged 1256 60/40 treatment, the box is the cleanest available retail borrowing or lending instrument: the rate is often within 5–25 bps of broker margin call rates for borrowing, and within a few bps of T-bill rates for lending. **Sold** SPX boxes are the institutional retail-tier alternative to broker margin loans for accessing leverage; the implied rate is typically materially below the margin rates that retail brokers charge (where the broker's spread over fed funds is often 100–400 bps).

**Worked example:** SPX 6,000, 90 DTE. Construct a box at strikes 6,000 / 6,100. Width = $100 per share = $10,000 per box. Suppose the net credit received from selling the box is $9,940. Implied loan: receive $9,940 today, owe $10,000 in 90 days. Implied annualized rate = (60 / 9,940) × (365 / 90) ≈ **2.45% APR**. If T-bills yield 4.2%, that's a *very cheap* loan — but liquidity in box spreads on listed-only exchanges varies widely, and you generally need to trade them on tastytrade, Interactive Brokers, or a specialty broker that quotes box-spread liquidity. Some brokers won't execute boxes at all.

**Failure modes:**

- **Early assignment on the short legs.** Even SPX boxes (European) are safe; SPY (American) boxes carry early-assignment risk on the short put (deep ITM puts get exercised early when the discounted strike exceeds time value). Stick to European-style index options for boxes.
- **Counterparty / clearing-firm risk.** A famously cautionary tale: a Robinhood user in 2019 sold "infinite leverage" by repeatedly selling boxes — the system didn't margin the future obligation correctly. The leverage was real; when SPX moved, the user was wiped out by margin calls on positions that had been booked as a riskless arbitrage. The box itself is riskless at expiration; *the path to expiration* can produce margin calls if the broker doesn't compute the offsetting risk correctly.
- **Friction.** Round-trip execution cost on a four-leg structure is typically 1–4 cents per share of width. On a $10,000 box, that's $100–$400 — meaningful relative to the ~$60 implied-rate spread above.

**The honest framing:** boxes are an *interest-rate* instrument that happens to be constructed out of options. The Greeks are not the interesting part; the implied rate is.

### Conversion / Reversal

**Conversion:** long stock + short call + long put at same strike (=long synthetic short via puts + actual long stock). The position is delta-neutral and locks in a small profit if the put-call parity gap is mispriced in the right direction.

**Reversal:** the mirror — short stock + long call + short put. Used when the parity gap is mispriced the other way.

Both structures are professional arbitrage trades that retail traders almost never see economic versions of — bid-ask costs typically exceed the arbitrage spread. The pedagogical point is that *put-call parity is enforced by the existence of these structures*. Anyone who quotes prices that violate parity is offering an immediate arbitrage to professional desks; the prices snap back within milliseconds.

---

## Cards are starting points, not signals

A payoff geometry is necessary but not sufficient. Every strategy above also requires:
- A market thesis (Section 10A.5)
- A regime check (Section 10A dashboard + 10F composite)
- A conviction score (Section 12B)
- An explicit sizing rule (Section 12C)
- A pre-committed kill condition

Picking a structure because the payoff diagram looks attractive is the most common retail failure mode. **Remember that the structure is just the vehicle for expressing a forecast, not the forecast itself.** The work that produces edge is in steps 1, 2, and 3 above — not in selecting an exotic combination of legs.

---

## Appendix · View → structure cross-index

The strategy cards above are organized by structural family for reference lookup. For trade design, however, you typically start with a *view* and look for the structures that express it cleanly. This cross-index provides that inverse mapping.

### How to use this table

1. Identify your view from the left column ("I think SPX will drift up over 2-4 weeks").
2. The middle column lists structures that express the view, ordered roughly by preference for a typical swing-trading retail account.
3. The right column flags structures that *look* like they'd work but have hidden problems for this view.

| View | Prefer (in order) | Avoid (and why) |
|---|---|---|
| **Modest bullish drift** (1-3% over 2-4 weeks) | Equity → Long call spread (45 DTE) → Put credit spread (30 DTE, below support) → Diagonal call (back ATM, short front near target) | Naked long call (theta + vega risk for marginal directional gain); Short put strangle (asymmetric tail) |
| **Strong bullish breakout** (>5% in 1-2 weeks) | Equity → Long call (30-60 DTE, slightly OTM) → Long call spread (if IV elevated) | Calendar/diagonal (slow-drift vehicles; wrong for breakouts) |
| **Bearish breakdown / momentum continuation down** | Long put spread (30-60 DTE) → Short shares (if equities account) → Bear call spread (above resistance) | Naked long put (vega risk on the spike); Short call (unbounded loss) |
| **Modest bearish drift** | Equity short → Put debit spread → Call credit spread | Long put (overpays for slow move) |
| **Mean reversion: oversold → rebound** | Long equity → Short put credit spread → Long call spread | Long straddle (no directional bias needed; bias here is bullish); Iron condor (capped upside) |
| **Mean reversion: overbought → fade** | Short equity → Bear call spread → Put debit spread | Naked call (unbounded); long put (overpriced after the run) |
| **Range-bound consolidation** (no clear direction) | Iron condor → Iron butterfly → Short strangle (advanced; defined-size only) | Calendar/diagonal (these need a slight directional bias, not pure range) |
| **Compressed → expecting volatility expansion** (direction unknown) | Long straddle → Long strangle → Calendar (long forward vol) | Short premium of any kind (you'd be selling vol that's about to rise) |
| **Vol expansion priced in, expecting crush** | Short straddle (defined-risk preferred via iron butterfly) → Iron condor → Calendar with crush expectation | Long straddle (you'd be buying vol that's about to crush) |
| **Income on existing equity position** | Covered call → Collar (if hedging concern) → Diagonal covered call | Selling cash-secured puts on the same name you already own (concentrates risk) |
| **Pre-earnings momentum (exit before event)** | Equity → Long call (30-45 DTE) → Long call spread | Diagonal call (front-month short loses on IV ramp); Calendar (same issue) |
| **Post-earnings drift / gap-and-go (PEAD)** | Equity → Long call spread (30-45 DTE) → Put credit spread (below the gap) | Calendar/diagonal (post-event surface is collapsed; these are pre-event vehicles); 7-DTE options (theta destroys before drift develops) |
| **Hedging a long equity book** | Long put (30-90 DTE, 5-10% OTM) → Collar → Put spread (defined cost) | Selling the underlying (gives up upside) — depends on tax/cost-basis context |
| **Skew trade: put skew rich, expecting normalization** | Put ratio spread (long inner, short more outer) → Short put spread funded by put debit | Naked short far-OTM put (catches the falling knife) |
| **Term structure trade: front rich vs back** | Calendar (sell front, buy back) → Diagonal (same idea, different strikes) | Direct outright vol trade without the term structure exposure |
| **Synthetic financing (no cash for shares)** | Synthetic long (long call + short put ATM) → Long deep ITM call (acts like shares) | Margin equity (uses interest, not directly synthetic) |
| **Long volatility hedge for a short-vol book** | Long VIX call (90-180 DTE, OTM) → Long SPX put (90+ DTE, 8-10% OTM) → Long calendar | Short-dated VIX calls (theta destroys before stress unfolds) |

### Notes on the cross-index

- **The preference ordering is for typical retail swing accounts ($100k-$1M, options-enabled, comfortable with 30-60 DTE positions).** Different scales and risk preferences justify different orderings; portfolio managers running pure premium-selling books have different defaults than discretionary swing traders.
- **Liquidity is assumed.** Many structures listed require deep options markets (SPX, SPY, QQQ, large-cap single names). On illiquid underlyings, equity is often the only safe expression.
- **Tax context matters.** SPX/XSP enjoy 1256 60/40 treatment; SPY does not. Cards 1-7 favor cash-settled SPX/XSP equivalents for the same view when account size permits. See Section 3C.
- **The "avoid" column is structural, not absolute.** A structure listed as "avoid" might be correct in unusual conditions (e.g., a calendar might work for a breakout if the implied move surface is unusually flat). The avoid column captures the *typical* case.
- **Greek profiles still apply.** Every structure has its own delta/gamma/theta/vega profile. The cross-index narrows your candidate set; the strategy cards above provide the Greek details that disambiguate among candidates.

When designing a trade: identify view → narrow candidates via this index → consult strategy cards for Greeks/risk → apply 12B conviction or 12B Real Value (single names) → enter via 12C pipeline.

---

## Appendix A · Options margin mechanics

Margin requirements determine *how big* a position the broker will allow, which directly caps the strategies you can run. The same legs produce wildly different margin charges across the three retail margin regimes.

### Cash account

You post the full notional of any obligation you take on. Cash-secured puts require strike × 100 cash per contract. Covered calls require owning the underlying shares. No naked short calls or short puts. No spreads with short legs uncollateralized.

This is the most restrictive regime and also the safest: there are *no margin calls because there is no borrowed margin*. Most retail accounts that aren't actively trading should default to cash accounts and only upgrade when the strategy demands it.

### Reg-T margin

Formula-driven margin requirements. The key Reg-T charges for options:

- **Long call or long put:** Pay the premium in full. No further margin.
- **Short uncovered call:** 20% of underlying value, minus OTM amount, plus the option premium, with a floor of 10% of underlying. For SPX 6,000 with a 6,100 strike short call: 0.20 × 6,000 − 100 = $1,100/share × 100 = $110,000 of margin per contract.
- **Short cash-secured put:** 20% of underlying minus OTM amount + premium, same formula, floored at 10%.
- **Vertical spread (credit):** Margin = width of spread − net credit received. A 10-wide SPX put credit spread for $2 credit requires $800 margin per contract.
- **Vertical spread (debit):** Pay the net debit; no further margin.
- **Iron condor / iron butterfly:** Margin = the larger of the two vertical-spread margins (since the underlying can't be in both wings simultaneously). This is the *symmetrical-wings* netting; non-symmetrical wings get treated differently.
- **Calendar / diagonal:** Long-leg debit minus short-leg credit, with the long expiration counting fully and the short subtracted (you net the short credit against the long debit).

Reg-T is *fixed* and *formulaic*. It doesn't move with realized volatility. In stress, your margin requirement on a $1,100 short call stays $1,100; what changes is your account equity if the position goes against you. The danger in Reg-T is not margin expansion but *position size relative to equity* — if equity falls and margin obligation doesn't, you get a margin call.

### Portfolio Margin (PM)

PM uses *risk-based* margin: the broker simulates your full portfolio under a ±15% SPX move combined with implied-volatility shocks, and requires you to post collateral against the *worst-case loss* in that scenario set. For diversified, hedged portfolios, PM is far more capital-efficient than Reg-T — same risk, but the broker netting actually reflects that the position is hedged.

The catch: **PM is stress-tested**. When realized volatility spikes, the broker's implied-vol shock parameter widens; the worst-case scenario gets worse; the margin requirement expands. In calm markets, a PM account might run at 5-10× the leverage Reg-T would permit. In a March-2020 or Volmageddon-type stress, the same PM account could see margin requirements double or triple overnight.

PM requires a minimum account size (typically $125,000, sometimes $150,000-200,000 depending on broker), demonstrated experience, and an application process. The capital efficiency is real, but so is the stress-amplification.

### SPAN — futures and options on futures

For futures (ES, MES, etc.) and options on futures (also ES options, /VX VIX futures, /CL crude options), margin is computed using **SPAN** (Standard Portfolio Analysis of Risk), a risk-based system developed by CME. SPAN is conceptually similar to PM — it simulates a range of price and vol scenarios and requires posting against the worst case — but it operates at the *exchange clearing* layer, so the parameters are set by the exchange rather than the broker, and they apply uniformly across all futures-cleared accounts.

SPAN is typically far more capital-efficient than Reg-T for futures and options on futures. A single ES futures contract has roughly $13,000-15,000 of initial SPAN margin — versus the $300,000 notional. This is why futures are the cleanest leveraged equity exposure available: SPAN's risk-based approach captures the actual hedging, the contract is European, and the 1256 tax treatment is automatic.

### What to take away

The choice of margin regime is a strategic decision tied to portfolio composition and stress tolerance, not a "more is better" choice. Cash accounts have zero margin call risk. Reg-T offers leverage at a fixed cost. PM offers capital efficiency that contracts violently in stress. SPAN offers the cleanest risk-based margin for futures-based strategies. Match the regime to the strategy.

---

## Appendix B · Exercise and assignment mechanics

Options exercise is governed by the Options Clearing Corporation (OCC), which is the central counterparty for every listed US options contract. Understanding the OCC process eliminates most of the "surprises" that hit traders on expiration days.

### Standard expiration timeline (monthly equity options, third Friday)

- **Thursday close (T-1):** All open positions still alive. Wholesalers post final-hour quotes. Pin risk peaks for short options near strikes.
- **Friday close (T = expiration, ~16:00 ET for equities, 16:15 ET for SPX/XSP):** Final settlement print computed. Equity options settle to the official 4:00 PM close. SPX/XSP weekly options settle to the 4:15 PM PM-settled close. SPX monthlies (third-Friday standard) settle to the Friday-morning SOQ (Special Opening Quotation, an opening-print auction with its own quirks).
- **Friday evening — auto-exercise:** Per OCC Rule 805, any long option that closes more than $0.01 in-the-money is automatically exercised by the OCC unless the holder explicitly files a "do not exercise" instruction with their broker by the cutoff (typically 5:30 PM ET Friday). This is the source of most "I got assigned overnight" surprises — the OCC's $0.01 threshold is unforgiving.
- **Saturday — assignment notification:** The OCC notifies clearing firms of net exercises. Clearing firms allocate assignment to short holders using one of two methods (random or FIFO; brokers disclose which they use).
- **Monday morning — settlement:** Equity options assigned settle as stock-for-cash via DTC. Cash-settled index options settle as wire transfers.

### Early exercise (American style)

For American-style options (single-name equities, SPY, QQQ, IWM, etc.), the holder can exercise *any* trading day before expiration. The OCC accepts exercise notices throughout the day; assignment is allocated to short holders typically overnight, settled the next business day.

The economic conditions for rational early exercise:

- **American calls on dividend-paying stocks:** exercise just before ex-dividend if (dividend > remaining time value). The trader captures the dividend at the cost of the option's remaining time value.
- **Deep ITM American puts:** exercise when (strike × interest rate × time-to-expiry > remaining time value). The trader receives the strike cash now and reinvests at the risk-free rate.

For European-style options (SPX, XSP, NDX, VIX, RUT — all cash-settled indices), early exercise is impossible by contract design. The contract specification only permits exercise at the official expiration print.

### The "expired worthless" edge case

A short option holder occasionally sees an option close $0.005 ITM at the close, just under the OCC's $0.01 auto-exercise threshold. The option is recorded as "expired" and the short holder keeps the full premium. But the underlying may continue to trade in after-hours, sometimes pushing through the strike enough that the long holder *manually exercises* (this is allowed up to the 5:30 PM cutoff). The short holder, having priced the position as "expired," wakes up Monday to discover an unwanted assignment.

The defense: **close any short option trading within $0.05 of the strike in the final hour before expiration.** The OCC threshold is too coarse to rely on; manual exercise by a long holder during the post-close window is real risk. The cheapest insurance is closing the short.

### SOQ settlement for SPX monthlies (third Friday)

Standard monthly SPX options (third Friday of every month) settle to the **Special Opening Quotation (SOQ)** — a Friday-morning opening-print auction that produces a single index level used for settlement.

The SOQ has historically been a source of pin-risk surprises. The opening-print auction can produce settlement values materially different from the previous Thursday's close, especially in high-vol regimes. A trader short an SPX call at 6,000 with SPX closing at 5,998 on Thursday might find the SOQ Friday morning prints at 6,005 — and the short call is assigned at 6,005, generating an unexpected $500/contract loss that didn't exist at the Thursday close.

The defense: **close SPX monthly options Thursday afternoon, not Friday morning.** This is the single most important operational rule for trading SPX monthlies. Weekly SPX (PM-settled to the Friday 4:15 PM close) does not have this SOQ risk; only the monthlies do.

### Cash-settled vs physical-settled

Cash-settled (SPX, XSP, NDX, RUT, VIX): on assignment, your account receives or pays cash equal to the difference between the strike and the settlement level, multiplied by the multiplier. No shares change hands. No weekend gap risk on the underlying.

Physical-settled (SPY, QQQ, IWM, AAPL, NVDA, every single-name): on assignment, shares actually move. Long call exercised → you receive 100 shares at strike. Short put assigned → you receive 100 shares at strike (paid for from your account). Short call assigned → you deliver 100 shares (sold short from your account if you don't already own them). The shares show up Monday morning, fully exposed to the weekend gap.

Cash-settlement is structurally cleaner for systematic income strategies. This is the central operational reason the curriculum prefers XSP over SPY for retail premium-selling vehicles, alongside the 1256 tax advantage.
