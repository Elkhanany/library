# Audit kit — read in full before starting

You are auditing a finished 79-chapter breast cancer reference before it is merged.
The reader is a practising breast medical oncologist. The author is one too.

**You do not edit chapters.** You report findings to your assigned file. Another process applies fixes.

## Where things are

| Path | What |
|---|---|
| `books/breast-cancer/chapters/BC-###.md` | The prose. 79 files. |
| `books/breast-cancer/references.yaml` | 741 entries under `refs:`. Each has authors, title, journal, year, volume, pages, pmid, doi. |
| `books/breast-cancer/trials.yaml` | 112 entries under `trials:`. Each has acronym, phase, setting, subtype, topic, sometimes `claim` and `primary_ref`. |
| `books/breast-cancer/outline.yaml` | Structure. 14 parts, 79 chapters, 673 sections. |
| `books/breast-cancer/CONVENTIONS.md` | Authoritative on macros, blocks and voice. |

## Macros you will see

```
[@key]                        reference from references.yaml
[@key1; @key2]                grouped
{{trial:key}}                 trial from trials.yaml
[[BC-###]]  [[BS-####]]       chapter or section cross-reference
[[term:key]]                  glossary term
```

Fenced blocks: ```interplay target=BC-###```, ```practice```, ```caution```.

## The standard the book was written to

- A citation key may only be used if it exists in `references.yaml`. No invented keys, PMIDs or DOIs.
- A number must be traceable to its cited source. A number without a source was supposed to be dropped.
- Say what a number is a number *of*. A hazard ratio without its comparison is decoration.
- Separate biology from measurement. If a claim is about an assay threshold, a sampling scheme or a
  scoring convention, it should say so.
- Voice: do not chain independent clauses, give each its own sentence. Mean 15 to 18 words. Nothing
  over about 35, except enumerations. No em dashes anywhere.

## Verifying with PubMed

You have `mcp__PubMed__search_articles` and `mcp__PubMed__get_article_metadata`. Use them.
Fetch the abstract and check the number against it. An abstract that does not contain the number is
not proof the number is wrong, but it is a flag worth reporting as UNVERIFIED rather than WRONG.

## Severity

- **BLOCKER** — a number, hazard ratio, survival figure, dose or indication that is wrong, or a claim
  that would lead a reader to a wrong clinical decision. Say what the correct value is.
- **MAJOR** — a claim not supported by the cited source, a citation pointing at the wrong paper, a
  significance claim that misstates the trial, an internal contradiction between chapters.
- **MINOR** — style, register, a missing denominator, an imprecise but not misleading statement.

## Output format — write your findings file as you go, do not hold them to the end

```markdown
# Audit: <your scope>

## BLOCKER
### BC-###  BS-####
**Claim as written:** <quote the sentence>
**Problem:** <what is wrong>
**Correct value / fix:** <the corrected statement, with PMID if you verified it>
**Source checked:** PMID ######## / not verifiable

## MAJOR
...
## MINOR
...

## Summary
<counts by severity, and the three things most worth fixing before merge>
```

If a chapter is clean, say nothing about it. Do not pad. A short honest report beats a long one.
