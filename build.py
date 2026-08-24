#!/usr/bin/env python3
"""
From Newton to M-Theory — build script.

Chapter content lives as HTML fragments in src/<slug>.html.
This wraps each in the shared shell (CSS + JS inlined so every chapter
is standalone), builds the index hub and the Math Ledger.

    python3 build.py
"""
import json, os, re, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, ".staging")

CDN = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9"

# ---------------------------------------------------------------- curriculum
# (part label, part subtitle, [ (num, slug, title, is_math_chapter) ... ])
PARTS = [
 ("Part 0 · The Toolkit", "Rebuild the floor. No physics yet — but every example comes from physics.", [
  ("0.1","ch0-1","What a Derivative Really Is",True),
  ("0.2","ch0-2","Integration and Accumulation",True),
  ("0.3","ch0-3","Series, Approximation, Orders of Magnitude",True),
  ("0.4","ch0-4","Vector Spaces and Linear Maps",True),
  ("0.5","ch0-5","Inner Products, Eigenvectors, Spectral Theorem",True),
  ("0.6","ch0-6","Multivariable Calculus",True),
  ("0.7","ch0-7","Fields, Flux, and the Big Theorems",True),
  ("0.8","ch0-8","Differential Equations and the Oscillator",True),
  ("0.9","ch0-9","Fourier, Delta Functions, Probability",True),
 ]),
 ("Part I · The Action Principle", "The most-skipped prerequisite in physics — and the reason people wall out at GR.", [
  ("1.1","ch1-1","What's Wrong With Forces",False),
  ("1.2","ch1-2","Stationary Action",True),
  ("1.3","ch1-3","Hamilton and Phase Space",False),
  ("1.4","ch1-4","Noether's Theorem",False),
 ]),
 ("Part II · Special Relativity", "Geometry replaces mechanics.", [
  ("2.1","ch2-1","The Crisis of 1900",False),
  ("2.2","ch2-2","The Lorentz Transformation, Derived",False),
  ("2.3","ch2-3","Minkowski Geometry",False),
  ("2.4","ch2-4","Tensors, Honestly",True),
  ("2.5","ch2-5","Relativistic Dynamics",False),
  ("2.6","ch2-6","Electromagnetism Is Relativity",False),
 ]),
 ("Part III · General Relativity", "Geometry becomes dynamical.", [
  ("3.1","ch3-1","The Equivalence Principle",False),
  ("3.2","ch3-2","Manifolds",True),
  ("3.3","ch3-3","Metric and Connection",True),
  ("3.4","ch3-4","Curvature",True),
  ("3.5","ch3-5","Forms, Lie Derivatives, Killing Vectors",True),
  ("3.6","ch3-6","The Einstein Field Equations",False),
  ("3.7","ch3-7","Schwarzschild: The Solution and Its Orbits",False),
  ("3.8","ch3-8","Light, Redshift, and What a Horizon Is",False),
  ("3.9","ch3-9","Cosmology, and a Loose Thread",False),
 ]),
 ("Part IV · Quantum Mechanics", "Linear algebra, taken absolutely seriously.", [
  ("4.1","ch4-1","What Classical Physics Cannot Do",False),
  ("4.2","ch4-2","The Linear Algebra of Quantum States",True),
  ("4.3","ch4-3","Function Spaces: Measure, L², and Completeness",True),
  ("4.4","ch4-4","Operators in Infinite Dimensions",True),
  ("4.5","ch4-5","The Schrödinger Equation",False),
  ("4.6","ch4-6","Systems You Can Solve in One Dimension",False),
  ("4.7","ch4-7","Symmetry, Commutators, and the Classical Limit",False),
  ("4.8","ch4-8","Angular Momentum and Spin",False),
  ("4.9","ch4-9","The Hydrogen Atom",False),
  ("4.10","ch4-10","Perturbation Theory and Transitions",False),
  ("4.11","ch4-11","Identical Particles, Entanglement, and Measurement",False),
 ]),
 ("Part V · Quantum Field Theory", "Particles stop being fundamental.", [
  ("5.1","ch5-1","Why Quantum Mechanics and Relativity Force Fields",False),
  ("5.2","ch5-2","Classical Field Theory",False),
  ("5.3","ch5-3","Quantising a Field",False),
  ("5.4","ch5-4","Distributions, Contours, and the Propagator",True),
  ("5.5","ch5-5","The Dirac Equation",False),
  ("5.6","ch5-6","The Path Integral",False),
  ("5.7","ch5-7","Gaussian and Grassmann Integration",True),
  ("5.8","ch5-8","Interactions, Wick's Theorem, and the Feynman Rules",False),
  ("5.9","ch5-9","A Real Calculation",False),
  ("5.10","ch5-10","Loops, Divergences, and Regularisation",False),
  ("5.11","ch5-11","Renormalisation and the Renormalisation Group",False),
 ]),
 ("Part VI · Gauge Theory and the Standard Model", "Symmetry, made local, generates every force.", [
  ("6.1","ch6-1","Lie Groups and Lie Algebras",True),
  ("6.2","ch6-2","Representations",True),
  ("6.3","ch6-3","The Gauge Principle",False),
  ("6.4","ch6-4","Yang–Mills",False),
  ("6.5","ch6-5","QCD and Asymptotic Freedom",False),
  ("6.6","ch6-6","Spontaneous Symmetry Breaking and the Higgs Mechanism",False),
  ("6.7","ch6-7","The Electroweak Theory",False),
  ("6.8","ch6-8","The Standard Model, and What It Does Not Explain",False),
 ]),
 ("Part VII · Strings and M-Theory", "Where gravity stops being an add-on and starts being unavoidable.", [
  ("7.1","ch7-1","Why Quantum Gravity Is Hard",False),
  ("7.2","ch7-2","The Bosonic String",False),
  ("7.3","ch7-3","Conformal Symmetry and the Virasoro Algebra",True),
  ("7.4","ch7-4","Quantising the String, and D = 26",False),
  ("7.5","ch7-5","The Spectrum",False),
  ("7.6","ch7-6","Superstrings and D = 10",False),
  ("7.7","ch7-7","T-Duality and D-Branes",False),
  ("7.8","ch7-8","Compactification, Dualities, M-Theory",False),
  ("7.9","ch7-9","Black Hole Entropy, Holography, and the Accounting",False),
 ]),
]

FLAT = [(num, slug, title, part[0], m)
        for part in PARTS for (num, slug, title, m) in part[2]]


def shell(title, body, chapter=None, sidebar_head="Contents", home="index.html",
          extra_js="", wide=False, base=""):
    """base: relative prefix to reach build/ root, e.g. '' or '../'"""
    css = open(os.path.join(ASSETS, "book.css")).read()
    js = open(os.path.join(ASSETS, "book.js")).read()
    k = base + "vendor/katex"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — From Newton to M-Theory</title>
<link rel="stylesheet" href="{k}/katex.min.css"
      onerror="this.onerror=null;this.href='{CDN}/katex.min.css'">
<style>
{css}
</style>
<script>
{js}
</script>
<script defer src="{k}/katex.min.js"
        onerror="this.onerror=null;var s=document.createElement('script');s.src='{CDN}/katex.min.js';document.head.appendChild(s)"></script>
<script defer src="{k}/auto-render.min.js"
        onerror="this.onerror=null;var s=document.createElement('script');s.src='{CDN}/contrib/auto-render.min.js';document.head.appendChild(s)"></script>
</head>
<body{f' data-chapter="{chapter}"' if chapter else ''}>
<div class="wrap">
<nav class="sidebar">
  <a class="sb-home" href="{home}">← Newton to M-Theory</a>
  <p class="sb-title">{sidebar_head}</p>
  <div id="sb-toc"></div>
</nav>
<main class="main">
<div class="col{' wide' if wide else ''}">
{body}
</div>
</main>
</div>
{extra_js}
</body>
</html>
"""


def chapnav(i):
    prev_ = FLAT[i - 1] if i > 0 else None
    next_ = FLAT[i + 1] if i < len(FLAT) - 1 else None
    parts = ['<nav class="chapnav">']
    if prev_ and os.path.exists(os.path.join(SRC, prev_[1] + ".html")):
        parts.append(f'<a class="prev" href="{prev_[1]}.html"><span>Previous</span>'
                     f'{prev_[0]} · {html.escape(prev_[2])}</a>')
    else:
        parts.append('<span class="dead"></span>')
    if next_ and os.path.exists(os.path.join(SRC, next_[1] + ".html")):
        parts.append(f'<a class="next" href="{next_[1]}.html"><span>Next</span>'
                     f'{next_[0]} · {html.escape(next_[2])}</a>')
    else:
        parts.append('<span class="dead"></span>')
    parts.append('</nav>')
    return "\n".join(parts)


def build():
    os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
    v_src, v_dst = os.path.join(ROOT, "vendor"), os.path.join(OUT, "vendor")
    if os.path.isdir(v_src):
        shutil.rmtree(v_dst, ignore_errors=True)
        shutil.copytree(v_src, v_dst)
    built = set()

    for i, (num, slug, title, partlabel, _m) in enumerate(FLAT):
        f = os.path.join(SRC, slug + ".html")
        if not os.path.exists(f):
            continue
        raw = open(f).read()
        extra = ""
        m = re.search(r"<!--SCRIPT-->(.*?)<!--/SCRIPT-->", raw, re.S)
        if m:
            extra = "<script>\n" + m.group(1) + "\n</script>"
            raw = raw.replace(m.group(0), "")
        body = raw + "\n" + chapnav(i)
        out = shell(f"{num} {title}", body, chapter=num,
                    sidebar_head=f"Ch {num}", home="../index.html", extra_js=extra,
                    base="../")
        open(os.path.join(OUT, "chapters", slug + ".html"), "w").write(out)
        built.add(slug)

    # ---- index hub ----
    total = len(FLAT)
    done = len(built)
    rows = []
    for label, sub, chs in PARTS:
        rows.append('<section class="part">')
        rows.append(f'<h2 class="part-head">{html.escape(label)}</h2>')
        rows.append(f'<p class="part-sub">{html.escape(sub)}</p>')
        rows.append('<ul class="clist">')
        for num, slug, title, ismath in chs:
            tag = '<span class="tag">math</span>' if ismath else ''
            # The plain-language tag is read out of the chapter file rather than
            # kept in a list here, so it can only ever say what is actually true.
            src_f = os.path.join(ROOT, "src", slug + ".html")
            if os.path.exists(src_f) and "<!--REGISTER:clear-->" in open(src_f, encoding="utf-8").read(1000):
                tag += '<span class="tag clear">clear</span>'
            if slug in built:
                rows.append(f'<li><span class="cnum">{num}</span>'
                            f'<span><a href="chapters/{slug}.html">{html.escape(title)}</a>'
                            f'{tag} <span class="tag ready">ready</span></span></li>')
            else:
                rows.append(f'<li><span class="cnum">{num}</span>'
                            f'<span class="pending">{html.escape(title)}{tag}</span></li>')
        rows.append('</ul></section>')

    body = f"""
<div class="hero">
<p class="eyebrow">A build-it-yourself book</p>
<h1>From Newton to M-Theory</h1>
<p class="subtitle">Special relativity, general relativity, quantum mechanics, quantum field
theory, the Standard Model, and string theory — derived, not asserted.</p>
<p>Every theory in this book is the same three moves: <b>pick a symmetry, write the most general
action invariant under it, quantize</b>. Nothing is stated that hasn't been built. Where a step is
quoted rather than derived, it is marked <b>⚑</b> so you always know what you're standing on.</p>
<p style="color:var(--ink-soft);font-size:.95rem">
<b>{done} of {total}</b> chapters built &nbsp;·&nbsp; 23 of them dedicated math chapters
&nbsp;·&nbsp; <a href="ledger.html">Math Ledger</a></p>
</div>
{''.join(rows)}
"""
    open(os.path.join(OUT, "index.html"), "w").write(
        shell("Contents", body, sidebar_head="Parts", home="index.html", wide=True))

    # ---- through-line ----
    tl = os.path.join(SRC, "_throughline.html")
    if os.path.exists(tl):
        open(os.path.join(OUT, "throughline.html"), "w").write(
            shell("The Through-Line", open(tl).read(), sidebar_head="Through-Line",
                  home="index.html", wide=True))

    # ---- math ledger ----
    led = os.path.join(SRC, "_ledger.html")
    ledger_body = open(led).read() if os.path.exists(led) else "<h1>Math Ledger</h1><p>Coming with the next batch.</p>"
    open(os.path.join(OUT, "ledger.html"), "w").write(
        shell("Math Ledger", ledger_body, sidebar_head="Ledger", home="index.html", wide=True))

    print(f"built {done}/{total} chapters → {OUT}")


if __name__ == "__main__":
    build()
