() => {
  /* Masked-overflow sweep (W0-HARNESS, PDA-09). The page shell (html, body, .wrap, .main,
     .col) is forced to overflow:visible, so a clip on the shell cannot hide an element that
     pokes past the viewport. Reports every topmost element whose right edge passes the
     viewport by more than 1px. An element inside its own scroller (overflow-x auto/scroll),
     inside a component that clips on purpose (overflow hidden/clip below the shell), inside
     position:fixed chrome, or hidden, is not an offender. The same logic is inlined in
     tools/navcheck.py (SWEEP_JS); keep the two together. */
  const vw = document.documentElement.clientWidth || innerWidth;
  const st = document.createElement('style');
  st.textContent = 'html,body,.wrap,.main,.col{overflow:visible!important}';
  document.head.appendChild(st);
  const natural = document.documentElement.scrollWidth;
  const SHELL = new Set([document.documentElement, document.body,
                         ...document.querySelectorAll('.wrap,.main,.col')]);
  const desc = el => {
    const one = e => { let s = e.tagName.toLowerCase(); if (e.id) s += '#' + e.id;
      const c = typeof e.className === 'string' ? e.className.trim() : '';
      if (c) s += '.' + c.split(/\s+/).slice(0, 2).join('.'); return s; };
    return (el.parentElement ? one(el.parentElement) + '>' : '') + one(el);
  };
  const offend = new Set(), out = [];
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect();
    if (r.width === 0 || r.right <= vw + 1) continue;
    const cs = getComputedStyle(e);
    if (cs.position === 'fixed' || cs.visibility !== 'visible' || cs.display === 'none') continue;
    if (e.closest('.katex-mathml')) continue;
    let skip = false;
    for (let a = e.parentElement; a; a = a.parentElement) {
      const acs = getComputedStyle(a);
      if (acs.position === 'fixed') { skip = true; break; }
      const ox = acs.overflowX;
      if (ox === 'auto' || ox === 'scroll') { skip = true; break; }
      if ((ox === 'hidden' || ox === 'clip') && !SHELL.has(a)) { skip = true; break; }
    }
    if (skip) continue;
    offend.add(e);
    if (e.parentElement && offend.has(e.parentElement)) continue;
    out.push({sel: desc(e), right: Math.round(r.right),
              text: (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50)});
  }
  st.remove();
  return {vw: vw, natural: natural, offenders: out};
}
