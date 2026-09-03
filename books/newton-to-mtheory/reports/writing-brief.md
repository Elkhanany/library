# Brief: writing a new chapter

This is the brief for writing a chapter **from scratch**. `reports/register-brief.md` is a different
document — it is for converting an existing chapter, and its whole subject is what must not change.
Nothing here is optional and nothing here is a second pass. The register is the first draft.

Read before you start:

- `reports/register-sample.md` — the reader's own rewrite of Chapter 2.1 §1. **Binding.** Where
  anything below disagrees with it, the sample wins.
- `CONVENTIONS.md` in full, including *"The plain-language register"*.
- `MATHPLAN-4.md` for this chapter's numbered build items and its fixed section list.
- `python3 debts.py <N.M>` — every sentence in the written book that names your chapter. Each one is
  a requirement, not a hope.
- Two finished chapters, read at length, not skimmed: **`src/ch3-6.html`** for how a derivation
  chapter runs, and **`src/ch4-2.html`** for how a chapter that builds machinery for later use runs.

## Who is reading

A breast medical oncologist. Strong mathematically, rebuilding physics from scratch, reading in the
evening after clinic. He is not short of intelligence and he is short of working memory for your
notation. Every time he has to scroll back to find what a symbol meant, you have lost him for a
paragraph.

He has said what he wants, twice, and both times it was about the same thing:

> *"very dense and theatrical without classical simplicity that can make deep understanding clear."*

> *"narrative flow of the text that handles one idea to the next naturally while keeping equations
> all in context."*

---

# Part 1 · Narrative flow

**This is the part that matters most, and it is the part no checker can verify.** Everything in
Part 2 is measurable and is enforced by a script. Flow is not. It is judged by a reader, and a
review pass exists for it (`reports/flow-review-brief.md`). Write as though that reader is the only
check, because in practice they are.

## The test

Read your chapter aloud from the first line of a section to the last. **At no point should the
reader have to ask "why are we doing this?" and not already know the answer.** If they would, the
sentence that answers it belongs earlier, not later.

That is the whole of it. The rest of this section is how to get there.

## One thread, and it is never dropped

A section is an argument, not a list of true statements. It starts somewhere, it is going somewhere,
and every paragraph moves from one to the other. The reader should be able to stop at any paragraph
and say where they are in that journey.

Concretely:

**Open every section by saying where it is going.** Not what it contains — where it is *going*, and
what will be true at the end that is not true now. Chapter 3.6 §1 does this in three sentences:

> Here is where this section is going. We identify the source of gravity as the energy–momentum
> tensor of Chapter 2.6. We promote its conservation law to a curved manifold, and we write down its
> form for the two kinds of matter this book needs. The important consequence is that pressure is a
> source of gravity, and no Newtonian intuition supplies that.

Note the last sentence. It tells the reader which part to care about before they have met any of it.

**Close every section by saying what is now in hand**, and name the next thing it makes possible.
The seam between two sections is where a reader puts the book down. Give them a reason not to.

**Never let a paragraph begin cold.** A paragraph that opens with a new symbol, a new object or a
new claim, with no connection to the paragraph above it, is a dropped thread. The repair is almost
always one clause at the front: *"That leaves the question of…"*, *"The same argument, run in the
other direction, gives…"*, *"None of this yet says which geometry…"*.

**When you introduce a constraint, say what it will exclude.** When you make an assumption, say
where it will be paid for. When something is left undone, say which chapter does it. A forward
pointer is concrete or it is noise: not *"this will come back to haunt us"* but *"we will need this
in Chapter 4.6, where the barrier is finite and the wavefunction leaks through it."*

## Equations in context

An equation is a sentence in the argument, not an interruption to it. It arrives because the
argument needed it, and it leaves having changed what the reader knows.

**Before every display equation, the reader knows why it is coming.** State the goal, then take the
step:

> We want a tensor that reproduces that, and only two objects are available to build it out of,
> $u^{\mu}$ and $g^{\mu\nu}$:

Never the operation first. *"Differentiate both sides"* tells the reader what you did. *"We want the
velocity on its own, so differentiate both sides"* tells them why, which is the only part they
cannot reconstruct themselves.

**After a display equation, say what it means before moving on.** Not always — a definitional
display that the sentence runs through does not need a gloss, and adding one is padding. But a
result does. The rule is: if the reader would have to work out for themselves *what changed*, tell
them.

**Never put two display equations back to back with nothing between them.** This is the one flow
failure that is measurable, and it is checked (see Part 2). The algebra being complete is not the
same as the thread being followable, and this is where the thread most often drops.

**Keep a symbol's meaning within reach.** If a symbol has not appeared for two pages, remind the
reader what it is when it returns — in three words, inside the sentence, not in a parenthesis.

**Grind boxes are the pressure valve.** Long algebra the reader opens deliberately goes in a
`<details class="grind">`. That is what lets the main line stay a line. If a stretch of your section
is six manipulations with nothing to say between them, it belongs in a grind box and the main text
should state what goes in, what comes out, and why the middle is safe to skip.

## Pace — the cap

**About six new objects per chapter**, an object being what would earn a row in the Math Ledger.
Your `MATHPLAN` block states the count; if what you are writing is drifting past it, stop and say so
rather than writing a bigger chapter. Part IV's first three chapters carry twelve and thirteen, and
the reader told us plainly that this reads as running around.

Place **two or three sitting breaks** at the real seams:

    <p class="pause"><span>a natural place to stop &nbsp;·&nbsp; what follows builds the space itself</span></p>

A quiet rule across the column. It says where to stop and what the next stretch is about. No number,
nothing depends on it.

## Annotated equations

`\ann{expression}{label}` puts a label in small type under a brace. Use it on **the equation that
defines something or states a headline result, and nowhere else** — one or two per chapter. An
annotation under every display is noise. Never annotate a step inside a derivation: if the symbols
need explaining there, what is missing is the prose bridge. Labels are prose — *how stiff spacetime
is*, not *coupling constant*.

## Rhythm

- **One idea per sentence.** If you find yourself writing a dash, that is usually two sentences.
- **Short paragraphs.** Three or four sentences. Let the page breathe.
- **Bullets where a two-sided or three-sided comparison would tangle in prose.** Not for lists of
  facts — for comparisons the reader would otherwise have to hold in their head.
- **Vary the signposts.** "Here is where this section is going" is a good sentence and a bad tic.
  Chapter 3.7 had seven identical stage directions before they were varied.

## Everyday anchors, and the one hazard

The reader's clinical fluency is real and usable **in the main text** where the mathematics is
genuinely identical — first-order kinetics, log-odds, a rate constant, a dose–response curve.

**An analogy that is nearly right is worse than none.** This has already gone wrong once: Chapter
4.1's mass-action analogy mapped Einstein's $B_{21}$ onto an off-rate it does not correspond to, in
front of a reader who computes $K_D$ for a living, and the error was precisely what made the
argument look like it closed when it does not. Before you write an analogy, check the map term by
term. If any term has no counterpart, either say so explicitly — that is often the interesting part
— or drop the analogy.

## Forbidden

*Obviously, clearly, of course, it turns out that, it can be shown.* And *simply* used to wave past
work rather than to mean *in a simple way*. Each of these tells the reader that something is easy at
the exact moment they are finding it hard.

Do not hedge to sound friendly. *Perhaps, one might say, arguably* make prose worse, not warmer. The
fix for density is subtractive: split the sentence, delete the dash.

**"We", "let's" and "you" are permitted here** and this register deliberately overrides the
second-person-only rule and the ban on *let's*.

---

# Part 2 · What is checked

## Targets

    python3 registercheck.py --new src/chN-M.html

| | limit | why |
|---|---|---|
| em-dashes | ≤ 1.0 / 1000 prose words | the dash is where two ideas get welded |
| semicolons | ≤ 2.5 / 1000 prose words | same, one notch quieter |
| sentences over 35 words | ≤ 14% | not length itself — length *plus* interruption |
| consecutive equations with ≤ 8 words between | < 3% | the thread-drop, measured |

It also checks that `<!--REGISTER:clear-->` is line 1.

**These are necessary and nowhere near sufficient.** A chapter can pass every one of them and still
be unreadable, because the four things a script can count are not the four things that matter. Two
further flow metrics were built and calibrated against all thirty converted chapters, and both were
discarded: they fired mostly on correct writing, because a definitional display legitimately takes a
short lead-in and a result stated inside a sentence legitimately has little after it. Gating on
either would have taught the writer to pad. Flow is reviewed by a reader instead.

## Everything else

- `python3 tagcheck.py` — no `<` a browser reads as a tag, no unbalanced block element. **A `<`
  followed by a letter silently deletes text to the next `>`.** Inside maths write `\lt` and `\gt`.
- `python3 xrefcheck.py` — every "Chapter N.M" resolves. Then read `xrefcheck.py --all` for your own
  chapter's rows and confirm each target is about what you claimed. Fifty-five corrections across
  three batches, and thirteen of them were references that resolved to a real chapter about the
  wrong subject. Nothing else catches that.
- `python3 debts.py <N.M>` — run it again when you are done and confirm every promise is paid.
- `python3 make.py && python3 verify.py && python3 figcheck.py chN-M` before you report back.

## The contract that outranks all of this

**Nothing is asserted that has not been derived.** Anything quoted rather than proved carries ⚑, and
the sentence says who proves it and where. Metric signature $(+,-,-,-)$. Riemann convention
$[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$. $G$ and $c$ written out.
**Use the measured combination $GM$, never $G\times M$** — $GM_\odot$ is known to ten figures and
$G$ alone to five.

An agent that writes a chapter does not review it. Expect an independent pass, and expect it to find
things.
