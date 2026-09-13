# Audit: house style, voice and register consistency across all 79 chapters

Scope: rules 1 to 7 of the house style, plus register consistency. No chapter file was edited.
Method: a linter over all 79 files for the countable rules (dashes, sentence length, semicolons,
colons, clause chaining, filler), then reading of the opening paragraphs of every chapter and of
every flagged sentence for the judgement calls.

**Headline.** Rule 2 is perfect. Rules 4 and 7 are effectively perfect. Rule 3 holds book-wide with
28 exceptions, most of them legitimate enumerations. Rule 1 has a real, systematic answer, and it is
not the answer a linter gives. Rules 5 and 6 have a small number of genuine lapses. Register drift is
confined to a few identifiable chapters.

---

## Per-chapter statistics

`mean` / `med` / `p90` / `max` are sentence length in words. `>35` counts sentences over 35 words.
`semi` and `col` are semicolons and colons as punctuation (citation-internal `;` and numeric `1:2`
excluded). `and-j` is `, and <new subject> <verb>` clause joins; `/1k` normalises per 1000 words.
Citations, trial macros and cross-references are stripped before counting.

| Chapter | Sent | Words | Mean | Med | p90 | Max | >35 | >30 | Semi | Col | col/1k | and-j | /1k |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BC-010 | 187 | 2506 | 13.4 | 13 | 21 | 33 | 0 | 3 | 0 | 0 | 0.0 | 7 | 2.8 |
| BC-020 | 125 | 1919 | 15.4 | 14 | 26 | 33 | 0 | 5 | 0 | 0 | 0.0 | 9 | 4.7 |
| BC-030 | 133 | 1879 | 14.1 | 13 | 23 | 33 | 0 | 5 | 0 | 0 | 0.0 | 10 | 5.3 |
| BC-040 | 140 | 1879 | 13.4 | 12 | 23 | 35 | 0 | 4 | 0* | 1 | 0.5 | 6 | 3.2 |
| BC-050 | 155 | 2371 | 15.3 | 14 | 26 | 44 | 2 | 6 | 0* | 2 | 0.8 | 13 | 5.5 |
| BC-060 | 141 | 2163 | 15.3 | 14 | 28 | 40 | 2 | 7 | 0 | 0 | 0.0 | 8 | 3.7 |
| BC-070 | 180 | 2976 | 16.5 | 16 | 27 | 35 | 0 | 7 | 0 | 0 | 0.0 | 8 | 2.7 |
| BC-080 | 193 | 3276 | 17.0 | 16 | 27 | 45 | 2 | 9 | 0 | 2 | 0.6 | 9 | 2.7 |
| BC-090 | 173 | 2710 | 15.7 | 15 | 26 | 33 | 0 | 2 | 0 | 0 | 0.0 | 8 | 3.0 |
| BC-100 | 200 | 2858 | 14.3 | 13 | 23 | 33 | 0 | 3 | 0 | 0 | 0.0 | 11 | 3.8 |
| BC-110 | 237 | 3377 | 14.2 | 13 | 23 | 33 | 0 | 5 | 0 | 0 | 0.0 | 8 | 2.4 |
| BC-120 | 150 | 2239 | 14.9 | 14 | 26 | 32 | 0 | 1 | 0 | 0 | 0.0 | 5 | 2.2 |
| BC-130 | 63 | 943 | 15.0 | 15 | 22 | 28 | 0 | 0 | 0 | 0 | 0.0 | 1 | 1.1 |
| BC-140 | 184 | 2603 | 14.1 | 13 | 25 | 34 | 0 | 7 | 0 | 0 | 0.0 | 8 | 3.1 |
| BC-150 | 194 | 2838 | 14.6 | 14 | 27 | 34 | 0 | 6 | 0 | 0 | 0.0 | 2 | 0.7 |
| BC-160 | 124 | 1731 | 14.0 | 13 | 24 | 29 | 0 | 0 | 0 | 1 | 0.6 | 6 | 3.5 |
| BC-170 | 149 | 2147 | 14.4 | 14 | 23 | 33 | 0 | 2 | 0 | 0 | 0.0 | 4 | 1.9 |
| BC-180 | 156 | 2282 | 14.6 | 14 | 24 | 37 | 1 | 4 | 0 | 2 | 0.9 | 10 | 4.4 |
| BC-190 | 161 | 2349 | 14.6 | 14 | 24 | 31 | 0 | 1 | 0 | 2 | 0.9 | 9 | 3.8 |
| BC-200 | 155 | 2312 | 14.9 | 14 | 24 | 32 | 0 | 3 | 0 | 1 | 0.4 | 6 | 2.6 |
| BC-210 | 163 | 2320 | 14.2 | 13 | 23 | 32 | 0 | 3 | 0 | 0 | 0.0 | 7 | 3.0 |
| BC-220 | 164 | 2489 | 15.2 | 15 | 25 | 32 | 0 | 2 | 0 | 1 | 0.4 | 9 | 3.6 |
| BC-230 | 176 | 2731 | 15.5 | 15 | 26 | 36 | 1 | 8 | 0 | 1 | 0.4 | 7 | 2.6 |
| BC-240 | 139 | 2122 | 15.3 | 15 | 24 | 35 | 0 | 3 | 0 | 0 | 0.0 | 6 | 2.8 |
| BC-250 | 208 | 3292 | 15.8 | 15 | 27 | 36 | 2 | 8 | 0 | 2 | 0.6 | 13 | 3.9 |
| BC-260 | 149 | 1966 | 13.2 | 12 | 22 | 31 | 0 | 3 | 0 | 0 | 0.0 | 5 | 2.5 |
| BC-270 | 113 | 1716 | 15.2 | 14 | 26 | 32 | 0 | 3 | 0 | 0 | 0.0 | 4 | 2.3 |
| BC-280 | 171 | 2551 | 14.9 | 14 | 24 | 52 | 2 | 8 | 0 | 0 | 0.0 | 15 | 5.9 |
| BC-290 | 157 | 2258 | 14.4 | 14 | 23 | 32 | 0 | 1 | 0 | 0 | 0.0 | 4 | 1.8 |
| BC-300 | 167 | 2677 | 16.0 | 15 | 26 | 41 | 3 | 8 | 0 | 1 | 0.4 | 10 | 3.7 |
| BC-310 | 124 | 1765 | 14.2 | 13 | 25 | 32 | 0 | 1 | 0 | 0 | 0.0 | 7 | 4.0 |
| BC-320 | 187 | 2787 | 14.9 | 14 | 26 | 33 | 0 | 5 | 0 | 0 | 0.0 | 11 | 3.9 |
| BC-330 | 238 | 3665 | 15.4 | 14 | 26 | 32 | 0 | 6 | 0 | 0 | 0.0 | 10 | 2.7 |
| BC-340 | 109 | 1518 | 13.9 | 12 | 24 | 33 | 0 | 2 | 0 | 0 | 0.0 | 6 | 4.0 |
| BC-345 | 206 | 3005 | 14.6 | 14 | 24 | 32 | 0 | 3 | 0 | 1 | 0.3 | 6 | 2.0 |
| BC-350 | 178 | 2778 | 15.6 | 15 | 26 | 33 | 0 | 5 | 0 | 0 | 0.0 | 8 | 2.9 |
| BC-360 | 174 | 2857 | 16.4 | 16 | 27 | 33 | 0 | 7 | 0 | 0 | 0.0 | 9 | 3.2 |
| BC-370 | 143 | 2343 | 16.4 | 15 | 27 | 43 | 1 | 3 | 0 | 1 | 0.4 | 14 | 6.0 |
| BC-380 | 144 | 2406 | 16.7 | 15 | 27 | 33 | 0 | 6 | 0 | 0 | 0.0 | 7 | 2.9 |
| BC-390 | 231 | 3605 | 15.6 | 15 | 26 | 41 | 2 | 11 | 0 | 1 | 0.3 | 9 | 2.5 |
| BC-400 | 140 | 1953 | 13.9 | 13 | 23 | 34 | 0 | 3 | 0 | 0 | 0.0 | 3 | 1.5 |
| BC-410 | 151 | 2407 | 15.9 | 15 | 26 | 33 | 0 | 4 | 0 | 0 | 0.0 | 8 | 3.3 |
| BC-420 | 183 | 2993 | 16.4 | 16 | 25 | 33 | 0 | 7 | 0 | 0 | 0.0 | 7 | 2.3 |
| BC-430 | 173 | 2919 | 16.9 | 16 | 27 | 32 | 0 | 4 | 0 | 0 | 0.0 | 10 | 3.4 |
| BC-440 | 135 | 1977 | 14.6 | 15 | 24 | 32 | 0 | 2 | 0 | 0 | 0.0 | 2 | 1.0 |
| BC-450 | 146 | 2243 | 15.4 | 15 | 24 | 32 | 0 | 4 | 0 | 0 | 0.0 | 3 | 1.3 |
| BC-460 | 188 | 2815 | 15.0 | 14 | 25 | 43 | 1 | 2 | 0 | 1 | 0.4 | 6 | 2.1 |
| BC-470 | 142 | 2276 | 16.0 | 16 | 24 | 33 | 0 | 4 | 0 | 0 | 0.0 | 8 | 3.5 |
| BC-480 | 168 | 2539 | 15.1 | 14 | 26 | 33 | 0 | 5 | 0 | 0 | 0.0 | 4 | 1.6 |
| BC-490 | 203 | 3543 | 17.5 | 17 | 27 | 35 | 0 | 11 | 0 | 0 | 0.0 | 0 | 0.0 |
| BC-500 | 199 | 3296 | 16.6 | 15 | 28 | 34 | 0 | 11 | 0 | 0 | 0.0 | 7 | 2.1 |
| BC-510 | 174 | 2939 | 16.9 | 16 | 28 | 35 | 0 | 5 | 0 | 0 | 0.0 | 8 | 2.7 |
| BC-520 | 139 | 2097 | 15.1 | 14 | 25 | 35 | 0 | 3 | 0 | 0 | 0.0 | 7 | 3.3 |
| BC-530 | 101 | 1592 | 15.8 | 16 | 24 | 35 | 0 | 5 | 0 | 0 | 0.0 | 2 | 1.3 |
| BC-540 | 168 | 2760 | 16.4 | 15 | 27 | 44 | 1 | 10 | 0 | 0 | 0.0 | 6 | 2.2 |
| BC-550 | 132 | 1771 | 13.4 | 12 | 22 | 32 | 0 | 1 | 0 | 0 | 0.0 | 5 | 2.8 |
| BC-560 | 211 | 3079 | 14.6 | 14 | 23 | 34 | 0 | 2 | 0 | 0 | 0.0 | 5 | 1.6 |
| BC-570 | 176 | 2611 | 14.8 | 14 | 25 | 34 | 0 | 5 | 0 | 0 | 0.0 | 6 | 2.3 |
| BC-580 | 147 | 2242 | 15.3 | 15 | 25 | 32 | 0 | 4 | 0 | 0 | 0.0 | 8 | 3.6 |
| BC-590 | 172 | 2712 | 15.8 | 15 | 26 | 35 | 0 | 6 | 0 | 0 | 0.0 | 5 | 1.8 |
| BC-600 | 153 | 2679 | 17.5 | 18 | 28 | 34 | 0 | 7 | 0 | 0 | 0.0 | 7 | 2.6 |
| BC-610 | 158 | 2253 | 14.3 | 13 | 25 | 34 | 0 | 4 | 0 | 0 | 0.0 | 5 | 2.2 |
| BC-620 | 157 | 2252 | 14.3 | 13 | 24 | 35 | 0 | 5 | 0 | 1 | 0.4 | 3 | 1.3 |
| BC-630 | 138 | 2118 | 15.3 | 14 | 25 | 33 | 0 | 4 | 0 | 0 | 0.0 | 7 | 3.3 |
| BC-640 | 213 | 3253 | 15.3 | 15 | 26 | 33 | 0 | 7 | 0 | 0 | 0.0 | 10 | 3.1 |
| BC-650 | 184 | 2873 | 15.6 | 15 | 25 | 34 | 0 | 6 | 0 | 2 | 0.7 | 11 | 3.8 |
| BC-660 | 50 | 736 | 14.7 | 16 | 22 | 26 | 0 | 0 | 0 | 0 | 0.0 | 6 | 8.2 |
| BC-670 | 60 | 945 | 15.8 | 13 | 27 | 54 | 3 | 4 | 0 | 0 | 0.0 | 2 | 2.1 |
| BC-680 | 104 | 1523 | 14.6 | 14 | 24 | 33 | 0 | 3 | 0 | 0 | 0.0 | 2 | 1.3 |
| BC-690 | 346 | 5014 | 14.5 | 14 | 25 | 48 | 2 | 7 | 0 | 3 | 0.6 | 12 | 2.4 |
| BC-700 | 132 | 1983 | 15.0 | 14 | 24 | 34 | 0 | 6 | 0 | 0 | 0.0 | 5 | 2.5 |
| BC-710 | 215 | 3380 | 15.7 | 14 | 27 | 53 | 2 | 6 | 0 | 2 | 0.6 | 8 | 2.4 |
| BC-720 | 144 | 2316 | 16.1 | 15 | 27 | 33 | 0 | 7 | 0 | **8** | **3.5** | 6 | 2.6 |
| BC-730 | 113 | 1684 | 14.9 | 15 | 23 | 34 | 0 | 2 | 0 | 0 | 0.0 | 5 | 3.0 |
| BC-740 | 180 | 2743 | 15.2 | 14 | 26 | 35 | 0 | 3 | 0 | 2 | 0.7 | 8 | 2.9 |
| BC-750 | 94 | 1540 | 16.4 | 16 | 24 | 33 | 0 | 3 | 0 | 1 | 0.6 | 8 | 5.2 |
| BC-760 | 128 | 2000 | 15.6 | 15 | 25 | 36 | 1 | 4 | 0 | 0 | 0.0 | 2 | 1.0 |
| BC-770 | 111 | 1602 | 14.4 | 14 | 24 | 34 | 0 | 1 | 0 | 2 | 1.2 | 5 | 3.1 |
| BC-780 | 123 | 1801 | 14.6 | 14 | 25 | 33 | 0 | 4 | 0 | 2 | 1.1 | 4 | 2.2 |

**Book totals: 79 chapters, 191,668 words, 12,592 sentences, mean 15.2 words.**
Chapter means run 13.2 (BC-260) to 17.5 (BC-490, BC-600). Zero dashes of any kind.

`*` The two apparent semicolons, in BC-040 L184 and BC-050 L7, are both inside the cytogenetic
designation `der(1;16)`. **There are zero semicolons used as punctuation in the entire book.**

### What the table says about drift

There is very little. Mean sentence length has a standard deviation of about 1.0 word across 79
chapters written by parallel agents. Fourteen chapters sit just under the 15-word floor (lowest
BC-260 13.2, BC-010 13.4, BC-040 13.4, BC-550 13.4) and three sit at or above the ceiling (BC-490
17.5, BC-600 17.5, BC-080 17.0). None of these is a problem on its own. The low-mean chapters are the
argumentative and conceptual ones, where the short declarative is the point. The high-mean chapters
are the ones densest in trial results, where a sentence has to carry a population, a comparison and
an interval. That covariance is a sign of one hand rather than of drift.

---

## Rule 2: dashes. Clean. Nothing to fix.

Verified across every byte of all 79 files, not only for em and en dashes but for every dash-like
Unicode codepoint: U+2010 hyphen, U+2011 non-breaking hyphen, U+2012 figure dash, U+2013 en dash,
U+2014 em dash, U+2015 horizontal bar, U+2212 minus sign. **Zero occurrences of all seven.** The only
`--` sequences are the YAML front-matter delimiters. The only non-ASCII characters in 191,668 words
are 13 beta, 11 alpha, 1 gamma and 1 capital delta, all inside protein and receptor names. No further
work is needed on this rule.

## Rule 4: semicolons and colons. Effectively clean.

Zero semicolons as punctuation. 47 colons in 191,668 words, 0.25 per 1000. Every one introduces a
genuine series, which CONVENTIONS.md permits. One chapter leans on them, below.

## Rule 7: filler. Effectively clean.

Scanned for eighteen filler and throat-clearing constructions ("it is important to note", "it is
worth noting", "plays an important role", "the advent of", "cannot be overstated", "has
revolutionised", "paradigm shift", "in today's era", "this chapter will discuss", and others). Two
hits in 191,668 words, both false positives on reading. The book also never explains a basic term:
a scan for definitional constructions attached to `neoadjuvant`, `adjuvant`, `chemotherapy`,
`mastectomy`, `hazard ratio`, `biopsy` and twelve others returned nothing. Forty first sentences
share 60% or more of their heading's content words, but on reading all forty, thirty-eight name the
subject and then immediately make a claim about it, which is the correct topic-sentence pattern
rather than restatement. The two exceptions are listed under MINOR.

---

# MAJOR

### Rule 1: the one structural finding. All 79 chapters

**Pattern as written:** the construction `<independent clause>, and <new subject> <verb>` occurs
**541 times**, at 2.8 per 1000 words, in 78 of 79 chapters. Examples, one from each of four chapters:

> "Two surgical conclusions follow with real force, and that force is what kept the model alive for
> eighty years." (BC-010)
> "Incidence below age 50 is rising, and the rise is not obviously a detection artefact." (BC-020)
> "Calling its members a disease entity is a further claim, and it needs its own evidence." (BC-010)
> "Heterogeneity is measurable, it carries prognostic weight in at least one prospective neoadjuvant
> dataset, and it has no established role in selecting therapy." (BC-280)

**Problem:** under a strict reading of rule 1 every one of these chains independent clauses. But the
distribution is the finding. It is not concentrated in a subset of chapters, which is what agent
drift looks like. It is spread evenly across all fourteen parts at a nearly constant rate, and the
second clause is almost always a short reflective coda that comments on the first clause rather than
asserting a second, separable claim. This is one writer's rhythm, not a lapse. Two sub-patterns sit
inside it: the coda (`X is true, and that is why Y`) and the tricolon (`It is free, it is already in
the chart, and it predicts the yield`).

**Fix:** this is a decision for the author, not a linter fix, and it should be made once for the
whole book rather than chapter by chapter. Mechanically splitting all 541 would flatten the prose
into 12,000 identical short declaratives and would cost the book its best rhetorical move. My
recommendation is to keep the coda and the tricolon as sanctioned exceptions, write them into
CONVENTIONS.md explicitly so the rule stops reading as absolute, and apply the rule strictly only
where the second clause carries a **separately checkable claim**. Those cases are listed next and
there are only eleven.

### Rule 1: the eleven sentences that genuinely chain two separate claims

Each of these carries a substantive second assertion after the comma, not a comment, and each should
become two sentences.

**BC-060 BS-0460**. "The pan-cancer whole-genome analysis that followed used 84,729,690 somatic
mutations from 4,645 whole genomes and 19,184 exomes, and defined 49 single-base substitution
signatures, 11 doublet-base signatures, 4 clustered-base signatures and 17 small insertion and
deletion signatures."
→ "The pan-cancer whole-genome analysis that followed used 84,729,690 somatic mutations from 4,645
whole genomes and 19,184 exomes. It defined 49 single-base substitution signatures, 11 doublet-base
signatures, 4 clustered-base signatures and 17 small insertion and deletion signatures."
*(This also fixes the 40-word length.)*

**BC-100 BS-0850**. "It sorts tumours into basal, luminal and HER2 types, and it was also tested
against pathological complete response in 133 neoadjuvant patients."
→ "It sorts tumours into basal, luminal and HER2 types. It was also tested against pathological
complete response in 133 neoadjuvant patients."

**BC-130 BS-1090**. "Inhibition of PI3K increases oestrogen receptor transcriptional activity, ESR1
messenger RNA and receptor protein, and the effect was confirmed in tumours from patients receiving a
PI3K alpha inhibitor."
→ "Inhibition of PI3K increases oestrogen receptor transcriptional activity, ESR1 messenger RNA and
receptor protein. The effect was confirmed in tumours from patients receiving a PI3K alpha
inhibitor."

**BC-500 BS-4380**. "It was 29.0% with trastuzumab and docetaxel, with an interval of 20.6 to 38.5,
and the difference had a p value of 0.0141."
→ "It was 29.0% with trastuzumab and docetaxel, with an interval of 20.6 to 38.5. The difference had
a p value of 0.0141."

**BC-510 BS-4470**. "Pathological complete response was 53.4% with durvalumab against 44.2% with
placebo, and the difference was not significant, with a p value of 0.287."
→ "Pathological complete response was 53.4% with durvalumab against 44.2% with placebo. The
difference was not significant, with a p value of 0.287."

**BC-630 BS-5370**. "Adjuvant endocrine therapy was given to 76.8%, and it was tamoxifen in 88.4% of
those."
→ "Adjuvant endocrine therapy was given to 76.8%. It was tamoxifen in 88.4% of those."

**BC-640 BS-5500**. "Time to first clinical fracture favoured denosumab, with a hazard ratio of 0.50
and a 95% confidence interval of 0.39 to 0.65, and there were 92 fractures against 176."
→ "Time to first clinical fracture favoured denosumab, with a hazard ratio of 0.50 and a 95%
confidence interval of 0.39 to 0.65. There were 92 fractures against 176."

**BC-300 BS-2480**. "A tumour that is subclonally complex before treatment has more routes available
to it than one that is not, and the therapeutic pressure that follows does not create those routes so
much as choose among them."
→ "A tumour that is subclonally complex before treatment has more routes available to it than one
that is not. The therapeutic pressure that follows does not create those routes so much as choose
among them." *(also fixes 36 words)*

**BC-390 BS-3550**. "A test that detects the shedding, dividing fraction of residual disease will
find the patients whose recurrence was going to be early, and those are the patients for whom an
earlier start of existing therapy is least likely to be curative."
→ "A test that detects the shedding, dividing fraction of residual disease will find the patients
whose recurrence was going to be early. Those are the patients for whom an earlier start of existing
therapy is least likely to be curative." *(This is the chapter's central argument. Splitting it makes
the point land harder, not softer. 41 words to 22 and 21.)*

**BC-230 BS-1890**. "Class II expression on tumour cells is a separate question and is associated in
breast cancer with greater immune infiltration and better outcome, consistent with a role in
sustaining CD4 help rather than in direct killing."
→ "Class II expression on tumour cells is a separate question. It is associated in breast cancer with
greater immune infiltration and better outcome, consistent with a role in sustaining CD4 help rather
than in direct killing."

**BC-300 BS-2600**. "In serena6, patients on first-line endocrine therapy with a CDK4/6 inhibitor
were monitored for the emergence of ESR1 mutation in circulating tumour DNA, and those in whom it
emerged were switched to camizestrant before any radiographic progression."
→ "In serena6, patients on first-line endocrine therapy with a CDK4/6 inhibitor were monitored for
the emergence of ESR1 mutation in circulating tumour DNA. Those in whom it emerged were switched to
camizestrant before any radiographic progression."

### Rule 3: the two sentences that most need splitting

**BC-670 BS-5690**. 54 words, the longest sentence in the book, in the chapter about explaining
numbers clearly.
> "A patient told that out of a hundred women like her, roughly seven will avoid a recurrence and
> roughly two will avoid a death by seven years, and that all hundred will take a drug with diarrhoea
> and fatigue for two years, has been given the same evidence in a form she can use."

**Problem:** 45 words separate the subject "A patient" from its verb "has been given". The sentence
demonstrates the failure it is arguing against.
**Suggested rewrite:** "Now take the same evidence differently framed. Out of a hundred women like
her, roughly seven will avoid a recurrence and roughly two will avoid a death by seven years. All one
hundred will take a drug with diarrhoea and fatigue for two years. A patient told that has been given
the evidence in a form she can use." *(18, 21, 16, 15 words.)*

**BC-280 BS-2360**. 52 words, the longest non-enumerative sentence outside BC-670.
> "The 2023 ASCO and College of American Pathologists update affirmed the existing recommendations
> and declined to create new result categories, stating that it is premature to do so, while
> acknowledging that the 0 against 1+ distinction is now clinically relevant because of the entry
> criteria of the trial that supported regulatory approval."

**Problem:** three subordinate layers and two separate claims (what the guideline did, and why the
distinction now matters).
**Suggested rewrite:** "The 2023 ASCO and College of American Pathologists update affirmed the
existing recommendations. It declined to create new result categories, calling that premature. It
acknowledged that the 0 against 1+ distinction is now clinically relevant, because of the entry
criteria of the trial that supported regulatory approval." *(13, 13, 24 words.)*

### Rule 5: a hazard ratio repeated in three chapters with no comparison stated

**BC-300 BS-2490, BC-345 BS-2970, BC-390 BS-3510**. the same figure, the same omission, three times.

> BC-300: "Patients carrying the mutation had substantially shorter progression-free survival on
> subsequent aromatase inhibitor based therapy, with a hazard ratio of 3.1."
> BC-345: "Carriers had a hazard ratio of 3.1 for progression on subsequent aromatase inhibitor based
> therapy."
> BC-390: "They carried a hazard ratio of 3.1 for progression-free survival on subsequent aromatase
> inhibitor based therapy."

**Problem:** 3.1 against what. Non-carriers is the obvious answer but it is never stated in any of the
three, and no confidence interval is given in any of the three. BC-300 compounds it with
"substantially shorter", an adjective standing in for the medians. This is the exact pattern the
house style names: "a hazard ratio without its comparison is decoration."
**Fix:** state the comparator and the interval once and reuse the same wording in all three, so the
three chapters agree: "...against patients without the mutation, with a hazard ratio of 3.1 (95% CI
...)". Drop "substantially shorter" in BC-300 and give the medians, or let the ratio carry it alone.

### Rule 5: "statistically significant" with no figure attached, twice, in two chapters

**BC-360 BS-3190** and **BC-380 BS-3450**. the same claim, both times with no number.
> BC-360: "Small but statistically significant differences in the score were observed between major
> racial and ethnic groups."
> BC-380: "The WISDOM study found small but statistically significant differences in polygenic risk
> score between major racial and ethnic groups, and had to adapt the score for use in diverse
> populations."

**Problem:** "small but statistically significant" with no effect size, no interval and no p is the
textbook case rule 5 exists to catch. The word "small" is doing quantitative work it cannot do, and
in a passage arguing that a miscalibrated score assigns the wrong screening interval, the size of the
miscalibration is the whole question.
**Fix:** give the mean score difference between groups, or the shift in the risk distribution, or
state that the published report gives only a p value and say so.

### Rule 5: a ratio whose referent is never named

**BC-400 BS-3610**
> "Accuracy of risk perception improved with a risk ratio of 1.94 across 25 studies. The proportion of
> people taking a passive role in the decision fell."

**Problem:** two numbers missing their referents in consecutive sentences. A risk ratio of 1.94 for
what proportion, against what comparator (usual care, presumably, but it is not stated), and 1.94
times as likely to do what. Then "fell" with no figure at all, in a paragraph where every other
result carries one.
**Fix:** "Participants using an aid were 1.94 times as likely to hold an accurate perception of their
risk as those receiving usual care, across 25 studies. The proportion taking a passive role in the
decision fell from X% to Y%."

### Rule 6: "PD-L1-positive" used bare, two paragraphs before the chapter explains that it is not one test

**BC-470 BS-4120**
> "Median progression-free survival in the intention-to-treat population was 7.2 against 5.5 months,
> with a hazard ratio of 0.80. In the PD-L1-positive subgroup it was 7.5 against 5.0 months, with a
> hazard ratio of 0.62."

**Problem:** the pembrolizumab result in the paragraph immediately above is correctly anchored to its
measurement ("combined positive score of 10 or more"). The atezolizumab result is not. "PD-L1
positive" there means the SP142 immune-cell score at 1% or more of tumour area, a different antibody,
a different cell population and a different threshold. The next section, BS-4130, opens by saying
"PD-L1 is the one in use and it is not one test" and then explains exactly this. Leaving the phrase
bare two paragraphs earlier is the conflation that section exists to prevent, and a reader skimming
for the numbers will carry away that the two trials selected the same population.
**Fix:** "In the subgroup with PD-L1-expressing immune cells covering 1% or more of tumour area, scored
on the SP142 assay, it was 7.5 against 5.0 months, with a hazard ratio of 0.62."

### Rule 6: four prevalence figures quoted without the threshold that produces them

**BC-210 BS-1700**
> "A systematic review of 15 studies covering 13,914 patients estimated that a median of 11% of breast
> cancers are lymphocyte-predominant, with individual study estimates ranging from 5% to 26%."
> "CD8 infiltrates were reported in a median of 60% of triple-negative tumours, 61% of HER2-positive
> tumours, and 43% of hormone-receptor-positive HER2-negative tumours. High FOXP3 infiltration was
> reported in a median of 70%, 67% and 38% of the same three groups."
> "In luminal HER2-negative disease, complete response occurred in 45 of 759 patients with low
> lymphocyte scores and in 49 of 172 with high scores."

**Problem:** "lymphocyte-predominant", "CD8 infiltrates present", "high FOXP3", "low" and "high"
lymphocyte scores are all threshold categories, and none of the five thresholds is stated. The
five-to-twenty-six per cent spread across studies is presented as though it were variation between
populations. It is very largely variation between definitions, since the contributing studies used
different cut-offs and different scored compartments. The chapter earns the right to be precise here,
because BS-1660 immediately above does the measurement work properly ("What is reported is the
percentage of stromal area... The convention was built for reproducibility, and every number below
depends on it"). BS-1700 then drops it.
**Fix:** add one clause to the first sentence: "...are lymphocyte-predominant, with individual study
estimates ranging from 5% to 26%, a spread that reflects differing cut-offs and scored compartments
rather than differing populations." Then state the cut-point used for "low" and "high" in the Denkert
pooled analysis.

---

# MINOR

## Register: the chapters that read as a different hand

I read the opening two paragraphs of all 79 chapters, plus every subtitle and first section heading.
Seventy-three are unmistakably one voice: a claim in the first sentence, the reason the convention
exists in the second, no preamble. Six are not.

### BC-020 BS-0120 and BC-710 BS-6040: the same textbook opener, twice

> BC-020: "Breast cancer is the most frequently diagnosed cancer in women worldwide. Estimates from
> the GLOBOCAN database put the burden at over 2.3 million new cases and 685000 deaths in women in
> 2020."
> BC-710: "Breast cancer is the most commonly diagnosed cancer worldwide. In 2020 there were over 2.3
> million new cases and 685 000 deaths. By 2040, on population growth and ageing alone, the projection
> is over 3 million new cases and 1 million deaths each year."

**Problem:** two chapters open with the same sentence, the same source and the same three numbers.
This is the one genuinely textbook move in the book, and a breast oncologist does not need to be told
that breast cancer is the commonest cancer in women. Both chapters recover in their second paragraph
(BC-020's "The gap between those two proportions is the chapter in one line" is exactly the right
register), which makes the opener look like a habit rather than a judgement. Note also the
inconsistent thousands separator between the two: `685000` against `685 000`.
**Suggested rewrite for BC-020:** open on the second paragraph's argument and let the burden figures
follow. "Incidence is concentrated where survival is best. In the 2022 estimates, cancer of the
female breast accounted for 11.6% of all new cancer cases and 6.9% of all cancer deaths worldwide.
The gap between those two proportions is this chapter in one line."
**Suggested rewrite for BC-710:** the chapter's own subtitle is the better opener. "Five-year
survival for the same disease runs from under 40% to near 90%. Almost none of that spread is
biology." Then the burden numbers.

### BC-640 BS-5430: explains why chemotherapy causes myelosuppression

> "Cytotoxic toxicity is the toxicity of a mechanism that does not distinguish tumour from renewing
> normal tissue. The organs affected are the ones with the fastest turnover. Marrow, gut epithelium,
> hair follicle, and gonad are hit for the same reason."

**Problem:** this is the one place the book explains something the reader has known since their first
year of training. It is the register CONVENTIONS.md rules out ("The reader already treats this
disease"). The paragraph then recovers strongly ("Febrile neutropenia risk is a property of the
regimen rather than of the patient. That is why primary growth factor prophylaxis is decided at the
point of regimen selection"), which is the chapter's real voice.
**Suggested rewrite:** cut the three explanatory sentences and open on the claim. "Myelosuppression
sets the schedule. Febrile neutropenia risk is a property of the regimen rather than of the patient,
which is why primary growth factor prophylaxis is decided at the point of regimen selection rather
than after the first episode."

### BC-600 BS-5170: opens as a signpost rather than an argument

> "Brain metastases are common in HER2-positive and triple-negative disease and less common in
> hormone receptor-positive HER2-negative disease, following the site distribution described in
> [@kennecke2010]. The colonisation biology, including the mediators identified in [@bos2009] and the
> serpin-dependent survival and vascular co-option described in [@valiente2014], belongs to
> [[BC-320]]."

**Problem:** the first sentence states a distribution the reader knows; the second is a list of three
citations whose only content is that the material is elsewhere. No claim is made in the opening
paragraph. Compare BC-450, which handles the same "this belongs to another chapter" job in one line
and then immediately asserts something: "The receptor biology is in [[BC-150]] and is not restated.
What belongs here is that an antibody against HER2 has three mechanisms and a kinase inhibitor has one
of them."
**Suggested rewrite:** "The colonisation biology belongs to [[BC-320]] and is not restated. What
belongs here is that screening asymptomatic patients is not supported by randomised evidence, and
that should be stated rather than implied." Then the existing second paragraph follows directly.

### BC-160 BS-1290: textbook sequence before any claim

> "Mitogenic signalling converges on one transcriptional decision. Cyclin D accumulates in response to
> growth factor and hormone input, then binds CDK4 or CDK6. The resulting complex phosphorylates
> retinoblastoma protein. Hypophosphorylated Rb holds E2F transcription factors inactive until that
> phosphorylation releases them. S-phase genes are then transcribed."

**Problem:** five sentences of narrated pathway before anything is asserted. Milder than BC-640, and
defensible in a mechanism chapter, but it is the only biology chapter that narrates rather than
argues in its opening. Compare BC-180's opening, which states the same kind of mechanism and
immediately says why it matters: "That restriction is why the pathway matters most at the replication
fork, and why its failure produces a replication-linked phenotype rather than a general repair
defect." BC-160 does eventually reach its claim ("That point is the restriction point, and CDK4/6
inhibitors work by holding the cell behind it") but only in the second paragraph.
**Fix:** move the restriction-point claim up and compress the narration behind it.

### BC-020 BS-0180: announces a definition instead of giving one

> "Overdiagnosis is a formal concept with a precise definition."

**Problem:** a sentence whose only content is that a definition is coming. This is the one
throat-clearing opener in the book.
**Suggested rewrite:** "Overdiagnosis is the detection of a cancer that would never have become
symptomatic in the patient's lifetime. It is not misdiagnosis, and it is not a false positive."
(The chapter already has the second sentence, four paragraphs on.)

### BC-560 BS-4820: restates its heading with a fact the reader uses daily

> Heading: "First-line endocrine therapy with CDK4/6 inhibition"
> First sentence: "First-line treatment is endocrine therapy with a CDK4/6 inhibitor for most
> patients."

**Problem:** the only restatement in the book that adds nothing. Every other high-overlap opener
(forty checked) makes a claim.
**Fix:** open on the question the section actually answers, which is which inhibitor and for how
long, since the three do not carry the same survival evidence. That point is made further down and
would work better first.

**Everything else is in voice.** Scans for promotional adjectives (24 hits), promotional verbs,
double hedging, "growing body of evidence", "we now know", "of course / obviously", "in summary /
taken together" and weak modals returned almost nothing, and on reading, every hit is analytic rather
than promotional: "robust to sampling", "excellent specificity", "landmark 3-year survival",
"promising strategy, not an established equivalence". No chapter is promotional about a therapy. The
nine "double hedges" are all deliberate disjunctions ("may or may not"), which is honesty rather than
hedging.

## Rule 3: the remaining long sentences, classified

**28 sentences exceed 35 words in 12,592.** One of those 28 is a false positive: BC-540 BS-4700 is
two sentences that my splitter merged because the second begins with a digit ("...the example worth
knowing. 4480 postmenopausal women were randomised..."). That leaves 27.

**Exempt. Colon introducing a series, no action needed (11).**
BC-050 BS-0360 (44w, relative risk across three histologic groups) · BC-080 BS-0640 (45w, the same
sentence) · BC-080 BS-0650 (43w, four density categories) · BC-370 BS-3350 (43w, "The calculation uses
five measurements:") · BC-390 BS-3550 (38w, "should state six things:") · BC-460 BS-4100 (43w,
"several baseline factors associated with higher risk:") · BC-690 BS-5920 (48w, "the three that
matter:") · BC-690 BS-5950 (40w, three findings) · BC-710 BS-6050 (53w, six WHO regions) · BC-710
BS-6070 (40w, "The benchmarks are, in order:") · BC-760 BS-6550 (36w, three-part list without a
colon). These are exactly the case CONVENTIONS.md exempts. Leave them.

Two of the eleven carry a small improvement worth making anyway:
- **BC-710 BS-6050** (53w) is lumpy because only the first of six regions carries its uncertainty
  interval inline. Split the African figure out: "Median five-year net survival was 39.1% in the
  African Region, with an uncertainty interval of 34.1% to 44.7%. Across the other five WHO regions it
  ran 61.0% in the Eastern Mediterranean, 66.3% in South-East Asia, 81.1% in the Western Pacific,
  84.0% in Europe and 88.5% in the Americas."
- **BC-690 BS-5920** (48w) chains before the colon ("Three numbers are obtainable..., and they are the
  three that matter:"). Trim to "Three numbers are obtainable from most cancer registries or
  electronic records, and they are the ones that matter:" or drop the first clause.

**Already covered above as rule 1 splits (5).** BC-060 BS-0460 (40w) · BC-300 BS-2480 (36w) · BC-300
BS-2600 (37w) · BC-390 BS-3550 (41w) · BC-230 BS-1890 (36w).

**Already covered above as the two worst (2).** BC-670 BS-5690 (54w) · BC-280 BS-2360 (52w).

**Genuinely long, worth splitting, not yet listed (2).**

**BC-050 BS-0420** (37w), "If the invasive population is a sample of the in situ population rather
than a selected subset of it, then what changes at the boundary is the boundary, or the stroma on the
other side of it."
→ "Suppose the invasive population is a sample of the in situ population rather than a selected subset
of it. Then what changes at the boundary is the boundary itself, or the stroma on the other side of
it."

**BC-060 BS-0520** (36w), "The consensus catalogue built from 9,423 tumour exomes using 26 algorithms
identified 299 driver genes and more than 3,400 putative missense driver mutations, of which
experimental validation confirmed 60% to 85% as likely drivers."
→ "The consensus catalogue built from 9,423 tumour exomes using 26 algorithms identified 299 driver
genes and more than 3,400 putative missense driver mutations. Experimental validation confirmed 60% to
85% of those mutations as likely drivers."

**Acceptable as dense single results, no action (7).** BC-180 BS-1450 (37w, OlympiAD) · BC-250 BS-2090
(36w) · BC-250 BS-2100 (36w, ATAC body mass index) · BC-280 BS-2300 (36w) · BC-300 BS-2490 (41w) ·
BC-670 BS-5680 (36w) · BC-670 BS-5710 (37w). Each carries one claim with a population, a comparison
and an interval. A 36-word sentence that is doing that work is not a style failure.

**One chapter's distribution is genuinely off.** BC-670 has a median of 13 words and a maximum of 54,
and holds 3 of the book's 27 over-35 sentences in only 945 words. That is the most skewed
distribution in the book, and it is in the chapter about communicating clearly. Fixing the 54-word
sentence resolves most of it.

## Rule 4: the one chapter that leans on colons

**BC-720** carries 8 colons in 2,316 words, 3.5 per 1000, against a book rate of 0.25. Every one is
legitimate on its own, but three sit in consecutive paragraphs in BS-6190 with identical construction:

> "Structure indicators describe what a service has: a linear accelerator, an accredited laboratory, a
> specialist nurse."
> "Process indicators describe what a service does: the proportion receiving an assay, the proportion
> starting treatment within a target interval."
> "Outcome indicators describe what happens to patients: survival, recurrence, patient-reported
> outcome."

**Problem:** not a rule violation but a rhythm one. Three sentences with the same shape in a row read
as a slide rather than as prose, and the chapter uses the same `X is: a, b, c` frame four more times
(BS-6160, BS-6170 twice, BS-6210).
**Fix:** vary one or two. "Structure indicators describe what a service has, such as a linear
accelerator, an accredited laboratory or a specialist nurse. Process indicators describe what it does.
The proportion receiving an assay and the proportion starting treatment within a target interval are
both process measures. Outcome indicators describe what happens to patients."

## Rule 5: smaller instances

**BC-250 BS-2040**. "Carriage was associated with a hazard ratio of 11.1 for subsequent haematologic
cancer and 1.4 for all-cause mortality." Against non-carriers, presumably, but it is not stated, and
neither ratio carries an interval. An 11.1 is a large enough number that its denominator should be
explicit.
→ "Against non-carriers, carriage was associated with a hazard ratio of 11.1 for subsequent
haematologic cancer and 1.4 for all-cause mortality."

**BC-250 BS-2110**. "Among 4459 patients with stage I to III disease, high allostatic load carried a
hazard ratio of 1.46 for all-cause mortality." The comparator is missing. **BC-690 BS-5810 quotes the
same finding from the same source and gets it right**: "high allostatic load carried a hazard ratio of
1.46 for all-cause mortality **against low allostatic load**". Copy BC-690's wording into BC-250. This
is a three-word fix and it removes an internal inconsistency between two chapters.

**BC-620 BS-5320**. "10-year relapse-free survival was 56% with standard chemotherapy and 50% with
capecitabine, with a hazard ratio of 0.80. Breast cancer-specific survival was 88% against 82%, with a
hazard ratio of 0.62. Overall survival was 62% against 56%, with a hazard ratio of 0.84." Three hazard
ratios, none with a stated direction and none with an interval. The reader has to infer from the
percentages which arm is the numerator. Say it once: "...with a hazard ratio of 0.80 for standard
chemotherapy against capecitabine."

**BC-560 BS-4820**. "A post hoc subgroup analysis suggested a survival benefit from first-line use in
premenopausal patients, with a hazard ratio of 0.53." No interval on a post hoc subgroup ratio, in a
caution block whose whole purpose is to restrain over-reading. Add the interval or say it was not
reported.

**BC-590 BS-5110**. "Confirmed response rates across the expression range were 70.6% in
HER2-overexpressing disease, 37.5% in HER2-low disease and 29.7% in HER2 non-expressing disease." Three
percentages, no denominators. In this dataset the non-expressing group is much the smallest, so 29.7%
rests on very few patients and the reader cannot tell. Give n for each band.

**BC-370 BS-3270**. "A negative result on a test with 85% sensitivity leaves substantial residual
probability when pretest probability was high to begin with." Which test has 85% sensitivity, and
substantial means what. In a passage arguing that clinicians misread negative tests, the worked number
is the argument.
→ "A negative result on a test with 85% sensitivity leaves 15% of cancers undetected. At a pretest
probability of 50%, a negative result still leaves a post-test probability near 13%."

**BC-580 BS-5080**. "Response rates in the refractory setting are low, at 5% for single-agent
chemotherapy in ascent." 5% of how many, and response by what criteria.

**BC-050 BS-0360 and BC-080 BS-0640**. the same null claim in both chapters, both without a figure:
"A family history added no significant further risk in that cohort" / "Family history did not add
significant further risk in women who already had atypia." A null result stated with "no significant"
and no interval cannot be distinguished from an underpowered one, which matters because both chapters
then tell the reader this is "counterintuitive and clinically consequential". Give the relative risk
with its interval.

**Three more bare magnitude words with no figure:** BC-210 BS-1680 ("significantly better disease-free
survival than patients with equally high scores and few or no structures") · BC-510 BS-4460
("substantially better prognosis without chemotherapy", and "dense lymphocytic infiltration" with no
threshold, which is also a rule 6 point) · BC-750 BS-6440 ("substantially reducing reader workload").

BC-420 BS-3760 looked like the same fault ("Radiation gave that group no significant benefit") but is
not: the next sentence supplies the interaction p of 0.066 and calls it "the honest summary of where
the evidence stands". No change needed.

## Cross-chapter repetition

25 sentences of 12 words or more appear verbatim in more than one chapter. **Twenty-two of them are
trial results**, and a reference book should state the same number the same way in two places, so
these are a sign of discipline rather than of copy-paste. Three are prose rather than data and read as
duplication:

- **BC-345 BS-3040 / BC-550 BS-4770**. two consecutive sentences copied whole: "A rising tumour
  marker with stable imaging and a stable patient is not progression. It is a reason to shorten the
  interval to the next assessment."
- **BC-220 BS-1740 / BC-230 BS-1880**. "In those tumours CD8 T cells sat in collagen-rich
  peritumoural stroma rather than in tumour parenchyma."
- **BC-260 BS-2160 / BC-270 BS-2210**. "between 66 and 69% of the variance sat between fields of view
  within a single section."

Also near-duplicates worth reconciling: **BC-050 BS-0360 and BC-080 BS-0640** carry the same 44-word
relative-risk sentence differing only in "breast cancer" against "subsequent breast cancer"; and
**BC-090 BS-0770** ("Inflammatory breast cancer is a clinical diagnosis") and **BC-520 BS-4550**
("Inflammatory breast cancer is diagnosed clinically") open adjacent arguments with the same sentence
reworded. In each case one of the two should cross-reference rather than restate.

## Smallest things

- **BC-730 BS-6240**. "And lines have no microenvironment, so every finding about tumour-stroma or
  tumour-immune interaction... is unavailable in them by construction." The only sentence-initial "And"
  in the book. Use "Third," to match the "Lines were selected... Lines drift..." series it closes.
- **BC-020 BS-0120 / BC-710 BS-6040**. thousands separators disagree between chapters (`685000`
  against `685 000`). The book otherwise uses commas (`21,457`, `84,729,690`, `4,459`). Three
  conventions are in use; pick one.
- **BC-560 BS-4900**. "Lobular carcinoma behaves differently in the metastatic setting, and most of
  the difference is a measurement problem rather than a treatment problem." This is the book's thesis
  in one line and it is excellent. Noted here only because it is the model the six off-voice openers
  should be rewritten against.

---

# Summary

**Counts.** BLOCKER 0. MAJOR 8 findings covering 25 sentences. MINOR 6 off-voice chapters, 2 long
sentences, 1 colon-heavy chapter, 10 unanchored-number instances, 5 cross-chapter duplications, 3
trivia.

**Rule-by-rule verdict.**

| Rule | Verdict |
|---|---|
| 1. No chained independent clauses | 541 instances book-wide at a constant rate. A house rhythm, not drift. 11 genuinely chain two separate claims. |
| 2. No em or en dashes | **Perfect. Zero, across all seven dash codepoints.** |
| 3. Mean 15-18, nothing over 35 | Book mean 15.2, chapter means 13.2 to 17.5. 27 real sentences over 35, of which 11 are exempt enumerations, 9 need splitting, 7 are acceptable dense results. |
| 4. Avoid semicolons and colons | **Zero semicolons.** 47 colons, all legitimate series. One chapter (BC-720) leans on them. |
| 5. Say what a number is a number of | The weakest rule. ~15 instances, and one hazard ratio repeated unanchored across three chapters. |
| 6. Separate biology from measurement | Strong, because it is the book's subject. 2 genuine lapses, both in chapters that get it right elsewhere. |
| 7. No filler | **Effectively perfect.** 2 hits in 191,668 words, both false positives. Never explains a basic term. |
| Register | 73 of 79 chapters are unmistakably one voice. 6 openings read as a different hand. |

**The three things most worth fixing before merge.**

1. **Decide rule 1 once, at book level, and write the decision into CONVENTIONS.md.** The `, and <new
   subject> <verb>` coda appears 541 times at an almost constant rate across all 79 chapters. That
   uniformity is the evidence that it is the author's own device rather than agent drift, and
   mechanically splitting all 541 would cost the book its best rhetorical move. Sanction the coda and
   the tricolon explicitly, then apply the rule strictly to the 11 sentences listed above that chain
   two separately checkable claims. Doing this first prevents a fix pass from flattening 12,000
   sentences in pursuit of a rule the author does not actually want applied absolutely.

2. **Fix the six unanchored numbers that a reader could act on.** The ESR1 hazard ratio of 3.1 appears
   in BC-300, BC-345 and BC-390 with no comparator and no interval in any of the three. BC-250 quotes
   the allostatic load hazard ratio without its comparator while BC-690 quotes the same finding from
   the same source correctly. BC-470 calls a subgroup "PD-L1-positive" two paragraphs before the
   chapter explains that PD-L1 is not one test, and the two trials in that section selected patients
   on different antibodies and different thresholds. BC-620 gives three hazard ratios with no stated
   direction. These are cheap fixes and each removes either an internal inconsistency or a reading a
   clinician could carry into clinic.

3. **Rewrite the six off-voice openings, starting with BC-020 and BC-710.** Those two open with the
   same textbook sentence, the same source and the same three numbers, telling a breast oncologist
   that breast cancer is the commonest cancer in women. BC-640 explains why cytotoxics cause
   myelosuppression. BC-600 opens with two sentences that make no claim. Each chapter's own second
   paragraph, or its own subtitle, is a better opener than what is there, so these are cuts rather
   than rewrites. Six openings out of seventy-nine is a very small number, and fixing them makes the
   book read as one hand throughout.
