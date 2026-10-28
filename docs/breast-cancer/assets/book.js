/* ============================================================
   From Newton to M-Theory — shared behaviour
   ============================================================ */

/* ---------- theme ----------
   The theme is decided before first paint by the boot script pwa.py puts in
   <head> (DESIGN.md section 4), and the control is the library bar's own
   button, which pwa.js wires. This file used to default to 'light' here and
   overwrite that decision, so an OS-dark reader was switched to light at their
   first chapter (NAV-02, PDA-01). Now it only fills the gaps:

   - With no data-theme at all (no boot script: the Dropbox build) it resolves
     the stored nmt-theme, then the OS setting, and stamps that.
   - At window load, if nothing has wired the bar's button (html.theme-wired
     absent: the Dropbox build, or an installed copy whose shell is older than
     this page), it builds the floating #themer, so no page is ever left
     without a working theme control. Built at load rather than at
     DOMContentLoaded because pwa.js, deferred, has wired the bar by then. */
(function () {
  var root = document.documentElement;
  var KEY = 'library:v1';
  if (root.getAttribute('data-theme') !== 'dark' && root.getAttribute('data-theme') !== 'light') {
    var t = '';
    try { t = localStorage.getItem('nmt-theme') || ''; } catch (e) {}
    if (t !== 'dark' && t !== 'light')
      t = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    root.setAttribute('data-theme', t);
  }
  window.addEventListener('load', function () {
    if (root.classList.contains('theme-wired') || document.getElementById('themer')) return;
    var b = document.createElement('button');
    b.id = 'themer';
    b.type = 'button';
    function paint() {
      var dark = root.getAttribute('data-theme') === 'dark';
      b.textContent = dark ? 'Light' : 'Dark';
      b.title = dark ? 'Switch to light' : 'Switch to dark';
    }
    paint();
    b.onclick = function () {
      var nxt = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', nxt);
      paint();
      /* The press is the reader's choice, under both keys the boot script
         reads, so the next page opens in it whichever shell serves it. The
         figures redraw from the data-theme observer in NMT below. Written
         again after a tick: an older pwa.js answers the attribute change by
         saving its own copy of library:v1, which would put back the look it
         read at load. */
      function remember() {
        try { localStorage.setItem('nmt-theme', nxt); } catch (e) {}
        try {
          var s = JSON.parse(localStorage.getItem(KEY) || '{}') || {};
          s.look = nxt;
          localStorage.setItem(KEY, JSON.stringify(s));
        } catch (e) {}
      }
      remember();
      setTimeout(remember, 0);
    };
    document.body.appendChild(b);
    /* An older nav.css keeps a gutter open in the bar for a toggle that says
       it is there; the current one places it below any bar instead. */
    root.classList.add('has-themer');
  });
})();

var NMT = (function () {
  var redraws = [];

  /* ---------- KaTeX ----------
     A book that writes money sets window.NMT_NO_DOLLAR_MATH on its staged
     page (tools/build.py, book.json "math_delimiters": "brackets"), and its
     maths is then only ever between \( \) and \[ \]: a dollar sign is a price. */
  function typeset() {
    if (!window.renderMathInElement) return;
    var delims = [
      { left: '$$', right: '$$', display: true },
      { left: '\\[', right: '\\]', display: true },
      { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false }
    ];
    if (window.NMT_NO_DOLLAR_MATH) {
      delims = delims.filter(function (d) { return d.left.charAt(0) !== '$'; });
    }
    renderMathInElement(document.body, {
      delimiters: delims,
      throwOnError: false,
      strict: false,
      macros: {
        '\\dd': '\\mathrm{d}',
        '\\ee': '\\mathrm{e}',
        '\\ii': '\\mathrm{i}',
        /* \dv and \pdv take an optional order, as the physics package does, because
           \dv[2]{u}{\varphi} is what anyone writing a second derivative reaches for.
           Without this KaTeX reads "[" as the first argument and renders d[ over d2
           with "]u\varphi" trailing — no error, just a silently wrong equation. Six
           of those sat in Chapter 3.7, one inside its boxed orbit equation. */
        /* \ann{expression}{label} writes the label in small type under a brace,
           so a reader meeting an equation for the first time can see what each
           piece of it is without scrolling back for the symbol. Use it on the
           equation that defines something or states a headline result, and
           nowhere else — an annotation under every display is noise, and the
           device only works while it is rare. */
        '\\ann': '\\underbrace{#1}_{\\;\\text{\\scriptsize #2}\\;}',
        '\\dvn': '\\frac{\\mathrm{d}^{#1}#2}{\\mathrm{d}#3^{#1}}',
        '\\pdvn': '\\frac{\\partial^{#1}#2}{\\partial #3^{#1}}',
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

  /* ---------- sitting breaks ----------
     The authored break is one span: "a natural place to stop · the equation is
     on the table; what follows is ...". It is split at the first separator
     (JavaScript's \s includes the U+00A0 of the authored "&nbsp;·&nbsp;") into
     the kicker, span.k, and the line, span.t, which book.css sets as a label
     between two rules with a wrapping italic line beneath (DESIGN.md section
     6, Callouts, preambles and sitting breaks). Any markup inside the span is
     carried across by a Range, not rebuilt from text. The build saves the
     column, so a break that already has its .k or .t is left alone; one with
     no separator becomes the line alone. */
  function sittingBreaks() {
    [].forEach.call(document.querySelectorAll('.main .pause'), function (p) {
      if (p.querySelector('.k, .t')) return;
      var s = null;
      for (var c = p.firstElementChild; c; c = c.nextElementSibling)
        if (c.tagName === 'SPAN') { s = c; break; }
      if (!s) {
        s = document.createElement('span');
        while (p.firstChild) s.appendChild(p.firstChild);
        p.appendChild(s);
      }
      var w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT, null, false), node = null, m = null;
      while (w.nextNode()) {
        m = /\s*·\s*/.exec(w.currentNode.nodeValue);
        if (m) { node = w.currentNode; break; }
      }
      var t = document.createElement('span');
      t.className = 't';
      if (!node) {
        while (s.firstChild) t.appendChild(s.firstChild);
        p.replaceChild(t, s);
        return;
      }
      var k = document.createElement('span');
      k.className = 'k';
      var r = document.createRange();
      r.setStart(s, 0);
      r.setEnd(node, m.index);
      k.appendChild(r.extractContents());
      /* what is left of the node now starts with the separator */
      node.nodeValue = node.nodeValue.slice(m[0].length);
      while (s.firstChild) t.appendChild(s.firstChild);
      p.insertBefore(k, s);
      p.replaceChild(t, s);
    });
  }

  /* ---------- section headings ---------- */
  /* Both navigations hang off these, and both need the ids to agree with the ones
     the build already wrote into the page, so the numbering is derived the same
     way in every case: position in the h2/h3 sequence. */
  function sectionHeadings() {
    var hs = Array.prototype.slice.call(document.querySelectorAll('.main h2, .main h3'));
    hs.forEach(function (h, i) { if (!h.id) h.id = 'sec-' + i; });
    return hs;
  }

  /* The words a heading is known by in a list or a label: without KaTeX's hidden
     MathML copy, which textContent would otherwise read out a second time. */
  function headingText(h) {
    var c = h.cloneNode(true);
    [].forEach.call(c.querySelectorAll('.katex-mathml, .eqnum'), function (e) {
      if (e.parentNode) e.parentNode.removeChild(e);
    });
    return (c.textContent || '').replace(/\s+/g, ' ').trim();
  }

  /* ---------- sidebar TOC ---------- */
  function buildTOC(hs) {
    var box = document.getElementById('sb-toc');
    if (!box) return;
    /* The built pages ship with this list already rendered — webbuild.py captures
       #sb-toc and writes it into the file — so filling it again in the reader's
       browser would list every section twice. */
    if (!box.children.length) {
      hs.forEach(function (h) {
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        if (h.tagName === 'H3') a.className = 'lvl3';
        box.appendChild(a);
      });
    }
    /* Which entry is active is decided by the spy below, from layout, after
       the boot. Nothing is marked here: the build saves this list. */
  }

  /* ---------- the phone's chrome: folio bar and drawer ---------- */
  /* Below 1000px the sidebar is hidden, which leaves a sixty-thousand-pixel
     chapter with no way through it but the scrollbar. Two things put the
     sidebar's jobs back within reach of a thumb (DESIGN.md section 6):

     - the folio bar, fixed at the foot of the screen: the previous chapter
       ("‹ 67"), the section being read, which opens the drawer, and the next
       chapter ("69 ›"). The arrows carry chapter numbers because they jump
       chapters, not sections.
     - the drawer, a bottom sheet: the way up to the part ("← Part XII · …"),
       the position and the title with a visible Close, the previous and next
       chapters as cards, and the sections.

     Neighbours are read from the chapter foot (.chapnav a.prev and a.next) and
     the way up from the sidebar (.sb-home), both written by the build, so the
     Dropbox build, which has no nav.json, navigates the same way.

     None of this is inside .main .col or #sb-toc, so the build never saves it:
     every reader builds their own, with the handlers attached. The folio sits
     right after the bar, so it is the next thing Tab reaches (PDA-05); the
     sheet and its scrim are appended to <body>.

     A shell older than this file (an installed copy that has not taken the
     update yet) has no folio styles. The shell announces them with
     --lib-folio in nav.css; without it the drawer button is appended to <body>
     as the floating button that shell knows how to draw. */

  /* Glyphs are inline SVG in currentColor, so they survive forced colours
     (PDA-07: the three-bar icon drawn with background:currentColor did not). */
  function glyph(d, size, filled) {
    return '<svg class="g" viewBox="0 0 16 16" width="' + size + '" height="' + size +
      '" aria-hidden="true" focusable="false"><path d="' + d + '" ' +
      (filled ? 'fill="currentColor"' :
        'fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"') +
      '/></svg>';
  }
  var G = {
    prev: glyph('M10 3.5 5.5 8l4.5 4.5', 16),
    next: glyph('M6 3.5 10.5 8 6 12.5', 16),
    up: glyph('M13 8H3.5M7.5 4 3.5 8l4 4', 16),
    close: glyph('M4.5 4.5l7 7M11.5 4.5l-7 7', 16),
    caret: glyph('M4 10.25h8L8 5.5z', 12, true),
    grab: '<svg viewBox="0 0 36 4" width="36" height="4" aria-hidden="true" focusable="false">' +
          '<rect width="36" height="4" rx="2" fill="currentColor"/></svg>'
  };

  /* A neighbour as the chapter foot names it: its href, its number and its
     title. The card's direction label and any part line are set aside, and
     the number is the first "67 · " or "1.2 · " in what is left. */
  function neighbour(dir) {
    var a = document.querySelector('.chapnav a.' + dir);
    if (!a) return null;
    var c = a.cloneNode(true);
    [].forEach.call(c.querySelectorAll('*'), function (e) {
      var s = (e.textContent || '').replace(/\s+/g, ' ').trim();
      if (e.parentNode && (/^[‹←<\s]*(previous|next)( chapter)?[\s›→>]*$/i.test(s) ||
                           /^part\s+[0-9ivxlcdm]+\b/i.test(s)))
        e.parentNode.removeChild(e);
    });
    var t = (c.textContent || '').replace(/\s+/g, ' ').trim();
    var m = t.match(/(\d+(?:\.\d+)*)\s*·\s*/);
    var num = m ? m[1] : '', title = m ? t.slice(m.index + m[0].length).trim() : t;
    if (!m) {
      /* the number in an element of its own, with no separator after it */
      var parts = [], w = document.createTreeWalker(c, NodeFilter.SHOW_TEXT, null, false);
      while (w.nextNode()) parts.push(w.currentNode.nodeValue);
      var m2 = parts.join(' ').replace(/\s+/g, ' ').trim().match(/^(\d+(?:\.\d+)*)\s+(.+)$/);
      if (m2) { num = m2[1]; title = m2[2]; }
    }
    return { href: a.getAttribute('href'), num: num, title: title,
             label: num ? num + ' · ' + title : title };
  }

  var mnav = null;          /* the drawer's controls, once built */

  function buildMobileNav(hs) {
    if (document.getElementById('mnav')) return;
    if (!document.querySelector('.main')) return;
    var h2s = hs.filter(function (h) { return h.tagName === 'H2'; });
    /* Two reasons to build the drawer and they are separate. A chapter with
       several sections needs the list, to jump between them. A chapter in a
       book's reading sequence needs the way up, the position and the
       neighbours, however few sections it has. The sidebar title is what
       marks a page as sitting in such a sequence: a standalone page such as
       the trial registry carries none and builds no drawer. */
    var sbTitle = document.querySelector('.sb-title');
    if (h2s.length < 2 && !sbTitle) return;

    var body = document.body, root = document.documentElement;
    var modern = !!getComputedStyle(root).getPropertyValue('--lib-folio').trim();
    var contents = !!document.querySelector('.main h2.part-head');
    var idle = contents ? 'Parts' : 'Sections';
    var foot = document.querySelector('.chapnav');

    var btn = document.createElement('button');
    btn.id = 'mnav-btn';
    btn.type = 'button';
    btn.setAttribute('aria-controls', 'mnav');
    btn.setAttribute('aria-expanded', 'false');
    if (modern) {
      btn.innerHTML = '<span class="folio-sec"></span>' + G.caret;
      btn.firstChild.textContent = idle;
      btn.setAttribute('aria-label', idle);
    } else {
      btn.setAttribute('aria-label', 'Sections in this chapter');
      btn.innerHTML = '<span id="mnav-ico"><i></i><i></i><i></i></span>';
    }

    var scrim = document.createElement('div');
    scrim.id = 'mnav-scrim';

    var panel = document.createElement('nav');
    panel.id = 'mnav';
    panel.tabIndex = -1;
    panel.setAttribute('aria-label', contents ? 'Parts' : 'Sections and chapters');
    panel.setAttribute('aria-hidden', 'true');
    if (modern) panel.innerHTML = '<span class="mn-grab" aria-hidden="true">' + G.grab + '</span>';

    /* 1. The way up: the sidebar's own up-link, at least 48px tall. */
    var home = document.querySelector('.sidebar .sb-home');
    if (home) {
      var up = document.createElement('a');
      up.className = 'mn-up';
      up.setAttribute('href', home.getAttribute('href') || 'contents.html');
      up.innerHTML = G.up + '<span></span>';
      up.lastChild.textContent = (home.textContent || '').replace(/^[\s←‹<]+/, '')
                                                          .replace(/\s+/g, ' ').trim();
      panel.appendChild(up);
    }

    /* 2. The head: the position (the sidebar's title, written at build), the
       title, and a Close a reader can see. */
    var h1 = document.querySelector('.main h1');
    var head = document.createElement('div');
    head.className = 'mn-head';
    head.innerHTML = '<div class="mn-hd"><p class="mn-kicker"></p><p class="mn-title"></p></div>' +
                     '<button class="mn-close" type="button">' + G.close + '<span>Close</span></button>';
    head.querySelector('.mn-kicker').textContent =
      sbTitle ? sbTitle.textContent.replace(/\s+/g, ' ').trim() : idle;
    head.querySelector('.mn-title').textContent = h1 ? headingText(h1) : document.title;
    panel.appendChild(head);

    /* 3. The neighbours, as cards. A missing one keeps its slot as a span, so
       the first and last chapters have the same shape as every other. */
    if (foot) {
      var row = document.createElement('div');
      row.className = 'mn-seq';
      [['prev', 'Previous', 'No previous chapter'], ['next', 'Next', 'No next chapter']]
        .forEach(function (s) {
          var n = neighbour(s[0]);
          var el = document.createElement(n ? 'a' : 'span');
          el.className = s[0];
          if (n) el.setAttribute('href', n.href);
          el.innerHTML = '<span class="mn-dir">' + (s[0] === 'prev' ? G.prev : '') + '<span></span>' +
                         (s[0] === 'next' ? G.next : '') + '</span><span class="mn-ch"></span>';
          el.querySelector('.mn-dir span').textContent = s[1];
          el.querySelector('.mn-ch').textContent = n ? n.label : s[2];
          row.appendChild(el);
        });
      panel.appendChild(row);
    }

    /* 4. The sections. */
    var list = document.createElement('div');
    list.className = 'mn-list';
    h2s.forEach(function (h) {
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = headingText(h);
      list.appendChild(a);
    });
    panel.appendChild(list);

    /* The folio bar: 44px arrows built from the chapter foot, with the drawer
       button between them. A missing neighbour keeps its slot, so the centre
       never moves; a page with no chapter foot (contents, ledger) has empty
       slots. */
    function arrow(dir) {
      var n = foot ? neighbour(dir) : null, el;
      if (n) {
        el = document.createElement('a');
        el.setAttribute('href', n.href);
        el.setAttribute('aria-label', (dir === 'prev' ? 'Previous' : 'Next') + ' chapter: ' + n.label);
        el.innerHTML = dir === 'prev' ? G.prev + '<span></span>' : '<span></span>' + G.next;
        el.querySelector('span').textContent = n.num;
      } else {
        el = document.createElement('span');
        el.setAttribute('aria-hidden', 'true');
        if (foot) el.innerHTML = dir === 'prev' ? G.prev : G.next;
      }
      el.className = 'folio-' + dir + (n ? '' : ' folio-off');
      return el;
    }

    if (modern) {
      var folio = document.createElement('nav');
      folio.className = 'folio';
      folio.setAttribute('aria-label', contents ? 'Parts' : 'Chapter');
      folio.appendChild(arrow('prev'));
      folio.appendChild(btn);
      folio.appendChild(arrow('next'));
      var bar = document.querySelector('.topnav');
      if (bar && bar.parentNode) bar.parentNode.insertBefore(folio, bar.nextSibling);
      else body.insertBefore(folio, body.firstChild);
      root.classList.add('has-folio');
      body.appendChild(scrim);
      body.appendChild(panel);
    } else {
      body.appendChild(scrim);
      body.appendChild(panel);
      body.appendChild(btn);
    }

    function isOpen() { return panel.classList.contains('open'); }
    function setOpen(on, refocus) {
      btn.classList.toggle('open', on);
      panel.classList.toggle('open', on);
      scrim.classList.toggle('open', on);
      root.classList.toggle('mnav-open', on);
      btn.setAttribute('aria-expanded', on ? 'true' : 'false');
      panel.setAttribute('aria-hidden', on ? 'false' : 'true');
      if (!modern) btn.setAttribute('aria-label', on ? 'Close sections' : 'Sections in this chapter');
      if (on) {
        chromeShow();
        spyNow(true);
        keepInView(list.querySelector('a.active'), list);
        panel.focus({ preventScroll: true });
      } else if (refocus) {
        btn.focus({ preventScroll: true });
      }
    }

    btn.addEventListener('click', function () { setOpen(!isOpen(), true); });
    scrim.addEventListener('click', function () { setOpen(false, true); });
    head.querySelector('.mn-close').addEventListener('click', function () { setOpen(false, true); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) setOpen(false, true);
    });
    window.addEventListener('resize', function () {
      if (isOpen() && window.innerWidth > 1000) setOpen(false, false);
    });

    /* Tab stays inside the open sheet: behind it is a page under a scrim. */
    panel.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !isOpen()) return;
      var f = [].filter.call(panel.querySelectorAll('a[href], button'), function (x) {
        return x.getClientRects().length > 0;
      });
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1], at = document.activeElement;
      if (e.shiftKey && (at === first || at === panel)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && (at === last || at === panel)) { e.preventDefault(); first.focus(); }
    });

    /* The handle is real: dragging the head of the sheet down closes it. */
    dragToClose(panel, function (t) {
      return !!(t && t.closest && t.closest('.mn-grab, .mn-up, .mn-head'));
    }, function () { setOpen(false, true); });

    [].forEach.call(list.querySelectorAll('a'), function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var id = a.getAttribute('href').slice(1);
        var t = document.getElementById(id);
        setOpen(false, false);
        if (!t) return;
        jumping();
        t.scrollIntoView({ behavior: still() ? 'auto' : 'smooth', block: 'start' });
        /* replace rather than push: tapping a section is a scroll, not a
           navigation, and it should not take over the back button. */
        if (history.replaceState) history.replaceState(null, '', '#' + id);
        /* From the keyboard, the reader continues from the heading. */
        if (e.detail === 0) {
          if (!t.hasAttribute('tabindex')) t.setAttribute('tabindex', '-1');
          t.focus({ preventScroll: true });
        }
      });
    });

    mnav = { btn: btn, panel: panel, list: list, idle: idle,
             label: modern ? btn.querySelector('.folio-sec') : null };
    SPY = null;             /* collect again, with the drawer's list */
  }

  /* ---------- dragging a sheet closed ----------
     The drawer and the reference sheet both draw a handle. Dragging the head
     of either down more than 64px closes it; less, and it springs back. Pointer
     capture starts only once the drag has begun, so a tap on a link or on
     Close in the head is still a tap. The head's touch-action is none (nav.css),
     so the browser does not take the gesture for a scroll. */
  function dragToClose(sheet, isHead, close) {
    var y0 = null, pid = null, dy = 0, live = false;
    sheet.addEventListener('pointerdown', function (e) {
      if (e.button !== 0 || !isHead(e.target)) return;
      y0 = e.clientY; pid = e.pointerId; dy = 0; live = false;
    });
    sheet.addEventListener('pointermove', function (e) {
      if (y0 === null || e.pointerId !== pid) return;
      dy = e.clientY - y0;
      if (!live) {
        if (dy < -12) { y0 = null; return; }        /* a drag up is not a close */
        if (dy < 6) return;
        live = true;
        try { sheet.setPointerCapture(pid); } catch (x) { /* already released */ }
        sheet.classList.add('dragging');
        sheet.style.transition = 'none';
      }
      sheet.style.transform = 'translateY(' + Math.max(0, dy) + 'px)';
      e.preventDefault();
    });
    function end(e) {
      if (y0 === null || e.pointerId !== pid) return;
      var was = live, far = live && dy > 64 && e.type === 'pointerup';
      y0 = null; pid = null; live = false;
      if (!was) return;
      sheet.classList.remove('dragging');
      sheet.style.transition = '';
      sheet.style.transform = '';
      /* a drag that ends over a link is not a click on it */
      var swallow = function (ev) { ev.preventDefault(); ev.stopPropagation(); };
      sheet.addEventListener('click', swallow, true);
      setTimeout(function () { sheet.removeEventListener('click', swallow, true); }, 0);
      if (far) close();
    }
    sheet.addEventListener('pointerup', end);
    sheet.addEventListener('pointercancel', end);
  }

  /* ---------- find a chapter (contents pages) ----------
     One search box after the contents head's count line. It filters the rows
     by number and title as the reader types, hides a part with no match, says
     so when nothing matches, and clears on Escape. It is built from the page
     itself, so it works offline and in the Dropbox build. The build saves
     .main .col, so the box and its status line are inserted only if they are
     not there already, and the wiring (a property, not an attribute) is never
     saved. */
  function norm(s) {
    s = String(s || '').toLowerCase();
    if (s.normalize) s = s.normalize('NFD').replace(/[̀-ͯ]/g, '');
    return s.replace(/[·•,;:()\[\]"“”‘’']/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function findChapter() {
    var col = document.querySelector('.main .col');
    if (!col) return;
    var rows = col.querySelectorAll('.clist li');
    if (!rows.length) return;

    var input = col.querySelector('input.toc-find');
    if (!input) {
      input = document.createElement('input');
      input.type = 'search';
      input.className = 'toc-find';
      input.placeholder = 'Find a chapter';
      input.setAttribute('aria-label', 'Find a chapter');
      input.setAttribute('autocomplete', 'off');
      input.setAttribute('spellcheck', 'false');
      input.setAttribute('enterkeyhint', 'search');
      var head = col.querySelector('.toc-head');
      var count = head && head.querySelector('.toc-count');
      if (head && !count) {
        [].some.call(head.querySelectorAll('p, div, span'), function (e) {
          var t = e.textContent || '';
          if (/\d/.test(t) && /\bchapters?\b/i.test(t) && !e.querySelector('p, div')) { count = e; return true; }
          return false;
        });
      }
      if (count) count.parentNode.insertBefore(input, count.nextSibling);
      else if (head) head.appendChild(input);
      else {
        var first = col.querySelector('h2.part-head, .clist');
        while (first && first.parentElement !== col &&
               first.parentElement.firstElementChild === first) first = first.parentElement;
        if (!first || !first.parentNode) return;
        first.parentNode.insertBefore(input, first);
      }
    }
    var note = input.parentNode.querySelector('.toc-none');
    if (!note) {
      note = document.createElement('p');
      note.className = 'toc-none';
      note.setAttribute('role', 'status');
      note.setAttribute('aria-live', 'polite');
      input.parentNode.insertBefore(note, input.nextSibling);
    }
    if (input._wired) return;
    input._wired = true;

    var items = [].map.call(rows, function (li) {
      var c = li.cloneNode(true);
      [].forEach.call(c.querySelectorAll('.tag, .katex-mathml'), function (e) {
        if (e.parentNode) e.parentNode.removeChild(e);
      });
      var n = li.querySelector('.cnum');
      return { li: li, num: n ? n.textContent.trim() : '', text: norm(c.textContent), ok: true };
    });

    /* A part is its head and what follows it up to the next part: the wrapper
       that holds exactly one part head, or else the head and its siblings. */
    var parts = [].map.call(col.querySelectorAll('h2.part-head'), function (h) {
      var els = [];
      var w = h.parentElement;
      if (w && w !== col && w.querySelectorAll('h2.part-head').length === 1) els = [w];
      else {
        els = [h];
        for (var s = h.nextElementSibling; s && !(s.matches && s.matches('h2.part-head')); s = s.nextElementSibling)
          els.push(s);
      }
      var mine = items.filter(function (it) {
        return els.some(function (e) { return e.contains(it.li); });
      });
      return { els: els, items: mine };
    });

    function show(e, on) { e.style.display = on ? '' : 'none'; }
    function run() {
      var q = norm(input.value);
      var words = q ? q.split(' ') : [];
      var numeric = /^\d+(\.\d*)?$/.test(q);
      var shown = 0;
      items.forEach(function (it) {
        it.ok = !q || (numeric ? it.num.indexOf(q) === 0
                               : words.every(function (w) { return it.text.indexOf(w) >= 0; }));
        show(it.li, it.ok);
        if (it.ok) shown++;
      });
      parts.forEach(function (p) {
        if (!p.items.length) return;
        var any = p.items.some(function (it) { return it.ok; });
        p.els.forEach(function (e) { show(e, any); });
      });
      var msg = q && !shown ? 'No chapter matches' : '';
      if (note.textContent !== msg) note.textContent = msg;
    }
    input.addEventListener('input', run);
    input.addEventListener('search', run);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && input.value) {
        e.preventDefault();
        input.value = '';
        run();
      }
    });
    if (input.value) run();
  }

  /* ============================================================
     MiniPlot — a small canvas plotting helper.
     No dependencies. Handles retina, theme colours, axes, grid.
     ============================================================ */
  /* A colour role, resolved to something a canvas and a string test can both
     use. getPropertyValue() returns a derived role as unresolved color-mix()
     text, and a computed colour serialises as color(srgb ...); the chapter
     figures test for '#' and parse hex. So color() sets var(--x) on a probe,
     paints the probe's computed colour into a 1x1 canvas and reads the pixel
     back as #rrggbb (rgba() if it is translucent), cached per theme (DESIGN.md
     section 3). pwa.js has its own copy for theme-color. */
  var probe = null, pctx = null, cache = {};
  function color(name) {
    var root = document.documentElement;
    var key = (root.getAttribute('data-theme') || '') + '|' + name;
    if (cache[key] !== undefined) return cache[key];
    var out = '';
    try {
      if (getComputedStyle(root).getPropertyValue(name).trim()) {
        var host = document.body || root;
        if (!probe) {
          probe = document.createElement('i');
          probe.setAttribute('aria-hidden', 'true');
          probe.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden;' +
                                'visibility:hidden;pointer-events:none';
        }
        if (probe.parentNode !== host) host.appendChild(probe);
        probe.style.color = 'var(' + name + ')';
        var c = getComputedStyle(probe).color;
        if (!pctx) {
          var cv = document.createElement('canvas');
          cv.width = cv.height = 1;
          pctx = cv.getContext('2d', { willReadFrequently: true });
        }
        pctx.clearRect(0, 0, 1, 1);
        pctx.fillStyle = '#010203';
        pctx.fillStyle = c;
        if (pctx.fillStyle !== '#010203') {
          pctx.fillRect(0, 0, 1, 1);
          var d = pctx.getImageData(0, 0, 1, 1).data;
          out = d[3] < 255
            ? 'rgba(' + d[0] + ',' + d[1] + ',' + d[2] + ',' + (d[3] / 255).toFixed(3) + ')'
            : '#' + [d[0], d[1], d[2]].map(function (v) {
                return (v < 16 ? '0' : '') + v.toString(16); }).join('');
        }
      }
    } catch (e) { out = ''; }
    /* only a real answer is kept: before the stylesheet arrives there is none */
    if (out) cache[key] = out;
    return out;
  }

  /* What MiniPlot and the chapter figures ask for. A font role (--sans,
     --serif, --mono) comes back as written; a colour role comes back resolved,
     so a figure keeps working when its colour is derived rather than typed. */
  function css(v) {
    var raw = getComputedStyle(document.documentElement).getPropertyValue(v).trim();
    if (!raw || /^--(lib-)?(sans|serif|mono)$|^--f-/.test(v)) return raw;
    return color(v) || raw;
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

  /* Every figure redraws when the theme changes, whoever changed it: the bar's
     button announces it with a library:theme event, and anything else (the
     floating toggle, a test, an older shell) at least changes the attribute.
     Both paths meet in one frame, so a press redraws once. Registered here,
     outside the boot handler, so the build's runtime_js() leaves it alone. */
  var redrawQueued = false;
  function redrawSoon() {
    if (redrawQueued) return;
    redrawQueued = true;
    (window.requestAnimationFrame || setTimeout)(function () {
      redrawQueued = false;
      redrawAll();
    });
  }
  window.addEventListener('library:theme', redrawSoon);
  if (window.MutationObserver) {
    new MutationObserver(redrawSoon).observe(document.documentElement,
      { attributes: true, attributeFilter: ['data-theme'] });
  }

  /* An animated figure writes live values into its readouts, and the build saves
     the finished DOM to disk — so whatever the animation happened to reach in the
     moment before the snapshot gets baked into the file. That made ch0-8 differ
     between two builds of identical source, which is why it turned up in every
     batch. A figure that animates registers a reset here; the build calls it
     before saving, so the file on disk always shows the t = 0 state. */
  var snapshots = [];
  function onSnapshot(f) { snapshots.push(f); }
  function resetForSnapshot() {
    snapshots.forEach(function (f) { try { f(); } catch (e) {} });
    redrawAll();
  }

  /* ---------- the clinical apparatus ----------
     DESIGN.md section 6 (Cards, Evidence tables, References). Everything here
     runs at build time too, on the staged file:// page whose .main .col the
     build then saves, so every change it makes inside the column is
     idempotent (it checks before it writes) and leaves no state class behind:
     a title moves to data-facts once; tab stops are recomputed, not added to;
     the scroll cue's class is cleared before the save (onSnapshot); chips
     become links only off file:, so the saved page and the Dropbox build keep
     them as spans. */
  function onFile() { return location.protocol === 'file:'; }

  /* A trial's row in the registry. Not under file:, where there is none. */
  function registryHref(key) { return 'trials.html#t-' + encodeURIComponent(key); }

  /* The marks that have a card: trials named in the column (in prose, in
     tables and as chips) and defined terms. Their facts move from the title
     attribute, which the browser would show as a second, unstyled tooltip,
     to data-facts. Chips become links to the registry. Then the first mark of
     each trial or term in each h2 section becomes a tab stop, and the rest
     are pointer-only, so a chapter with 134 trial marks does not add 134 tab
     stops. */
  function marks() {
    var col = document.querySelector('.main .col');
    if (!col) return [];
    var list = [].slice.call(col.querySelectorAll('.trial[data-trial], .gloss'));
    list.forEach(function (el) {
      if (!el.hasAttribute('title')) return;
      if (!el.hasAttribute('data-facts')) el.setAttribute('data-facts', el.getAttribute('title'));
      el.removeAttribute('title');
    });
    if (!onFile()) {
      list = list.map(function (el) {
        if (el.tagName === 'A' || !el.classList.contains('chip')) return el;
        var a = document.createElement('a');
        [].forEach.call(el.attributes, function (at) {
          if (at.name !== 'tabindex' && at.name !== 'role') a.setAttribute(at.name, at.value);
        });
        a.setAttribute('href', registryHref(el.getAttribute('data-trial')));
        while (el.firstChild) a.appendChild(el.firstChild);
        el.parentNode.replaceChild(a, el);
        return a;
      });
    }
    var seen = {};
    [].forEach.call(col.querySelectorAll('h2, .trial[data-trial], .gloss'), function (el) {
      if (el.tagName === 'H2') { seen = {}; return; }
      var key = el.hasAttribute('data-trial') ? 't:' + el.getAttribute('data-trial')
              : 'g:' + (el.textContent || '').replace(/\s+/g, ' ').trim().toLowerCase();
      var first = !seen[key];
      seen[key] = true;
      if (el.tagName === 'A') {
        if (first) el.removeAttribute('tabindex');
        else el.setAttribute('tabindex', '-1');
      } else if (first) {
        el.setAttribute('tabindex', '0');
        el.setAttribute('role', 'button');
      } else {
        el.removeAttribute('tabindex');
        el.removeAttribute('role');
      }
    });
    return list;
  }

  /* ---------- the references list ----------
     Collapsed under "All N references" (R-07). Opened for a #references or
     #r- address, on load and on hashchange; before a clicked citation jumps
     (refCards); and for printing, restored afterwards. The card and the
     sheet read entries out of it open or closed. */
  function refsBox() { return document.querySelector('.main details.refs-list'); }
  function openRefs() {
    var d = refsBox();
    if (d && !d.open) d.open = true;
    return d;
  }
  function refsList() {
    var d = refsBox();
    if (!d || d._wired) return;
    d._wired = true;
    function target() {
      var h = '';
      try { h = decodeURIComponent(location.hash.slice(1)); } catch (e) { h = location.hash.slice(1); }
      return h === 'references' || h.indexOf('r-') === 0 ? h : '';
    }
    /* The browser may have tried to scroll to an entry inside the closed
       list and found nothing to scroll to; once it is open, bring the entry
       to the top unless it is already in view. */
    function land(h) {
      var t = h && document.getElementById(h);
      if (!t) return;
      var r = t.getBoundingClientRect();
      if (r.top >= 0 && r.bottom <= window.innerHeight) return;
      t.scrollIntoView({ block: 'start' });
    }
    function check(scroll) {
      var h = target();
      if (!h) return;
      openRefs();
      if (scroll) land(h);
    }
    check(false);
    window.addEventListener('load', function () { check(true); });
    window.addEventListener('hashchange', function () { check(true); });
    var was = null;
    window.addEventListener('beforeprint', function () {
      if (was === null) was = d.open;
      d.open = true;
    });
    window.addEventListener('afterprint', function () {
      if (was !== null) d.open = was;
      was = null;
    });
  }

  /* ---------- evidence tables: the scroll cue ----------
     "→ more columns" (generated content, book.css) shows while the table is
     wider than its box and not scrolled to its right end. The class is state,
     so the build clears it before saving the page. */
  function evidenceCues() {
    var evs = [].slice.call(document.querySelectorAll('.main .evidence'));
    if (!evs.length) return;
    function box(ev) { return ev.querySelector('.ev-scroll') || ev; }
    function update(ev) {
      var s = box(ev);
      var more = s.scrollWidth > s.clientWidth + 1 &&
                 s.scrollLeft + s.clientWidth < s.scrollWidth - 2;
      if (ev.classList.contains('more') !== more) ev.classList.toggle('more', more);
    }
    function all() { evs.forEach(update); }
    var queued = false;
    function soon() {
      if (queued) return;
      queued = true;
      (window.requestAnimationFrame || setTimeout)(function () { queued = false; all(); });
    }
    evs.forEach(function (ev) {
      var s = box(ev);
      if (s._cue) return;
      s._cue = true;
      s.addEventListener('scroll', function () { update(ev); }, { passive: true });
      if (window.ResizeObserver) new ResizeObserver(soon).observe(s);
    });
    all();
    window.addEventListener('resize', soon);
    window.addEventListener('load', soon);
    onSnapshot(function () { evs.forEach(function (ev) { ev.classList.remove('more'); }); });
  }

  /* ---------- display maths: fit, scroll, hang, number ----------
     DESIGN.md section 6, Equations and figures. For each display in the
     column, measured on the reader's own page:
     - it fits: nothing is done;
     - it overflows its box by a little: its font-size is set so that it fits,
       down to a floor of .9em;
     - it overflows by more: it keeps its size and scrolls inside its box, and
       .scrolls paints the edge shades (book.css);
     - except that from 1200px an unnumbered display that the margin track can
       hold hangs into it at full size, and the panel it sits in (a worked
       example, say) grows to the right to hold it while the panel's prose
       keeps the measure.
     Then each equation's number stays on the display's line if the centred
     display leaves room for it, and drops below it (.eq-drop) if not. From
     1200px, where the margin track is wide enough to hold it (book.css
     decides, by a container query on .main), the number is in the track and
     never collides; where the track is too narrow, as it is with a large
     default text size, the same rule decides as below 1200px.

     Layout is read in batches, all resets first, so a chapter of a hundred
     displays costs a handful of layouts rather than hundreds. The whole pass is
     recomputed on DOMContentLoaded, when the fonts are ready, on load, on a
     change of width and when a <details> opens, so a size the build captured
     would be harmless; the build's snapshot clears it anyway (onSnapshot), and
     no state is saved into the page. Registered outside the boot handler
     (DESIGN.md section 8), since it needs rendered maths and layout. */
  var FIT_FLOOR = 0.9, NUM_GAP = 12, HANG_GAP = 16;
  var fitted = { ds: [], eqs: [], panels: [] };

  /* The rendered maths' left and right, whatever its box does: the union of
     KaTeX's top-level pieces, which are laid out on one line. */
  function mathExtent(d) {
    var L = Infinity, R = -Infinity, bs = d.querySelectorAll('.katex-html > .base');
    for (var i = 0; i < bs.length; i++) {
      var r = bs[i].getBoundingClientRect();
      if (r.width) { if (r.left < L) L = r.left; if (r.right > R) R = r.right; }
    }
    return R > L ? { L: L, R: R, w: R - L } : null;
  }

  function tidy(el) { if (!el.getAttribute('style')) el.removeAttribute('style'); }

  /* The numbered equation an a.eqref points at on this page, or null. */
  function eqTarget(a) {
    var h = a.getAttribute('href') || '', id = '';
    if (h.charAt(0) !== '#') return null;
    try { id = decodeURIComponent(h.slice(1)); } catch (e) { id = h.slice(1); }
    var el = id && document.getElementById(id);
    return el && el.classList.contains('eq') ? el : null;
  }

  function unfit() {
    fitted.ds.forEach(function (d) {
      d.style.fontSize = ''; d.style.marginRight = '';
      d.classList.remove('scrolls');
      tidy(d);
    });
    fitted.panels.forEach(function (p) {
      p.style.marginRight = ''; p.style.paddingRight = '';
      p._hang = 0;
      tidy(p);
    });
    fitted.eqs.forEach(function (e) { e.classList.remove('eq-drop'); });
    fitted = { ds: [], eqs: [], panels: [] };
  }

  /* Fit a set of displays. hang: allow the margin track (the column only). */
  /* How far the maths runs past its box: the wider of its drawn extent and
     what the box would scroll by (a boxed or braced display can scroll a
     pixel or two further than its ink). */
  function overBy(d, B) {
    var x = mathExtent(d);
    return Math.max(x ? x.w - B : 0, d.scrollWidth - d.clientWidth);
  }

  function fitSet(ds, hang) {
    var m = ds.map(function (d) {
      if (!d.getClientRects().length) return null;       /* not rendered: a closed <details> */
      var x = mathExtent(d), B = d.clientWidth;
      if (!x || !B) return null;
      var ov = overBy(d, B);
      return { d: d, B: B, W: B + Math.max(0, ov), ov: ov, k: 1 };
    });
    var live = m.filter(function (o) { return o && o.ov > 0.5; });
    /* Scaling is not quite linear (rules and struts snap to pixels), so the
       size is stepped down from the measured overflow and measured again, a
       few times at most, never below the floor. */
    for (var pass = 0; pass < 3 && live.length; pass++) {
      live.forEach(function (o) {
        /* one per cent under the measured ratio, so that one pass is
           nearly always enough: each pass is a layout of the chapter */
        var k = Math.floor(o.k * (o.B - 1) / (o.B + o.ov) * 990) / 1000;
        if (k >= FIT_FLOOR) { o.k = k; o.d.style.fontSize = k + 'em'; }
        else { o.k = 0; o.d.style.fontSize = ''; tidy(o.d); }
      });
      live = live.filter(function (o) {
        if (!o.k) return false;
        o.ov = overBy(o.d, o.B);
        return o.ov > 0.5;
      });
    }
    /* still over after the last pass: back to full size, to scroll */
    live.forEach(function (o) { o.k = 0; o.d.style.fontSize = ''; tidy(o.d); });
    m.forEach(function (o) { if (o && o.k === 1) o.k = o.ov > 0.5 ? 0 : 1; });
    var room = 0, col = null;
    if (hang) {
      var main = document.querySelector('.main');
      col = main && main.querySelector('.col');
      room = main ? parseFloat(getComputedStyle(main).getPropertyValue('--breakout')) : 0;
      room = isFinite(room) ? room - HANG_GAP : 0;
    }
    var hung = [];
    m.forEach(function (o) {
      if (!o || o.k) return;                              /* fits, or fitted */
      var need = Math.ceil(o.W - o.B) + 2;
      if (room > 0 && col && need <= room && !o.d.closest('.eq') && col.contains(o.d)) {
        var top = o.d;
        while (top.parentElement && top.parentElement !== col) top = top.parentElement;
        var panel = top !== o.d && !/^(SPAN|P)$/.test(top.tagName) ? top : null;
        hung.push({ d: o.d, need: need, panel: panel });
        if (panel) panel._hang = Math.max(panel._hang || 0, need);
      } else {
        o.d.classList.add('scrolls');
      }
    });
    hung.forEach(function (h) {
      if (h.panel && fitted.panels.indexOf(h.panel) < 0) {
        h.panel._pad = parseFloat(getComputedStyle(h.panel).paddingRight) || 0;
        fitted.panels.push(h.panel);
      }
    });
    hung.forEach(function (h) {
      h.d.style.marginRight = -h.need + 'px';
      if (h.panel) {
        h.panel.style.marginRight = -h.panel._hang + 'px';
        h.panel.style.paddingRight = (h.panel._pad + h.panel._hang) + 'px';
      }
    });
    fitted.ds = fitted.ds.concat(ds);
  }

  /* Each number on its display's line when the centred maths leaves room for
     it, else below it. */
  function numberSet(eqs) {
    var drop = eqs.filter(function (e) {
      var n = null, d = e.querySelector('.katex-display');
      for (var c = e.firstElementChild; c; c = c.nextElementSibling)
        if (c.classList.contains('eqnum')) { n = c; break; }
      if (!n || !d) return false;
      var nr = n.getBoundingClientRect(), x = mathExtent(d);
      if (!nr.width || !x) return false;
      var b = d.getBoundingClientRect();
      var L = Math.max(x.L, b.left), R = Math.min(x.R, b.right);
      return nr.left < R + NUM_GAP && nr.right > L - NUM_GAP;
    });
    drop.forEach(function (e) { e.classList.add('eq-drop'); });
    fitted.eqs = fitted.eqs.concat(eqs);
  }

  /* The width and the state of the fonts the last pass measured at. The
     status is read after the pass, whose layout is what asks for the maths
     faces: a pass made while they were loading is made again when they
     arrive, and only then. */
  var fitWidth = -1, fitFonts = '';
  function fonts() { return document.fonts ? document.fonts.status : 'loaded'; }
  function fitMaths() {
    if (!booted && document.readyState === 'loading') return;
    unfit();
    fitSet([].slice.call(document.querySelectorAll('.main .col .katex-display')), true);
    numberSet([].slice.call(document.querySelectorAll('.main .col .eq')));
    fitWidth = window.innerWidth;
    fitFonts = fonts();
    if (fitFonts !== 'loaded' && document.fonts && document.fonts.ready)
      document.fonts.ready.then(function () { refit(false); });
  }
  var fitT = 0;
  function refit(force) {
    if (!force && window.innerWidth === fitWidth && fitFonts === 'loaded') return;
    clearTimeout(fitT);
    fitT = setTimeout(fitMaths, 90);
  }
  /* the first pass is registered after the boot handler, below */
  window.addEventListener('load', function () { refit(false); });
  window.addEventListener('resize', function () { refit(false); });
  /* A <details> that opens shows displays nothing could measure while it
     was closed: those are fitted where they are, and nothing else moves. */
  document.addEventListener('toggle', function (e) {
    var t = e.target;
    if (!t || !t.open || !t.querySelector || !t.closest('.main .col')) return;
    var ds = [].slice.call(t.querySelectorAll('.katex-display')).filter(function (d) {
      return !d.style.fontSize && !d.style.marginRight && !d.classList.contains('scrolls');
    });
    if (!ds.length) return;
    fitSet(ds, true);
    numberSet([].slice.call(t.querySelectorAll('.eq')));
  }, true);
  onSnapshot(function () { clearTimeout(fitT); unfit(); });
  /* A printed page is laid out at the paper's width, which nothing here
     measured: it prints the maths at its own size, the numbers in the
     reserved space book.css gives them in print, and no panel reaching into
     a margin the paper does not have. Fitted again afterwards. */
  window.addEventListener('beforeprint', function () { clearTimeout(fitT); unfit(); });
  window.addEventListener('afterprint', function () { refit(true); });

  /* ---------- the reference card ----------
     Bring the reference to the citation rather than sending the reader to the
     foot of a twenty-thousand-word chapter and losing their place. The same
     card, and on a thumb the same sheet, serves a trial mark (its facts and
     its row in the registry) and a defined term (its definition).

     The entry is read out of the page's own reference list, so there is no
     second copy to keep in step, nothing to fetch, and it works with the
     network off. Books with no citations and no marks have none of these
     elements and this returns immediately, so nothing is added to a page that
     cannot use it. */
  function refCards() {
    var cites = [].slice.call(document.querySelectorAll('a.cite[href^="#r-"]'));
    var mks = marks();
    /* An equation reference (physics) gets the same card: a clone of the
       equation's display and its number, made when the card opens, and "Go to
       equation". The link itself still jumps. */
    var eqrefs = [].slice.call(document.querySelectorAll('.main a.eqref[href^="#"]'))
      .filter(function (a) { return !!eqTarget(a); });
    if (!cites.length && !mks.length && !eqrefs.length) return;

    /* A mouse gets a card on hover. A thumb has no hover, so it gets a sheet on
       tap -- and there the tap must not also jump to the list. */
    var hoverable = !(window.matchMedia && matchMedia('(hover: none)').matches);
    var card = null, scrim = null, openFor = null, showT = 0, hideT = 0;

    function build() {
      if (card) return;
      card = document.createElement('div');
      card.className = 'refcard';
      card.id = 'refcard';
      document.body.appendChild(card);
      card.addEventListener('mouseenter', function () { clearTimeout(hideT); });
      card.addEventListener('mouseleave', schedHide);
      card.addEventListener('focusin', function () { clearTimeout(hideT); });
      card.addEventListener('focusout', function (e) {
        var to = e.relatedTarget;
        if (to && (card.contains(to) || to === openFor)) return;
        if (!scrim) schedHide();
      });
      card.addEventListener('keydown', function (e) {
        /* The card sits at the end of <body>, so a Tab out of it would land
           on whatever follows the page, and the page would scroll there. Tab
           and Shift+Tab close it instead: Shift+Tab goes back to the mark,
           Tab on to the next stop after the mark, and the reader keeps the
           place. */
        if (e.key === 'Tab') {
          var from = openFor;
          if (!from) return;
          e.preventDefault();
          close();
          var to = e.shiftKey ? null : nextStop(from);
          /* The next stop takes focus only when it starts within one screen
             below the mark; it is focused with scrolling allowed, so the
             browser brings it into view with a small scroll. A stop farther
             away than that, or none at all, leaves focus on the mark without
             scrolling, so focus never lands out of sight. */
          if (to && to.getBoundingClientRect().top - from.getBoundingClientRect().top >= innerHeight) to = null;
          if (to) to.focus();
          else from.focus({ preventScroll: true });
          return;
        }
        if (e.key !== 'Escape') return;
        var back = openFor;
        close();
        if (back && back.focus) back.focus({ preventScroll: true });
      });
      /* The sheet's handle is real, as the drawer's is: drag its head down
         more than 64px and it closes. */
      dragToClose(card, function (t) {
        return !!(scrim && t && t.closest && t.closest('.rc-head'));
      }, function () { close(); });
    }

    function entry(a) {
      var id = (a.getAttribute('href') || '').slice(1);
      /* getElementById rather than a selector: a reference key may contain
         characters that would need escaping in CSS. */
      var li = id && document.getElementById(id);
      return li && li.tagName === 'LI' ? li : null;
    }
    function isCite(a) { return a.classList.contains('cite'); }
    function isEq(a) { return a.classList.contains('eqref'); }
    function label(a) {
      var t = (a.textContent || '').replace(/\s+/g, ' ').trim();
      return isEq(a) ? 'Equation ' + t : t;
    }

    /* The first keyboard stop after the mark in document order, outside the
       card, or null. */
    function nextStop(a) {
      var sel = 'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),' +
                'textarea:not([disabled]),summary,[tabindex]:not([tabindex="-1"])';
      var all = document.querySelectorAll(sel);
      for (var i = 0; i < all.length; i++) {
        var el = all[i];
        if (el === a || card.contains(el)) continue;
        if (!(a.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
        if (a.contains(el) || el.closest('[hidden],[inert]')) continue;
        if (!el.getClientRects().length) continue;
        return el;
      }
      return null;
    }

    function place(a) {
      /* Fixed coordinates, so the card is positioned against the viewport and
         does not need the page's scroll offset. Preferred below the mark;
         flipped above when the room is not there. Clamped to a 12px gutter so
         it can never sit half off a narrow screen. A mark that wraps is
         placed by its first line. */
      var m = 12, rs = a.getClientRects(), r = rs.length ? rs[0] : a.getBoundingClientRect();
      var c = card.getBoundingClientRect();
      var top = r.bottom + 8;
      if (top + c.height > innerHeight - m) {
        var above = r.top - c.height - 8;
        if (above >= m) top = above;
        else top = Math.max(m, innerHeight - c.height - m);
      }
      var left = Math.min(Math.max(m, r.left + r.width / 2 - c.width / 2),
                          innerWidth - c.width - m);
      card.style.top = Math.round(top) + 'px';
      card.style.left = Math.round(left) + 'px';
    }

    /* The card's content, as nodes. A citation: its number and the entry.
       A trial: the name, the facts and the registry link. A term: the term
       and its definition. */
    function fill(a, asSheet) {
      var head = document.createElement(asSheet ? 'div' : 'span'), frag = document.createDocumentFragment();
      if (asSheet) {
        head.className = 'rc-head';
        head.innerHTML = '<span class="rc-close"></span>';
      }
      if (isEq(a)) {
        var eq = eqTarget(a), d = eq && eq.querySelector('.katex-display');
        if (!d) return null;
        if (asSheet) frag.appendChild(head);
        var box = document.createElement('div');
        box.className = 'rc-eq';
        var dc = d.cloneNode(true);
        dc.removeAttribute('style');
        dc.classList.remove('scrolls');
        [].forEach.call(dc.querySelectorAll('[id]'), function (e) { e.removeAttribute('id'); });
        box.appendChild(dc);
        for (var c = eq.firstElementChild; c; c = c.nextElementSibling) {
          if (c.classList.contains('eqnum')) { box.appendChild(c.cloneNode(true)); break; }
        }
        frag.appendChild(box);
        var go = document.createElement('a');
        go.className = 'rc-go';
        go.setAttribute('href', '#' + eq.id);
        go.textContent = 'Go to equation';
        go.addEventListener('click', function () { close(); });
        frag.appendChild(go);
        return frag;
      }
      if (isCite(a)) {
        var li = entry(a);
        if (!li) return null;
        var n = document.createElement('span');
        n.className = 'rc-n';
        n.textContent = 'Reference ' + (a.textContent || '').trim();
        if (asSheet) { head.appendChild(n); frag.appendChild(head); } else frag.appendChild(n);
        var body = document.createElement('div');
        body.innerHTML = li.innerHTML;
        while (body.firstChild) frag.appendChild(body.firstChild);
        return frag;
      }
      var t = document.createElement('span');
      t.className = 'rc-t';
      t.textContent = (a.textContent || '').replace(/\s+/g, ' ').trim();
      if (asSheet) { head.appendChild(t); frag.appendChild(head); } else frag.appendChild(t);
      var facts = a.getAttribute('data-facts') || a.getAttribute('title') || '';
      if (facts) {
        var f = document.createElement('p');
        f.className = 'rc-f';
        f.textContent = facts;
        frag.appendChild(f);
      }
      var key = a.getAttribute('data-trial');
      if (key && !onFile()) {
        var go = document.createElement('a');
        go.className = 'rc-go';
        go.setAttribute('href', registryHref(key));
        go.textContent = 'Full record in the Trial Registry →';
        frag.appendChild(go);
      }
      return frag;
    }

    function show(a, asSheet) {
      build();
      var content = fill(a, asSheet);
      if (!content) return;
      close(true);
      openFor = a;
      card.className = 'refcard' + (asSheet ? ' sheet' : '') + (isEq(a) ? ' rc-eqcard' : '');
      card.setAttribute('role', isCite(a) && !asSheet ? 'tooltip' : 'dialog');
      if (!isCite(a)) card.setAttribute('aria-label', label(a));
      else card.removeAttribute('aria-label');
      card.innerHTML = '';
      card.appendChild(content);
      /* the cloned display is fitted to the card as the page's are to the
         column: a little small, or scrolling with its edge shades */
      if (isEq(a)) fitSet([].slice.call(card.querySelectorAll('.katex-display')), false);
      a.setAttribute('aria-expanded', 'true');
      if (!isCite(a)) a.setAttribute('aria-controls', 'refcard');
      if (asSheet) {
        scrim = document.createElement('div');
        scrim.className = 'refscrim';
        scrim.addEventListener('click', function () { close(); });
        document.body.appendChild(scrim);
        card.style.top = card.style.left = '';
        requestAnimationFrame(function () {
          if (scrim) scrim.classList.add('on');
          card.classList.add('on');
        });
      } else {
        card.style.visibility = 'hidden';
        card.classList.add('on');
        requestAnimationFrame(function () {
          place(a); card.style.visibility = '';
        });
      }
    }

    function close(immediate) {
      clearTimeout(showT); clearTimeout(hideT);
      if (openFor) {
        openFor.removeAttribute('aria-expanded');
        openFor.removeAttribute('aria-controls');
        openFor = null;
      }
      if (card) card.classList.remove('on');
      if (scrim) {
        var s = scrim; scrim = null;
        s.classList.remove('on');
        if (immediate) s.remove();
        else setTimeout(function () { s.remove(); }, 220);
      }
    }
    function schedHide() { clearTimeout(hideT); hideT = setTimeout(close, 180); }

    function hover(a) {
      a.addEventListener('mouseenter', function () {
        clearTimeout(hideT);
        if (openFor === a) return;
        clearTimeout(showT);
        showT = setTimeout(function () { show(a, false); }, 110);
      });
      a.addEventListener('mouseleave', function () {
        clearTimeout(showT); schedHide();
      });
      /* Keyboard reaches the same card. */
      a.addEventListener('focus', function () { if (openFor !== a) show(a, false); });
      a.addEventListener('blur', function (e) {
        if (card && e.relatedTarget && card.contains(e.relatedTarget)) return;
        schedHide();
      });
    }

    cites.forEach(function (a) {
      if (hoverable) hover(a);
      a.addEventListener('click', function (e) {
        /* Only on a touch screen does the tap take over from the jump. With a
           mouse the click still goes to the list, which is where a reader who
           clicked rather than hovered was asking to go; the list opens first,
           so the jump has somewhere to land. */
        if (hoverable) { openRefs(); return; }
        if (!entry(a)) return;
        e.preventDefault();
        show(a, true);
      });
    });

    eqrefs.forEach(function (a) {
      if (a._card) return;
      a._card = true;
      if (hoverable) hover(a);
      /* With a mouse or a keyboard the link jumps, as it always did, and the
         card closes first so that it is not left following a mark the page
         has just scrolled away. On a thumb the tap opens the sheet, whose
         "Go to equation" makes the jump. */
      a.addEventListener('click', function (e) {
        if (hoverable) { close(); return; }
        e.preventDefault();
        if (openFor === a) { close(); return; }
        show(a, true);
      });
    });

    mks.forEach(function (a) {
      if (a._card) return;
      a._card = true;
      var link = a.tagName === 'A';
      if (hoverable) hover(a);
      /* A tap opens the sheet, as it does for a citation; the sheet carries
         the registry link. With a mouse or a keyboard a chip that is a link
         goes to the registry, and any other mark opens its card. */
      a.addEventListener('click', function (e) {
        if (link && hoverable) return;
        e.preventDefault();
        if (openFor === a && !hoverable) { close(); return; }
        show(a, !hoverable);
      });
      if (link) return;
      a.addEventListener('keydown', function (e) {
        if (e.key !== 'Enter' && e.key !== ' ' && e.key !== 'Spacebar') return;
        e.preventDefault();
        if (openFor !== a) show(a, !hoverable);
        /* A card show() has just opened stays hidden until it is placed on
           the next frame, and a hidden link cannot take focus. Place it now,
           so Enter on a mark whose card Escape had closed still moves focus
           into the card. */
        if (card && openFor === a && card.style.visibility === 'hidden') {
          place(a); card.style.visibility = '';
        }
        /* From the keyboard the card's one link is the next stop. */
        var go = card && card.querySelector('.rc-go');
        if (go) go.focus({ preventScroll: true });
      });
    });

    addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' || !openFor) return;
      var back = openFor, inside = card && card.contains(document.activeElement);
      close();
      if (inside && back.focus) back.focus({ preventScroll: true });
    });
    /* A card pinned to a viewport coordinate is wrong the moment anything moves
       under it, so on any scroll it is placed again, once a frame, or closed
       when its mark has left the screen or its table's scroller. Capture,
       because scroll does not bubble and the mark may sit inside a scroll
       container of its own -- an evidence table scrolls sideways by design,
       and without this the card stayed put while the mark it belongs to slid
       out from under it. */
    var following = false;
    addEventListener('scroll', function () {
      if (!openFor || scrim || following) return;
      following = true;
      (window.requestAnimationFrame || setTimeout)(function () {
        following = false;
        if (!openFor || scrim) return;
        /* A card follows its mark while the mark is in view, or while the
           keyboard is on the mark or in the card (the scroll a focus starts
           to bring the mark into view); once the mark has gone, so does the
           card. */
        var r = openFor.getBoundingClientRect(), sc = openFor.closest('.ev-scroll');
        var box = sc ? sc.getBoundingClientRect() : { left: 0, right: innerWidth };
        var gone = r.bottom < 0 || r.top > innerHeight || r.right < box.left || r.left > box.right;
        var kept = document.activeElement === openFor || card.contains(document.activeElement);
        if (gone && !kept) close();
        else place(openFor);
      });
    }, { passive: true, capture: true });
    addEventListener('resize', function () { close(); });
  }

  /* ---------- where the reader is: the spy ----------
     One answer for three surfaces: the sidebar's section list, the drawer's
     list and the folio's label (NAV-08). The active entry is the last heading
     whose top is above the bar's visible bottom edge plus 24px (0 + 24 while
     headroom has the bar out of view). Nothing is active only above the first
     heading. It is computed from layout, on a scroll throttled to one frame,
     on load, on hashchange, on resize and after pwa.js restores a position,
     rather than from an observer that only saw headings entering a band at
     the top, which was wrong on every scroll up and empty after any jump.

     The sidebar keeps the active entry in view by scrolling itself, never the
     page. These listeners are registered here, outside the boot handler, so
     runtime_js() leaves them alone (DESIGN.md section 8). */
  var SPY = null, booted = false;
  var DOC = document.documentElement;

  function narrow() { return !!(window.matchMedia && matchMedia('(max-width: 1000px)').matches); }
  function still() { return !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches); }

  function spyCollect() {
    var hs = [].slice.call(document.querySelectorAll('.main h2[id], .main h3[id]'));
    function links(box) {
      var m = {};
      if (box) [].forEach.call(box.querySelectorAll('a[href^="#"]'), function (a) {
        m[a.getAttribute('href').slice(1)] = a;
      });
      return m;
    }
    var sb = links(document.getElementById('sb-toc'));
    var mn = links(mnav && mnav.list);
    /* Whatever an earlier script or an older build left marked is cleared:
       nothing is active until it has been measured. */
    [].forEach.call(document.querySelectorAll('#sb-toc a.active, #mnav .mn-list a.active'), function (a) {
      a.classList.remove('active');
      a.removeAttribute('aria-current');
    });
    SPY = { hs: hs, at: undefined, sbOn: null, mnOn: null,
            sb: hs.map(function (h) { return sb[h.id] || null; }),
            mn: hs.map(function (h) { return mn[h.id] || null; }) };
  }

  /* The bar's visible bottom edge: 0 with no bar (the Dropbox build) or while
     headroom has it hidden; otherwise where it ends when shown, even halfway
     through the transition back. */
  function chromeEdge() {
    var bar = document.querySelector('.topnav');
    if (!bar || DOC.classList.contains('chrome-hidden')) return 0;
    var r = bar.getBoundingClientRect();
    return r.height ? Math.max(0, r.top) + r.height : 0;
  }

  /* The nearest scrolling box between el and stop, and el kept inside it. */
  function keepInView(el, stop) {
    if (!el || !stop) return;
    for (var box = el.parentElement; box; box = box.parentElement) {
      var o = getComputedStyle(box).overflowY;
      if ((o === 'auto' || o === 'scroll') && box.scrollHeight > box.clientHeight + 1) break;
      if (box === stop) return;
    }
    if (!box || !box.clientHeight) return;
    var b = box.getBoundingClientRect(), r = el.getBoundingClientRect(), pad = 16;
    if (r.top < b.top + pad) box.scrollTop -= b.top + pad - r.top;
    else if (r.bottom > b.bottom - pad) box.scrollTop += r.bottom - b.bottom + pad;
  }

  function mark(was, now) {
    if (was === now) return now;
    if (was) { was.classList.remove('active'); was.removeAttribute('aria-current'); }
    if (now) { now.classList.add('active'); now.setAttribute('aria-current', 'location'); }
    return now;
  }

  function spyNow(force) {
    if (!booted) return;
    if (!SPY) spyCollect();
    var edge = chromeEdge() + 24, at = -1, i, k;
    for (i = 0; i < SPY.hs.length; i++) {
      var r = SPY.hs[i].getBoundingClientRect();
      if (!r.width && !r.height) continue;         /* not rendered: inside a closed <details> */
      if (r.top < edge) at = i; else break;
    }
    if (at === SPY.at && !force) return;
    SPY.at = at;

    var sl = null, h2 = -1;
    for (k = at; k >= 0 && !sl; k--) sl = SPY.sb[k];
    for (k = at; k >= 0; k--) if (SPY.hs[k].tagName === 'H2') { h2 = k; break; }
    var ml = h2 >= 0 ? SPY.mn[h2] : null;

    SPY.sbOn = mark(SPY.sbOn, sl);
    if (sl) keepInView(sl, document.querySelector('.sidebar') || sl.parentElement);
    SPY.mnOn = mark(SPY.mnOn, ml);
    if (ml && mnav && mnav.panel.classList.contains('open')) keepInView(ml, mnav.list);

    if (mnav && mnav.label) {
      var t = h2 >= 0 ? (ml ? ml.textContent : headingText(SPY.hs[h2]))
            : at >= 0 ? headingText(SPY.hs[at]) : mnav.idle;
      if (mnav.label.textContent !== t) {
        mnav.label.textContent = t;
        mnav.btn.setAttribute('aria-label', t === mnav.idle ? t : mnav.idle + ': ' + t);
      }
    }
  }

  /* ---------- headroom ----------
     Below 1000px, on the chapter shell, reading down takes the bar and the
     folio out of view (html.chrome-hidden; transforms only, nav.css). They
     come back on a deliberate scroll up: 48px of it, counted from the last
     downward movement, or a flick. A nudge up to re-read a line does not
     bring back 100px of chrome. They always show above 120px, in the last
     1.5 viewports of the page, while keyboard focus is in the bar or the
     folio, and while the drawer or the bar's menu is open. */
  var HR = { y: 0, up: 0, down: 0, t: [], jumpTill: 0, shell: null };

  function chromeHidden(on) {
    if (DOC.classList.contains('chrome-hidden') === on) return;
    DOC.classList.toggle('chrome-hidden', on);
    spyNow(true);
  }
  function chromeShow() { HR.up = HR.down = 0; chromeHidden(false); }

  /* An in-page jump (a section in the drawer, a cross-reference, a restored
     position) leaves the chrome where it is until the scroll it started ends,
     so the heading lands below the bar the scroll padding allowed for. */
  function jumping() { HR.jumpTill = Date.now() + 3000; HR.up = HR.down = 0; }

  function holding() {
    if (document.querySelector('#mnav.open, .topnav.menu-open')) return true;
    var a = document.activeElement;
    if (!a || !a.closest || !a.closest('.topnav, .folio')) return false;
    try { return a.matches(':focus-visible'); } catch (e) { return true; }
  }

  function flick(now) {
    var s = HR.t;
    if (s.length < 3) return false;
    var a = s[0], b = s[s.length - 1], dt = b[0] - a[0];
    return dt >= 24 && (a[1] - b[1]) / dt > 1;       /* up, faster than 1000px/s */
  }

  function headroom(y, now) {
    var dy = y - HR.y;
    HR.y = y;
    if (HR.shell === null) HR.shell = !!document.querySelector('.wrap .main, .wrap .sidebar');
    if (!HR.shell || !narrow()) { HR.up = HR.down = 0; chromeHidden(false); return; }
    var H = DOC.scrollHeight, vh = window.innerHeight;
    if (y < 0 || y > H - vh + 1) return;              /* the rubber band at either end */
    HR.t.push([now, y]);
    while (HR.t.length && now - HR.t[0][0] > 150) HR.t.shift();
    if (y <= 120 || y >= H - 1.5 * vh || holding()) { chromeShow(); return; }
    if (dy > 0) {
      HR.up = 0;
      HR.down += dy;
      if (HR.down > 8 && Date.now() >= HR.jumpTill) chromeHidden(true);
    } else if (dy < 0) {
      HR.down = 0;
      HR.up -= dy;
      if (HR.up >= 48 || flick(now)) chromeShow();
    }
  }

  var ticking = false;
  function frame() {
    ticking = false;
    if (!booted) return;
    var y = window.pageYOffset || DOC.scrollTop || 0;
    headroom(y, window.performance && performance.now ? performance.now() : Date.now());
    spyNow(false);
  }
  function soon() {
    if (ticking) return;
    ticking = true;
    (window.requestAnimationFrame || setTimeout)(frame);
  }

  window.addEventListener('scroll', soon, { passive: true });
  window.addEventListener('resize', function () { if (SPY) SPY.at = undefined; soon(); });
  window.addEventListener('scrollend', function () {
    if (HR.jumpTill) { HR.jumpTill = 0; HR.up = HR.down = 0; }
  });
  window.addEventListener('hashchange', function () { jumping(); chromeShow(); soon(); });
  window.addEventListener('load', function () {
    HR.y = window.pageYOffset || 0;
    spyNow(true);
  });
  /* pwa.js has put the reader back where they were */
  window.addEventListener('library:restored', function () {
    HR.y = window.pageYOffset || 0;
    jumping();
    chromeShow();
    spyNow(true);
  });
  /* A link to a place on this page is a jump too. The flag goes up here, in
     the click, before the scroll the link starts; a link whose handler kept it
     from jumping (a citation that opens its sheet on a thumb) is not one. */
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented) return;
    var a = e.target && e.target.closest && e.target.closest('a[href^="#"]');
    if (a && a.getAttribute('href').length > 1) { jumping(); chromeShow(); }
  });
  document.addEventListener('focusin', function () { if (holding()) chromeShow(); });

  /* ---------- boot ---------- */
  window.addEventListener('DOMContentLoaded', function () {
    /* numbered at build time */
    sittingBreaks();
    var hs = sectionHeadings();
    buildTOC(hs);
    buildMobileNav(hs);
    findChapter();
    refsList();
    evidenceCues();
    refCards();
    });

  /* The spy's first answer, once the boot has built the lists it marks.
     Registered after the boot handler, so it runs after it. A page opened at
     a #fragment is a jump: the browser's scroll to it does not hide the
     chrome. */
  window.addEventListener('DOMContentLoaded', function () {
    booted = true;
    HR.y = window.pageYOffset || 0;
    if (location.hash) jumping();
    spyNow(true);
  });

  /* The displays' first fit, after the boot. While the maths faces are
     still arriving a display measured now is the wrong width and would be
     measured again, a layout of the whole chapter each time, so the first
     fit waits for them (and load, below, makes it in any case). */
  window.addEventListener('DOMContentLoaded', function () {
    if (fonts() === 'loading' && document.fonts.ready)
      document.fonts.ready.then(function () { refit(false); });
    else fitMaths();
  });

  return { Plot: Plot, figure: figure, redrawAll: redrawAll, css: css, color: color,
           typeset: typeset, onSnapshot: onSnapshot, resetForSnapshot: resetForSnapshot };
})();
