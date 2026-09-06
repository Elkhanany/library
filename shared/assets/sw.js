/* The library's service worker.
 *
 * tools/pwa.py prepends BUILD, FILES, SLUGS and CASUAL to this file and writes
 * the result to docs/sw.js. Edit this source, never the generated copy.
 *
 * Two rules govern everything below, and both come from iOS rather than from
 * taste:
 *
 *   No promise this worker returns may hang. iOS kills a service worker that
 *   sits busy, and a fetch handler that never settles does not fail over to the
 *   network -- it hangs the page instead, which is worse than having no worker
 *   at all. So every network call is raced against a timeout and every cache
 *   read is wrapped, and every path ends in a real Response.
 *
 *   The reader's downloads are not ours to delete. A book's cache is named for
 *   the book and never for a build, so a typo fix in one chapter costs one
 *   fetch rather than orphaning sixty-five megabytes somebody chose to store.
 */

/* elkhanany.github.io is one origin shared with every other Pages project on
 * the account, and Cache Storage is per-origin, so every name is prefixed. A
 * bare 'shell-v1' would collide with a neighbouring repo's worker. */
const SHELL = 'lib:shell:' + BUILD;
const BOOK = slug => 'lib:book:' + slug;

const NAV_TIMEOUT = 8000;
const API_TIMEOUT = 4000;

/* Anything raced against this settles, one way or the other. */
function timeout(ms) {
  return new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms));
}
function net(req, ms) {
  return Promise.race([fetch(req), timeout(ms)]);
}

self.addEventListener('install', e => e.waitUntil((async () => {
  const c = await caches.open(SHELL);
  /* One file at a time, never cache.addAll. addAll is atomic: a single 404 or
   * one quota refusal rejects the whole batch, the install fails, the worker
   * goes redundant and the site silently ends up with no worker at all. A
   * per-file loop degrades to a partial shell instead, which cache-first
   * simply misses past. */
  for (const f of FILES) {
    try {
      const r = await fetch(f, { cache: 'reload' });
      if (!r.ok) continue;
      await c.put(f, r.clone());
      /* The hub is reachable as both index.html and the bare directory. */
      if (f === 'index.html') await c.put('./', r);
    } catch (err) { /* activate will not have it; the network will serve it */ }
  }
  /* No skipWaiting here. Taking over mid-session would prune the previous
   * shell out from under a reader who has a three-megabyte chapter open, and
   * its stylesheet and fonts would vanish. The page asks, on a tap. */
})()));

self.addEventListener('activate', e => e.waitUntil((async () => {
  await self.clients.claim();
  const keep = new Set([SHELL].concat(SLUGS.map(BOOK)));
  const orphans = [];
  for (const k of await caches.keys()) {
    if (!k.startsWith('lib:') || keep.has(k)) continue;
    if (k.startsWith('lib:book:')) {
      /* A book that has left the library. Its cache is NOT deleted: throwing
       * away hundreds of megabytes somebody deliberately downloaded, because
       * an author reordered the shelf, is the wrong default. The hub offers
       * it back to them with a Delete button. */
      orphans.push(k.slice('lib:book:'.length));
      continue;
    }
    await caches.delete(k);          /* superseded shell, and only that */
  }
  for (const c of await self.clients.matchAll()) {
    c.postMessage({ type: 'ORPHANS', slugs: orphans });
  }
})()));

/* Which book, if any, owns a path under /library/. */
function slugOf(url) {
  const parts = url.pathname.split('/').filter(Boolean);
  for (const s of SLUGS) if (parts.indexOf(s) !== -1) return s;
  return null;
}

async function fromAnyCache(req) {
  try {
    return await caches.match(req, { ignoreSearch: true });
  } catch (err) {
    return undefined;
  }
}

/* A casually-visited page is worth keeping, but not without bound. Cache
 * Storage preserves insertion order, so the oldest keys are the front of the
 * list -- an LRU-ish policy with no index to maintain alongside it. A book the
 * reader actually downloaded is never trimmed. */
async function keepBounded(cache, slug) {
  const limit = CASUAL[slug] || 0;
  if (!limit) return;
  try {
    const resident = await cache.match('__resident__');
    if (resident) {
      const r = await resident.json();
      if (r && r.complete) return;
    }
    const keys = (await cache.keys()).filter(k => !k.url.endsWith('__resident__'));
    for (let i = 0; i < keys.length - limit; i++) await cache.delete(keys[i]);
  } catch (err) { /* trimming is housekeeping; never let it break a response */ }
}

self.addEventListener('fetch', e => {
  const req = e.request;

  /* Hand back to the browser entirely. Not respondWith(fetch(req)) -- that
   * would route the request through this worker for no benefit and one more
   * way to hang. */
  if (req.method !== 'GET') return;
  if (req.headers.has('range')) return;   /* Safari's media probe; a cached 200
                                             here breaks playback outright */

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (!url.pathname.startsWith(new URL('./', self.location).pathname)) return;
  if (url.pathname.endsWith('/sw.js')) return;

  const file = url.pathname.split('/').pop() || '';

  /* Small, and the update UI reads them, so they must be fresh when the
   * network allows and present when it does not. */
  if (file === 'catalog.json' || file === 'offline.json' ||
      file.endsWith('.webmanifest')) {
    e.respondWith((async () => {
      try {
        const r = await net(req, API_TIMEOUT);
        if (r && r.ok) {
          const c = await caches.open(SHELL);
          c.put(req, r.clone()).catch(() => {});
          return r;
        }
      } catch (err) { /* fall through */ }
      return (await fromAnyCache(req)) ||
             new Response('{}', { headers: { 'Content-Type': 'application/json' } });
    })());
    return;
  }

  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      const hit = await fromAnyCache(req);
      if (hit) return hit;
      try {
        const r = await net(req, NAV_TIMEOUT);
        if (r && r.ok) {
          const slug = slugOf(url);
          if (slug) {
            const c = await caches.open(BOOK(slug));
            await c.put(req, r.clone());
            keepBounded(c, slug);
          }
          return r;
        }
        if (r) return r;
      } catch (err) { /* offline, or the network is worse than offline */ }
      return (await caches.match('offline.html')) ||
             new Response('<h1>Offline</h1>', {
               status: 503, headers: { 'Content-Type': 'text/html' } });
    })());
    return;
  }

  const d = req.destination;
  if (d === 'style' || d === 'script' || d === 'font' || d === 'image') {
    e.respondWith((async () => {
      const hit = await fromAnyCache(req);
      if (hit) return hit;
      try {
        const r = await net(req, NAV_TIMEOUT);
        if (r && r.ok) {
          const slug = slugOf(url);
          const c = await caches.open(slug ? BOOK(slug) : SHELL);
          c.put(req, r.clone()).catch(() => {});
        }
        return r;
      } catch (err) {
        return new Response('', { status: 504 });
      }
    })());
  }
  /* Everything else: no respondWith, so the browser behaves as if this worker
   * did not exist. */
});

/* Exactly one inbound message. There is deliberately no PRECACHE_BOOK: a
 * sixty-five megabyte download runs in the page, where it can report progress
 * and survive, because iOS terminates a worker that stays busy and there is no
 * Background Fetch to hand it to. */
self.addEventListener('message', e => {
  if (e.data && e.data.type === 'SKIP_WAITING') self.skipWaiting();
});
