# Section 3 · Markets
*What you're actually trading.*

Before we describe the dealers' end of the trade in Sections 6-9, we have to be precise about what is *being* traded. "The S&P 500" is casually used in financial conversation as if it were a single object, but on a screen it is at least **six distinct products** — an index level, an ETF, a futures family, and three different options markets — each with its own settlement rules, contract size, tax treatment, dealer ecosystem, and trading hours. Confusion between them produces a surprising amount of bad retail decision-making, including some of the most expensive mistakes a US retail trader can make.

This section also covers the layer beneath the product: the **market microstructure** through which orders actually execute. The path from your click in a brokerage app to a printed trade involves a routing decision that determines who fills you, at what price, on what venue, and at what cost. Understanding this layer separates retail traders who lose 50 basis points per round trip to invisible costs from those who lose 5 basis points. The two layers together — what to trade and how to execute — define the operational baseline that every later strategy assumes.

The four sub-chapters: **3A** anatomizes SPX and its six tradeable instruments. **3B** walks through US equity microstructure, the National Best Bid and Offer, wholesalers and dark pools, and the current state of payment for order flow regulation. **3C** explains the four account tiers retail traders can access and the single most consequential operational choice in US options trading — Section 1256 tax treatment. **3D** closes with order types and execution discipline.

---

## 3A · What is the S&P 500, actually?

The S&P 500 is a list of approximately 500 US large-cap stocks chosen by the **S&P U.S. Index Committee**. Inclusion criteria include market capitalization (currently a $20.5 billion minimum as of 2025, periodically raised by S&P), domicile (US), liquidity (high public float and turnover), financial viability (positive as-reported earnings in the most recent quarter and trailing year), and a minimum public float share (now 50% as of 2025). The committee meets quarterly to make additions and deletions; rebalances happen on the third Friday of the rebalance month, and the trading volume on those days has historically spiked as index-tracking funds adjust their holdings.

The level you see quoted as "SPX" is a **float-adjusted, market-cap-weighted index**. Each component contributes to the index in proportion to the market value of its publicly tradeable shares — that is, excluding insider holdings, government holdings, and other restricted shares — divided by a continuously-updated number called the **divisor**:

```
SPX_t = (Σ_i Price_{i,t} × FloatShares_{i,t}) / Divisor_t
```

The divisor is the load-bearing piece nobody talks about. Its sole purpose is to keep the index level continuous across **structural events that would otherwise create artificial discontinuities** — index reconstitution (adds/deletes), spin-offs, special dividends that effectively return capital outside the float, and other corporate actions that change the float-adjusted market cap without reflecting a real change in shareholder value.

A few details that are commonly misstated:

- **Ordinary cash dividends do NOT change the divisor.** When a constituent goes ex-dividend, its stock price drops by roughly the dividend amount, the index level drops accordingly, and the divisor stays put. This is why SPX is a *price-return* index — the natural drift from dividend payments is built into the published level. (Total-return tracking lives in SPTR, which separately accrues a dividend index.)
- **Ordinary stock splits do NOT require divisor changes either** in a float-cap-weighted index. A 2-for-1 split halves the share price and doubles the float share count, so Price × FloatShares is unchanged. The divisor is unaffected. (This is unlike the price-weighted Dow Industrials, whose divisor *must* change for every split.)
- **What actually moves the divisor:** S&P committee adds and deletes (an addition increases the divisor so the index doesn't gap up; a deletion decreases it so it doesn't gap down), spin-offs (the parent's float market cap drops on the spin date, so the divisor drops to compensate), and special dividends large enough to be classified by S&P methodology as a return of capital.

The divisor is publicly disclosed by S&P (it's currently in the eight-billion range and drifts as the committee makes adjustments) but is rarely cited in financial media. Without it, the SPX level would gap visibly every time the committee reconstituted the index or a constituent spun off a subsidiary — and there are dozens of those events per year. The fact that the SPX level you saw yesterday is comparable in real economic terms to the level five years ago is entirely the divisor's job.

> *The SPX index level is a real number. The SPX trade is a derivative contract on that number. The two are connected by a divisor that is, in some sense, the most important number in equity finance — and one that 99% of retail traders have never heard of.*

### The six products that all track SPX

Below is the operational reference table. The same underlying exposure — the level of the S&P 500 — is delivered through six different contracts, each with its own price scaling, settlement convention, tax treatment, trading hours, and dealer infrastructure. Confusion between these products is one of the most expensive sources of retail error.

| Product | Full name | Multiplier | Tick | Settle | Tax | Hours | Why it matters |
|---|---|---|---|---|---|---|---|
| **SPX** | S&P 500 cash index options | $100 × index level | $0.05 / $0.10 | Cash; AM (monthly) / PM (weekly, 0DTE) | 1256 60/40 | 9:30–4:15 ET + extended | Largest contract size; institutional default; AM-settle has expiry-day quirks |
| **XSP** | Mini-SPX options | $100 (1/10th SPX) | $0.05 / $0.10 | Cash; PM | 1256 60/40 | 9:30–4:15 ET | Retail-friendly; same tax treatment as SPX; cleaner for cash-secured strategies |
| **SPY** | S&P 500 ETF options | $100 shares | $0.01 / $0.05 | **Physical** (shares delivered) | **Ordinary**; short-term gains if <1 yr | 9:30–4:00 ET + extended | Most liquid options on earth by volume; physical settle = assignment risk |
| **ES** | E-mini S&P 500 futures | $50 per point | 0.25 = $12.50 | Cash; quarterly (Mar/Jun/Sep/Dec) | 1256 60/40 | Near-24h Sun–Fri | Cleanest leveraged equity exposure; financing baked into basis |
| **MES** | Micro E-mini | $5 per point | 0.25 = $1.25 | Cash; quarterly | 1256 60/40 | Near-24h Sun–Fri | Retail-sized ES; 1/10th the size; same tax treatment |
| **VIX** | VIX options | $100 × index level | $0.05 | Cash; AM, Wednesday expiries | 1256 60/40 | Standard + extended | European-style; settles to SOQ Wed AM, which differs from VIX close |

A single contract of each, with SPX at 6,000:

- 1 SPX option contract represents $600,000 of notional exposure to SPX.
- 1 XSP option contract represents $60,000 — exactly 1/10th.
- 1 SPY option contract represents 100 shares of SPY at roughly $600 each = $60,000 (SPY is designed to track 1/10th the SPX index level, so 1 SPY ≈ 1 XSP in notional, but they're very different products operationally).
- 1 ES futures contract is $50 per point × 6,000 = $300,000 of notional.
- 1 MES futures contract is $5 per point × 6,000 = $30,000.
- 1 VIX option contract is $100 × VIX level (around $1,500 if VIX is at 15).

### Why three different settlement rules matter

Two SPX options expiring on the same Friday can settle to *different* prices, because monthly SPX expires AM while weekly and 0DTE SPX expire PM. AM settlement uses the **Special Opening Quotation (SOQ)** — a synthetic open-print constructed from the first reported trade of each constituent stock that morning. PM settlement uses the **official 4:00 PM close**.

The AM-PM gap is small on most days and large on event Fridays. If half the dealer book is hedged against AM-settle SPX and the other half against PM-settle SPX, the dealer carries intraday risk that AM ≠ PM. That risk is non-trivial on OPEX (third) Fridays, and it is one of the reasons OPEX Friday opens can show a sharp, uncorrelated move in the first ten minutes as dealers reconcile the SOQ they actually got versus the SOQ their books were hedged against. This mechanic is invisible to retail charts but is the canonical reason "the first thirty minutes of OPEX Friday are weird." If you're going to trade through OPEX morning, knowing why it's weird is the difference between being hit by it and trading around it.

There's a secondary effect. The SOQ is constructed from the first reported trade in each component. On a typical day, all 500 components open within a few seconds of 9:30. On a stressed day — heavy overnight news, large global moves, or a circuit-breaker scenario — components can stagger their opens over many minutes. The SOQ that results is a synthetic level that may differ measurably from any quoted SPX value at any given moment. Cash-settled options that reference the SOQ pay or receive cash based on that synthetic value, not on the post-open continuous SPX. Traders running expiration-day strategies who don't understand this can be surprised by a 30-cent or larger discrepancy between their expected and realized settlement.

### Cash settlement is a feature, not a bug

SPX, XSP, ES, MES, and VIX all settle in **cash**. SPY settles in **shares (physical)**. The difference is enormous for any strategy held to expiration.

**Cash settlement** means an in-the-money option simply credits or debits the cash difference between strike and settlement price. There is no exercise, no assignment, no shares delivered, no overnight gap risk between expiry and the next morning. You wake up Monday morning with cash exactly equal to the in-the-money amount (or no change if out of the money).

**Physical settlement** means an in-the-money short option results in shares changing hands at the strike. The direction depends on which side you wrote:

- **Short call assigned** — you must **deliver 100 shares per contract at strike**. Covered (you own the shares): the shares are sold at strike. Naked: you end up short the stock at strike basis, exposed to overnight upside.
- **Short put assigned** — you must **receive 100 shares per contract at strike** (i.e., buy at strike). Cash-secured (you have the collateral): your cash converts into stock at strike basis. Naked margin: long stock position consumes buying power.

Either way, you wake up to a position you didn't have when you went to sleep, marked at whatever price the market reopens at. The price gap between Friday's 4:00 PM mark and Monday's open is yours to absorb. For SPY this is typically small — a fraction of a percent on a normal weekend — but on event weekends or during stress, the Monday gap can be 3–5% or more. Anyone running SPY short puts who happens to have a strike near Friday's close is essentially long a weekend gap-risk option they didn't price into the trade.

**SOQ risk on cash-settled OPEX.** Cash-settled SPX/XSP/VIX options expire to the Special Opening Quotation (SOQ), a synthetic level built from the first reported trade of each constituent stock Friday morning. The SOQ can differ materially from Thursday's close due to overnight news and the staggered opening rotation. A short put expiring "safely OTM" Thursday at 4 PM can be ITM at Friday SOQ. **Cash-settled OPEX positions should be closed Thursday afternoon, not held into the SOQ.**

For individual stocks (which we'll touch on only briefly here — single-stock options are not the focus of this book), the gap risk is dramatically worse. Earnings releases, M&A announcements, or surprise news can produce 10–20% gaps. Anyone running short puts on individual names is structurally short jump risk, and the variance risk premium they collect may or may not be enough to compensate.

### The retail XSP advantage (revisited in 3C)

For any cash-secured systematic put-writing strategy, **XSP is the retail-correct choice**. You get the same SPX exposure, scaled to 1/10th the notional (so the position is sized appropriately in any retail account), with the same 1256 60/40 tax treatment as full SPX, with cash settlement (no Monday-gap risk), and with European-style exercise (no early assignment). Most retail traders use SPY puts because SPY is what they see — it's the most-quoted equity ETF, it's prominently displayed in brokerage apps, and many retail-targeted strategy videos use it as the example. This is operationally inferior on every dimension except spread width, where SPY is slightly tighter (typically $0.01-$0.02 on ATM SPY options vs $0.05-$0.10 on XSP).

The tax difference alone — covered in detail in 3C — is approximately 12-14 percentage points of after-tax return for a top-bracket US individual taxpayer. On a strategy that captures 8% annual returns, that's 100 basis points of after-tax return turned on or off by instrument choice. Over a decade of compounding on a substantial account, that gap is a small house.

### Trading hours and the "ES tells you SPX" mechanism

Cash SPX trades only during US regular-session hours (9:30 AM to 4:00 PM ET). The futures (ES, MES) trade nearly 24 hours, from Sunday 6:00 PM ET through Friday 5:00 PM ET, with a brief daily maintenance window. SPX options have extended hours on Cboe from 8:15 PM ET the previous evening through 9:15 AM ET — but the cash SPX *index* doesn't exist outside of US RTH.

When you see "S&P futures up 0.4% overnight" in financial media, that is ES — the cash SPX index simply doesn't exist between 4:00 PM and 9:30 AM. The opening print of SPX at 9:30 AM is constructed from the actual stock opens of all 500 components, which is why it sometimes prints away from where futures were trading thirty seconds earlier. Smart traders watch ES overnight to anticipate where SPX will open; the basis between ES and SPX during overnight hours encodes the market's evolving consensus.

There's a structural arbitrage that keeps the two locked together during US hours: if ES trades meaningfully above SPX (adjusted for financing and dividends), arbitrageurs short ES and buy a basket of SPX components. If ES trades meaningfully below SPX, they do the reverse. This arbitrage runs continuously during US hours and keeps the ES-SPX basis tight. During overnight hours, the basis can drift because no one can directly arbitrage against the cash SPX (which doesn't exist), and so the basis becomes a forward-looking estimate.

### Why this matters for everything that follows

Section 6 onward will describe dealer hedging in detail. The dealer who has sold an SPX option needs to hedge their resulting delta exposure. They typically do this in **ES futures** rather than in cash SPX or SPY, for three reasons: (1) ES has tighter spreads at institutional size than SPY; (2) ES trades nearly 24 hours, while cash SPX doesn't, so overnight risk can be hedged; (3) ES margining is more capital-efficient under SPAN than SPY shares under Reg-T.

When you read in Section 6 that "the dealer buys shares to hedge their short call," the literal-share interpretation is wrong. The dealer is buying ES futures contracts in size, with cash-share hedging used only at the margin to flatten remaining basis. The flow shows up in the SPX cash market only indirectly, through the arbitrage that links the two. This matters operationally because the highest-frequency intraday momentum effects from dealer hedging (Section 6D) show up most clearly in *ES* prints, not in SPY prints — though the two are correlated enough that SPY shows them too, slightly delayed.

---

## 3B · Where your order goes: exchanges, wholesalers, and the NBBO

Most retail traders see "buy" and "sell" as primitive actions. They are not. Between your click and the actual counterparty there is a routing decision that determines who fills you, at what price, and on what venue. Understanding the routing layer is the difference between believing "the market" took the other side of your trade and knowing that a *specific wholesaler* with a specific business model did.

### The NBBO — the rule everyone is supposedly following

Since the SEC's adoption of **Regulation NMS in 2005**, US equities and single-name options have been required to execute at or better than the **National Best Bid and Offer (NBBO)** — the highest bid and the lowest offer across all registered exchanges and dark pools at the moment of execution. The NBBO is computed continuously by the **Securities Information Processor (SIP)** — a regulated infrastructure that aggregates quotes from every venue and publishes a consolidated tape.

When you submit a market order, your broker must route it to a venue that can fill you at or inside the SIP NBBO at that microsecond. This sounds like a hard constraint. In practice, it's a soft one, and the reality of execution is more interesting than the regulation suggests.

### Lit exchanges, dark pools, and the wholesaler bypass

US equity orders can be routed to three types of venues:

**Lit exchanges** display their order books publicly. As of 2025 there are 16 registered US equity exchanges, the major ones being NYSE, Nasdaq, Cboe BZX, Cboe BYX, Cboe EDGX, Cboe EDGA, IEX (the "speed-bump" exchange), MEMX, MIAX Pearl, NYSE Arca, NYSE American, and several others. Each one has its own fee schedule, latency profile, and order-type matrix. Institutional orders typically route across multiple lit exchanges to minimize impact.

**Dark pools** — formally called Alternative Trading Systems (ATSs) — are non-displayed order books run by banks and brokers. UBS ATS, Goldman Sigma X, JP Morgan JPM-X, Credit Suisse CrossFinder, Barclays LX, Liquidnet, and many others. Orders rest in dark pools without being publicly displayed; they fill against incoming orders at the prevailing NBBO mid or at negotiated price improvement levels. Dark pools handle roughly 12-15% of US equity volume on a typical day; on stress days the share can rise as institutional sell flow seeks anonymity.

**Wholesalers** are off-exchange principal liquidity providers — firms that pay broker-dealers for the right to internalize retail order flow against their own principal books, rather than route the orders to exchanges. The current US wholesaler hierarchy in retail equities (as of late 2025/early 2026 data):

- **Citadel Securities** — approximately 35% of all US-listed retail equities and options volume, ~25% of total equities trading across all customer types
- **Virtu Financial** — approximately 15-20%, the historical second place
- **Hudson River Trading** — approximately 20% of US cash equities (institutional + retail), launched in retail wholesaling in 2022
- **Jane Street** — approximately 10% of US cash equities, dominant in ETF and institutional, launched retail wholesaling in 2019
- **G1 Execution Services (Susquehanna)** — smaller share, dominant historically in options
- **Wolverine Trading, IMC, DRW, Optiver** — institutional and option-specific franchises

The numbers shift by product. Citadel Securities is overwhelmingly dominant in retail equities. Jane Street has emerged as the dominant ETF market-maker. Susquehanna and Wolverine retain large institutional options franchises. The concentration in retail flow has *increased* since 2020 despite the entry of HRT and Jane Street — the franchise economics favor scale.

For US-listed options specifically, the wholesaler share is even higher than for equities. Citadel Securities, Susquehanna, and Wolverine together execute roughly 85% of retail options order flow. Most retail options orders never touch a public order book.

> *"As the leading U.S. retail market maker, executing roughly 35% of all U.S.-listed retail volume, Citadel Securities has a unique vantage point into retail investor behavior and the forces shaping market impact."*
> — Citadel Securities Equity Pulse, January 2026

Jane Street disclosed record-shattering revenue figures of $20.5 billion in 2024 and $39.6 billion in 2025 from its market-making operations — the rough size of those numbers tells you how thick the layer of intermediation is between you and any retail counterparty with an actual directional view.

### Payment for order flow, demystified

**Payment for order flow (PFOF)** is the payment a wholesaler sends back to the broker for the right to fill that broker's order flow. The wholesaler earns the bid-ask spread on the trade (plus any price-improvement premium they choose to offer); they share a small portion with the broker as a per-contract or per-share kickback.

For US-listed equities, PFOF runs in the range of $0.001 to $0.003 per share — roughly 0.1 to 0.3 basis points on a $100 stock. Small. For US-listed options, PFOF is much larger relative to position size: $0.40 to $0.65 per contract per side for retail SPY/QQQ options. On a 1-contract retail SPY options trade, the broker is paid roughly $0.50 to internalize it through a wholesaler; the wholesaler earns multiple dollars of edge on the trade as compensation for taking the position and the resulting hedge obligation.

PFOF is controversial because the broker's incentive is to route to the highest-paying venue, which is not necessarily the venue with the best execution. The historical academic debate has been whether retail execution under PFOF is genuinely worse than execution on lit exchanges, after accounting for the price improvement that wholesalers do typically provide. The empirical evidence is mixed and depends on the metric used.

In December 2022, the SEC under then-Chair Gary Gensler proposed **Rule 615** (the "Order Competition Rule"), which would have required certain retail marketable equity orders that were going to be internalized to instead be exposed to a public auction to potentially capture price improvement competitively. The rule was passed by the Commission 3-2 in proposal but never finalized.

**Rule 615 was formally withdrawn on June 17, 2025** by the SEC under the new administration, along with twelve other Gensler-era proposed rules. This is the current state of the regulation. PFOF remains legal in the US. The UK and EU regulators have banned PFOF outright. The US allows it with disclosure requirements (Rule 605/606 reports) but no structural intervention against the wholesaler-internalization business model.

> *"Without accurately assessing current retail execution quality (including reviewing execution quality reports from retail broker-dealers), the Commission can't conclude that fundamental changes to retail order execution practices are warranted, as contemplated by the 'Best Execution' and 'Order Competition' proposals."*
> — Citadel Securities, public comment letter on Rule 615 (2023)

For the foreseeable future, the wholesaler model is the operational reality of US retail trading.

### Reg NMS 605 and 606 — the only public lens on retail execution quality

> **Rule 605** (since 2001, amended substantially in 2024): each market center — exchange, ATS, wholesaler internalizer — must publish monthly reports on execution quality at the *order-type level*. Mandatory metrics include the realized-spread, the effective-spread, the price-improvement rate, the average response time, and (post-2024) breakdowns by order size and time-of-day buckets. Reports are downloadable as plain-text from each market center's website.
>
> **Rule 606** (since 2001, amended in 2018 and 2020): each broker-dealer must publish quarterly reports on *where* it routed retail and institutional non-directed orders, with the proportions of total flow sent to each market center. Post-2018, the report also includes the dollar amount of payment-for-order-flow received from each routing venue, broken down by S&P-500 vs non-S&P, market vs marketable-limit, and other categories.
>
> **What's in the reports — and what isn't.** The 605 reports show *averages* of execution quality: e.g., "Citadel Securities provided $0.0017 per share of price improvement on average for SPY market orders sized 100-499 shares in October." This is informative but coarse. Two important things the reports do *not* show: (1) *order-level* execution quality (you can't reconstruct your own trades), and (2) any breakdown of how price improvement was *distributed* across orders (a wholesaler can boost the average by improving large favorable trades while leaving small marginal trades at NBBO). For options, the equivalent disclosures are weaker still; the 605 framework was originally NMS-stock-focused, and option-specific reporting standards are evolving.
>
> **Operational use.** A retail trader who wants to compare brokers should look at *Rule 606 reports* (where does my broker send my orders?) and the *Rule 605 reports* of the venues those orders are sent to (what execution quality do those venues deliver, on average?). The combination gives a defensible apples-to-apples comparison across brokers; it is the single most underused public dataset in retail execution analysis. Most retail traders have never opened either report. Both are public.

### The wholesaler's math, the dealer's math, the franchise

Citadel Securities, Susquehanna International Group, and Wolverine are not just options market makers. They are also the dominant retail equity wholesalers. The same firm that takes the other side of your SPY put option also takes the other side of your SPY share purchase. The two desks share infrastructure, capital, and inventory; they hedge across each other. When Citadel sells you a SPY put, the SPY shares they buy as the hedge may come from another piece of internal Citadel flow, crossing the book entirely without touching a lit exchange.

This is the "internalization" model in its full form. Retail buy-side flow and retail sell-side flow are netted against each other inside the wholesaler's book. Only the residual — the net of all retail buys against retail sells — actually needs to be hedged in the external market. Because retail flow is roughly balanced on most days (slightly more buying than selling on average, but the imbalance is small), the gross flow seen by the wholesaler is far larger than the net hedging flow they actually generate.

For SPX, XSP, and other index options, the routing is simpler: these only trade on Cboe, and most retail brokers route them directly to the Cboe order book. **There is no wholesaler bypass for SPX**. This is one of several reasons SPX/XSP spreads are somewhat wider than SPY: the wholesaler price-improvement machinery doesn't apply.

It is also one of the reasons that GEX models computed from SPY open interest can be misleading (a point we'll develop in detail in Section 8A): SPY OI represents gross open interest, but the actual hedge flow generated by SPY options is much smaller than that gross because wholesalers internalize so much of it. SPX OI, by contrast, represents flow that all sits on the Cboe book — wholesalers cannot internalize it because they are not the counterparty — and so the dealer hedging implications of SPX OI are larger per unit of OI than the same OI in SPY.

### FLEX options: the institutional sidewalk

A growing share of institutional options trading happens through **FLEX options** — exchange-listed contracts with customizable strikes, expirations, and exercise styles, traded primarily on Cboe. FLEX volumes have exploded in recent years:

- 2012: ~12 million total FLEX contracts traded annually
- 2019: ~125,000 contracts per day; total open interest 2 million
- 2024: ~200 million FLEX contracts traded annually
- 2025: average daily volume of **1.3-1.4 million contracts/day**, +65% YoY
- 2025 breakdown: single-stock FLEX ~958k/day, ETF FLEX ~301k/day, index FLEX ~29k/day
- 2025 open interest: 35 million contracts (17.5× the 2019 level)

FLEX growth has tracked institutional demand for tailored hedges. A pension fund that wants a put struck exactly at its actuarial liability level, not at the nearest 25-point grid; an autocallable issuer that needs to hedge a knock-in level at a specific spot price; a structured-product desk that needs a non-standard expiration to match an internal liability schedule — all of them use FLEX. The dealer on the other side of a FLEX position hedges it alongside their listed book, and the resulting hedge flows show up in the lit markets without any FLEX identifier on the trade tape.

This matters for GEX modeling: FLEX positions are visible to Cboe (which records the trades) but not to the public OPRA feed in a way that makes them attributable to specific strikes for GEX computation. The major published GEX models (SqueezeMetrics, SpotGamma, Tier1Alpha) all see FLEX volume in aggregate but cannot decompose it cleanly by strike. The result: published GEX models systematically *under*-count the gamma exposure dealers actually have. This effect is small on a typical day and large during stress episodes when FLEX-based hedging activity spikes. Section 8A returns to this in detail.

### Order types and what each one does

Five order types cover 95% of retail decisions. Knowing what each one promises (and what it doesn't) is one of the cheapest sources of slippage reduction available.

**Market.** Buy at the best available offer / sell at the best available bid. Crosses the spread immediately. No price guarantee — you fill at whatever price is available. In thin markets or at the open, can fill far from the NBBO.

**Limit.** Buy at or below your stated price / sell at or above. No fill guarantee. Sits passive on the book until matched or canceled.

**Marketable limit.** A limit order set at or through the NBBO. Behaves like a market order with a price ceiling. The recommended retail default for size — gets you a fill in normal conditions while capping slippage in stress.

**IOC (Immediate-or-Cancel).** Fill what you can at the limit price, cancel the rest. Useful for taking liquidity off the book without leaving a resting order behind.

**MOC (Market-on-Close).** Execute at the official closing print. The 4:00 PM print is determined by a closing auction. MOC orders are guaranteed to fill at the close, but the close price itself is set by the auction imbalance.

The recommended discipline: **use marketable limits as the default**. They get you filled in normal conditions, and they protect you from blow-up fills in stress. Save market orders for tiny orders in highly liquid names where slippage is bound to be negligible.

### The closing auction (revisited)

Between 3:50 PM and 4:00 PM ET, US equity exchanges enter their closing auction process. Imbalances are published every few seconds starting around 3:50 — "12 million shares to buy at SPY at the close" — so that liquidity providers know to step in if they want to take the other side. The final 10 seconds set the official close, which is the print used by MOC orders, by ETF NAV computations, by most index benchmarks, and by S&P's official daily index level.

The closing auction has grown structurally larger over the past decade as passive index funds have grown:

- 2010: ~5-7% of NYSE volume in the closing auction
- 2020: ~10-12%
- 2025: estimates ranging from 12% to 18% of total NYSE consolidated tape volume on typical days, higher on rebalance dates

For index ETFs specifically (SPY, QQQ, IWM), the share is higher — closer to 20-25% — because passive index funds rebalance to the close. NYSE's own reporting through 2024 documented that closing auctions had reached new highs both in absolute daily traded shares and notional, and in their share of consolidated US equity volume.

The microstructure consequence is that the last 30 minutes of the trading day are dominated by mechanical, non-fundamental order flow. This is where dealer hedging concentrates, where index funds rebalance, where pension funds size positions to specific weights, and where vol-targeting strategies execute their daily risk adjustments. The Baltussen-Da-Lammers-Martens paper on intraday momentum we'll discuss in Section 6D is partly about this: the last 30 minutes systematically displays different statistical properties than the rest of the day because the *composition of order flow* is different.

For retail traders, the implication is operational: avoid placing market orders in the last 15 minutes of the trading day unless you've thought through what's happening in the auction. The spreads can widen, the price can swing on imbalance updates, and the close-print itself may be substantially different from the level you saw 30 seconds before 4:00.

### What this means for dealers

Dealer hedging — the subject of every subsequent chapter — is executed primarily in two places: **lit-exchange spot SPY/SPX shares for delta hedges**, and **CME ES futures for larger or more cost-sensitive hedges**. The wholesaler ecosystem we've described is one piece; the dealer hedging ecosystem on top of it is another. The Baltussen et al. (2021) finding that the last 30 minutes of trading concentrates intraday momentum is partly mechanical: dealers' end-of-day rebalancing flows through the auction, where it interacts with mandatory index-fund rebalancing and the day's accumulated charm/vanna decay from the options book. The auction is where the day's options-related hedge obligations get settled into the underlying.

One subtle implication of the wholesaler concentration: SPY options flow is largely internalized, meaning the wholesaler sees both retail buys and retail sells and crosses them internally. The actual "dealer delta hedge" they need is smaller than the gross retail flow would suggest. SPX options flow, by contrast, all hits the Cboe order book — the institutional dealer there has to hedge the full *gross* position, not the net. This is one reason why "SPX dealer gamma" and "SPY dealer gamma" are not literally the same concept, and why SqueezeMetrics-style GEX calculations on SPY tend to overestimate the actual hedge flow.

---

## 3C · Account types, margin, and the 1256 advantage

Two strategies with identical pre-tax P&L can produce wildly different *after-tax* outcomes depending on the wrapper, the account type, and whether the underlying instrument qualifies for **Section 1256** treatment under US tax law. This is one of the genuinely free lunches available to US retail traders, and most retail strategies fail to capture it because they default to the most-familiar instrument (SPY) instead of the tax-optimal one (XSP, ES, or SPX).

### The four account tiers

US brokerage accounts come in four primary capacity tiers, each with different rules about what can be traded and how much leverage is available. Capacity escalates upward; you cannot trade naked short calls in a cash account, but you can do everything a cash account permits in a portfolio-margin account.

**Cash account.** Settled funds only. No borrowing. No naked short options. Cash-secured puts, covered calls, long options, and long stock all permitted. The default retail tier. Equities settle T+1 as of May 2024 (the SEC moved the standard from T+2 to T+1); options settle T+1 also. The cash account is structurally safe because you cannot lose more than you have — there is no margin extension to draw down, no margin call, no forced liquidation. The price is capital inefficiency: cash-secured strategies tie up dollar-for-dollar against potential assignment.

**Reg-T margin account.** Fixed-percentage margin rules under Federal Reserve Regulation T. 50% initial margin on stock purchases, 25% maintenance. Options buying power generally limited. Pattern Day Trader rules apply for active accounts under $25,000 — accounts with fewer than $25k equity that execute four or more "day trades" in a five-trading-day rolling window get flagged and restricted. Most retail accounts with $2,000+ equity qualify for Reg-T margin. The naked short option permission level requires specific approval and demonstrated experience.

**Portfolio Margin account.** Stress-tested theoretical-loss margin. Requires $125,000+ equity (FINRA minimum) and broker approval. Margin requirements are computed against a ±15% SPX stress scenario plus implied volatility shifts; for diversified, well-hedged books the requirement is dramatically lower than Reg-T. For an iron condor on SPX with both wings 5% out-of-the-money, Reg-T might require collateral equal to the full wing width; portfolio margin might require only the loss that would occur in a ±15% scenario — perhaps 1/3 the Reg-T number. **The catch**: PM requirements expand non-linearly in stress, sometimes doubling or tripling overnight as house overlays kick in. This is a critical feature, not a bug — covered below.

**Futures / 1256 account.** Separately permissioned for futures (ES, MES, ZN, CL, etc.) and futures options. Futures use **SPAN-based margin** (developed by the CME), which is typically 5–8% of notional for major equity futures and is computed against a stress-scenario matrix. Both gain and loss receive 1256 60/40 tax treatment regardless of holding period. ES at SPX 6,000 has notional $300,000; initial margin is around $15,000-$22,000 depending on conditions, intraday margin can be lower. This is genuinely powerful leverage with clean tax treatment.

### Section 1256 — the 60/40 rule

Under Internal Revenue Code Section 1256, certain financial contracts receive a uniquely favorable tax treatment that applies *regardless of holding period*:

```
1256 split: 60% long-term capital gains + 40% short-term capital gains
```

For a US individual taxpayer in the top federal bracket (37% ordinary income, 23.8% long-term capital gains including the 3.8% Net Investment Income Tax), the blended rate on 1256 gains works out to approximately **27-28%**, versus approximately **40-41%** on ordinary short-term capital gains for instruments not in the 1256 regime.

That is roughly **12-14 percentage points of after-tax savings** applied to every dollar of P&L generated by 1256 instruments. For a systematic monthly put-write strategy earning 8% annual gross, that's approximately 100 basis points of after-tax return turned on or off by instrument choice. Over a decade of compounding, the gap is substantial: 100 bps × 10 years = roughly 10% more terminal wealth, before accounting for the compounding of the saved taxes themselves (which adds another few percent).

**1256-qualified instruments include:**
- Cash-settled broad-based index options (SPX, XSP, NDX, RUT, VIX, NDXP)
- Regulated futures contracts (ES, MES, ZN, ZB, CL, ZC, GC, all CME/CBOT/NYMEX/COMEX equity, rate, and commodity futures)
- Options on regulated futures contracts (ES options, MES options, etc.)
- Broad-based index options on Cboe (the operative legal definition is in IRC §1256(g)(3))
- Non-equity options that meet the "broad-based" test

**1256 does NOT cover:**
- ETF options (SPY, QQQ, IWM, etc. — these are *equity* options, not index options, even though they track indices)
- Single-name stock options
- Narrow-based index options (some sector ETFs, individual industry indices)
- Stocks themselves (standard short/long-term capital gains rules apply)

The "broad-based" test for index options requires (loosely) that the underlying index include 10+ component securities and that no single component exceed 30% of the index weight. SPX clearly qualifies; sector ETF options like XLE or XLF do not.

### SPY vs XSP: the one decision that matters

This is the single highest-leverage operational choice in retail systematic options strategies, and it costs nothing to make. A retail trader running monthly cash-secured ATM puts on SPY vs XSP will see identical pre-tax P&L (modulo a few basis points of spread). After tax, in the top bracket, **XSP delivers roughly 10% more after-tax return on the same gross premium captured** over a multi-year horizon. The only operational price is XSP's slightly wider bid-ask spreads, which cost perhaps 5-10 bps annualized — easily outweighed by the tax saving.

Concretely, suppose you sell ten SPY ATM monthly puts at a strike where each contract collects $300 in premium, for $3,000 gross premium. The contract notionals are equal to ten XSP contracts. Hold the strategy for a year, collecting twelve months of premium, win 9 of 12 months and lose 3:

- Gross premium collected: ~$36,000
- Expected losses on losing months: ~$15,000
- Net pre-tax P&L: ~$21,000

If you ran this with SPY in a Reg-T account at the top bracket:
- All gains and losses are short-term capital gains/losses (held less than 1 year)
- Effective tax rate: ~40-41%
- After-tax P&L: ~$12,400

If you ran the equivalent with XSP under 1256:
- 60/40 blended treatment regardless of holding period
- Effective tax rate: ~27-28%
- After-tax P&L: ~$15,200

The XSP version delivers approximately **$2,800 more after-tax** on the same pre-tax P&L. Over a decade of compounding, this gap is a small house, and the only operational change required is opening the XSP order ticket instead of the SPY one.

### Wash sale rules and tax efficiency

The IRS wash-sale rule disallows a loss on a security if a "substantially identical" security is purchased within 30 days before or after the loss-realizing trade. For stocks and most ETFs, this rule is easy to trigger accidentally — selling SPY for a loss and buying it back two weeks later disallows the loss, deferring it into the cost basis of the new position.

**For 1256 instruments, wash-sale rules do not apply.** Losses can be realized and immediately re-established without disallowance. This matters substantially for any strategy with frequent roll activity or that legitimately needs to harvest losses against gains for tax planning. A trader running monthly XSP credit spreads who has a losing month can close the position, realize the loss for tax purposes, and immediately re-enter a similar position — and the loss is fully usable against any other gains in the same year.

The wash-sale exemption for 1256 contracts is buried in the IRC and rarely discussed in retail education, but it interacts with the mark-to-market provision of §1256 (which requires you to mark all open 1256 positions to market at year-end and treat any gain/loss as recognized) to produce a clean tax accounting where every gain and every loss flows through to ordinary tax computation in the year it occurred, with no carryforward complexity from disallowed losses.

[INTERACTIVE: tax-drag-comparison]

### Margin behavior in stress (the real cost of Portfolio Margin)

Reg-T margin requirements are fixed and formulaic: 50% on stock, fixed formulas on options. They don't change in stress. Your margin requirement is the same on Monday as it was on Friday, regardless of overnight news.

Portfolio Margin requirements, by contrast, are **stress-tested**: the broker computes what your portfolio would lose under a ±15% SPX scenario combined with implied-volatility shocks, and requires you to post collateral against that theoretical loss. In calm conditions, PM allows far more leverage than Reg-T — diversified, hedged portfolios can run at 5–10× the leverage that Reg-T would permit. **In stress, PM requirements expand violently.**

The canonical worked example is March 2020. In the first three weeks of the COVID drawdown:

- February 21, 2020: SPX 3338, VIX 17
- March 16, 2020: SPX 2386 (intraday low ~2280), VIX 82.69

In the same period:

- Many PM accounts saw their margin requirements **double or triple** in 1-3 days as brokers increased their house-overlay add-ons
- The underlying ±15% scenario itself got adjusted upward by brokers (some moved to ±20% or ±25%) as the realized volatility regime shifted
- Implied-volatility shock components in the stress test grew larger as VIX rose
- Vol-targeting funds began de-grossing, which fed back into the PM margin calculations as VIX rose further

The combination produced a wave of forced liquidations across PM accounts. Traders who had been running at "comfortable" pre-stress leverage — say, 4× — found themselves looking at 8× or 10× requirements after the margin expansion, with no time to raise additional collateral. The broker's algorithm sells positions to bring the account back into compliance with the new margin level. The selling adds to the SPX downside, which raises VIX further, which further expands margin requirements at *other* PM accounts. The feedback loop is exactly the same in structure as the dealer-hedging feedback loop we'll describe in Section 8B, just operating through margin accounting instead of options Greeks.

The structural lesson: cash-secured strategies cannot be force-liquidated for margin reasons because there is no margin extension to expand. This is the operational reason cash-secured XSP put-writes are the recommended retail VRP harvest vehicle even though they are capital-inefficient compared to PM-leveraged versions. The capital inefficiency is the *insurance premium* against the path-dependent risk of margin expansion in stress. Portfolio margin is genuinely useful in calm conditions; it is genuinely dangerous in stress, and the danger is precisely the moments when you most want your account to survive intact.

### The five-product, three-account decision tree

**Cash account:** XSP cash-secured puts (capital-bound but operationally safest). Avoid SPY for any systematic strategy — the tax penalty is large and unnecessary.

**Reg-T:** SPY/XSP diagonal or vertical spreads if you need defined-risk leverage; ES futures via the 1256 path if you want clean leveraged equity exposure. The Reg-T tier is a good middle ground for traders who have outgrown cash accounts but aren't ready for the margin-expansion risk of portfolio margin.

**Portfolio Margin:** Sized XSP strangles or condors against a known stress budget, with **explicit pre-committed kill criteria for margin expansion scenarios**. Don't touch PM until you have at least 12 months of cash-account or Reg-T experience with the strategy and documented adherence to your written kill rules. The first PM account every trader opens is operated incorrectly; the second one is operated more carefully because the first one taught lessons that no amount of reading could have.

The choice between cash, Reg-T, and PM is one of the most consequential a retail trader makes, and most retail traders make it badly — by jumping to PM too early, by failing to write down stress-scenario kill rules, and by not understanding that PM margin requirements are *path-dependent* in a way that Reg-T's are not.

---

## 3D · Order book mechanics (equity execution side)

Section 2D introduced the order book to support the quant-trading strategy taxonomy. This section is the same mechanism viewed from the cash-equity execution side — what happens between your click and your fill, and why SPY orders go through a different routing path than SPX orders.

### The book's anatomy

Every liquid security has two queues of resting orders: **bids** (buyers willing to take at price X) and **asks** (sellers willing to give at price Y). The highest bid and lowest ask form the National Best Bid and Offer (NBBO) — the regulated reference price for US equities under Reg NMS. Behind them sit deeper levels with worse prices but more quantity available.

For SPY on a typical day, the top of the book is millions of shares deep — bids and asks at the NBBO might each carry 500,000 to 2 million share-equivalents of resting orders across all venues. Behind them, levels 1 cent away in each direction carry similar size. The book is unusually thick relative to most stocks because SPY is the most-traded ETF in the world.

For SPX index options, the book is much thinner per strike because each strike has its own order book and there are thousands of strikes across hundreds of expiries. ATM 0DTE strikes on a typical day might have 500-2,000 contracts at the NBBO; deep OTM strikes might have 5-50 contracts. The spreads are wider in absolute dollar terms (often $0.10 to $0.50 on liquid SPX strikes, vs $0.01-$0.02 on SPY) but the per-contract notional is also 10× larger, so the *percentage* spread is comparable.

### Where retail SPY orders actually go

For US equity options and shares, retail orders predominantly do not touch a public exchange book directly. They are routed to a wholesaler — Citadel Securities, Susquehanna, Virtu, Wolverine, Jane Street, Hudson River Trading — who fills the order from their own principal book. The wholesaler returns a small fraction of the captured spread to the broker as Payment for Order Flow (PFOF). For SPX and XSP (index options), there is no wholesaler bypass; orders route directly to the Cboe order book.

Two consequences flow from this routing structure. First, SPY/QQQ retail flow is largely internalized — the "GEX" computed from public OI on these names double-counts what wholesalers cross internally. Second, SPX/XSP flow hits a single transparent book — which is one of several reasons the dealer-mechanics chapters that follow specifically use SPX as their laboratory rather than SPY.

### Slippage and market impact

Section 2D's discussion of the square-root law of market impact applies directly here. The same effect on a small retail buy is usually negligible — SPY's top of book is many millions of shares deep, so a 100-share retail order has zero market impact. For institutional flow that needs to move millions at a time, slippage and market impact are the dominant execution costs, and they're why iceberg orders, VWAP execution algorithms, and dark pools exist. This is also why dealer hedging flow (Section 6 onward) uses ES futures rather than spot SPY: the futures book is the most capital-efficient place to absorb large hedging size with minimal market impact.

### The retail order types that actually matter

For day-to-day retail use, three order types cover 90% of decisions:

**Market order.** Guaranteed fill, no price control. Use only for tiny orders in highly liquid names.

**Limit order.** Price control, no fill guarantee. Use when price matters more than execution certainty.

**Marketable limit.** Limit set at the NBBO. Behaves like a market order in normal conditions but caps slippage in stress. **The retail default for any order of meaningful size.**

The discipline is simple and underappreciated: a marketable limit set at the offer is essentially identical to a market order on normal days, but it protects you from the kind of fat-finger blowup that occurs when an order arrives during a quote dropout, during a fast market, or during a circuit-breaker scenario. The cost of using marketable limits as the default is approximately zero. The benefit is that on the day when something genuinely goes wrong with the quote infrastructure, you don't fill 200 points away from the NBBO. **Always use marketable limits.**

### The 24/5 trading regime

A relatively recent development: as of late 2025 and early 2026, several US brokers (Robinhood, Schwab, Interactive Brokers, etc.) have launched **24/5 equity trading** — extended hours operations that allow trades in major equities (including SPY, QQQ) outside the traditional 9:30-4:00 US session, through partnerships with Blue Ocean ATS and similar overnight venues.

Liquidity in 24/5 sessions is thin compared to RTH. Spreads are wider, often by 5-20× the RTH spread. The Citadel Securities-disclosed data suggests post-market session activity is rising structurally — currently accounting for ~2% of notional and ~6% of shares traded for retail — but it remains a small fraction of total volume. For most retail strategies, 24/5 trading is not yet operationally relevant. For traders who need to respond to overnight news, it provides a path to execute that didn't exist in 2020.

The structural risk: a market order placed during 24/5 hours can fill at prices far from where the underlying will open during RTH. The bid-ask is wider, the depth is thinner, and the participants on the other side are different (often professional liquidity providers willing to quote only at unfavorable prices to retail). Use limit orders only during extended hours. Better, generally: don't trade during extended hours unless you have a specific reason.

---

## 3E · Execution as negative alpha

A strategy with a positive paper Sharpe and unsurprising mechanics can still be a net loser in a retail account. The reason is rarely the model — it's the **gap between the price you saw and the price you got**. Across the four-layer haircut framework introduced in 12A, execution friction (layer 3) typically destroys 20-30% of paper Sharpe even before behavior is considered. For multi-leg options strategies in single-name underlyings, the destruction can exceed 50%.

This section consolidates the practical rules. The mathematics is simple; the discipline is hard.

### The bid-ask trap, in numbers

Open any options chain on a single-name stock. The "last" price you see is irrelevant — it's the price of the last trade, which may have been seconds or hours ago, at whatever spread happened to exist then. The actionable prices are the **bid** (what you can sell at right now) and the **ask** (what you can buy at right now). Between them is the **spread**, and the spread is where edges go to die.

For SPX index options, typical bid-ask spreads run $0.10-$0.30 on ATM strikes during regular hours, widening to $0.50-$1.00 on wing strikes. For SPY, $0.01-$0.03 ATM. For NVDA or AAPL options at typical strikes, $0.05-$0.15 ATM. For a thinly-traded single-name option three weeks out at a 30-delta strike, you might see $0.50-$1.50 spreads on a $5 premium — **10-30% of the premium itself**.

A VRP-harvest strategy that collects 80 bps of annual edge over realized variance gets erased by a single 30% round-trip spread. The math: harvest $0.30 of edge per spread, give $0.40 to execution per trade across entry and exit. Net: lose money holding a "winning" strategy.

This is not hypothetical. It is the single most common reason retail options strategies underperform their backtests.

### The five rules of options execution

**Rule 1 — The bid-ask midpoint is the only fair reference price.** Compute mid = (bid + ask) / 2 at the moment of decision. Any limit order you place gets compared to this mid. "Selling at the mid" means an order at mid; "selling at $0.05 better than mid" means an order at mid + $0.05. Last price is decorative. Theoretical price (from vendor models) is informational, not actionable.

**Rule 2 — Marketable limits, not market orders.** A market order on a thin option chain at 9:32 AM can fill 30% above the prevailing mid in stress. Always use a limit. The limit can be aggressive (at the ask for a fast fill, or one penny inside it) but it must exist. The only exception is in clear emergencies — and a planned exit is never an emergency.

**Rule 3 — Multi-leg orders go in as multi-leg spreads, not legged manually.** When you place a vertical spread as two separate orders ("leg in" by selling one side, then buying the other), you take execution risk on the timing gap between fills. Even a 5-second gap during a fast tape can cost 5-15% of the spread credit. Use your broker's multi-leg ticket and price the spread as a single net debit/credit. The broker's market makers will fill or not — but you don't take legging risk.

**Rule 4 — Avoid the open, the close, and the lunch hour unless trading those windows is part of your strategy.** The first 15 minutes after the open feature the widest spreads of the day as overnight charm and vanna unwinds clear. The last 30 minutes feature mechanical rebalancing that creates price pressure unrelated to your thesis. The middle of the lunch hour (roughly 12:00-1:00 PM ET) often features thin liquidity. **The cleanest execution window is generally 10:30 AM to 11:30 AM ET and 1:30 PM to 2:30 PM ET.**

**Rule 5 — Estimate slippage before entering, not after.** For every trade, before clicking, compute: "If I have to exit at the bid (or buy at the ask), what does that do to my expected profit?" If exiting at the unfavorable side costs more than 25% of your expected profit, the trade is execution-marginal. Either improve execution (tighter strikes, more liquid expirations) or skip.

[INTERACTIVE: slippage-cost-calculator]

### Instrument selection as execution decision

**SPX vs SPY vs XSP.** All three reference the same underlying but have different execution characteristics:

- **SPX**: tightest bid-ask spreads on liquid strikes; 1256 tax treatment; cash-settled (no assignment risk); largest contract size ($5,000 notional per point at SPX 5,000). Best for size; worst for small accounts.
- **XSP**: identical structure to SPX at 1/10 the contract size; 1256 tax treatment; cash-settled. Spreads sometimes wider proportionally than SPX. **Best instrument for most retail swing-options traders.**
- **SPY**: highest liquidity in raw volume; tightest absolute spreads in dollars; 1099 tax treatment; American-style (early-assignment risk on ITM short legs near ex-div). Best for share-level execution; tax-disadvantaged for short-term trading.

For a retail trader running a Trend Pullback or Compression Breakout setup, **XSP is the default choice**. The marginal spread cost vs SPX is paid back many times over in tax efficiency, and the smaller contract size permits cleaner position sizing.

**Single-name options.** Mag-7 names (NVDA, AAPL, GOOGL, MSFT, META, AMZN, TSLA) have institutional-grade options liquidity — bid-ask spreads of $0.05-$0.15 on near-dated ATM strikes. Below the top 50 names, spreads widen dramatically. A small-cap biotech option might have $1.00 spreads on $3.00 premiums — **untradeable for any strategy whose edge isn't measured in percentage of underlying move, not in IV mispricing**.

### When legging is acceptable

Despite Rule 3, there are two cases where leg-by-leg execution beats multi-leg orders:

1. **When the multi-leg order won't fill.** Some thinly-traded strikes have market makers who won't price the spread as a package but will price each leg individually. After 30 seconds with no fill on a midpoint multi-leg order, you can try legging — but accept that your edge has just degraded.

2. **When you're closing a position into rapid movement and want to capture one side quickly.** If your iron condor's short call has moved deep ITM and the put side is worthless, closing the call side first protects against further loss; the worthless put side can close whenever. This is "scratching the trade" — not optimal execution but valid risk management.

### The journal entry

The mark of execution discipline is the post-trade journal. For every trade, record:

- Mid at decision time (before clicking)
- Limit price submitted
- Fill price
- Spread width at decision time
- Time of day
- Volume in the contract that day

Over 50 trades, this dataset reveals your personal slippage profile. Most retail traders, asked to estimate their average slippage, guess 10-20% of spread. The journaled data routinely shows 40-60%. The difference is not skill — it's discipline. Recognizing the gap is the first step to closing it.

> *Execution is the only Greek not derived from Black-Scholes. It is the largest, the most controllable, and the one most retail traders ignore.*
