/* ============================================================
   From Newton to M-Theory — shared behaviour
   ============================================================ */

/* ---------- theme ---------- */
(function () {
  var t = 'light';
  try { t = localStorage.getItem('nmt-theme') || 'light'; } catch (e) {}
  document.documentElement.setAttribute('data-theme', t);
  window.addEventListener('DOMContentLoaded', function () {
    var b = document.createElement('button');
    b.id = 'themer';
    b.textContent = t === 'dark' ? 'Light' : 'Dark';
    b.onclick = function () {
      var cur = document.documentElement.getAttribute('data-theme');
      var nxt = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', nxt);
      b.textContent = nxt === 'dark' ? 'Light' : 'Dark';
      try { localStorage.setItem('nmt-theme', nxt); } catch (e) {}
      if (window.NMT && NMT.redrawAll) NMT.redrawAll();
    };
    document.body.appendChild(b);
  });
})();

var NMT = (function () {
  var redraws = [];

  /* ---------- KaTeX ---------- */
  function typeset() {
    if (!window.renderMathInElement) return;
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false,
      strict: false,
      macros: {
        '\\dd': '\\mathrm{d}',
        '\\ee': '\\mathrm{e}',
        '\\ii': '\\mathrm{i}',
        '\\dv': '\\frac{\\mathrm{d}#1}{\\mathrm{d}#2}',
        '\\pdv': '\\frac{\\partial #1}{\\partial #2}',
        '\\abs': '\\left|#1\\right|',
        '\\norm': '\\left\\lVert #1\\right\\rVert',
        '\\ket': '\\left|#1\\right\\rangle',
        '\\bra': '\\left\\langle #1\\right|',
        '\\avg': '\\left\\langle #1\\right\\rangle',
        '\\half': '\\tfrac{1}{2}',
        '\\R': '\\mathbb{R}',
        '\\C': '\\mathbb{C}',
        '\\vv': '\\mathbf{#1}'
      }
    });
  }

  /* ---------- equation numbering + cross-refs ---------- */
  function numberEquations() {
    var chap = document.body.getAttribute('data-chapter') || '';
    var eqs = document.querySelectorAll('.eq');
    var map = {};
    var n = 0;
    eqs.forEach(function (eq) {
      n++;
      var label = chap ? chap + '.' + n : String(n);
      var s = document.createElement('span');
      s.className = 'eqnum';
      s.textContent = '(' + label + ')';
      eq.appendChild(s);
      if (eq.id) map[eq.id] = label;
    });
    document.querySelectorAll('.eqref').forEach(function (a) {
      var id = (a.getAttribute('href') || '').replace('#', '');
      if (map[id]) a.textContent = '(' + map[id] + ')';
      else a.textContent = '(?)';
    });
  }

  /* ---------- sidebar TOC ---------- */
  function buildTOC() {
    var box = document.getElementById('sb-toc');
    if (!box) return;
    var hs = document.querySelectorAll('.main h2, .main h3');
    var made = 0;
    hs.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + i;
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      if (h.tagName === 'H3') a.className = 'lvl3';
      box.appendChild(a);
      made++;
    });
    if (!made) return;
    var links = Array.prototype.slice.call(box.querySelectorAll('a'));
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (l) { l.classList.remove('active'); });
        var m = box.querySelector('a[href="#' + e.target.id + '"]');
        if (m) m.classList.add('active');
      });
    }, { rootMargin: '0px 0px -75% 0px' });
    hs.forEach(function (h) { obs.observe(h); });
  }

  /* ============================================================
     MiniPlot — a small canvas plotting helper.
     No dependencies. Handles retina, theme colours, axes, grid.
     ============================================================ */
  function css(v) {
    return getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  }

  function Plot(canvas, opts) {
    this.c = canvas;
    this.o = Object.assign({
      xmin: -1, xmax: 1, ymin: -1, ymax: 1,
      pad: { l: 46, r: 14, t: 14, b: 34 },
      xlabel: '', ylabel: '', grid: true, equal: false
    }, opts || {});
    this.resize();
  }

  Plot.prototype.resize = function () {
    var c = this.c;
    var w = c.clientWidth || 640;
    var h = parseFloat(c.getAttribute('data-h') || 320);
    var dpr = window.devicePixelRatio || 1;
    c.width = w * dpr; c.height = h * dpr;
    c.style.height = h + 'px';
    this.w = w; this.h = h;
    this.g = c.getContext('2d');
    this.g.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (this.o.equal) {
      var p = this.o.pad;
      var pw = w - p.l - p.r, ph = h - p.t - p.b;
      var sx = pw / (this.o.xmax - this.o.xmin);
      var sy = ph / (this.o.ymax - this.o.ymin);
      var s = Math.min(sx, sy);
      var cx = (this.o.xmin + this.o.xmax) / 2, cy = (this.o.ymin + this.o.ymax) / 2;
      this.o.xmin = cx - pw / (2 * s); this.o.xmax = cx + pw / (2 * s);
      this.o.ymin = cy - ph / (2 * s); this.o.ymax = cy + ph / (2 * s);
    }
  };

  Plot.prototype.X = function (x) {
    var p = this.o.pad;
    return p.l + (x - this.o.xmin) / (this.o.xmax - this.o.xmin) * (this.w - p.l - p.r);
  };
  Plot.prototype.Y = function (y) {
    var p = this.o.pad;
    return this.h - p.b - (y - this.o.ymin) / (this.o.ymax - this.o.ymin) * (this.h - p.t - p.b);
  };
  Plot.prototype.invX = function (px) {
    var p = this.o.pad;
    return this.o.xmin + (px - p.l) / (this.w - p.l - p.r) * (this.o.xmax - this.o.xmin);
  };
  Plot.prototype.invY = function (py) {
    var p = this.o.pad;
    return this.o.ymin + (this.h - p.b - py) / (this.h - p.t - p.b) * (this.o.ymax - this.o.ymin);
  };

  function ticks(lo, hi, target) {
    var span = hi - lo;
    var raw = span / (target || 6);
    var mag = Math.pow(10, Math.floor(Math.log10(raw)));
    var norm = raw / mag;
    var step = (norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10) * mag;
    var out = [], t = Math.ceil(lo / step) * step;
    for (; t <= hi + step * 1e-9; t += step) out.push(Math.abs(t) < step * 1e-9 ? 0 : t);
    return { vals: out, step: step };
  }

  Plot.prototype.axes = function (o) {
    o = o || {};
    var g = this.g, p = this.o;
    g.clearRect(0, 0, this.w, this.h);
    g.fillStyle = css('--paper'); g.fillRect(0, 0, this.w, this.h);
    var tx = ticks(p.xmin, p.xmax, o.nx || 6), ty = ticks(p.ymin, p.ymax, o.ny || 5);
    var fmt = o.fmt || function (v, st) {
      var d = Math.max(0, -Math.floor(Math.log10(st)) );
      return v.toFixed(Math.min(d, 4));
    };
    if (p.grid) {
      g.strokeStyle = css('--rule-soft'); g.lineWidth = 1;
      tx.vals.forEach(function (v) {
        g.beginPath(); g.moveTo(this.X(v) + .5, this.Y(p.ymin)); g.lineTo(this.X(v) + .5, this.Y(p.ymax)); g.stroke();
      }, this);
      ty.vals.forEach(function (v) {
        g.beginPath(); g.moveTo(this.X(p.xmin), this.Y(v) + .5); g.lineTo(this.X(p.xmax), this.Y(v) + .5); g.stroke();
      }, this);
    }
    g.strokeStyle = css('--rule'); g.lineWidth = 1.4;
    var y0 = (p.ymin <= 0 && p.ymax >= 0) ? 0 : p.ymin;
    var x0 = (p.xmin <= 0 && p.xmax >= 0) ? 0 : p.xmin;
    g.beginPath(); g.moveTo(this.X(p.xmin), this.Y(y0)); g.lineTo(this.X(p.xmax), this.Y(y0)); g.stroke();
    g.beginPath(); g.moveTo(this.X(x0), this.Y(p.ymin)); g.lineTo(this.X(x0), this.Y(p.ymax)); g.stroke();

    g.fillStyle = css('--ink-faint');
    g.font = '11px ' + css('--sans');
    g.textAlign = 'center'; g.textBaseline = 'top';
    tx.vals.forEach(function (v) {
      if (Math.abs(v) < tx.step * 1e-9 && p.ymin <= 0 && p.ymax >= 0) return;
      g.fillText(fmt(v, tx.step), this.X(v), this.Y(y0) + 6);
    }, this);
    g.textAlign = 'right'; g.textBaseline = 'middle';
    ty.vals.forEach(function (v) {
      if (Math.abs(v) < ty.step * 1e-9 && p.xmin <= 0 && p.xmax >= 0) return;
      g.fillText(fmt(v, ty.step), this.X(x0) - 7, this.Y(v));
    }, this);
    if (p.xlabel) {
      g.textAlign = 'right'; g.textBaseline = 'bottom';
      g.fillStyle = css('--ink-soft'); g.font = 'italic 12px ' + css('--serif');
      g.fillText(p.xlabel, this.w - p.pad.r, this.h - 4);
    }
    if (p.ylabel) {
      g.save(); g.translate(11, p.pad.t); g.rotate(-Math.PI / 2);
      g.textAlign = 'right'; g.textBaseline = 'top';
      g.fillStyle = css('--ink-soft'); g.font = 'italic 12px ' + css('--serif');
      g.fillText(p.ylabel, 0, 0); g.restore();
    }
    return this;
  };

  Plot.prototype.fn = function (f, o) {
    o = o || {};
    var g = this.g, p = this.o, N = o.N || 700, first = true;
    g.save();
    g.beginPath();
    g.rect(p.pad.l, p.pad.t, this.w - p.pad.l - p.pad.r, this.h - p.pad.t - p.pad.b);
    g.clip();
    g.beginPath();
    for (var i = 0; i <= N; i++) {
      var x = p.xmin + (p.xmax - p.xmin) * i / N;
      var y = f(x);
      if (!isFinite(y)) { first = true; continue; }
      var px = this.X(x), py = this.Y(y);
      if (py < -1e4) py = -1e4; if (py > 1e4) py = 1e4;
      if (first) { g.moveTo(px, py); first = false; } else g.lineTo(px, py);
    }
    g.strokeStyle = o.color || css('--accent');
    g.lineWidth = o.width || 2;
    if (o.dash) g.setLineDash(o.dash);
    g.stroke();
    g.restore();
    return this;
  };

  Plot.prototype.path = function (pts, o) {
    o = o || {};
    var g = this.g;
    g.save();
    g.beginPath();
    g.rect(this.o.pad.l, this.o.pad.t, this.w - this.o.pad.l - this.o.pad.r,
           this.h - this.o.pad.t - this.o.pad.b);
    g.clip();
    g.beginPath();
    for (var i = 0; i < pts.length; i++) {
      var px = this.X(pts[i][0]), py = this.Y(pts[i][1]);
      if (i === 0) g.moveTo(px, py); else g.lineTo(px, py);
    }
    if (o.close) g.closePath();
    if (o.fill) { g.fillStyle = o.fill; g.fill(); }
    if (o.color !== null) {
      g.strokeStyle = o.color || css('--accent');
      g.lineWidth = o.width || 2;
      if (o.dash) g.setLineDash(o.dash);
      g.stroke();
    }
    g.restore();
    return this;
  };

  Plot.prototype.dot = function (x, y, o) {
    o = o || {};
    var g = this.g;
    g.beginPath();
    g.arc(this.X(x), this.Y(y), o.r || 4, 0, 7);
    g.fillStyle = o.color || css('--accent'); g.fill();
    if (o.ring) { g.strokeStyle = css('--paper'); g.lineWidth = 1.8; g.stroke(); }
    return this;
  };

  Plot.prototype.seg = function (x1, y1, x2, y2, o) {
    o = o || {};
    var g = this.g;
    g.save(); g.beginPath();
    g.moveTo(this.X(x1), this.Y(y1)); g.lineTo(this.X(x2), this.Y(y2));
    g.strokeStyle = o.color || css('--ink-faint');
    g.lineWidth = o.width || 1.4;
    if (o.dash) g.setLineDash(o.dash);
    g.stroke(); g.restore();
    return this;
  };

  Plot.prototype.text = function (x, y, s, o) {
    o = o || {};
    var g = this.g;
    g.fillStyle = o.color || css('--ink-soft');
    g.font = (o.font || '12px ' + css('--sans'));
    g.textAlign = o.align || 'left';
    g.textBaseline = o.baseline || 'bottom';
    g.fillText(s, this.X(x) + (o.dx || 0), this.Y(y) + (o.dy || 0));
    return this;
  };

  /* register a figure so it redraws on theme change + resize */
  function figure(canvasId, draw) {
    var c = document.getElementById(canvasId);
    if (!c) return null;
    var run = function () { draw(c); };
    redraws.push(run);
    run();
    var to;
    window.addEventListener('resize', function () {
      clearTimeout(to); to = setTimeout(run, 120);
    });
    return run;
  }

  function redrawAll() { redraws.forEach(function (f) { try { f(); } catch (e) {} }); }

  /* ---------- boot ---------- */
  window.addEventListener('DOMContentLoaded', function () {
    numberEquations();
    buildTOC();
    if (window.katex) { typeset(); }
    else {
      var iv = setInterval(function () {
        if (window.renderMathInElement) { clearInterval(iv); typeset(); redrawAll(); }
      }, 60);
      setTimeout(function () { clearInterval(iv); }, 8000);
    }
  });

  return { Plot: Plot, figure: figure, redrawAll: redrawAll, css: css, typeset: typeset };
})();
