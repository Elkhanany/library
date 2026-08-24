# Applying this batch

`nmt-part0-clear.bundle` sits on `497f8f2`, which is what GitHub currently has. It carries **five
commits**: Part I's conversion (which you had not synced yet), Part 0's conversion, the
cross-reference audit, and the status update. One bundle, one pull.

```bash
cd ~/path/to/newton-to-mtheory
git pull ~/Downloads/nmt-part0-clear.bundle main
git push
```

`apply-batch.sh` does not exist in your tree until this lands, which is why the first command is the
long form. After this it will, and the next batch is just `./apply-batch.sh`.

Nothing else is needed. `docs/` is built and committed, so Pages updates on push.

## What changed

**Twelve chapters now carry the `clear` tag** in the contents list: all of Part 0, plus 1.1–1.3.
The tag is read out of the chapter file at build time, so it can only ever say what is true.

**Thirty-one content corrections**, listed with their reasoning in `reports/part0-corrections.md`.
Fifteen came out of reading Part 0 closely enough to re-say it. Sixteen came from `xrefcheck.py`,
which is new: it proves every "Chapter N.M" in the book resolves, and prints all 590 distinct
source–target pairs beside the title each actually lands on, so the half a machine cannot judge is
one page instead of an evening.

Two of those sixteen were quietly corrupting future work rather than the current text. `debts.py`
hands every promise to whoever writes the target chapter, so Chapter 7.1's brief had picked up a
requirement to derive the Born–Infeld action, and 4.5's had picked up a tunnelling barrier.

## One thing worth your eye

Chapter 1.3 leans twice on "the inverse function theorem of Chapter 0.6", and the whole
Legendre-transform argument rests on it. Chapter 0.6 states only the *implicit* function theorem.
The chapter was named correctly; the theorem was never stated anywhere in the book. I have stated it
in 0.6 §8 with a ⚑, since its proof is a contraction-mapping argument that belongs to a real
analysis course, and noted it is equivalent to the implicit version already quoted in §7.

If you would rather it were derived than quoted, say so and I will build it — but it would be the
first genuinely analytic proof in Part 0, and I do not think it earns its place.
