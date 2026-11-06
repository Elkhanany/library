# Registry completeness sweep, November 2026

The second completeness pass on `trials.yaml`, after the October pass that added 170 catalogue records
from the High impact reviews. That pass could only find trials those reviews cited, so NSABP B-17, B-24,
UK/ANZ DCIS and SweDCIS, among others, were still missing. This pass looked for every randomised breast
cancer trial the registry should hold.

**Status: list saved, records not yet built.** The build is planned for the week of 9 November 2026.

## What is here

| File | What it holds |
|---|---|
| `to-add.json` | The 674 trials to add, one object each: name (and the other names it was seen under), registration number, phase, randomised or not, setting, whether a guideline cites it, the primary PMID, every PMID from the sweep that belongs to it, PMIDs found on PubMed during triage, and the earliest year seen |
| `to-add.csv` | The same 674 as a table, guideline-cited first |
| `triage-decisions.json` | Every decision the triage made, 1,283 objects: 806 add (674 trials once duplicates across chunks were merged), 142 already in the registry under another key, 335 excluded with the reason |
| `scripts/` | `gather.py` (fetch from PubMed), `match.py` (match against the registry), `consolidate.py` (merge the triage chunks), and the triage brief |

## How the list was made (5 to 6 November 2026)

1. **Sources.** PubMed papers tagged phase 3 in breast cancer, or randomised trials naming phase 3 in the
   title or abstract (about 2,700 papers); the cited references of the 79 ESMO and ASCO breast guidelines
   from 2015 on (PubMed holds reference lists for 18 of them, 1,273 references); and the NCCN v6.2026
   reference list in `../nccn-breast-v6.2026-references.csv`. 3,559 papers in all, fetched from PubMed.
2. **Matching.** A paper was set aside when its PMID was already a reference of a registry trial (446),
   when its NCT or ISRCTN number was on a registry record (208), or when a registry trial's name was in its
   title (298). 1,033 papers were not trial reports and 19 were not about breast cancer. 1,555 papers
   were left.
3. **Triage.** Eight agents read the 1,555 papers and sorted them into trials. They grouped secondary
   analyses with their parent trial, searched PubMed for primary reports, and decided:
   - **add** a randomised trial of any phase that NCCN, ESMO or ASCO cites, a non-randomised study a
     guideline relies on, or a randomised phase 3 trial with a published primary result;
   - **exists** for a trial already in the registry under another name;
   - **exclude** for everything else, with the reason.
4. **Merging.** Duplicates across chunks were merged on registration number, PMID and name: 806 add
   decisions became 674 trials. NSABP B-24 was added by hand, because the triage confirmed it was missing
   but no paper in the sweep carried it.

## The 674

| Source | Kind | Trials |
|---|---|---|
| Cited by NCCN, ESMO or ASCO | randomised treatment trials | 105 |
| | non-randomised studies the guidelines rely on | 31 |
| | supportive care, survivorship, screening | 28 |
| PubMed phase 3, no guideline citation | randomised treatment trials | 439 |
| | randomised supportive or survivorship trials | 70 |
| | screening | 1 |

Earliest paper seen: 82 before 2000, 351 from 2000 to 2014, 239 from 2015 on.

## The decision still open

Which of the 674 to build. The three choices that were put on 6 November:

1. **All 674.** This matches the aim of a registry that holds every trial. The registry would hold about 1,270 records.
2. **604:** all guideline-cited trials, the randomised phase 3 treatment trials and the screening trial,
   without the 70 supportive and survivorship trials no guideline cites.
3. **The 164 guideline-cited trials only**, with the rest kept here for a later round.

## Before building, check

- **Registration numbers.** Some triage agents gave NCT numbers from memory and said so in their reports.
  Treat every `nct` as unverified until ClinicalTrials.gov confirms it.
- **Attributions the triage inferred.** The `reason` field names the inferred ones. Examples: HeCOG
  translational papers attached to HE 10/97 or HE 10/00, and a Swedish VEGF paper attached to the 2 vs 5
  years tamoxifen trial.
- **Pooled or paired trials** that may need splitting into two records:
  - fulvestrant 0020 and 0021;
  - DBCG 82b and 82c;
  - anastrozole 0004 and 0005;
  - NEAT and BR9601.
- **Excluded only because no primary report was found:** IRMA, TAXIS, HYPORT-Adjuvant, BONBIS, HYPOSIB,
  Young Boost, NEOS, JCOG 8808 and others. Search again before the build, because a primary paper may have
  appeared since.
- **Name collisions with existing keys.** The French FNCLCC TAM-01 is not the registry's `tam01`, the
  Japanese EMERALD is not `emerald`, and the first-line metastatic PF-05280014 trial is not
  `pf-05280014-neoadjuvant`.
- **Building the records.** Use the October method: catalogue records built from
  `scripts/BRIEF-catalogue.md` and checked against PubMed, about 30 records per agent. Change its date and
  paths before reuse.
