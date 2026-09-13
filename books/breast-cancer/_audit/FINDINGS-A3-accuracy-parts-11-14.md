# Audit: factual and numerical accuracy, Parts XI to XIV (BC-610 to BC-780)

Scope: 18 chapters, BC-610 through BC-780. Every quantitative claim was extracted and checked
against the cited source's PubMed abstract, and against full text where the abstract was
insufficient. Roughly 160 distinct numerical claims across 190 citation keys were checked.

Overall the numerical accuracy is high. The disparities chapters (BC-690, BC-700, BC-710), which
were flagged as the highest-risk area, are the cleanest in the range: every mortality gap,
incidence ratio, survival difference, screening rate, delay interval and cost figure I checked
reproduced exactly from its source. The problems that remain are concentrated in BC-740, where
three of the methodological worked examples are wrong or backwards, and in a small number of
places where a citation points at the wrong paper or a claim outruns what the source shows.

Chapters clean on every claim checked: BC-610, BC-620, BC-630, BC-660, BC-690 (one minor),
BC-700 (one minor), BC-720, BC-730.

## BLOCKER

_(none)_

No number in this range would lead a reader to a wrong dose, indication or clinical decision.
The BC-740 findings below are methodological rather than clinical, and are filed as MAJOR.

## MAJOR

### BC-740  BS-6370
**Claim as written:** "{{trial:nsabp-b51}} reported an invasive recurrence-free interval hazard
ratio of 0.88 with a confidence interval from 0.60 to 1.28 [@mamounas2025]. That is a superiority
trial that did not demonstrate benefit from regional nodal irradiation in that population. It is
not a demonstration that omitting radiation is equivalent, because the interval extends to 1.28
and the trial was not powered against a pre-specified non-inferiority margin."
**Problem:** The conclusion is right and the reason given for it is the wrong end of the interval.
The hazard ratio of 0.88 is regional nodal irradiation against no irradiation, so values below 1
favour irradiation. The bound that defeats an equivalence reading is therefore the **lower** bound
of 0.60, which leaves open a 40% relative reduction in events from irradiation, that is a
substantial harm from omitting it. The upper bound of 1.28 is the bound in the direction where
irradiation is worse than omission, which if anything supports omission. This is the section whose
whole thesis is that "Non-inferiority is claimed when the entire confidence interval for the
difference lies on the acceptable side of the margin". Naming the wrong side in the worked
counterexample teaches the error the section exists to prevent.
**Correct value / fix:** "It is not a demonstration that omitting radiation is equivalent. The
interval runs down to 0.60, so a 40% relative reduction in events from regional nodal irradiation
is entirely compatible with these data, and the trial was not powered against a pre-specified
non-inferiority margin."
**Source checked:** PMID 40466065 (HR 0.88, 95% CI 0.60 to 1.28; 92.7% against 91.8% event-free;
1556 patients analysed)

### BC-740  BS-6340
**Claim as written:** "A biomarker-selected trial restricts entry to patients with a marker and
tests one intervention... It cannot answer whether the marker predicts benefit, because there is
no marker-negative arm. {{trial:solar1}} and {{trial:capitello291}} are biomarker-selected in this
sense."
**Problem:** Both named trials are counterexamples to the category they are used to illustrate.
SOLAR-1 randomised 572 patients into **two cohorts by PIK3CA mutation status**, including a
non-mutated cohort, and reported a hazard ratio of 0.85 in that non-mutated cohort. It is the
textbook case of a trial that *did* include a marker-negative comparison and *could* therefore
speak to whether the marker predicts benefit. CAPItello-291 did not select on biomarker at all:
708 patients were randomised regardless of AKT pathway status, 289 (40.8%) had alterations, and
the trial carried a dual primary endpoint in the overall and altered populations.
**Correct value / fix:** Either replace both examples with genuinely biomarker-restricted trials,
or keep them and make the opposite point, that SOLAR-1 and CAPItello-291 show what including a
marker-negative population buys you. INAVO120 (PIK3CA alteration required for entry) and EMERALD
(ESR1-mutant subgroup prespecified) are the better illustrations.
**Source checked:** PMID 31091374, 37256976

### BC-690  BS-5900
**Claim as written:** "Entry to {{trial:solar1}} and {{trial:inavo120}} required a PIK3CA
alteration, and the drugs approved on those trials are prescribed on the same basis [@andre2019;
@turner2024inavo120]."
**Problem:** True of INAVO120, not of SOLAR-1. SOLAR-1 enrolled 572 patients into two cohorts by
PIK3CA mutation status, 341 with confirmed mutations and the remainder without, and reported a
progression-free survival hazard ratio of 0.85 (0.58 to 1.25) in the non-mutated cohort. Entry did
not require the alteration; the approval restricted to it. The argument the section builds on this,
that a population with lower PIK3CA mutation frequency has lower eligibility for the drug class by
arithmetic alone, survives intact, because it rests on the approved indication rather than on the
trial entry criterion. But the sentence as written is a factual error about a trial, in the chapter
whose stated discipline is stating what was measured.
**Correct value / fix:** "Approval of the drugs tested in {{trial:solar1}} and {{trial:inavo120}}
is restricted to tumours carrying a PIK3CA alteration, and they are prescribed on that basis."
**Source checked:** PMID 31091374, 39476340

### BC-670  BS-5690
**Claim as written:** "The seven-year invasive disease-free survival difference is 77.4% against
70.9%, and the seven-year overall survival difference is 86.8% against 85.0% with a hazard ratio
of 0.84 [@johnston2020]."
**Problem:** Citation points at the wrong paper. The key `johnston2020` resolves to PMID 32954927,
the 2020 JCO primary monarchE report at the preplanned interim analysis, which reports **2-year**
IDFS rates of 92.2% against 88.7% with a hazard ratio of 0.75, and reports no overall survival
result at all. The 7-year IDFS and OS figures come from a later monarchE analysis. This is the
worked example on which the whole absolute-versus-relative argument of BC-670 rests, so the
numbers need to point at the report that contains them.
**Correct value / fix:** Add the reference for the monarchE long-term (7-year) analysis to
references.yaml and cite it here. If the 7-year numbers cannot be sourced, fall back to the
interim figures in PMID 32954927, which support the same argument: a 3.5 point IDFS difference
at 2 years against a hazard ratio of 0.75.
**Source checked:** PMID 32954927

### BC-740  BS-6400 (internal contradiction with BC-690 BS-5900)
**Claim as written:** "This matters biologically and not only ethically. Ancestry-associated
differences in tumour biology are documented in [[BC-700]]."
**Problem:** Two errors in one sentence. The cross-reference is wrong: BC-700 is "Access,
affordability, and financial toxicity"; the material is in BC-690 BS-5900. More seriously, the
sentence asserts as established exactly the claim BS-5900 spends a whole section dismantling.
BS-5900 states: "In nearly all of the studies below, participants were classified by self-reported
race. Ancestry was not estimated. The results are therefore race-associated. Calling them
ancestry-associated is a substitution the data do not support," and "The one study that measured
ancestry rather than race found no ancestry association." BS-5950 then lists "publication of
unreplicated ancestral claims" as one of the five ways disparities research causes harm. BC-740
commits that error two chapters later.
**Correct value / fix:** "Race-associated differences in tumour biology, and the reasons for not
calling them ancestry-associated, are set out in [[BS-5900]]."
**Source checked:** internal; supporting sources PMID 40858906 (no ancestry association), 27915434
(differences vanish within triple-negative disease)

### BC-770  BS-6620 and BC-780  BS-6680
**Claim as written:** BS-6620: "Evolution-informed timing is the version that has now worked."
BS-6680: "{{trial:serena6}} is the first evidence that acting at the moment of emergence rather
than at progression changes outcomes [@turner2026serena6]."
**Problem:** No number is given anywhere in the book for SERENA-6, which is presented as the most
consequential new result in Part XIV and is invoked in three separate sections. And "changes
outcomes" is undifferentiated. SERENA-6 demonstrated progression-free survival and second
progression-free survival benefit. Overall survival is not established. BS-6420 in BC-740 sets the
rule: "Progression-free survival benefit is a real benefit when progression is symptomatic and the
toxicity is tolerable. It is not evidence of longer life, and it should not be described to a
patient as though it were." BS-6620 and BS-6680 breach the book's own rule.
**Correct value / fix:** Median progression-free survival 16.8 months (95% CI 14.7 to 19.4) with
camizestrant plus CDK4/6 inhibitor against 9.2 months (7.2 to 9.7) with continued aromatase
inhibitor plus CDK4/6 inhibitor, hazard ratio 0.45 (0.34 to 0.59). Median second progression-free
survival 25.7 against 19.1 months, hazard ratio 0.63 (0.46 to 0.86). 315 patients randomised from
3256 screened by ctDNA. Say that the benefit shown is on progression, not on survival.
**Source checked:** PMID 42442380

### BC-710  BS-6150
**Claim as written:** "The figure to hold is the last one. One paper in seven about health in a
sub-Saharan African country had no author from any country in the region."
**Problem:** The 13.5% is quoted correctly in the preceding sentence, but the gloss changes what
"local" means. Hedt-Gauthier defines a local author as one affiliated with **the country the paper
is about**. Authors from other African countries are a separate category, and the paper's headline
finding is that local representation was *highest* when collaborators came from another African
country. The proportion of papers with no sub-Saharan African author at all is not reported and
would be smaller.
**Correct value / fix:** "One paper in seven about health in a sub-Saharan African country had no
author affiliated with the country the paper was about."
**Source checked:** PMID 31750000

### BC-730 BS-6280, BC-750 BS-6430, BC-780 BS-6710
**Claim as written:** BS-6280: "Spatial proteomics found that receptor protein states within a
single tumour vary in ways transcriptional subtyping does not capture." BS-6430: "Spatial
proteomic analysis of breast tumours found receptor protein phenotypes within single tumours that
transcriptional classification does not resolve." BS-6710: "Spatial protein-level heterogeneity
within single tumours produces receptor phenotypes that transcriptional classification does not
resolve [@mardamshina2025]."
**Problem:** Half right, and the wrong half is the comparator. Full text confirms the first half:
the study scored a Receptor-ITH index from co-existing receptor subtypes within single tumours,
found receptor diversity significantly lower in high-grade tumours across 385 tumours (p = 0.003),
and found "discordance between the receptor expression patterns and the overall proteomic
patterns, as often protein-based clusters included regions with distinct receptor expression."
But the comparison made is **spatial proteomics against immunohistochemical receptor
classification**, not against transcriptional classification. No transcriptional subtyping of
these regions was performed. IHC-versus-RNA discordance appears only in the Introduction as
background citing prior work. The headline finding is that proteomic intratumour heterogeneity
rises with grade, is independent of genomic heterogeneity, and tracks microenvironmental
differences. BS-6710 uses this as the first of the three pillars of the book's central argument,
so the comparator matters.
**Correct value / fix:** "Spatial proteomics across 280 tumour regions found receptor phenotypes
co-existing within single tumours, and found regional proteomic states that the tumour's assigned
receptor classification does not resolve. Proteomic heterogeneity rose with grade, was independent
of genomic heterogeneity, and tracked microenvironmental differences."
**Source checked:** PMID 41290667, full text via PMC12647654

## MINOR

### BC-740  BS-6370
**Claim as written:** "Work through {{trial:import-low}}... The control event rate is around 1%. A
margin has to be set as an absolute difference at that rate, and a margin of two percentage points
would permit a tripling of relapse."
**Problem:** This is the worked example in the section whose own practice block tells the reader to
find "the margin and its justification" before accepting a non-inferiority claim, and the worked
example never states the margin the trial actually used. A hypothetical "two percentage points"
sits where the real number belongs. The same omission applies to FAST-Forward and SENOMAC in the
two following paragraphs.
**Correct value / fix:** IMPORT LOW prespecified a 2.5 percentage point absolute increase in 5-year
local relapse, equivalent to a critical hazard ratio of 2.03. FAST-Forward prespecified an excess
of no more than 1.6 percentage points against an assumed 2% 5-year incidence for 40 Gy, critical
hazard ratio 1.81. SENOMAC required the upper bound of the confidence interval for the hazard ratio
to lie below 1.44. Quoting the real margins makes the point the section is making, and the IMPORT
LOW margin of 2.5 points against a 1.1% control rate is a more striking illustration than the
hypothetical.
**Source checked:** PMID 28779963, 32580883, 38598571

### BC-740  BS-6390
**Claim as written:** "Progression-free survival from the second line onward was 31.0 against 26.8
months and not statistically significant."
**Problem:** Mis-describes the endpoint. SONIA's primary endpoint PFS2 runs from randomisation to
progression after second-line treatment, not from the second line onward. BC-770 BS-6630 describes
the same result correctly as "progression-free survival from randomisation to second progression",
so the two chapters disagree about what the number measures. The hazard ratio, 0.87 (0.74 to 1.03),
is also omitted in a section that tells readers to read the interval rather than the P value.
**Correct value / fix:** "Progression-free survival from randomisation to progression after
second-line treatment was 31.0 against 26.8 months, hazard ratio 0.87 with a 95% interval of 0.74
to 1.03."
**Source checked:** PMID 39604725

### BC-740  BS-6390 and BC-770  BS-6630
**Claim as written:** "overall survival was 47.9 against 48.1 months [@sonke2024]."
**Problem:** The SONIA overall survival figures are not in the abstract, which reports PFS2,
treatment duration and adverse events only.
**Correct value / fix:** Not verifiable from the abstract. UNVERIFIED, not wrong.
**Source checked:** PMID 39604725

### BC-680  BS-5750
**Claim as written:** "Taxane and platinum neuropathy is covered in [[BC-610]]."
**Problem:** Wrong chapter. BC-610 is "Young adults, fertility, and pregnancy". Chemotherapy-induced
peripheral neuropathy is BC-640 BS-5430.
**Correct value / fix:** "[[BS-5430]]".
**Source checked:** internal

### BC-660  BS-5670
**Claim as written:** "A survivorship programme that assumes an end date has nothing to offer
someone in year nine of continuous therapy. That population is addressed directly in [[BS-5570]]."
**Problem:** Wrong section. BS-5570 is "Bone health and cardiovascular risk after treatment".
Survivorship in metastatic disease is BS-5610.
**Correct value / fix:** "[[BS-5610]]".
**Source checked:** internal

### BC-770  BS-6600
**Claim as written:** "Most patients found to be ctDNA-positive already had detectable metastatic
disease on imaging at the time of detection, and pembrolizumab did not clear ctDNA."
**Problem:** The second clause carries no denominator, and the denominator is very small. Of those
allocated to intervention, 23 of 32 (72%) had metastases on staging, four declined, and only five
actually commenced pembrolizumab. None of those five achieved sustained clearance. A reader should
know the negative result rests on five patients, particularly since BS-6600 uses it to conclude
that residual disease detection "is not yet a treatment strategy".
**Correct value / fix:** "72% of those allocated to intervention already had metastases on staging
at the moment of ctDNA detection. Only five patients started pembrolizumab, and none achieved
sustained ctDNA clearance."
**Source checked:** PMID 36423745

### BC-760  BS-6540
**Claim as written:** "The nearer-term contribution in breast cancer is diagnostic rather than
therapeutic. Fluoroestradiol PET images oestrogen receptor expression across all sites of disease
simultaneously... their limitation is sensitivity for low-level expression rather than concept."
**Problem:** The opposite of the failure the chapter guards against elsewhere. 18F-fluoroestradiol
PET is not a nearer-term prospect, it is an approved and clinically available agent with guideline
standing. Placing it in a chapter of platforms "in development", and describing its limitation only
as assay sensitivity, understates its availability to a reader deciding whether they can order it.
The cited meta-analysis supports clinical utility rather than the between-lesion heterogeneity
claim it is attached to.
**Correct value / fix:** Say that FES PET is already approved and available, and give the
supporting number: across 12 studies and 308 participants, clinical benefit from endocrine therapy
followed a positive FES scan in 66% and a negative scan in 11%, risk ratio 3.21 (1.96 to 5.25).
**Source checked:** PMID 40081952

### BC-750  BS-6440
**Claim as written:** "In a randomised screening trial, AI-supported single reading against
standard double reading detected cancers at a comparable or higher rate while substantially
reducing reader workload [@lang2023]."
**Problem:** Both quantities are available and neither is given. "Substantially" is doing work a
number should do, in the one section of the chapter that claims computation has delivered.
**Correct value / fix:** Cancer detection rate 6.1 per 1000 screened against 5.1 per 1000, ratio
1.2 (1.0 to 1.5); screen-reading workload reduced by 44.3%; 80 033 women randomised. The later
analysis adds 105 934 women, detection ratio 1.29 (1.09 to 1.51, p = 0.0021), workload reduced
44.2%, with no significant increase in false positives.
**Source checked:** PMID 37541274, 39904652

### BC-700  BS-5980
**Claim as written:** "Among patients with early-stage, oestrogen receptor-positive, HER2-negative
disease in a population-based cohort of 2998 women, 62% had no 21-gene assay performed."
**Problem:** 2998 is the whole Carolina Breast Cancer Study Phase 3 cohort. The 62% applies to the
eligible early-stage, ER-positive, HER2-negative subset, which is smaller. BC-720 BS-6180 words it
correctly as "62% of those eligible", so the two chapters disagree.
**Correct value / fix:** "in a population-based cohort of 2998 women, 62% of those eligible had no
21-gene assay performed."
**Source checked:** PMID 39621782

### BC-690  BS-5870
**Claim as written:** "Breast cancer incidence rose 1.4% annually in women younger than 50 between
2012 and 2021, against 0.7% annually in women aged 50 and over."
**Problem:** The numbers are right, the qualification is dropped. The source states that the
steeper increase in the under-50 group "was only significant among White women". In a chapter
whose stated discipline is "stating what variable was measured, in every sentence that reports a
difference", the clause belongs.
**Correct value / fix:** Add that the difference between age groups was significant only among
White women.
**Source checked:** PMID 39352042

### BC-640  BS-5500
**Claim as written:** "In women who were postmenopausal when treatment began, recurrence fell with
a rate ratio of 0.86... Breast cancer mortality fell with a ratio of 0.82... Fractures were reduced
with a ratio of 0.85."
**Problem:** The first four ratios are the postmenopausal-restricted figures and are exact. The
fracture rate ratio of 0.85 (0.75 to 0.97) is the **overall** figure in the EBCTCG meta-analysis,
not the postmenopausal-restricted one, but the sentence sits inside a list introduced by "In women
who were postmenopausal when treatment began".
**Correct value / fix:** Move the fracture figure out of the postmenopausal list, or mark it as the
overall result: "Across the whole population, fractures were reduced with a ratio of 0.85."
**Source checked:** PMID 26211824

### BC-640  BS-5430
**Claim as written:** "One trial enrolled women with stage I or II disease receiving a taxane, an
anthracycline, or both. Scalp cooling made hair loss of less than 50% after the fourth cycle
significantly more likely than no cooling [@nangia2017]."
**Problem:** The effect size is extreme and is replaced by the word "significantly". This is the
one prevention in the section with a randomised result, and the number is the point.
**Correct value / fix:** "Hair preservation occurred in 48 of 95 cooled women (50.5%) and 0 of 47
controls, and the trial was stopped early for efficacy."
**Source checked:** PMID 28196254

### BC-650  BS-5540
**Claim as written:** "A systematic review of 72 studies found that overall more than one in five
women who survive breast cancer develop arm lymphoedema."
**Problem:** "More than one in five" is the source's own conclusion sentence, derived from the
prospective-cohort subset estimate of 21.4% (14.9 to 29.8). The pooled estimate across all 72
studies was 16.6% (13.6 to 20.2). Since this section's entire argument is that case definition and
study design drive the reported incidence, giving both numbers would make the point rather than
blunt it.
**Correct value / fix:** "Pooled incidence across 72 studies was 16.6%, and 21.4% when restricted
to the 30 prospective cohorts."
**Source checked:** PMID 23540561

### BC-660  BS-5640
**Claim as written:** "In a prospective cohort, socially isolated women had worse outcomes after
breast cancer diagnosis than socially integrated women [@kroenke2006]."
**Problem:** No number, for a claim the section explicitly labels "not a soft variable" and "a
biological finding as much as a psychosocial one". The effect is large and quantified.
**Correct value / fix:** "Socially isolated women had a 66% higher risk of all-cause mortality
(hazard ratio 1.66, 1.04 to 2.65) and roughly double the risk of breast cancer mortality (hazard
ratio 2.14, 1.11 to 4.12) compared with socially integrated women."
**Source checked:** PMID 16505430

### BC-630  BS-5370
**Claim as written:** "A prospective cohort of 448 men found reduced disease-free survival in those
not receiving tamoxifen [@eggemann2020]."
**Problem:** No effect size, in a section whose argument is that the male evidence base is thin and
that every number in it should be stated with its denominator.
**Correct value / fix:** "After adjustment for prognostic factors, tamoxifen reduced the recurrence
rate by 68%, hazard ratio 0.32 with a 95% interval of 0.14 to 0.74."
**Source checked:** PMID 32367072

### BC-650  BS-5580
**Claim as written:** "Higher body mass index was associated with more recurrences in an
exploratory analysis of an adjuvant endocrine therapy trial, and the association was stronger on
anastrozole than on tamoxifen [@sestak2010]."
**Problem:** The direction is right and the significance is overstated. The ATAC analysis reports
that "the relative benefit of anastrozole versus tamoxifen was **nonsignificantly** better in thin
women compared to overweight women". The second clause is stated here as an established
interaction. No numbers are given for the BMI-recurrence association either.
**Correct value / fix:** "Women with a body mass index above 35 had more recurrences than those
below 23, adjusted hazard ratio 1.39 (1.06 to 1.82). The relative benefit of anastrozole over
tamoxifen was greater in thinner women, but that interaction did not reach significance."
**Source checked:** PMID 20547990

### BC-620  BS-5320
**Claim as written:** "Among patients with metastatic breast cancer receiving capecitabine, about
25% were sarcopenic on computed tomography... Toxicity after the first cycle occurred in 50% of
sarcopenic patients against 20% of non-sarcopenic patients [@prado2009]."
**Problem:** All percentages correct; the denominator is 55 women. A 50-against-20 percent
difference in a 55-patient cohort reads very differently with the denominator attached, and this is
the evidence on which the chapter's dosing argument rests.
**Correct value / fix:** Add "in a cohort of 55 women".
**Source checked:** PMID 19351764

### BC-760  BS-6550
**Claim as written:** "The honest current position is that this class has strong mechanistic
justification, no established role in breast cancer, and a plausible future as combination
partners."
**Problem:** Globally this is not quite true. The HDAC inhibitor tucidinostat with exemestane is
approved in China for hormone receptor-positive, HER2-negative advanced breast cancer on the basis
of a positive randomised trial. In a book that devotes a full chapter to the fact that treatment
availability differs by country (BC-710), an unqualified "no established role" is a high-income
statement presented as a global one.
**Correct value / fix:** "no established role in breast cancer outside China, where an HDAC
inhibitor is approved with exemestane in the hormone receptor-positive setting."
**Source checked:** not verifiable from the references currently in references.yaml; flagged for
the author to confirm and source.

### BC-780  BS-6720
**Claim as written:** "Survival differs several-fold between high-income and low-income settings."
**Problem:** Overstates the book's own figures. The WHO estimates cited in BC-710 give median
5-year net survival of 39.1% in the African Region against 88.5% in the Region of the Americas,
a 2.3-fold difference; CONCORD-3 gives 90.2% in the United States against 66.1% in India, a
1.4-fold difference. "Several-fold" is not supported by either source. BC-710's own subtitle states
it accurately as "under 40% to near 90%".
**Correct value / fix:** "Five-year survival runs from under 40% in the WHO African Region to near
90% in the Region of the Americas."
**Source checked:** PMID 42420542, 29395269

## Verified correct, spot-check record

These were checked against source and reproduced exactly. Listing them so the same ground is not
re-covered.

- BC-690 BS-5860: 38% mortality gap, 5% lower incidence, 58% against 68% localised, lowest survival
  in every subtype and stage except localised (PMID 39352042). All exact.
- BC-690 BS-5860: ko2020 20% against 11% stage III, odds ratio 1.46 falling to 1.29, 45 to 47%
  mediated by insurance (PMID 31917398). Exact.
- BC-690 BS-5860 and BS-5920: TAILORx 9719 enrolled, no RS or ESR1/PGR/HER2 difference by race,
  distant recurrence hazard ratio 1.60 (1.07 to 2.41), overall survival 1.41 (1.05 to 1.90),
  693 Black women, 7.1% (PMID 32986828). Exact.
- BC-690 BS-5860 and BS-5910, BC-700 BS-5990: Military Health System 998 against 3899, 22 against
  21 days median, 3.6 and 8.9 days at the 75th and 90th percentiles, breast-conserving surgery
  hazard ratio 1.45 (1.06 to 2.01), unchanged by adding time to surgery (PMID 30673075). Exact.
- BC-690 BS-5830: Plascak 14 964, odds ratios 0.34, 0.67 and hazard ratio 0.48, present only in
  non-Latina White women (PMID 35802373). Lima 60 773, 29%, 37%, 64%, persisting after adjustment
  for insurance and treatment, elevated risk in D-graded tracts specific to non-Hispanic White
  cases (PMID 40178940). Both exact, including the counterintuitive direction the caution block
  is built on.
- BC-690 BS-5840, BS-5910, BC-700 BS-5980, BC-720 BS-6170: Lawson 46 185 mammograms, 45 186 women,
  109 facilities, six states; 34.6%, 16.2%, 12.2%; relative risks 1.52 Black, 1.66 Asian, 1.50
  Hispanic at 30 days; 1.28 (1.11 to 1.47) at 90 days; sequential adjustment 1.28 to 1.27 to 1.20
  (PMID 35737381). Every figure exact, including which step of the adjustment moved the estimate.
- BC-690 BS-5880: Yu 910 415 total, 63 405 Asian, 5.9% against 2.7% stage IV, 89.4% (88.7 to 90.1)
  against 78.0% (74.1 to 81.3), Southeast Asian the only subgroup without better adjusted overall
  survival than White women (PMID 34792814). Exact, including the reversal the section turns on.
- BC-690 BS-5870: Carolina Breast Cancer Study 496 cancers, basal-like 39% against 14% and 16%,
  luminal A 36% against 59% and 54%, HER2+/ER- not varying (PMID 16757721). Exact.
- BC-690 BS-5930: Loree 230 trials, 63.0%, 7.8%, 112 293 participants, 3.1/6.1/76.3/18.3%, 22%,
  44% and 98% of expected (PMID 31415071). Unger 13 studies, 8883 patients, 55.6% (43.7 to 67.3),
  21.5%, 14.8%, 8.1% (PMID 30856272). Wendler 20 studies, over 70 000 individuals, 45.3% against
  41.8%, odds ratio 1.06 (0.78 to 1.45); 55.9% against 41.8%, odds ratio 1.33 (1.08 to 1.65)
  (PMID 16318411). All exact.
- BC-690 BS-5900: Keenan 42.9/27.6%, 20.0/33.9%, 5.1 units (2.4 to 7.7), 39.0/18.6% (PMID
  26371147). Ademuyiwa 1104 patients, 46/27%, 23/34%, no difference within triple-negative (PMID
  27915434). Yao 462 women, portrait resembling Asian and non-Hispanic White, no ancestry
  association (PMID 40858906). Van Alsten 357 against 948, 52% and 18% Black, TP53 and FAT1 up,
  PIK3CA/CDH1/DDR2/GATA3 down, higher aneuploidy, socioeconomic patterning (PMID 39879109). All
  exact, and the synthesis paragraph is a fair reading of all four.
- BC-690 BS-5810, BS-5820: allostatic load hazard ratio 1.46, mean load higher in Black patients,
  dose-dependent gradient across quartiles (PMID 37200034). Exact.
- BC-700 BS-5970: COST validated in 233 stage IV patients, single latent variable, correlations
  with income, distress and two quality-of-life instruments, willingness to discuss costs not
  associated with distress (PMID 27716900). Ramsey 4728 filings among 231 596, 3841 matched per
  group, hazard ratio 1.79 (1.64 to 1.96) (PMID 26811521). Exact.
- BC-700 BS-6030, BC-720 BS-6160 and BS-6230: Freund 10 521 and 2105, 73%/40%/31%, no benefit in
  the first 90 days, 1.51 (1.23 to 1.84) and 1.43 (1.10 to 1.86) from 91 to 365 days, greatest
  benefit where usual-care delays were longest (PMID 24938303). Exact, including the null half
  the chapter makes its point from.
- BC-710 BS-6040: 2.3 million cases and 685 000 deaths in 2020, over 3 million and 1 million by
  2040, under 40 to over 80 per 100 000 (PMID 36084384). BS-6050: 39.1% (34.1 to 44.7), 61.0%,
  66.3%, 81.1%, 84.0%, 88.5% (PMID 42420542); 90.2% and 66.1% (PMID 29395269). All exact.
- BC-710 BS-6050 and BS-6070: Ghana 214 staged, 10.3% stage I/II, 50% stage III, 39.3% stage IV,
  all diagnosed within 31 days, 45 of 243 (18.5%) completing treatment, 2.5% annual mortality
  reduction goal (PMID 40324119). ABC-DO 22 to 49% on the first two indicators, under 30% on the
  third (PMID 40034567). Exact.
- BC-710 BS-6090 and BC-720 BS-6230: Mumbai 20 clusters, 151 538 women aged 35 to 64, four
  screening rounds, 37% against 47% stage III/IV, 20.82 against 24.62 per 100 000 person-years,
  rate ratio 0.85 (0.71 to 1.01), post hoc 0.71 (0.54 to 0.94) over 50 and 0.93 (0.79 to 1.09)
  under 50 (PMID 33627312). Exact, and the caution block correctly identifies the 30% figure as
  post hoc.
- BC-710 BS-6110 and BC-700 BS-6000: Fundytus 948 oncologists, 82 countries, 19 of 20 on the
  Essential Medicines List, 12 cytotoxic, 13 approved before 2000, availability 9 to 54% / 13 to
  90% / 68 to 94%, catastrophic expenditure 13 to 68% against 0 to 9%, 40% of household
  consumption net of food (PMID 34560006). Every figure exact.
- BC-710 BS-6120: 2.2 million additional patients, 1.4 million with breast cancer (PMID 39362232);
  5 billion lacking access to surgery (PMID 28588908). Exact.
- BC-720 BS-6190: 21 Asian countries, over 60% with no national staging or interval data, five of
  21 reporting treatment completion, varying definitions (PMID 38125964). Exact.
- BC-720 BS-6200 and BS-6230: Medicaid expansion 9322 patients, adjusted hazard ratio 1.22 (1.10 to
  1.35) before and 0.96 (0.86 to 1.08) after (PMID 35389432); 3.62 points (1.63 to 5.61) at 30
  days, no change at 90 days, no change at minority-serving hospitals (PMID 33974827). Exact, and
  the pairing of the two is a fair reading.
- BC-720 BS-6220: Health Equity Implementation Framework, hepatitis C application, general against
  group-specific barriers (PMID 30866982). Accurate.
- BC-740 BS-6360: CTNeoBC 12 trials, 11 955 patients, event-free survival hazard ratio 0.48 and
  overall survival 0.36 for ypT0/is ypN0, strongest in triple-negative and in HER2-positive
  hormone-receptor-negative disease treated with trastuzumab, trial-level R-squared 0.03 for
  event-free survival and 0.24 for overall survival, authors explicit that surrogacy was not
  validated (PMID 24529560). Every figure exact. This is the best-executed passage in the chapter.
- BC-740 BS-6370: IMPORT LOW 1.1% against 0.5% at 5 years (PMID 28779963); FAST-Forward 26 Gy in
  five fractions non-inferior to 40 Gy in fifteen (PMID 32580883); SENOMAC 89.7% against 88.7%,
  hazard ratio 0.89 (0.66 to 1.19) (PMID 38598571). All exact.
- BC-740 BS-6380 and BS-6420: 78 of 132 drugs, 59.1% (PMID 38085161); 19 of 93, 20%, with 19
  confirming the same surrogate and 20 a different one (PMID 31135808); ASCENT 12.1 against 6.7
  months (PMID 33882206); TROPiCS-02 14.4 against 11.2 months (PMID 37633306). All exact.
- BC-750 BS-6440: pathologist overall percent agreement 25% for IHC 0 (PMID 36788069); 10 models,
  1124 slides, 733 patients, 65.1% median pairwise agreement, kappa 0.51, 97.3% for 3+ against not
  3+, lowest in HER2-low, pathologists numerically higher (PMID 41489584). Exact, and the caution
  block's conclusion that reproducibility has been relocated rather than solved is the right
  reading.
- BC-750 BS-6490: 17.7% to 46.5% (PMID 31649194). Exact.
- BC-610: partridge2016 17 575 and 1916, 6.4 years, hazard ratio 1.4 (1.2 to 1.7), luminal A 2.1
  (1.4 to 3.2), luminal B 1.4 (1.1 to 1.9), borderline in triple-negative, absent in HER2-positive
  (PMID 27480155). POEMS 135 with complete data, 8% against 22%, odds ratio 0.30 (0.09 to 0.97)
  (PMID 25738668). Lambertini five trials, 873 patients, 14.1% against 30.9%, adjusted odds ratio
  0.38 (0.26 to 0.57), pregnancy 10.3% against 5.5% (PMID 29718793). Nichols 15 studies, risk
  elevated beyond 20 years, crossover only for ER-positive, modified by family history, age at
  first birth and parity, not by breastfeeding (PMID 30534999). Goddard 10-year window, greatest
  in stage I and II, both receptor groups, persisting 15 years in receptor-positive, more
  lymphovascular invasion and nodal involvement, no Ki67 increase (PMID 30646210). Amant 129
  children, 96 chemotherapy-exposed, no Bayley difference, normal cardiac evaluation, prematurity
  the driver (PMID 26415085). POSITIVE 516 women, median age 37, 93.4% stage I or II, 497 followed,
  368 pregnancies, 317 live births, 1638 patient-years, 44 events against a threshold of 46, 8.9%
  against 9.2%, median follow-up 41 months (PMID 37133584). Lambertini 2021 relative risk 0.40
  (0.32 to 0.49), disease-free survival 0.66, overall survival 0.56, no congenital excess (PMID
  34197218). Arecco 0.96 (0.75 to 1.24) and 0.46 (PMID 37879234). Hershman 8769, 32%, 72%, 49%,
  under-40 hazard ratio 1.51 (1.23 to 1.85) (PMID 20585090). McGale 476 373, 3.1 points, greater
  in younger women (PMID 40865997). Every number in the chapter is exact.
- BC-620: GAP70+ 40 practices, 718 patients, 51% against 71%, relative risk 0.74 (0.64 to 0.86),
  falls 12% against 21% (PMID 34741815). Handforth 20 studies, 2916 patients, 42% (6 to 86) and
  43% (13 to 79) (PMID 25403592). CALGB 49907 633 women, 11.4 years, 56%/50% hazard ratio 0.80,
  88%/82% hazard ratio 0.62, 62%/56% hazard ratio 0.84 not significant (PMID 31339827). PRIME II
  1326 women, 9.1 years, 9.5% against 0.9%, 80.8% against 80.7% (PMID 36791159). CARG-BC 473
  patients, 46%, the eight predictors named exactly, 19/54/87% (PMID 33444080). Mohamed 47 studies,
  57%, 4 of 9, 3 of 3 (PMID 31570516). Maggiore 500 adults, mean five medications, range 0 to 23
  (PMID 25041361). Rae CYP2D6 not associated with recurrence (PMID 22395643). Henricks
  genotype-guided reduction improved safety (PMID 30348537). All exact.
- BC-630: Cardoso 1822 enrolled, 1483 analysed, 68.4 years, 99.3/81.9/96.9%, 76.8% endocrine
  therapy of which 88.4% tamoxifen, 4% conservation, 18% sentinel node (PMID 29092024). Eggemann
  2018 89.2% against 85.1% on tamoxifen, 73.3% in 30 men against 85.0% in 60 women on aromatase
  inhibitor (PMID 29098396). De Blok 2260 trans women, 33 991 person-years, 15 cancers, median 18
  years of hormone treatment, standardised incidence ratio 46.7 (27.2 to 75.4) and 0.3 (0.2 to
  0.4), 1229 trans men, 14 883 person-years, four cancers (PMID 31088823). WHI 27 347 women, 16 608
  with a uterus, 584 at 0.45% against 447 at 0.36%, hazard ratio 1.28 (1.13 to 1.45), no mortality
  difference, oestrogen alone lower incidence and lower mortality (PMID 32721007). Morch 1.8
  million women, 10.9 years, 11 517 cancers, 1.20 (1.14 to 1.26), 1.09 to 1.38 by duration (PMID
  29211679). All exact. The BS-5380 caution about a 46-fold ratio on a near-zero baseline is a
  correct and well-made point.
- BC-640: Seretny 31 studies, 4179 patients, 68.1%/60.0%/30.0% (PMID 25261162). Rugo 27.3% against
  56.3% (PMID 28196257). Andre 36.6% against 0.7%, 9.9% against 0.3%, 25.0% against 4.2% (PMID
  31091374). Turner 12.1% against 0.3%, 9.3% against 0.3%, 13.0% against 2.3% (PMID 37256976).
  Powell 1150 patients, 15.4%, grade 5 2.2%, 77.4% grade 1 or 2, 87.0% within 12 months, median 5.4
  months, adjudication earlier for 53.2% by a median of 43 days (PMID 35963179). DESTINY-Breast03
  10.5% against 1.9% (PMID 35320644). ASCENT neutropenia 51% against 33%, diarrhoea 10% against
  under 1% (PMID 33882206). Cardinale 9%, 3.5 months, 98% within a year, 11% full and 71% partial
  recovery (PMID 25948538). Ewer 38 patients, 0.61 to 0.43 to 0.56, 1.5 months, 3 of 25 on
  rechallenge (PMID 16258084). Darby 2168 women, 963 cases and 1205 controls, 4.9 Gy, 7.4% per
  gray, no threshold (PMID 23484825). ABCSG-18 3420 women, hazard ratio 0.50 (0.39 to 0.65), 92
  against 176 fractures, benefit above and below a T-score of minus 1, no osteonecrosis (PMID
  26040499). EBCTCG 0.86 (0.78 to 0.94), 0.82, 0.72, 0.82 (0.73 to 0.93) (PMID 26211824). McGale
  13.6% and 2.1 points, 5.6% and 3.1 points, therapy associations by class, under 1% absolute
  excess for each non-breast type, 7% of excess attributable to adjuvant therapy (PMID 40865997).
  All exact. The trastuzumab deruxtecan interstitial lung disease management thresholds in the
  practice block match label guidance.
- BC-650: GIVIO 1320 women, 71 months, 132 against 122 deaths, no difference in time to detection
  or quality of life (PMID 8182811). Rosselli Del Turco 1243 patients, more and earlier
  intrathoracic and bone metastases, 18.6% against 19.5% (PMID 7848404). Ridner 508 patients, 4.9%
  against 14.7%, about 10 points, not significant (PMID 31054038). Schmitz 141 survivors, 11%
  against 12%, fewer exacerbations, greater strength (PMID 19675330). Janelsins 581 and 364, 45.2%
  against 10.4%, 36.5% against 13.6%, regimen and hormone and radiotherapy not associated (PMID
  28029304). Holmes relative risk 0.50 (0.34 to 0.74), 6 points absolute at 10 years, 3 to 5 hours
  of walking (PMID 15914748). CHALLENGE 90.3% against 83.2% at 8 years, hazard ratio 0.63 (0.43 to
  0.94) (PMID 40450658). WHI dietary 19.6 years, 0.85 (0.74 to 0.96) and 0.79 (0.64 to 0.97) (PMID
  32031879). MA.32 no invasive disease-free survival improvement (PMID 35608580). Grunfeld 968
  patients, 17 (3.5%) against 18 (3.7%), 0.19 points (minus 2.26 to 2.65), 54 against 64
  recurrences, 29 against 30 deaths (PMID 16418496). Mariotto 154 794 women, three in four from
  stage I to III (PMID 28522448). All exact.
- BC-680: Temel 11.6 against 8.9 months (PMID 20818875). Bakitas 322 patients, quality of life and
  mood improved, symptom intensity and service use unchanged (PMID 19690306). Zimmermann 24 clinics,
  3.56 points at three months with P = 0.07, secondary endpoints met at four months (PMID
  24559581). Wright 332 dyads, 37.0%, 8.3% against 5.8%, ventilation 11.0 to 1.6%, resuscitation
  6.7 to 0.8%, intensive care 12.4 to 4.1%, hospice 44.5 to 65.6%, caregiver odds ratio 3.37 (PMID
  18840840). Guo 27 862 matched adults, hospice 52.4 to 71.0% and 63.2 to 80.4%, three-day
  enrolment 44.0 to 65.5% and 52.6 to 74.2%, no interaction on any outcome (PMID 40566741). All
  exact. The palliative care survival position in the caution block is correct and correctly
  sourced.
- BC-760 and BC-770: VERITAC-2 270 ESR1-mutant patients, 5.0 against 2.1 months, hazard ratio 0.58;
  624 randomised, 3.8 against 3.6 months, hazard ratio 0.83, P = 0.07 (PMID 40454645). LUMINA 2.3%
  5-year local recurrence (PMID 37585627). CLEVER described accurately as an approach taken rather
  than a result claimed (PMID 40897974). DESTINY-Breast04 and DAISY correctly used to make the
  bystander-delivery point (PMID 35665782, 37488289). DESTINY-Breast12 intracranial activity
  correctly described (PMID 39271844). No agent in either chapter is described as approved when it
  is investigational. Vepdegestrant, patritumab deruxtecan, B7-H3 and LIV-1 conjugates, bispecific
  T-cell engagers, CAR-T, neoantigen vaccines, CDK7/CDK9 inhibitors and adaptive dosing are all
  correctly presented as investigational. The only error in this direction runs the other way and
  is the FES PET item filed above.

## Summary

**BLOCKER: 0.  MAJOR: 7.  MINOR: 15.**

The three things most worth fixing before merge:

1. **BC-740 BS-6370, the NSABP B-51 counterexample names the wrong end of the confidence
   interval.** The bound that defeats an equivalence reading is 0.60, not 1.28. This sits in the
   one section of the book whose explicit job is to teach the reader which side of the interval a
   non-inferiority claim depends on, and as written it teaches the inverse. Cheap to fix, expensive
   to leave.

2. **BC-740 BS-6340 uses SOLAR-1 and CAPItello-291 as examples of biomarker-selected trials with
   no marker-negative arm.** SOLAR-1 had a marker-negative cohort and reported its hazard ratio.
   CAPItello-291 did not select on biomarker at all. Both are counterexamples to the category. The
   same error appears in BC-690 BS-5900, which states that entry to SOLAR-1 required a PIK3CA
   alteration; the downstream argument there survives because the approval is biomarker-restricted
   even though the trial was not.

3. **SERENA-6 is invoked three times with no number and described as changing "outcomes".** The
   demonstrated benefit is on progression-free survival and second progression-free survival, not
   on survival, and BC-740 BS-6420 explicitly forbids conflating the two. Add 16.8 against 9.2
   months, hazard ratio 0.45, and name the endpoint.

Two further items worth attention: the monarchE 7-year figures in BC-670 BS-5690 are attached to
the 2020 interim report, which contains 2-year figures and no survival result; and the
mardamshina2025 claim, repeated in three chapters and load-bearing in BC-780 BS-6710, names
transcriptional classification as the comparator when the study compared spatial proteomics against
immunohistochemical receptor classification.

Note on the disparities chapters: BC-690, BC-700 and BC-710 were the flagged risk area and are the
strongest chapters in the range. Roughly sixty individual disparity figures were checked against
source and all reproduced, including the ones most often misquoted in this literature, the redlining
studies whose associations appear in White and not Black women, the Southeast Asian survival
reversal, the Wendler consent-rate finding and the Unger barrier sequence. The two minor items filed
against them are a dropped significance qualification and a misplaced denominator.
