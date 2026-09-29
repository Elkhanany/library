# Chapter 12 — Setup cards
## One-page operational references

> **Core intuition.** A setup card is a one-page operational reference that compresses a strategy into the form needed for live execution: edge source, regime requirement, sizing, kill rule. This chapter has cards for every tradeable strategy in the book, plus "do-not-trade" cards for the rejected strategies. The cards are designed for printing, taping next to your monitor, or copying into a trading journal.

---

## Card format

Every card has the same fields:

```
NAME: [strategy name]
EDGE SOURCE: [risk premium / behavioral / institutional / microstructure]
CATEGORY: [foundation / factor / overlay / filter / rejected]
EVIDENCE TIER: [T1 / T2 / T3]
REGIME REQUIRED: [conditions for entry]
INSTRUMENT: [vehicle]
ENTRY: [specific rule]
EXIT: [specific rule]
EXPECTED RETURN SOURCE: [what generates P&L]
MAIN HIDDEN EXPOSURE: [crash beta / decay / etc]
STRESS LOSS S1/S2/S3: [P&L grid]
SIZING CAP: [max notional / max portfolio loss]
KILL RULE: [trigger]
CONFIDENCE GRADE: [high / medium / low]
NOT TO TRADE WHEN: [explicit conditions]
```

---

## Allocatable strategies — Setup cards

### CARD 01: Long Equity (ERP)

```
NAME:               Long Equity / ERP
EDGE SOURCE:        Risk premium (Source 1)
CATEGORY:           Foundation premium
EVIDENCE TIER:      T1 (Mehra-Prescott; Dimson-Marsh-Staunton 35 markets)
REGIME REQUIRED:    Default state; reduce only on extreme valuation+breadth
INSTRUMENT:         SPY/VOO (US), VXUS (ex-US), VT (global)
ENTRY:              Lump sum or DCA into broad index
EXIT:               No tactical exit; tax-aware rebalancing only
EXPECTED RETURN:    Long-run real ~4-5% (forward-looking)
                    Long-run nominal ~7-9%
HIDDEN EXPOSURE:    Crash beta = 1.0 by definition
                    Multi-decade negative real return possible (Japan 1989-2010)
STRESS LOSS:
  S1 (-10/+10):     -10% of allocation
  S2 (-20/+25):     -20% of allocation
  S3 (-35/+50):     -35% of allocation
  S4 (1987 gap):    -22% overnight
SIZING CAP:         50-65% of portfolio
KILL RULE:          1/CAPE - 10Y < -1% sustained AND 12m EPS growth negative
                    → reduce 25%, not full exit
CONFIDENCE:         HIGH
NOT TO TRADE WHEN:  Cannot tolerate 35-50% drawdown
                    Need capital within 5 years
```

### CARD 02: VRP Harvest (XSP cash-secured put-write)

```
NAME:               VRP Harvest / XSP ATM Monthly Put-Write
EDGE SOURCE:        Risk premium (Source 1)
CATEGORY:           Foundation premium
EVIDENCE TIER:      T1 (Bondarenko, Carr-Wu, Jurek-Stafford)
REGIME REQUIRED:    VIX/VIX3M < 1.00 + 21d realized < implied + TED < 100bps
INSTRUMENT:         XSP options (mini-SPX, 1256 60/40 tax)
ENTRY:              Sell ATM monthly put, 30-45 DTE
                    Cash-secured (full collateral against strike)
EXIT:               21 DTE → close and roll
                    OR if MTM gain > 50% of premium → take profit
EXPECTED RETURN:    Premium ~2-3% strike/month
                    Net ~3-5% annual after losses (realistic retail)
HIDDEN EXPOSURE:    Tail beta ~1.0 in left tail
                    Skew tax (-2.09 vs SPX -0.81)
STRESS LOSS (per ATM contract on $580 strike):
  S1 (-10/+10):     -$3,500 / contract MTM
  S2 (-20/+25):     -$10,000 / contract MTM
  S3 (-35/+50):     -$20,000 / contract MTM
SIZING CAP:         10-15% portfolio risk
                    Max contracts: B_exp / L_max where B_exp = 5% portfolio
KILL RULE (LAYERED):
  VIX/VIX3M > 1.00 for 3 closes → halt new entries
  VIX/VIX3M > 1.05 for 3 closes → reduce sizing 50%
  21d realized > implied → halt new entries
  Sleeve drawdown > 20% PTP → close entirely, reassess
RE-ENTRY:           VIX/VIX3M < 1.00 for 5 closes → 25% target
                    Then 50%, then 100% over 3 weeks
CONFIDENCE:         HIGH (with discipline)
NOT TO TRADE WHEN:  Backwardation
                    Negative VRP (realized > implied)
                    Major macro event imminent (FOMC, CPI, jobs)
                    Can't tolerate 6-month underwater periods
```

### CARD 03: Trend-Following (DBMF)

```
NAME:               Trend-Following / Time-Series Momentum
EDGE SOURCE:        Mixed (mostly risk premium, some behavioral)
CATEGORY:           Foundation premium
EVIDENCE TIER:      T1 (Hurst-Ooi-Pedersen 140 years; Moskowitz-Ooi-Pedersen)
REGIME REQUIRED:    None — structural allocation
INSTRUMENT:         DBMF (preferred) or KMLM (alternative)
                    NOT: stacked vehicles unless deliberately seeking leverage
ENTRY:              Build over 3 months, not lump sum
EXIT:               Hold across cycles; do not auto-exit during droughts
EXPECTED RETURN:    Live realized 0.20-0.40 Sharpe retail
                    ~3-6% annual standalone
                    Larger portfolio contribution via crash skew
HIDDEN EXPOSURE:    Multi-year drought possible (2011-2018 was 7 years)
                    Manager dispersion 200-400 bps annually
STRESS LOSS:
  S1 (-10/+10):     -2 to +1% (mostly flat)
  S2 (-20/+25):     -2 to +5% (often positive)
  S3 (-35/+50):     -5 to +15% (often strongly positive — crash hedge)
  Slow drawdown:    Often POSITIVE (8 of 10 largest 60/40 drawdowns)
SIZING CAP:         10-15% of portfolio
KILL RULE:          DBMF tracking to BTOP50 > 4% annualized for 4 quarters
                    OR drawdown > 25% PTP
                    NOT: poor 1-year performance (this triggers normally)
CONFIDENCE:         HIGH (for portfolio role; medium for standalone)
NOT TO TRADE WHEN:  Cannot tolerate 3-7 year droughts
                    Will panic-exit during chop regimes
```

### CARD 04: Cross-Asset Carry

```
NAME:               Cross-Asset Carry
EDGE SOURCE:        Risk premium (Source 1) + institutional
CATEGORY:           Foundation premium (supplementary)
EVIDENCE TIER:      T1 (Koijen-Moskowitz-Pedersen-Vrugt 2018)
REGIME REQUIRED:    TED < 200 bps + MOVE < 150
INSTRUMENT:         RSST (return-stacked products) if available
                    Self-managed: complex; not recommended
EXPECTED RETURN:    Live retail Sharpe 0.15-0.30
                    Diversified across asset classes (FX/bonds/commodities/equity)
HIDDEN EXPOSURE:    Liquidity events crash carry trades violently
                    AUDJPY-style ~40% drawdowns in stress
STRESS LOSS:
  S1 (-10/+10):     -3% of allocation
  S2 (-20/+25):     -8% of allocation
  S3 (-35/+50):     -15 to -25% of allocation
SIZING CAP:         5-10% of portfolio
KILL RULE:          TED > 200 bps OR MOVE > 150 → halt new positions
                    Carry-spread-to-vol < 0.3 → reduce sizing
CONFIDENCE:         MEDIUM (limited retail access at quality)
NOT TO TRADE WHEN:  Liquidity stress regime
                    Implementation requires self-managed multi-asset (skip)
```

### CARD 05: Quality Factor Tilt (QUAL)

```
NAME:               Quality / Profitability Factor
EDGE SOURCE:        Mixed (risk premium + behavioral)
CATEGORY:           Equity factor tilt
EVIDENCE TIER:      T1 (Novy-Marx 2013, Asness-Frazzini-Pedersen 2019)
REGIME REQUIRED:    None — structural tilt
INSTRUMENT:         QUAL (iShares MSCI Quality, 0.15%)
                    Alternative: COWZ (free cash flow, 0.49%)
ENTRY:              Replace 8-12% of equity allocation with QUAL
EXIT:               Hold across cycles; tax-aware rebalancing
EXPECTED RETURN:    Live retail ~0.30-0.45 Sharpe (above SPX baseline ~0.4)
                    Excess return ~50-150 bps annual
HIDDEN EXPOSURE:    Equity beta ~0.95 (still loses in crashes)
                    Tracking error to SPX ~3-4%
STRESS LOSS:        ~90% of SPX loss in crashes
SIZING CAP:         8-12% of equity sleeve
KILL RULE:          24-month rolling Sharpe < 0 → reduce 50%
                    Tracking to academic factor > 4% → switch vehicle
CONFIDENCE:         HIGH (most durable factor)
NOT TO TRADE WHEN:  Will panic-exit during 2-3 year underperformance
```

### CARD 06: Momentum Factor Tilt (MTUM)

```
NAME:               Cross-Sectional Momentum
EDGE SOURCE:        Behavioral (Source 2)
CATEGORY:           Equity factor tilt
EVIDENCE TIER:      T1 with decay (Jensen-Kelly-Pedersen 2023: ~47% post-pub)
REGIME REQUIRED:    No sustained equity drawdown >6 months
INSTRUMENT:         MTUM (iShares MSCI Momentum, 0.15%)
ENTRY:              5-10% of equity allocation
EXIT:               Reduce 50% during sustained equity drawdown >6 months
EXPECTED RETURN:    Live retail ~0.20-0.35 Sharpe
                    Excess return ~30-100 bps annual
HIDDEN EXPOSURE:    Crash risk during V-bottom reversals (-73% in 3 months 2009)
                    High turnover ~80%/year (tax inefficient in taxable)
STRESS LOSS:
  Slow drawdown:    Tracks SPX
  V-bottom rally:   -20 to -40% additional from momentum-specific crash
SIZING CAP:         5-10% of equity sleeve
KILL RULE:          After 6+ month sustained equity drawdown → reduce 50% until 3m equity return positive
                    Tracking to UMD > 4% → switch vehicle
CONFIDENCE:         MEDIUM (real but decayed)
NOT TO TRADE WHEN:  In a taxable account if alternatives available
                    During market bear-market V-shaped reversal
```

### CARD 07: Value Factor Tilt

```
NAME:               Value Factor (HML or composite value)
EDGE SOURCE:        Mixed (behavioral + risk premium)
CATEGORY:           Equity factor tilt
EVIDENCE TIER:      T1 with controversy (Arnott-Harvey-Kalesnik-Linnainmaa 2021)
REGIME REQUIRED:    None — structural; multi-decade patience required
INSTRUMENT:         RAFI fundamental funds (FNDX, FNDA)
                    OR AVUV (small-cap value with quality screen)
ENTRY:              3-8% of equity allocation
EXIT:               Hold through multi-year drawdowns
EXPECTED RETURN:    Live retail ~0.10-0.30 Sharpe above SPX
                    Highly cyclical
HIDDEN EXPOSURE:    Multi-year (5-10 year) drawdowns documented
                    2010-2020 worst value drawdown in modern history
SIZING CAP:         3-8% of equity sleeve
KILL RULE:          24-month rolling Sharpe < -0.3 → REASSESS, not auto-exit
                    Don't auto-cut during multi-year drawdowns
CONFIDENCE:         MEDIUM (real but path-punishing)
NOT TO TRADE WHEN:  Will panic-exit during 5-year drawdown
                    Have less than 20-year horizon
```

### CARD 08: Low-Vol Factor Tilt (USMV)

```
NAME:               Low-Volatility / BAB (long-only)
EDGE SOURCE:        Institutional (Source 3) + behavioral
CATEGORY:           Equity factor tilt
EVIDENCE TIER:      T1 with caveat (Novy-Marx-Velikov 2022 reduces FP Sharpe)
REGIME REQUIRED:    Avoid liquidity stress
INSTRUMENT:         USMV (iShares Min Vol, 0.15%) or SPLV
ENTRY:              3-8% of equity allocation
EXIT:               Hold; reduce slightly in liquidity stress
EXPECTED RETURN:    Live retail ~0.25-0.40 Sharpe
                    Lower drawdowns than SPX
HIDDEN EXPOSURE:    Still has equity beta ~0.6
                    Underperforms during high-beta rallies (2020-2021)
SIZING CAP:         3-8% of equity sleeve
KILL RULE:          Liquidity stress (TED > 200, MOVE > 150) → reduce 25%
CONFIDENCE:         MEDIUM (real but smaller than headline FP Sharpe)
NOT TO TRADE WHEN:  Highly leveraged long-short version (retail can't size safely)
```

### CARD 09: FOMC Cycle Overlay (Modulation)

```
NAME:               Cieslak FOMC Even-Week Overlay
EDGE SOURCE:        Institutional (Source 3) — Fed reaction function
CATEGORY:           Structural overlay
EVIDENCE TIER:      T2 (Cieslak et al. 2019; OOS replication thin post-2019)
REGIME REQUIRED:    Normal FOMC schedule (not break-glass intervention)
INSTRUMENT:         Time discretionary equity entries to even-week starts
                    DO NOT rotate SPY (tax-inefficient)
ENTRY:              Modulate, don't rotate
                    Tax-deferred: optional rotation 1.0× / 0.75× equity
EXPECTED RETURN:    +0.10-0.30 Sharpe addition (with caveats)
                    Possibly decayed post-2015
HIDDEN EXPOSURE:    Decay risk if Fed transparency continues to improve
SIZING CAP:         Modulation only — not new sleeve
KILL RULE:          2-year rolling odd-week return ≥ even-week → suspend
                    Implementation cost > 30 bps annualized → skip
CONFIDENCE:         LOW-MEDIUM
NOT TO TRADE WHEN:  Taxable account (tax acceleration kills small alpha)
                    Cycle disrupted (e.g., 2022 hiking cycle)
```

### CARD 10: EOQ Rebalancing Trade

```
NAME:               End-of-Quarter Pension Rebalancing
EDGE SOURCE:        Institutional (Source 3) — mandate-driven flow
CATEGORY:           Structural overlay
EVIDENCE TIER:      T2 (Etula et al. 2020; NBER WP 33554)
REGIME REQUIRED:    SPX-bond divergence > 1.5% during quarter
INSTRUMENT:         ES + ZN futures (1256 tax)
DIRECTION RULE:
  Stocks OUTPERFORMED bonds → SHORT ES / LONG ZN
  Stocks UNDERPERFORMED bonds → LONG ES / SHORT ZN
  ★ Sign correction from v1 framework — do not reverse ★
ENTRY:              T-5 trading days of quarter end
EXIT:               T+1 to T+3 of new quarter
EXPECTED RETURN:    ~17 bps next-day equity effect at extreme divergence
                    Untested live for retail
HIDDEN EXPOSURE:    Recent paper, retail replication uncertain
SIZING CAP:         0.5% portfolio risk per leg for first 8 quarters
KILL RULE:          After 4 quarters, hit rate < 50% OR P&L negative → suspend
                    Quarterly divergence < 1.5% → skip the trade
CONFIDENCE:         LOW-MEDIUM (T2, replication needed)
NOT TO TRADE WHEN:  Quarterly divergence < 1.5%
                    Personal P&L track < 4 quarters and negative
```

---

## Filters — Reference cards

### CARD F1: VIX Term-Structure Filter

```
FILTER:             VIX / VIX3M ratio
USES:               Modulate short-vol sleeve sizing
RULE (LAYERED):
  Ratio > 1.00 for 3 closes:    Halt new short-vol entries
  Ratio > 1.05 for 3 closes:    Halt all put sales; reduce existing 50%
  Ratio > 1.15 for 3 closes:    Close non-essential short-vol
  Ratio < 1.00 for 5 closes:    Phased re-entry 25% / 50% / 100% over 3 weeks
DO NOT:             Buy VXX or VIX futures based on this filter
```

### CARD F2: Realized vs Implied Vol

```
FILTER:             21-day realized vol vs current implied vol
USES:               Confirm short-vol regime
RULE:
  Realized < Implied:           Premium-selling regime acceptable
  Realized > Implied:           Negative VRP — halt new entries
  Realized > Implied + 5 vol:   Close existing if oversized
DO NOT:             Treat as standalone signal (always combine with term structure)
```

### CARD F3: Liquidity Composite

```
FILTER:             TED, MOVE, HY OAS combined
USES:               Reduce all leveraged exposure
RULE:
  TED > 200 bps OR MOVE > 150 OR HY OAS > 600 bps → reduce all leveraged exposure 50%; halt new positions
NORMALIZATION:      Wait for sustained recovery before re-entering
```

### CARD F4: GEX Directional Sign (low-confidence)

```
FILTER:             GEX direction (positive vs negative)
USES:               Soft regime context only
RULE:
  Negative GEX → expect higher realized vol; reduce put-write 10-15%
  Positive GEX → expect compressed vol; OK to size normally
DO NOT:             Trade specific GEX levels (call wall / put wall)
                    Size positions based on GEX magnitude
NOTE:               Cboe 2025 — 0DTE MM hedging only ~0.2% of liquidity
                    Use as supplementary signal only
```

---

## DO-NOT-TRADE cards

These cards exist to inoculate the reader against narrative-driven retail bait.

### CARD X1: Pre-FOMC Drift

```
WHY YOU MIGHT BE TEMPTED:
  Lucca-Moench 2015 documented 49 bps avg pre-FOMC return 1994-2011
WHY IT'S DEAD:
  Kurov-Halova-Wolfe-Gilbert 2021: effect disappeared post-2015
  Cause: Fed transparency reforms (dot plot 2014, forward guidance)
LESSON:
  Mechanism-clear edges can decay suddenly when policy responds
DO NOT TRADE.
```

### CARD X2: S&P 500 Inclusion

```
WHY YOU MIGHT BE TEMPTED:
  Historical 7%+ inclusion premium (Shleifer 1986)
WHY IT'S DEAD:
  Greenwood-Sammon 2024: <1% post-2010
  Index funds got smarter; arbitrageurs ate the obvious mispricing
LESSON:
  Institutional edges can be eaten by sophisticated capital
DO NOT TRADE.
```

### CARD X3: Naive Single-Name Earnings Short-Vol

```
WHY YOU MIGHT BE TEMPTED:
  IV crushes 30+ vol points after earnings
  Premiums look "rich" 1-2 days before
WHY IT'S WRONG:
  Adams-Neururer 2020: NEGATIVE MEAN despite positive median at retail
  Single-name skew tax exceeds premium harvested
INSTITUTIONAL VARIANT:
  Cao-Han-Tong-Zhan 2022 cross-sectional 200+ names works
  Retail can't replicate the cross-sectional infrastructure
LESSON:
  Win rate ≠ EV; structural negative skew dominates at single-name retail
DO NOT TRADE (systematic single-name short-vol).
ACCEPTABLE:        Calendar spreads on rare opportunities (small)
```

### CARD X4: GEX Level Scalping

```
WHY YOU MIGHT BE TEMPTED:
  Public GEX models show specific "call walls" and "put walls"
  Compelling story about dealer hedging
WHY IT'S WRONG:
  Public GEX models are model-dependent (vendors disagree)
  Post-2022 0DTE explosion changed structure
  Cboe 2025: 0DTE MM hedging ~0.2% of SPX liquidity
LESSON:
  Narrative compellingness ≠ evidence quality
DO NOT TRADE (specific levels).
ACCEPTABLE:        Directional sign as low-confidence regime context only
```

### CARD X5: Systematic Iron Condors

```
WHY YOU MIGHT BE TEMPTED:
  "Defined risk" income strategy
  Markets are usually range-bound
  Theta accumulates daily
WHY IT'S WRONG:
  CBOE CNDR 1986-2024: ~690% return vs SPX TR ~5,500%
  Empirical underperformance over 38 years is decisive
  Wing breaks dominate aggregate P&L
LESSON:
  Defined per-trade max loss ≠ defined aggregate loss
DO NOT TRADE (systematic).
ACCEPTABLE:        Discretionary occasional condors at extreme IV (small)
```

### CARD X6: Put-Spread + LEAP Combination

```
WHY YOU MIGHT BE TEMPTED:
  "Short premium funds long LEAP"
  "Leveraged equity exposure with VRP edge"
WHY IT'S WRONG:
  Decomposition: ~1.4× SPX with embedded 50-150 bps leverage drag
  Net "edge" over simple leverage is approximately zero
  Path properties WORSE than ES futures
LESSON:
  Decomposition kills false-edge claims
DO NOT TRADE.
USE INSTEAD:       ES futures, 2× ETFs, or box-spread financing + SPY
```

### CARD X7: VIX ETPs (Long or Short)

```
LONG VIX (VXX, UVXY):
  -99.84% lifetime VXX 2009-2024
  Roll decay 5-15%/year normal, much higher in extended contango
  
SHORT VIX (formerly XIV):
  XIV terminated -96% in a single day Feb 2018
  SVXY de-leveraged but still subject to catastrophic moves
  
DO NOT TRADE either side.
USE INSTEAD:       SPX/XSP options directly with explicit position management
```

---

## How to use these cards

1. **Print or copy** the cards relevant to your portfolio
2. **Reference before trading** — verify every condition is met
3. **Update on regime change** — annotate "currently halted" / "currently active"
4. **Review quarterly** — confirm kill rules haven't triggered
5. **Annual recalibration** — review cards against latest evidence

The cards are deliberately rigid. Their value is in being binding when you're tempted to override them.

---

## A note on rigidity vs flexibility

Some readers will object: "But trading requires judgment, not rigid rules."

Trading at the *signal level* requires interpretation. Trading at the *strategy level* requires written rules. The card format formalizes the strategy level. Within each card, you exercise discretion about whether the conditions apply right now — but the cards themselves are not for daily revision.

The right balance: **discretion at observation; mechanism at execution.** When you see something interesting, you observe and interpret. When you decide to act, the cards constrain how. This is what disciplined trading looks like operationally.

---

## Self-check (chapter)

1. Pick 3 cards relevant to your portfolio. Verify each condition applies right now.
2. For each "do-not-trade" card, articulate why you might be tempted to trade it anyway. What's the empirical evidence that should override the temptation?
3. State the difference between a setup card (allocatable strategy) and a filter card (regime modulator).
4. What's the role of the kill rule in each card?
5. Why are the EOQ rebalancing direction rules called out specifically?

---

## Where this fits

Chapter 11 walked through reasoning chains. Chapter 12 compresses the operational specifics into one-page references. Chapter 13 will give the signal-to-trade pipeline (the grammar by which observations become positions). Chapter 14 covers portfolio framework, kill criteria, and revalidation cadence.

The cards in Chapter 12 are the operational layer of the framework. Chapters 13-14 are how everything fits together over time.

[← Previous: Chapter 11 — Worked examples](12_ch11_worked_examples.md) | [Next: Chapter 13 — Signal-to-trade pipeline →](14_ch13_pipeline.md)
