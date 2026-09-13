# Audit: cross-reference integrity, thread resolution, and internal contradictions (all 79 chapters)

Scope: every `[[BC-###]]`, `[[BS-####]]` and `interplay target=` pointer; every promised
resolution ("taken up in", "resolves in", "is developed in", "set out in"); numerical and conceptual
contradictions between chapters; orphans and duplication.

**Structural check passed.** A script resolved all 518 `[[BC-###]]`, 646 `[[BS-####]]` and 47
`interplay target=` pointers against `outline.yaml`. Every one resolves to a real id. No malformed
tokens, no self-references, no pointers to non-existent appendices. The failures below are semantic:
the pointer resolves, but the target does not contain what the sentence says it contains.

---

## BLOCKER

None. No finding in this scope meets the kit's BLOCKER bar of a wrong hazard ratio, survival figure,
dose or indication. Every trial statistic that appears in more than one chapter was compared and they
agree: KEYNOTE-522, KATHERINE, CREATE-X, TAILORx, RxPONDER, MINDACT, monarchE, SOFT-TEXT, OlympiA,
OlympiAD, EMBRACA, TBCRC 048, SOLAR-1, CAPItello-291, INAVO120, EMERALD, EMBER-3, SERENA-6, PALOMA-3,
SONIA, DAISY, DESTINY-Breast04 and 06, HER2CLIMB, DESTINY-Breast12, TROPiCS-02, ASCENT, KEYNOTE-355,
PRIME II, LUMINA and CTNeoBC. Where two chapters give different figures for the same trial, each
correctly names the analysis it is reporting. The closest approaches to a BLOCKER are the palliative
care contradiction, the SONIA endpoint definition and the lymphoedema incidence, all under MAJOR.

---

## MAJOR

### BC-680  BS-5750 — skeletal biology pointed at the HER2 chapter
**Claim as written:** "Bone metastasis dominates it, and the skeletal biology that drives it is in [[BC-570]]."
**Problem:** BC-570 is *Metastatic HER2-positive disease*. Zero occurrences of "skeletal" or
"osteoclast" in that file. The skeletal biology is BC-320 BS-2750 (*Bone, liver, lung, and brain
microenvironments compared*, which carries the `@kang2003` osteolytic cooperative programme); the
management is BC-600 BS-5190 (*Bone metastases and skeletal-related events*).
**Correct value / fix:** "...the skeletal biology that drives it is in [[BS-2750]], and its management in [[BS-5190]]."
**Source checked:** internal (grep BC-570 / BC-600 / BC-320)

### BC-680  BS-5750 — taxane and platinum neuropathy pointed at the young-adults chapter
**Claim as written:** "Neuropathic pain in this population usually has a name. Taxane and platinum neuropathy is covered in [[BC-610]]."
**Problem:** BC-610 is *Young adults, fertility, and pregnancy*. Zero occurrences of "neuropath".
The material is BC-640 BS-5430 (*Acute and chronic cytotoxic toxicity*). BC-640 BS-5490 itself points
at BS-5430 for exactly this.
**Correct value / fix:** `[[BS-5430]]`
**Source checked:** internal (grep BC-610 = 0 hits, BC-640 = 4 hits)

### BC-700  BS-5990 and BC-710  BS-6120 — hypofractionation evidence pointed at the in situ chapter
**Claim as written:** (BC-700) "The clinical evidence for hypofractionation is developed in [[BC-480]]."
(BC-710) "It requires a change in schedule... The evidence base sits in [[BC-480]]."
**Problem:** BC-480 is *Atypia and in situ disease* and contains zero occurrences of
"hypofractionation". The evidence is BC-420 BS-3740 (*Fractionation, hypofractionation, and
acceleration*). Both chapters build a health-systems argument on that evidence and send the reader
somewhere that cannot supply it. In BC-710 the sentence is the load-bearing justification for a claim
that 1.4 million additional breast cancer patients could be treated with existing resources.
**Correct value / fix:** both `[[BS-3740]]`
**Source checked:** internal (grep BC-480 = 0 hits, BC-420 = 2 hits)

### BC-740  BS-6400 — ancestry-associated tumour biology pointed at the affordability chapter
**Claim as written:** "This matters biologically and not only ethically. Ancestry-associated differences in tumour biology are documented in [[BC-700]]."
**Problem:** BC-700 is *Access, affordability, and financial toxicity*, zero occurrences of
"ancestry". The material is BC-690 BS-5900, *Ancestry-associated tumor biology, what replicates and
what is confounded*. The mis-pointer matters beyond navigation: BS-5900's stated position is that most
such claims rest on cohorts where race was recorded and ancestry was not, which is the caveat this
sentence needs and loses.
**Correct value / fix:** `[[BS-5900]]`
**Source checked:** internal (grep BC-700 = 0 hits, BC-690 = 15 hits)

### BC-750  BS-6470 — genomic assays pointed at the screening chapter
**Claim as written:** "This is the distinction that separates the genomic assays in [[BC-360]] from ordinary prognostic scores. {{trial:tailorx}} and {{trial:rxponder}} were run because a prognostic score, however accurate, does not establish that withholding chemotherapy is safe."
**Problem:** BC-360 is *Screening and early detection*. Genomic assays, TAILORx and RxPONDER are BC-380
(*Prognostic and predictive assays and somatic profiling*) and BC-490 BS-4300 (*Genomic assays and the
decision to omit chemotherapy*).
**Correct value / fix:** `[[BC-380]]`, or `[[BS-4300]]` for the clinical application
**Source checked:** internal

### BC-730  BS-6240 — TNBC transcriptional programmes pointed at the cell cycle chapter
**Claim as written:** "MDA-MB-231 carries a disproportionate share of what is claimed about triple-negative disease, despite being a poor representative of the common triple-negative transcriptional programmes described in [[BC-160]]."
**Problem:** BC-160 is *Cell cycle regulation*. TNBC transcriptional programmes are BC-120, specifically
BS-1060 (*Why TNBC classifiers disagree with one another*) and BS-1050.
**Correct value / fix:** `[[BC-120]]` or `[[BS-1060]]`
**Source checked:** internal

### BC-780  BS-6680 — non-genetic tolerance pointed at the dissemination chapter
**Claim as written:** "Non-genetic tolerance is a reversible transcriptional state that does not require mutation and is described in [[BC-320]]."
**Problem:** BC-320 is *Metastatic dissemination and organ tropism*. Reversible drug-tolerant states are
BC-310 (*Plasticity and non-genetic heterogeneity*). The book routes there consistently elsewhere
(BC-300 BS-2550, BC-345 BS-2970, BC-200 BS-1630).
**Correct value / fix:** `[[BC-310]]`
**Source checked:** internal

### BC-780  BS-6690 and BC-760  BS-6530 — TIL work pointed at the host-factors chapter
**Claim as written:** (BC-780) "The TIL work in [[BC-250]] is the strongest signal and is not sufficient as a single marker."
(BC-760) "It requires resectable tumour with adequate lymphocyte infiltration, which reconnects it to the TIL biology in [[BC-250]]."
**Problem:** BC-250 is *Host and tumor interactions* and contains **zero** occurrences of the word
"lymphocyte". TIL biology and standardised scoring is BC-210 BS-1660; the subtype distribution is
BC-210 BS-1700.
**Correct value / fix:** both `[[BS-1660]]`
**Source checked:** internal (grep BC-250 = 0, BC-210 = 21)

### BC-780  BS-6690 and BC-760  BS-6520 — immune escape pointed at the stromal-architecture chapter
**Claim as written:** (BC-780) "The mechanisms of acquired immune escape in [[BC-220]] are described and not yet targetable."
(BC-760) "This bypasses antigen presentation entirely, which is the step most reliably lost in the immune evasion described in [[BC-220]]."
**Problem:** BC-220 is *Cellular architecture of the tumor microenvironment*: fibroblasts, myeloid
cells, endothelium, adipocytes, matrix, nerves. Its one immune section, BS-1740, is fibroblast
**exclusion**, a different mechanism from antigen-presentation loss. Acquired immune escape is BC-230
BS-1930; MHC and antigen presentation loss is BC-230 BS-1890.
**Correct value / fix:** BC-780 -> `[[BS-1930]]`; BC-760 -> `[[BS-1890]]`
**Source checked:** internal

### BC-650  BS-5610 contradicts BC-680  BS-5740 on whether early palliative care extends survival
**Claim as written (BC-650, inside a `caution` block):** "Early integration of palliative care improves
quality of life and, in some settings, survival [@temel2010], and that argument is in [[BS-5740]]."
**Problem:** BS-5740 is the section that argues the opposite, and says so in its own `caution` block:
"Do not sell early palliative care on survival. The pooled evidence does not support it, and a
colleague who checks the meta-analysis will discount everything else you said." It gives the
Kavalieratos meta-analysis of 43 trials in 12,731 patients with a survival hazard ratio of 0.90 (0.69
to 1.17). BC-550 handles the same trial correctly: "The population was lung cancer and the result
should not be transferred to breast cancer as a survival claim." So BC-650 both asserts a claim the
book rejects and points the reader at the section that rejects it, as if for support. This is the
worst kind of mis-pointer, because it is a promise to a target that refutes the promise.
**Correct value / fix:** "Early integration of palliative care improves quality of life and symptom
burden. The survival evidence does not support a survival claim, and the reasoning is in [[BS-5740]]."
**Source checked:** internal; BS-5740 and @kavalieratos2016 as quoted there

### Eight papers carry two separate reference keys, split across different chapters
**Claim as written:** n/a, this is a registry defect visible only across chapters.
**Problem:** `references.yaml` contains eight pairs of entries with identical DOI, PMID, title, journal,
volume and pages. They are separate entries, not aliases (the file does use an `alias` mechanism
elsewhere, 49 times). In every case the two keys are used by different chapters, which is the
signature of parallel authoring:

| Paper | Key A (chapters) | Key B (chapters) |
|---|---|---|
| EBCTCG tamoxifen 2011 (PMID 21802721) | `davies2011` (BC-010) | `ebctcg2011tam` (BC-430) |
| EBCTCG radiotherapy 2011 (PMID 22019144) | `ebctcg2011` (BC-520, BC-530) | `ebctcg2011rt` (BC-420) |
| EBCTCG OFS 2022 (PMID 35123662) | `ebctcg2022` (BC-490) | `ebctcg2022ofs` (BC-430) |
| NSABP B-06 (PMID 12393820) | `fisher2002` (BC-410) | `fisher2002b06` (BC-010) |
| GeparNuevo primary (PMID 31095287) | `loibl2019` (BC-510) | `loibl2019geparnuevo` (BC-540) |
| GeparNuevo update (PMID 35961599) | `loibl2022` (BC-510) | `loibl2022geparnuevo` (BC-540) |
| KEYNOTE-522 EFS (PMID 35139274) | `schmid2022` (BC-540) | `schmid2022k522efs` (BC-510) |
| PALOMA-3 cyclin E1 (PMID 30807234) | `turner2019` (BC-345, BC-450, BC-560) | `turner2019ccne1` (BC-160) |

Consequences: APP-I (*Full bibliography with cited-in backlinks*) will list each of these papers twice
under two numerals, and the backlinks will be split so a reader following one sees only half the
chapters that cite the paper. Two chapters reporting the same numbers from the same paper will appear
to be citing different sources. `CONVENTIONS.md` is explicit: "Never rename a key. Add an alias
instead."
**Correct value / fix:** keep one key per paper and convert the other to an alias. Note the entries
also disagree on metadata: `loibl2019` carries `trial: geparnuevo` and `type: trial` while
`loibl2019geparnuevo` carries `type: primary`, and the same split exists for schmid2022.
**Source checked:** `references.yaml`, DOI and PMID identity

### BC-740  BS-6390 misstates what SONIA's primary endpoint measures, contradicting BC-770
**Claim as written:** (BC-740) "Progression-free survival **from the second line onward** was 31.0
against 26.8 months and not statistically significant."
(BC-560 BS-4820) "Median progression-free survival **after two lines** was 31.0 months against 26.8
months."
(BC-770 BS-6630) "no significant difference in progression-free survival **from randomisation to second
progression**, at 31.0 against 26.8 months."
**Problem:** SONIA's primary endpoint (PFS2) is time from randomisation to progression after
second-line treatment. BC-770 states this correctly. BC-740's "from the second line onward" names a
different time origin, and BC-560's "after two lines" is ambiguous. The error is worst in BC-740,
whose whole section is about reading endpoints precisely, and the book's own rule is to say what a
number is a number of.
**Correct value / fix:** "Progression-free survival from randomisation to progression after second-line
treatment was 31.0 against 26.8 months, hazard ratio 0.87, 95% CI 0.74 to 1.03, P = 0.10."
**Source checked:** PubMed PMID 39604725 (Sonke et al, Nature 2024, DOI 10.1038/s41586-024-08035-2),
which defines the primary endpoint as "the time from randomization to disease progression after
second-line treatment (progression-free survival 2 (PFS2))"

### SONIA overall survival figures are attributed to two different sources in different chapters
**Claim as written:** (BC-430 BS-3850) "overall survival of 47.9 and 48.1 months ... [@sonke2024]";
(BC-740 BS-6390) "overall survival was 47.9 against 48.1 months [@sonke2024]";
(BC-770 BS-6630) "overall survival was 47.9 against 48.1 months"; (BC-560 BS-4820) "Median overall
survival was 47.9 months against 48.1 months, with a hazard ratio of 0.91 [@wortelboer2026]."
**Problem:** the same two medians are attributed to `@sonke2024` in three chapters and to
`@wortelboer2026` in a fourth. The Nature 2024 primary report does not present overall survival
medians; its reported outcome is PFS2. One of the two attributions is wrong and they cannot both be
the source of the same figure.
**Correct value / fix:** attribute the OS medians to the single report that contains them, in all four
chapters. Add the hazard ratio (0.91) in all four, since three of them give the medians without it.
**Source checked:** PubMed PMID 39604725 abstract, which reports PFS2 and not OS medians

### BC-410 and BC-650 give incompatible headline lymphoedema incidences from the same review
**Claim as written:** (BC-410 BS-3690) "In a systematic review of 72 studies the pooled incidence of
unilateral arm lymphoedema after breast cancer was 16.6%, with a 95% confidence interval of 13.6% to
20.2% [@disipio2013]."
(BC-650 BS-5540) "A systematic review of 72 studies found that overall **more than one in five** women
who survive breast cancer develop arm lymphoedema ... [@disipio2013]."
**Problem:** both sentences are accurate quotations of the same paper, and they are incompatible as a
reader receives them. 16.6% is not more than one in five. The reconciliation, which neither chapter
supplies, is that 16.6% is the pooled estimate across all 72 studies and 21.4% is the estimate
restricted to the 30 prospective cohorts, which is what the authors' "more than one in five"
conclusion rests on. BC-410 states the 21.4% figure; BC-650 does not. BC-410 also carries a caution
block warning that "Quoting a single incidence figure to a patient without saying how it was measured
overstates the precision of what is known", which is exactly what BC-650 then does.
**Correct value / fix:** BC-650 should read "pooled incidence 16.6%, rising to 21.4% in prospective
cohorts, which is the basis of the authors' statement that more than one in five women develop it."
**Source checked:** PubMed PMID 23540561 (DiSipio et al, Lancet Oncol 2013, DOI
10.1016/S1470-2045(13)70076-7): "a pooled estimate of 16.6% (95% CI 13.6-20.2). Our estimate was 21.4%
(14.9-29.8) when restricted to data from prospective cohort studies"

### BC-160  BS-1300 promises not to repeat material and then repeats it, duplicating BC-345  BS-2980
**Claim as written:** "The cleanest clinical demonstration is the {{trial:paloma3}} circulating tumour
DNA analysis, set out in [[BS-2500]] and not repeated here."
**Problem:** the sentence is followed, in the same section, by a full restatement of the PALOMA-3
cyclin E1 analysis: 302 patients, 194 palbociclib and 108 placebo, PFS 7.6 against 14.1 months in the
palbociclib arm and 4.0 against 4.8 in the placebo arm. BC-345 BS-2980 carries the identical figures
in the identical order, and neither section acknowledges the other. The two also cite the same paper
under different keys (`turner2019ccne1` in BC-160, `turner2019` in BC-345). BS-2500, the section
BC-160 points to, is about ctDNA-detected escape routes, not the cyclin E1 tissue analysis, so the
"not repeated here" promise points at the wrong target as well.
**Correct value / fix:** own the cyclin E1 analysis in one place. BC-345 BS-2980 is the natural home,
since it is the resistance-mechanism chapter and it adds the sampling point about metastatic against
archival tissue. BC-160 should state the mechanism and point across.
**Source checked:** internal

### BC-180  BS-1450 leaves OlympiA's survival question open where BC-490 and BC-510 close it
**Claim as written:** (BC-180) "Three-year invasive disease-free survival was 85.9% against 77.1%,
hazard ratio 0.58 [@tutt2021]. At that interim analysis there were 59 deaths on olaparib and 86 on
placebo, a difference that did not cross the prespecified significance boundary [@tutt2021]."
(BC-490 BS-4330 and BC-510 BS-4500) "At a median follow-up of 6.1 years ... For overall survival it was
0.72, with an interval of 0.56 to 0.93. Six-year overall survival was 87.5% with olaparib and 83.2%
with placebo [@garber2026]."
**Problem:** each statement is correct for the analysis it names, and BC-180 says "at that interim
analysis". But BC-180 never signals that mature data exist, so a reader of the biology chapter alone
comes away believing the adjuvant survival question is unresolved, while two management chapters treat
it as settled. This is the framing contradiction the audit brief is looking for, arriving through
differential follow-up rather than through a wrong number.
**Correct value / fix:** BC-180 should add one sentence: "At a median follow-up of 6.1 years the
overall survival hazard ratio was 0.72, with a 95% confidence interval of 0.56 to 0.93 [@garber2026]."
**Source checked:** internal; the two citations are correctly assigned in all three chapters

---

## MINOR

### BC-470  BS-4160 — suppressive microenvironment pointed at the architecture chapter
**Claim as written:** "Trafficking into the tumour is the first. The suppressive microenvironment is
the second [[BC-220]]."
**Problem:** BC-350 BS-3150 sets the book's own division: "Cellular architecture is in [[BC-220]],
functional states in [[BC-230]]". Immunosuppression is a functional state. BC-230 carries BS-1830
(*Inflammation and local immunosuppression*) and BS-1880 (*TGF-beta and metabolic immunosuppression*).
BC-220 is defensible only through BS-1740 and BS-1760.
**Correct value / fix:** `[[BC-230]]`.

### BC-690  BS-5860 calls 9,719 the TAILORx enrolment, where BC-380 and BC-490 call it 10,273
**Claim as written:** "{{trial:tailorx}} enrolled 9719 women with hormone receptor-positive,
HER2-negative, node-negative disease."
**Problem:** BC-380 states it precisely: "TAILORx enrolled 10,273 women ... of whom 9,719 were eligible
with follow-up." BC-490 BS-4300 also uses 10,273 as the enrolment. BC-690 BS-5930 gets it right
("9719 eligible participants"); BS-5860 in the same chapter does not.
**Correct value / fix:** "the 9,719 eligible participants with follow-up".

### All nine appendices are orphans
**Problem:** `outline.yaml` defines APP-A through APP-I. Across all 79 chapters there are zero
`[[APP-x]]` cross-references and zero prose mentions of any appendix by name. Several appendices are
clearly meant to be reachable from the prose, in particular APP-E (*Trial endpoints and evidence
appraisal glossary*), which is the natural companion to BS-6360 and BS-6370, APP-C (*Biomarker and
assay reference*) for BC-110, and APP-F (*Cross-chapter biological interplay map*) for BC-350.
**Correct value / fix:** decide whether the appendices ship. If they do, they need inbound pointers
from the chapters whose material they index.

### BC-550 carries no interplay block, against the stated convention for Parts VIII to X
**Problem:** `CONVENTIONS.md`: "Every disease-focused chapter in Parts VIII, IX and X should carry at
least one interplay block." All 21 other chapters in PT-08, PT-09 and PT-10 have one. BC-550 (*General
principles of metastatic management*) has none.
**Correct value / fix:** add one, most naturally targeting BC-300, since BS-4780 already argues that a
single progressing deposit implies a resistant subclone in one place.

### Three interplay blocks target chapters outside Part VI
**Problem:** the convention is that an interplay block ties a chapter "back to the heterogeneity
argument" in Part VI. Fifty-four of the 58 blocks do. Three do not: BC-180 targets BC-210, BC-640
targets BC-460, and BC-350 targets BC-690. BC-350's is the odd one, because BC-350 is the Part VI hub
that every other block points into.
**Correct value / fix:** either retarget, or record the exception in CONVENTIONS.

### Twenty-nine trials in the registry are named in prose without the `{{trial:}}` macro
**Problem:** the registry backlink and the `claim` field do not apply where the acronym is written out.
The affected chapters and trials: BC-140 (BOLERO-2, PALOMA-3), BC-170 (SOLAR-1 x3, CAPItello-291 x3,
INAVO120 x2, BOLERO-2), BC-180 (TBCRC 048), BC-250 (MA.32), BC-370 (c-TRAK TN), BC-390 (c-TRAK TN,
PADA-1, SWOG S0500 x2), BC-500 (DESTINY-Breast05), BC-510 (KEYNOTE-522), BC-560 (SERENA-6,
TROPiCS-02, TROPION-Breast01), BC-570 (DESTINY-Breast03, DESTINY-Breast12, HER2CLIMB), BC-580
(ASCENT-03, TROPION-Breast02). BC-170 is the worst affected and is discussed under structure below.
**Correct value / fix:** convert to the macro where an entry exists, or add the missing registry
entries (TROPION-Breast01, TROPION-Breast02, ASCENT-03, DESTINY-Breast05, MA.32, SABR-COMET appear to
be named in prose without one).

### Cross-chapter passages that duplicate without acknowledging each other
**Problem:** beyond the PALOMA-3 case reported under MAJOR, a near-duplicate paragraph detector found
these pairs at very high overlap. None of them cross-references the other, so the same material is
stated twice with no indication of which chapter owns it.

| Pair | Shared material |
|---|---|
| BC-580 BS-5040 / BC-590 BS-5120 / BC-560 BS-4860 / BC-180 BS-1450 | OlympiAD and EMBRACA reported four times with the same numbers |
| BC-580 BS-5040 / BC-590 BS-5120 / BC-560 BS-4860 | TBCRC 048 response rates reported three times |
| BC-345 BS-3020 / BC-470 BS-4170 | Zaretsky melanoma JAK1/JAK2 and B2M paragraph, near verbatim |
| BC-050 BS-0360 / BC-080 BS-0640 | Hartmann benign-biopsy relative risk gradient, near verbatim |
| BC-510 BS-4500 / BC-540 BS-4690 | CREATE-X reported twice with identical numbers |
| BC-220 BS-1740 / BC-230 BS-1880 | Mariathasan urothelial TGF-beta exclusion paragraph |
| BC-700 BS-6000 / BC-710 BS-6110 | Fundytus availability and catastrophic expenditure figures |
| BC-470 BS-4180 / BC-640 BS-5470 | The KEYNOTE-522 curative-intent endocrinopathy argument |
| BC-430 BS-3860 / BC-490 BS-4360 | Hershman adherence cohort, near verbatim |
| BC-430 / BC-490 BS-4290 | SOFT and TEXT eight-year figures, near verbatim |
| BC-050 BS-0430 / BC-060 BS-0510 | Navin and Gao subclonal architecture paragraph |
| BC-040 BS-0340 / BC-050 | Nishimura der(1;16) dating paragraph |
| BC-570 BS-4990 / BC-590 BS-5130 | Neratinib in HER2-mutant disease, near verbatim |
| BC-340 BS-2930 / BC-390 BS-3530 | Gebhart zirconium-89 trastuzumab PET figures |
| BC-345 BS-3010 / BC-580 BS-5040 | The HRD-score-as-history `caution` block, near verbatim |
| BC-345 BS-3000 / BC-460 BS-4080 BS-4090 | DAISY PTEN-loss hazard ratio and MDR1 sentences, verbatim |
| BC-040 BS-0310 / BC-250 BS-2050 | Lyons postpartum involution experiment |
| BC-360 BS-3260 / BC-710 BS-6090 | Mumbai cluster-randomised clinical breast examination trial |
| BC-345 BS-3030 / BC-580 BS-5090 | The Mai sequential-conjugate 75.2% series |
| BC-020 BS-0170 / BC-690 BS-5860 | Giaquinto 38% mortality and 5% incidence figures |
| BC-280 BS-2360 / BC-590 BS-5110 | The 2023 ASCO/CAP guideline paragraph |
| BC-630 BS-5410 / BC-640 BS-5510 | The 476,373-woman second-primary cohort |

Most of these are defensible as deliberate repetition for a reference book that is read by chapter.
The ones worth resolving are the four-way OlympiAD/EMBRACA repetition, the three-way TBCRC 048
repetition, and the Zaretsky, Mariathasan and Hartmann paragraphs, where the wording is close enough
to read as copied rather than restated.


---

## Structural observations for the restructure

### 1. Every wrong-target pointer but one originates in Parts XII to XIV

This is the single most useful pattern in the audit. Of the thirteen confirmed wrong-target pointers,
twelve are written in BC-650, BC-680, BC-700, BC-710, BC-730, BC-740, BC-750, BC-760 or BC-780, and
they point backwards into Parts III to X. The one exception, BC-470 BS-4160, is also the mildest.

| Source part | Source chapter | Points at | Should point at |
|---|---|---|---|
| PT-12 | BC-680 | BC-570 | BC-320 BS-2750 / BC-600 BS-5190 |
| PT-12 | BC-680 | BC-610 | BC-640 BS-5430 |
| PT-12 | BC-650 | BS-5740 (claim inverted) | BS-5740 (claim corrected) |
| PT-13 | BC-700 | BC-480 | BC-420 BS-3740 |
| PT-13 | BC-710 | BC-480 | BC-420 BS-3740 |
| PT-14 | BC-730 | BC-160 | BC-120 BS-1060 |
| PT-14 | BC-740 | BC-700 | BC-690 BS-5900 |
| PT-14 | BC-750 | BC-360 | BC-380 |
| PT-14 | BC-760 | BC-220 | BC-230 BS-1890 |
| PT-14 | BC-760 | BC-250 | BC-210 BS-1660 |
| PT-14 | BC-780 | BC-320 | BC-310 |
| PT-14 | BC-780 | BC-250 | BC-210 BS-1660 |
| PT-14 | BC-780 | BC-220 | BC-230 BS-1930 |

In almost every case the wrong target sits beside the right one in the outline: BC-220 beside BC-230,
BC-250 in the same part as BC-210, BC-320 beside BC-310, BC-360 in the same part as BC-380, BC-700
beside BC-690, BC-570 in the same part as BC-600. The signature is an author choosing an identifier
from the outline by title similarity without opening the target. The forward-pointing chapters, which
were written first, do not show it: Parts I to X point at each other accurately throughout.

**Consequence for the restructure.** Whatever else moves, Parts XII to XIV need every one of their
outbound pointers re-verified against the target text, not against the outline.

### 2. Chapters carrying material that belongs elsewhere

**BC-170 (PI3K, AKT, mTOR) is a clinical chapter wearing a biology chapter's title.** It carries the
full reporting of SOLAR-1, CAPItello-291, INAVO120 and BOLERO-2, with denominators, medians, hazard
ratios, a rash-and-hyperglycaemia toxicity comparison and a `caution` block about cross-trial median
comparison. All of it duplicates BC-450 BS-3980 and BC-560 BS-4850, and all of it names the trials in
prose rather than through the `{{trial:}}` macro, so the registry does not know these appearances
exist. This is the clearest single relocation in the book: the trial reporting belongs in BC-450 and
BC-560, and BC-170 should keep the pathway architecture and the grouping argument.

**BC-345 is a cross-index rather than a chapter.** Its identifier is the only one off the by-ten
sequence, so it was inserted after the outline was set. It has the second-highest outbound link count
in the book (29 pointers to 19 chapters) and it restates material from BC-140, BC-160, BC-180, BC-230,
BC-280, BC-300, BC-460 and BC-470. It is well written and it duplicates by design. The restructure
should decide explicitly whether it is a chapter or an appendix, because at present it competes with
BC-300 (the two acknowledge this: "one process at two time points") and with BC-350.

**BC-390 is functioning as a trials chapter.** PADA-1, SERENA-6, c-TRAK TN and SWOG S0500 are all
reported in prose with denominators and hazard ratios, three of them without the macro. That reporting
is the substance of the chapter, and it sits oddly in Part VII alongside BC-360 and BC-370.

**BC-250 BS-2110 is a part opener for Part XIII sitting inside Part V.** Its title says so ("the
bridge to Part XIII"). It is the second-most-pointed-to section in BC-250. Worth promoting or moving.

**Dormancy-directed strategy is split three ways** across BC-330, BC-770 BS-6610 and BC-780 BS-6670,
with each pointing at the other two. The biology has a home. The strategy does not.

**The pCR endpoint argument is split between BC-090 BS-0790, BC-540 BS-4670/4680 and BC-740 BS-6360,**
and this one works. BC-540 raises the thread, says where it resolves, and BC-740 resolves it and says
so. It is the model the rest of the book's threads should follow.

### 3. The seams

- **BC-220 / BC-230 (cellular architecture against functional states).** Three mis-pointers land here.
  The division is stated once, in BC-350 BS-3150, and nowhere in the two chapters themselves. Authors
  downstream cannot tell which chapter owns immune evasion.
- **BC-210 / BC-250 (immunology against host factors).** Two chapters cite BC-250 for TIL biology.
  BC-250 contains the word "lymphocyte" zero times. The titles do not separate the two well enough.
- **BC-310 / BC-320 (plasticity against dissemination).** One mis-pointer, plus BC-320 and BC-310
  cross-reference each other four times on the same state-change material.
- **BC-420 / BC-480 / BC-620 (radiation omission and fractionation).** Four chapters point at the
  fractionation evidence; two of them point at BC-480, which does not contain it.
- **BC-360 / BC-380 (screening against assays).** BC-360 points outward to BC-080, BC-330, BC-390,
  BC-690, BC-700 and BC-750 more often than into its own part, and BC-750 mistakes it for BC-380.
- **PT-12 boundary (BC-650 / BC-660 / BC-680 / BC-700).** Work, finance, visibility and palliative
  integration are argued across all four, and the one place where the book contradicts itself on an
  interpretive question (early palliative care and survival) sits on this seam.

### 4. Link topology

Inbound links concentrate hard. Nine chapters take 40% of all inbound pointers: BC-280 (60 pointers
from 33 chapters), BC-300 (56/29), BC-350 (44/39), BC-110 (44/24), BC-740 (46/26), BC-390 (42/29),
BC-345 (36/13), BC-330 (35/23), BC-690 (29/18). These are the load-bearing chapters and none of them
can move without rewriting a third of the book's pointers.

At the other end, five chapters are near-orphans that the restructure should look at:

| Chapter | Inbound (distinct source chapters) |
|---|---|
| BC-530 Locoregional recurrence | 1 (BC-420 only) |
| BC-630 Sex, gender, and uncommon disease contexts | 1 (BC-650 only) |
| BC-130 Hallmarks and pathway logic | 2 (BC-190, BC-450) |
| BC-190 Metabolism, proteostasis, stress responses | 2 (BC-170, BC-200) |
| BC-720 Implementation, policy, and quality of care | 2 (BC-400, BC-660) |

BC-670 (*Communication and shared decision-making*) is the reverse case: five chapters point into it
and it emits exactly one pointer, to one chapter. It receives argument and returns none.

No chapter has zero inbound pointers, and no cross-reference is broken.

---

## Summary

**Counts.** 0 BLOCKER, 16 MAJOR, 7 MINOR.

All 1,164 cross-reference tokens resolve. The failures are semantic, and they cluster: thirteen
pointers name a real chapter that does not contain what the sentence says it contains, and twelve of
those thirteen were written in Parts XII to XIV pointing backwards.

**The three things most worth fixing before merge.**

1. **BC-650 BS-5610 asserts that early palliative care extends survival and cites BS-5740 as its
   support, when BS-5740 exists to say the opposite.** It is the only place in the book where one
   chapter takes an interpretive position the book explicitly rejects elsewhere, it does so inside a
   `caution` block, and it points the reader at the refutation as if for corroboration. One sentence
   fixes it.

2. **The eight duplicated reference keys.** Each of EBCTCG tamoxifen, EBCTCG radiotherapy, EBCTCG OFS,
   NSABP B-06, GeparNuevo primary, GeparNuevo update, KEYNOTE-522 EFS and PALOMA-3 cyclin E1 exists
   twice in `references.yaml` with identical DOI and PMID, and in every case the two keys are used by
   different chapters. This will print each paper twice in the bibliography and split its cited-in
   backlinks. It is mechanical to fix and invisible until the book is built.

3. **The thirteen wrong-target pointers, and the audit habit they imply.** Four of them are actively
   misleading to a reader: bone pain sent to the HER2 chapter, chemotherapy-induced neuropathy sent to
   the pregnancy chapter, hypofractionation evidence sent to the in situ chapter twice, and ancestry
   biology sent to the affordability chapter, where the confounding caveat that BC-690 supplies is
   lost. Fixing the thirteen is an hour. The habit worth adopting is that a pointer written from a
   late chapter into an early one must be checked against the target text.

One further note for the restructure rather than for the merge: all nine appendices (APP-A to APP-I)
have zero inbound references from any chapter, and BC-550 is the only chapter in Parts VIII to X
without an interplay block.

