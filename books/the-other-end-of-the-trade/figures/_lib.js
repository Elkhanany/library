/* ============================================================
   The Other End of the Trade: what every figure shares.

   tools/spx.py puts this once at the head of a chapter's SCRIPT block, before
   the figures on that page, so a figure may call DL.* freely. The numbers are
   the Dealer Mechanics Lab's own (src/lib/math.js, synth.js, indicators.js),
   ported line for line, so a figure computes what the app's widget computed.
   Everything drawn goes through NMT.Plot and takes its colours from the
   theme's roles (DL.color), so a figure follows the light and dark themes
   and redraws when the reader switches.

   Two rules every figure keeps, because the build runs the page and saves
   its column (DESIGN.md section 8):
   - the markup is static. A script writes text into outputs and draws on
     canvases; it never adds or removes elements inside the figure;
   - the first state is fixed. Seeds are constants and nothing animates
     until the reader asks, so two builds of the same source are identical.
   ============================================================ */
var DL = (function () {
  'use strict';

  /* ---------- the normal distribution (Abramowitz and Stegun 26.2.17) ---------- */
  function N(x) {
    var a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741,
        a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
    var sign = x < 0 ? -1 : 1;
    var ax = Math.abs(x) / Math.sqrt(2);
    var t = 1 / (1 + p * ax);
    var y = 1 - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * Math.exp(-ax * ax);
    return 0.5 * (1 + sign * y);
  }
  function phi(x) { return Math.exp(-0.5 * x * x) / Math.sqrt(2 * Math.PI); }

  /* ---------- Black-Scholes-Merton (r = 0.04, q = 0 unless given) ---------- */
  function d1(S, K, T, sigma, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    return (Math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * Math.sqrt(T));
  }
  function d2(S, K, T, sigma, r, q) { return d1(S, K, T, sigma, r, q) - sigma * Math.sqrt(T); }
  function bsPrice(S, K, T, sigma, type, r, q) {
    r = r == null ? 0.04 : r; q = q || 0; type = type || 'call';
    if (T <= 0) return type === 'call' ? Math.max(S - K, 0) : Math.max(K - S, 0);
    var D1 = d1(S, K, T, sigma, r, q), D2 = D1 - sigma * Math.sqrt(T);
    if (type === 'call') return S * Math.exp(-q * T) * N(D1) - K * Math.exp(-r * T) * N(D2);
    return K * Math.exp(-r * T) * N(-D2) - S * Math.exp(-q * T) * N(-D1);
  }
  function bsDelta(S, K, T, sigma, type, r, q) {
    r = r == null ? 0.04 : r; q = q || 0; type = type || 'call';
    if (T <= 0) {
      if (type === 'call') return S > K ? 1 : S < K ? 0 : 0.5;
      return S < K ? -1 : S > K ? 0 : -0.5;
    }
    var D1 = d1(S, K, T, sigma, r, q);
    return type === 'call' ? Math.exp(-q * T) * N(D1) : Math.exp(-q * T) * (N(D1) - 1);
  }
  function bsGamma(S, K, T, sigma, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    if (T <= 1e-6) return S === K ? 1000 : 0;
    var D1 = d1(S, K, T, sigma, r, q);
    return Math.exp(-q * T) * phi(D1) / (S * sigma * Math.sqrt(T));
  }
  function bsVega(S, K, T, sigma, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    if (T <= 0) return 0;
    return S * Math.exp(-q * T) * phi(d1(S, K, T, sigma, r, q)) * Math.sqrt(T);
  }
  function bsTheta(S, K, T, sigma, type, r, q) {
    r = r == null ? 0.04 : r; q = q || 0; type = type || 'call';
    if (T <= 0) return 0;
    var D1 = d1(S, K, T, sigma, r, q), D2 = D1 - sigma * Math.sqrt(T);
    var t1 = -(S * Math.exp(-q * T) * phi(D1) * sigma) / (2 * Math.sqrt(T));
    if (type === 'call') return t1 - r * K * Math.exp(-r * T) * N(D2) + q * S * Math.exp(-q * T) * N(D1);
    return t1 + r * K * Math.exp(-r * T) * N(-D2) - q * S * Math.exp(-q * T) * N(-D1);
  }
  function bsRho(S, K, T, sigma, type, r, q) {
    r = r == null ? 0.04 : r; q = q || 0; type = type || 'call';
    if (T <= 0) return 0;
    var D2 = d2(S, K, T, sigma, r, q);
    return type === 'call' ? K * T * Math.exp(-r * T) * N(D2) : -K * T * Math.exp(-r * T) * N(-D2);
  }
  function bsVanna(S, K, T, sigma, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    if (T <= 0) return 0;
    var D1 = d1(S, K, T, sigma, r, q), D2 = D1 - sigma * Math.sqrt(T);
    return -Math.exp(-q * T) * phi(D1) * (D2 / sigma);
  }
  function bsCharm(S, K, T, sigma, type, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    if (T <= 0) return 0;
    var D1 = d1(S, K, T, sigma, r, q), D2 = D1 - sigma * Math.sqrt(T);
    var term = -phi(D1) * ((2 * (r - q) * T - D2 * sigma * Math.sqrt(T)) / (2 * T * sigma * Math.sqrt(T)));
    return Math.exp(-q * T) * term;
  }
  /* every price and Greek at once, as the app's bsm() */
  function bsm(S, K, T, sigma, r, q) {
    r = r == null ? 0.04 : r; q = q || 0;
    var D1 = d1(S, K, T, sigma, r, q), D2 = D1 - sigma * Math.sqrt(T);
    var Nd1 = N(D1), Nd2 = N(D2), pd1 = phi(D1);
    var eqT = Math.exp(-q * T), erT = Math.exp(-r * T), sT = Math.sqrt(T);
    return {
      d1: D1, d2: D2, Nd1: Nd1, Nd2: Nd2,
      callPrice: S * eqT * Nd1 - K * erT * Nd2,
      putPrice: K * erT * (1 - Nd2) - S * eqT * (1 - Nd1),
      callDelta: eqT * Nd1,
      putDelta: eqT * (Nd1 - 1),
      gamma: T <= 0 ? 0 : eqT * pd1 / (S * sigma * sT),
      vega: S * eqT * pd1 * sT,
      callTheta: -(S * eqT * pd1 * sigma) / (2 * sT) - r * K * erT * Nd2 + q * S * eqT * Nd1,
      putTheta: -(S * eqT * pd1 * sigma) / (2 * sT) + r * K * erT * (1 - Nd2) - q * S * eqT * (1 - Nd1),
      callRho: K * T * erT * Nd2,
      putRho: -K * T * erT * (1 - Nd2),
      vanna: -eqT * pd1 * (D2 / sigma),
      charm: T <= 0 ? 0 : eqT * (-pd1 * ((2 * (r - q) * T - D2 * sigma * sT) / (2 * T * sigma * sT)))
    };
  }

  /* ---------- seeded randomness (Mulberry32, Box-Muller), as the app ---------- */
  function rng(seed) {
    var a = seed >>> 0;
    return function () {
      var t = (a += 0x6d2b79f5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function gauss(r) {
    var u = 1 - r(), v = r();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  /* ---------- synthetic price tapes (src/lib/synth.js) ---------- */
  var REGIMES = [
    { end: 40, drift: 0.0001, vol: 0.008, label: 'Stage 1 · Basing', stage: 1 },
    { end: 110, drift: 0.0030, vol: 0.013, label: 'Stage 2 · Markup', stage: 2 },
    { end: 145, drift: -0.0020, vol: 0.020, label: 'Pullback', stage: 2 },
    { end: 200, drift: 0.0034, vol: 0.014, label: 'Continuation', stage: 2 },
    { end: 240, drift: 0.0001, vol: 0.022, label: 'Stage 3 · Distribution', stage: 3 },
    { end: 295, drift: -0.0030, vol: 0.020, label: 'Stage 4 · Markdown', stage: 4 },
    { end: 350, drift: 0.0008, vol: 0.012, label: 'New Stage 1', stage: 1 }
  ];
  function ohlc(n, seed, regimes, start) {
    n = n || 300; seed = seed == null ? 7 : seed; regimes = regimes || REGIMES; start = start || 100;
    var r = rng(seed), out = [], price = start;
    for (var i = 0; i < n; i++) {
      var g = null;
      for (var k = 0; k < regimes.length; k++) if (i < regimes[k].end) { g = regimes[k]; break; }
      if (!g) g = regimes[regimes.length - 1];
      var ret = g.drift + g.vol * gauss(r);
      var open = price, close = Math.max(0.5, price * (1 + ret));
      var wick = price * g.vol * (0.4 + r() * 0.9);
      var high = Math.max(open, close) + wick * r();
      var low = Math.min(open, close) - wick * r();
      var volume = Math.floor(400000 + r() * 1400000 * (1 + Math.abs(ret) * 25));
      out.push({ i: i, open: open, high: high, low: low, close: close, volume: volume,
                 regime: g.label, stage: g.stage });
      price = close;
    }
    return out;
  }
  function aggregate(data, k) {
    var out = [];
    for (var i = 0; i < data.length; i += k) {
      var ch = data.slice(i, Math.min(i + k, data.length));
      if (!ch.length) break;
      out.push({ i: out.length, open: ch[0].open, close: ch[ch.length - 1].close,
                 high: Math.max.apply(null, ch.map(function (d) { return d.high; })),
                 low: Math.min.apply(null, ch.map(function (d) { return d.low; })),
                 volume: ch.reduce(function (s, d) { return s + d.volume; }, 0) });
    }
    return out;
  }

  /* ---------- indicators (src/lib/indicators.js): arrays aligned to the data ---------- */
  function key(k) { return k || 'close'; }
  function sma(data, n, k) {
    k = key(k);
    return data.map(function (_, i) {
      if (i < n - 1) return null;
      var s = 0;
      for (var j = i - n + 1; j <= i; j++) s += data[j][k];
      return s / n;
    });
  }
  function ema(data, n, k) {
    k = key(k);
    var a = 2 / (n + 1), r = [], prev = data.length ? data[0][k] : 0;
    data.forEach(function (d, i) {
      if (i === 0) r.push(prev);
      else { prev = a * d[k] + (1 - a) * prev; r.push(prev); }
    });
    return r;
  }
  function stdDev(data, n, k) {
    k = key(k);
    return data.map(function (_, i) {
      if (i < n - 1) return null;
      var s = data.slice(i - n + 1, i + 1), m = 0, v = 0;
      s.forEach(function (x) { m += x[k]; }); m /= n;
      s.forEach(function (x) { v += (x[k] - m) * (x[k] - m); });
      return Math.sqrt(v / n);
    });
  }
  function bollinger(data, n, mult) {
    n = n || 20; mult = mult || 2;
    var m = sma(data, n), s = stdDev(data, n);
    return { mid: m,
             upper: m.map(function (v, i) { return v == null ? null : v + mult * s[i]; }),
             lower: m.map(function (v, i) { return v == null ? null : v - mult * s[i]; }) };
  }
  function trueRange(data) {
    return data.map(function (d, i) {
      if (i === 0) return d.high - d.low;
      var pc = data[i - 1].close;
      return Math.max(d.high - d.low, Math.abs(d.high - pc), Math.abs(d.low - pc));
    });
  }
  function atr(data, n) {
    n = n || 14;
    var tr = trueRange(data), r = [], prev = null;
    tr.forEach(function (v, i) {
      if (i < n - 1) { r.push(null); return; }
      if (i === n - 1) {
        var init = tr.slice(0, n).reduce(function (a, b) { return a + b; }, 0) / n;
        r.push(init); prev = init; return;
      }
      prev = (prev * (n - 1) + v) / n;
      r.push(prev);
    });
    return r;
  }
  function donchian(data, n) {
    n = n || 20;
    return data.map(function (_, i) {
      if (i < n - 1) return { upper: null, lower: null, mid: null };
      var s = data.slice(i - n + 1, i + 1);
      var u = Math.max.apply(null, s.map(function (x) { return x.high; }));
      var l = Math.min.apply(null, s.map(function (x) { return x.low; }));
      return { upper: u, lower: l, mid: (u + l) / 2 };
    });
  }
  function rsi(data, n) {
    n = n || 14;
    var r = new Array(data.length).fill(null), g = 0, l = 0, rs;
    for (var i = 1; i < data.length; i++) {
      var c = data[i].close - data[i - 1].close, gain = Math.max(c, 0), loss = Math.max(-c, 0);
      if (i <= n) {
        g += gain / n; l += loss / n;
        if (i === n) { rs = l === 0 ? 100 : g / l; r[i] = 100 - 100 / (1 + rs); }
      } else {
        g = (g * (n - 1) + gain) / n; l = (l * (n - 1) + loss) / n;
        rs = l === 0 ? 100 : g / l; r[i] = 100 - 100 / (1 + rs);
      }
    }
    return r;
  }
  function macd(data, fast, slow, signal) {
    fast = fast || 12; slow = slow || 26; signal = signal || 9;
    var ef = ema(data, fast), es = ema(data, slow);
    var line = ef.map(function (v, i) { return v - es[i]; });
    var sig = ema(line.map(function (v) { return { close: v }; }), signal);
    return { line: line, signal: sig, hist: line.map(function (v, i) { return v - sig[i]; }) };
  }
  function adx(data, n) {
    n = n || 14;
    var tr = trueRange(data), plusDM = [], minusDM = [];
    for (var i = 0; i < data.length; i++) {
      if (i === 0) { plusDM.push(0); minusDM.push(0); continue; }
      var up = data[i].high - data[i - 1].high, dn = data[i - 1].low - data[i].low;
      plusDM.push(up > dn && up > 0 ? up : 0);
      minusDM.push(dn > up && dn > 0 ? dn : 0);
    }
    function wilder(arr) {
      var r = new Array(arr.length).fill(null), prev = null;
      arr.forEach(function (v, i) {
        if (i < n - 1) return;
        if (i === n - 1) { prev = arr.slice(0, n).reduce(function (a, b) { return a + b; }, 0); r[i] = prev; return; }
        prev = prev - prev / n + v; r[i] = prev;
      });
      return r;
    }
    var trS = wilder(tr), pS = wilder(plusDM), mS = wilder(minusDM);
    var plusDI = trS.map(function (v, i) { return v == null || pS[i] == null ? null : 100 * pS[i] / v; });
    var minusDI = trS.map(function (v, i) { return v == null || mS[i] == null ? null : 100 * mS[i] / v; });
    var dx = plusDI.map(function (v, i) {
      return v == null || minusDI[i] == null ? null : 100 * Math.abs(v - minusDI[i]) / ((v + minusDI[i]) || 1);
    });
    var out = new Array(data.length).fill(null), prev = null, count = 0, sum = 0;
    for (var j = 0; j < dx.length; j++) {
      if (dx[j] == null) continue;
      count++;
      if (count <= n) { sum += dx[j]; if (count === n) { prev = sum / n; out[j] = prev; } }
      else { prev = (prev * (n - 1) + dx[j]) / n; out[j] = prev; }
    }
    return { adx: out, plusDI: plusDI, minusDI: minusDI };
  }

  /* ---------- writing numbers ----------
     A true minus sign (U+2212) rather than a hyphen, as the prose writes
     them, and thousands grouped with commas. */
  var MINUS = '−';
  function num(x, d) {
    if (x == null || !isFinite(x)) return '—';
    d = d == null ? 2 : d;
    var s = Math.abs(x).toFixed(d);
    var parts = s.split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    s = parts.join('.');
    return (x < 0 && Number(s.replace(/,/g, '')) !== 0 ? MINUS : '') + s;
  }
  function signed(x, d) {
    if (x == null || !isFinite(x)) return '—';
    var s = num(x, d);
    return x > 0 && Number(Math.abs(x).toFixed(d == null ? 2 : d)) !== 0 ? '+' + s : s;
  }
  function pct(x, d) { return x == null || !isFinite(x) ? '—' : num(x * 100, d == null ? 1 : d) + '%'; }
  function spct(x, d) { return x == null || !isFinite(x) ? '—' : signed(x * 100, d == null ? 1 : d) + '%'; }
  function usd(x, d) {
    if (x == null || !isFinite(x)) return '—';
    var s = num(Math.abs(x), d == null ? 2 : d);
    return (x < 0 && s.replace(/[0.,]/g, '') !== '' ? MINUS : '') + '$' + s;
  }
  function compact(x, d, prefix) {
    if (x == null || !isFinite(x)) return '—';
    prefix = prefix || ''; d = d == null ? 1 : d;
    var a = Math.abs(x), sign = x < 0 ? MINUS : '';
    if (a >= 1e12) return sign + prefix + (a / 1e12).toFixed(d) + 'T';
    if (a >= 1e9) return sign + prefix + (a / 1e9).toFixed(d) + 'B';
    if (a >= 1e6) return sign + prefix + (a / 1e6).toFixed(d) + 'M';
    if (a >= 1e3) return sign + prefix + (a / 1e3).toFixed(d) + 'K';
    return sign + prefix + a.toFixed(d);
  }

  /* ---------- the page: outputs and controls ---------- */
  function $(id) { return document.getElementById(id); }
  /* Text into an element, only when it changes, so the build captures one
     settled state and a redraw does not churn the DOM. */
  function out(id, text) {
    var el = typeof id === 'string' ? $(id) : id;
    if (el && el.textContent !== String(text)) el.textContent = String(text);
  }
  function val(id) { var el = $(id); return el ? parseFloat(el.value) : NaN; }
  function checked(id) { var el = $(id); return !!(el && el.checked); }
  /* Call fn whenever any of these controls moves. */
  function bind(ids, fn) {
    ids.forEach(function (id) {
      var el = $(id);
      if (!el) return;
      el.addEventListener('input', fn);
      el.addEventListener('change', fn);
    });
  }
  /* A row of buttons acting as one choice: each button carries data-v, the one
     chosen has .on and aria-pressed="true". Returns a function giving the
     current value. The first state is whichever button the markup marked
     .on, so the saved page and the live page agree. */
  function seg(id, fn) {
    var box = $(id);
    if (!box) return function () { return null; };
    var bs = [].slice.call(box.querySelectorAll('button[data-v]'));
    function current() {
      for (var i = 0; i < bs.length; i++) if (bs[i].classList.contains('on')) return bs[i].getAttribute('data-v');
      return bs.length ? bs[0].getAttribute('data-v') : null;
    }
    bs.forEach(function (b) {
      b.addEventListener('click', function () {
        bs.forEach(function (o) {
          var on = o === b;
          o.classList.toggle('on', on);
          o.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        if (fn) fn(b.getAttribute('data-v'));
      });
    });
    return current;
  }
  function still() {
    return !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  }
  /* Register a canvas figure. draw(canvas) is called now, on resize and on
     a change of theme (NMT.figure). Returns the redraw. */
  function figure(canvasId, draw) {
    if (!window.NMT) return function () {};
    return NMT.figure(canvasId, draw) || function () {};
  }
  function redraw() { if (window.NMT) NMT.redrawAll(); }

  /* ---------- colour ----------
     A role from the stylesheet, resolved for the current theme: accent,
     familiar, insight, warn, plain, ink, ink-soft, ink-faint, rule, rule-soft,
     paper, bg. The app's amber is the accent here; its cyan and violet are
     familiar, its green insight, its rose plain. */
  function color(role) { return window.NMT ? NMT.css('--' + role) : '#888888'; }
  function fade(c, a) {
    var m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(c || '');
    if (m) return 'rgba(' + parseInt(m[1], 16) + ',' + parseInt(m[2], 16) + ',' + parseInt(m[3], 16) + ',' + a + ')';
    var r = /rgba?\(([^)]+)\)/.exec(c || '');
    if (r) {
      var p = r[1].split(',');
      return 'rgba(' + p[0] + ',' + p[1] + ',' + p[2] + ',' + a + ')';
    }
    return c;
  }

  /* ---------- drawing on an NMT.Plot ---------- */

  /* NMT.Plot's own axes with a format for each axis, and ticks you choose.
       o.x, o.y      a function (value, step) -> label, or false for none
       o.nx, o.ny    how many ticks to aim for (as Plot.axes)
       o.xs, o.ys    the tick values themselves, overriding nx and ny
       o.grid        false for no grid (default: the plot's own setting)
     Paints the ground first, as Plot.axes does, so call it before drawing. */
  function ticks(lo, hi, target) {
    var span = hi - lo, raw = span / (target || 6);
    var mag = Math.pow(10, Math.floor(Math.log10(raw))), norm = raw / mag;
    var step = (norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10) * mag;
    var out = [];
    for (var t = Math.ceil(lo / step) * step; t <= hi + step * 1e-9; t += step)
      out.push(Math.abs(t) < step * 1e-9 ? 0 : t);
    return { vals: out, step: step };
  }
  function axes(p, o) {
    o = o || {};
    var g = p.g, P = p.o;
    var tx = o.xs ? { vals: o.xs, step: o.xs.length > 1 ? Math.abs(o.xs[1] - o.xs[0]) : 1 }
                  : ticks(P.xmin, P.xmax, o.nx || 6);
    var ty = o.ys ? { vals: o.ys, step: o.ys.length > 1 ? Math.abs(o.ys[1] - o.ys[0]) : 1 }
                  : ticks(P.ymin, P.ymax, o.ny || 5);
    function dflt(v, st) { return num(v, Math.min(Math.max(0, -Math.floor(Math.log10(st))), 4)); }
    var fx = o.x === false ? null : (o.x || dflt), fy = o.y === false ? null : (o.y || dflt);
    g.clearRect(0, 0, p.w, p.h);
    g.fillStyle = color('paper'); g.fillRect(0, 0, p.w, p.h);
    if (o.grid == null ? P.grid : o.grid) {
      g.strokeStyle = color('rule-soft'); g.lineWidth = 1;
      tx.vals.forEach(function (v) {
        g.beginPath(); g.moveTo(p.X(v) + .5, p.Y(P.ymin)); g.lineTo(p.X(v) + .5, p.Y(P.ymax)); g.stroke(); });
      ty.vals.forEach(function (v) {
        g.beginPath(); g.moveTo(p.X(P.xmin), p.Y(v) + .5); g.lineTo(p.X(P.xmax), p.Y(v) + .5); g.stroke(); });
    }
    g.strokeStyle = color('rule'); g.lineWidth = 1.4;
    var y0 = (P.ymin <= 0 && P.ymax >= 0) ? 0 : P.ymin;
    var x0 = o.yAt != null ? o.yAt : ((P.xmin <= 0 && P.xmax >= 0) ? 0 : P.xmin);
    g.beginPath(); g.moveTo(p.X(P.xmin), p.Y(y0)); g.lineTo(p.X(P.xmax), p.Y(y0)); g.stroke();
    if (o.yAxis !== false) {
      g.beginPath(); g.moveTo(p.X(x0), p.Y(P.ymin)); g.lineTo(p.X(x0), p.Y(P.ymax)); g.stroke();
    }
    g.fillStyle = color('ink-faint');
    g.font = '11px ' + color('sans');
    if (fx) {
      g.textAlign = 'center'; g.textBaseline = 'top';
      tx.vals.forEach(function (v) { g.fillText(fx(v, tx.step), p.X(v), p.Y(P.ymin) + 6); });
    }
    if (fy) {
      g.textAlign = 'right'; g.textBaseline = 'middle';
      ty.vals.forEach(function (v) { g.fillText(fy(v, ty.step), p.X(P.xmin) - 7, p.Y(v)); });
    }
    if (P.xlabel) {
      g.textAlign = 'right'; g.textBaseline = 'bottom';
      g.fillStyle = color('ink-soft'); g.font = 'italic 12px ' + color('serif');
      g.fillText(P.xlabel, p.w - P.pad.r, p.h - 4);
    }
    if (P.ylabel) {
      g.save(); g.translate(11, P.pad.t); g.rotate(-Math.PI / 2);
      g.textAlign = 'right'; g.textBaseline = 'top';
      g.fillStyle = color('ink-soft'); g.font = 'italic 12px ' + color('serif');
      g.fillText(P.ylabel, 0, 0); g.restore();
    }
    return p;
  }

  function clip(p) {
    var g = p.g, o = p.o;
    g.save();
    g.beginPath();
    g.rect(o.pad.l, o.pad.t, p.w - o.pad.l - o.pad.r, p.h - o.pad.t - o.pad.b);
    g.clip();
  }
  /* Vertical bars from a baseline (o.base, default 0), o.w wide in data units.
     o.color is a colour or a function (value, index) -> colour. */
  function bars(p, xs, ys, o) {
    o = o || {};
    var g = p.g, base = o.base || 0, w = o.w == null ? 0.8 : o.w;
    clip(p);
    for (var i = 0; i < xs.length; i++) {
      if (ys[i] == null || !isFinite(ys[i])) continue;
      var x0 = p.X(xs[i] - w / 2), x1 = p.X(xs[i] + w / 2);
      var y0 = p.Y(base), y1 = p.Y(ys[i]);
      g.fillStyle = typeof o.color === 'function' ? o.color(ys[i], i) : (o.color || color('accent'));
      g.fillRect(Math.min(x0, x1), Math.min(y0, y1), Math.max(1, Math.abs(x1 - x0)), Math.abs(y1 - y0));
    }
    g.restore();
  }
  /* Horizontal bars: ys are positions, xs the lengths from o.base. */
  function hbars(p, ys, xs, o) {
    o = o || {};
    var g = p.g, base = o.base || 0, h = o.h == null ? 0.8 : o.h;
    clip(p);
    for (var i = 0; i < ys.length; i++) {
      if (xs[i] == null || !isFinite(xs[i])) continue;
      var y0 = p.Y(ys[i] - h / 2), y1 = p.Y(ys[i] + h / 2);
      var x0 = p.X(base), x1 = p.X(xs[i]);
      g.fillStyle = typeof o.color === 'function' ? o.color(xs[i], i) : (o.color || color('accent'));
      g.fillRect(Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.max(1, Math.abs(y1 - y0)));
    }
    g.restore();
  }
  /* A filled band between two curves (lo may be a number: the baseline). */
  function band(p, xs, hi, lo, fill) {
    var g = p.g;
    clip(p);
    g.beginPath();
    var started = false;
    for (var i = 0; i < xs.length; i++) {
      if (hi[i] == null) continue;
      if (!started) { g.moveTo(p.X(xs[i]), p.Y(hi[i])); started = true; }
      else g.lineTo(p.X(xs[i]), p.Y(hi[i]));
    }
    for (var j = xs.length - 1; j >= 0; j--) {
      var l = typeof lo === 'number' ? lo : lo[j];
      if (l == null || hi[j] == null) continue;
      g.lineTo(p.X(xs[j]), p.Y(l));
    }
    g.closePath();
    g.fillStyle = fill;
    g.fill();
    g.restore();
  }
  /* A series as a line, skipping nulls (a gap, not a drop to zero). */
  function line(p, xs, ys, o) {
    var pts = [], runs = [];
    for (var i = 0; i < xs.length; i++) {
      if (ys[i] == null || !isFinite(ys[i])) { if (pts.length) runs.push(pts); pts = []; continue; }
      pts.push([xs[i], ys[i]]);
    }
    if (pts.length) runs.push(pts);
    runs.forEach(function (r) { if (r.length > 1) p.path(r, o || {}); });
  }
  function hline(p, y, o) {
    o = o || {};
    p.seg(p.o.xmin, y, p.o.xmax, y, { color: o.color || color('ink-faint'), width: o.width || 1, dash: o.dash });
  }
  function vline(p, x, o) {
    o = o || {};
    p.seg(x, p.o.ymin, x, p.o.ymax, { color: o.color || color('ink-faint'), width: o.width || 1, dash: o.dash });
  }
  /* Candles for OHLC data at x = index. */
  function candles(p, data, o) {
    o = o || {};
    var g = p.g, up = o.up || color('insight'), dn = o.down || color('plain');
    var w = Math.max(1, (p.X(1) - p.X(0)) * 0.6);
    clip(p);
    data.forEach(function (d, i) {
      var x = p.X(o.x ? o.x(d, i) : i), c = d.close >= d.open ? up : dn;
      g.strokeStyle = c; g.fillStyle = c; g.lineWidth = 1;
      g.beginPath(); g.moveTo(x, p.Y(d.high)); g.lineTo(x, p.Y(d.low)); g.stroke();
      var y0 = p.Y(Math.max(d.open, d.close)), y1 = p.Y(Math.min(d.open, d.close));
      g.fillRect(x - w / 2, y0, w, Math.max(1, y1 - y0));
    });
    g.restore();
  }
  /* A small key, top left inside the plot: [{label, color, dash, box}]. */
  function legend(p, items, o) {
    o = o || {};
    var g = p.g, x = p.o.pad.l + 10 + (o.dx || 0), y = p.o.pad.t + 12 + (o.dy || 0);
    g.save();
    g.font = '11px ' + color('sans');
    g.textBaseline = 'middle';
    items.forEach(function (it) {
      g.strokeStyle = it.color; g.fillStyle = it.color; g.lineWidth = 2;
      if (it.box) g.fillRect(x, y - 4, 12, 8);
      else {
        g.setLineDash(it.dash || []);
        g.beginPath(); g.moveTo(x, y); g.lineTo(x + 14, y); g.stroke();
        g.setLineDash([]);
      }
      g.fillStyle = color('ink-soft');
      g.fillText(it.label, x + 19, y);
      x += 19 + g.measureText(it.label).width + 14;
    });
    g.restore();
  }
  /* Tick labels at chosen x positions (a categorical axis): draw the axes with
     p.axes({nx: 0}) or grid off first. */
  function xticks(p, xs, fmt) {
    var g = p.g;
    g.save();
    g.fillStyle = color('ink-faint');
    g.font = '11px ' + color('sans');
    g.textAlign = 'center'; g.textBaseline = 'top';
    xs.forEach(function (x, i) { g.fillText(fmt ? fmt(x, i) : String(x), p.X(x), p.h - p.o.pad.b + 6); });
    g.restore();
  }

  return {
    N: N, phi: phi, d1: d1, d2: d2, bsm: bsm,
    bsPrice: bsPrice, bsDelta: bsDelta, bsGamma: bsGamma, bsVega: bsVega,
    bsTheta: bsTheta, bsRho: bsRho, bsVanna: bsVanna, bsCharm: bsCharm,
    rng: rng, gauss: gauss, ohlc: ohlc, aggregate: aggregate, REGIMES: REGIMES,
    sma: sma, ema: ema, stdDev: stdDev, bollinger: bollinger, trueRange: trueRange,
    atr: atr, donchian: donchian, rsi: rsi, macd: macd, adx: adx,
    MINUS: MINUS, num: num, signed: signed, pct: pct, spct: spct, usd: usd, compact: compact,
    $: $, out: out, val: val, checked: checked, bind: bind, seg: seg, still: still,
    figure: figure, redraw: redraw,
    color: color, fade: fade, clip: clip, axes: axes, ticks: ticks,
    bars: bars, hbars: hbars, band: band, line: line, hline: hline, vline: vline,
    candles: candles, legend: legend, xticks: xticks
  };
})();
