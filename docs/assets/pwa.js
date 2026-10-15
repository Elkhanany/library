/* The library's client-side app layer.
 *
 * Loaded with defer on every built page, from the block tools/pwa.py injects.
 * One file rather than an addition to book.js, for two reasons: book.js also
 * ships to the file:// Dropbox build via tools/make.py, where none of this
 * applies and a service worker cannot even be registered; and the philosophy
 * book's single-file landing page loads book.js not at all, so anything added
 * there would silently skip the most app-like page in the library.
 *
 * Everything here is additive. With JavaScript off, or on a browser with no
 * service worker, or when the registration fails, every page still renders and
 * every link still works -- the reader simply does not get the offline layer.
 */
(function () {
  'use strict';

  var KEY = 'library:v1';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var html = document.documentElement;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}') || {}; }
    catch (e) { return {}; }
  }
  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* private mode */ }
  }

  var state = load();

  /* ================================================================ the bar
   * Everything in this first part works on any page that carries the library
   * bar, file:// included, because none of it needs a worker: the theme
   * button, the Menu, and the skip link. The app layer proper starts below the
   * file:// check. */

  /* ---------------------------------------------------------------- colour
   * A custom property's value cannot be read as a colour: getPropertyValue()
   * returns the unresolved color-mix() text, and a computed colour serialises
   * as color(srgb ...), which not every consumer accepts. So a colour is
   * resolved by setting var(--x) on a probe element, painting the probe's
   * computed colour into a 1x1 canvas, and reading the pixel back as #rrggbb
   * (DESIGN.md section 3). book.js has its own copy as NMT.color(). */
  var probe = null, cx = null;
  function resolve(name) {
    try {
      if (!getComputedStyle(html).getPropertyValue(name).trim()) return '';
      var host = document.body || html;
      if (!probe) {
        probe = document.createElement('i');
        probe.setAttribute('aria-hidden', 'true');
        probe.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden;' +
                              'visibility:hidden;pointer-events:none';
      }
      if (probe.parentNode !== host) host.appendChild(probe);
      probe.style.color = 'var(' + name + ')';
      var c = getComputedStyle(probe).color;
      if (!cx) {
        var cv = document.createElement('canvas');
        cv.width = cv.height = 1;
        cx = cv.getContext('2d', { willReadFrequently: true });
      }
      cx.clearRect(0, 0, 1, 1);
      cx.fillStyle = '#010203';
      cx.fillStyle = c;
      if (cx.fillStyle === '#010203') return '';     /* the canvas could not read it */
      cx.fillRect(0, 0, 1, 1);
      var d = cx.getImageData(0, 0, 1, 1).data;
      if (d[3] < 255) return 'rgba(' + d[0] + ',' + d[1] + ',' + d[2] + ',' + (d[3] / 255).toFixed(3) + ')';
      return '#' + [d[0], d[1], d[2]].map(function (v) { return (v < 16 ? '0' : '') + v.toString(16); }).join('');
    } catch (e) { return ''; }
  }

  /* The browser's own chrome follows the page (PDA-14): every theme-color meta
   * is set to the ground the page is actually painted in, --bg where the page
   * has one and --paper on the two philosophy books. On the hub that is the
   * media pair, which then agrees with the reader's choice rather than the
   * OS's. */
  function themeColor() {
    var c = resolve('--bg') || resolve('--paper');
    if (!c || c.charAt(0) !== '#') return;
    document.querySelectorAll('meta[name="theme-color"]').forEach(function (m) {
      if (m.getAttribute('content') !== c) m.setAttribute('content', c);
    });
  }

  /* ----------------------------------------------------------------- theme
   * The boot script in <head> decided the theme before first paint (pwa.py
   * BOOT: library:v1.look, then nmt-theme, then the OS). This wires the one
   * control, button.nav-theme, the last item in the bar on every page. Nothing
   * is written until the reader presses it: the old passive write of the
   * current theme pinned OS-dark readers to light (NAV-02, PDA-01). */
  function dark() { return html.getAttribute('data-theme') === 'dark'; }

  function paintThemeButtons() {
    var on = dark();
    document.querySelectorAll('button.nav-theme').forEach(function (b) {
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.title = on ? 'Switch to light' : 'Switch to dark';
    });
  }

  function flipTheme() {
    var t = dark() ? 'light' : 'dark';
    html.setAttribute('data-theme', t);
    state.look = t;
    delete state.theme;          /* the passive key, never read again */
    save(state);
    /* The older key too, so a page this shell has not replaced yet -- whose
     * book.js still reads nmt-theme -- opens in the theme the reader chose. */
    try { localStorage.setItem('nmt-theme', t); } catch (e) { /* private mode */ }
    paintThemeButtons();
    themeColor();
    try { window.dispatchEvent(new CustomEvent('library:theme', { detail: { theme: t } })); }
    catch (e) { /* no CustomEvent constructor: the attribute observers still fire */ }
  }

  function wireTheme() {
    var bs = document.querySelectorAll('button.nav-theme');
    if (!bs.length) return;
    bs.forEach(function (b) {
      if (b.getAttribute('data-wired')) return;
      b.setAttribute('data-wired', '1');
      b.addEventListener('click', flipTheme);
      b.hidden = false;
    });
    /* book.js reads this at window load: with it, no floating #themer. */
    html.classList.add('theme-wired');
    paintThemeButtons();
  }

  /* Anything else that flips the attribute -- book.js's fallback toggle on a
   * page this shell reaches before its own button is wired -- keeps the
   * button's state and the browser chrome in step. */
  new MutationObserver(function () { paintThemeButtons(); themeColor(); })
    .observe(html, { attributes: true, attributeFilter: ['data-theme'] });

  /* ------------------------------------------------------------------ menu
   * At 640px and below the book's destinations fold under one button, and
   * Library and the theme button stay in the bar (DESIGN.md section 6).
   * Escape closes it and gives focus back to the button; so do a tap outside
   * it and choosing a link. */
  function wireMenu() {
    var bar = $('.topnav');
    var btn = bar && bar.querySelector('button.nav-menu');
    var panel = btn && document.getElementById(btn.getAttribute('aria-controls') || 'nav-dest');
    if (!btn || !panel || btn.getAttribute('data-wired')) return;
    btn.setAttribute('data-wired', '1');

    function open() { return bar.classList.contains('menu-open'); }
    function set(on, refocus) {
      bar.classList.toggle('menu-open', on);
      btn.setAttribute('aria-expanded', on ? 'true' : 'false');
      if (!on && refocus) btn.focus();
    }
    btn.addEventListener('click', function () { set(!open()); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && open()) set(false, true);
    });
    document.addEventListener('click', function (e) {
      if (open() && !btn.contains(e.target) && !panel.contains(e.target)) set(false);
    });
    panel.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('a')) set(false);
    });
    addEventListener('resize', function () { if (open() && innerWidth > 640) set(false); });
    btn.hidden = false;
  }

  /* ------------------------------------------------------------- skip link
   * nav.py puts "Skip to text" first on every page, aimed at #text. A page
   * whose own markup names its text keeps that target. Otherwise nav.py left a
   * placeholder just after the bar (.skip-target), and the id moves from it to
   * the page's own main, .main, .app or .hero, in that order of preference, so
   * on a chapter the skip passes the sidebar too. Following the link focuses
   * the target, so the next Tab starts inside the text. */
  function wireSkip() {
    var target = document.getElementById('text');
    if (!target || target.classList.contains('skip-target')) {
      var sels = ['main', '.main', '.app', '.hero'], found = null;
      for (var i = 0; i < sels.length && !found; i++) found = $(sels[i]);
      if (found) {
        if (!found.id) {
          if (target) target.removeAttribute('id');
          found.id = 'text';
        }
        target = found;
      }
    }
    if (!target) return;
    document.querySelectorAll('a.skip').forEach(function (a) {
      if (a.getAttribute('data-wired')) return;
      a.setAttribute('data-wired', '1');
      if (a.getAttribute('href') !== '#' + target.id) a.setAttribute('href', '#' + target.id);
      a.addEventListener('click', function (e) {
        e.preventDefault();
        if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
        target.focus();
      });
    });
  }

  function wireBar() { wireTheme(); wireMenu(); wireSkip(); themeColor(); }
  if (document.readyState === 'loading') addEventListener('DOMContentLoaded', wireBar);
  else wireBar();
  /* the stylesheets may still have been arriving the first time */
  addEventListener('load', themeColor);

  /* file:// has no origin a worker can be registered against, and the Dropbox
   * build is opened exactly that way. Leave now rather than throwing. */
  if (location.protocol === 'file:') return;

  /* The book this page belongs to. The bar says so (nav.py stamps data-book),
   * and whenever it does the page sits one directory down, so ROOT is '../'.
   * That is right however docs/ is served: under the Pages project prefix,
   * at the root of a local preview, or on a custom domain. Deriving both from
   * the path assumed the prefix, and a root-served page lost the drawer's
   * prev/next, the arrow keys and position memory without a word (NAV-19).
   * The path is the fallback, for a page with no bar, and it is read below
   * the site root, which is the directory above this script's own assets/.
   * It used to skip one directory as the Pages project prefix ("library"),
   * which on the root of a domain is the book itself. */
  var SLUG = null, ROOT = './';
  (function () {
    var tn = document.querySelector('.topnav[data-book]');
    if (tn) {
      SLUG = tn.getAttribute('data-book') || null;
      ROOT = '../';
      return;
    }
    var base = '/', me = document.currentScript, path = location.pathname;
    try { if (me && me.src) base = new URL('../', me.src).pathname; }
    catch (e) { /* the root of the origin, then */ }
    if (path.indexOf(base) === 0) path = path.slice(base.length);
    var parts = path.split('/').filter(Boolean);
    var f = parts[parts.length - 1] || '';
    var dirs = /\.html?$/.test(f) ? parts.slice(0, -1) : parts.slice();
    /* a book is the first directory under the root; the hub has none */
    if (dirs.length >= 1) { SLUG = dirs[0]; ROOT = '../'; }
  })();

  /* ------------------------------------------------------- reading position
   * Where the reader was, per page, so a returning reader lands where they
   * left off. Deliberately does not fight a #hash: a link into a specific
   * section must win over a remembered scroll.
   *
   * And where they are in each book (DESIGN.md section 8): lastBy[slug] =
   * {url, num, title, pct, at}, written on a chapter page only, with the
   * number and title from nav.json, so the hub's Continue strip, the front
   * door, the contents page and continue.html?b= all name the same chapter
   * the same way. A front door or a contents page is not a place in the book
   * and records nothing there. It used to be one state.last for the whole
   * library, a document title and no number, so a reader of two books could
   * only ever continue the one they opened last (NAV-01). */
  function pageKey() { return location.pathname; }
  var restoring = null;          /* the stored place, until it is restored */

  function scrollPct() {
    var y = window.scrollY || document.documentElement.scrollTop || 0;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    return { y: y, pct: h > 0 ? Math.min(100, Math.round(100 * y / h)) : 0 };
  }

  function recordPlace(where) {
    var c = at(HERE);
    if (!SLUG || !c) return;
    /* before the stored scroll is put back, the page is at its top; the
     * place is still the one it is about to return to */
    var pct = (restoring && !where.y) ? restoring.pct : where.pct;
    state.lastBy = state.lastBy || {};
    state.lastBy[SLUG] = { url: pageKey(), num: c.num, title: c.title,
                           pct: pct || 0, at: Date.now() };
  }

  function rememberScroll() {
    if (!SLUG) return;
    var w = scrollPct();
    state.pos = state.pos || {};
    if (!(restoring && !w.y)) {
      state.pos[pageKey()] = { y: w.y, pct: w.pct, at: Date.now() };
    }
    recordPlace(w);
    save(state);
  }

  var t = null;
  addEventListener('scroll', function () {
    if (t) return;
    t = setTimeout(function () { t = null; rememberScroll(); }, 700);
  }, { passive: true });
  addEventListener('pagehide', rememberScroll);

  if (SLUG && !location.hash) {
    var rec = (state.pos || {})[pageKey()];
    /* Only worth restoring if they were meaningfully into the page. */
    if (rec && rec.y > 400) {
      restoring = rec;
      addEventListener('load', function () {
        requestAnimationFrame(function () {
          restoring = null;
          /* At once: the page's smooth scrolling would otherwise carry the
           * reader through the chapter to their place. */
          try { window.scrollTo({ top: rec.y, left: 0, behavior: 'instant' }); }
          catch (e) { window.scrollTo(0, rec.y); }
          /* book.js answers this: the sidebar, the drawer and the folio say
           * where the reader now is, and the chrome is shown (DESIGN.md
           * section 6, the spy). */
          try { window.dispatchEvent(new CustomEvent('library:restored', { detail: { y: rec.y } })); }
          catch (e) { /* no CustomEvent: the scroll event still reaches the spy */ }
        });
      });
    }
  }

  /* ------------------------------------------------------------ connectivity
   * A banner only when it is true and only while it is true. */
  var bar = null;
  function offlineBar(show) {
    if (show && !bar) {
      bar = document.createElement('div');
      bar.className = 'pwa-offline';
      bar.textContent = 'Offline — showing what is stored on this device';
      document.body.appendChild(bar);
    } else if (!show && bar) { bar.remove(); bar = null; }
  }
  addEventListener('online', function () { offlineBar(false); });
  addEventListener('offline', function () { offlineBar(true); });
  if (!navigator.onLine) addEventListener('DOMContentLoaded', function () { offlineBar(true); });

  /* ------------------------------------------------------------------ toast */
  function toast(msg, actionLabel, action) {
    var d = document.createElement('div');
    d.className = 'pwa-toast';
    var s = document.createElement('span'); s.textContent = msg; d.appendChild(s);
    if (actionLabel) {
      var b = document.createElement('button');
      b.textContent = actionLabel;
      b.onclick = function () { d.remove(); action(); };
      d.appendChild(b);
    }
    var x = document.createElement('button');
    x.className = 'x'; x.setAttribute('aria-label', 'Dismiss');
    x.textContent = '×';
    x.onclick = function () { d.remove(); };
    d.appendChild(x);
    document.body.appendChild(d);
    return d;
  }

  /* -------------------------------------------------------- service worker */
  var reg = null, reloading = false;

  if ('serviceWorker' in navigator) {
    addEventListener('load', function () {
      navigator.serviceWorker.register(ROOT + 'sw.js', { updateViaCache: 'none' })
        .then(function (r) {
          reg = r;
          r.addEventListener('updatefound', function () {
            var w = r.installing;
            if (!w) return;
            w.addEventListener('statechange', function () {
              /* controller present distinguishes an update from a first
               * install; on a first install there is nothing to reload for. */
              if (w.state === 'installed' && navigator.serviceWorker.controller) {
                toast('A new version of the library is ready.', 'Reload', function () {
                  if (r.waiting) r.waiting.postMessage({ type: 'SKIP_WAITING' });
                });
              }
            });
          });
        })
        .catch(function () { /* no worker; the site is a plain website */ });
    });

    navigator.serviceWorker.addEventListener('controllerchange', function () {
      if (reloading) return;      /* guard: controllerchange can fire twice */
      reloading = true;
      location.reload();
    });

    var offeredContent = false;
    navigator.serviceWorker.addEventListener('message', function (e) {
      if (e.data && e.data.type === 'ORPHANS' && e.data.slugs.length) {
        state.orphans = e.data.slugs; save(state);
      }
      /* The worker found that a page or dataset this reader has stored is no
       * longer what the site serves. Offer it once per visit: the page they
       * are reading is fine, it is simply not the current one. */
      if (e.data && e.data.type === 'CONTENT_UPDATED' && !offeredContent) {
        offeredContent = true;
        toast('This book has been updated.', 'Reload', function () {
          location.reload();
        });
      }
    });

    /* An installed app resumes from the switcher rather than cold-starting, so
     * the browser's own update schedule can strand a reader on a stale build
     * for days. Ask on return to the page, at most every five minutes. */
    var lastCheck = 0;
    function maybeUpdate() {
      if (!reg || document.visibilityState !== 'visible') return;
      var now = Date.now();
      if (now - lastCheck < 300000) return;
      lastCheck = now;
      reg.update().catch(function () {});
    }
    addEventListener('visibilitychange', maybeUpdate);
    addEventListener('pageshow', maybeUpdate);
  }

  /* ---------------------------------------------------------- the download
   * Runs in the page, never in the worker: iOS terminates a worker that stays
   * busy, and sixty-five megabytes is well past that. Resumable, because it
   * will be interrupted. */
  function bookCache(slug) { return 'lib:book:' + slug; }

  async function resident(slug) {
    try {
      /* caches.open() creates the cache if it is missing, so asking whether a
       * book is stored would quietly create an empty cache for every book in
       * the catalogue and make caches.keys() lie about what is downloaded. */
      if (!(await caches.has(bookCache(slug)))) return null;
      var c = await caches.open(bookCache(slug));
      var r = await c.match('__resident__');
      return r ? await r.json() : null;
    } catch (e) { return null; }
  }

  async function markResident(slug, data) {
    var c = await caches.open(bookCache(slug));
    await c.put('__resident__', new Response(JSON.stringify(data),
      { headers: { 'Content-Type': 'application/json' } }));
  }

  async function download(slug, onProgress) {
    var manifest = await (await fetch(ROOT + slug + '/offline.json',
      { cache: 'no-store' })).json();
    var have = (await resident(slug)) || { files: {} };
    var c = await caches.open(bookCache(slug));
    var names = Object.keys(manifest.files);
    var todo = names.filter(function (p) { return have.files[p] !== manifest.files[p]; });

    var done = names.length - todo.length, failed = 0;
    for (var i = 0; i < todo.length; i++) {
      var path = todo[i];
      try {
        var r = await fetch(ROOT + path, { cache: 'reload' });
        if (!r.ok) throw new Error(r.status);
        await c.put(ROOT + path, r);
        have.files[path] = manifest.files[path];
        done++;
        /* Written after every file, so an interrupted download resumes rather
         * than starting over. */
        if (done % 5 === 0) {
          await markResident(slug, { complete: false, files: have.files,
                                     bytes: manifest.bytes, at: Date.now() });
        }
      } catch (err) {
        failed++;
        if (String(err && err.name) === 'QuotaExceededError') {
          await markResident(slug, { complete: false, files: have.files,
                                     bytes: manifest.bytes, at: Date.now() });
          throw err;
        }
      }
      if (onProgress) onProgress(done, names.length, failed);
    }
    await markResident(slug, {
      complete: failed === 0, files: have.files, digest: manifest.digest,
      bytes: manifest.bytes, at: Date.now()
    });
    return { done: done, total: names.length, failed: failed };
  }

  async function removeBook(slug) {
    try { await caches.delete(bookCache(slug)); } catch (e) { /* nothing to do */ }
  }

  async function usage() {
    if (!navigator.storage || !navigator.storage.estimate) return null;
    try { return await navigator.storage.estimate(); } catch (e) { return null; }
  }

  function mb(n) {
    if (n == null) return '';
    return n >= 1048576 ? (n / 1048576).toFixed(n >= 10485760 ? 0 : 1) + ' MB'
                        : Math.max(1, Math.round(n / 1024)) + ' KB';
  }

  /* -------------------------------------------------------- install coaching
   * iOS fires no beforeinstallprompt, so there is no prompt to show -- only
   * instructions, and only to someone who could act on them: an iOS Safari
   * user who has not already installed. Shown once, then never again. */
  function isStandalone() {
    return navigator.standalone === true ||
           matchMedia('(display-mode: standalone)').matches;
  }
  function isIOS() {
    return /iPad|iPhone|iPod/.test(navigator.userAgent) ||
           (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  }

  function maybeCoach(host) {
    if (!host || isStandalone() || state.coached || !isIOS()) return;
    var d = document.createElement('div');
    d.className = 'pwa-install';
    d.innerHTML = '<b>Keep the library on your Home Screen</b>' +
      '<p>Tap the Share button, then <b>Add to Home Screen</b>. ' +
      'It opens full screen, and books you download stay readable offline.</p>';
    var b = document.createElement('button');
    b.textContent = 'Got it';
    b.onclick = function () { state.coached = 1; save(state); d.remove(); };
    d.appendChild(b);
    host.appendChild(d);
  }

  /* --------------------------------------------------------------- the hub
   * Drawn here rather than emitted by the build, because every word of it is
   * live: where the reader is in each book, what is stored, how far a
   * download has got, what a rebuild has changed underneath it. A
   * server-rendered answer would be wrong the moment it was painted. The hub
   * emits the empty places (DESIGN.md section 6, Hub): section[data-continue],
   * one button[data-offline] per tile, and p[data-store] below the grid. */

  /* "68 · Deciding whether to treat". The number is the one the contents page
   * shows, which in the physics book is "2.1" and in the clinical book is
   * "68", and neither is the index. */
  function label(c) { return c.num + ' · ' + c.title; }

  /* The Continue strip: one row per book the reader has a place in, most
   * recent first. The book's name and colours come from its own tile, so a
   * book that has left the shelf is not offered. */
  function continueStrip() {
    var sec = document.querySelector('section[data-continue]');
    var list = sec && sec.querySelector('ol');
    if (!list) return;
    var by = state.lastBy || {};
    var rows = Object.keys(by).map(function (slug) { return [slug, by[slug]]; })
      .filter(function (r) { return r[1] && r[1].url; })
      .sort(function (a, b) { return (b[1].at || 0) - (a[1].at || 0); });
    list.textContent = '';
    rows.forEach(function (r) {
      var tile = document.querySelector('.book[data-slug="' + r[0] + '"]');
      if (!tile) return;
      var name = (tile.querySelector('h2') || tile).textContent.trim();
      var pct = Math.max(0, Math.min(100, Math.round(r[1].pct || 0)));
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.setAttribute('href', r[1].url);
      a.setAttribute('data-book', r[0]);
      a.setAttribute('style', tile.getAttribute('style') || '');
      a.setAttribute('aria-label', 'Continue ' + name + ' at ' + label(r[1]) +
                                   ', ' + pct + '% through');
      a.innerHTML = '<span class="c-book"></span><span class="c-ch"></span>' +
                    '<span class="c-rule" aria-hidden="true"><i></i></span>';
      a.querySelector('.c-book').textContent = name;
      a.querySelector('.c-ch').textContent = label(r[1]);
      a.querySelector('.c-rule i').style.width = pct + '%';
      li.appendChild(a);
      list.appendChild(li);
    });
    sec.hidden = !list.children.length;
  }

  /* The offline chip on each tile. What it says is what this device holds:
   * "Download · 2.2 MB", "Update · 3 files", "Stored · Remove", or the
   * progress of a download under way. The separate "Read offline" list that
   * repeated the four books under the shelf is gone (NAV-13). */
  function chip(btn) {
    var slug = btn.getAttribute('data-offline');
    var tile = btn.closest('.book');
    var name = tile ? (tile.querySelector('h2') || tile).textContent.trim() : slug;
    var man = null;

    function set(text, aria, disabled) {
      btn.textContent = text;
      if (aria) btn.setAttribute('aria-label', aria); else btn.removeAttribute('aria-label');
      btn.disabled = !!disabled;
      btn.hidden = false;
    }

    async function paint() {
      var res = await resident(slug);
      if (!man) {
        /* offline and never fetched the manifest: say only what is known */
        if (res && res.complete) {
          set('Stored · Remove', 'Remove ' + name + ' from this device');
          btn.onclick = wipe;
        } else { btn.hidden = true; }
        return;
      }
      var stale = res && res.files
        ? Object.keys(man.files).filter(function (p) { return res.files[p] !== man.files[p]; })
        : Object.keys(man.files);
      if (res && res.complete && !stale.length) {
        set('Stored · Remove', 'Remove ' + name + ' from this device (' + mb(man.bytes) + ')');
        btn.onclick = wipe;
      } else if (res && stale.length && stale.length < Object.keys(man.files).length) {
        set('Update · ' + stale.length + (stale.length === 1 ? ' file' : ' files'),
            'Update the stored copy of ' + name + ': ' + stale.length +
            (stale.length === 1 ? ' file' : ' files') + ' changed');
        btn.onclick = pull;
      } else {
        /* Both numbers, deliberately. They differ by more than tenfold, and
         * quoting only the small one would be a way of not telling the reader
         * what they are agreeing to. */
        set('Download · ' + mb(man.wire),
            'Download ' + name + ' to read offline: about ' + mb(man.wire) +
            ' to fetch, ' + mb(man.bytes) + ' stored');
        btn.onclick = pull;
      }
    }

    async function pull() {
      set('Downloading · 0%', null, true);
      try {
        var r = await download(slug, function (done, total) {
          btn.textContent = 'Downloading · ' + Math.floor(100 * done / total) + '%';
        });
        if (r.failed) {
          toast(r.failed + ' file' + (r.failed === 1 ? '' : 's') + ' of ' + name +
                ' could not be fetched. Try again to finish.');
        }
      } catch (err) {
        toast((err && err.name === 'QuotaExceededError')
          ? 'Not enough room on this device for ' + name + '. What downloaded is kept.'
          : 'The download of ' + name + ' was interrupted. Try again to resume.');
      }
      await paint();
      storeLine();
    }

    async function wipe() {
      if (!confirm('Remove ' + name + ' from this device? You can download it again.')) return;
      btn.disabled = true;
      await removeBook(slug);
      await paint();
      storeLine();
    }

    fetch(slug + '/offline.json').then(function (r) { return r.json(); })
      .then(function (m) { man = m; }, function () { /* offline: paint what is known */ })
      .then(paint);
  }

  /* One quiet line under the grid: what the library uses on this device,
   * the Reset that is the reader's only recovery from a worker gone bad
   * (behind a confirmation, and visibly not a peer of Download), and a
   * Delete for any book that has left the library but not this device. */
  var storeBusy = false;
  function storeLine() {
    var p = document.querySelector('p[data-store]');
    if (!p || storeBusy) return;
    storeBusy = true;
    usage().then(function (u) {
      storeBusy = false;
      p.textContent = '';
      if (u && u.usage) {
        p.appendChild(document.createTextNode('Using ' + mb(u.usage) +
          (u.quota ? ' of about ' + mb(u.quota) : '') + ' on this device. '));
      }
      var reset = document.createElement('button');
      reset.type = 'button';
      reset.textContent = 'Reset offline data';
      reset.onclick = function () {
        if (confirm('Remove every downloaded book and reset the offline store?'))
          window.LibraryPWA.reset();
      };
      p.appendChild(reset);
      (state.orphans || []).forEach(function (slug) {
        p.appendChild(document.createTextNode(' · '));
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = 'Delete ' + slug + ', no longer in this library';
        b.onclick = async function () {
          await removeBook(slug);
          state.orphans = (state.orphans || []).filter(function (s) { return s !== slug; });
          save(state);
          storeLine();
        };
        p.appendChild(b);
      });
      p.hidden = false;
    });
  }

  function hub() {
    continueStrip();
    if (!('caches' in window)) return;
    document.querySelectorAll('button[data-offline]').forEach(chip);
    storeLine();
    var p = document.querySelector('p[data-store]');
    if (p) {
      /* the coaching card goes after the line, never inside it */
      var host = document.createElement('div');
      p.parentNode.insertBefore(host, p.nextSibling);
      maybeCoach(host);
    }
  }

  if (!SLUG) {
    if (document.readyState === 'loading') addEventListener('DOMContentLoaded', hub);
    else hub();
    /* back from a chapter by the browser's back button: the page may come
     * from the back/forward cache with the strip as it was */
    addEventListener('pageshow', function (e) {
      if (e.persisted) { state = load(); continueStrip(); }
    });
  }

  /* ------------------------------------------------------------ resume
   * A returning reader's place, offered where they arrive in a book
   * (DESIGN.md sections 6 and 7). What the front door does depends on how
   * the book is read, which nav.json carries from book.json "reading":
   *
   *   sequential  the primary becomes "Continue reading" over "1.1 · ...",
   *               and "Begin" moves to the first text link;
   *   reference   the primary stays Contents, and "Continue at 68 · ..."
   *               is the first text link.
   *
   * On the contents page the row is marked "Last read", and a "Jump to where
   * you were" link sits above the first part. The front door's primary is
   * found by the contract, .cta > .btn with .btn-main and .btn-sub, and
   * nothing else about the page is assumed. */
  function resume() {
    var last = (state.lastBy || {})[SLUG];
    if (!NAV || !last || !last.url) return;
    var here = file(location.pathname);
    var text = label(last);

    var btn = document.querySelector('.cta > .btn');
    if (btn && !btn.hasAttribute('data-resumed') && file(last.url) !== here) {
      btn.setAttribute('data-resumed', '');
      var firstGo = btn.parentNode.querySelector('.go');
      var go = document.createElement('a');
      go.className = 'go';
      if (NAV.reading === 'sequential') {
        /* the original primary, kept as the first text link */
        var main = btn.querySelector('.btn-main');
        go.setAttribute('href', btn.getAttribute('href'));
        go.textContent = (main ? main.textContent : btn.textContent).trim();
        if (btn.getAttribute('aria-label')) go.setAttribute('aria-label', btn.getAttribute('aria-label'));
        btn.setAttribute('href', last.url);
        btn.setAttribute('aria-label', 'Continue reading, ' + text);
        btn.innerHTML = '<span class="btn-main">Continue reading</span><span class="btn-sub"></span>';
        btn.querySelector('.btn-sub').textContent = text;
      } else if (NAV.reading === 'reference') {
        go.setAttribute('href', last.url);
        go.textContent = 'Continue at ' + text;
      } else {
        go = null;
      }
      if (go) btn.parentNode.insertBefore(go, firstGo || btn.nextSibling);
    }

    var rows = document.querySelectorAll('.clist li');
    for (var i = 0; i < rows.length; i++) {
      var a = rows[i].querySelector('a[href]');
      if (!a || file(a.getAttribute('href')) !== file(last.url)) continue;
      if (rows[i].hasAttribute('data-last')) break;
      rows[i].setAttribute('data-last', '');
      var tag = document.createElement('span');
      tag.className = 'tag last';
      tag.textContent = 'Last read';
      rows[i].appendChild(tag);
      var part = document.querySelector('h2.part-head');
      var block = part && (part.closest('section') || part);
      if (block && block.parentNode && !document.querySelector('.pwa-jump')) {
        var p = document.createElement('p');
        p.className = 'pwa-jump';
        var j = document.createElement('a');
        j.setAttribute('href', last.url);
        j.setAttribute('aria-label', 'Jump to where you were: ' + text);
        j.textContent = 'Jump to where you were';
        p.appendChild(j);
        block.parentNode.insertBefore(p, block);
      }
      break;
    }
  }

  /* ------------------------------------------------------ chapter navigation
   * One reading order per book, in nav.json, for the one thing only a script
   * with the whole book in view can do: the arrow keys. Everything else about
   * moving through a book is written into the page at build and read from it
   * there (DESIGN.md section 8): the sidebar's up-link and folio row, the
   * chapter foot, and from those, book.js's folio bar and drawer. That is
   * what lets the Dropbox build, which has no nav.json and no pwa.js,
   * navigate the same way.
   *
   *   desktop     the arrow keys, which is what a keyboard is for
   *   phone       book.js's folio bar and drawer
   *   standalone  a back control, because a home-screen app has no browser
   *               chrome to provide one
   *
   * The position ("Chapter 68 of 98") is written into the sidebar at build,
   * and the drawer's kicker copies it; this no longer appends one to either,
   * which printed it twice once the build wrote it. */

  var NAV = null;          /* the book's reading order, once fetched */
  var HERE = -1;           /* this page's index in it, or -1 off-book */

  function file(href) {
    var f = String(href || '').split('/').pop().split('#')[0].split('?')[0];
    try { return decodeURIComponent(f); } catch (e) { return f; }
  }

  function at(i) {
    return NAV && i >= 0 && i < NAV.chapters.length ? NAV.chapters[i] : null;
  }

  function go(c) { if (c) location.href = c.href; }

  /* ---- the drawer row, for an older page
   * book.js builds the prev/next row itself now, from the chapter foot. A
   * stored page whose book.js predates that builds a drawer without one; it
   * gets the row from the reading order here, as it always did, so its
   * drawer keeps its neighbours under this shell. */

  function drawerNav() {
    var panel = document.getElementById('mnav');
    if (!panel || panel.querySelector('.mn-seq')) return;
    if (HERE < 0) return;        /* contents, trials, ledger: in the book but
                                    not in its reading sequence */

    var prev = at(HERE - 1), next = at(HERE + 1);
    if (!prev && !next) return;

    var row = document.createElement('div');
    row.className = 'mn-seq';
    [['prev', prev, 'Previous', 'No previous chapter'],
     ['next', next, 'Next', 'No next chapter']].forEach(function (spec) {
      var c = spec[1];
      /* A span rather than no element at all: the first and last chapters
       * then keep the same two-column shape as every other, so the control a
       * thumb is aiming for does not move between pages. */
      var el = document.createElement(c ? 'a' : 'span');
      el.className = spec[0];
      if (c) el.href = c.href;
      el.innerHTML = '<span class="mn-dir"></span><span class="mn-ch"></span>';
      el.querySelector('.mn-dir').textContent = spec[2];
      el.querySelector('.mn-ch').textContent = c ? label(c) : spec[3];
      row.appendChild(el);
    });

    var list = panel.querySelector('.mn-list');
    if (list) panel.insertBefore(row, list); else panel.appendChild(row);
  }

  /* book.js builds the drawer on DOMContentLoaded. Both scripts are waiting on
   * the same event, so rather than depend on which handler runs first, try
   * once now and once after a frame. */
  function whenDrawer() {
    drawerNav();
    requestAnimationFrame(function () { drawerNav(); });
  }

  /* ---- the keyboard */

  function typing(e) {
    var t = e.target;
    if (!t) return false;
    if (t.isContentEditable) return true;
    return /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName);
  }

  addEventListener('keydown', function (e) {
    if (HERE < 0) return;
    if (e.metaKey || e.ctrlKey || e.altKey || e.shiftKey) return;
    if (typing(e)) return;
    /* an open dialog or drawer owns the keyboard while it is open */
    if (document.querySelector('dialog[open]')) return;
    var btn = document.getElementById('mnav-btn');
    if (btn && btn.getAttribute('aria-expanded') === 'true') return;

    if (e.key === 'ArrowLeft') { go(at(HERE - 1)); }
    else if (e.key === 'ArrowRight') { go(at(HERE + 1)); }
    else return;
    e.preventDefault();
  });

  /* ---- standalone back
   * The stylesheet used to say that no navigation needed injecting here,
   * because the top bar already carries Library and Chapters. That is true of
   * reaching a place and false of coming back from one: a reader who followed a
   * cross-reference three chapters deep has nothing to return along, and in a
   * home-screen app there is no browser chrome to do it for them. */

  function backControl() {
    if (!isStandalone()) return;
    var bar = document.querySelector('.topnav');
    if (!bar || bar.querySelector('.pwa-back')) return;
    if (history.length <= 1) return;

    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pwa-back';
    b.setAttribute('aria-label', 'Back');
    b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" width="18" height="18">'
      + '<path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2"'
      + ' stroke-linecap="round" stroke-linejoin="round"/></svg>';
    b.onclick = function () { history.back(); };
    bar.insertBefore(b, bar.firstChild);
  }

  async function chapterNav() {
    if (!SLUG) return;
    try { NAV = await (await fetch('nav.json')).json(); }
    catch (e) { return; }                    /* not a chaptered book, or offline
                                                before the book was downloaded */
    if (!NAV || !NAV.chapters || !NAV.chapters.length) { NAV = null; return; }

    var here = file(location.pathname);
    for (var i = 0; i < NAV.chapters.length; i++) {
      if (file(NAV.chapters[i].href) === here) { HERE = i; break; }
    }
    /* A chapter is a place in the book: record it now, before any scroll. */
    if (HERE >= 0) { recordPlace(scrollPct()); save(state); }
    if (document.readyState === 'loading') addEventListener('DOMContentLoaded', resume);
    else resume();
    /* Not gated on HERE. The prev/next row is meaningless on the contents
     * page or the trial registry, and drawerNav() declines to draw it there
     * itself. The book's destinations are not repeated in the drawer: the bar
     * carries them, under Menu on a phone (NAV-07). */
    if (document.readyState === 'loading') {
      addEventListener('DOMContentLoaded', whenDrawer);
    } else {
      whenDrawer();
    }
  }

  /* The back control does not depend on the reading order, and used to be
   * called from inside the fetch that loads one. So the two books that have no
   * reading order got no back control -- in a home-screen app, where there is
   * no browser chrome either, the atlas was somewhere a reader could arrive and
   * not leave. It is called here instead, where a book having chapters or not
   * has nothing to do with it. */
  if (SLUG) { backControl(); chapterNav(); }

  /* What the hub uses to draw the shelf. Everything above is generic. */
  window.LibraryPWA = {
    state: state, save: save, root: ROOT, slug: SLUG,
    /* Where this page sits in its book, once the reading order has arrived.
     * The arrow keys do nothing until it has, which is one cached fetch of a
     * few kilobytes; this is how a test waits for that rather than sleeping,
     * and how a reader reporting "the keys did nothing" can be answered. */
    nav: function () {
      return { ready: !!NAV, index: HERE, count: NAV ? NAV.count : 0 };
    },
    download: download, resident: resident, removeBook: removeBook,
    usage: usage, mb: mb, toast: toast, coach: maybeCoach,
    standalone: isStandalone, ios: isIOS,
    reset: async function () {
      if ('serviceWorker' in navigator) {
        var rs = await navigator.serviceWorker.getRegistrations();
        for (var i = 0; i < rs.length; i++) await rs[i].unregister();
      }
      for (var k of await caches.keys()) if (k.startsWith('lib:')) await caches.delete(k);
      location.reload();
    }
  };
})();
