# The binding sample for the plain-language register

Written by the reader, 24 August 2026, as a rewrite of Chapter 2.1 §1. Everything about the `clear`
register is calibrated from this. Where a rule in `CONVENTIONS.md` disagrees with this text, this
text wins.

---

### 1. Galilean Relativity, Stated Precisely

Let's start by looking closely at an idea that has been central to physics for over four hundred
years: Galilean relativity. To understand the crisis that sparked modern physics, we first need to
separate the core principle of relativity from the specific mathematical transformation we use to
calculate it. For centuries, these two concepts were treated as the exact same thing. Once we pry
them apart, the path forward will become much clearer.

#### 1.1 The Transformation

Imagine two observers, each with their own coordinate system or "frame" of reference. We will call
the stationary frame S and the moving frame S'. Let's give them both a measuring tape and a clock,
and assume they perfectly agree on how to use them.

To keep the math simple, we'll align their axes and have them start their stopwatches at t=0 exactly
when they pass each other. After that moment, the S' frame slides away in the positive x direction
at a steady speed v. This setup is known as the standard configuration, and it will be our baseline
for exploring relativity.

Now, suppose something happens — an "event" — and both observers write down where and when it
occurred.

- The observer in frame S records the position as x and the time as t.
- Meanwhile, the origin of the moving frame S' has shifted forward by a distance of v × t. Because
  of this shift, the moving observer will measure the event's position as x − vt.

We are also going to make a crucial assumption here: both observers will record the exact same time
t. This leads us directly to the classical Galilean transformation:

[EQUATION]

Let's pause and look at that final equation, t' = t. It might look like simple bookkeeping, but it
actually contains a massive physical claim: that there is a single, universal clock ticking at the
exact same rate for everyone in the universe, regardless of how fast they are moving. Isaac Newton
built his mechanics on this idea of absolute time. It feels so intuitive to our everyday experience
that it is hard to realize it is merely an assumption.

As we dive deeper into relativity, the first three equations will survive with a few tweaks, but
this universal time equation will completely fall apart.

#### 1.2 Velocities Add

Next, let's see how our observers view motion. Imagine a particle traveling along a path. The
stationary observer tracks its position as x(t). Using our transformation, the moving observer
tracks its position as x'(t') = x(t) − vt.

To find the particle's velocity, we just need to take the derivative. Since we assumed that time is
the same for both observers (t' = t), differentiating with respect to t' is identical to
differentiating with respect to t:

[EQUATION]

This equation tells us something very familiar: velocities simply add or subtract depending on your
point of view. If you throw a ball forward inside a moving train, a person standing on the platform
sees the ball moving at the speed of the throw plus the speed of the train. For everyday objects,
this is incredibly accurate.

But notice the hidden mechanics here: the subtraction comes from the shift in space, while the ease
of the derivative relies entirely on the assumption that t' = t. When that assumption about time
breaks later on, this rule for adding velocities will have to change too.
