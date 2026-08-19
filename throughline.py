#!/usr/bin/env python3
"""
Build src/_throughline.html by extracting every "In plain terms" box, in book order.

The Through-Line is never authored directly — it is assembled from the chapters, so it
cannot drift out of sync. Edit a box in a chapter and it changes here on the next build.
Bridging passages between parts live in BRIDGES below and are the only prose written here.
"""
import os, re, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")

spec = importlib.util.spec_from_file_location("bp", os.path.join(ROOT, "build.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

BOX_RE = re.compile(
    r'<div class="callout plain">\s*<span class="ct">.*?<span class="pnum">([\d.]+)</span>'
    r'\s*</span>\s*(.*?)\s*</div>', re.S)

BRIDGES = {
"Part 0 · The Toolkit": """
<p>What follows is the whole book, with the mathematics taken out.</p>
<p>Each passage below was written to close a section of a chapter, in the reader's own language
rather than the chapter's. Read in place they are pauses for breath. Read here, one after another,
they are a continuous account of how physics arrived at its present picture of the world, with no
equation anywhere in it. The finished arc runs from the definition of a derivative to what string
theory is actually claiming; what exists today runs as far as the field equations of gravity, and
the closing passage at the foot of the page says what that leaves owed.</p>
<p>One idea runs underneath all of it. <b>Ask what stays the same when you change your point of
view. Whatever survives is real; whatever does not was a fact about where you were standing.</b>
Everything that follows is that sentence, applied to progressively larger questions.</p>
<p>Four moves recur, and their names are worth having before meeting them. The first is a choice of
perspective, which is what coordinates, bases, frames and gauges all are, and separating what
depends on it from what does not is this book's central habit. The second is a problem falling apart
into independent pieces, which happens under a different name in nearly every part and is one
theorem spent over and over. The third is that nearly everything is an approximation, since physics
does not usually solve its problems but expands them, and the honest version of the method names
what was thrown away. The fourth is the thing that had to exist: most of the objects here were not
invented but cornered, forced into being by a requirement rather than chosen for convenience.</p>
<p>Part 0 builds tools rather than physics. But the tools are not neutral, and the choices made in
building them decide what can be said later.</p>""",

"Part I · The Action Principle": """
<p>The trade about to be made is not obviously a good one, and the least flattering version of it
should be put first.</p>
<p>Newtonian mechanics has a hole in the middle of it. The second law predicts nothing at all until
somebody supplies a force, and every force is imported from outside, fitted to data and justified by
working. What is about to replace it has a hole in precisely the same place. One function is still
supplied by hand, and no argument in this part derives it. The only change &mdash; and the whole of
Part I is the case that this is the change that matters &mdash; is that the function becomes a
single number attached to each history the world might follow, in place of a bundle of arrows
attached to each body at each instant.</p>
<p>Three things are bought with that, and the third is the one worth the fare. A number does not
care which coordinates it is written in, so the equations keep their shape when the description
changes, which arrows conspicuously fail to do. A number can be written down for a thing that has no
particles to hang arrows on, which is what a field is. And a number can be asked to stay unchanged
under some transformation, whereupon it hands back a conserved quantity without being asked twice.
That last is the largest result in classical physics, and it cannot even be stated in the language
being given up.</p>""",

"Part II · Special Relativity": """
<p>Two statements were held on excellent evidence by the 1890s, and they cannot both be true.</p>
<p>The first is old and Galilean: the laws of physics read the same in any laboratory moving
steadily, confirmed every time nobody in a ship's cabin falls over. The second is that the equations
of electricity and magnetism contain a speed, assembled out of two constants measured with a
capacitor and a current balance, with no light anywhere in the measurement, and that the speed comes
out as the speed of light. A speed in a law is a speed with respect to something, and three decades
of increasingly delicate experiments failed to say what.</p>
<p>Part I supplied the instrument for handling a collision of this kind, though not the answer.
Writing a theory as one number per history made it possible to ask of any law whether its shape
survives a change of description, and to read that off the shape rather than grind through the
algebra. The question is about to be put to Maxwell's equations, and the answer is that they survive
a transformation nobody had thought to write down.</p>
<p>One thing should be named in advance so that it does not arrive as a conjuring trick. What has to
be surrendered is not the ether, which nobody will miss. It is the shared present: the assumption,
so deep that physics before this point has no name for it, that two events either happen at the same
moment or do not, and that everybody can be told which.</p>""",

"Part III · General Relativity": """
<p>Three chapters ago the interval was a fact about a fabric nobody could move. It is about to
become the thing that moves.</p>
<p>What Part II delivered was a geometry with a speed limit written into it rather than into any
material, and a way of telling, by looking at the shape of an equation, whether a law was about the
world or about a laboratory. What it could not deliver was gravity, and the reason is worth stating
precisely rather than as a slogan. Newton's law of gravitation names two masses and the distance
between them, and the distance between them at a given moment is exactly the kind of quantity the
last part showed to be a fact about who is asking. There is no repair available that keeps a force
and fixes the timing, because the trouble is not the speed at which gravity travels but the
arithmetic in which the law is written.</p>
<p>What follows takes the one measured coincidence that nobody in three centuries could explain,
that a body's reluctance to be pushed and its response to gravity are the same number, and treats it
as the whole of the subject. The price is that the arena stops being furniture. Distance becomes a
field with equations of its own, the toolkit's warning about comparing an arrow here with an arrow
there comes due, and by the end of this part the shape of space and the contents of space are two
halves of one equation.</p>""",

"Part IV · Quantum Mechanics": """
<p>A run of results in Part 0 was proved, admired and then left lying about with no visible use.
They are all collected here, at once.</p>
<p>That a self-partnered map has real multipliers and perpendicular special directions. That a
rotation with no real special direction acquires two the instant complex numbers are admitted, and
that their multipliers are phases. That a map whose partner undoes it changes no length, so anything
evolving by one keeps its total for ever. That a function on an interval is a sum over a basis of
waves, and that the total of the whole is the sum of the totals of the parts. None of that was
physics when it was proved. All of it is the physics now.</p>
<p>What forces the change is that two assumptions carried unexamined through everything so far both
fail, and they fail together. The first is that a thing has a definite state and that measuring it
is a matter of sufficient care. The second is that a quantity nobody has measured nevertheless has a
value. Neither survives contact with experiment at the scale of an atom, and what replaces them is
not a repair to mechanics but a different kind of object altogether: a direction in an abstract
space, evolving by a rotation, with measurement a projection onto an axis and the prediction the
squared length of the shadow.</p>""",

"Part V · Quantum Field Theory": """
<p>Confine a particle to a small enough box and the last two parts, working together, will put a
second particle in it.</p>
<p>The mechanism is a multiplication of two results, neither of them in any doubt. Squeezing
something into a region makes its momentum, and so its energy, uncertain by an amount that grows as
the region shrinks; and energy amounting to twice a particle's rest mass is enough to make a fresh
pair out of nothing. So there is a size below which the question <i>how many particles are in
here</i> stops having an answer, and the size is neither small nor exotic. A theory whose central
object is a particle, and whose central question is where that particle is, cannot be written down
at all.</p>
<p>What replaces it was built in the toolkit for an entirely different purpose. Two masses joined by
springs have two normal modes; a chain of them has as many modes as masses; let the number run away
and the chain becomes a continuous medium whose modes are waves. A field is what infinitely many
coupled oscillators turn into, which was promised at the time and is collected here. Quantise those
oscillators one at a time and the particle stops being the thing that exists: it becomes the name
for one unit of excitation in one mode, the way a note is not an object but a way a string is
moving.</p>""",

"Part VI · Gauge Theory and the Standard Model": """
<p>Nothing so far has said why there are the particular forces there are, and the question has been
quietly assembling its own answer since Part 0.</p>
<p>Two loose threads are the whole of it. The first was noticed while the electromagnetic potentials
were being introduced: a whole function's worth of freedom sits in them that no measurement can see,
and it was named at the time as the seed from which every force in the Standard Model grows. The
second was raised at the close of the chapter on symmetry. A field of complex values whose physics
is unchanged when its phase is turned by one angle everywhere carries a conserved charge, and that
charge is electricity &mdash; but requiring the angle to be the same everywhere requires
instantaneous agreement across the universe, which the part after it made an incoherent thing to
ask.</p>
<p>Put the two together and what comes out is one demand, made four times. Let the angle vary from
place to place; the invariance breaks; the only repair available is a new field whose transformation
law is built to cancel the breakage; and the new field's own equations are then not chosen but
forced. Run that on a circle and electromagnetism appears. Run it on the rotations of a two-part
object and the weak interaction appears, on a three-part object and the strong. The forces are not
four facts about the world. They are one construction, performed on four different symmetries.</p>""",

"Part VII · Strings and M-Theory": """
<p>What follows is the least secure part of this book, and saying so before rather than afterwards
is the only honest way to begin it.</p>
<p>Look back along the arc first, because it has been one method throughout. Name a symmetry, write
down the most general law respecting it, quantise. That produced mechanics, then electromagnetism,
then the weak and strong interactions, and the agreement between calculation and measurement in the
last of those is the closest agreement of the kind anywhere in science. Applied to gravity the same
procedure produces a theory that returns infinity for quantities measured to be finite, and the
device that rescued every earlier case &mdash; absorbing the infinities into a short list of
measured constants &mdash; needs an endless list here and therefore rescues nothing.</p>
<p>Strings are the most developed proposal for what to do about that. The single change is to
replace the point with an object of finite extent, whereupon gravity is not added to the theory but
is unavoidable in it, which is either the deepest fact in physics or the most seductive coincidence
in it. What follows builds the construction in the same way everything else here was built, and then
separates, without softening and without advocacy, what is derived from what is conjectured, and
what has been tested from what has not.</p>"""
}

CLOSING = """
<p>That is as far as the argument has been carried, and it is worth saying plainly where it stops
rather than letting the page run out.</p>
<p>Four things have been built. There is a toolkit, which turned out not to be neutral, since
defining a derivative as a linear stand-in rather than as a slope is what allowed one definition to
survive several variables, then whole histories, then curved space. There is a mechanics in which
forces are not primitive, one number is attached to each history the world might follow, and every
continuous symmetry hands back a conserved quantity. There is a geometry in which one speed is the
same for everybody with nothing for it to be measured against, and in which electricity and
magnetism stop being two fields and become one object, sliced differently by observers in different
states of motion. And there is a gravity that is not a force but the shape of the arena, cornered
into its final form by the demand that the geometry side of the equation impose no condition on
matter that matter has never been observed to obey.</p>
<p>What is owed is larger than what has been delivered. Part III is finished, so the account of gravity
has now been run against a star, against light and against the universe, and the last of those
returned the news that a growing universe has no conserved energy for anything to belong to. Nothing here has said what happens when a thing has no definite state,
though the mathematics that answers it was built in Part 0 for reasons with no physics in them.
Nothing has said why there are the particular forces there are, though the shape of the answer has
been visible since the redundancy in the electromagnetic potentials was noticed and deliberately
left alone. And nothing has said what to do about the one subject that has refused every method that
worked for the others, which is the subject this whole arc has been walking towards. Those are the
promises made here and not yet kept, and they are kept in the order the book takes them.</p>"""


def extract():
    parts = []
    for label, sub, chs in bp.PARTS:
        entries = []
        for num, slug, title, _m in chs:
            f = os.path.join(SRC, slug + ".html")
            if not os.path.exists(f):
                continue
            boxes = BOX_RE.findall(open(f).read())
            if boxes:
                entries.append((num, title, slug, boxes))
        if entries:
            parts.append((label, sub, entries))
    return parts


def build():
    parts = extract()
    total = sum(len(b) for _, _, e in parts for *_, b in [e[0]] for _ in [0]) if parts else 0
    total = sum(len(bx) for _, _, entries in parts for *_, bx in entries)
    words = 0
    out = ['<p class="eyebrow">Reference</p>',
           '<h1>The Through-Line</h1>',
           '<p class="subtitle">The whole book in plain language, assembled from every '
           '&ldquo;In plain terms&rdquo; passage in order. No mathematics.</p>']

    for label, sub, entries in parts:
        out.append('<div class="callout plain bridge">%s</div>' % BRIDGES.get(label, ""))
        out.append('<h2>%s</h2>' % html.escape(label))
        out.append('<p class="part-sub">%s</p>' % html.escape(sub))
        for num, title, slug, boxes in entries:
            out.append('<h3><a href="%s.html">%s &nbsp;%s</a></h3>' %
                       (slug, num, html.escape(title)))
            for pnum, body in boxes:
                words += len(re.sub(r"<[^>]+>", " ", body).split())
                out.append('<div class="tl-item"><span class="tl-num">%s</span>\n%s\n</div>'
                           % (pnum, body.strip()))

    first = parts[0][0].split(" ")[1].rstrip("·").strip() if parts else "0"
    last = parts[-1][0].split(" ")[1].rstrip("·").strip() if parts else "0"
    span = ("Part %s only" % first) if first == last else ("Parts %s to %s of eight" % (first, last))
    hdr = ('<p style="color:var(--ink-soft);font-size:.95rem">'
           '<b>%d passages</b> &nbsp;·&nbsp; about %s words &nbsp;·&nbsp; '
           '%s, complete through cosmology &nbsp;·&nbsp; '
           'reads start to finish as one essay &nbsp;·&nbsp; '
           '<a href="ledger.html">Math Ledger</a></p>' % (total, f"{words:,}", span))
    out.append('<div class="callout plain bridge tl-closing">%s</div>' % CLOSING)
    out.insert(3, hdr)
    open(os.path.join(SRC, "_throughline.html"), "w").write("\n\n".join(out))
    print(f"through-line: {total} passages, {words:,} words")


if __name__ == "__main__":
    build()
