"""Compact research verification and a richer real AyvaTech gallery capture."""
import json, os
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public'/'projects'
log=Path(os.environ['TEMP'])/'kyamich-site-research-fixed.log'
for line in log.read_text().splitlines():
    if line.startswith(('SITE_EVIDENCE ','ROUTE_EVIDENCE ')):
        kind,raw=line.split(' ',1)
        d=json.loads(raw)
        print(kind,d['slug'],d['status'],d['url'])
        if kind=='SITE_EVIDENCE':
            print('TECH',json.dumps({'slug':d['slug'],'headers':d.get('headers'),'fonts':d.get('fonts'),'next':d.get('nextEvidence'),'styles':d.get('styles'),'errors':d.get('errors'),'unloadedImages':sum(not i['loaded'] for i in d['images'])}))
        if 'contact' in d['url']:
            print('CONTACT_TEXT',json.dumps(d['text'][:3600]))
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=2)
    page.goto('https://www.ayvatech.az/',wait_until='load')
    page.evaluate('document.fonts.ready')
    page.wait_for_timeout(1800)
    section=page.locator('h2',has_text='Seçilmiş məhsullar').first
    section.evaluate('(el) => window.scrollTo({top: el.getBoundingClientRect().top + window.scrollY - 100, behavior: "instant"})')
    page.wait_for_timeout(2000)
    target=OUT/'ayva-tech-gallery.png'
    page.screenshot(path=str(target),animations='disabled')
    with Image.open(target) as im:
        im.convert('RGB').save(target.with_suffix('.webp'),'WEBP',quality=88,method=6)
        im.thumbnail((1440,1000))
        im.convert('RGB').save(OUT/'ayva-tech-gallery-cover.webp','WEBP',quality=88,method=6)
    browser.close()
for path in sorted(OUT.glob('*.webp')):
    with Image.open(path) as im:
        print('WEBP',path.name,im.size,path.stat().st_size)
