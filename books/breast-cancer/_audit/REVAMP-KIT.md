# Revamp kit — read in full before editing a management chapter

Read alongside `WRITING-KIT.md` (the standing contract, including THE CITATION RULE) and
`CONVENTIONS.md` (macros, blocks, voice). This adds only what is new for this pass.

Ahmed's brief: revamp the management chapters extensively, incorporating the groundbreaking trials
now in the registry, and use the Chapter Stories as the argument the trials are evidence for.

## Three layers, three jobs

| Layer | Lives in | Says |
|---|---|---|
| Story | `stories.yaml` | what we were trying to find out, and whether we found it out |
| Table | `trials.yaml`, rendered by an `evidence` filter | what else is in this cell |
| Prose | the chapter | the argument, the judgement, what to do on Monday |

**Tables enumerate. Stories argue the question. Prose argues the decision.**

## The story block

````
```story ST-010
```                         the whole story: its premise, then all its questions

```story SQ-0040,SQ-0050
```                         selected questions from one story
````

No body. One block, one story: you cannot mix questions from two stories in one block. The renderer
prints each question as five labelled moves (rationale, experiment, finding, limitation, next) and
the trials that carry it, and **every trial in a story block counts as a citation of that trial**,
so a story block clears debt.

A story carries no figures, by design, so a story and a table can never disagree about a number.

Use `python3 tools/stories.py --tree` to see every story and question, and
`python3 tools/stories.py --render ST-###` to read one in full before you write around it.

Pick the block that fits the chapter's job. An evidence chapter that owns a position renders the
whole story. A decision chapter that touches one question of it renders just that question.

## The evidence block

````
```evidence setting=metastatic subtype=TNBC line=1L modality=immunotherapy,chemo
```
````

No body. Rows render from `trials.yaml`. Check any filter with
`python3 tools/evidence.py --render "<filter>"` before you commit to it. A filter matching no trial
fails the build.

## What to do with numbers already in the prose

This is the specific instruction for this pass, and it applies to every chapter you touch.

**Move enumerated results out of prose and into a generated table.** A paragraph that recites
four trials with their hazard ratios is a table written by hand. Replace it with an `evidence`
block and prose that says what the four trials together establish.

**Keep a number in prose only where the argument is about that number.** Two trials of one class
disagreeing, an absolute benefit that a relative one misrepresents, a confidence interval whose
bound carries the argument. Then quoting it is analysis, not enumeration.

When in doubt, ask whether the sentence would still make its point if the number were replaced by
"a large difference". If yes, the number belongs in the table.

Do not delete a fact that exists nowhere else. If a number is in the prose and not in the registry,
put it in your trials patch so the table can carry it.

## Clearing trial debt

`python3 tools/evidence.py --gaps` lists every trial assigned to a chapter that the chapter never
cites. Your chapter's debts are named there. A trial is cited when it appears as `{{trial:key}}` in
prose, in a rendered evidence table, or in a story block.

Clearing a debt does not mean naming every trial in a sentence. A trial that belongs in a table is
cited by the table. Reach for prose only when the trial changes the argument.

If a trial is assigned to your chapter and does not belong there, say so in your report rather than
forcing it in. Mis-assignment is a registry fix, not a prose problem.

## Registry patches

**Do not edit `trials.yaml`, `references.yaml` or `stories.yaml` directly.** Several agents are
working at once. Write additions and changes to:

- `_audit/PATCH-trials-<your-chapter-ids>.yaml`
- `_audit/PATCH-refs-<your-chapter-ids>.yaml`

as a mapping of key to the fields you are adding or changing. They are merged centrally.

Every reference must be verified against PubMed before use. Never invent a key, PMID or DOI.

## Before you report

```
cd /tmp/lib
python3 tools/evidence.py --check
python3 tools/stories.py --check
grep -c '^## BS-' books/breast-cancer/chapters/BC-###.md     # must match the spec
```

Headings must match `_specs/BC-###.txt` byte for byte. No em dashes. Do not chain independent
clauses. Mean sentence length 15 to 18 words, nothing over about 35 outside an enumeration.
