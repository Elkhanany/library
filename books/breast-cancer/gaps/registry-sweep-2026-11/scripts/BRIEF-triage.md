# Brief: triage candidate papers for the breast cancer trial registry completeness sweep

The registry is /home/user/library/books/breast-cancer/trials.yaml (593 trials; each has a key, an
`acronym`, often an `nct`, and `pubs` pointing at /home/user/library/books/breast-cancer/references.yaml,
whose entries carry a `pmid` and a `trial` key). Read only; edit nothing under /home/user/library.

A script gathered PubMed papers from three sources (the NCCN v6.2026 breast reference list, the reference
lists of ESMO and ASCO breast guidelines, and every PubMed paper tagged phase 3 in breast cancer) and removed
those already matched to the registry by PMID, registration number or a trial name in the title. What is left
is in your input file: a list of groups (papers sharing a registration number or a guessed trial name, or a
single paper), each with the papers' PMID, year, journal, title, publication types, registration numbers,
sources ("nccn", "guideline:<pmid>", "pubmed-phase3"), the first 900 characters of the abstract, and
`maybe_registry`: registry keys whose name appears in the title or abstract (a hint only, often wrong).

The grouping is rough. Two groups may be one trial; one group may hold two trials; a group named
"name:ADJUVANTBREAST" may hold NSABP B-17 papers. Work out the real trial behind each paper.

## Your job

For every paper decide which trial it reports, and then for every trial decide one of:

- **exists**: the trial is already in the registry under some key (grep trials.yaml for its name, drug,
  NCT number and acronym spellings; grep references.yaml for its PMID). Give the key.
- **add**: a trial the registry should hold as a new catalogue record, because it is either
  (a) a randomised trial of any phase in breast cancer, or in women at risk of it, cited by a guideline
      (source "nccn" or "guideline:..."), or a non-randomised study a guideline cites as evidence for a
      recommendation (a single-arm registration trial, a prospective omission or de-escalation cohort); or
  (b) a randomised phase 3 trial in breast cancer, or in women at risk of it, whose primary efficacy
      result is published (the paper in hand, or one you find on PubMed).
  Treatments, local therapy, prevention, screening and imaging strategies, and supportive or survivorship
  interventions all count.
- **exclude**: everything else. Give the reason in a few words. Typical reasons: not a trial report
  (methods, quality assurance, pharmacokinetics, a translational or biomarker study of samples); a
  non-randomised "phase 3" study no guideline cites; a mixed-tumour trial in which breast cancer is a
  minority and that no guideline cites for breast cancer; a pilot or feasibility study; a trial whose only
  report is a protocol or trial-in-progress paper.

A secondary analysis, update or substudy of a trial is not a separate trial: attach it to its parent. If the
parent exists in the registry, the paper's trial is "exists". If the parent is new, the parent is "add" and the
paper is one of its PMIDs.

Use PubMed (ToolSearch "select:mcp__PubMed__get_article_metadata,mcp__PubMed__search_articles") when you
need to find a trial's primary report or confirm what a paper is. Use it sparingly: most decisions can be made
from the title and abstract. Do not use web search.

## Output

Write a JSON list to your output path, one object per distinct trial you found (not per paper):

{"decision": "add" | "exists" | "exclude",
 "name": "the trial's usual name, e.g. NSABP B-17, SweDCIS, UK/ANZ DCIS, or a descriptive name if it has none",
 "registry_key": "<key, for exists>",
 "nct": "NCT... or ISRCTN... if known, else null",
 "phase": "3" | "2" | "2/3" | ... | null,
 "randomised": true | false | null,
 "setting": "early | metastatic | dcis | prevention | screening | ...",
 "guideline_cited": true | false,
 "primary_pmid": "PMID of the main efficacy report if known (for add)",
 "pmids": ["every PMID in your input that belongs to this trial"],
 "other_pmids_found": ["PMIDs you found on PubMed that belong to it (for add)"],
 "reason": "one short phrase (required for exclude; optional otherwise)"}

Every PMID in your input must appear in exactly one object's "pmids". Check that with a script before you
finish. Final message: counts of add / exists / exclude, and any trial you were unsure about, with why.
