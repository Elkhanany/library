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

  /* file:// has no origin a worker can be registered against, and the Dropbox
   * build is opened exactly that way. Leave immediately rather than throwing. */
  if (location.protocol === 'file:') return;

  var KEY = 'library:v1';
  var $ = function (s, r) { return (r || document).querySelector(s); };

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); }
    catch (e) { return {}; }
  }
  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* private mode */ }
  }

  var parts = location.pathname.split('/').filter(Boolean);
  var SLUG = null, ROOT = './';

  /* The book a page belongs to is the directory it sits in, and the hub is the
   * only page with no such directory. Derived from the path rather than stamped
   * into the page, so it cannot go stale. */
  (function () {
    var f = parts[parts.length - 1] || '';
    var isFile = /\.html?$/.test(f);
    var dirs = isFile ? parts.slice(0, -1) : parts.slice();
    /* dirs[0] is the Pages project prefix ("library"); a book adds one more. */
    if (dirs.length >= 2) { SLUG = dirs[dirs.length - 1]; ROOT = '../'; }
  })();

  var state = load();

  /* ---------------------------------------------------------------- theme
   * The inline boot script stamped data-theme before first paint. book.js owns
   * the toggle and writes its own key; rather than editing book.js -- which
   * also ships to the Dropbox build, where a slip would break the toggle on
   * every page at once -- watch the attribute it sets and mirror it. */
  var meta = document.querySelector('meta[name="theme-color"]:not([media])');
  function syncTheme() {
    var t = document.documentElement.getAttribute('data-theme') || 'light';
    if (state.theme !== t) { state.theme = t; save(state); }
    if (meta) {
      var dark = meta.getAttribute('data-dark');
      var light = meta.getAttribute('data-light') || meta.content;
      if (!meta.getAttribute('data-light')) meta.setAttribute('data-light', light);
      if (dark) meta.content = (t === 'dark') ? dark : light;
    }
  }
  new MutationObserver(syncTheme).observe(document.documentElement,
    { attributes: true, attributeFilter: ['data-theme'] });
  syncTheme();

  /* ------------------------------------------------------- reading position
   * Where the reader was, per page, so the hub can offer to continue and a
   * returning reader lands where they left off. Deliberately does not fight a
   * #hash: a link into a specific section must win over a remembered scroll. */
  function pageKey() { return location.pathname; }

  function rememberScroll() {
    if (!SLUG) return;
    var y = window.scrollY || document.documentElement.scrollTop || 0;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    state.pos = state.pos || {};
    state.pos[pageKey()] = { y: y, pct: h > 0 ? Math.round(100 * y / h) : 0 };
    state.last = {
      slug: SLUG, url: pageKey(),
      title: (document.title || '').split('—')[0].trim(),
      at: Date.now()
    };
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
      addEventListener('load', function () {
        requestAnimationFrame(function () { window.scrollTo(0, rec.y); });
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

    navigator.serviceWorker.addEventListener('message', function (e) {
      if (e.data && e.data.type === 'ORPHANS' && e.data.slugs.length) {
        state.orphans = e.data.slugs; save(state);
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

  /* What the hub uses to draw the shelf. Everything above is generic. */
  window.LibraryPWA = {
    state: state, save: save, root: ROOT, slug: SLUG,
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
