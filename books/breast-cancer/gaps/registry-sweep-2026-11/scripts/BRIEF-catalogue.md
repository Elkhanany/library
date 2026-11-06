# Brief: catalogue records for the breast cancer trial registry

The registry is /home/user/library/books/breast-cancer/trials.yaml, its references
/home/user/library/books/breast-cancer/references.yaml. Read CONVENTIONS.md in that folder:
"Registry fields", "The trial registry and Appendix A", "Catalogue records", "Evidence weight", and
the line-of-therapy paragraphs (from "A line in metastatic disease is the position..." through the
`entry=` paragraph). Look at three existing records of the same kind as yours before you write any
(for example monarche, cleopatra, ascent, tropion-b05, neostar), and copy their style.

The aim is completeness. Every trial in your input file is cited by high-impact clinical reviews and
is not in the registry. Each becomes one new record with `catalogue: true`, filled from its
publications and verified against PubMed. No chapter prose and no story question changes: catalogue
records are kept out of every evidence table and story by the flag.

Sources. PubMed only (ToolSearch "select:mcp__PubMed__get_article_metadata,mcp__PubMed__search_articles,mcp__PubMed__get_full_text_article"; batch up to 50 PMIDs per metadata call). ClinicalTrials.gov
(https://clinicaltrials.gov/api/v2/studies/NCTxxxxxxxx) only to confirm an NCT number or an
eligibility rule the paper does not state, and say so in `note`. Every figure must appear in the
abstract (or the PMC full text). Each number states its comparison and population. Where an abstract
misprints a figure, leave it out and say so in notes.

For each trial:
1. Find its primary report (the paper the trial is known for) and, where it exists, its final or
   long-term report. Use the PMIDs in your input as the starting point; search PubMed for the
   primary or final paper if the cited one is a substudy. Before writing anything, grep trials.yaml
   for the trial's name, drug and NCT: if the trial is already there under another name, do not make
   a record; put it in your final message as a duplicate.
2. Write the record: acronym, arms, discipline, endpoint, line, line_basis and prior_therapy (advanced
   disease only), modality, n (randomised; for a single-arm study the analysed population, said so in
   note), nct (only if PubMed prints it or ClinicalTrials.gov confirms it), note (only if a row needs
   it), os ("not yet reported" or "not reported" if the papers give none), phase, population,
   primary_ref (the paper the tabulated result comes from: for a mature trial usually the long-term
   report), pubs (every paper you used, primary_ref included, each with kind and role), result
   (primary endpoint with its comparison, never a bare hazard ratio), setting, status (reported),
   subtype, topic, year (of primary_ref), digest.methods and digest.results from the primary_ref
   abstract, `catalogue: true`, and `weight: exploratory` for single-arm, phase 1 or
   non-comparative studies. Use the vocabulary in /home/user/library/tools/evidence.py VOCAB exactly.
   Line tags follow CONVENTIONS (spans; first-line designs stay 1L; a required prior treatment given
   in the curative setting counts as a line; the HR+ endocrine-phase-as-one-line rule for
   chemotherapy and conjugate trials). Omit `chapters`, `cited_by` and `reviewed` (the tool sets it).
3. References: one references.yaml entry per paper, keyed surname + year + trial slug (for example
   cuzick2002ibis1), with authors ("Surname AB, Surname CD, Surname EF, et al."), doi, journal (PubMed
   ISO abbreviation), pmid (string), title (no trailing full stop), trial (record key), type: trial,
   verified: true, year, and volume/pages if PubMed has them. Grep references.yaml for each PMID
   first: if a paper is already there under another key, reuse that key in pubs and do not add it
   again.
4. Record keys follow the registry's key policy: lowercase acronym, suffixed with the population when
   a name is reused (dare-tbcrc). Grep trials.yaml for the key first.

Output: a JSON list in the format /home/user/library/tools/registry_apply.py documents in its
docstring (read it), one object per trial: {"key", "verdict": "confirmed", "final": {"field_changes":
[], "pubs_add": [], "new_refs_yaml": "<two-space-indented references entries>", "new_record_yaml":
"<two-space-indented trials entry>", "prose_edits": [], "stories_named": [], "notes": "..."}}.
Build it with a script so the YAML is valid (yaml.safe_dump, width 116), not by hand.

Test it: copy the tree (cp -r /home/user/library/books /home/user/library/tools <yourdir>/lib/), run
`python3 tools/registry_apply.py <batch> --dry --date=2026-10-29` and then the real apply in the copy,
then `python3 tools/evidence.py --check`, `python3 tools/evidence.py --lines` and
`python3 tools/synthcheck.py --quiet`. Nothing may be skipped and no check may get worse. Do not
edit anything under /home/user/library.

Final message: how many records and references you wrote, every trial you found already in the
registry or could not verify, every figure you left out and why, and anything a reviewer should check.
