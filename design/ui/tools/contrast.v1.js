() => {
  /* Text-contrast census for prodshot.py --eval "$(cat contrast.js)".
     Every visible element that directly holds text is measured against the background it
     actually sits on (ancestor backgrounds composited, element/ancestor opacity applied).
     Background images and canvases are ignored, so a text over a picture reads as over the
     nearest solid colour. Returns failing groups: ratio < 4.5, or < 3 for large text
     (>= 24px, or >= 18.66px at weight >= 700). */
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; };
  const over = (top, bot) => { const a = top[3]; return [0,1,2].map(i => top[i]*a + bot[i]*(1-a)).concat([1]); };
  const lum = c => { const f = v => { v /= 255; return v <= .03928 ? v/12.92 : Math.pow((v+.055)/1.055, 2.4); };
    return .2126*f(c[0]) + .7152*f(c[1]) + .0722*f(c[2]); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x,y)+.05)/(Math.min(x,y)+.05); };
  function bgOf(el) {
    const stack = [];
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const c = parse(getComputedStyle(e).backgroundColor); if (c && c[3] > 0) { stack.push(c); if (c[3] >= 1) break; }
    }
    let base = [255,255,255,1];
    for (let i = stack.length - 1; i >= 0; i--) base = over(stack[i], base);
    return base;
  }
  function opac(el) { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; }
  const groups = {}; let n = 0;
  document.querySelectorAll('body *').forEach(el => {
    if (['SCRIPT','STYLE','NOSCRIPT','svg','SVG','CANVAS','OPTION'].includes(el.tagName)) return;
    if (el.closest('.katex-mathml,[aria-hidden="true"]')) return;
    const own = [...el.childNodes].some(t => t.nodeType === 3 && t.textContent.trim());
    if (!own) return;
    const cs = getComputedStyle(el); if (cs.visibility !== 'visible' || cs.display === 'none') return;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
    const fg0 = parse(cs.color); if (!fg0) return;
    const bg = bgOf(el); const fg = over([fg0[0], fg0[1], fg0[2], fg0[3] * opac(el)], bg);
    const cr = ratio(fg, bg); n++;
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700;
    const need = (size >= 24 || (size >= 18.66 && bold)) ? 3 : 4.5;
    if (cr + 1e-6 >= need) return;
    const key = el.tagName.toLowerCase() + (el.classList.length ? '.' + [...el.classList].join('.') : '') + ' @' + Math.round(size) + 'px';
    const g = groups[key] || (groups[key] = {n: 0, min: 99, sample: ''});
    g.n++; if (cr < g.min) { g.min = Math.round(cr*100)/100; g.sample = el.textContent.trim().slice(0, 40); }
  });
  const fails = Object.entries(groups).sort((a, b) => b[1].n - a[1].n).map(([k, v]) => ({el: k, n: v.n, min: v.min, sample: v.sample}));
  return {measured: n, failing: fails.reduce((s, f) => s + f.n, 0), groups: fails.slice(0, 25)};
}
