# Literature search brief: dealer gamma exposure (GEX)

## The book and why this search
"The Other End of the Trade" is a textbook on SPX/XSP options and dealer mechanics, in the
library at /home/user/library/books/the-other-end-of-the-trade. Its reader knows algebra and
introductory statistics. Part VIII, "The whole market" (chapters/8a.md to 8d.md, with notes in
notes/8a.md to 8d.md), adds up every dealer's gamma into gamma exposure (GEX) and asks what the
total does to prices: the sign problem, the gamma flip and walls, two regimes (damping and
amplifying), feedback mathematics, stress episodes (Volmageddon 2018, March 2020, August 2024,
GME 2021) and gamma squeezes. Related chapters: 6D (gamma), 7B (second-order Greeks: vanna,
charm), 9A (VIX and the vanna loop), 9B (0DTE), 9C (reading the tape), 10H and 10I (the Edge
Book's skeptical view of GEX levels), 11A (a market dashboard).

The author wants Part VIII rewritten and much expanded into a synthesis of the whole GEX
literature, theory, evidence and practice, with a commercial heatmap product (Skylit's
"Heatseeker", GEX and VEX heatmaps by strike and expiry) as an example of applying the theory
in practice. Your search feeds that rewrite.

## Rules
- Never invent a paper, an author, a number, a journal, a volume or a page. Every source you
  list must be confirmed by a search result (Consensus or WebSearch) that shows its title and
  authors. Give the URL(s) that confirmed it.
- Mark any detail you could not confirm "[unverified]" (for example a page range or an exact
  effect size you remember but did not see). Omit it if in doubt.
- Record numbers with their units and sample exactly as the source states them.
- Working papers are fine, but label them (SSRN, NBER, arXiv, and the year of the version).
- Vendor and practitioner material is fine, but label it as such, and separate what it claims
  from what anyone has tested.
- Network: skylit.ai, ssrn.com, arxiv.org, scribd.com and most publisher sites are blocked for
  direct fetching. WebSearch works (its results include summaries of the pages), and the
  Consensus academic search works (load it with ToolSearch "select:mcp__Consensus__search";
  run Consensus searches one at a time, and wait and retry if you hit a rate limit). WebFetch
  may work for some other hosts; try it when a page matters.
- Do not edit anything under /home/user/library. Write only your output file.

## Output
Write one markdown file (the path is in your task). For each source:

### <Key, e.g. NiPearsonPoteshman2005>
- Citation: Authors (Year). "Title." Journal Volume(Issue): pages. DOI or URL.
- Type: peer-reviewed article | working paper (where, which version) | book | practitioner
  white paper | vendor documentation | regulator or exchange report
- Verified via: the URLs that confirm it; which details are unverified
- Question: what it asks
- Data and method: sample, period, instruments, approach
- Findings: key results with numbers and units
- Limits: caveats, disputes, later work that qualifies it
- Use in the book: the topic it serves and the claim it supports or contradicts

End with a synthesis: what the literature agrees on; where it disagrees; what is untested or
only claimed; numbers worth quoting (with source keys); and figure ideas (interactive figures
that would show a finding: what they draw and what the reader controls).

Your final reply to me: the output path, the number of sources, and the ten most important
findings in two lines each.

## Save as you go (the container can restart and lose unsaved work)
Create your output file at once with a heading, then APPEND each source entry to it as soon as
you have verified it, and append the synthesis at the end. Never hold more than one entry in
memory unsaved. If your output file already exists when you start, read it, keep every entry
in it, and continue from where it stops without redoing what is there.
