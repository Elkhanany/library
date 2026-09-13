---
id: threads
title: "Cross-cutting threads"
status: brief
---

Four arguments recur across parts. Each is one argument told several times, and the reader
should be able to trace it. Every instance carries an explicit forward or backward reference.

## 1 · HER2 as the spine of `her2-het` and `adc`

The genetic against protein-level distinction in [[BC-280]], the bystander effect in [[BC-460]],
and the antigen-threshold-as-eligibility lesson in [[BC-590]] are one argument told three times.
They must cross-reference each other explicitly. A reader who reads any one of them should be
told where the other two are.

## 2 · The surrogate endpoint thread

pCR in [[BC-500]], [[BC-510]], and [[BC-540]]. MRD and ctDNA in [[BC-390]]. OS against PFS in
[[BC-740]]. A reader should be able to trace one question across the book, which is what does
this endpoint actually predict. The KEYNOTE-522 result, where OS benefit exceeds what pCR
predicts [@schmid2024k522os], is the thread's strongest single data point.

## 3 · The de-escalation thread

Surgery, axilla, radiation, chemotherapy omission by genomic assay, and chemotherapy-sparing
HER2 regimens all belong to one movement. [[BC-400]] names it. [[BC-410]], [[BC-420]],
[[BC-480]], [[BC-490]], [[BC-500]], and [[BC-510]] instantiate it. [[BC-740]] owns the
methodology of proving less-is-not-worse.

**Structural requirement.** Every de-escalation instance carries an explicit forward reference to
the non-inferiority margin discussion in [[BC-740]]. The recurring reader confusion is conflating
no significant difference with proven equivalent, and a single methods chapter cannot fix it
unless the disease chapters point at it.

## 4 · The disparities and access thread

Equity is not quarantined in Part XIII. Every disease chapter carries an interplay callout, for
example PIK3CA mutation frequency by ancestry in [[BC-560]] and trial representation in
[[BC-740]]. [[BC-250]] provides the biological bridge through allostatic load, so the thread
enters the book as biology rather than as an addendum.

## Interplay callout requirement

Every disease-focused chapter in Parts IX and X carries at least one:

````
```interplay target=BC-280
One or two sentences tying this chapter's subtype content back to the heterogeneity or
microenvironment argument.
```
````

The build renders it as a styled aside and adds the edge to appendix APP-F. `validate.py` warns
when a disease chapter has none.
