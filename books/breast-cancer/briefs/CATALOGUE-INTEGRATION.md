---
id: catalogue-integration
title: "Bringing the catalogue trials into the chapters"
status: plan
---

The registry holds 591 trials. 165 of them are catalogue records (`catalogue: true`): verified and
listed in Appendix A, but argued nowhere in the book and shown in no evidence table. This plan says
which of them the chapters should take up, where, and how, so that the book argues the evidence the
registry now holds rather than only listing it.

## What taking a trial out of the catalogue involves

Removing the flag is the last step, not the first. When it comes off:

- the record enters every evidence table whose filter it matches, so each such table's caption and
  every sentence that counts its rows must be re-read (`tabdiff.py` lists them);
- unless its family is declared out of scope (prevention, DCIS, radiotherapy, surgery, supportive,
  screening, local recurrence), it must be named in the story question it answers, or synthcheck
  reports it as an orphan;
- if a table shows it, the chapter must discuss it, or synthcheck reports it as untold.

So each trial is given one of three outcomes.

| Tier | Outcome | For |
|---|---|---|
| A | Argued in prose, named in its story question, shown in its tables | randomised trials that answer, sharpen or contradict a question a chapter already asks |
| B | Shown in its tables, mentioned in the paragraph that introduces the table, no argument of its own | older randomised trials that belong to a record the chapter tabulates (historic tamoxifen and anthracycline trials) |
| C | Stays catalogue | single-arm, phase 1, pilot, metabolic and feasibility studies, and trials no chapter question touches |

## What the mapping found

Computed from the registry on 2026-10-29 (`scratchpad/plan/catalogue-map.json`):

- 62 of the 165 would enter at least one existing evidence table if the flag came off: BC-850 (16
  rows), BC-810 (11), BC-790 (10), BC-890 (9), BC-900 (8), BC-840 (5), BC-830 (4), BC-490, BC-510
  and BC-880 (3 each), BC-920 (2), and one each in BC-590, BC-600, BC-640 and BC-870.
- 103 would enter no table. Most are exploratory single-arm studies; the rest sit in settings the
  chapters do not tabulate (prevention, supportive care, most radiotherapy).
- Three are already cited by the prose and need only naming, as IBIS-I, IBIS-II, MAP.3, EORTC 10853
  and TAMRAD were on 29 October: FinXX (BC-440), the GEC-ESTRO partial-breast trial (BC-480) and
  IBCSG 23-01 (BC-410).
- One structural issue: an all-comers trial (subtype `all`) matches every subtype table by design.
  That is why fourteen all-comers adjuvant chemotherapy trials (TACT, TACT2, AGO ETC, SWOG S9313,
  MA.5 and others) would land in BC-850's triple-negative tables, and eleven all-comers neoadjuvant
  trials in BC-810's receptor-positive ones. Decision 2 below.

## Decisions needed before work starts

1. **The tiering rule above.** Tier A is the expensive one (new prose, story edits, re-argued
   tables). The work packages below propose about 70 tier-A trials, 30 tier-B and 65 tier-C.
2. **All-comers trials in subtype tables.** Either (a) accept the wildcard, so BC-850 and BC-810
   gain the all-comers rows and their captions say so, or (b) add a filter that holds a block to its
   own subtype, so all-comers chemotherapy trials are argued once, in BC-440 (cytotoxic
   chemotherapy) and BC-490 (adjuvant chemotherapy), and not repeated in every subtype chapter.
   Recommendation: (b). The subtype chapters argue what is specific to the subtype, and fourteen
   all-comers rows would bury the triple-negative trials in BC-850's table.
3. **Historic trials in tables (tier B).** NATO, NSABP B-05, B-09, B-21 and B-33 and similar would
   join BC-790's adjuvant endocrine table. Recommendation: yes, because completeness was the point of
   the catalogue, and the table caption can say which rows predate aromatase inhibitors.
4. **Pace.** One work package per review round, as with the ESMO update, or all at once. Each
   package is one drafting agent, a review by me against PubMed and the conventions, then apply,
   checks and commit.

## Work packages

Ordered by how much each changes what a reader is told. Each package names its tier-A and tier-B
trials; everything else in its area stays tier C (listed at the end).

**WP1 · Naming only (quick).** FinXX in BC-440, GEC-ESTRO in BC-480, IBCSG 23-01 in BC-410, as for
the five trials on 29 October. FinXX also enters BC-850's tables (see decision 2).

**WP2 · Prevention, BC-080.** Tier A: STAR, RUTH, MORE/CORE, PEARL, Generations, the Royal Marsden
and Italian tamoxifen trials, HOT, LIBER (letrozole in BRCA carriers, 2025), the Decensi low-dose
tamoxifen and fenretinide 2×2 trial, the fenretinide second-breast-cancer trial. The chapter argues
IBIS-I, IBIS-II and MAP.3 already. What it lacks is the SERM comparison (STAR), the raloxifene and
lasofoxifene osteoporosis trials that measured breast cancer as an outcome, and the two tamoxifen
trials that disagreed with IBIS-I. Prevention is a declared out-of-scope family, so no story work.

**WP3 · Local therapy, BC-410, BC-420, BC-550, BC-600.** Tier A: SUPREMO (chest-wall radiotherapy
in intermediate risk, 10-year survival, NEJM 2025), TARGIT-A and ELIOT (intraoperative partial-breast
radiotherapy), CHN-HypoPMRT, JCOG1017 (surgery of the primary in de novo stage IV disease; joins
EA2108 and LTMBC in the disease-control tables, which needs its topic tag), GANEA 2 and the Martelli
elderly-axilla trial in BC-410. Tier C: PRIME I (quality of life only; PRIME II is the trial that
answers the question and is not yet in the registry).

**WP4 · Neoadjuvant chemotherapy and the pCR argument, BC-810, BC-540, BC-830, BC-860.** Tier A:
GeparTrio (response-guided switching), the two GeparQuinto cohorts (neoadjuvant bevacizumab raised
pCR without a survival gain; lapatinib was worse than trastuzumab), NSABP B-40, ARTemis and SWOG S0800
(bevacizumab again), GeparQuattro, EORTC 10994 (TP53 did not predict taxane benefit), REMAGUS 02 and
NeoPHOEBE. Tier B: GeparDuo, EORTC 10902, the MDACC weekly paclitaxel trial, Aberdeen. These trials
carry the book's argument that pathological complete response is not a surrogate for survival, which
BC-540 makes with fewer examples than it could.

**WP5 · Adjuvant chemotherapy, BC-440, BC-490, BC-850.** Tier A: BEATRICE (adjuvant bevacizumab in
triple-negative disease), FinXX and US Oncology 01062 (adjuvant capecitabine, beside CREATE-X and
SYSUCC-001), IBCSG 22-00 (metronomic maintenance, beside SYSUCC-001), TACT, TACT2, AGO ETC and
GONO-MIG-1 (dose density and sequencing), SUCCESS-A (gemcitabine and zoledronate duration). Tier B:
SWOG S9313, MA.5, WSG AM-01, ICE II, Chemo-N0, NSABP B-05. Where these land depends on decision 2.

**WP6 · Adjuvant endocrine history, BC-790.** Tier B: NATO, NSABP B-09, B-21, B-33, NCCTG 89-30-52,
BASO II, the Bedognetti timing trial. Tier A: NSABP B-21 deserves a sentence in BC-480/BC-790's
small-tumour argument (tamoxifen, radiotherapy or both for tumours of 1 cm or less). Tier C: HEART,
the Francini exemestane metabolic trial, the Wisconsin bone-density study.

**WP7 · HER2-positive disease, BC-820, BC-840, BC-900, BC-910, BC-470.** Tier A: BOLERO-1 and
BOLERO-3 (everolimus in HER2-positive metastatic disease), LUX-Breast 1 (afatinib), the neratinib
against lapatinib-capecitabine phase 2, HERITAGE and PF-05280014 (biosimilar trastuzumab, one
paragraph), PRESENT, the GP2 and AE37 vaccine trials and the nelipepimut-trastuzumab trial (HER2
peptide vaccination failed at phase 3; one paragraph in BC-470 or BC-820), TrastuRel. Tier B: the
early single-agent trastuzumab studies (Cobleigh, Baselga 1996, Pegram), which the registry now holds
as the drug's first evidence. Tier C: the phase 1 vaccine and kinase-inhibitor studies.

**WP8 · Hormone receptor-positive metastatic disease, BC-870, BC-880, BC-890.** Tier A: SWOG S1416
(cisplatin with veliparib in BRCA-like disease), SAFIR02-Breast IMMUNO (durvalumab maintenance, also
BC-470), CA163-048 (ixabepilone with capecitabine). Tier B: IMMU-132-01, DS8201-A-J101 and
U31402-A-J101 as the single-arm studies that preceded ASCENT, the DESTINY-Breast trials and
HERTHENA-Breast; BC-890's weight=any table shows them already once the flag is off. Tier C: the
vorinostat, AZD4547, palbociclib-Rb, tremelimumab and alpelisib-nab-paclitaxel studies.

**WP9 · Triple-negative metastatic disease, BC-920, BC-740.** Tier A: the iniparib randomised
phase 2 (a positive phase 2 overturned at phase 3; it belongs in BC-740's argument about phase 2
results as much as in BC-920), KEYNOTE-086 and KEYNOTE-012 (single-agent pembrolizumab before
KEYNOTE-119), BALI-1, LEAP-005. Tier C: the phase 1 checkpoint and kinase studies.

**WP10 · Supportive care and survivorship, BC-640, BC-650.** Tier A: PRADA (cardioprotection
during adjuvant therapy), and one paragraph on non-hormonal treatment of vasomotor symptoms built
from N03C5, the electroacupuncture-gabapentin trial, ACCLIMAT, MENOS 1, the hypnosis trial and the
negative soy and vitamin E trials. Tier B: the lidocaine dyspareunia and vaginal estriol trials in
BC-650. Supportive is a declared out-of-scope family, so no story work.

**Stays catalogue (tier C), about 65 trials.** Phase 1 vaccine and targeted-agent studies, pilot and
feasibility studies, metabolic and bone-density studies of tamoxifen, single-arm neoadjuvant
endocrine studies (N007, NEOCENT, POP, MONALEESA-1 and the letrozole studies), the HER2 DC1 DCIS
vaccine, and pan-tumour basket trials with small breast cohorts. Each remains in Appendix A and the
workbook. Any can be promoted when a chapter question needs it.

## How each package runs

As the October update did: one drafting agent per package, working from a brief and writing a batch
for `tools/registry_apply.py` that removes the flag, edits prose and stories by exact quote, and lists
the story questions it re-read. I review every batch against PubMed and CONVENTIONS before applying.
After applying: `tabdiff.py` against the previous registry, `evidence.py --check`, `--lines` and
`--sync-chapters`, `synthcheck.py`, `stories.py --check`, `numcheck.py`, `stylecheck.py`, the build,
and then commit. The site rebuild and its checks run once at the end of each round, followed by a
pull request.

## Not in this plan

The completeness sweep from guideline reference lists and a PubMed search for phase 3 breast trials
(which would add NSABP B-17, B-24, UK/ANZ DCIS, SweDCIS and others as catalogue records) is a
separate step, with a reminder set for 5 November.
