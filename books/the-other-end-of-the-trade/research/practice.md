# PRACTICE: how practitioners measure and display dealer positioning

Research file for the Part VIII rewrite of "The Other End of the Trade". Area: practice, the tools and methods practitioners use to estimate and draw dealer gamma (GEX) and vanna (VEX), with Skylit's Heatseeker as the worked example. Compiled 2026-09-29.

## How this file was built, and what to trust

- **No page was read directly.** WebFetch was refused by the egress proxy for every host tried: skylit.ai, docs.skylit.ai, squeezemetrics.com, spotgamma.com, cboe.com, vol.land, substack.com, netlify.app, scribd.com, sites.google.com, flashalpha.com and topwhops.com. Every vendor fact below comes from WebSearch result summaries, which quote or paraphrase the page. Text in quotation marks is the wording those summaries showed. It could not be checked against the live page and may carry light paraphrase by the search engine. Treat every quotation as "as shown in a search summary".
- **The session's shared WebSearch budget (200 calls) ran out** part way through this task. Topics I could not search at all are listed under "Gaps" at the end: the bank desks (Goldman Sachs, Nomura's McElligott, JPMorgan's Kolanovic), GEXBot, Barchart's method, Tier1Alpha's method, the price and delay of Cboe Open-Close and ISE data, and the origin of the phrase "window of weakness".
- **Academic sources** were confirmed with Consensus. Their numbers come from the abstracts Consensus showed.
- **Labels.** [vendor claim] means a vendor's statement about its own product. [third party] means a review or affiliate site, often paid by referral. [unverified] means no search result confirmed the detail. [derived here] means I computed it from standard option formulas; it is not a source's number.
- **Dates.** Vendor pages carry no dates in the summaries; "n.d." means undated, read via search on 2026-09-29.
- **After a container restart (2026-09-30).** A second pass kept everything above and added: the missing vendors and bank desks to Part B (Tier1Alpha, BarchartGEX, GEXBot, NomuraMcElligott, GoldmanFishman2020, JPMorganKolanovic2023, and entries for the Cboe notes the B1 table already cited); Parts C to F; entries for every academic key Parts A and B cite; and the synthesis. WebSearch worked again in this pass, so the topics the first bullet list names as unsearched (the bank desks, GEXBot, Barchart, Tier1 Alpha, Cboe Open-Close and ISE prices, "window of weakness") were searched; what is still missing is listed under "Gaps" at the end. Hosts refused in this pass as well: tier1alpha.com, threadreaderapp.com, barchart.com, docs.gexbot.com, heisenbergreport.com, finanz.dk, theocc.com, federalregister.gov, sec.gov, cdn.cboe.com, data.nasdaq.com, dev.to, diva-portal.org. One source was read directly: GEXBot's public API specification on GitHub (cloned, read, then deleted). Academic entries were confirmed with Consensus or WebSearch; their co-author names and page ranges are marked where the result did not show them.

---

## Part A. Skylit's Heatseeker in depth

### A1. What the heatmap plots

| Element | What Skylit says (quotations as shown in search summaries) | Source key |
|---|---|---|
| Rows | Strikes. "Rows are strikes, columns are expirations, and each cell is a node." | SkylitReading, SkylitModule |
| Columns | One per expiration: "Each column on the heatmap represents a different contract expiration, such as the current expiration, next week, two weeks out, or later periods." "The same strike can look different depending on the expiration selected. A major node several expirations out may not be a major node for the current expiration." | SkylitDocs |
| Cell value | A signed number per strike and expiry: "Each strike displays a value (positive or negative)." "Each node has a number attached to it, which reflects how strong the magnetic effect is. The higher the value of a node (regardless of + or -), the more powerful the pull/explosion is likely to be." | SkylitDocs |
| Units | Not stated on any page found. Skylit's own examples are in dollars ("$2 billion", "$200 million"). No page says whether a cell is dollars per 1% move, per point, or something else. | SkylitIntroGamma |
| Color | "positive exposure shown in green to yellow and negative exposure shown in blue to purple". "Bright Yellow (Pika) Nodes represent price areas where dealers are positioned in a way that absorbs price movement, while Dark Purple (Barney) Nodes indicate areas where dealer positioning amplifies price movement." | SkylitDocs |
| Exposure views | A GEX/VEX switch. "You can choose GEX for today's levels, or VEX for a multi-day view and days when volatility spikes." "Day traders use it for intraday levels, watching the same-day column on indexes and the nearest expiration on single names." VEX is used "for a view of roughly five days and out". | SkylitModule, SkylitVEX |
| Markers | "The King is the starred cell." "the strike nearest price highlighted". | SkylitModule |
| Filters | The sidecar filters: "the number of expirations shown, the number of nodes shown, the selected exposure type, and current versus expanded expiration views". | SkylitDocs |
| Updating | "maps dealer exposure at every strike and every expiration and updates live through the session". The module page claims "a one-second refresh with expiration-level heatmaps". The Discord bot "streams SPXW, SPY, QQQ, IWM, and VIX maps every 15 seconds" [third party, from the Whop listing]. | SkylitModule, SkylitReviews |
| Velocity | "clicking the lightning button and picking a timeframe from 1 min to 1 day"; an "Increasing and Decreasing filter" shows "only growing or only shrinking nodes". | SkylitModule |
| Alerts | "Right-click any node to get an alert as price approaches it or taps it, or to track how the node's size changes through the day." | SkylitModule |
| Modes | Swing Mode ("Full dealer exposure heatmap across strikes and expirations"), Trinity Mode (SPXW, SPY and QQQ side by side), Velocity Mode. | SkylitModule, SkylitTrinity |
| Coverage | Lower tiers: SPX(W), SPY, QQQ, IWM, VIX. Pro: "300+", "3,500+" or "5,000+" tickers, depending on the page. The counts disagree. | SkylitReviews, SkylitToolComparisons |

### A2. Named concepts, with Skylit's definitions

| Concept | Definition as shown | Source key |
|---|---|---|
| Node | A cell. "Every node on the Heatseeker map acts like a magnet in the market, where price is attracted to these zones due to dealer positioning — yet these same areas can also act as walls that repel price and create reversals." | SkylitDocs |
| King Node | "The King Node is the strike carrying the largest absolute exposure value on the board. Not the largest positive, not the largest negative. The largest absolute." It is "the most influential node on the map — where Market Makers typically prefer to settle price by the end of day (EOD) or end of week (EOW) for swing trades." "King Nodes are not defined by color. They can appear as yellow or purple." | SkylitReading, SkylitDocs |
| King Node, second definition | "The strongest +GEX node across the heatmap is called the King Node, it acts as the primary structural gravity center for price." This contradicts the absolute-value definition. | SkylitGEX |
| Gatekeeper | "defensive levels that often block price from reaching the King Node"; they "act like bouncers at the door of a nightclub". "A Gatekeeper sits between two larger structural nodes. Its job is not to be the target. Its job is to determine whether price can reach the target cleanly or gets stopped in transit." | SkylitReading, SkylitDocs |
| Floor | "A floor is a large node sitting beneath current price. As price declines toward it, dealer hedging from that level becomes active. The larger the node, the more mechanical buying gets activated on approach." "The strongest floor is always the largest exposure node below spot, not the nearest node, the biggest one." | SkylitReading |
| Ceiling | "a large node above spot, and dealers at that level are positioned to sell as price rises into them." The strongest ceiling is "the largest exposure node above current price." | SkylitReading |
| Pika node | Yellow, positive GEX: "When dealers are net long gamma, shown as yellow Pika nodes on Heatseeker, their hedging works against the market's direction." | SkylitIntroGamma, SkylitGEX |
| Barney node | Purple, negative GEX: "When dealers are net short gamma, shown as purple Barney nodes on Heatseeker, their hedging runs with the market's direction." "Positive gamma creates friction, while negative gamma creates fuel." | SkylitIntroGamma |
| Absolute Value Rule | "size determines influence, regardless of sign". "A yellow Pika node with $2 billion in exposure has more structural weight than a purple Barney node with $200 million, and the larger node is going to dominate." "don't filter by color first—look at the largest nodes across the whole structure, then assess whether they're positive or negative." | SkylitIntroGamma |
| Pika Cloud | "a dense cluster of multiple positive gamma nodes sitting in close proximity on the map". Inside one, "the trend halts, movement becomes inefficient, and price sticks, rotates, and struggles to move cleanly in either direction." "A large Pika Cloud below spot is a strong mechanical floor; a large Pika Cloud above spot is a thick resistance ceiling." | SkylitPatterns |
| Air pocket | "a zone with low or weak GEX exposure. Minimal structural resistance. Minimal structural support. When price enters an air pocket, movement becomes faster with no mechanical drag." | SkylitAirPockets |
| Liquidity vacuum | "an extended air pocket. Multiple consecutive zones of low GEX exposure stacked together. In a liquidity vacuum, price doesn't just speed up. It can gap. Levels don't work." | SkylitAirPockets |
| Velocity Mode | "tracks the rate of change in dealer positioning, measuring how quickly nodes are growing, shrinking, appearing, or disappearing across recent updates". "Space (an air pocket) plus fuel (high rate of change) equals acceleration." | SkylitAirPockets |
| Node lifecycle | Four stages. Fresh: "untested and at full strength"; fresh nodes "produce the strongest reactions (~80% probability when spot approaches)". Tested: "one price interaction and a portion of its positioning has been absorbed". Delivered: "already produced a reaction and its mechanical obligation is partially or fully satisfied". Decaying: "Influence weakens over time with no further price interaction." Also: "Growth equals intent. Decay equals protection." | SkylitNodeLifecycle |
| Reshuffle | "Reshuffles happen when dealer exposure shifts quickly, often without warning"; one "often follows large volatility events like CPI, FOMC, or Power Hour when market makers rebalance risk"; "power hour liquidation can reshuffle maps entirely." | SkylitDocs, SkylitReviews |
| Range day | "positive gamma predominates and price stays inside a floor and ceiling". | SkylitRegimes |
| Trend day | Negative gamma: "every rally generates more buying from dealers rebalancing, every decline generates more selling". | SkylitRegimes |
| Whipsaw day | "a recognition that the map is giving conflicting signals across indices. The only edge in a Whipsaw environment comes from fading the extreme ends of ranges rather than chasing directional momentum". | SkylitRegimes |
| Trinity Mode | "a combined heatmap view of SPX, SPY, and QQQ displayed simultaneously - three panels, side by side, live." "A node that stands alone on one instrument is a signal worth noting, not a setup worth sizing into. Full alignment (all three agree) represents high-probability conditions." | SkylitTrinity |
| Rug | "a bearish configuration with positive gamma stacked above spot and negative gamma sitting below spot, with spot positioned below the positive node." "a ceiling that not only blocks price but pushes it down faster once rejected." | SkylitPatterns |
| Reverse Rug | "the exact mirror, with negative gamma above spot and positive gamma below spot. Spot sits above the positive node." Called "one of the higher-conviction bullish setups on the map". | SkylitPatterns |
| Beach Ball | "when price overshoots a node, punches through it, and then reacts. Like pushing a beach ball underwater: the deeper it goes, the stronger the release." "The overshoot is not the trade. The reaction that follows the overshoot is the trade." "This is NOT a breakout." | SkylitPatterns |
| Negative GEX pit | "a price zone where dealer positioning turns fully pro-cyclical, displayed in purple on the heatmap, where the crowd holds a heavy concentration of puts and dealers are net short gamma." Its end is "hedge exhaustion": "When the ball hits the bottom of the pool (ITM saturation), there's nothing left to push against." | SkylitNegativeGEX |
| Squeeze setup | "when GEX and VEX are pointing in opposing directions ... The gamma impulse fires first, sharp, fast, mechanical. Then the vanna flow catches up as implied volatility mean-reverts, generating a response in the opposite direction." | SkylitNegativeGEX |
| VEX | "the aggregate sum of vanna across all open options positions at a given strike. It tells you the direction and magnitude of the hedging flow dealers will produce as IV moves." | SkylitVEX |
| GEX/VEX alignment | "GEX is the hand brake; VEX is the slope of the hill". "GEX governs the range; VEX governs the drift." | SkylitVEX |
| Charts First | "the workflow rule that chart structure must precede exposure data in every trade decision." | SkylitChartsFirst |

### A3. The trading rules Skylit gives

1. **Target the King.** "Treat it as your primary destination target for the session. Mark it clearly on your chart as your EOD or EOW anchor." (SkylitReading)
2. **Gatekeepers decide the path.** A held Gatekeeper means price "stalls in the region it's already in"; a broken one means price "typically accelerates into the cleared zone"; "failed tests at these levels can trigger trend shifts." (SkylitReading, SkylitDocs)
3. **Floors and ceilings frame the day.** "the relationship between spot and its nearest floor and ceiling is the single most useful piece of context you can have for any intraday trade". (SkylitReading)
4. **Size before color** (the Absolute Value Rule). (SkylitIntroGamma)
5. **Rug.** "Watch for the Rug setup on the approach to a large positive node when negative gamma sits within the current session's expected range." (SkylitPatterns)
6. **Beach Ball.** Trade the reversion after an overshoot, not the overshoot; identify it by "the failure to follow through. Price moves through the node but does not build momentum on the other side. The tape stalls." (SkylitPatterns)
7. **Pit reversal.** "Wait for a failed continuation attempt into the pit, a wick or absorption ... Pair it with a VIX curl down from its peak. Enter on the first pullback from the initial snap, not on the snap itself." (SkylitNegativeGEX)
8. **Air pocket plus velocity.** "When Velocity Mode shows a rapidly growing node adjacent to an air pocket, that combination is one of the highest-conviction setups in the framework." (SkylitAirPockets)
9. **Lifecycle.** Prefer fresh nodes; the framework "helps traders avoid trading levels that have lost their structural strength through repeated testing." (SkylitNodeLifecycle)
10. **Whipsaw days.** Fade range extremes; do not chase. (SkylitRegimes)
11. **Trinity.** Size only when SPX, SPY and QQQ agree. (SkylitTrinity)
12. **Confirmation.** "Treat each node as a level of interest, not a trade trigger, and let price action confirm your setups — Heatseeker™ is a lens, not an entry system." Three checks: nearby magnets (King or Gatekeeper), "confirmation or rejection wick", and SPX, SPY and QQQ "in agreement". GEX/VEX confluence is "one of the most powerful confirmations". (SkylitDocs best practices)
13. **Tenor.** "For options 0–5 DTE, gamma is dominant; for 7–180 DTE, vanna is dominant". (SkylitVEX)
14. **Vol spikes.** "When vol spikes, back-end +VEX creates significant sell flow that's entirely invisible in a front-month gamma map. A market that looks well-supported by +GEX on the day's expiration can experience a sharp rug-pull once far-expiry vanna flips to sell flow". (SkylitVEX)
15. **Charts first.** "Always form your thesis from price structure before checking Heatseeker". (SkylitChartsFirst, SkylitDocs)

### A4. What Skylit says about how positioning is estimated

- **Data.** "Market data is licensed directly from OPRA, NASDAQ and CBOE. Dealer positioning is derived by Skylit from that data, not reported by the exchanges." (Skylit home page, SkylitModule)
- **Method.** The calculations "run on custom inference models and proprietary intelligence built from years of research into dealer microstructure" (docs, as shown in a search summary). No page found gives the formula, the sign rule for calls and puts, the volatility surface used, or how trades are classified.
- **Sign.** No per-type convention is published. The education pages describe dealers on either side ("When a dealer is long calls (bought from a customer selling them), they're long delta, so they sell stock. When they're short calls (sold to a customer buying them), they're short delta, so they buy stock."), and the pit page assumes "the crowd holds a heavy concentration of puts and dealers are net short gamma". The sister product Flowseeker "streams options flow with the side it filled on and its size against open interest", so the platform classifies trade side. Skylit does not say whether Heatseeker's nodes use that classification.
- **Open interest against intraday flow.** Maps update intraday and "Nodes can vanish, weaken, or reappear at new levels intraday." A third-party review adds: "Overnight recalculation of open interest matters far more for swing traders, as intraday 15-second updates are mostly noise." [third party]
- **Expiries.** The same-day column (SPXW 0DTE) is on the board. Nothing found mentions FLEX options or over-the-counter books.
- **A point Skylit does not make** [derived here]. Even with open interest frozen, a node's size moves during the day, because gamma depends on spot, implied volatility and time. At the money, Black-Scholes gamma scales roughly as one over the square root of time left, so an at-the-money 0DTE node is about \(\sqrt{6.5/1} \approx 2.5\) times larger with one hour left than at the open. "Velocity" can therefore show Greek drift rather than new positions, and Skylit does not separate the two.

### A5. Numbers stated by Skylit or about it

| Number | Context | Status |
|---|---|---|
| ~80% | Fresh nodes' reaction "probability when spot approaches" | [vendor claim], no method or sample given (SkylitNodeLifecycle) |
| 85–90% | Accuracy "during the creator's personal usage", with "your results may vary" | [vendor claim] in the FAQ, as reported by third-party pages (SkylitReviews) |
| $2 billion against $200 million | The Absolute Value Rule example | Illustration, not data (SkylitIntroGamma) |
| 0–5 DTE / 7–180 DTE | Gamma-dominant and vanna-dominant tenors | [vendor claim] (SkylitVEX) |
| 1 s / 15 s | Web refresh / Discord bot refresh | [vendor claim] / [third party] |
| $99.99, $299, $699 per month | Community, Initiate and Pro plans; one page lists Initiate at $100 a week | [third party], not checked on Skylit's own site |
| 4.8–4.9 stars, 313–372 reviews | Trustpilot score and count, varying by date of the snapshot | [third party] |
| "over 2,300 members since launching in 2025" | Community size | [third party] |
| "~50% win rates" | For users "who treat large gamma nodes as 'buy signals'" | [third party] claim in a review, no data |

### A6. Skylit's claims set against the evidence

| Claim | Evidence bearing on it | Verdict |
|---|---|---|
| The King Node is where market makers "prefer to settle price" at EOD or EOW | Pinning is real but small: closing prices of optionable stocks cluster at strikes, altering returns by at least 16.5 bp per expiry (NiPearsonPoteshman2005). S&P 500 futures are pulled to the at-the-money strike on serial-option expiries and pushed away from it before SPX expiries, a notional shift of at least $115 million per expiry (GolezJackwerth2012). | A weak, sign-dependent version is supported at expiry. No test of "the largest absolute node" as a daily or weekly target was found. |
| Absolute size matters more than sign | Hedging per 1% move at a strike is proportional to the node's size, so size sets how large the flow is. Its sign sets its direction: positive gamma trades against the move, negative gamma with it. Negative gamma goes with intraday momentum and positive gamma with reversal (BaltussenDaLammersMartens2021, BarbonBuraschi2020); Bitcoin expiry reversals are strongest when gamma is negative (Weiss2026). Skylit's own floor definition ("mechanical buying gets activated on approach") holds only for positive gamma. | Half right. Size predicts how much hedging, not which way. "Magnet or wall" wording makes the rule hard to falsify. No test found. |
| Fresh nodes react about 80% of the time | None published. | Untested [vendor claim]. |
| 85–90% accuracy | A founder's personal record, no definition of "accuracy". | Untested [vendor claim]. |
| Velocity plus an air pocket is a high-conviction setup | Intraday node changes mix Greek drift and inferred flow. Trade-side classification errs on 13% to 41% of classifiable option trades depending on the rule (SavickasWilson2003). Public-OI proxies track dealer inventory poorly for 0DTE, correlation 0.53 (ArdiaVaudescal2026). | Untested, and built on the noisiest part of the data. |
| Same-day nodes drive intraday price | Cboe puts net market-maker 0DTE gamma at $170M–$670M through the day, 0.04%–0.17% of daily S&P futures liquidity, and "at best just 0.2%" (Cboe0DTEsDecoded2025). | Contradicted in size, if Cboe's customer-side data are right. |
| GEX and VEX add information | In one pre-registered SPY test, GEX's link to next-day realized volatility falls from ρ = −0.36 to −0.03 (p = 0.18) after controlling for the VIX and at-the-money IV; VEX falls to ρ = −0.01 (FlashAlphaBacktest2026). Public-OI net gamma does predict next-half-hour variance, about 36% lower per standard deviation for non-0DTE gamma (ArdiaVaudescal2026). | Mixed: some intraday variance information; little beyond implied volatility at the daily horizon. |
| Trinity agreement raises the odds | None published. SPX, SPY and QQQ books overlap in holders, so agreement is partly the same fact seen three times. | Untested. |

### A7. Inconsistencies inside Skylit's own material

1. **Two King definitions.** "largest absolute exposure value" (reading-heatseeker, docs, module page) against "The strongest +GEX node" (gex-trading, gamma-exposure).
2. **Negative GEX as a ceiling.** support-resistance-gex says "In a low-VIX environment, the most common configuration is positive GEX sitting below spot as a mechanical floor, with negative GEX above acting as a ceiling." The Reverse Rug page says negative gamma above spot "amplifies any bounce".
3. **Floors by size, mechanics by sign.** A floor is the "largest exposure node below spot", which may be purple, yet the page says "mechanical buying gets activated on approach", which only a positive node implies.
4. **Vanna sign.** vex-trading states "A dealer who is short options carries positive vanna." Black-Scholes vanna is positive for out-of-the-money calls and negative for out-of-the-money puts [derived here], so a dealer short options has positive vanna only on the put wing. The page's example (short puts, falling IV, dealer buys back stock) is the put case.
5. **Refresh and coverage.** One second against 15 seconds; 300+, 3,500+ or 5,000+ tickers.

---

## Part A sources: Skylit

### SkylitDocs
- Citation: Skylit (n.d.). Heatseeker documentation: "Introduction", "Core Concepts", "How to read and use Heatseeker", "Best practices", "Limitations", "FAQs". https://docs.skylit.ai/ , https://docs.skylit.ai/core-concepts , https://docs.skylit.ai/how-to-read-and-use-heatseeker , https://docs.skylit.ai/best-practices , https://docs.skylit.ai/limitations , https://docs.skylit.ai/faqs
- Type: vendor documentation
- Verified via: WebSearch results listing each page title and URL, with summaries (queries on 2026-09-29). Pages not fetched (docs.skylit.ai blocked). Page dates unverified.
- Question: how to read the map and use it.
- Data and method: none disclosed beyond "custom inference models and proprietary intelligence".
- Findings: the color scale (green to yellow positive, blue to purple negative), the magnet language, King Nodes by absolute value, "Rate of Change" (how fast liquidity changes), best practices (context not signals; three confirmations; GEX/VEX confluence) and four limitations: "Not 100% Accurate" ("random events such as news headlines, earnings reports, or geopolitical shocks can instantly alter dealer flows"), "Low volume periods can skew heatmap efficacy", "Map Reshuffles", and "Context Matters" ("Don't trade off a single node or isolated event"). "Heatseeker is contextual intelligence, not a trading signal."
- Limits: marketing and education pages; no test, sample or error rate.
- Use in the book: the primary description of the heatmap and its vocabulary; the limitations page supports the book's "context, not a trade" rule in the vendor's own words.

### SkylitModule
- Citation: Skylit (n.d.). "Heatseeker: GEX and VEX Heatmap by Strike" and the Skylit home page. https://www.skylit.ai/modules/heatseeker , https://www.skylit.ai/
- Type: vendor documentation (product page)
- Verified via: WebSearch result titles and summaries. Not fetched.
- Question: what the product shows.
- Data and method: "Market data is licensed directly from OPRA, NASDAQ and CBOE. Dealer positioning is derived by Skylit from that data, not reported by the exchanges."
- Findings: rows are strikes and columns expirations; King starred; strike nearest price highlighted; GEX/VEX switch; one-second refresh claim; Velocity timeframes of 1 minute to 1 day; increasing and decreasing filters; node alerts; Trinity Mode.
- Limits: product claims.
- Use in the book: the figure specification in Part F; the data-source sentence is the only method statement Skylit makes.

### SkylitReading
- Citation: Skylit (n.d.). "Reading Heatseeker Maps: King Nodes, Gatekeepers, Floors, and ..." https://www.skylit.ai/learn/reading-heatseeker
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Question: how to build "a structural picture of dealer positioning" from a map.
- Data and method: none.
- Findings: definitions of King Node (largest absolute), Gatekeeper, floor and ceiling ("the largest exposure node below spot, not the nearest"); the King as "primary destination target".
- Limits: no evidence offered.
- Use in the book: the core vocabulary.

### SkylitIntroGamma
- Citation: Skylit (n.d.). "Intro to Gamma: Pika Nodes, Barney Nodes, and the Absolute Value ..." https://www.skylit.ai/learn/intro-to-gamma
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Question: how sign and size show on the map.
- Findings: Pika (yellow, long gamma) and Barney (purple, short gamma) nodes; the Absolute Value Rule with the $2 billion against $200 million example.
- Limits: the rule is asserted, not tested; see A6.
- Use in the book: the "absolute size matters more than sign" claim, which the book can set against the sign mechanics of Chapter 8A.

### SkylitGEX
- Citation: Skylit (n.d.). "Gamma Exposure (GEX) Explained: The Market's Shock Absorber"; "How to Trade with GEX: Nodes, Flip Zones & Scenarios"; "Support & Resistance from GEX: King Nodes & Air Pockets". https://www.skylit.ai/learn/gamma-exposure , https://www.skylit.ai/learn/gex-trading , https://www.skylit.ai/learn/support-resistance-gex
- Type: vendor education articles
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: "+GEX below spot acts as support, +GEX above spot acts as resistance, and where GEX sign changes is where polarity flips, and where the most violent moves occur." The second King definition ("strongest +GEX node"). GEX levels describe "where dealers are mechanically obligated to hedge right now". Advice: "Treat these as zones of interest, not precise levels, and use price confirmation before entering."
- Limits: internal contradictions (A7).
- Use in the book: flip zones and walls in Skylit's words; an example of a vendor's two definitions of one term.

### SkylitNegativeGEX
- Citation: Skylit (n.d.). "Negative GEX Explained: Pits, Reversals & Squeeze Setups." https://www.skylit.ai/learn/negative-gex
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: the pit, hedge exhaustion at "ITM saturation", the reversal entry rule paired with "a VIX curl down from its peak", and the GEX-VEX squeeze.
- Limits: the exhaustion story is a metaphor. The mechanism it gestures at is real: deep in-the-money gamma is small, so dealer selling slows, and customers closing puts make dealers buy back hedges (a "put-covering" flow). Neither is shown to release "all at once".
- Use in the book: negative-gamma regimes and the vanna rebound after stress (Chapters 8B, 9A).

### SkylitVEX
- Citation: Skylit (n.d.). "Vanna Exposure (VEX): The Vol–Spot Feedback Loop"; "How to Trade with VEX: Vanna Flows & Vol Regimes"; "GEX vs VEX: When Greeks Align and When They Fight". https://www.skylit.ai/learn/vanna-exposure , https://www.skylit.ai/learn/vex-trading , https://www.skylit.ai/learn/gex-vex-alignment
- Type: vendor education articles
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: VEX defined as aggregate vanna by strike; a four-cell scenario matrix ("+VEX below spot (support in calm, rug-pull risk in stress), –VEX below spot (fragile floor in calm, fast bounces in stress), +VEX above spot (breakouts in calm, caps in rising vol), and –VEX above spot (soft ceiling in calm, squeeze fuel during vol spike)"); gamma dominant at 0–5 DTE, vanna at 7–180 DTE; "GEX governs the range; VEX governs the drift"; the vanna rally loop ("IV drops push dealer delta long, triggering buying").
- Limits: the vanna sign statement is incomplete (A7, item 4); no test.
- Use in the book: the VEX view of the heatmap; vanna rallies (Chapters 7B, 9A).

### SkylitPatterns
- Citation: Skylit (n.d.). "Heatseeker Patterns: Rug, Reverse Rug, Pika Clouds, and Beach Ball ..." https://www.skylit.ai/learn/heatseeker-patterns
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: the four named patterns and their rules (A2, A3).
- Limits: no frequency, hit rate or sample.
- Use in the book: examples of level-based pattern trading that the Edge Book rejects (Chapters 10H, 10I).

### SkylitNodeLifecycle
- Citation: Skylit (n.d.). "Node Lifecycle: Fresh, Tested, Delivered, and Decaying Levels." https://www.skylit.ai/learn/node-lifecycle
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: the four stages; "~80% probability" for fresh nodes; "A node that gets bigger over multiple sessions is a node with dealers accumulating real positioning behind it. A node that was large yesterday and is smaller today is a hedge bleeding off."
- Limits: the 80% has no method. Day-to-day size changes also come from spot, IV and time (A4).
- Use in the book: a clear case of a number without evidence.

### SkylitRegimes
- Citation: Skylit (n.d.). "Gamma Regime Awareness: Range Days, Trend Days, and Whipsaw Days ..." https://www.skylit.ai/learn/gamma-regimes
- Type: vendor education article
- Verified via: WebSearch title and summary. Not fetched.
- Findings: "Positive gamma creates range days, negative gamma creates trend days, and mixed signals create whipsaw days."
- Limits: no test.
- Use in the book: the two regimes of Chapter 8B in vendor language.

### SkylitAirPockets
- Citation: Skylit (n.d.). "Air Pockets, Liquidity Vacuums, and Velocity Mode." https://www.skylit.ai/learn/air-pockets-velocity
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: air pocket, liquidity vacuum and velocity definitions; air pocket plus growing node as a top setup.
- Limits: "low GEX" is not quantified.
- Use in the book: the low-gamma gap between strikes, which Chapter 8A's profile shows as the flat part of the curve.

### SkylitTrinity
- Citation: Skylit (n.d.). "Trinity Mode: Cross-Index Alignment with SPX, SPY, and QQQ." https://www.skylit.ai/learn/trinity-mode
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: three live panels; SPX, SPY and QQQ options "carry distinct positioning distributions, different strikes in different notional sizes, different expiry concentrations, different institutional footprints"; agreement is "high-probability".
- Limits: no test; SPY's book is shaped by wholesaler internalization (Chapter 2B), a caveat Skylit does not raise.
- Use in the book: why a number built from SPY differs from one built from SPX (Chapter 8A's practice box).

### SkylitChartsFirst
- Citation: Skylit (n.d.). "Charts First: Market Structure Before Exposure." https://www.skylit.ai/learn/charts-first
- Type: vendor education article
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: "You form the thesis from the chart, then you check Heatseeker to see if the structure underneath supports it or kills it"; Heatseeker "is a confirmation tool, not a signal generator".
- Limits: none beyond being vendor advice.
- Use in the book: the vendor agrees with the book's rule that flow and positioning confirm a thesis and never write one (Chapter 11A).

### SkylitDealerPositioning
- Citation: Skylit (n.d.). "Dealer Positioning: How Market Makers Move Price." https://www.skylit.ai/learn/dealer-positioning
- Type: vendor education article
- Verified via: WebSearch title and summary. Not fetched.
- Findings: the sign chain for long and short calls; "The core assumption underlying this framework is that dealer hedging is mechanical and non-discretionary."
- Limits: the assumption is contested: option market makers appear to delta hedge selectively (Dong2025) and some hedge with minimum-variance deltas that already include vanna (HullWhite2017).
- Use in the book: the mechanical-hedging assumption behind every map.

### SkylitToolComparisons
- Citation: Skylit (n.d.). "Best GEX Tools for Options Traders in 2026"; "Best Vanna Exposure (VEX) Tools for Trading". https://www.skylit.ai/learn/best-gex-tools , https://www.skylit.ai/learn/best-vanna-tools
- Type: vendor comparison pages (written by a competitor of the tools compared)
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: Heatseeker "shows VEX with vol regime integration, cross-expiry tenor breakdown, and GEX alignment at full strike-level resolution", "over 3,500+ tickers on Pro"; QuantData lists VEX with GEX, DEX and CHEX "starting around $62/month"; VolSignals is "$300/month" and "Zoom-based commentary"; OptionsDepth centers on gamma, charm and delta exposure.
- Limits: self-interested.
- Use in the book: the landscape of vanna and charm tools.

### SkylitFlowseeker
- Citation: Skylit (n.d.). "Introduction to Flowseeker: Real-Time Institutional Flow"; "Navigating Flowseeker". https://www.skylit.ai/learn/intro-to-flowseeker , https://www.skylit.ai/learn/navigating-flowseeker
- Type: vendor education articles
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: captures "every options trade across all U.S. exchanges"; "Flow Score ranging from −100 to +100 for directional conviction, combining spread position, sweep detection, moneyness, DTE, size, and IV confirmation"; "FlowBonus score (0–100)"; sweeps "tagged and weighted differently from single-venue blocks".
- Limits: the side of fill is a quote-rule classification in effect, which misclassifies a known share of option trades (SavickasWilson2003, MuravyevPearson2020).
- Use in the book: how flow tools sign trades (Chapter 9C).

### SkylitReviews
- Citation: Third-party review and listing pages on Skylit: Trustpilot (https://www.trustpilot.com/review/skylit.ai and paginated copies); "Skylit Heatseeker Review 2026 — Is $699/Month Worth It?" (https://skylit-review.netlify.app/); "Skylit Heatseeker Review 2026 - Is This Premium Trading Tool Worth ..." (https://topwhops.com/skylit-review/); "I Tried Skylit's Heatseeker for Options Flow — Here's My Honest Take" (https://sites.google.com/view/brightavenue4148/heatseeker); "Skylit on Whop: Is the Heatseeker Options Flow Tool Actually Worth ..." (https://sites.google.com/view/glowoutlook0360/heatseeker); "Is Skylit on Whop a Scam? ..." (scribehow.com); getskylit.com; skylit-heatseeker.ratedgroups.com; panwhopticon.app.
- Type: third-party reviews and affiliate pages (authorship and independence unknown)
- Verified via: WebSearch titles and summaries. None fetched (all blocked).
- Findings: founder "Glitch (@glitchspx)"; "over 2,300 members since launching in 2025"; plan prices; the FAQ's "85-90%" personal-usage accuracy; Trustpilot 4.8 to 4.9. The recurring critical theme: the tool is "wrong as much as it is right", which one review attributes to "treating Heatseeker as a directional signal service". One reviewer reported being "pretty red" despite attending sessions. "the learning curve is steep."
- Limits: affiliate incentives; star ratings are not performance data.
- Use in the book: for the product's reach and cost only; not evidence of an edge.

---

## Part B. Other vendors and methods

### B1. Comparison at a glance

| Vendor or method | Quantity and unit | Sign assumption | Intraday method | Display | Headline claim | Key |
|---|---|---|---|---|---|---|
| SqueezeMetrics GEX (2016, revised 2017) | Per option line \(\Gamma \cdot OI \cdot 100\) for calls and \(\Gamma \cdot OI \cdot (-100)\) for puts, in shares per $1; the monitor quotes SPX GEX in dollars per SPX point | Dealers long calls (bought from covered-call writers), short puts (sold to hedgers) | End of day, open interest | One daily index number, with DIX | High GEX, low next-day volatility | SqueezeMetricsGEX, SqueezeMetricsMonitor |
| SqueezeMetrics Implied Order Book (2020) | Option-implied liquidity by price level | As above | End of day | An "implied order book" | Selling puts adds liquidity; buying puts places "stop-loss orders" that take it | SqueezeMetricsIOB2020 |
| Industry "per 1%" form | \(\Gamma \times\) modeled dealer position \(\times\) multiplier \(\times S^2 \times 0.01\), dollars per 1% move | Varies by vendor | Varies | Profile by strike; total | "the industry convention" | SpotGammaLevels |
| SpotGamma | Dollars per 1% move; key levels | Index: dealers short puts, long calls. Equities: dealers "short options for both puts and calls" | "Open Interest & Volume Adjustment" model on the four nearest expiries including 0DTE; TRACE's "Options Inventory Model", updated every minute; HIRO from every trade's delta notional | Key levels on charts; TRACE strike-by-time heatmap (red negative, purple positive); HIRO line | Call Wall caps, Put Wall supports, Volatility Trigger marks the regime | SpotGammaLevels, SpotGammaDDOI, SpotGammaIntraday |
| MenthorQ | Net GEX from open interest across expiries | Not published (search) | Not found | Levels drawn inside TradingView, TrendSpider, Quantower, Tickblaze | Call Resistance, Put Support, HVL regime line | MenthorQLevels |
| Volland (Wizard of Ops) | Dealer gamma, vanna and charm by strike and expiry | None assumed: each trade classified as a dealer buy or write | Order-by-order classification from OPRA | Vanna and charm exposure maps | ">90%" classification accuracy, "99%" on 0DTE; dealers more sensitive to IV than to spot | VollandDeLorenzo2023 |
| Unusual Whales | GEX, DEX, vanna, charm | Four methods, from Cboe market-maker data ("no assumptions") to "dealers are long all calls and short all puts" | "Periscope" (Cboe data, 10-minute or 1-minute refresh); bid/ask side attribution; raw volume | Greek-exposure pages per ticker | Ranks its own methods best to worst | UnusualWhalesGEX |
| Skylit Heatseeker | Signed exposure per strike and expiry, dollars | Not published | Not published ("custom inference models") | Strike-by-expiry heatmap, GEX/VEX switch | King Node, Gatekeepers, patterns | Part A |
| Cboe (exchange research) | Net market-maker gamma per 1% move from Cboe's customer-side data | Measured, not assumed | Intraday, from exchange data | Research notes | 0DTE market-maker hedging "at best just 0.2%" of SPX daily liquidity | CboeXu2023, Cboe0DTEsDecoded2025 |
| Tier1 Alpha (added after the restart) | Dealer gamma in dollars "per index point" | Not published | Not published ("daily gamma exposure models") | Newsletter charts; a Hedgeye report | "Gamma exposure is the throttle for volatility" | Tier1Alpha |
| Barchart (added) | Dollars per 1% move, from open interest, four nearby expiries | Calls positive, puts negative, for every ticker | End of day (not confirmed) | Free per-ticker GEX pages | None | BarchartGEX |
| GEXBot (added) | GEX per strike from open interest and from volume; State greeks from classified flow; units not stated | "net taker imbalances from the orderflow classification engine" (State); convention unstated (Classic) | 1- to 30-minute look-backs; one-second orderflow change; WebSocket feed | API and platform plugins | Zero gamma and "major" strikes by OI and by volume | GEXBot |
| Bank desks: Nomura, Goldman Sachs, JPMorgan (added) | "$Gamma", "Gamma Neutral" line; scenario flows | Not disclosed | Client notes, quoted in the press | Client notes | Gamma hedging "10-15% of total daily volumes on index futures" (Nomura, 2020); 0DTE "Volmageddon 2.0" risk (JPMorgan, 2023) | NomuraMcElligott, GoldmanFishman2020, JPMorganKolanovic2023 |

### SqueezeMetricsGEX
- Citation: SqueezeMetrics (2016; revised 2017). "Gamma Exposure (GEX)™ - Quantifying hedge rebalancing in SPX options." White paper. https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf
- Type: practitioner white paper
- Verified via: WebSearch results showing the title and PDF URL and summarizing it ("first published in March 2016, then revised in December 2017"). The PDF was not read (squeezemetrics.com blocked). The search summaries were my only view of the formula, the assumption and the quartile numbers.
- Question: whether the hedging needs implied by SPX option open interest explain SPX volatility.
- Data and method: gamma and open interest for every SPX option line, signed by an assumption about who holds each type; GEX set against subsequent SPX returns.
- Findings: "For call options, the formula is: GEX = Γ · OI · 100 ... For put options ... GEX = Γ · OI · (-100)". The assumption: calls are "sold by investors and bought by market makers (reflecting covered call strategies), while puts are mostly purchased by investors for downside protection and sold by market makers." "When comparing the highest and second-highest quartiles of GEX to subsequent SPX variance, the 1-day standard deviations are 0.55% and 0.85%, respectively." "When GEX is high, the option market is implying that volatility will be low."
- Limits: the sign rests entirely on the assumption; a review summary notes that "GEX assumes that all put options are sold by market makers, which is not the case in practice." The quartile numbers could not be checked against the PDF, nor could the sample period.
- Use in the book: the origin of the vendor formula (Chapter 8A). Two corrections to check in the PDF before publication: the paper dates from March 2016, revised December 2017, not 2017 alone; and its per-line formula is in shares per $1 (\(\Gamma \cdot OI \cdot 100\)), while the \(S^2 \times 0.01\) "per 1% move" form is the later industry convention.

### SqueezeMetricsMonitor
- Citation: SqueezeMetrics (n.d.). "A Handy-dandy Reference to the 'Master Spreadsheet'" (monitor guide), https://squeezemetrics.com/monitor/static/guide.pdf ; the DIX/GEX monitor, https://squeezemetrics.com/monitor/dix ; and the SqueezeMetrics thread "GEX is Gamma Exposure: ...", https://threadreaderapp.com/thread/1215761573194747904.html
- Type: vendor documentation
- Verified via: WebSearch result titles and summaries. Not fetched.
- Findings: units and reading of the index. "for every 1-point down (up) in the S&P 500, option dealers would need to buy (sell) $64,521,235 worth of S&P 500 index exposure" (a worked example for a GEX reading of 64,521,235). "Positive GEX means dealers are providing liquidity to (stabilizing) the market when spot price moves; negative GEX means dealers are taking liquidity from (destabilizing) the market". The thread says single-stock GEX is "measured in 1% moves and denominated in dollars" and that SPX index options "dwarf the size of gamma" from single stocks such as the FAANGs.
- Limits: one summary says "thousands of dollars per SPX point", which conflicts with the $64,521,235 example; the unit wording needs checking in the guide.
- Use in the book: units. A figure in dollars per point converts to dollars per 1% by multiplying by \(0.01\,S\) [derived here]: at SPX 3,000, $64.5 million per point is about $1.9 billion per 1% move.

### SqueezeMetricsIOB2020
- Citation: SqueezeMetrics (2020). "The Implied Order Book: Measuring S&P 500 liquidity with SPX options." White paper. Listed at https://www.goodreads.com/book/show/57020948-the-implied-order-book ; talk "The Implied Order Book, GEX, and how markets crash", https://www.youtube.com/watch?v=p9qSlW-jrrk
- Type: practitioner white paper
- Verified via: WebSearch results showing the title, author (SqueezeMetrics) and year. Text not read.
- Question: can option hedging requirements be read as resting liquidity in the index?
- Findings: "we can build a uniquely information-rich 'implied order book' simply by knowing how existing options must be hedged", to "see where option-originated liquidity is abundant, and where it is scarce". Selling a put means "indirectly (through the agency of the option dealer) adding liquidity to the market"; buying a put is "effectively placing stop-loss orders above and below the market, which take liquidity".
- Limits: framework, not a test; sign assumptions as in the GEX paper [unverified that they are unchanged].
- Use in the book: the cleanest practitioner statement of GEX as liquidity supplied or taken, a bridge to the feedback mathematics of Chapter 8B.

### SqueezeMetricsDIX2018
- Citation: SqueezeMetrics (2018). "Short is Long." White paper introducing the Dark Index (DIX). https://squeezemetrics.com/monitor/download/pdf/short_is_long.pdf
- Type: practitioner white paper
- Verified via: WebSearch results showing the title, PDF URL and "March 2018". Not fetched.
- Question: whether off-exchange short-sale volume measures investor buying.
- Data and method: FINRA Trade Reporting Facility short-sale volume, dollar-weighted across S&P 500 members, "since 2011".
- Findings: "When a market-maker fills an investor's buy order, the MM is facilitating the trade by shorting shares. Thus, short volume is actually representative of investor buying volume". The summary also reports "As short volume rises above 35%, average intraday returns are uniformly positive" [vendor claim].
- Limits: vendor claim; the practitioner test by Confirm Signal first found no signal, then retracted that finding after a data error (ConfirmSignal2021). [Correction added after the restart: the search summaries in ConfirmSignal2021 say the retracted 2021 results were "positive" ones; the corrected 2024 conclusion is unverified.]
- Use in the book: the other half of the SqueezeMetrics dashboard, and an example of a practitioner combining GEX with a flow measure.

### SpotGammaLevels
- Citation: SpotGamma (n.d.). Key-level help articles: "Call Wall: What It Is and How SpotGamma Uses It", "Put Wall: What It Is and How SpotGamma Uses It", "Zero Gamma", "Absolute Gamma", "Key Gamma Strike", "Hedge Wall", "Key Delta Strike"; articles "Gamma Exposure (GEX)", "What Are Call Walls and Put Walls? The Strikes That Shape Market ...", "The Volatility Trigger for ES Futures Traders". https://support.spotgamma.com/hc/en-us/articles/15297391724179-Call-Wall-What-It-Is-and-How-SpotGamma-Uses-It , https://support.spotgamma.com/hc/en-us/articles/15297856056979-Put-Wall-What-It-Is-and-How-SpotGamma-Uses-It , https://support.spotgamma.com/hc/en-us/articles/15297958613907-Zero-Gamma , https://support.spotgamma.com/hc/en-us/articles/15297255426195-Absolute-Gamma , https://support.spotgamma.com/hc/en-us/articles/15297780226451-Key-Gamma-Strike , https://support.spotgamma.com/hc/en-us/articles/15297582984723-Hedge-Wall , https://spotgamma.com/gamma-exposure-gex/ , https://spotgamma.com/call-wall-put-wall-explained/ , https://spotgamma.com/volatility-trigger-zero-gamma-trading/
- Type: vendor documentation
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings (definitions as shown):
  - Call Wall: "the strike with the largest net call gamma"; "the upper bound of the expected range". SpotGamma says it "originated and popularized" the term.
  - Put Wall: "the strike with the largest net put gamma"; "the lower bound".
  - Zero Gamma: "the modeled spot price where aggregate GEX crosses zero".
  - Volatility Trigger: "SpotGamma's most actionable level", which "identifies where dealers have their last major concentration of positive gamma support, which is different from Zero Gamma"; "a proprietary SpotGamma level derived from its estimated distribution of gamma rather than a generic zero crossover"; it "often sits several points above Zero Gamma".
  - Absolute Gamma: "the strike with the largest total gamma", "a strong support/resistance level and a magnet", "only used on index products". This is SpotGamma's analogue of Skylit's King Node.
  - Key Gamma Strike: "the largest magnitude of combined gamma", "highly-tactical".
  - Hedge Wall: for single stocks, like the Volatility Trigger, "predictive of future volatility behavior with statistical significance" [vendor claim; no test found].
  - Formula: "Dollar GEX per 1% move = Γ × modeled dealer position × contract multiplier × spot² × 0.01", with 0.01 described as "the industry convention".
- Limits: the wall explainers get the hedge direction backwards. The Call Wall page says "dealers who sold calls at that strike must sell shares as price approaches", then that the same short-call dealer is "short gamma" and must "buy shares as the underlying rises toward the strike". The Put Wall page says dealers "who sold puts at that strike must buy shares as price falls toward it". A dealer short a put must sell as price falls [derived here]. Resistance at the call wall needs dealers long those calls; support at the put wall needs dealers long those puts.
- Use in the book: the standard vocabulary of walls and flips. Correction for Chapter 8A: the book equates the gamma flip with SpotGamma's Volatility Trigger, but SpotGamma defines them as two levels.

### SpotGammaDDOI
- Citation: SpotGamma (n.d.). "DDOI (Dealer-Directional Positioning)", https://support.spotgamma.com/hc/en-us/articles/15246735925395-DDOI-Dealer-Directional-Positioning ; "Gamma Model Positioning Adjustments", https://spotgamma.com/spx-gamma-model-positioning-adjustments/ ; "SpotGamma vs. MenthorQ, Unusual Whales & Other Options Data ...", https://spotgamma.com/best-gamma-exposure-tool-comparison/
- Type: vendor documentation
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: "At SpotGamma, the working assumption for the sake of our models is that dealers are short options for both puts and calls on equities", while "SpotGamma models market makers to be short puts and long calls on index products, due to the prevalence of option strategies like collars and covered calls". Dealer-directional open interest is "the hidden positioning of open interest between market makers (dealers) and their customers"; "we can only estimate how dealers vs participants are positioned by the use of modeling and assumptions". A sensitivity test on data from February 7, 2020 assumed "the model is only 50% correct and the remaining 50% open interest is randomized to be long or short"; the summary gives simulated average gamma of "835 billion" at 50%, "1.02 trillion" at 60% and "1.18 trillion" at 70% (units not shown). The comparison page describes SGOI as estimates of "how market makers and buyside participants are actually positioned across the entire single-stock universe" and prices SpotGamma "starts at $299/mo".
- Limits: the equity assumption (dealers short both) is the opposite of what CBOE data showed for equity options in 1990–2001, where non-market-maker investors held more short than long open interest in both calls and puts (LakonishokLeePearsonPoteshman2004).
- Use in the book: a leading vendor states its sign rule, and it differs by product; its own randomization test is the sensitivity analysis Chapter 8A recommends.

### SpotGammaIntraday
- Citation: SpotGamma (n.d.). "What is the SpotGamma HIRO Indicator?", https://support.spotgamma.com/hc/en-us/articles/4420646443539-What-is-the-SpotGamma-HIRO-Indicator ; "SpotGamma HIRO User Guide" (updated June 25, 2026), https://spotgamma.com/hiro-user-guide ; "What is SpotGamma TRACE?", https://support.spotgamma.com/hc/en-us/articles/33607907909011-What-is-SpotGamma-TRACE ; "TRACE User Guide" (March 30, 2026), https://spotgamma.com/wp-content/uploads/2026/03/TRACE-User-Guide_30-March-2026.pdf ; "What is the Open Interest & Volume Adjustments index chart?", https://support.spotgamma.com/hc/en-us/articles/15350877023123-What-is-the-Open-Interest-Volume-Adjustments-index-chart ; "Gamma Exposure (GEX) Explained", https://spotgamma.com/gamma-exposure-explained/
- Type: vendor documentation
- Verified via: WebSearch titles, dates in titles, and summaries. Not fetched.
- Findings: HIRO ("Hedging Impact Real-Time Options") "measures and aggregates the delta notional value from every option trade, estimating the hedging requirement associated with each transaction"; an upward line "reflects the impact of traders buying calls and selling puts". The OI & Volume Adjustment model "estimates intraday position changes from live trade volume", applied "across the four nearest expirations — including 0DTE options". TRACE is "built off of SpotGamma's proprietary Options Inventory Model that determines intraday positioning for SPX options", "updates every 1-minute", offers "5-day forward projections" and a 0DTE-only strike plot; "Areas of the map that are red infer a relative MM negative gamma position, while purple indicates a positive gamma position."
- Limits: the classification behind HIRO and TRACE is not published; its error rate is unknown. TRACE's purple means positive gamma, the opposite of Skylit's purple.
- Use in the book: how a vendor fills the gap between daily open interest and an intraday map; TRACE is the strike-by-time counterpart of Heatseeker's strike-by-expiry map.

### MenthorQLevels
- Citation: MenthorQ (n.d.). "Key Levels and Key Terms Guide", https://menthorq.com/guide/key-levels-and-key-terms/ ; "Gamma Levels on ES Guide", https://menthorq.com/guide/gamma-levels-on-es/ ; "Gamma levels for Futures Trading Guide", https://menthorq.com/guide/gamma-levels-for-futures-trading/ ; TrendSpider listing "MenthorQ Gamma Levels", https://trendspider.com/trading-tools-store/indicators/6839db-menthorq-gamma-levels/
- Type: vendor documentation
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: the gamma engine "analyzes open interest, market positioning, and proprietary quantitative logic"; it calculates net GEX "by aggregating open interest across expirations". Call Resistance "Pinpoints the strike with the heaviest call-option gamma"; Put Support "Identifies the strike with the heaviest put-option gamma"; the High Volatility Level (HVL) "Marks the price where the cumulative gamma curve reverses slope, separating positive from negative gamma regimes". Levels are delivered into charting platforms rather than a separate app.
- Limits: no published sign rule found; no test.
- Use in the book: the same three levels under different names, a reminder that "put support" and "HVL" are one vendor's labels.

### VollandDeLorenzo2023
- Citation: DeLorenzo, J. (2023). "Impact of option dealer flows on equity returns." Ad Deum Funds / Volland. SSRN 4669282, posted December 19, 2023. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4669282 ; also https://vol.land/VollandWhitePaper.pdf and https://www.wizofops.com/uploads/1/1/6/8/116858111/impactofoptiondealerflowsonequityreturns.pdf . With "Volland Options Dealer Positioning Dashboard User Guide" (June 2024), https://vol.land/VollandUserGuide_Jun24.pdf
- Type: working paper (SSRN, 2023) by a vendor, plus vendor documentation
- Verified via: WebSearch results showing title, author, SSRN number and date. Not fetched. Co-authors: the summary names Jason DeLorenzo as sole author (Jill A. DeLorenzo acknowledged for editing).
- Question: whether Volland's proprietary dealer positioning predicts equity returns.
- Data and method: OPRA trade feed; "On an option order-by-order basis using executed price, surrounding orders, Black-Scholes fair value, and Bid/Ask spreads as a guide, Volland determines if each order filled is a buy or a write on the dealer side"; positions compiled per strike and expiry, Greeks computed on the aggregate.
- Findings: "option dealer hedging is a major driver in market movements"; "option dealers are predominantly more sensitive to changes in implied volatility than to the movement in the underlying equity"; on 0DTE, "analyzing charm yields a significant edge when applied in the right time frame relative to expiration"; claimed accuracy "over 90% accuracy over all expirations, with 99% accuracy in 0DTE options" [vendor claim; how accuracy was measured is not shown]. The user guide: charm "is the opposite sign of vanna on each strike" because it is computed for "+1 day passing"; "Dealers will trade options to become risk neutral in aggregate vanna and charm."
- Limits: proprietary data; the accuracy claim has no disclosed benchmark; written by the vendor.
- Use in the book: the vanna-and-charm school of practice, and a vendor that rejects the sign convention altogether.

### WizardOfOps2026
- Citation: Wizard of Ops (2026). "The Most Accurate Way: The Volland Way." Substack, September 11, 2026. https://wizardofops.substack.com/p/the-most-accurate-way-the-volland ; with "Why Not GEX?", https://www.wizofops.com/articles/why-not-gex
- Type: vendor commentary (Volland's creator)
- Verified via: WebSearch title, date and summary for the Substack post; the "Why Not GEX?" page appeared as a result title and URL with a summary. Not fetched.
- Findings: criticizes "the cottage industry of dealer positioning services that use reductive assumptions, including GEX, open/close data, and midpoint analysis". On GEX: it "assumes all puts are bought and all calls sold using open interest, is easy to calculate and right maybe ±75% of the time, but while many puts are bought, there are a lot sold as well, so there is no telling the magnitude of each strike". On midpoint (quote-side) classification: "more accurate than other methods including GEX, but there are way too many common scenarios where this is incorrect". On open-close data: it "doesn't tell you what you really want to know". Volland's own feed is "the full OPRA data feed ... averaging roughly 200 billion messages per day".
- Limits: a competitor's critique; the "±75%" is an unsupported figure.
- Use in the book: a practitioner inside the industry calling the standard convention "useless and obsolete" — the model-risk point of Chapter 8A from a vendor.

### UnusualWhalesGEX
- Citation: Unusual Whales (n.d.). "An overview of Gamma Exposure and GEX tools." https://unusualwhales.substack.com/p/an-overview-of-gamma-exposure-and (also https://unusualwhales.com/information/an-overview-of-gamma-exposure-and-gex-tools ); per-ticker pages such as https://unusualwhales.com/stock/SPY/greek-exposure
- Type: vendor documentation
- Verified via: WebSearch titles and summaries. Not fetched.
- Findings: four methods ranked best to worst. (1) "Periscope SPX MM GEX", SPX only, "uses CBOE data and makes no assumptions about dealer positioning", with "10-minute refresh for Retail Pro subscription and 1-minute refresh for Retail Max". (2) Intraday volume with bid/ask side attribution ("Directionalized Volume"). (3) Intraday volume assuming "dealers are long all calls and short all puts traded". (4) Open interest assuming "dealers are long all calls and short all puts in open interest". The general theory "assumes that market makers are the counterparty to nearly every options transaction, and that on balance they end up buying calls and selling puts."
- Limits: "no assumptions" holds only as far as Cboe's own customer and market-maker flags are complete; SPX trades on Cboe venues, so coverage is good for SPX but not for multi-listed SPY.
- Use in the book: the clearest public ranking of measurement methods, from assumed signs to exchange-reported positions; evidence that exchange market-maker data reach retail tools intraday.

### OtherGEXTools
- Citation: Other GEX products seen in results (titles and URLs only unless stated): FlashAlpha, "Free GEX Chart - Live Gamma Exposure by Strike" (https://flashalpha.com/tools/gamma-exposure) and API pages; QuantWheel, "Free GEX Heatmap (Gamma Exposure by Strike)" (https://quantwheel.com/tools/gex-heatmap) and "Call walls, put walls and the gamma flip" (https://quantwheel.com/how-to/understand-walls-and-flip); TradeEcho, "Best GEX Tools for Options Traders (2026), Compared" (https://tradeecho.com/best-gex-tools) and "GEX heatmaps and dealer positioning" (https://tradeecho.com/features/dealeredge); gex-levels.com, "Call Wall & Put Wall Explained: What Gamma-Derived Levels Really ..." (https://gex-levels.com/blog/call-wall-put-wall-explained); ZeroGEX methodology (https://zerogex.io/methodology); Options Analysis Suite, "Gamma Exposure (GEX) & Greeks by Strike" (https://www.optionsanalysissuite.com/documentation/gamma-exposure); GEXHorizon SPX page (https://gexhorizon.com/gamma-exposure/spx); Barchart, "S&P 500 Index Gamma Exposure (GEX)" (https://www.barchart.com/stocks/quotes/$SPX/gamma-exposure); OptionsDepth, "Market Makers' Charm Exposure Projection" (https://www.optionsdepth.com/resouce/market-makers-charm-exposure-projection); VannaCharm, "Introducing VannaCharm" (https://vannacharm.com/blog/introducing-vannacharm); Glassnode Research, "Introducing: Taker-Flow-Based Gamma Exposure" (https://research.glassnode.com/gamma-exposure/).
- Type: vendor documentation
- Verified via: WebSearch result titles and URLs. Methods not verified, except that one summary of generic tools says "Platforms differ on three inputs: which expirations are included, how dealer positioning is inferred (long-vs-short assumption), and how implied volatility is fit."
- Findings: the product space is crowded, cheap at the low end (free heatmaps) and mostly undisclosed in method. Glassnode signs crypto option positions by taker flow, the same idea as bid/ask attribution.
- Limits: no methods read; Barchart's convention in particular is unverified.
- Use in the book: a footnote on how many free heatmaps exist, each with an undisclosed sign rule.

### Sen2026
- Citation: Sen, N. (2026). "Gamma Exposure (GEX) without the Paywall: A Fully Disclosed Dealer-gamma Engine for Gold and S&P 500 Futures at US$42.80 a Month." University of Liverpool Management School. SSRN 7098358 (posting date shown as July 11 or July 28, 2026). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7098358
- Type: working paper (SSRN, 2026)
- Verified via: WebSearch results showing title, author, affiliation and abstract text. Not fetched.
- Question: can a fully disclosed GEX engine be built cheaply?
- Data and method: CME S&P 500 and COMEX gold futures options; "Black-76 pricing with per-strike implied volatility, the standard dealer-sign convention", "normalization formats, zero-gamma level solutions, call and put walls, tiered pinning strikes, vanna and charm overlays, and a three-horizon regime framework"; execution bridge to Sierra Chart or NinjaTrader.
- Findings: commercial services "cost roughly US$99 to US$1,999 per month, cover mainly U.S. equity indices, and disclose little of their methodology"; the disclosed engine runs for US$42.80 a month; "no mainstream commercial provider publishes native gamma exposure for gold futures".
- Limits: a methods paper; no predictive test reported in the summary.
- Use in the book: a complete public recipe (per-strike IV rather than one flat volatility, zero-gamma solved numerically, walls, pins) and a citable statement that vendors disclose little.

### Chilingarian2026
- Citation: Chilingarian, A. (2026). "The Sign of Dealer Gamma: A Reproducible, Auditable Framework for Computing S&P 500 Gamma Exposure (GEX)." SSRN 7131778 (posting date shown as June 26 or July 31, 2026). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7131778
- Type: working paper (SSRN, 2026)
- Verified via: WebSearch results showing title, author and abstract text. Not fetched.
- Question: how to make the sign of GEX explicit and auditable.
- Findings: "Because Black-Scholes gamma is identical and positive for calls and puts at the same strike, the sign in any GEX aggregate is an inventory assumption, and when left implicit, a mislabeled term can silently invert the entire regime." The paper sets out "a three-model taxonomy", "ratifies one convention (Model A, the SqueezeMetrics open-interest proxy) as a written contract", fixes the aggregation formula and "its unit scale", gives "a correctness rule" for the gamma flip, shows on "a real 10,223-contract SPX snapshot" how switching conventions changes GEX, and "identifies a reproducible software failure mode".
- Limits: a methods paper; the other two models in the taxonomy are not named in the summary.
- Use in the book: independent support for Chapter 8A's core point, that the sign is an assumption and that the regime can invert silently.

### RiskNet2024
- Citation: Risk.net (2024). "Traders dredge 0DTE data for intraday gamma insights." December 18, 2024. https://www.risk.net/markets/7960641/traders-dredge-0dte-data-for-intraday-gamma-insights (republished at https://optionmetrics.com/news/traders-dredge-0dte-data-for-intraday-gamma-insights/ )
- Type: trade press
- Verified via: WebSearch titles and summaries. Not fetched (paywalled).
- Findings: "firms such as UBS, BofA and OptionMetrics are investing in continuous net options position monitoring." "The gamma profile of options dealers – reflecting the net end-of-day position that must be delta hedged – has become a keenly watched indicator of expected market turbulence. With half of all trading in S&P 500 options now coming from zero-day-to-expiry (0DTE) contracts, some bank research teams are starting to factor these exposures into their gamma indicators."
- Limits: press summary; bank methods not described.
- Use in the book: the only verified statement in this search about bank desks' gamma indicators (see Gaps for the named strategists). A related Risk.net title, "After the selloff, competing theories on dealer gamma" (https://www.risk.net/markets/7959811/after-the-selloff-competing-theories-on-dealer-gamma), was seen but its content was not.

### Tier1Alpha
- Citation: Tier1 Alpha (n.d.; posts 2023 to 2024). Home page, https://tier1alpha.com/ ; X account @t1alpha, including "Gamma exposure is the throttle for volatility." (https://x.com/t1alpha/status/1682821058456616960), "1/ Navigating Negative Gamma: 🧵 Dealers remain ..." (https://x.com/t1alpha/status/1719002496163807425) and "Gamma acts as a throttle for volatility, while ..." (https://x.com/t1alpha/status/1816187637411242454); Hedgeye, "Hedgeye announces partnership with options research provider Tier 1 Alpha" (https://app.hedgeye.com/insights/136818-hedgeye-announces-partnership-with-options-research-provider-tier-1-al) and "Tier 1 Alpha's Market Situation Report" (https://accounts.hedgeye.com/products/market_situation_report/972!973).
- Type: practitioner research (newsletter, social posts, a report sold through Hedgeye)
- Verified via: WebSearch titles and summaries (two queries, 2026-09-29). tier1alpha.com and threadreaderapp.com are blocked for fetching. The post dates (2023-07-22, 2023-10-30, 2024-07-24) are decoded from the X post IDs [derived here], not read on the posts.
- Question: how dealer gamma, volatility and systematic flows drive the index.
- Data and method: not published in anything found. The site describes research on "market structure through options, volatility, passive flows, and systematic rebalancing", "built for markets dominated by machines", and offers "daily gamma exposure models". No sign rule, expiry set or intraday method was found.
- Findings: the framing is a chain: "Gamma exposure is the throttle for volatility", and "volatility is the toggle for equity exposure" (volatility-targeting funds size their equity holdings by realized volatility). The October 2023 thread: dealers "remain excessively short-gamma with around $1.7 billion to hedge per index point", "close to record levels since 2018" [as shown in a search summary]. The Hedgeye report covers "Dealer Gamma and volatility-term structure, and the explosive use of 0dte Contracts".
- Limits: check the unit before quoting. At SPX near 4,100 (late October 2023), $1.7 billion per point would be about $70 billion per 1% move [derived here], far above the per-point example in SqueezeMetrics' guide ($64.5 million per point). Either the search summary garbled the unit or Tier1's measure is defined differently. No test of the model was found.
- Use in the book: the practitioner version of the chain from dealer gamma to realized volatility to volatility-control selling (Chapters 8B, 9A); an example of a per-point unit that needs converting before comparison.

### BarchartGEX
- Citation: Barchart (n.d.). "S&P 500 Index Gamma Exposure (GEX)", https://www.barchart.com/stocks/quotes/$SPX/gamma-exposure ; the same page for SPY (https://www.barchart.com/etfs-funds/quotes/SPY/gamma-exposure), QQQ, the Nasdaq 100 ($IUXX) and single stocks such as AMZN and OPEN; and the article "Gamma Exposure Explained: How to See the Hidden Price Points Where Market Makers Move Stocks", https://www.barchart.com/story/news/35756961/gamma-exposure-explained-how-to-see-the-hidden-price-points-where-market-makers-move-stocks
- Type: vendor documentation (free web pages on a market-data site)
- Verified via: WebSearch titles and summary (query of 2026-09-29). barchart.com is blocked for fetching, so the page text was seen only as summarized.
- Question: the per-ticker GEX of a mass-market data site.
- Data and method: "Gamma exposure levels are calculated on 4 nearby expirations (the first 2 weeklies and the first 2 monthlies), based on a 1% move of the underlying security using gamma and open interest." Sign: "Gamma exposure levels are always positive for call options and negative for put options", which is the SqueezeMetrics convention (dealers long calls, short puts) applied to every ticker.
- Findings: none; a display, not a study.
- Limits: the convention is the same for index and single-stock options, where SpotGamma assumes dealers short both types on equities (SpotGammaDDOI) and CBOE data show public investors net short both types (LakonishokLeePearsonPoteshman2004). Four expiries leave out the quarterly and LEAPS open interest that some index vendors include. The update timing (end of day or intraday) was not visible.
- Use in the book: the free, widely seen default: open interest, four expiries, dollars per 1% move, calls positive and puts negative. Resolves Part B's earlier gap on Barchart's convention.

### GEXBot
- Citation: NFA LLC (2026). "gexbot-openapi: The NFA gexbot OpenAPI Specification", version 2.5.5 (commit of 2026-09-20). https://github.com/nfa-llc/gexbot-openapi ; product site https://www.gexbot.com/ ; documentation https://docs.gexbot.com/ (glossary at https://docs.gexbot.com/glossary/); a scribd copy titled "Understanding GEXBOT Classic Features" (https://www.scribd.com/document/681253879/NFA-Docs).
- Type: vendor documentation (public API specification)
- Verified via: WebSearch titles and summaries (query of 2026-09-29); the GitHub repository was read directly (README and the JSON specification). docs.gexbot.com and scribd.com are blocked for fetching.
- Question: what a data vendor for futures and platform traders delivers, by package.
- Data and method: three packages, each a different answer to the open-interest problem.
  - Classic: GEX per strike computed twice, from open interest and from volume. Each strike row is "[strike, gex_vol, gex_oi, priors]", and "priors holds the 1, 5, 10, 15 and 30 minute lookback GEX values". Categories: "`gex_full` - Full aggregation of GEX (call/put), up to 90 days out", "`gex_zero` - Only next expiry+0 ... 0dte", "`gex_one` - Only next expiry+1". Key levels ("majors"): "Zero Gamma, Major Positive/Negative GEX by OI and Volume".
  - State: per-strike delta, gamma "(long/short)", vanna and charm for the 0DTE and 1DTE expiries (or a named expiry). "The values are net taker imbalances from the orderflow classification engine."
  - Orderflow: "`agg_*` - the cumulative sum of the transactions since the 09:30 ET session open. It resets each day"; "`net_*` ... the net taker exposure across the active chain at this moment"; "`*oflow` - the change in the taker exposure over the last second."
  - Delivery: REST, a real-time WebSocket feed, 90 days of history, an end-of-day report, and plugins for NinjaTrader, ATAS, MotiveWave and Sierra Chart (plugins per the search summary).
- Findings: none; a data product. The example response for SPX shows "zero_gamma", "major_pos_vol" and "major_pos_oi" at different strikes (7135 and 7200) at the same moment, so the volume-based and open-interest-based maps name different key levels.
- Limits: the specification gives no unit for the GEX values and no rule for classifying a trade's taker side; no accuracy figure.
- Use in the book: the cleanest public statement of the three layers every intraday map combines: yesterday's open interest, today's raw volume, and today's side-classified flow. The "priors" and "maxchange" look-backs are the same idea as Skylit's Velocity Mode.

### NomuraMcElligott
- Citation: McElligott, C. (Nomura, cross-asset strategy), client notes as quoted by others: SpotGamma, "March '20 Nomura Gamma" (https://spotgamma.com/march-20-nomura-gamma/), "Nomura McElligot Options Gamma Update" (https://spotgamma.com/nomura-mcelligot-options-gamma-update/), "Nomura August 2020 Gamma Update" (https://spotgamma.com/nomura-gamma-august-2020-aapl/), "Nomura Gamma Update" (https://spotgamma.com/nomura-gamma-update/), "Is Nomura Reading SpotGamma Notes?" (https://spotgamma.com/nomura-spotgamma-gamma-overlap/); Heisenberg Report, "Nomura's McElligott On 'Classic Short Gamma' And $62 Billion In Potential Vol Target Fund De-Risking", January 28, 2020 (https://heisenbergreport.com/2020/01/28/nomuras-mcelligott-on-classic-short-gamma-and-62-billion-in-potential-vol-target-fund-de-risking/).
- Type: bank strategist research (client notes, not public), known only through press and vendor quotation
- Verified via: WebSearch titles and summaries (four queries, 2026-09-29). spotgamma.com and heisenbergreport.com are blocked for fetching. No Nomura note was seen directly.
- Question: where dealers' index gamma sits against spot, and what flows it and volatility-targeting funds imply.
- Data and method: not disclosed in anything seen. The notes report dealer "$Gamma" for SPX, QQQ and single stocks and a "Gamma Neutral" line (the flip), and pair them with estimates of rebalancing by volatility-targeting funds.
- Findings (as quoted): the late-January 2020 close was "textbook Dealer Gamma-hedging", "classic 'Short Gamma'"; volatility-targeters' implied notional exposure had grown by more than $250 billion since the previous September and "would have recently touched upwards of ~$360 billion"; the headline figure was $62 billion of potential de-risking (from the Heisenberg title). A note quoted by SpotGamma put SPX dealers "Short Gamma" below 3852 with spot at 3850, "near or below the 'Gamma Neutral' line"; after an expiration, QQQ's aggregate "$Gamma" dropped by over 50%, "unclenching" the index. From the March 2020 report: "the flows from option gamma hedging can account for 10-15% of total daily volumes on index futures" [as shown in a search summary of SpotGamma's page].
- Limits: second-hand quotations of proprietary notes; the method and the sign assumptions are unknown. SpotGamma's own post asks whether Nomura was reading SpotGamma's notes, so bank and vendor estimates may share inputs and are not independent confirmations. The 10-15% figure is an estimate by the same desk, not a measurement.
- Use in the book: the bank-desk vocabulary the press repeats ("short gamma", "gamma neutral", "unclenching" after expiration) and the pairing of dealer gamma with volatility-control flows (Chapters 8B, 8C, 9A); the 10-15% share, quoted as Nomura's estimate, gives the reader a sense of scale to set against Cboe's 0.2% for 0DTE alone.

### GoldmanFishman2020
- Citation: Fishman, R. (Goldman Sachs, equity derivatives strategy) (2020). "Q&A on Gamma and Option-Driven flows", client note, republished as "All You Ever Wanted To Know About Gamma, Op-Ex, And Option-Driven Equity Flows" by ZeroHedge (https://cms.zerohedge.com/markets/all-you-ever-wanted-know-about-gamma-op-ex-and-option-driven-equity-flows ; a copy dated June 10, 2020 at https://www.nationandstate.com/2020/06/10/all-you-ever-wanted-to-know-about-gamma-op-ex-and-option-driven-equity-flows/), by SpotGamma ("Goldman: All You Ever Wanted To Know About Gamma, Op-Ex, And ...", https://spotgamma.com/all-you-ever-wanted-to-know-about-gamma/) and by OptionsHawk ("Q&A on Gamma and Equity Option Flows with Goldman Sachs", https://optionshawk.com/exclusive/qa-on-gamma-and-equity-option-flows-with-goldman-sachs/).
- Type: bank strategist research (client note), known through republication
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). All copies blocked for fetching. The date comes from the URL of one copy [unverified against the note].
- Question: what gamma is, when it matters, and how expiration changes it.
- Data and method: explanatory note; no model of dealer positions was seen in the summaries.
- Findings (as shown): gamma is "one of the larger sources of non-fundamental economic activity in global markets" and has "the potential to be one of the most important non-fundamental flows in equity markets (particularly when 'short gamma' causes volatility to accelerate), but tracking gamma is complex and dynamic". It "is most likely to be relevant when open interest is concentrated in specific strikes, particularly near-the-money strikes". Into expiration "near-the-money options' gamma rises, while far out-of-the-money options' gamma falls." The long-gamma mechanism is stated through who does not hedge: "Investors who sell options to generate yield and do not delta-hedge those options leave the counterparty who bought the options (typically a delta-hedging entity) long the option, and therefore long gamma", whose hedging "has the potential to reduce market volatility".
- Limits: a teaching note, not an estimate; the full text was not seen.
- Use in the book: a bank strategist's own statement that tracking gamma is "complex and dynamic", and the clearest press-circulated account of why overwriting leaves dealers long gamma (Chapters 8A, 8B); op-ex mechanics for Part D.
- Related press numbers, flagged: crypto-news aggregators in 2026 attribute to Goldman a "record $2.6 trillion" of S&P 500 call notional on May 7 and "$7.5 billion in net short gamma exposure" on dealers' books around an April 1, 2026 breakout, and report that "By May 8, net gamma exposure for the S&P 500 reached $107.18 billion" (https://cryptobriefing.com/goldman-record-gamma-squeeze-sp-options/ , https://www.bitget.com/news/detail/12560605429559 , https://letsdatascience.com/news/sp-500-records-26t-in-calls-sparks-massive-gamma-squeeze-338a9fa3). No unit is given, the $107 billion figure has no stated source, and a "Record $2.6 Trillion In Option Notional" headline about Goldman also ran in November 2021 (https://macro.economicblogs.org/zerohedge/2021/11/durden-goldman-stunned-2-6-trillion-notional/). Do not quote these as data; they are useful only as an example of dealer-gamma numbers that lose their units and sources in retelling.

### JPMorganKolanovic2023
- Citation: Kolanovic, M. (JPMorgan, chief market strategist), client note of February 2023, as reported by Bloomberg: "JPMorgan Strategist Kolanovic Warns of 'Volmageddon 2.0' Risk in Options Market", February 15, 2023 (https://www.bloomberg.com/news/articles/2023-02-15/jpmorgan-strategist-kolanovic-warns-of-volmageddon-2-0-risk-in-options-market ; also https://news.bloomberglaw.com/capital-markets/jpmorgans-kolanovic-warns-of-volmageddon-2-0-risk-in-options); "JPMorgan Spells Out 'Volmageddon' Risk on Zero-Day Option Craze", March 6, 2023 (https://www.bloomberg.com/news/articles/2023-03-06/jpmorgan-spells-out-volmageddon-risk-on-zero-day-option-craze); Fortune, February 16, 2023 (https://fortune.com/2023/02/16/jpmorgan-volmageddon-meme-stocks-federal-reserve-kolanovic/); Grabien, "Kolanovic Warns 0DTE Can Lead To Volmageddon 2.0, $30 Billion In ..." (https://news.grabien.com/thewire/kolanovic-warns-0dte-can-lead-to-volmageddon-20-dollar-30-billion-in-i). The rebuttals: Advisor Perspectives, "Bank of America Says Options-Driven 'Volmageddon 2.0' Warning Is Overblown", February 23, 2023 (https://www.advisorperspectives.com/articles/2023/02/23/bank-of-america-says-options-driven-volmageddon-2-0-warning-is-overblown); SpotGamma, "No, 0DTE Will Not Result In 'Volmageddon:' BofA Derivative Gurus Respond To Kolanovic" and "Volmageddon? No; JPM, BofA Say 0-DTE Options Are Suppressing Intraday Vol" (https://spotgamma.com/no-0dte-will-not-result-in-volmageddon-bofa-derivative-gurus-respond-to-kolanovic/ , https://spotgamma.com/volmageddon-no-jpm-bofa-say-0-dte-options-are-suppressing-intraday-vol/).
- Type: bank strategist research (client note), known through press reports
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). Bloomberg and SpotGamma not fetched (paywalled or blocked).
- Question: does the growth of 0DTE options create a crash risk like February 2018?
- Data and method: JPMorgan's estimates of 0DTE volume and of flows under stress scenarios; the model was not seen.
- Findings (as reported): 0DTE "daily notional volumes ... is around $1 trillion" by the team's estimate; "options are net sold by directional investors, and the supply of gamma is likely causing a suppression of realized intraday volatility, but if there is a big move when these options get in the money, and sellers cannot support these positions, forced covering would result in very large directional flows"; the risk comes from "a heavy imbalance, such as too many non-hedgers short downside"; in the worst case of thin trading, a 5% drop in the S&P 500 could snowball into another 20% if all traders offloaded 0DTE holdings; a headline figure of "$30 billion" of intraday selling (Grabien title; the unit and scenario were not visible). JPMorgan's own quantitative group reported that 0DTE "is not primarily driven by retail players" and that much of it is "one dynamic-hedger trading with another dynamic hedger, and/or underlying replacement (buying calls instead of long stock)".
- Limits: a scenario, not an estimate of actual dealer gamma. Bank of America's derivatives strategists called it "overblown" a week later, and SpotGamma's summary of the JPM and BofA material is that 0DTE was "suppressing intraday vol". Cboe's customer-flow data later showed market-maker 0DTE gamma small and balanced (CboeXu2023, Cboe0DTEsDecoded2025). Kolanovic left JPMorgan in 2024 after a run of poor market calls (AdvisorHub, https://www.advisorhub.com/jpmorgans-kolanovic-to-exit-amid-string-of-poor-stock-calls/), which bears on his record as a forecaster, not on the mechanics.
- Use in the book: the canonical "0DTE Volmageddon" claim that Part E sets against Cboe's measurement; in the text, a worked contrast between a scenario (what could happen if one side is imbalanced) and a measurement (what the imbalance was). Chapter 9B.

### CboeXu2023
- Citation: Xu, M. (Cboe Global Markets, VP and Head of Derivatives Market Intelligence) (2023). "Volatility Insights: Much Ado About 0DTEs - Evaluating the Market Impact of SPX 0DTE Options." Cboe Insights. https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/ ; republished as "Much Ado About 0DTEs: Separating Fact From Fiction", IBKR Campus, September 8, 2023, https://www.interactivebrokers.com/campus/traders-insight/securities/options/much-ado-about-0dtes-separating-fact-from-fiction/
- Type: exchange research note
- Verified via: WebSearch titles and summaries (three queries, 2026-09-30). cboe.com blocked for fetching. The Cboe posting date is not shown; the IBKR copy is dated September 8, 2023, and the note's example is from August 15 (2023).
- Question: does SPX 0DTE trading move the index through market-maker hedging?
- Data and method: Cboe's own SPX trade data with the account-type flags that separate customers from market makers; net market-maker 0DTE positions rebuilt through the day, their gamma computed, and the implied hedge set against S&P 500 futures volume.
- Findings: "market maker positioning is fairly de minimis, with net gamma exposure ranging from $170mm to $670mm throughout the day", hedging flows "between 0.04% to 0.17% of the daily S&P futures liquidity"; in extreme cases, the change in market-maker delta for a 1% SPX move is "between 1.3 and 1.9 percent of S&P futures daily notional volume". Example: on August 15, "over 100,000 contracts of a 4440-strike put traded", yet market makers "were left short only about 3,000 contracts by the end of the day, or just 3% of the gross volume". Conclusion: "no discernible market impact from 0DTE option trading", with SPX intraday volatility and price patterns "in line with historical averages".
- Limits: SPX on Cboe only (no SPY, no ES options, no over-the-counter hedges); the exchange has a commercial interest in 0DTE growth; averages can hide the tail days that matter. The per-1% unit of "$170mm to $670mm" is implied by the method but not shown in the summary [unverified].
- Use in the book: the measured counterweight to both the 0DTE-crash story (JPMorganKolanovic2023) and to same-day nodes on vendor heatmaps; the 3% example is the cleanest illustration of why volume is not position (Part C, Chapter 9B).

### Cboe0DTEsDecoded2025
- Citation: Xu, M. (2025). "0DTEs Decoded: Positioning, Trends, and Market Impact." Cboe Insights, May 2, 2025. https://www.cboe.com/insights/posts/0-dt-es-decoded-positioning-trends-and-market-impact/
- Type: exchange research note
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30) showing title, author and date. Not fetched.
- Question: an update of CboeXu2023 as 0DTE volume grew.
- Data and method: as in CboeXu2023, on Cboe's customer and market-maker flags.
- Findings: SPX 0DTE volume has "grown more than five-fold over the past 3 years, now averaging almost 2M contracts a day"; "retail now making up around 50-60% of SPX 0DTE trading"; "Customer activity in 0DTE options continues to be extremely balanced, and as a result, net market maker gamma hedging remains de minimis, representing at best, just 0.2% of the SPX daily liquidity"; "what matters for determining the potential impact of market maker gamma hedging activity is the balance of the volume between buys vs. sells, not the notional size"; "over 95% of all 0DTE trades are done in a limited risk format (either long options outright or short via spreads)".
- Limits: as for CboeXu2023. Note for Part A6: the $170M to $670M and 0.04% to 0.17% figures come from the 2023 note; the "at best just 0.2%" is the 2025 note's.
- Use in the book: the single most quotable measured number against 0DTE-driven dealer flow; the "balance, not notional" sentence states in one line why gross 0DTE volume says little about dealer gamma (Chapter 9B, Part E).

---

## Part C. The measurement problem in practice

### C1. The clock problem

- **One count a day.** OCC computes open interest once, overnight, from clearing members' end-of-day records, reconciles it, and shows it on its site the next morning; the industry-wide file arrives the next business day morning (OCCOpenInterest). Open interest is a count of contracts, not of sides: it says nothing about who is long.
- **A live map has three inputs, only one of them observed.** Every intraday heatmap combines (1) yesterday's open interest with an assumed or estimated sign, (2) today's trades, whose side and whose open-or-close status must be inferred, and (3) today's Greeks, recomputed from spot, implied volatility and time. Only the third is exact.
- **Greek drift alone moves the map** [derived here]. With open interest frozen, an at-the-money 0DTE SPX contract at a 16% implied volatility carries about $549,000 of dollar gamma per 1% move at the open, against about $52,000 for a 30-day at-the-money contract, and at the money its gamma grows about 2.5 times from the open to the last hour and about 5 times to the last 15 minutes (the \(1/\sqrt{\tau}\) scaling). Skylit's "Velocity" and GEXBot's 1- to 30-minute "priors" therefore show node growth that needs no new positions at all (SkylitModule, GEXBot). No vendor found separates Greek drift from inferred flow in its display.
- **The morning reset.** When the next OCC file lands, the estimate built from yesterday's flow is replaced by the reconciled count. Skylit's "reshuffles" and the third-party remark that "Overnight recalculation of open interest matters far more for swing traders" (SkylitReviews) describe this reset from the user's side.

### C2. How vendors infer intraday position changes

Four methods, in the order Unusual Whales ranks its own (UnusualWhalesGEX), with what each gets wrong:

| Method | Who uses it | What it assumes | Known error |
|---|---|---|---|
| Exchange origin data: each trade flagged customer, professional, broker-dealer or market maker, buy or sell, open or close | Cboe research (CboeXu2023, Cboe0DTEsDecoded2025); Unusual Whales "Periscope" for SPX; academic studies (DimErakerVilkov2024, AmayaGarciaAresPearsonVasquez2025) | That the exchange's "market maker" code is the dealer | Misses dealers who trade as broker-dealers, upstairs and OTC hedges; one exchange's slice of multi-listed products (CboeOpenClose, ISETradeOutline) |
| Side classification of each trade (quote rule, Lee-Ready, proprietary rules) | SpotGamma HIRO and TRACE ("Options Inventory Model"), Volland (order by order, "a buy or a write on the dealer side"), GEXBot State and Orderflow ("net taker imbalances"), Skylit Flowseeker, OptionMetrics Signed Volume | That the liquidity taker is a customer and the passive side a dealer | 17% to 41% of classifiable option trades signed wrongly by the standard rules; index complex-order legs "misclassified almost 50% of the time" (SavickasWilson2003); much taker flow is professionals timing executions (MuravyevPearson2020); open or close unknown |
| Raw volume with an assumed sign | Unusual Whales method 3; GEXBot Classic "gex_vol"; SpotGamma's "Open Interest & Volume Adjustment" on the four nearest expiries (in part) | Every trade adds to the dealers' assumed side | Volume is not position: on one day a 4440 put traded over 100,000 contracts and left market makers short about 3,000, "just 3% of the gross volume" (CboeXu2023) |
| Open interest with an assumed sign | SqueezeMetrics, Barchart, MenthorQ, most free heatmaps | Dealers long calls and short puts (or a per-product variant) | The sign rests on the convention (Chilingarian2026); equity evidence contradicts it (LakonishokLeePearsonPoteshman2004) |

Two findings bound how well any of this can work. Public-open-interest gamma tracks a dealer-inventory benchmark at a correlation of 0.99 for non-0DTE options but 0.53 for 0DTE (ArdiaVaudescal2026). And market makers "match most 0DTE order flows", so their same-day gamma comes mostly from older positions that have aged into expiry (AdamsFontaineOrnthanalai2024). Both point the same way: for longer expiries, yesterday's open interest is most of the story; for same-day options, the flow that intraday maps chase is mostly offset, and the part that is not is the part public data measure worst.

### C3. Who is long and who is short: the data, their cost and their delay

| Source | What it records | Coverage | Delay | Cost (as found) | Key |
|---|---|---|---|---|---|
| OCC daily open interest | Contracts outstanding per series; FLEX reports; cleared OTC S&P 500 options | All U.S. listed options | Overnight; OCC site next morning; industry next business day | Public site; file fees [unverified] | OCCOpenInterest |
| Cboe Open-Close, end of day | Volume by origin (customer, professional customer, broker-dealer, market maker) × buy or sell × open or close; size buckets | Cboe's exchanges: all SPX, Cboe's share of multi-listed | End of day | $500 a month; history $400 per request per month, from January 2018 | CboeOpenClose |
| Cboe Open-Close, intraday | The same in snapshots | As above | 10-minute snapshots, within 5 minutes; a one-minute product | $1,000 a month (10-minute); $5,000 a month (one-minute); redistribution $5,000 to $7,500 a month | CboeOpenClose |
| ISE Trade Outline (formerly Open/Close Trade Profile) | Opening and closing volume for firm, customer, professional and (recently) market maker; 80+ fields | ISE and GEMX | End of day and intraday | Revised July 2024 [amount unverified] | ISETradeOutline |
| OptionMetrics Signed Volume | Buyer- or seller-initiated volume by Lee-Ready; at bid, ask or midpoint | 10,000+ underlyings, from 2016 | Nightly; 5- and 30-minute snapshots | [unverified] | OptionMetricsSignedVolume |
| Academic proprietary histories | Positions or open and close volume by investor class | CBOE and ISE, often 1990s to 2010s | Research only | Not for sale in that form | LakonishokLeePearsonPoteshman2004, SavickasWilson2003 |

So the side of an SPX trade is observable within minutes for a few thousand dollars a month, while the side of an SPY trade is split across exchanges and, for retail orders internalized by wholesalers, partly off-exchange (Chapter 2B). This is why the one vendor method that claims "no assumptions" covers SPX only (UnusualWhalesGEX), and why most retail maps assume a sign.

### C4. 0DTE, FLEX and over-the-counter books

- **0DTE.** Positions opened and closed within the day never reach OCC's open interest. Vendors handle this three ways: volume adjustments on the nearest expiries (SpotGammaIntraday), classified flow for the 0DTE and 1DTE expiries (GEXBot State), or exchange origin data (Unusual Whales Periscope). The measured answers are consistent with one another and not with the vendor stories: customer 0DTE flow is "extremely balanced" and net market-maker hedging is "at best, just 0.2% of the SPX daily liquidity" (Cboe0DTEsDecoded2025); market-maker 0DTE gamma is "on average positive and negatively related to future intraday volatility" (DimErakerVilkov2024); 0DTE days show index volatility 60 to 90 annualized basis points lower (AdamsFontaineOrnthanalai2024); negative market-maker gamma costs "at most 3.3 percentage points of annualized daily volatility" (AmayaGarciaAresPearsonVasquez2025). A heatmap that colors its same-day column from open interest under the long-calls, short-puts convention paints the opposite sign to these measurements whenever puts dominate at spot.
- **FLEX.** FLEX series are cleared by OCC, which publishes FLEX open interest reports, but they sit outside the standard chains most vendors ingest. Buffer ETFs alone held more than $70 billion by mid-2025, and their dealers hedge partly "through the broader listed options complex" (FLEXDefinedOutcome), so part of the FLEX book's gamma reappears in listed open interest with a sign no convention assigns correctly. No public estimate of FLEX gamma was found.
- **Over the counter.** OCC has cleared some OTC S&P 500 options since 2014 (OCCOpenInterest); bilateral OTC books (structured notes, bank-issued hedges, systematic strategies sold to institutions) leave no public record. In foreign exchange, where trade repositories collect reports, researchers rebuilt the aggregate dealer gamma, found it negative, and measured its effect on volatility (Anderegg2022). No equivalent for U.S. equity-index OTC options was found. Chapter 8A's statement that "On a stress day the invisible FLEX and OTC books can dominate the listed number" is therefore plausible but untested: nothing found quantifies it.
- **The known exception.** One institutional position is public by construction: JPMorgan's Hedged Equity collar, about 35,000 SPX contracts per leg each quarter (JPMCollar). It is the one strike where the holder is known rather than assumed: the fund is long the upper put, so whoever sold it, typically dealers, is short it.

### C5. Units

Four units are in use, and vendors often do not say which [conversions derived here]:

| Unit | Per option line | Converts to dollars per 1% by | Used by |
|---|---|---|---|
| Shares (index units) per $1 | \(\Gamma \cdot OI \cdot 100\) | multiply by \(S^2 \times 0.01\) | SqueezeMetrics' paper (SqueezeMetricsGEX) |
| Dollars per index point | \(\Gamma \cdot OI \cdot 100 \cdot S\) | multiply by \(0.01\,S\) | SqueezeMetrics' index monitor; Tier1 Alpha (SqueezeMetricsMonitor, Tier1Alpha) |
| Dollars per 1% move | \(\Gamma \cdot OI \cdot 100 \cdot S^2 \cdot 0.01\) | (itself) | SpotGamma, Barchart, the book (SpotGammaLevels, BarchartGEX) |
| Share or futures equivalents per 1% | \(\Gamma \cdot OI \cdot 100 \cdot S \cdot 0.01\) index units; divide dollars by \(50\,S\) for E-mini contracts | multiply index units by \(S\) | Desk usage; not a vendor default |
| Unstated | (not given) | cannot be converted | Skylit, GEXBot |

Worked conversions: $10 billion per 1% at SPX 6,000 is about $167 million per point, 1.67 million index units, or about 33,000 E-mini contracts per 1% move. SqueezeMetrics' example of $64.5 million per point is about $1.9 billion per 1% at SPX 3,000; Tier1 Alpha's $1.7 billion per point would be about $70 billion per 1% at SPX 4,100, far outside other figures. An SPY or XSP contract carries about one tenth of an SPX contract's dollar gamma at the same moneyness, because its underlying is one tenth the size. Vanna exposure has no settled unit; the book's figure uses dollars of dealer delta per volatility point.

Three levels of aggregation also need naming: a cell (one strike, one expiry), a strike profile (one strike summed across expiries), and a total (all strikes and expiries). A heatmap's colors are relative to whatever maximum it is scaled to, so "a big node" means big against the largest cell displayed, not big against market liquidity.

### C6. What follows for reading an intraday map

A change in a node between two refreshes has three sources: Greek drift at fixed positions, estimated new positions, and (overnight) the reset to OCC's reconciled count. They call for different readings, and no vendor found shows them separately. The evidence ranks their reliability in the reverse of the attention they get: yesterday's open interest for longer expiries is the best-measured input (ArdiaVaudescal2026), Greek drift is exact arithmetic, and same-day flow, the input intraday products sell, is the least reliable and, by the measurements above, mostly offset within the dealers' own books.

### Part C sources

(Entries are filed where they were verified. Some here, such as NiPearsonPoteshman2005, BarbonBuraschi2020 and BaltussenDaLammersMartens2021, are cited mainly in Parts A, D and E; likewise Willeboordse2026 and SpotGammaWorkflow sit under Part D sources.)

### OCCOpenInterest
- Citation: The Options Clearing Corporation (n.d.). Market data reports: "Daily Open Interest" (https://www.theocc.com/market-data/market-data-reports/other-market-data-info/batch-processing/daily-open-interest), "Open Interest" (https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/open-interest), "Flex Reports" (https://www.theocc.com/market-data/market-data-reports/series-and-trading-data/flex-reports), "OTC Open Interest" (https://www.theocc.com/market-data/market-data-reports/other-market-data-info/batch-processing/otc-open-interest); clearing pages "OTC Products" and "OTC S&P 500 Equity Index" (https://www.theocc.com/clearance-and-settlement/clearing/otc-products , https://www.theocc.com/Clearance-and-Settlement/Clearing/OTC-Products/OTC-S-and-P-500-Equity-Index-Product-Specification) and "FLEX Options" (https://www.theocc.com/clearance-and-settlement/clearing/flex-options). With two explanatory pages: Market Chameleon, "Open Interest" (https://marketchameleon.com/Learn/OpenInterest) and GEXmetrix, "The Intraday Open Interest Problem: Why Real-Time OI Does Not Exist ..." (https://www.gexmetrix.com/blog/intraday-oi-problem, a vendor blog).
- Type: clearinghouse data documentation, with a data-vendor explainer and a GEX-vendor blog
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). theocc.com blocked for fetching, so report layouts, fields and fees were not seen [unverified].
- Question: when open interest is known, and which books it covers.
- Data and method: OCC is the central counterparty for U.S. listed options and computes open interest from clearing members' end-of-day positions.
- Findings (as shown): "Open interest is calculated centrally on an end-of-day basis by the Options Clearing Corp (OCC) for US options"; it is "calculated overnight ... based on end-of-day settled trades", after "a multi-stage reconciliation" in which "Every clearing member firm submits its end-of-day position records" and OCC "cross-references those submissions against each other, chases down discrepancies, catches settlement failures, and produces a settled OI figure for every contract". "The next morning, Open interest is displayed on the OCC web site but it is not distributed industry-wide until the next business day morning." Open interest counts contracts, not sides: it rises by one when a trade opens a new contract, falls by one when a trade closes one, and is unchanged when a contract changes hands. OCC also publishes FLEX open interest reports, and since 2014 clears some over-the-counter S&P 500 index options, which "must be negotiated and matched OTC" and are sent to OCC "via an approved OTC Trade Source".
- Limits: open interest by strike carries no side and no account type; whether OCC's public files split open interest by customer, firm and market maker was not seen [unverified]. Cleared OTC S&P 500 options are only the part of the OTC market that dealers choose to clear.
- Use in the book: the fixed point of every GEX map: one reconciled count per contract per day, without sides, published the morning after. Everything a heatmap shows between two OCC files is inference (Part C); FLEX and some OTC index options do reach OCC, so "invisible" (Chapter 8A) should read "absent from the free chain feeds most vendors use".

### CboeOpenClose
- Citation: Cboe Global Markets (n.d.). "Cboe Open-Close Data" (https://go.cboe.com/Cboe-Open-Close); "Cboe Open-Close Volume Summary" on Cboe DataShop (https://datashop.cboe.com/cboe-options-open-close-volume-summary); fees in the Cboe Exchange, Inc. Fees Schedule (September 15, 2026 version, https://cdn.cboe.com/resources/membership/Cboe_FeeSchedule.pdf; earlier versions filed with the SEC, e.g. https://www.sec.gov/files/rules/sro/cboe/2024/34-99326-ex5.pdf) and in 2026 SEC rule filings for Cboe EDGX and BZX (SR-CboeEDGX-2026-041, https://www.sec.gov/files/rules/sro/cboeedgx/2026/34-105558-ex5.pdf ; SR-CboeBZX-2026-064, https://www.sec.gov/files/rules/sro/cboebzx/2026/34-106147-ex5.pdf ; SR-CboeBZX-2025-063, https://www.sec.gov/files/rules/sro/cboebzx/2025/34-103055.pdf); Federal Register notice of January 18, 2024 (https://www.federalregister.gov/documents/2024/01/18/2024-00848/self-regulatory-organizations-cboe-exchange-inc-notice-of-filing-and-immediate-effectiveness-of-a).
- Type: exchange data documentation and fee schedules (regulatory filings)
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). cboe.com, cdn.cboe.com, sec.gov and federalregister.gov are blocked for fetching, so the fee tables were seen only as summarized. Which exchange each fee applies to, and whether fees are per exchange, are [unverified].
- Question: what the exchange sells about who traded, which side and whether the trade opened or closed a position.
- Data and method: trades on Cboe's options exchanges (the summary lists BZX, C1, C2 and EDGX; SPX itself trades only on Cboe Options, C1) are bucketed "by origin (customer, professional customer, broker-dealer and market maker), buy/sell, and open/close"; customer and professional-customer volume are "further broken down into trade size buckets". End-of-day files give this "at the option level", by side, price and transaction type. The intraday product is built from "snapshots taken every 10 minutes throughout the trading day" and "available to subscribers within five minutes of the conclusion of each 10-minute period"; a one-minute intraday product also exists.
- Findings (fees as summarized): end-of-day subscription "$500 per month"; ten-minute intraday "$1,000 per month or $12,000 per year"; one-minute intraday "$5,000 per month or $60,000 per year"; ad-hoc historical end-of-day data "$400 per request per month", from January 2018; external distribution of derived data "$5,000 per month" (ten-minute and end-of-day) and "$7,500 per month" (one-minute).
- Limits: covers only Cboe's own exchanges, so it sees all SPX volume but only Cboe's share of multi-listed SPY, QQQ and single-stock volume; "market maker" is the exchange's origin code, not every dealer (an upstairs desk that hedges a client's over-the-counter option trades as a broker-dealer or does not appear); FLEX and OTC trades are outside it. The data give opening and closing volume by origin, so a net market-maker position is rebuilt by accumulating it, which drifts unless anchored to OCC open interest.
- Use in the book: the one public data set that answers "who is long and who is short" for SPX, the source behind Cboe's 0DTE notes and the vendor feeds that say they make "no assumptions" (UnusualWhalesGEX); its price ($500 to $5,000 a month per product, plus distribution fees) explains why most retail tools assume a sign instead (Part C).

### ISETradeOutline
- Citation: Nasdaq ISE (n.d.). "Frequently Asked Questions ISE Open/Close Trade Profile" (https://www.nasdaqtrader.com/content/ProductsServices/DATAPRODUCTS/ISE/ISE-GEMX%20Consolidated%20Trade%20Profile%20FAQs%20v2.pdF); "ISE Open/Close Trade Profile GEMX ... Field Description", May 2017 (https://www.nasdaqtrader.com/content/ProductsServices/DATAPRODUCTS/ISE/ISE-GEMX%20Consolidated%20Field%20Description%20-%20May%202017%20v2.pdf); Nasdaq Data Link listings "Nasdaq ISE Options - Trade Outline EOD" (https://data.nasdaq.com/databases/ISEEOD) and NITO (https://data.nasdaq.com/databases/NITO); Nasdaq Data News #2024-3 on fee changes (https://www.nasdaqtrader.com/TraderNews.aspx?id=DN2024-3); SR-ISE-2026-17 (https://www.sec.gov/files/rules/sro/ise/2026/34-105288-ex5.pdf); Finextra, "ISE introduces open/close trade profile offering" (https://www.finextra.com/pressarticle/18447/ise-introduces-openclose-trade-profile-offering).
- Type: exchange data documentation
- Verified via: WebSearch titles and summaries (one query, 2026-09-30). nasdaqtrader.com, data.nasdaq.com and sec.gov not fetched (blocked or not tried after other blocks). Fee amounts and the launch year are [unverified].
- Question: the ISE counterpart of Cboe's Open-Close data.
- Data and method: "over 80 fields for each series including opening and closing volume for firm, customer and professional trades", for "each option series listed on ISE in which an electronic trade occurred during the day", as an end-of-day file or an intraday file (the intraday file lacks the closing prices and total industry volume). The product "was recently updated to add Market Makers as a trade origin type" and renamed from "ISE Open/Close Trade Profile" to "ISE Trade Outline". Nasdaq revised its fees effective July 1, 2024.
- Findings: none; a data product.
- Limits: ISE volume only (with GEMX in the consolidated file); ISE does not list SPX, so for the S&P 500 it covers SPY and other multi-listed products, a share of their volume.
- Use in the book: the second source of side-and-origin data, and the reason an SPY map cannot be "measured" the way Cboe measures SPX: each exchange sells only its own slice of multi-listed volume.

### SavickasWilson2003
- Citation: Savickas, R., and Wilson, A. J. (2003). "On Inferring the Direction of Option Trades." Journal of Financial and Quantitative Analysis 38 [issue and pages unverified]. DOI 10.2307/4126747. https://consensus.app/papers/details/408b45d1301f52ab97e64c135752d938/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, first author, year, journal, DOI and abstract (query of 2026-09-30). The co-author's initials, issue and pages were not shown [unverified].
- Question: how well stock-market rules for signing trades (buy or sell) work on option trades.
- Data and method: a proprietary CBOE data set that records the true direction of each option trade; the quote rule, Lee and Ready (1991), Ellis, Michaely and O'Hara (2000) and the tick rule compared against it.
- Findings: the four rules "sign correctly 83%, 80%, 77%, and 59% of all classifiable trades, respectively", each on its own classifiable sample ("the quote rule cannot classify midspread trades"). "Outside-quote and reversed-quote trades are highly misclassified by all four rules." Index option complex-trade components not executed on the retail automatic system "are misclassified almost 50% of the time by any method"; dropping them (15% of the sample) raises the quote rule's success to "over 87%". Underlying price changes around the trade improve precision.
- Limits: a 1990s floor-and-early-electronic sample; today's option market has more complex orders, more price improvement at the midpoint, and faster quotes, which cut both ways. Later work (MuravyevPearson2020; Grauer and co-authors, "Option Trade Classification", SSRN 4098475, 2022, seen as a title only) revisits the problem.
- Use in the book: the error rate under every intraday heatmap that signs flow from the quote: one trade in five or six signed wrongly, and spreads, the dominant 0DTE structure (Cboe0DTEsDecoded2025: over 95% limited-risk), are the worst case. Supports Chapter 9C's caution about reading the tape.

### MuravyevPearson2020
- Citation: Muravyev, D., and Pearson, N. D. (2020). "Options Trading Costs Are Lower than You Think." Review of Financial Studies [volume, issue and pages unverified]. DOI 10.1093/rfs/hhaa010. https://consensus.app/papers/details/91e7a7bd6fd75c71a26aed3e79507231/ ; earlier SSRN version "Option Trading Costs Are Lower than You Think" (2019), DOI 10.2139/ssrn.2580548, https://consensus.app/papers/details/0b3f2f59f5a658aaa3c443e98b01810c/
- Type: peer-reviewed article (with an SSRN working-paper version)
- Verified via: Consensus results showing title, first author, year, journal, DOI and abstract (query of 2026-09-30). Consensus lists the authors as "D. Muravyev et al."; the co-author's name is from this file's key and is [unverified] here.
- Question: why measured option spreads look so large, and who pays them.
- Data and method: high-frequency equity option trades and quotes; option price changes predicted from recent stock price changes; effective spreads and price impact recomputed allowing for "execution timing".
- Findings: "a large proportion of option trades exploit this predictability to take liquidity at low cost, buying and selling immediately before option prices are expected to change"; timing-adjusted effective spreads are "one-third smaller" for the average trade and "five times smaller" for trades that reflect timing; "conventional measures of price impact overstate it by a factor of more than two"; "most option trades originate from investors who time executions, for example proprietary traders and institutional investors who have access to execution algorithms". The SSRN version adds that "the bid-ask midpoint can be a poor proxy for the true value of a security, conditional on the occurrence of a trade".
- Limits: equity options, not SPX; about costs, not about dealer inventories.
- Use in the book: two cautions for flow-signed maps (Part C). The midpoint that quote-rule signing leans on is a poor guide to value at the moment of a trade, and the liquidity taker is often a professional timing its execution, not a customer whose counterparty is a hedging dealer, so "taker bought, so the dealer is short" fails for much of the volume.

### LakonishokLeePearsonPoteshman2004
- Citation: Lakonishok, J., Lee, I., Pearson, N. D., and Poteshman, A. M. (2004). "Investor Behavior in the Option Market." NBER Working Paper 10264. DOI 10.3386/w10264. https://consensus.app/papers/details/87fe5f9bc2525863b94ac6faa6bec918/ . Published as "Option Market Activity", Review of Financial Studies (2007), DOI 10.1093/rfs/hhl025, https://consensus.app/papers/details/6e8a52aa67a25e719372db6e517e122c/
- Type: working paper (NBER, 2004), later a peer-reviewed article (RFS, 2007)
- Verified via: Consensus results showing both titles, "Josef Lakonishok et al.", years, DOIs and abstracts (query of 2026-09-30). The co-authors' names are from this file's key and are [unverified] here; the RFS volume and pages are [unverified].
- Question: who holds which side of equity options.
- Data and method: "a unique and detailed dataset of open interest and volume for all contracts listed on the Chicago Board Options Exchange over the 1990 through 2001 period", split by type of non-market-maker investor.
- Findings: "(1) non-market maker investors have about four times more long call than long put open interest, (2) these investors have more short than long open interest in both calls and puts"; the RFS version adds that "a large percentage of call writing is part of covered call positions" and that straddles and strangles are "a small fraction of option trading volume".
- Limits: equity options on CBOE, 1990 to 2001; index options and the 0DTE era are outside the sample.
- Use in the book: the best-documented historical answer to the sign question for single stocks: public investors net short both calls and puts, so market makers net long both. It contradicts SpotGamma's working assumption that dealers are short both on equities (SpotGammaDDOI) and the calls-positive, puts-negative rule Barchart applies to every ticker (BarchartGEX).

### NiPearsonPoteshman2005
- Citation: Ni, S. X., Pearson, N. D., and Poteshman, A. M. (2005). "Stock Price Clustering on Option Expiration Dates." Journal of Financial Economics [volume and pages unverified]. DOI 10.1016/j.jfineco.2004.08.005. https://consensus.app/papers/details/00f6db59793954a6b7d502a06400bf9e/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "S. X. Ni et al.", year, journal, DOI and abstract (query of 2026-09-30). Co-authors from this file's key [unverified here].
- Question: does option trading move the prices of the underlying stocks at expiration?
- Data and method: closing prices of optionable and non-optionable stocks on expiration dates, with CBOE data on who trades.
- Findings: "on expiration dates the closing prices of stocks with listed options cluster at option strike prices"; "On each expiration date, the returns of optionable stocks are altered by an average of at least 16.5 basis points, which translates into aggregate market capitalization shifts on the order of $9 billion"; "hedge re-balancing by option market-makers and stock price manipulation by firm proprietary traders contribute to the clustering".
- Limits: single stocks, monthly expirations of the pre-weekly era; the effect is an average across stocks, not a prediction for one strike on one day.
- Use in the book: the measured size of pinning (Chapter 8A quotes the 16.5 bp), and the benchmark against which Skylit's King-Node "settle price" claim is set in Part A6 and Part E.

### BarbonBuraschi2020
- Citation: Barbon, A., and Buraschi, A. (2020). "Gamma Fragility." SSRN working paper 3725454. DOI 10.2139/ssrn.3725454. https://consensus.app/papers/details/70a13a4ad8305d80b3a58f2ab9d5bc71/
- Type: working paper (SSRN, 2020 version)
- Verified via: Consensus result showing title, "A. Barbon et al.", year, DOI and abstract (query of 2026-09-30). The co-author's name is from this file's key [unverified here]; later versions not checked.
- Question: do dealers' aggregate gamma imbalances cause intraday momentum or reversal in the underlying?
- Data and method: "a large panel of equity options" used "to compute a proxy of stock-level gamma imbalance", interacted with the underlying's illiquidity.
- Findings: "intra-day momentum (reversal) is explained by the interaction of negative (positive) ex-ante gamma imbalance and illiquidity. The effect is stronger for the least liquid underlying securities"; gamma imbalance "is related to the frequency and the magnitude of flash crash events".
- Limits: the gamma imbalance is a proxy built from public data with an assumed sign; effects are conditional on illiquidity.
- Use in the book: academic support for the sign mechanics that Skylit's Absolute Value Rule sets aside (Part A6): negative gamma goes with momentum, positive with reversal.

### BaltussenDaLammersMartens2021
- Citation: Baltussen, G., Da, Z., Lammers, S., and Martens, M. (2021). "Hedging demand and market intraday momentum." Journal of Financial Economics [volume and pages unverified]. DOI 10.1016/j.jfineco.2021.04.029. https://consensus.app/papers/details/daa1769f2ffb58d588e1b315f3eb9e62/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "Guido Baltussen et al.", year, journal, DOI and abstract (query of 2026-09-30). Co-authors from this file's key [unverified here].
- Question: does hedging of short gamma create intraday momentum at the market level?
- Data and method: "intraday returns on over 60 futures on equities, bonds, commodities, and currencies between 1974 and 2020".
- Findings: "The return during the last 30 minutes before the market close is positively predicted by the return during the rest of the day"; the effect "reverts over the next days"; the paper links it "to the gamma hedging demand from market participants such as market makers of options and leveraged ETFs".
- Limits: gamma is estimated, not observed; leveraged ETF rebalancing is a second, separate source of end-of-day flow.
- Use in the book: the late-day window that Skylit calls "Power Hour" and blames for "reshuffles" is where the literature finds hedging flow in the price (Part D); the reversal over later days is the reason a map's end-of-day signal need not carry into the next session.

### Anderegg2022
- Citation: Anderegg, B., and co-authors [co-authors not shown] (2022). "The Impact of Option Hedging on the Spot Market Volatility." Journal of International Money and Finance [volume and pages unverified]. DOI 10.1016/j.jimonfin.2022.102627. https://consensus.app/papers/details/26ae2470017f5d8c945bf61b115a874d/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "B. Anderegg et al.", year, journal, DOI and abstract (query of 2026-09-30).
- Question: how much does option market makers' delta hedging change spot volatility in foreign exchange, an over-the-counter market?
- Data and method: a model with an aggregate option market maker (OMM) and an aggregate option market taker; the OMM's gamma exposure is reconstructed "by using trade repository data" for 21 October 2017 to 30 June 2018.
- Findings: the reconstructed OMM gamma "is negative"; "a negative gamma exposure of the OMM of approximately −1000 billion USD (which is around what we observe from our reconstructed OMM data) leads to an absolute increase in volatility of 0.7% in EURUSD and 0.9% in USDJPY." (The abstract does not state the gamma unit.)
- Limits: FX, not equity index options; a short sample.
- Use in the book: the counterexample to "OTC books are invisible": where regulators collect trade reports, dealer gamma can be rebuilt from records rather than assumed, and its sign then tested. U.S. equity-index OTC options have no public equivalent (Part C).

### ArdiaVaudescal2026
- Citation: Ardia, [first name not shown], and Vaudescal, [first name not shown] (2026). "The Intraday Gamma-Variance Channel with Public Options Data." SSRN working paper 7202999, posted July 29, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7202999
- Type: working paper (SSRN, 2026)
- Verified via: WebSearch result showing the title, the authors' surnames, the SSRN number, the date and abstract text (query of 2026-09-30). Not fetched (ssrn.com blocked). First names and affiliations [unverified].
- Question: does the intraday link between dealer gamma and variance, documented with proprietary positions, survive when net gamma is rebuilt from public open interest?
- Data and method: "five years of half-hour SPX observations"; net gamma from public open interest, split into 0DTE and non-0DTE buckets, compared with "a dealer-inventory benchmark sharing an open-interest seed"; dynamic-error models, a HAR horse race, predictive-ordering checks, SPY and QQQ replications, machine learning.
- Findings: "a one-standard-deviation increase in non-0DTE net gamma predicts next-bar realized variance about 36 percent lower, nearly twice the published coefficient"; the public proxy "correlates at 0.99 for non-0DTE and 0.53 for 0DTE" with the dealer-inventory benchmark, "so the bucket contrast carries the dilution reading"; the association "reproduces on SPY and QQQ options".
- Limits: a new working paper; the benchmark shares its open-interest seed with the proxy, so 0.99 is an upper bound on agreement for longer expiries, and it is the 0DTE bucket, where intraday maps focus, that the proxy tracks worst.
- Use in the book: the best current evidence on both sides of Part C's question. Public open interest carries real information about next-half-hour variance for non-0DTE options; for same-day options, which open and close inside one session, open-interest maps diverge from dealer inventory.

### Dong2025
- Citation: Dong, Y.-J. (2025). "Cross Market Price Discovery and Selective Delta Hedging in the Option Market." SSRN working paper 5529499. DOI 10.2139/ssrn.5529499. https://consensus.app/papers/details/adb5fb2fc9c95976ac1c6b836815f5bc/
- Type: working paper (SSRN, 2025)
- Verified via: Consensus result showing title, author, year, DOI and abstract (query of 2026-09-30).
- Question: how much does an option trade move the underlying stock, and which trades get hedged?
- Data and method: "trade-level OPRA and TAQ data for S&P 500 stocks in 2020"; price impact over five minutes and stock order-book activity within 100 milliseconds of option trades.
- Findings: "an option trade moves the underlying price by 0.56 basis points over five minutes, about one-sixth the effect of a stock trade"; the impact "increases monotonically with money-ness and absolute delta, and concentrates in single-leg and limit-order-book trades, while auction and multi-leg trades have negligible effects"; the pattern is "consistent with the hypothesis where option market makers selectively delta hedge their orders".
- Limits: single stocks, one year (2020); the hedging is inferred from timing, not observed.
- Use in the book: against the "hedging is mechanical and non-discretionary" premise of vendor maps (SkylitDealerPositioning). Multi-leg trades, the bulk of 0DTE (Cboe0DTEsDecoded2025), show negligible hedging footprints, which fits a dealer who nets risk across its book before trading the underlying.

### HullWhite2017
- Citation: Hull, J. C., and White, A. (2017). "Optimal Delta Hedging for Options." Journal of Banking and Finance [volume and pages unverified]. DOI 10.1016/j.jbankfin.2017.05.006. https://consensus.app/papers/details/7323868486ab5f8ca88824c9cf073c56/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "John C. Hull et al.", year, journal, DOI and abstract (query of 2026-09-30). The co-author's name is from this file's key [unverified here].
- Question: what delta minimizes the variance of a hedged option position when volatility moves with the price?
- Data and method: an empirical model of the minimum-variance delta, tested on S&P 500 options and on S&P 100, Dow Jones, single-stock and ETF options.
- Findings: "the normally calculated delta does not minimize the variance of changes in the value of a trader's position ... because there is a non-zero correlation between movements in the price of the underlying asset and movements in the asset's volatility"; "The minimum variance delta takes account of both price changes and the expected change in volatility conditional on a price change"; the model improves on stochastic-volatility models "even when the latter are calibrated afresh each day for each option maturity".
- Limits: a hedging study; it does not say what dealers actually use.
- Use in the book: a dealer who hedges with the minimum-variance delta already folds the average vanna effect of a spot move into its hedge, so a map that adds Black-Scholes GEX and a separate VEX flow double counts part of it (Part F, Chapter 7B).

### DimErakerVilkov2024
- Citation: Dim, C., Eraker, B., and Vilkov, G. (2024). "0DTEs: Trading, Gamma Risk and Volatility Propagation." SSRN working paper 4692190 (first posted November 2023). DOI 10.2139/ssrn.4692190. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692190 ; also https://www.researchgate.net/publication/377984312_0DTEs_Trading_Gamma_Risk_and_Volatility_Propagation and the Western Finance Association portal (https://westernfinance-portal.org/viewpaper?n=950096).
- Type: working paper (SSRN)
- Verified via: WebSearch results showing title, the three authors, SSRN number, posting month and abstract text; Consensus listing (title, "Chukwuma Dim et al.", 2024, DOI; no abstract) (queries of 2026-09-30). The data source (which Cboe data set) and sample period are [unverified].
- Question: is 0DTE trading on the S&P 500 destabilizing for the index?
- Data and method: 0DTE SPX trading with market makers' inventories measured by the net gamma of their positions (the exact data set is not stated in the summaries).
- Findings: "Market Makers' inventory, as measured by the net gamma of their positions, is on average positive and negatively related to future intraday volatility"; "Positive (negative) Market Makers' inventory gamma strengthens intraday price reversal (momentum)"; "The empirical evidence is consistent with delta-hedging but inconsistent with information-based trading."
- Limits: working paper; the sign is measured for market makers as the exchange defines them, not for every dealer.
- Use in the book: the measured sign that Chapter 8A already uses; for Part C, the proof that a measured market-maker gamma exists and differs from both vendor conventions, and for Part E, the academic answer to the 0DTE-crash story: on average dealers are long 0DTE gamma, which damps.

### AdamsFontaineOrnthanalai2024
- Citation: Adams, G. (University of Pennsylvania), Fontaine, J.-S. (Bank of Canada), and Ornthanalai, C. (University of Toronto) (2024). "The Market for 0DTE: The Role of Liquidity Providers in Volatility Attenuation." SSRN working paper 4881008, version of May 3, 2024. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4881008
- Type: working paper (SSRN, 2024 version)
- Verified via: WebSearch result showing title, authors, affiliations, date and abstract (query of 2026-09-30). Not fetched. Chapter 8A cites it as "Adams and co-authors (2025)"; a 2025 version was not seen [unverified].
- Question: does market makers' intermediation of 0DTE SPX options raise or lower index volatility?
- Data and method: "intraday option trading volume from 2019--2023"; identification from "exogenous variation in contract expiration days" (days with and without a same-day expiry).
- Findings: 0DTE intermediation "lowers the index volatility, on average"; "the index volatility decreases by 60–90 annualized basis points on days with 0DTE trading"; "Market makers match most 0DTE order flows, but absorb end-users' trades in long-dated options that eventually become 0DTE positions. Hedging these expiring positions then creates intraday order flow in the index futures that dampens volatility."
- Limits: working paper; an average effect over 2019 to 2023.
- Use in the book: two points for Part C. The dealer's same-day gamma comes mostly from older positions that have aged into expiry, which are in yesterday's open interest, not from today's 0DTE flow, which market makers largely match. So a same-day column built from open interest may be closer to the dealers' book than a flow-based "0DTE" map. And the measured effect damps: 60 to 90 basis points of annualized volatility lower on 0DTE days.

### AmayaGarciaAresPearsonVasquez2025
- Citation: Amaya, D., Garcia-Ares, P. A., Pearson, N. D., and Vasquez, A. (2025). "0DTE Index Options and Market Volatility: How Large is Their Impact?" SSRN working paper 5113405 (January 2025; one result dates it January 25, another January 27). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5113405 ; hosted by Cboe at https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf
- Type: working paper (SSRN, 2025), distributed by Cboe's Options Institute
- Verified via: WebSearch results showing the title, the four authors, the SSRN number, the date and abstract text (two queries, 2026-09-30). Not fetched (ssrn.com and cdn.cboe.com blocked). Sample period and data vendor [unverified].
- Question: how large can options market makers' 0DTE gamma hedging be in its effect on index volatility?
- Data and method: "proprietary trade data to determine the aggregate position of OMMs and their gamma"; an upper-bound estimate of the effect of OMM gamma on index volatility.
- Findings (as shown): the average impact of 0DTE trading "is to reduce volatility because OMMs typically have positive gamma positions"; negative OMM gamma cost "at most 3.3 percentage points of annualized daily volatility, and 6.4 points over 30 minutes".
- Limits: an upper bound, not a typical value; hosting by Cboe is not the same as authorship by Cboe, but the exchange has an interest in the result.
- Use in the book: an academic bound to set beside Cboe's own 0.2% (Cboe0DTEsDecoded2025) and against the JPMorgan scenario (JPMorganKolanovic2023): on the worst negative-gamma days, market-maker hedging adds a few points of annualized volatility, not a crash.

### OptionMetricsSignedVolume
- Citation: OptionMetrics (n.d.). "IvyDB Signed Volume", https://optionmetrics.com/signed-volume/ ; press releases "OptionMetrics Launches IvyDB Signed Volume for Tracking of Daily Options Order Flows, Participant Activity, Buy/Sell Pressure on Options Markets", Business Wire, January 27, 2020 (https://www.businesswire.com/news/home/20200127005149/en/...), and "OptionMetrics Releases Signed Volume 2.0 with Insights on Retail Participant Activity ...", Business Wire, April 7, 2021 (https://www.businesswire.com/news/home/20210407005293/en/...); "OptionMetrics releases its new IvyDB Signed Volume intraday dataset" (https://fxnewsgroup.com/forex-news/platforms/optionmetrics-releases-its-new-ivydb-signed-volume-intraday-dataset/).
- Type: vendor documentation (academic and institutional data vendor)
- Verified via: WebSearch titles, dates in the URLs and summaries (query of 2026-09-30). Not fetched. Price [unverified; not shown].
- Question: the standard commercial data set of signed option volume.
- Data and method: "Trades ... are assigned as either buyer-initiated or seller-initiated based on the trade price and the bid-ask quote at the time of the trade", using "the Lee and Ready algorithm (1991)"; volume flagged as at the bid, at the ask or at the midpoint; "over 10,000 underlying stocks and indices", history from January 2016 (version 2.0), "updated nightly"; later "five- and 30-minute snapshot intervals throughout the day" in addition to the end-of-day file; extra fields on small trades as a retail marker, marketed for "0DTE options, meme stocks, hedging flows, and other market-making activities".
- Findings: none; a data product.
- Limits: the side is inferred, not reported, so it carries the error rates of SavickasWilson2003; it says who initiated, not whether the other side was a dealer.
- Use in the book: shows that the institutional standard for intraday "side" is the same quote-rule inference retail flow tools use (Part C); only exchange origin data (CboeOpenClose, ISETradeOutline) record the side.

### FLEXDefinedOutcome
- Citation: Innovator ETFs (n.d.). "FLEX Options: The Engine Behind Defined Outcome ETFs™", https://www.innovatoretfs.com/pdf/flex_options_overview.pdf ; Cboe (n.d.). "FLEX® Options: Customized Tools for Portfolio Management", https://cdn.cboe.com/resources/education/research_publications/FLEX_QRG.PDF ; Cboe Insights, "How Outcome Based ETFs Are Reshaping Investor Demand", https://www.cboe.com/insights/posts/how-outcome-based-etfs-are-reshaping-investor-demand/ ; ETF Database, "Behind Buffer ETFs' Latest First-of-a-Kind Strategies", July 11, 2025, https://etfdb.com/news/2025/07/11/behind-buffer-etfs-latest-strategies/ ; Cerulli, "Defined Outcome ETF™ Industry Could Quadruple in Assets by 2030", https://www.cerulli.com/press-releases/defined-outcome-etf-industry-could-quadruple-in-assets-by-2030 ; FOW, "ANALYSIS: Cboe looks to buoy FLEX market with complex order rollout", https://www.fow.com/insights/analysis-cboe-looks-to-buoy-flex-market-with-complex-order-rollout
- Type: issuer and exchange product literature, trade press
- Verified via: WebSearch titles and summaries (query of 2026-09-30). Not fetched.
- Question: how large is the FLEX book that most GEX maps leave out, and who is on the other side?
- Data and method: descriptive.
- Findings (as shown): FLEX options, "launched in 1993", let users set "exercise prices, exercise styles, and expiration dates" on indexes such as SPX and on single stocks. Buffer (defined-outcome) ETFs are built from them; the category had "more than $70 billion in assets" by mid-2025, with "more than $8 billion" of net inflows in the first half of 2025. FLEX liquidity in these ETFs "is supported by more than 10 of the world's leading market makers and investment banks", and "market makers hedge through the broader listed options complex"; investors "typically use positions in the lit market as a hedge".
- Limits: issuer marketing; no public figure for FLEX SPX open interest was found in this search (OCC publishes FLEX open interest reports; see OCCOpenInterest).
- Use in the book: FLEX is not invisible, but it is outside the standard chains that vendors ingest; its dealers partly hedge with listed options, so part of a buffer ETF's gamma reappears in listed open interest with a sign no convention assigns correctly. Buffer ETFs reset on fixed calendar dates, a source of predictable, dated flows (Part D).

### JPMCollar
- Citation: SpotGamma (n.d.). "What Is the JPM Collar? The Market's Biggest Options Trade, Explained ..." (https://spotgamma.com/jpm-collar-explained/) and "GEX & JPM Collar: SpotGamma on TastyTrade" (https://spotgamma.com/gex-jpm-collar/); Tickmill, "Institutional Insights: The JPM Collar & It's Market Implications" (https://www.tickmill.com/blog/institutional-insights-the-jpm-collar-its-market-implications); OptionsTradingIQ, "The JPM Collar and Does It Matter" (https://optionstradingiq.com/jpm-collar-trade/); HMA Quant (Substack), "JPMORGAN(JHEQX) Q1 2026: Anatomy of a Market Narrative Failure" (https://hmaquant.substack.com/p/jpmorganjheqx-q1-2026-anatomy-of) and "JPMorgan's Q1 2026 Collar: Decoding a $12 Billion Hedge Strategy" (https://hmaquant.substack.com/p/jpmorgans-q1-2026-collar-decoding); Hypercall, "The JPM Collar: Why One Options Trade Moved the Entire Market" (https://docs.hypercall.xyz/insights/jpm-collar-q1-2026); social posts giving estimated Q3 2026 strikes (https://x.com/julie_wade/status/2087881359670862057). The fund: JPMorgan Hedged Equity Fund, ticker JHEQX (https://www.morningstar.com/funds/xnas/jheqx/quote).
- Type: vendor and practitioner commentary (no JPMorgan document was seen)
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). Not fetched.
- Question: how one known, dated institutional position shows on GEX maps, and whether the maps read it correctly.
- Data and method: the fund's quarterly collar is public through its holdings; vendors place its strikes on their maps.
- Findings (as shown): the collar is "the single largest systematic options structure in the U.S. equity market", "updated every three months with about 35,000 SPX contracts and around $22 billion in value for each part"; the fund "buys a put spread below the market for downside protection and sells calls above the market to finance those puts". Vendor claims: "The JPM put strike consistently registers as the largest single-strike GEX concentration in the SPX options market"; "the market holds near the JP Morgan put strike through expiration — supported by dealer hedging flows — and then sells off meaningfully after the quarterly roll". Estimated Q3 2026 strikes: a 7,890 short call, a 7,090 long put and a 5,990 short put [social media estimate]. HMA Quant's Q1 2026 account: the dealer was "short the 6475 put", short gamma, so "Dealers consume liquidity instead of providing it", with "±200-point bursts within 30-minute windows"; SPX "closed Friday at 6,368", leaving the 6475 put "107 points ITM".
- Limits: no measured test; the "holds then sells off" pattern is a vendor's reading of past quarters. The Q1 2026 account is one quarter.
- Use in the book: the cleanest case of a known sign. The fund is long the upper put, so the dealer is short it: short gamma at that strike, an amplifier on a break, while charm and vanna decay of the same short put (dealers buying back hedges as the put loses delta) can support price above the strike while it is out of the money. One strike, two opposite stories depending on which side of it spot is and which Greek dominates: a worked example for Chapter 8C and Part D's expiration effects, and a caution against "largest node = support".

---

## Part D. How practitioners use the maps

### D1. Daily workflows, as vendors describe them

| Step | SpotGamma | Skylit | Others |
|---|---|---|---|
| Before the open | Read the Founder's Note: Call Wall, Put Wall, Zero Gamma, Volatility Trigger and implied move, published morning and evening; paste the "Daily Key Levels SPX" into TradingView (SpotGammaWorkflow) | Mark the King Node as the "EOD or EOW anchor"; note the nearest floor and ceiling and the Gatekeepers between spot and the King (SkylitReading) | MenthorQ levels drawn inside charting platforms (MenthorQLevels); GEXBot "majors" through platform plugins (GEXBot); Barchart's free pages (BarchartGEX) |
| Form a view | Levels frame "the expected price range for the day" | "Charts First": the thesis comes from price structure, then the map "supports it or kills it" (SkylitChartsFirst) | Bank notes frame the regime: "short gamma", "gamma neutral", volatility-control flows (NomuraMcElligott, Tier1Alpha) |
| During the session | Levels "hold for the trading session"; TRACE and HIRO show intraday flow against them (SpotGammaWorkflow, SpotGammaIntraday) | Watch the same-day column on indexes; Velocity Mode; node alerts; three confirmations (a nearby King or Gatekeeper, a "confirmation or rejection wick", SPX, SPY and QQQ agreeing) (SkylitModule, SkylitDocs) | GEXBot's one-second orderflow and 1- to 30-minute look-backs (GEXBot) |
| Into the close | (not stated) | "power hour liquidation can reshuffle maps entirely" (SkylitReviews) | The last 30 minutes carry measurable hedging flow in index futures (BaltussenDaLammersMartens2021) |

Two designs sit under these routines. SpotGamma fixes its levels for the session from overnight data and shows the day's flow in separate tools; Skylit lets its nodes move all day. Fixed levels can be logged and tested; moving nodes answer "what now" but leave no record of what a trader saw when acting, which is the look-ahead trap LuxAlgo warns about (LuxAlgoGEXCaution).

Both vendors frame the product as context, not a signal: "Heatseeker is contextual intelligence, not a trading signal" (SkylitDocs); levels "do not reveal every dealer's inventory or guarantee where price will turn" (LuxAlgoGEXCaution). The book's Edge tradition goes further and uses only the sign, as a sizing input worth "10% to 15% of one filter's weight" (Chapter 10H).

### D2. Levels as support, resistance and targets

- **The rules.** Call wall as resistance and put wall as support (SpotGammaLevels, MenthorQLevels); the King Node as the "primary destination target"; floors, ceilings and Gatekeepers (SkylitReading); the flip or "Volatility Trigger" as the regime line.
- **What the mechanics require** [derived here]. A strike damps a move toward it only if dealers are long gamma there, that is, long those options. If they are short them, hedging runs with the move and a break accelerates. The sign at a strike is exactly what open interest does not show (C2). SpotGamma's own wall explainers state the hedge direction backwards (SpotGammaLevels), and Skylit's floor is defined by size while its mechanics need a sign (Part A7). The one strike whose holder is public, the JPM collar's upper put, is a short-gamma strike for whoever sold it, typically dealers: an accelerator on a break, not a floor (JPMCollar).
- **How large the effects are.** Measured pinning in single stocks is at least 16.5 basis points per expiration (NiPearsonPoteshman2005); S&P 500 futures move at least $115 million of notional per expiration, toward the strike on some expiries and away from it on others (GolezJackwerth2012). These are real and small; none is a test of trading a named level intraday, and no such test was found.
- **Two kinds of "target".** A "magnet" in vendor language mixes two things: gamma-driven pinning near expiry, which the literature supports weakly, and a destination for the day or week, which it has not tested.

### D3. Expiration effects

- **Into expiration.** Near-the-money gamma rises and far out-of-the-money gamma falls (GoldmanFishman2020). The practitioner account of the "vanna and charm rally" is that dealers short out-of-the-money puts hold short-stock hedges and buy them back as the puts lose delta to time decay (charm) and to falling implied volatility (vanna) (KarsanWindowOfWeakness). The one academic study that fits this shape finds high returns in the option-expiration week for S&P 100 stocks and names the same two channels, "a reduction in short-stock hedge positions" and "declining risk perceptions" as implied volatility falls (StiversSun2013).
- **After expiration.** Expiring gamma "unclenches" the index (NomuraMcElligott), and the one to two weeks after monthly expiration are the "window of weakness" when the supportive flows are absent (KarsanWindowOfWeakness). The academic analogue is modest: fourth-Friday weeks "underperform modestly" for S&P 100 stocks (StiversSun2013). No test on SPX itself was found, and the direction of the whole account depends on dealers being short the decaying puts, the sign convention again.
- **Expiration day.** Pinning is measured in basis points (NiPearsonPoteshman2005, GolezJackwerth2012). Expiry reversals in Bitcoin are strongest when estimated dealer gamma is negative (Weiss2026). Not every expiry move is hedging: exercise of deep in-the-money calls and immediate sale of the stock drops prices by 0.8 percentage point in heavily affected single stocks (Chiang2014), a channel absent in cash-settled SPX.
- **Quarterly and dated flows.** The JPM collar resets every three months, about 35,000 SPX contracts per leg (JPMCollar); buffer ETFs reset on their own fixed dates (FLEXDefinedOutcome). Vendors claim the market "holds near the JP Morgan put strike through expiration" and "sells off meaningfully after the quarterly roll" [vendor claim, untested]; in the last week of the first quarter of 2026, SPX closed a Friday more than 100 points below that strike (JPMCollar).
- **VIX expiration.** Practitioners pair the monthly SPX expiration with the VIX expiration ("OPEX and VOLEX") (KarsanWindowOfWeakness). No source on VIX-settlement effects was searched for this file [gap].

### D4. Combining GEX with other data

| Combination | Who | Evidence on the combination |
|---|---|---|
| GEX with dark-pool short volume (DIX) | SqueezeMetrics (SqueezeMetricsDIX2018) | A popular test was retracted for a data error; the corrected advice is to normalize by volatility (ConfirmSignal2021) |
| GEX with the volatility term structure and volatility-control flows | Tier1 Alpha, Nomura (Tier1Alpha, NomuraMcElligott) | None published by them |
| GEX with VEX; a "VIX curl" to time pit reversals; three indices agreeing | Skylit (SkylitVEX, SkylitNegativeGEX, SkylitTrinity) | None published; VEX correlates +0.72 with the VIX and adds nothing after VIX and IV controls in one test (FlashAlphaBacktest2026) |
| GEX with an implied move and intraday flow | SpotGamma (SpotGammaWorkflow, SpotGammaIntraday) | None published |
| GEX sign as one light in a stack with VIX/VIX3M, realized against implied volatility, funding gauges and breadth | The book's Edge tradition (Chapter 10H) | The daily-horizon test above supports a small weight: most of GEX's link to next-day volatility is already in the VIX and at-the-money IV (FlashAlphaBacktest2026). At the half-hour horizon, public-OI gamma keeps information after HAR controls (ArdiaVaudescal2026) |

No test of GEX combined with breadth was found [gap].

### D5. Where practice agrees and where it splits

- **Agreement.** Every vendor whose guidance was seen, and the one vendor test, call the maps context rather than signals (SkylitDocs, SkylitChartsFirst, SpotGammaWorkflow, LuxAlgoGEXCaution, FlashAlphaBacktest2026).
- **Splits.** Fixed levels against moving nodes (SpotGamma against Skylit); size first (Skylit's Absolute Value Rule) against sign first (the mechanics and the literature); gamma for 0 to 5 days and vanna for 7 to 180 days (SkylitVEX) against a single aggregate; one sign rule for all products (Barchart) against per-product rules (SpotGamma) against measured signs (Cboe data).

### Part D sources

### KarsanWindowOfWeakness
- Citation: Karsan, C. (Kai Volatility Advisors), interviews and talks: Option Alpha, "Interview with Cem Karsan of Kai Volatility Advisors" (https://optionalpha.com/interviews/cem-karsan); "Cem Karsan On Volatility In A Window Of Weakness" (https://www.youtube.com/watch?v=BgEFb7Unafg); "Cem Karsan on Volatility & a Potential Weak Moment for Markets" (https://www.youtube.com/watch?v=D_p2Z3et81s); "Cem Karsan on Why Opex Week Is the Best Time to Sell Volatility" (https://www.youtube.com/watch?v=o8NMI3jpu3A); Top Traders Unplugged, "The Unpinning of Volatility & How to Prepare for What is Coming ft. Cem Karsan" (https://www.toptradersunplugged.com/podcast/the-unpinning-of-volatility-and-how-to-prepare-ft-cem-karsan/); Mutiny Fund, "Episode 24: Cem Karsan" (https://mutinyfund.com/cem-karsan/). Secondary accounts: Systematic Individual Investor, "How To VANNA" (November 5, 2020, https://systematicindividualinvestor.com/2020/11/05/how-to-vanna/) and "Tradable Effects of Options Market Liquidity Flows" (March 12, 2021, https://systematicindividualinvestor.com/2021/03/12/tradable-effects-of-options-market-liquidity-flows/); Investing.com, "S&P 500: Welcome to the Window of Weakness" (https://www.investing.com/analysis/sp-500-welcome-to-the-window-of-weakness-200641914); TradingView scripts "Charm + Vanna Window (Monthly OPEX)" (https://www.tradingview.com/script/mvEJiFm7-eksOr-Charm-Vanna-Window-Monthly-OPEX/) and "Index Options Expirations and Calendar Effects" (https://www.tradingview.com/script/1pxhsycN-Index-Options-Expirations-and-Calendar-Effects/).
- Type: practitioner commentary (a volatility fund manager's talks), with secondary retail write-ups and indicators
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). Nothing fetched. Who coined "window of weakness" is not established by these results; Karsan is the practitioner most associated with it, and one summary shows him saying "some people call it" that [origin unverified].
- Question: why the weeks after a monthly expiration behave differently from the weeks before it.
- Data and method: none published; a flow argument.
- Findings (as shown): dealers "are often buying back stock as risk premia decays (charm) and buying back stock as implied volatility compresses (vanna)", so into expiration these flows support the index. "After October expiration has passed, there's a window of non-strength some people call it a window of weakness—a period where flows have subsided." A secondary account: "The one to two weeks following the day of the monthly options expiration generally represents a short period whereby supportive Vanna and Charm flows that drive stocks higher under normal market conditions are much less prominent." A TradingView description ties the window to the calendar: after "OPEX and VOLEX" (the monthly SPX and VIX expirations) have "unpinned", with the quarterly JHEQX expiry still ahead. Karsan's related claim: OPEX week is "the best time to sell volatility".
- Limits: no published test by the originator. The mechanism needs dealers to be short the puts whose delta decays (so that decay makes them buy), which is the long-calls, short-puts convention; under the opposite sign the same decay makes them sell. The seasonal pattern, if any, has not been separated from other calendar effects (month-end flows, VIX expiration, the Fed calendar).
- Use in the book: the practitioner source of the "window of weakness" and "vanna and charm rally into expiry" ideas that Part D describes and Part E tests; a clean example of a claim whose direction depends entirely on the sign convention (Chapters 7B, 9A).

### StiversSun2013
- Citation: Stivers, C., and co-author [shown as "et al."; Sun, L., per common citation, unverified] (2013). "Returns and Option Activity over the Option-Expiration Week for S&P 100 Stocks." Journal of Banking and Finance [volume and pages unverified]. SSRN DOI 10.2139/ssrn.1571786. https://consensus.app/papers/details/ef9d378c9d985089bbb62e69ec34370e/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "Chris Stivers et al.", year, journal, DOI and abstract (query of 2026-09-30).
- Question: are returns different in the week of monthly option expiration for heavily optioned large stocks?
- Data and method: S&P 100 stocks; weekly returns in the week ending on the month's third Friday (the "OE week") against other weeks, other stocks with less option activity, and asset-pricing alphas.
- Findings: "the weekly returns over option-expiration (OE) weeks (a month's third-Friday week) tend to be high" relative to less-optioned stocks, the stock's own other weeks, and risk; "a month's fourth-Friday weekly returns underperform modestly". Two suggested contributors: "delta-hedge rebalancing by option market makers, with a reduction in short-stock hedge positions over the OE week", and "declining risk perceptions over the OE week, as measured by option-derived implied volatilities".
- Limits: single stocks in the S&P 100, the monthly-expiration era; the mechanisms are "likely partial contributors", not identified.
- Use in the book: the closest academic analogue of the practitioners' "rally into OPEX, weakness after" (KarsanWindowOfWeakness): the expiration-week strength and the modest weakness in the following week are documented; its two suggested channels are the charm-like unwinding of short-stock hedges and the vanna-like fall in implied volatility. It supports the pattern for large single stocks, not a trading rule for SPX (Part D, Part E).

### Chiang2014
- Citation: Chiang, C.-H. (2014). "Stock returns on option expiration dates: Price impact of liquidity trading." Journal of Empirical Finance [volume and pages unverified]. DOI 10.1016/j.jempfin.2014.03.003. https://consensus.app/papers/details/dbf20fc71a1a50eebf3b0bf43db28158/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, author, year, journal, DOI and abstract (query of 2026-09-30).
- Question: why do some stocks fall on expiration dates?
- Data and method: stocks sorted by the amount of deep in-the-money call open interest at expiration.
- Findings: "stocks with a sufficiently large amount of deeply in-the-money call options experience a significant return drop of 0.8 percentage point on option expiration dates; this price movement is then followed by a short-term reversal", attributed to "selling pressure from call option buyers who exercise deeply in-the-money calls and sell the acquired stocks immediately", which is "offset neither by parallel option writers' purchases nor by put option rebalancing".
- Limits: single stocks with physical delivery; SPX options settle in cash, so this channel does not apply to SPX itself.
- Use in the book: an expiration effect that is not dealer hedging at all, a reminder that not every expiration-day move is gamma (Part D); and a reason SPY, which settles by delivery, and SPX, which settles in cash, can behave differently at expiry. Related: Cao and co-authors (Management Science, 2020, DOI 10.1287/mnsc.2020.3803, https://consensus.app/papers/details/044ab7b7425e5bc3a403f455c5bd2306/) find "selling pressure from stocks delivered at option expiration" on the third Friday.

### GolezJackwerth2012
- Citation: Golez, B., and Jackwerth, J. (2012). "Pinning in the S&P 500 Futures." Journal of Financial Economics [volume and pages unverified]. DOI 10.1016/j.jfineco.2012.06.010. https://consensus.app/papers/details/79ed465239ea504e828a0b00e3462b1d/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "Benjamin Golez et al.", year, journal, DOI and abstract (query of 2026-09-30). The co-author's name is from this file's key [unverified here].
- Question: does option expiration pin the S&P 500 futures?
- Data and method: S&P 500 futures around the expirations of serial options on the futures and of SPX index options.
- Findings: futures "are pulled toward the at-the-money strike price on days when serial options on the S&P 500 futures expire (pinning) and are pushed away from the cost-of-carry adjusted at-the-money strike price right before the expiration of options on the S&P 500 index (anti-cross-pinning)"; the effects come from "market makers' rebalancing of delta hedges due to the time decay of those hedges as well as in response to reselling (and early exercise) of in-the-money options by individual investors"; "The associated shift in notional futures value is at least $115 million per expiration day."
- Limits: a pre-0DTE sample; the direction depends on which options expire and who holds them.
- Use in the book: at the index level, the expiry effect exists, is small, and can repel as well as attract. It is the measured backdrop to "the King Node is where price settles" (Part A6, Part E) and to charm-driven expiry flows (Part D): time decay of hedges is one of the two channels the paper names.

### Weiss2026
- Citation: Weiss, D., and co-authors [shown as "et al."] (2026). "Bitcoin option expiration, gamma exposure, and intraday price reversals." Finance Research Letters [volume and article number unverified]. DOI 10.1016/j.frl.2026.110340. https://consensus.app/papers/details/2e40fd2d230854c7a3bd30709703188f/
- Type: peer-reviewed article
- Verified via: Consensus result showing title, "Dustin Weiss et al.", year, journal, DOI and abstract (query of 2026-09-30).
- Question: do daily Deribit option expirations move Bitcoin's spot price?
- Data and method: intraday Bitcoin spot returns and trading around Deribit expirations, from spot exchanges and Deribit perpetual futures.
- Findings: "a statistically and economically significant return reversal around expiration"; the effect "concentrates on days with elevated at-the-money open interest and is strongest when cumulative gamma exposure is negative, which is consistent with positive feedback trading pressure induced by option market makers hedging net short exposure"; trading rises around expiry; implied "annual wealth transfers of approximately USD 50 million between option writers and holders".
- Limits: a different market, with one dominant venue and a settlement index built from a few spot exchanges; the gamma sign is estimated.
- Use in the book: an out-of-sample confirmation of the sign mechanics around expiry (Part A6, Part D): expiry effects are strongest when estimated dealer gamma is negative, the opposite of "the biggest node pins price regardless of sign".

### Willeboordse2026
- Citation: Willeboordse, F. H. (2026). "Does gamma survive the close?" Finance Research Letters [volume and article number unverified]. DOI 10.1016/j.frl.2026.110281. https://consensus.app/papers/details/e898787a6205536da8612750954bc698/ ; also https://www.sciencedirect.com/science/article/pii/S1544612326008093
- Type: peer-reviewed article
- Verified via: Consensus result showing title, author, year, journal, DOI and abstract; WebSearch result showing the ScienceDirect page (queries of 2026-09-30).
- Question: does Black-Scholes gamma identify the convexity actually earned in daily option returns?
- Data and method: "182 million intraday trade pairs and 0.16–2.6 million daily pairs per symbol across five underlyings (2020–2025)"; empirical gamma estimated from price changes and compared with model gamma.
- Findings: "The correlation between empirical and theoretical gamma does not improve from intraday to daily horizons—it turns significantly negative (−0.25 to −0.47 across symbols)"; the negative correlation "becomes more severe as vega exposure grows relative to gamma exposure"; the evidence "is most consistent with substantial vega contamination through negative spot–IV comovement (the leverage-effect channel)"; "The ½Γ_BS(ΔS)² term can be computed but does not isolate convexity exposure."
- Limits: a single-author letter; five underlyings (which ones not shown); about option returns, not hedging flows.
- Use in the book: a measurement critique of every GEX number (Part E): the Black-Scholes gamma that vendors multiply by open interest is not the convexity a position experiences over a day, because implied volatility moves against spot. It supports treating GEX and VEX together (Chapter 7B) and the minimum-variance delta point (HullWhite2017).

### SpotGammaWorkflow
- Citation: SpotGamma (n.d.). "Options Key Levels Explained" (https://spotgamma.com/options-key-levels-explained/); "Sharpen Your Skills — Starting the Day With SpotGamma" (https://spotgamma.com/sharpen-your-skills-starting-the-day-with-spotgamma-2/); "How to Use SpotGamma" course (https://spotgamma.com/courses/how-to-use-spotgamma/); "How do I upload to TradingView?" (https://support.spotgamma.com/hc/en-us/articles/1500006839001-How-do-I-upload-to-TradingView); "Key Trading Levels From SpotGamma" (https://spotgamma.com/key-trading-levels-from-spotgamma/); Founder's Note archive (https://spotgamma.com/category/daily-note/page/2/).
- Type: vendor documentation (user guidance)
- Verified via: WebSearch titles and summaries (query of 2026-09-30). Not fetched.
- Question: how a leading vendor tells users to run a trading day with its levels.
- Data and method: none; a workflow.
- Findings (as shown): "The main SpotGamma key levels are the Call Wall, Put Wall, and the Volatility Trigger. Each level marks a different type of hedging behavior in the underlying, or the expected price range price for the day." The daily Founder's Note "publishes the Call Wall, Put Wall, Zero Gamma, Volatility Trigger, and the implied move for the major indices each morning and evening, with context on how positioning has shifted." Morning routine: open the portal's "Daily Key Levels SPX" pop-up and copy the levels into TradingView. "SpotGamma sets the published key levels daily, and they hold for the trading session. The model recalculates them for the next session as new positioning data comes in, rather than moving around during the day. TRACE shows how price is interacting with them in real time as new flow and same-day trades come in, so you can see whether a level is being defended or tested."
- Limits: guidance, not evidence.
- Use in the book: the other design choice for Part D and Part F. SpotGamma fixes its levels for the session from the overnight data and shows intraday flow separately (TRACE, HIRO); Skylit lets its nodes move all day. The first keeps levels stable and testable; the second is more responsive and far harder to test, because the level a trader acted on may no longer be on the map.

---

## Part E. Critiques

### E1. Academic critiques

No academic paper found tests trading a named GEX level (a wall, a flip, a King Node) as support, resistance or target. The academic literature bears on the maps in four other ways:

1. **The sign is assumed, and often wrong.** "Because Black-Scholes gamma is identical and positive for calls and puts at the same strike, the sign in any GEX aggregate is an inventory assumption", and a mislabeled term "can silently invert the entire regime" (Chilingarian2026). CBOE data showed equity investors net short both calls and puts, so market makers long both (LakonishokLeePearsonPoteshman2004). In SPX 0DTE, measured market-maker gamma is "on average positive" (DimErakerVilkov2024), and market makers "match most 0DTE order flows" (AdamsFontaineOrnthanalai2024). The long-calls, short-puts convention paints put-heavy strikes as short gamma, the opposite of these measurements.
2. **The inputs are noisy.** Standard rules sign 17% to 41% of option trades wrongly, and index complex-order legs about half the time (SavickasWilson2003); the liquidity taker is often a professional timing its execution, not a customer facing a hedging dealer (MuravyevPearson2020); public open interest tracks dealer inventory at a correlation of only 0.53 for 0DTE (ArdiaVaudescal2026).
3. **The model may not describe the hedge.** Market makers appear to hedge selectively, with negligible footprints from multi-leg trades (Dong2025); the variance-minimizing delta already folds in the average volatility response to a price move (HullWhite2017); and Black-Scholes gamma correlates negatively (−0.25 to −0.47) with the convexity positions actually earn at a daily horizon, because implied volatility moves against spot (Willeboordse2026).
4. **The effects are real but small, and sign-dependent.** Negative gamma goes with momentum and positive with reversal, conditional on illiquidity (BarbonBuraschi2020, BaltussenDaLammersMartens2021, Weiss2026); market-maker 0DTE gamma damps on average, and at its worst adds at most 3.3 points of annualized volatility (AmayaGarciaAresPearsonVasquez2025); pinning is basis points per expiry (NiPearsonPoteshman2005, GolezJackwerth2012). One dissent: 0DTE trading raises volatility, "primarily driven by speculative retail investors", even after controlling for market-maker gamma hedging (BrogaardHanWon2026). None of these supports "the largest node, whatever its sign, is where price goes".

### E2. The Edge Book's view (Chapters 10H and 10I), checked against this search

| The Edge Book says | What this search found | Status |
|---|---|---|
| Use the sign of GEX only as low-confidence regime context, "10% to 15% of one filter's weight"; "Do not size on the magnitude of GEX" | At the daily horizon, GEX's link to next-day realized volatility falls from −0.36 to −0.03 after VIX and IV controls (FlashAlphaBacktest2026); SpotGamma's own randomization test shows the model's total moving with the share of positions it gets right (SpotGammaDDOI) | Supported |
| "Public GEX models are model-dependent": vendors differ on who is long and short | Vendors' stated rules differ by product and from one another (SpotGammaDDOI, BarchartGEX, UnusualWhalesGEX, VollandDeLorenzo2023); one vendor calls the standard convention right "maybe ±75% of the time" (WizardOfOps2026) | Supported |
| The 0DTE explosion changed the structure; "more than 40% of SPX volume in 0DTE options, on the Edge Book's count" | 0DTE is 48% of index option trading by August 2023 (BrogaardHanWon2026); almost 2 million SPX 0DTE contracts a day by 2025 (Cboe0DTEsDecoded2025) | Supported (the 40% is the book's own count) |
| "A Cboe study of 2025 estimates 0DTE market-maker hedging at about 0.2% of SPX daily liquidity" | Confirmed: "at best, just 0.2% of the SPX daily liquidity", Xu, May 2, 2025 (Cboe0DTEsDecoded2025) | Supported, with a scope note: the figure is for 0DTE hedging; the walls most maps draw come mostly from longer-dated open interest, so "level effects it creates are small" is an extrapolation from 0DTE to all levels |
| "Specific rules for trading levels are not validated in the academic literature" | No academic test of level trading was found in this search either | Supported (absence of evidence) |
| Open-interest concentrations are "descriptive, not predictive" | Aggregate public-OI gamma does predict next-half-hour variance for non-0DTE options (ArdiaVaudescal2026), and changes in GEX may predict returns (HarbourfrontGEXReturns, second-hand) | Partly contradicted for the aggregate at short horizons; untested for single strikes |
| Chapter 8A (the Lab): the standard formula "was adopted in some form by every later vendor, including SpotGamma, Tier1Alpha and Cboe's own derivative dashboards" | SpotGamma uses a per-1% form with its own sign rules; Tier1 Alpha's method is unpublished; no Cboe dashboard applying the formula was found; Cboe's research measures signs from its own data | Not confirmed; revise |

### E3. Cboe's statements and the replies

- **Cboe's position.** Customer 0DTE flow is balanced, so net market-maker gamma is small: "$170mm to $670mm throughout the day", hedging "between 0.04% to 0.17% of the daily S&P futures liquidity" (CboeXu2023), later "at best, just 0.2%" (Cboe0DTEsDecoded2025). Its best single illustration: over 100,000 contracts of one put traded in a day and market makers ended short about 3,000. Its best single sentence: "what matters ... is the balance of the volume between buys vs. sells, not the notional size".
- **Replies.** JPMorgan's "Volmageddon 2.0" warning was a scenario of one-sided positioning under thin liquidity, not a measurement (JPMorganKolanovic2023); Bank of America called it "overblown". SpotGamma argues that flows "do not drive all stocks all of the time, when they do they can dominate", a claim about tails that its proprietary model cannot show against Cboe's data (SpotGammaOnCboe2023).
- **Caveats on Cboe's side.** The data are Cboe's own market-maker flags, so dealers trading as broker-dealers, hedges in SPY or futures options, and OTC books are outside them (CboeOpenClose); Cboe sells 0DTE volume; and whether the measure includes positions opened before the day that become 0DTE, which Adams and co-authors identify as the source of most dealer 0DTE gamma, is not stated in the summaries [unverified]. The academic studies with independent authors reach the same sign and a similar size (DimErakerVilkov2024, AdamsFontaineOrnthanalai2024, AmayaGarciaAresPearsonVasquez2025).

### E4. Practitioners who tested the tools and found them wanting

- **FlashAlpha**, testing its own product over 1,972 SPY days: GEX "works raw" but adds little after VIX and at-the-money IV controls; VEX "is mostly a VIX proxy" (FlashAlphaBacktest2026).
- **Confirm Signal**: the most-read test of SqueezeMetrics' GEX and DIX had a "fatal data error" and "positive" results that were retracted; the corrected advice is to normalize by volatility (ConfirmSignal2021).
- **Skylit's own users** (third-party reviews): the tool is "wrong as much as it is right" when used as a directional signal; "~50% win rates" for users who treat large nodes as buy signals [third party, no data] (SkylitReviews). Skylit's own Limitations page: "Not 100% Accurate", "Map Reshuffles", "Low volume periods can skew heatmap efficacy" (SkylitDocs).
- **HMA Quant** on the JPM collar in the first quarter of 2026: the strike sold as support was a dealer short-gamma strike, with "±200-point bursts within 30-minute windows" and a Friday close more than 100 points through it (JPMCollar).
- **Vendors on one another**: Volland's creator calls the open-interest convention "right maybe ±75% of the time" and quote-side classification wrong in "way too many common scenarios" (WizardOfOps2026); a Liverpool working paper notes that commercial services "disclose little of their methodology" (Sen2026).
- **Method warnings**: do not backtest today's levels "as though they were known then" (LuxAlgoGEXCaution).
- **Counterweights**: public-OI gamma predicts next-half-hour variance (ArdiaVaudescal2026); changes in GEX may predict returns (HarbourfrontGEXReturns). Both concern the aggregate, not named strikes.
- **Gap**: no critique by a named, independent volatility practitioner (for example Benn Eifert or Kris Abdelmessih) was found in search summaries; a Moontower post appeared as a title only [unverified content].

### E5. Claims, critiques and status at a glance

| Claim (who) | Critique | Status |
|---|---|---|
| Walls are support and resistance (SpotGamma, MenthorQ) | Requires dealers long gamma at the strike; the sign is assumed; SpotGamma's explainers state the hedge direction backwards | Mechanism conditional on sign; no test of trading found |
| The largest node, whatever its sign, is the target (Skylit) | Sign sets the direction of hedging; measured effects are sign-dependent | Contradicted in mechanism; untested as a rule |
| 0DTE dealer hedging drives the day (retail maps; JPMorgan scenario) | Cboe: at best 0.2% of liquidity; academic studies: market-maker 0DTE gamma positive on average and damping | Contradicted in size and sign on average; tails disputed |
| GEX predicts next-day volatility (vendors) | Mostly the VIX's and implied volatility's information | Weak once controlled |
| Intraday nodes show new positioning (Skylit Velocity, flow maps) | Greek drift alone moves nodes; classification errors; 0DTE proxies track inventory poorly | Unseparated; noisiest input |
| Rally into OPEX, weakness after (Karsan) | Academic analogue in S&P 100 stocks; direction depends on sign; no SPX test | Partly supported for single stocks; untested for SPX |

### Part E sources

### FlashAlphaBacktest2026
- Citation: FlashAlpha (2026). "GEX Backtest: 8 Years of SPY Show Gamma Exposure Mostly Tracks ..." https://flashalpha.com/articles/gex-dex-vex-chex-8-year-backtest-spy-vix-control ; the same study by its author, Dobrowolski, T., "I Backtested My Own GEX Product Across 8 Years of SPY. Most of It Is Just VIX", dev.to, https://dev.to/tomasz_dobrowolski_35d32c/i-backtested-my-own-gex-product-across-8-years-of-spy-most-of-it-is-just-vix-a53 ; related, "Quantifying Dealer Positioning with GEX, VEX, and CHEX — A Developer's Guide", https://dev.to/tomasz_dobrowolski_35d32c/quantifying-dealer-positioning-with-gex-vex-and-chex-a-developers-guide-318n
- Type: vendor research (a GEX data vendor testing its own product), self-described as pre-registered
- Verified via: WebSearch titles and summaries (query of 2026-09-30). flashalpha.com and dev.to blocked for fetching, so the sign convention, the pre-registration document and any level tests were not seen [unverified]. Year 2026 from the stated sample end.
- Question: do GEX, DEX, VEX and CHEX predict next-day realized volatility beyond what the VIX and implied volatility already say?
- Data and method: "a pre-registered backtest on 1,972 SPY days (2018-2026)"; correlations of each exposure with next-day realized volatility, raw and after controlling for the VIX and at-the-money implied volatility.
- Findings: GEX's correlation with next-day realized volatility is −0.36 raw, −0.14 after the VIX control, and −0.03 (p = 0.18) after the VIX and at-the-money IV controls. VEX correlates +0.72 with the VIX and +0.76 with at-the-money IV; residualized, ρ = −0.01 (p = 0.77). Conclusion: "GEX should be used as a regime label, not a standalone forecast"; the exposures "add little after VIX and ATM IV controls".
- Limits: one vendor's own construction on SPY, daily horizon only; an intraday or level-based test would be a different question (ArdiaVaudescal2026 finds information at the half-hour horizon). Pre-registration is claimed, not seen.
- Use in the book: the clearest practitioner test that sets GEX against the obvious alternative, the implied volatility the options already price. At the daily horizon the sign's information is mostly the VIX's (Part E); this supports the Edge Book's "low-confidence regime context" weighting (Chapter 10H).

### ConfirmSignal2021
- Citation: Confirm Signal (Substack) (2021). "Testing SqueezeMetrics GEX and DIX Indices", September 25, 2021, https://confirmsignal.substack.com/p/testing-squeezemetrics-gex-and-dix ; revisited in a post of July 8, 2024 on the same Substack (title not shown). Related practitioner pages seen as titles only: "Research - Predict the Market With the Dark Index and Gamma Exposure" (https://www.financetldr.com/p/research-dark-index-and-gamma-exposure), "GEX : GCBT - Good Coder Bad Trader" (https://goodcoderbadtrader.com/gex).
- Type: practitioner blog test
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). Not fetched. The two summaries disagree on what the corrected analysis concluded [unverified].
- Question: do SqueezeMetrics' GEX and DIX predict S&P 500 returns?
- Data and method: SqueezeMetrics' published GEX and DIX series against subsequent S&P 500 returns.
- Findings (as shown): the 2021 post "contained an error", with an edit note: "my analysis and conclusions below are wrong"; it "had a fatal data error". The 2024 post says the original "got more engagement than anything else written, probably because it contains 'positive' results", fixes the data pipeline, and recommends looking at DIX "on a one-month timeframe" and normalizing it "using realized volatility, one-month ATM IV, or VIX". One summary says the corrected results appeared to support SqueezeMetrics' intuition; the other does not say.
- Limits: a blog; the corrected numbers were not seen.
- Use in the book: a cautionary tale for Part E. The most-read practitioner test of the original GEX index was the one with a data error and "positive" results; the correction drew less attention; and the corrected advice, normalize by volatility, points the same way as FlashAlphaBacktest2026. Correction to this file: the SqueezeMetricsDIX2018 entry says the test "first found no signal, then retracted that finding"; the summaries seen here say the retracted 2021 results were the "positive" ones.

### HarbourfrontGEXReturns
- Citation: Harbourfront Quant (Substack) (n.d.). "Gamma Exposure and S&P500 Return Predictability." https://harbourfrontquant.substack.com/p/gamma-exposure-and-s-and-p500-return . Related posts: "The Rise of 0DTE Options: Cause for Concern or Business as Usual?" (https://harbourfrontquant.substack.com/p/the-rise-of-0dte-options-cause-for), "Reflexivity and the Dynamics of Option Markets" (https://harbourfrontquant.substack.com/p/reflexivity-and-the-dynamics-of-option).
- Type: practitioner research summary (it appears to summarize a study by other authors, who are not named in the search summary [unverified])
- Verified via: WebSearch title and summary (query of 2026-09-30). Not fetched; the underlying study, its data and its GEX construction were not seen.
- Question: do changes in GEX predict S&P 500 returns?
- Data and method: an autoregressive distributed lag (ARDL) model of S&P 500 returns with GEX, compared with a model without GEX and a random walk; out-of-sample Diebold-Mariano tests; subperiods before and after 2020.
- Findings (as shown): "Variations in the derivative of GEX have a statistically significant relationship with subsequent returns on the S&P 500", robust before and after 2020 "though somewhat diminished in the latter period"; price effects "persist beyond intraday horizons and into the following trading days"; adding GEX "significantly enhances the model's forecasting performance relative to both a GEX-excluding specification and a random walk benchmark".
- Limits: second-hand; no VIX or implied-volatility control is mentioned, which is the control that removed most of GEX's information in FlashAlphaBacktest2026; changes in GEX, not levels or walls, are the predictor.
- Use in the book: the counterweight in Part E: not every test finds nothing. Where GEX shows information, it is in changes and in the aggregate, not in named strikes, and it must survive the volatility controls before it counts as new.

### BrogaardHanWon2026
- Citation: Brogaard, J., Han, J., and Won, P. [first names and initials of the second and third authors not shown; unverified] (2023; revised January 21, 2026). "Does 0DTE Options Trading Increase Volatility?" SSRN working paper 4426358, first posted April 22, 2023. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426358 ; an earlier title, "How Does Zero-Day-To-Expiry Options Trading Affect the Volatility of Underlying Assets", https://www.researchgate.net/publication/370319866_How_Does_Zero-Day-To-Expiry_Options_Trading_Affect_the_Volatility_of_Underlying_Assets
- Type: working paper (SSRN, revision of January 2026)
- Verified via: WebSearch result showing the title, "Brogaard, Han, and Won", SSRN number, dates and abstract text (query of 2026-09-30). Not fetched.
- Question: does 0DTE trading raise index volatility?
- Data and method: index 0DTE volume from January 2011 to August 2023; "the staggered introduction of index weekly options as an instrument variable".
- Findings: monthly index 0DTE volume rose "from 0.08 million contracts in January 2011 to 34.4 million contracts in August 2023" and "now accounts for 48% of the trading in index options"; "a one standard deviation increase in 0DTE options trading leads to a 9.10% increase relative to the mean value of volatility, which is 15.91% of its standard deviation"; "Even after controlling for option market makers' gamma hedging, ... the overall impact on volatility remains positive and is primarily driven by speculative retail investors."
- Limits: a working paper; volume, not dealer positions, is the treatment; the instrument (weekly listings) may affect volatility through channels other than 0DTE.
- Use in the book: the academic dissent in Part E. The papers that measure market-maker gamma find it damps (DimErakerVilkov2024, AdamsFontaineOrnthanalai2024, AmayaGarciaAresPearsonVasquez2025); this one finds 0DTE trading raises volatility through speculation, not through dealer hedging. Both can hold: the dealer channel can be small and stabilizing while the trading itself adds volatility, which is the opposite of the story most heatmaps tell.

### LuxAlgoGEXCaution
- Citation: LuxAlgo (n.d.). "SpotGamma Levels: Interpreting Dealer Positioning" (https://www.luxalgo.com/blog/spotgamma-levels-reveal-dealer-positioning/) and "Gamma Exposure: Breadth, Sentiment & External Data Concept" (https://www.luxalgo.com/library/concept/gamma-exposure/).
- Type: vendor education pages (a charting-indicator vendor)
- Verified via: WebSearch titles and summaries (two queries, 2026-09-30). Which of the two pages carries each sentence is not clear from the summaries [unverified]. Not fetched.
- Question: how to test gamma levels honestly.
- Findings (as shown): "Do not backtest today's gamma levels across earlier dates as though they were known then. A valid historical gamma study needs timestamped historical levels, their update times, and a supported way to align that data with the price series." GEX levels "are useful inputs to a trading plan, but they do not reveal every dealer's inventory or guarantee where price will turn"; "High gamma does not guarantee pinning"; GEX "describes market structure and volatility sensitivity—not the market's next direction".
- Limits: advice, not a test.
- Use in the book: the look-ahead trap in any level study (Part E), sharpest for intraday maps whose nodes move: a fair test needs the map as it stood at each moment, which vendors that let nodes move all day rarely archive. Pairs with Chapter 10A's testing discipline.

### SpotGammaOnCboe2023
- Citation: SpotGamma (2023). "Analysis: The CBOE 0DTE Report." https://spotgamma.com/cboe-0dte/ ; with a video, "CBOE's 0DTE Gamma Paper" (https://www.youtube.com/watch?v=ng6jeLRCrz0), and a third-party summary, "Summary and Analysis of CBOE report on 0DTE options trading" (https://docmcgraw.substack.com/p/summary-and-analysis-of-cboe-report).
- Type: vendor commentary
- Verified via: WebSearch titles and summary (query of 2026-09-30). Not fetched. The year is inferred from the report it answers (CboeXu2023) [unverified].
- Question: is Cboe right that 0DTE market-maker hedging has "de minimis" impact?
- Findings (as shown): SpotGamma's position "contradicts this view, arguing that while options flows, including 0DTE, do not drive all stocks all of the time, when they do they can dominate"; it points to TRACE, which "adds its proprietary Options Inventory Model and intraday trade data, including 0DTE activity, to estimate how positioning changes during the session".
- Limits: a vendor whose product depends on the opposite conclusion; its inventory model is proprietary, so its disagreement cannot be checked against Cboe's data.
- Use in the book: the vendor side of the Cboe debate in Part E, stated fairly: the dispute is over the tail (days when flows dominate), not the average, which Cboe and the academic studies measure.

---

## Part F. The heatmap's design, for a figure-builder

Sources: Part A (Skylit's display, as described in its own pages), SpotGammaIntraday (TRACE), GEXBot, and the book's figure `/home/user/library/books/the-other-end-of-the-trade/figures/gex-heatmap.html` (read on 2026-09-30).

### F1. Skylit's display, element by element

| Element | Skylit | Note for a builder |
|---|---|---|
| Rows | Strikes | Sort high strikes at the top, so up on the page is up in price |
| Columns | Expirations: "the current expiration, next week, two weeks out, or later periods"; the same strike "can look different depending on the expiration selected" | Label days to expiry; keep the same-day column first |
| Cell | "a value (positive or negative)" per strike and expiry, shown as a number in the cell | Units are not stated by Skylit; a figure must state them |
| Color | Positive "green to yellow", negative "blue to purple"; bright yellow "Pika", dark purple "Barney" | Vendors disagree on color meaning: SpotGamma TRACE uses purple for positive gamma and red for negative, the reverse of Skylit's purple. Use hue for sign with a legend that says what the sign does, and lightness for size |
| Ranking | King Node = largest absolute value on the board (one page says largest positive); floor = largest node below spot; ceiling = largest above; Gatekeeper = a node between spot and a larger target; Pika Cloud = a cluster of positive nodes; air pocket = a run of weak nodes | Every one of these depends on the scale, the expiries included and, for "support", the sign |
| Marks | King starred; strike nearest price highlighted | |
| Filters | Number of expirations shown; number of nodes shown; GEX or VEX; current against expanded expirations | The expiry filter can move the King from one column to another |
| Time | Live updates (1-second claim); Velocity Mode over 1 minute to 1 day; "Increasing and Decreasing" filters; node lifecycle (fresh, tested, delivered, decaying) | Node growth mixes Greek drift and inferred flow (Part C1) |
| Other | Trinity Mode (SPX, SPY and QQQ side by side); node alerts | |

### F2. What the book's figure already does

The figure draws a made-up SPX chain: strikes every 25 points from 5,700 to 6,300 (labeled every 100) against ten expiries (0, 1, 2, 3, 4, 7, 14, 21, 30 and 45 days). Each cell is \(\Gamma \cdot OI \cdot 100 \cdot S^2 \cdot 0.01\) signed by the chosen convention, in dollars of delta per 1% move; the VEX view is dollars of dealer delta per volatility point. Green marks cells where hedging opposes a move and rose where it joins one; depth scales with the cell's size against the largest cell, on the whole map or per expiry. A right panel sums each strike across all expiries. Rings number the three largest cells. A dashed line marks the gamma flip nearest spot, a solid line marks spot. Controls: spot (5,850 to 6,150), IV (8% to 40%), hours to the close (0.25 to 6.5), sign convention (Chapter 8A's "JPM-era" and "0DTE-era"), cells (GEX, size only, VEX) and color scale (whole map, each expiry). Readouts: total GEX (or size, or VEX), the largest cell, the same-day share of size, and the flip. Open interest is fixed at a spot of 6,000.

### F3. What the figure shows that Skylit does not

1. **The sign convention switch.** Every color flips while the rings stay where they are, so the reader sees that a map read by size alone cannot say which way dealers will trade. This is the direct test of Skylit's Absolute Value Rule, and Skylit publishes no convention at all.
2. **Stated units**: dollars per 1% move for GEX, dollars per volatility point for VEX.
3. **Greek drift at fixed positions.** The IV and hours-to-close sliders change every node with open interest held fixed, which is the confound inside Skylit's "Growth equals intent" and Velocity Mode (Part C1).
4. **Aggregates**: the cross-expiry strike profile, the total and the flip, which Skylit's per-expiry grid does not show.
5. **Normalization as a choice**: "whole map" against "each expiry" shows that "a big node" is big only relative to the chosen maximum.
6. **"Size only"**: the view Skylit's rule asks for, set beside the signed view.

### F4. What Skylit's display has that the figure lacks, ranked by what it would teach

1. **A strike-by-time view of one expiry through the day** (Skylit's live grid over time; SpotGamma TRACE's strike-by-time map). Draw the same-day expiry with strikes on the vertical axis and the session's clock on the horizontal axis, and fill it in three layers the reader can switch on one at a time: (a) Greek drift with open interest fixed, (b) a synthetic intraday tape that adds positions, signed with a classification error rate the reader sets (17% to 41%, SavickasWilson2003), and (c) the overnight reset to "true" positions. A readout splits each node's change into drift and flow. It teaches Part C in one picture: most of what a live map shows moving near the money late in the day is time, not new positions (\(1/\sqrt{\tau}\): about 2.5 times from the open to the last hour).
2. **Node lifecycle and velocity.** Mark each node as growing or shrinking over a look-back the reader sets (Skylit's increasing and decreasing filters). With the tape switched off, near-spot same-day nodes still "grow" and far nodes "decay", which falsifies "Growth equals intent" in the reader's hands.
3. **Skylit's named roles, computed by its own definitions.** Label the King (largest absolute value), the strongest floor and ceiling (largest node below and above spot) and a Gatekeeper (the largest node between spot and the King), with values in the cells, and shade air pockets (strikes whose summed absolute value falls below a threshold the reader sets). Then let the convention switch turn a "floor" into an accelerator and the expiry filter move the King between columns. It shows how much of the vocabulary is an artifact of scale, expiry set and assumed sign.
4. **An expiry filter** ("number of expirations shown"; "current versus expanded"). It teaches Skylit's own warning that "A major node several expirations out may not be a major node for the current expiration", and how the King jumps when the same-day column is dropped.
5. **VEX nodes with a volatility shock.** The figure already draws VEX cells but not the flow they imply. Add a change in implied volatility (in points) and show each strike's implied dealer trade, VEX times the change, next to the GEX trade for a spot move: Skylit's "GEX governs the range; VEX governs the drift" made computable, with a caption caution that dealers hedging with a minimum-variance delta already include part of this (HullWhite2017).
6. **A measured-sign option.** Add a third choice beside the two conventions: dealer shares of call and put open interest set by the reader (Chapter 8A's sensitivity-map idea), with a preset matching the measured finding that market makers are net long 0DTE gamma on average (DimErakerVilkov2024). It teaches that the two named conventions are both assumptions and that measurement exists for SPX.
7. **Trinity** (SPX, SPY and QQQ side by side) teaches less per unit of screen: the three books share holders, and SPY's flow is shaped by internalization (Chapter 2B). Lowest priority.

The pinning dynamics on expiration day already have their own figure (`figures/node-pin-sim.html`); cross-link rather than duplicate.

### F5. Specification list for an interactive version built from a synthetic chain

- **Data.** Strikes \(K_i\) on a 25-point grid; expiries \(T_j\) including a same-day column; call and put open interest per strike and expiry, made up and seeded; optional per-strike implied volatility (a skew) rather than one flat volatility, since the flat assumption understates put-wing gamma (Sen2026 uses per-strike IV). Dealer net contracts \(n_{ij} = s_c \cdot OI^{call}_{ij} + s_p \cdot OI^{put}_{ij}\), with \(s_c, s_p\) from the chosen convention or from reader-set shares.
- **Cell values.** GEX: \(n_{ij}\,\Gamma(S, K_i, T_j, \sigma_{ij}) \cdot 100 \cdot S^2 \cdot 0.01\), dollars per 1% move. VEX: \(n_{ij} \cdot \text{vanna} \cdot 100 \cdot S \cdot 0.01\), dollars of delta per volatility point. Optional charm: dollars of delta per day.
- **Axes.** Strike vertical, high at the top, labeled every 100 points; expiry horizontal, near to far, labeled in days; spot as a solid line, the flip as a dashed line. A second mode for one expiry: strike against time of day.
- **Color.** Diverging, one hue per sign, lightness by \((|x|/\max)^{0.6}\), near-neutral at zero; the legend states the hedge ("dealers long gamma: hedging opposes moves"; "short gamma: hedging joins moves"), not just "positive" and "negative"; theme colors only, colorblind-safe; avoid a vendor's palette, since vendors assign purple to opposite signs.
- **Scale.** Three choices: whole map, each expiry, and a fixed absolute scale in billions of dollars per 1% move, so the reader can compare cells with a market yardstick (for example the E-mini equivalents of C5).
- **Ranking and labels.** Top-N cells by absolute value, numbered; the King as number 1; floor, ceiling and Gatekeeper by Skylit's definitions; cell values in billions with sign; a tap or hover readout per cell: strike, expiry, call and put open interest, the sign assumption, GEX and VEX.
- **Aggregates.** Cross-expiry profile per strike, total GEX, the flip, the same-day share of size.
- **Reader controls (two to five at a time, per the book's figure rules).** Spot; implied volatility; hours to the close; sign convention (two presets and reader-set shares); view (GEX, VEX, size only); color scale; expiries included; number of labeled nodes; the synthetic tape on or off with its classification error; a new-seed button.
- **Readouts.** Total GEX per 1%, per point and in E-mini contracts per 1% (C5); the flip; the King's strike and expiry; floor and ceiling; the same-day share of size; in the time view, the share of node change from drift against flow.
- **Caption.** Says the chain is made up, the sign is assumed (or set by the reader), the units, and what to try: switch the convention and watch floors become accelerators; run the clock with the tape off and watch nodes "grow".

---

## Synthesis (whole file)

### S1. What the literature and practice agree on

1. **The sign mechanics are real.** Dealers long gamma trade against moves and dealers short gamma trade with them, and the aggregate shows in prices: momentum with negative gamma and reversal with positive gamma, conditional on illiquidity (BarbonBuraschi2020, BaltussenDaLammersMartens2021); market-maker 0DTE gamma that is positive on average goes with lower intraday volatility and more reversal (DimErakerVilkov2024); expiry reversals are strongest when gamma is negative (Weiss2026); in foreign exchange, rebuilt dealer gamma moves spot volatility (Anderegg2022).
2. **Public data do not show the sign.** Open interest is a count without sides, published the morning after (OCCOpenInterest). Every vendor fills the gap with a rule or a model, and the rules differ by vendor and by product (SpotGammaDDOI, BarchartGEX, UnusualWhalesGEX, VollandDeLorenzo2023, Chilingarian2026).
3. **Where the sign is measured, SPX 0DTE market makers are net long gamma on average, and their hedging is small.** Cboe: "at best, just 0.2%" of SPX daily liquidity (Cboe0DTEsDecoded2025); academics with independent data: positive on average (DimErakerVilkov2024), volatility 60 to 90 annualized basis points lower on 0DTE days (AdamsFontaineOrnthanalai2024), at most 3.3 points of annualized volatility on the worst days (AmayaGarciaAresPearsonVasquez2025).
4. **Expiry effects exist and are small.** At least 16.5 basis points per expiration in single stocks (NiPearsonPoteshman2005); at least $115 million of futures notional per expiration, toward or away from the strike (GolezJackwerth2012).
5. **Everyone says "context, not a signal".** Skylit ("contextual intelligence, not a trading signal"), SpotGamma, LuxAlgo, FlashAlpha's own test, and both of the book's traditions (SkylitDocs, SkylitChartsFirst, SpotGammaWorkflow, LuxAlgoGEXCaution, FlashAlphaBacktest2026; Chapters 10H, 10I).
6. **Vendors disclose little.** Commercial services "disclose little of their methodology" (Sen2026); Skylit publishes no formula, sign rule, units or classification method (Part A4).

### S2. Where they disagree

| Question | One side | Other side |
|---|---|---|
| Does size or sign decide what a node does? | Size: the Absolute Value Rule, King by absolute value (SkylitIntroGamma, SkylitReading) | Sign: hedging direction flips with it; measured effects are sign-dependent (BarbonBuraschi2020, Weiss2026); the figure's convention switch shows it |
| Does 0DTE trading destabilize the index? | Scenario risk (JPMorganKolanovic2023); "when they do they can dominate" (SpotGammaOnCboe2023); 0DTE trading raises volatility through speculation (BrogaardHanWon2026) | Market-maker hedging is small and damps on average (CboeXu2023, Cboe0DTEsDecoded2025, DimErakerVilkov2024, AdamsFontaineOrnthanalai2024, AmayaGarciaAresPearsonVasquez2025) |
| Which way are dealers positioned in single-stock options? | Short both calls and puts (SpotGamma's working assumption, SpotGammaDDOI) | Long both, from CBOE data for 1990 to 2001 (LakonishokLeePearsonPoteshman2004); calls long, puts short (BarchartGEX, SqueezeMetricsGEX) |
| Does open-interest gamma predict anything? | "Descriptive, not predictive" (Chapter 10H); adds little to the VIX at the daily horizon (FlashAlphaBacktest2026) | Predicts next-half-hour variance for non-0DTE options (ArdiaVaudescal2026); changes in GEX predict returns (HarbourfrontGEXReturns, second-hand) |
| Should levels move during the day? | Fixed for the session, flow shown separately (SpotGammaWorkflow) | Live nodes, velocity and lifecycle (SkylitModule, SkylitNodeLifecycle) |
| Does the dealer hedge the model delta mechanically? | "dealer hedging is mechanical and non-discretionary" (SkylitDealerPositioning) | Selective hedging (Dong2025); minimum-variance deltas (HullWhite2017); model gamma misstates daily convexity (Willeboordse2026) |
| Is the index gamma flip SpotGamma's Volatility Trigger? | The book's Chapter 8A treats them as one | SpotGamma defines two levels (SpotGammaLevels) |

### S3. Untested or only claimed

- **Skylit**: fresh nodes react "~80%" of the time; "85-90%" accuracy in the founder's use; the King as the day's or week's settle; Gatekeepers; Rug, Reverse Rug, Beach Ball and pit patterns; velocity plus air pocket as "highest-conviction"; Trinity agreement as "high-probability"; gamma dominant at 0 to 5 DTE and vanna at 7 to 180 DTE (Part A5, A6).
- **SpotGamma**: walls as range bounds; the Volatility Trigger as "most actionable"; the Hedge Wall as "predictive of future volatility behavior with statistical significance"; the JPM collar pattern "holds near the put strike, then sells off after the roll" (SpotGammaLevels, JPMCollar).
- **Volland**: ">90%" classification accuracy, "99%" on 0DTE (VollandDeLorenzo2023). **Wizard of Ops**: the convention is "right maybe ±75% of the time" (WizardOfOps2026).
- **Bank desks**: gamma hedging as "10-15% of total daily volumes on index futures" (NomuraMcElligott); 0DTE crash scenarios (JPMorganKolanovic2023). **Tier 1 Alpha**: "$1.7 billion to hedge per index point" (unit doubtful) (Tier1Alpha).
- **The OPEX calendar**: the "vanna and charm rally" into monthly expiration and the "window of weakness" after it on SPX (KarsanWindowOfWeakness); only a single-stock analogue is documented (StiversSun2013).
- **The book's own claims**: "On a stress day the invisible FLEX and OTC books can dominate the listed number" (Chapter 8A); FLEX and cleared OTC S&P 500 options do appear at OCC, and no estimate of their gamma was found (OCCOpenInterest, FLEXDefinedOutcome).
- **Any test of trading named levels** (walls, flips, Kings) without look-ahead bias: none found, academic or practitioner (LuxAlgoGEXCaution).

### S4. Numbers worth quoting

| Number | Unit and sample, as the source states | Key | Status |
|---|---|---|---|
| $170mm to $670mm | Net market-maker SPX 0DTE gamma "throughout the day" (2023 note) | CboeXu2023 | Exchange research |
| 0.04% to 0.17% | Implied hedging as a share of "daily S&P futures liquidity" | CboeXu2023 | Exchange research |
| 100,000 against 3,000 | Contracts of one put traded in a day, against market makers' net short at the close ("just 3% of the gross volume") | CboeXu2023 | Exchange research |
| "at best, just 0.2%" | Net market-maker 0DTE gamma hedging as a share of SPX daily liquidity (May 2, 2025) | Cboe0DTEsDecoded2025 | Exchange research |
| almost 2 million; 50% to 60%; over 95% | SPX 0DTE contracts a day; retail share of SPX 0DTE; share of 0DTE trades in limited-risk form | Cboe0DTEsDecoded2025 | Exchange research |
| 60 to 90 basis points | Lower annualized index volatility on days with 0DTE trading, 2019 to 2023 | AdamsFontaineOrnthanalai2024 | Working paper |
| at most 3.3 points (6.4 over 30 minutes) | Annualized daily volatility added by negative market-maker 0DTE gamma | AmayaGarciaAresPearsonVasquez2025 | Working paper, as summarized |
| +9.10% | Volatility relative to its mean per one-SD increase in 0DTE trading (IV design, 2011 to 2023) | BrogaardHanWon2026 | Working paper |
| about 36% lower; 0.99 and 0.53 | Next half-hour realized variance per one-SD of non-0DTE public-OI net gamma (five years of SPX half-hours); proxy-to-inventory correlation, non-0DTE and 0DTE | ArdiaVaudescal2026 | Working paper |
| −0.36, −0.14, −0.03 (p = 0.18) | Correlation of GEX with next-day realized volatility: raw, after VIX, after VIX and ATM IV (1,972 SPY days, 2018 to 2026) | FlashAlphaBacktest2026 | Vendor test |
| +0.72; −0.01 (p = 0.77) | VEX's correlation with the VIX; residual correlation with next-day realized volatility | FlashAlphaBacktest2026 | Vendor test |
| 83%, 80%, 77%, 59%; ~50% | Share of classifiable option trades signed correctly by the quote, Lee-Ready, EMO and tick rules; complex-order legs misclassified | SavickasWilson2003 | Peer-reviewed |
| one-third; five times; more than 2 | Effective spreads smaller once execution timing is counted (average, timed trades); overstatement of price impact | MuravyevPearson2020 | Peer-reviewed |
| 0.56 basis points | Five-minute price impact of an option trade on the stock, about one-sixth of a stock trade (S&P 500 stocks, 2020) | Dong2025 | Working paper |
| −0.25 to −0.47 | Correlation between empirical and Black-Scholes gamma at the daily horizon (five underlyings, 2020 to 2025) | Willeboordse2026 | Peer-reviewed letter |
| at least 16.5 basis points; about $9 billion | Return alteration per expiration for optionable stocks; market-cap shift | NiPearsonPoteshman2005 | Peer-reviewed |
| at least $115 million | Notional S&P 500 futures shift per expiration day | GolezJackwerth2012 | Peer-reviewed |
| −0.8 percentage point | Expiration-day return of stocks with large deep in-the-money call open interest, then reversal | Chiang2014 | Peer-reviewed |
| about USD 50 million | Annual transfer between Bitcoin option writers and holders from expiry reversals | Weiss2026 | Peer-reviewed |
| about 4 to 1 | Non-market-maker long call to long put open interest; net short both types (CBOE, 1990 to 2001) | LakonishokLeePearsonPoteshman2004 | NBER / RFS |
| −$1,000 billion; +0.7 and +0.9 points | Reconstructed FX dealer gamma; resulting volatility increase in EURUSD and USDJPY | Anderegg2022 | Peer-reviewed |
| 10% to 15% | Nomura's estimate of gamma hedging as a share of index-futures daily volume (2020) | NomuraMcElligott | Bank estimate, second-hand |
| about $1 trillion | JPMorgan's estimate of daily 0DTE notional volume (2023) | JPMorganKolanovic2023 | Bank estimate, press |
| about 35,000; about $22 billion | SPX contracts and value per leg of the quarterly JPM collar | JPMCollar | Vendor figure |
| more than $70 billion | Buffer (defined-outcome) ETF assets, mid-2025 | FLEXDefinedOutcome | Trade press |
| $500; $1,000; $5,000 a month | Cboe Open-Close: end of day; 10-minute intraday; one-minute intraday | CboeOpenClose | Fee schedule, as summarized |
| 10-minute snapshots within 5 minutes | Intraday Open-Close delay | CboeOpenClose | Exchange documentation |
| about $549,000 against $52,000; about 2.5 times | Dollar gamma per 1% of one at-the-money SPX contract at 16% IV, same-day at the open against 30-day; growth of at-the-money same-day gamma from the open to the last hour | Part C1 | [derived here] |
| $10 billion per 1% = about $167 million per point = about 33,000 E-mini contracts | Unit conversion at SPX 6,000 | Part C5 | [derived here] |

### S5. Figure ideas (interactive)

1. **One expiry through the day** (Part F4, item 1). Draws the same-day expiry as strike against time of day, in three switchable layers: Greek drift at fixed positions, a synthetic tape signed with a classification error, and the overnight reset. The reader controls the layers, the error rate (0% to 41%), the sign convention and the IV path. A readout splits each node's change into drift and flow. It shows that most late-day node growth near the money is time.
2. **Volume is not position.** Draws a synthetic 0DTE session as gross volume at one strike against the market makers' net position and against what a flow map infers. The reader sets how balanced customer flow is, the share of spreads, and the classification error. It reproduces Cboe's example (100,000 traded, 3,000 held) and shows "balance, not notional".
3. **What the sign assumption costs.** Draws the heatmap's named roles (King, floor, ceiling, Gatekeeper, flip) as the reader moves dealers' shares of call and put open interest continuously between the two conventions, with a marked region for the measured finding (market makers net long 0DTE gamma). It shows floors turning into accelerators and the flip moving, with the rings (size) unchanged.
4. **Does GEX add to the VIX?** Draws synthetic daily data in which next-day realized volatility depends on implied volatility and, by a weight the reader sets, on GEX; the reader also sets how strongly GEX and the VIX move together. Readouts give the raw and partial correlations, as in FlashAlpha's test. It teaches why a raw correlation of −0.36 can shrink to nothing once the VIX is controlled for.
5. **The OPEX calendar.** Draws a synthetic month of a large out-of-the-money put book decaying into monthly expiration, with dealer hedge trades per day from charm and from an implied-volatility path the reader sets, and the roll-off after expiry. A switch sets whether dealers are short or long the puts. It shows the "rally into OPEX, weakness after" story, and its reversal under the other sign.
6. **Vendor numbers on one scale.** Extends the book's units lab: the reader picks a published figure (SqueezeMetrics' $64.5 million per point, Tier 1 Alpha's $1.7 billion per point, Cboe's $170 million to $670 million, the book's $10 billion per 1%) and a spot level, and sees it in dollars per point, per 1%, E-mini contracts and a share of daily futures volume. It shows which numbers are comparable and which need a unit checked.
7. **Testing levels without look-ahead.** Draws a synthetic price path with levels computed as of each moment and levels computed from the day's final map. The reader switches which map a simple "fade the level" rule uses, and a readout gives the hit rate for each. It shows how a map that updates all day inflates backtests, the trap LuxAlgo warns about (Chapter 10A).

### S6. Corrections for the book

1. **Chapter 8A**: the gamma flip and SpotGamma's Volatility Trigger are two levels in SpotGamma's own definitions (SpotGammaLevels).
2. **Chapter 8A**: SqueezeMetrics' paper dates from March 2016, revised December 2017 (SqueezeMetricsGEX).
3. **Chapter 8A**: "adopted ... by ... Tier1Alpha and Cboe's own derivative dashboards" is not confirmed: Tier 1 Alpha publishes no method, and Cboe's research measures signs from its data rather than assuming them (Tier1Alpha, CboeXu2023).
4. **Chapter 8A**: "Adams and co-authors (2025)": the version seen is dated May 3, 2024, SSRN 4881008 (AdamsFontaineOrnthanalai2024); check for a 2025 revision before citing that year.
5. **Chapters 10H and 10I**: the Cboe figure is Xu, "0DTEs Decoded" (May 2, 2025), "at best, just 0.2%", and it concerns 0DTE hedging only. Extending it to all walls is an inference; the walls come mostly from longer-dated open interest (Cboe0DTEsDecoded2025, AdamsFontaineOrnthanalai2024).
6. **Chapter 8A**: FLEX and cleared OTC S&P 500 options are reported to OCC; "absent from the chains most vendors use" is accurate, "invisible" is not, and "can dominate ... on a stress day" is untested (OCCOpenInterest, FLEXDefinedOutcome).
7. **This file, Part A6**: the "$170M–$670M" and "0.04%–0.17%" figures are from the 2023 note (CboeXu2023), not the 2025 note.
8. **This file, SqueezeMetricsDIX2018**: the retracted Confirm Signal results were the "positive" ones (ConfirmSignal2021); a bracketed correction is in place.

### Gaps

- No vendor page could be read directly except GEXBot's GitHub specification; all other vendor text is as shown in search summaries.
- Skylit's units, sign rule, classification method and IV surface remain undisclosed.
- ISE Trade Outline fees; OCC file fields and fees; OptionMetrics prices.
- Whether Cboe's market-maker 0DTE measure includes positions opened before the day.
- The size of FLEX SPX open interest and of OTC index books; any estimate of their gamma.
- Goldman Sachs' full Q&A note; Bloomberg's JPMorgan articles; bank methods for dealer gamma.
- Tier 1 Alpha's unit and method.
- VIX-expiration (VOLEX) effects; any test of GEX combined with breadth.
- A named, independent practitioner critique (for example from Benn Eifert or Kris Abdelmessih): none found in summaries.
- The corrected conclusion of Confirm Signal's 2024 re-test; the numbers behind Harbourfront Quant's summary; the SqueezeMetrics quartile figures (0.55% and 0.85%) against the PDF.
