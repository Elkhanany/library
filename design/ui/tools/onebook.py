#!/usr/bin/env python3
"""Rebuild ONE book's pages into docs/<slug>/ (5-6 minutes for the clinical book, less for others),
then re-run the nav and app-layer passes over the whole site. Use after changing webbuild.SHELL,
build.py, or a book's src/ fragments. The hub (docs/index.html) is not rebuilt here; hub changes
need the full `python3 tools/webbuild.py`.

    python3 onebook.py <slug>
"""
import os, sys, asyncio
ROOT = '/home/user/library'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import library, webbuild, nav, pwa
from playwright.async_api import async_playwright
slug = sys.argv[1]
bk = next(b for b in library.books() if b.slug == slug)
async def main():
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        n, stats = await webbuild.build_book(bk, br)
        await br.close()
    print(f'{slug}: {n} chapters')
asyncio.run(main())
import shutil; shutil.rmtree(webbuild.STAGE, ignore_errors=True)
books = list(library.books())
print('bar on', nav.emit_all(books), 'pages; app layer on', pwa.emit_all(books), 'pages')
