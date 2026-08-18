# "In Plain Terms" — style and narrative plan

*The specification for ~150 boxes across 59 chapters. Written before insertion so that
the boxes read as one continuous voice rather than 150 separate asides.*

---

## 1. What these boxes are for

The book's main text is deliberately unyielding: it derives everything and asserts nothing. That
is the right register for the mathematics, and it is not going to change. But it is dry, and
dryness has a specific cost — a reader can follow every step of a derivation and still finish a
section without knowing *what happened*. The algebra is legible; the meaning is not.

Each box does three things, in this order of priority:

1. **Says what just happened**, in language that would survive being read aloud.
2. **Supplies the intuition the derivation assumed but never stated.** Almost every section has a
   motivating idea that was obvious to the author and therefore went unwritten. That idea is the
   most valuable thing the box can carry.
3. **Names the hidden move** — the assumption that quietly did the work, the reason this object
   and not some other one, the thing you'd have to un-learn later.

Equally important is what they are **not**:

- Not a summary of the algebra. If a box can be written by paraphrasing the equations, it has failed.
- Not a substitute for the derivation. A reader who reads only the boxes should end up correctly
  oriented, and aware they have not done the work.
- Not simplification. The reader is a scientist. The register changes; the respect does not.

---

## 2. The through-line

The boxes must be readable end to end as a single essay. That requires one governing idea, stated
in plain language, that every box is somewhere on. Here it is:

> **Ask what stays the same when you change your point of view. Whatever survives is real; whatever
> does not was a fact about where you were standing.**

This is the plain-language form of the book's technical spine (*pick a symmetry, write the most
general action invariant under it, quantize*), and it genuinely runs through every part:

| Part | The same idea, wearing that part's clothes |
|---|---|
| **0 · The Toolkit** | Numbers describe a thing only relative to a choice. The useful quantities are the ones whose change is *predictable* — and the useful basis is the one in which the problem falls apart into independent pieces. |
| **I · The Action Principle** | Forces are the wrong primitive. Attach one number to each possible history, and nature selects the history where that number stops changing. Every continuous symmetry then hands you a conservation law for free. |
| **II · Special Relativity** | The speed limit is built into the geometry, not into the materials. Observers slice one fabric differently; what they agree on is the interval. Magnetism turns out to be electricity, seen from a moving frame. |
| **III · General Relativity** | Gravity is not a force but the shape of the arena. Matter tells geometry how to bend; geometry tells matter how to move. Free fall is the straightest available motion. |
| **IV · Quantum Mechanics** | "What state is this in" stops having a single answer. The state is a direction in an abstract space, measurement is a projection, and the mathematics was already built in Part 0. |
| **V · Quantum Field Theory** | Relativity plus quantum mechanics makes particles untenable as fundamental objects. The field is fundamental; particles are its excitations, the way notes are excitations of a string. |
| **VI · Gauge Theory** | Demand that a symmetry hold *locally* rather than globally, and a force appears to enforce it. Every force in nature is that one demand, made of a different symmetry. |
| **VII · Strings and M-Theory** | Gravity refuses the treatment that worked for everything else. Strings are a proposal in which it is not added but unavoidable — followed by an honest accounting of what is known, conjectured, and untested. |

**Every box should be placeable on that table.** If an agent cannot say which row a box belongs to,
the box is describing machinery rather than meaning, and needs rewriting.

### The recurring motifs

Four threads recur. Boxes should name them *by the same words each time*, so the repetition is
felt as a drumbeat rather than read as an accident:

- **"A choice of perspective."** Coordinates, bases, frames, gauges. The book's central move is
  separating what depends on this from what does not.
- **"Falling apart into independent pieces."** Eigenvectors, normal modes, Fourier components,
  energy eigenstates, particle states. The same trick, seven times.
- **"Nearly everything is an approximation."** Physics is expanded, not solved. Say so, repeatedly.
- **"The thing that had to exist."** Most objects in this book were not invented, they were forced.
  Whenever a box can show that an object was *cornered into existence*, it should.

---

## 3. The voice

Calibrated from the reader's own rewrite, which is the binding sample.

**Do:**
- Long, complete, connected sentences. Let a thought finish before the next begins.
- Explicit connectives — *because*, *so that*, *which means*, *naturally*, *the reason is*. The
  reader should never have to supply the link themselves.
- Warm and patient. This is the voice of someone explaining over coffee, not delivering a verdict.
- Name the stakes: *the fatal error is…*, *what genuinely matters is…*, *most importantly of all…*
- Concrete physical pictures — arrows, sheets, contour lines, rulers, sloshing, stacks.

**Don't:**
- Clipped fragments and aphorisms. *"Slope gets you none of them."* is main-text voice, not this.
- Em-dash pile-ups. One per paragraph at most.
- Rhetorical questions, exclamation marks, "imagine you're on a train", "simply", "just", "of course".
- Second-guessing the reader's intelligence in either direction — no flattery, no talking down.

**Analogies:** only where the mapping is genuinely tight, and say what breaks when it does. A loose
analogy in a box like this is worse than none, because the reader will trust it.

**Mathematics:** essentially none. No display equations, ever. Named quantities in words
(*"the interval"*, *"the metric"*) rather than symbols. A bare symbol is permitted only where the
name would be clumsier, and never more than one or two per box. Where the main text says
$F^{\mu\nu}$, the box says *"the field tensor"*.

---

## 4. Form

| | |
|---|---|
| **Label** | `In plain terms` + number |
| **Numbering** | chapter.section — `3.4.2` closes §2 of Chapter 3.4 |
| **Placement** | At the **end** of each major section, immediately before the next `<h2>` |
| **Length** | 180–230 words. Two or three paragraphs. |
| **Density** | One per substantive `<h2>`. Skip "Worked examples", "Your turn", and any section under two paragraphs. Typically 6–9 per chapter. |
| **Colour** | Soft rose panel, full border — distinct from the amber warnings and the blue orientation boxes |
| **Markup** | `<div class="callout plain"><span class="ct">In plain terms <span class="pnum">3.4.2</span></span><p>…</p></div>` |

---

## 5. Continuity between boxes

This is what turns a pile of boxes into an essay, and it is the part most likely to be done badly
at scale.

- **Each box may assume every earlier box, and nothing later.** Written for a reader who has read
  the boxes and skipped the algebra.
- **Reach backwards by picture, not by citation.** *"the stack-of-sheets picture from the last
  chapter"* — not *"as shown in 2.4.3"*. The numbers exist for the ledger's benefit, not the prose's.
- **Forward promises are allowed and encouraged, but must be kept.** If a box says *"this becomes
  the whole of gravity"*, some later box has to collect. A register of these is maintained during
  the build and checked at the end.
- **No two consecutive boxes may open the same way.** At scale the temptation is *"The reason this
  matters is…"* every time. Vary deliberately.
- **The last box of a chapter should land**, giving the reader the sense that a thing was completed
  and naming what it now makes possible.

---

## 6. The Through-Line

A page, `throughline.html`, sitting beside the Math Ledger.

Assembled **by extraction**, not written by hand: a build step pulls every `.callout.plain` from
every chapter, in order, and lays them out as continuous prose with their chapter and section
headings. It therefore can never drift out of sync — edit a box and the Through-Line updates on the
next build.

Between the parts I'll write short **bridging passages** (150–250 words) in the same voice, doing
what a box cannot: standing outside the chapters and saying where the argument has got to and what
is about to be demanded of it. Eight bridges, one before each part.

Read start to finish, the result is roughly **30,000 words of plain-language physics** — a complete
account of the arc from *what is a derivative* to *what string theory is actually claiming*, with no
mathematics in it, that stands entirely on its own and can be read by someone who never opens a
chapter.

---

## 7. How it gets built

| Pass | What it does |
|---|---|
| **1 · Write** | Agents in batches of 4–5 chapters. Each gets this document, the target chapters, and **the full text of every box already written before its chapters** — so continuity is real rather than hoped for. Chapters are done in book order, never in parallel across a boundary. |
| **2 · Structure** | Rebuild everything; verify no box broke a `<details>` block, orphaned an equation, collided with an id, or changed a single character of the existing prose. A diff confirms insertions only. |
| **3 · Continuity** | One agent reads all ~150 boxes end to end, with no chapters, and reports: repeated openings, repeated analogies, forward promises never kept, places where the thread drops, and any box that cannot be placed on the §2 table. |
| **4 · Repair** | Fix what pass 3 found, then rebuild the Through-Line. |

**Batch order (complete):** 2.4 (sample), 0.1–0.3, 0.4–0.6, 0.7–0.9, I (1.1–1.4),
II-a (2.1–2.3), II-b (2.5–2.6). Parts 0, I and II are done — 138 passages, ~31,000 words.

### From Part III onward: one pass, not two

The catch-up is finished, and the four-pass process above is **retired for new chapters**. Every
chapter from 3.1 on is written with its boxes in place from the start, by the same agent, in the
same sitting. That agent gets this document alongside the chapter's mathematical plan.

The reason is not speed. An author who writes the derivation and its plain-language account together
knows which step was the one that mattered, and the box says so; an author arriving afterwards can
only summarise what is on the page. The 2.6 boxes are the evidence — they name the load-bearing move
in each section rather than paraphrasing it, because that chapter's structure was still live in
memory when they were written.

Two things stay:

- **The continuity input.** Each new chapter's brief carries the boxes that precede it, so the thread
  and the forward promises remain real rather than hoped for.
- **The periodic reunification pass.** At the end of each part, one agent reads every box written so
  far, end to end and with no chapters, and reports repeated openings, dropped threads, promises
  never collected, and any box that has drifted off the §2 table. That is cheap, catches the drift
  that accumulates invisibly, and is the only way a 400-passage essay stays one voice.

---

## 8. The test

A box has succeeded if a smart colleague who has never opened a physics textbook can read it and
come away with something true, non-trivial, and load-bearing — and if you, having just done the
derivation, read it and think *yes, that is what I just did, and now I can say it to someone else.*
