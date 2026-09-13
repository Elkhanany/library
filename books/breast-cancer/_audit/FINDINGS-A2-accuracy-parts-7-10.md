# Audit: factual and numerical accuracy, Parts VII-X (BC-360 through BC-600, 25 chapters)

Scope: every quantitative claim in BC-360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470,
480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600. Hazard ratios and confidence
intervals, median PFS and OS, pCR, iDFS and DFS, response rates, toxicity incidences, doses,
schedules, denominators and P values were extracted and checked against the cited reference in
`references.yaml` and, where a `claim` field exists, against `trials.yaml`.

Approximately 90 PMIDs were fetched and the abstracts read. All 338 distinct citation keys used in
this range resolve in `references.yaml`; no invented keys, PMIDs or DOIs were found.

---

## BLOCKER

None. No wrong hazard ratio, survival figure, dose, schedule, line of therapy or indication was
found in this range.

Specifically checked and correct:

- Every line-of-therapy statement. DESTINY-Breast03 second line after trastuzumab and a taxane;
  DESTINY-Breast06 after one or more lines of endocrine therapy and before chemotherapy for
  metastatic disease; TROPiCS-02 after an endocrine therapy, a taxane, a CDK4/6 inhibitor and two
  to four prior chemotherapy regimens; TROPION-Breast01 after one to two prior chemotherapy lines;
  ASCENT after two or more prior chemotherapy regimens; ASCENT-03 and ASCENT-04 first line in
  PD-L1-ineligible and PD-L1-positive disease respectively; HER2CLIMB after trastuzumab,
  pertuzumab and T-DM1; DESTINY-Breast05 restricted to node-positive residual disease or
  inoperable disease at diagnosis, which BC-500 explicitly contrasts against KATHERINE's wider
  eligibility.
- Every significance statement. NSABP B-59 (EFS not met, HR 0.80, stratified log-rank P=0.083),
  ALEXANDRA/IMpassion030 (futility stop at 2199 of 2300, HR 1.11, P=0.38), PALLAS and PENELOPE-B
  (both negative), MONARCH 3 (HR 0.804, P=0.0664, described as not significant), SONIA (PFS2 and
  OS both non-significant), TROPION-Breast01 final OS (HR 1.01, not significant), NSABP B-39
  (equivalence not met), MA.17R (OS not improved), GeparNuevo pCR (P=0.287, not significant),
  APHINITY OS (P=0.17 against a 0.0012 boundary), MINDACT, COMET, LUMINA, PHERGain, NeoPACT, APT
  and SABR-COMET (all correctly labelled as single-arm, non-inferiority, or phase 2 screening
  designs with the margin or alpha stated).
- Every trial in `trials.yaml` that carries a `claim` field and is cited in this range agrees with
  the chapter text, with the single exception recorded below (CLEOPATRA).
- The three known-good corrections are in place. DESTINY-Breast03 OS is stated as not reached in
  either arm with HR 0.64 and "52.6 vs 42.7 months" does not appear anywhere. MONARCH 3 final OS is
  given as HR 0.804, P=0.0664, non-significant. DESTINY-Breast05 iDFS is 92.4% vs 83.7% and ILD is
  9.6% vs 1.6%.

---

## MAJOR

### BC-450  BS-3950
**Claim as written:** "In first-line metastatic HER2-positive disease, adding pertuzumab to
trastuzumab and docetaxel gave a median overall survival of 56.5 months against 40.8 months. The
hazard ratio for death was 0.68, with a 95% confidence interval of 0.56 to 0.84 [@swain2015]."

**Problem:** Internal contradiction with BC-570 BS-4920, which states the CLEOPATRA median overall
survival as "57.1 months with pertuzumab against 40.8 months with placebo ... hazard ratio for
death was 0.69, and 8-year survival was 37% against 23% [@swain2020]", and with the registry entry
`cleopatra` in `trials.yaml`, whose `claim` is "OS 57.1 vs 40.8 months" with `primary_ref:
swain2020`. A reader comparing the two chapters sees two different median survivals for the same
trial with no explanation.

**Correct value / fix:** Both numbers are correct for the analysis each cites. 56.5 months is the
2015 confirmatory overall survival analysis (PMID 25693012); 57.1 months is the 2020 end-of-study
analysis at a median follow-up of about 99 months (PMID 32171426). The registry figure, 57.1, is
the current one. Either align BC-450 to the end-of-study analysis, or add the data cut to the
sentence, for example "at the 2015 confirmatory analysis, 56.5 months against 40.8 months, later
57.1 months at end of study [[BS-4920]]".

**Source checked:** PMID 25693012 and PMID 32171426.

### BC-450  BS-3970  /  BC-490  BS-4320
**Claim as written:** BC-450: "Ribociclib with a non-steroidal aromatase inhibitor in stage II or
III disease gave a hazard ratio of 0.75, with an interval of 0.62 to 0.91. Three-year rates were
90.4% against 87.1% [@slamon2024]." BC-490: "The final invasive disease-free survival analysis gave
a hazard ratio of 0.749, with an interval of 0.628 to 0.892, and three-year rates of 90.7% against
87.6% [@hortobagyi2025]."

**Problem:** Internal contradiction between chapters on the headline NATALEE result. Two different
three-year iDFS rate pairs are given for the same trial with no signposting.

**Correct value / fix:** Both are correct for their own source. 90.4% against 87.1% with HR 0.75
(95% CI 0.62 to 0.91, P=0.003) is the prespecified interim analysis at a January 2023 cutoff.
90.7% against 87.6% with HR 0.749 (95% CI 0.628 to 0.892, P=0.0012) is the final preplanned iDFS
analysis at a July 2023 cutoff. Name the analysis in both places, or cite only the final analysis
in BC-450 as well.

**Source checked:** PMID 38507751 (interim) and PMID 39442617 (final).

### BC-540  BS-4680
**Claim as written:** "The index is built from four measurements of the surgical specimen. They are
the two dimensions of the primary tumour bed, the proportion of that bed which is cancer, the
number of positive nodes, and the size of the largest nodal deposit [@symmans2007]."

**Problem:** The residual cancer burden index takes five inputs, and the one omitted here is the
percentage of the residual cancer that is in situ. That component is required, because RCB uses it
to derive the invasive cellularity from the overall cellularity. BC-370 BS-3350 states the index
correctly: "The calculation uses five measurements: the two largest dimensions of the residual
tumour bed, the proportion of that bed that is cellular, the proportion of cellularity that is in
situ, the number of positive nodes, and the diameter of the largest nodal deposit." The two
chapters therefore disagree about how a score the book relies on is computed, and the BC-540
version would produce a wrong number if a reader tried to apply it.

**Correct value / fix:** Use the BC-370 enumeration. "The index is built from five measurements of
the surgical specimen: the two largest dimensions of the residual tumour bed, the proportion of
that bed that is cellular, the proportion of that cellularity that is in situ, the number of
positive nodes, and the diameter of the largest nodal deposit."

**Source checked:** PMID 17785706. The rest of the BC-540 paragraph, including the development
cohort of 382 patients, the adjusted hazard ratio of 2.50 (95% CI 1.70 to 3.69), RCB-I in 17% and
RCB-III in 13%, is correct.

---

## MINOR

### BC-490  BS-4320
**Claim as written:** "...three-year rates of 90.7% against 87.6% [@hortobagyi2025]. At four years
the hazard ratio was 0.72 with rates of 88.5% against 83.6% [@fasching2025]. At a median follow-up
of 55.4 months the hazard ratio was 0.716... The absolute gap widened from 2.7 percentage points at
three years to 4.5 points at five years."

**Problem:** The paragraph is arithmetically self-contradicting as written. 90.7 minus 87.6 is 3.1
percentage points, not 2.7, and the four-year gap quoted two sentences earlier is 4.9 points, which
is larger than the five-year figure of 4.5. Every individual number is correct and sourced: the
2.7-point three-year gap comes from the four-year analysis (90.8% against 88.1%) and the 4.5-point
five-year gap from the five-year analysis. The reader cannot see that without being told.

**Correct value / fix:** Attribute the widening sentence to its own analysis, for example "In the
five-year analysis the absolute gap widened from 2.7 percentage points at three years to 4.5 points
at five years [@crown2025]", or drop the redundant four-year sentence.

**Source checked:** PMID 39442617, PMID 40996773, PMID 41320342.

### BC-490  BS-4300
**Claim as written:** "Among 6,693 enrolled patients, those at high clinical and low genomic risk
who received no chemotherapy had a five-year distant metastasis-free survival of 95.1%, above the
prespecified 92% boundary."

**Problem:** Two small imprecisions. First, the non-inferiority test in MINDACT was on the lower
boundary of the 95% confidence interval, not on the point estimate, so "95.1%, above the
prespecified 92% boundary" misdescribes the test. In the updated analysis the interval was 93.1% to
96.6%, and it is 93.1% that cleared 92%. Second, BC-380 BS-3380 gives 94.7% (95% CI 92.5 to 96.2)
for the same quantity. Both are right, 94.7% being the 2016 primary report and 95.1% the 2021
updated primary test population of 644 patients, but the difference is unexplained across chapters.

**Correct value / fix:** "...a five-year distant metastasis-free survival of 95.1%, with a 95%
confidence interval of 93.1% to 96.6%, whose lower boundary cleared the prespecified 92%
non-inferiority bound." Note the data cut in one of the two chapters.

**Source checked:** PMID 27557300 and PMID 33721561.

### BC-410  BS-3660  and  BC-420  BS-3730
**Claim as written:** "In {{trial:nsabp-b51}}, 1556 patients with biopsy-proven nodal disease who
reached ypN0 after neoadjuvant chemotherapy were randomised..." and "{{trial:nsabp-b51}} randomised
1556 patients whose biopsy-proven nodal disease had cleared to ypN0..."

**Problem:** 1641 patients were enrolled and randomised. 1556 were included in the primary-event
analysis, 772 in the irradiation group and 784 in the no-irradiation group.

**Correct value / fix:** "1641 patients were randomised, and 1556 were included in the
primary-event analysis." The hazard ratio of 0.88 (95% CI 0.60 to 1.28) and the point estimates of
92.7% and 91.8% are correct.

**Source checked:** PMID 40466065.

### BC-570  BS-4990  and  BC-590  BS-5130
**Claim as written:** "Fifty-seven patients had hormone receptor positive, HER2-mutant metastatic
breast cancer and had progressed on a CDK4/6 inhibitor. Neratinib with fulvestrant and trastuzumab
produced an objective response rate of 39% and median progression-free survival of 8.3 months."

**Problem:** The denominator is misattributed. SUMMIT reported 71 patients with hormone receptor
positive, HER2-mutant metastatic breast cancer; 57 of them received neratinib with fulvestrant and
trastuzumab, and the 39% response rate (95% CI 26 to 52) and 8.3-month median progression-free
survival belong to those 57. The chapter reads as if 57 were the size of the cohort.

**Correct value / fix:** "Seventy-one patients had hormone receptor positive, HER2-mutant metastatic
breast cancer. The 57 who received neratinib with fulvestrant and trastuzumab had an objective
response rate of 39% and median progression-free survival of 8.3 months."

**Source checked:** PMID 37597578.

### BC-460  BS-4080  (repeated in BC-570 BS-4940 and BC-580 BS-5090)
**Claim as written:** "Among 85 patients who received both trastuzumab deruxtecan and sacituzumab
govitecan, progression-free survival on the second conjugate was shorter than on the first in
75.2%."

**Problem:** The denominator is not 85. Fourteen of the 85 were still on treatment at data cutoff,
so the percentage is computed on an evaluable subset the source does not state cleanly, and 75.2%
has no integer solution over 85. The book's own rule is to say what a number is a number of.

**Correct value / fix:** Reproduce the source's framing with its caveat, for example "in 75.2% of
the evaluable patients, with 14 of the 85 still on treatment at data cutoff". The PTEN findings
quoted alongside it, HR 3.20 (1.47 to 6.97) for trastuzumab deruxtecan and 1.18 (0.54 to 2.56) for
sacituzumab govitecan, are correct.

**Source checked:** PMID 40440568.

### BC-370  BS-3270
**Claim as written:** "A negative result on a test with 85% sensitivity leaves substantial residual
probability when pretest probability was high to begin with."

**Problem:** 85% is presented as a property of a diagnostic test in this setting and carries no
source. It reads as an empirical figure rather than an illustration.

**Correct value / fix:** Either cite a sensitivity estimate for the modality being discussed, or
recast as explicitly hypothetical, for example "a test with a sensitivity of, say, 85%".

**Source checked:** not verifiable, no source given.

### BC-520  BS-4560
**Claim as written:** "Patients who were older, treated earlier in the period, on lower incomes,
publicly insured or more comorbid were significantly less likely to receive all three
[@rueth2014]."

**Problem:** The cited analysis also identified geographic region (living outside the Midwest) as a
significant predictor of not receiving trimodality therapy. The omission slightly understates how
much of the underuse is structural rather than clinical, which is the point the section is making.

**Correct value / fix:** Add region to the list. Everything else in the paragraph, including the
10,197 patients, the 58.4% to 73.4% range and the 55.4% and 37.3% five- and ten-year survival, is
correct.

**Source checked:** PMID 24888808.

### references.yaml, five duplicate entries reachable from this range
**Problem:** Five papers appear twice in `references.yaml` under two keys, as full duplicate entries
rather than aliases: `ebctcg2011rt` and `ebctcg2011` (PMID 22019144), `ebctcg2022ofs` and
`ebctcg2022` (PMID 35123662), `loibl2019` and `loibl2019geparnuevo` (PMID 31095287), `loibl2022`
and `loibl2022geparnuevo` (PMID 35961599), `schmid2022k522efs` and `schmid2022` (PMID 35139274).
Chapters in this range split across the pairs: BC-420 uses `ebctcg2011rt` while BC-520 and BC-530
use `ebctcg2011`; BC-430 uses `ebctcg2022ofs` while BC-490 uses `ebctcg2022`; BC-510 uses
`loibl2019`, `loibl2022` and `schmid2022k522efs` while BC-540 uses `loibl2019geparnuevo`,
`loibl2022geparnuevo` and `schmid2022`.

No chapter uses both spellings of a pair, so no page will number the same paper twice today. The
risk is maintenance: a correction applied to one entry will silently not reach the other, and the
appendix will list the same paper twice.

**Correct value / fix:** Keep one canonical key per paper and make the other an alias pointer rather
than a second full record, as CONVENTIONS.md requires.

**Source checked:** references.yaml, verified by PMID collision.

### BC-390  BS-3490 closing interplay block
**Claim as written:** "A test that detects the shedding, dividing fraction of residual disease will
find the patients whose recurrence was going to be early, and those are the patients for whom an
earlier start of existing therapy is least likely to be curative."

**Problem:** 41 words, and two independent clauses chained. The only sentence over the house limit
in the whole range.

**Correct value / fix:** Split at "and those are the patients".

**Source checked:** not applicable, style.

---

## Summary

**Counts.** BLOCKER 0. MAJOR 3. MINOR 9.

Roughly 400 discrete quantitative claims were checked against abstracts, and the numbers,
confidence intervals, denominators, doses, schedules and significance statements were right
essentially without exception. The trials that carry the highest risk of being got wrong were all
correct: DESTINY-Breast03, 04, 05, 06, 09 and 11; ASCENT, ASCENT-03 and ASCENT-04; TROPiCS-02,
TROPION-Breast01 and TROPION-Breast02; KEYNOTE-522 and KEYNOTE-355; monarchE, NATALEE, PALLAS and
PENELOPE-B; OlympiA, KATHERINE, CREATE-X; SOLAR-1, CAPItello-291, INAVO120; EMERALD, EMBER-3,
SERENA-6, SONIA; TAILORx, RxPONDER, MINDACT; HER2CLIMB, PATINA, CLEOPATRA and SUMMIT. The book is
also unusually disciplined about saying when a trial was single-arm, when an endpoint was immature,
and when a subgroup finding was post hoc.

**SERENA-6 note, since it was flagged for particular attention.** BC-560 BS-4840 states median
progression-free survival of 16.8 against 9.2 months with a hazard ratio of 0.45, second
progression-free survival of 25.7 against 19.1 months with a hazard ratio of 0.63, and a screening
denominator of 3,256 tested, 548 positive, 315 randomised. All six figures match the extended
analysis exactly, including the 16.8 months that differs from the 16.0 months of the earlier interim
report. The chapter has the newer numbers and is right.

**The three things most worth fixing before merge.**

1. **BC-540 BS-4680, the residual cancer burden formula.** This is the only finding in the range
   where a reader could act on the text and get a wrong answer. The in-situ proportion is a required
   input to the index and it is missing, and the chapter's own cross-reference in BC-370 BS-3350
   states the method correctly. One sentence to fix.

2. **The CLEOPATRA overall survival discrepancy between BC-450 and BC-570.** The book reports two
   different median survivals for the same trial in two chapters, and the registry in `trials.yaml`
   agrees with only one of them. Neither number is wrong. The fix is to name the data cut, or to
   move BC-450 to the end-of-study analysis the registry uses.

3. **The NATALEE three-year figures, in BC-450, BC-490 and within BC-490's own paragraph.** Three
   different analyses of the same trial are quoted across two chapters and inside one paragraph
   without being distinguished, producing a paragraph in BC-490 whose stated rates and stated
   absolute gap do not reconcile. Naming the analysis in each place resolves all of it.
