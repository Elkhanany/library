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

  /* ------------------------------------------------------------- the shelf
   * Rendered here rather than emitted by the build, because every word of it
   * is live: what is stored, how far a download has got, what a rebuild has
   * changed underneath it. A server-rendered shelf would be wrong the moment
   * it was painted. Only ever drawn on the hub. */

  async function shelf() {
    var host = document.querySelector('.wrap');
    if (!host || SLUG) return;

    var cat;
    try { cat = await (await fetch('catalog.json')).json(); }
    catch (e) { return; }                    /* no catalogue, no shelf */

    var sec = document.createElement('section');
    sec.className = 'pwa-shelf';
    sec.innerHTML = '<h2>Read offline</h2>';

    for (var i = 0; i < (cat.books || []).length; i++) {
      sec.appendChild(await row(cat.books[i]));
    }

    /* Books that have left the library but whose bytes are still here. */
    (state.orphans || []).forEach(function (slug) {
      var d = document.createElement('div');
      d.className = 'pwa-row';
      var n = document.createElement('div'); n.className = 'n';
      n.innerHTML = '<b>' + slug + '</b><span>No longer in this library — still on this device</span>';
      var b = document.createElement('button');
      b.textContent = 'Delete';
      b.onclick = async function () {
        await removeBook(slug);
        state.orphans = (state.orphans || []).filter(function (s) { return s !== slug; });
        save(state); d.remove();
      };
      d.appendChild(n); d.appendChild(b); sec.appendChild(d);
    });

    var note = document.createElement('p');
    note.className = 'pwa-note';
    sec.appendChild(note);
    usage().then(function (u) {
      if (!u || !u.usage) return;
      note.textContent = 'Using ' + mb(u.usage) +
        (u.quota ? ' of about ' + mb(u.quota) + ' available' : '') + ' on this device.';
    });

    /* Quiet, and behind a confirmation. It is the only user-side recovery from
     * a worker that has gone bad, so it has to be here -- but it throws away
     * every download, so it must not sit next to Download looking like a peer. */
    var reset = document.createElement('button');
    reset.className = 'quiet';
    reset.textContent = 'Reset offline data';
    reset.onclick = function () {
      if (confirm('Remove every downloaded book and reset the offline store?'))
        window.LibraryPWA.reset();
    };
    note.appendChild(document.createTextNode(' '));
    note.appendChild(reset);

    var foot = host.querySelector('footer');
    if (foot) host.insertBefore(sec, foot); else host.appendChild(sec);
    maybeCoach(sec);
  }

  async function row(book) {
    var d = document.createElement('div');
    d.className = 'pwa-row';
    var n = document.createElement('div'); n.className = 'n';
    var title = document.createElement('b'); title.textContent = book.name;
    var sub = document.createElement('span');
    n.appendChild(title); n.appendChild(sub);

    var btn = document.createElement('button');
    var bar = document.createElement('progress');
    bar.max = 1; bar.value = 0; bar.hidden = true;

    d.appendChild(n); d.appendChild(bar); d.appendChild(btn);

    var man = null;
    try { man = await (await fetch(book.slug + '/offline.json')).json(); }
    catch (e) { /* offline and never downloaded: leave the row informational */ }

    async function paint() {
      var res = await resident(book.slug);
      if (!man) {
        sub.textContent = res && res.complete ? 'Stored on this device' : 'Unavailable offline';
        btn.hidden = !(res && res.complete);
        btn.textContent = 'Remove';
        btn.onclick = wipe;
        return;
      }
      var stale = res && res.files
        ? Object.keys(man.files).filter(function (p) { return res.files[p] !== man.files[p]; })
        : Object.keys(man.files);

      if (res && res.complete && !stale.length) {
        sub.textContent = 'Stored — ' + man.count + ' files, ' + mb(man.bytes);
        btn.textContent = 'Remove'; btn.onclick = wipe;
      } else if (res && stale.length && stale.length < Object.keys(man.files).length) {
        sub.textContent = 'Updated — ' + stale.length +
          (stale.length === 1 ? ' file' : ' files') + ' changed';
        btn.textContent = 'Update'; btn.onclick = pull;
      } else {
        /* Both numbers, deliberately. They differ by more than tenfold, and
         * quoting only the small one would be a way of not telling the reader
         * what they are agreeing to. */
        sub.textContent = 'About ' + mb(man.wire) + ' to download, ' +
                          mb(man.bytes) + ' stored';
        btn.textContent = 'Download'; btn.onclick = pull;
      }
      btn.hidden = false; btn.disabled = false;
    }

    async function pull() {
      btn.disabled = true; btn.textContent = 'Downloading…';
      bar.hidden = false;
      try {
        var r = await download(book.slug, function (done, total) {
          bar.value = done / total;
          sub.textContent = done + ' of ' + total + ' files';
        });
        bar.hidden = true;
        if (r.failed) {
          sub.textContent = r.failed + ' file' + (r.failed === 1 ? '' : 's') +
            ' could not be fetched — try again to finish';
        }
      } catch (err) {
        bar.hidden = true;
        sub.textContent = (err && err.name === 'QuotaExceededError')
          ? 'Not enough room on this device — what downloaded is kept'
          : 'Download interrupted — try again to resume';
      }
      await paint();
    }

    async function wipe() {
      btn.disabled = true;
      await removeBook(book.slug);
      await paint();
    }

    await paint();
    return d;
  }

  if (!SLUG) addEventListener('DOMContentLoaded', function () { shelf(); });

  /* ------------------------------------------------------ chapter navigation
   * One reading order per book, in nav.json, and one set of controls over it,
   * so the two chaptered books navigate identically instead of merely looking
   * alike. Everything here is additive: with the file missing, the fetch
   * failing, or JavaScript off, every page still carries the top bar, the
   * section sidebar and the prev/next pair at the foot of the chapter that it
   * carried before.
   *
   * Three surfaces, because a book is read on three:
   *
   *   desktop     the arrow keys, which is what a keyboard is for
   *   phone       prev/next inside the drawer, reachable without scrolling
   *               past the chapter to find them
   *   standalone  a back control, because a home-screen app has no browser
   *               chrome to provide one
   *
   * The drawer is book.js's, built from the chapter's own H2s. This adds a row
   * to it rather than building a second one, so a reader has one drawer with
   * everything in it and not two that each know half. */

  var NAV = null;          /* the book's reading order, once fetched */
  var HERE = -1;           /* this page's index in it, or -1 off-book */

  function file(href) {
    var f = String(href || '').split('/').pop().split('#')[0].split('?')[0];
    try { return decodeURIComponent(f); } catch (e) { return f; }
  }

  function at(i) {
    return NAV && i >= 0 && i < NAV.chapters.length ? NAV.chapters[i] : null;
  }

  /* "57 · Metastatic triple-positive disease". The number is the one the
   * contents page shows, which in the physics book is "2.1" and in the clinical
   * book is "57", and neither is the index. */
  function label(c) { return c.num + ' · ' + c.title; }

  function go(c) { if (c) location.href = c.href; }

  /* ---- the drawer row */

  function drawerNav() {
    var panel = document.getElementById('mnav');
    if (!panel || panel.querySelector('.mn-seq')) return;
    if (HERE < 0) return;        /* contents, trials, ledger: in the book but
                                    not in its reading sequence */

    var prev = at(HERE - 1), next = at(HERE + 1);
    if (!prev && !next) return;

    var row = document.createElement('div');
    row.className = 'mn-seq';
    [['prev', prev, 'Previous'], ['next', next, 'Next']].forEach(function (spec) {
      var c = spec[1];
      /* A disabled span rather than no element at all: the first and last
       * chapters then keep the same two-column shape as every other, so the
       * control a thumb is aiming for does not move between pages. */
      var el = document.createElement(c ? 'a' : 'span');
      el.className = spec[0];
      if (c) el.href = c.href;
      el.innerHTML = '<span class="mn-dir"></span><span class="mn-ch"></span>';
      el.querySelector('.mn-dir').textContent = spec[2];
      el.querySelector('.mn-ch').textContent = c ? label(c) : '—';
      row.appendChild(el);
    });

    var list = panel.querySelector('.mn-list');
    if (list) panel.insertBefore(row, list); else panel.appendChild(row);

    /* Where in the book this is. The drawer already names the chapter; this
     * says how much of the book is behind and ahead of it, which is the thing
     * a contents page makes you leave the chapter to find out. */
    var k = panel.querySelector('.mn-kicker');
    if (k && HERE >= 0) k.textContent = k.textContent + ' · ' + (HERE + 1) + ' of ' + NAV.count;
  }

  /* ---- the destinations
   * The same links the top bar carries, in the drawer that is the whole of the
   * navigation on a phone. book.js gives the drawer one way out of the chapter,
   * "All chapters", because that is the only one a file:// build can know
   * about. A book with a trial registry and a stories index has three more, and
   * a reader holding a phone had to scroll back to the top of a five-thousand
   * word chapter to reach any of them.
   *
   * Taken from nav.json rather than read off the bar in the page, so it is the
   * same list on a chapter whose bar has scrolled away, in an installed app
   * with no browser chrome, and offline. */

  function drawerLinks() {
    var panel = document.getElementById('mnav');
    if (!panel || panel.querySelector('.mn-dest')) return;
    if (!NAV || !NAV.links || NAV.links.length < 2) return;

    var here = file(location.pathname);
    var box = document.createElement('div');
    box.className = 'mn-dest';
    NAV.links.forEach(function (item) {
      /* The page you are on is not somewhere to go. It stays in the list, so
       * the list is the same shape on every page, and stops being a control. */
      var on = file(item.href) === here;
      var el = document.createElement(on ? 'span' : 'a');
      if (!on) el.href = item.href;
      else el.setAttribute('aria-current', 'page');
      if (item.key === 'library') el.className = 'up';
      el.textContent = item.label;
      box.appendChild(el);
    });

    var foot = panel.querySelector('.mn-foot');
    if (foot) {
      panel.insertBefore(box, foot);
      /* book.js's "All chapters" is now the first entry of this list. Two
       * controls to the same page, one above the other, is worse than either. */
      var back = foot.querySelector('a');
      if (back) back.remove();
    } else {
      panel.appendChild(box);
    }
  }

  /* The same fact on the other surface. The sidebar is the desktop drawer and
   * already names the chapter; without this, position is something only a
   * phone reader is told. */
  function sidebarPosition() {
    var t = document.querySelector('.sidebar .sb-title');
    if (!t || HERE < 0 || t.dataset.pos) return;
    t.dataset.pos = '1';
    t.textContent = t.textContent + ' · ' + (HERE + 1) + ' of ' + NAV.count;
  }

  /* book.js builds the drawer on DOMContentLoaded and only when the chapter has
   * at least two H2s to list. Both scripts are waiting on the same event, so
   * rather than depend on which handler runs first, try once now and once after
   * a frame. */
  function whenDrawer() {
    drawerLinks();
    drawerNav();
    sidebarPosition();
    requestAnimationFrame(function () { drawerLinks(); drawerNav(); });
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
    /* Not gated on HERE. The prev/next row and the position are meaningless on
     * the contents page or the trial registry, and drawerNav() declines to
     * draw them there; the destinations are exactly as useful on those pages as
     * in a chapter, and returning early used to take them away. */
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
