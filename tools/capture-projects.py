"""Research only: capture live portfolio references without implementing the site."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'projects'
OUT.mkdir(parents=True, exist_ok=True)
SITES = [('nerj-metal', 'https://nerjmetal.com/'), ('talsan-power', 'https://talsanpower.com/'), ('ayva-tech', 'https://www.ayvatech.az/')]

def inspect(page):
    return page.evaluate('''() => ({url:location.href,title:document.title,lang:document.documentElement.lang,description:document.querySelector('meta[name="description"]')?.content,headings:[...document.querySelectorAll('h1,h2,h3')].map(e=>e.textContent.trim()),links:[...document.querySelectorAll('a[href]')].map(a=>({text:a.textContent.trim(),href:a.href})).filter((a,i,x)=>x.findIndex(b=>b.href===a.href)===i),scripts:[...document.scripts].map(s=>s.src).filter(Boolean),styles:[...document.querySelectorAll('link[rel="stylesheet"]')].map(e=>e.href),fonts:[...new Set([...document.querySelectorAll('h1,h2,p')].map(e=>getComputedStyle(e).fontFamily))],images:[...document.images].map(i=>({src:i.currentSrc,alt:i.alt,loaded:i.complete&&i.naturalWidth>0})),text:document.body.innerText.slice(0,18000),nextEvidence:typeof window.next!=='undefined'||!!window.__next_f})''')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    for slug, url in SITES:
        context = browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=2)
        page = context.new_page()
        errors=[]
        page.on('pageerror',lambda e: errors.append(str(e)))
        try:
            response=page.goto(url,wait_until='domcontentloaded',timeout=60000)
            page.wait_for_load_state('load',timeout=30000)
            page.evaluate('document.fonts.ready')
            page.wait_for_timeout(2200)
            for y in range(0,min(page.evaluate('document.body.scrollHeight'),18000),700):
                page.evaluate('(y)=>window.scrollTo(0,y)',y)
                page.wait_for_timeout(90)
            page.evaluate('window.scrollTo(0,0)')
            page.wait_for_timeout(900)
            evidence=inspect(page)
            evidence.update(slug=slug,status=response.status,headers={k:v for k,v in response.headers.items() if k in ['server','x-powered-by','content-type']},errors=errors)
            for kind, full in [('desktop',False),('full',True)]:
                target=OUT/f'{slug}-{kind}.png'
                page.screenshot(path=str(target),full_page=full,animations='disabled',timeout=60000)
                with Image.open(target) as im:
                    if full:
                        im.thumbnail((2880,16000))
                    im.convert('RGB').save(OUT/f'{slug}-{kind}.webp','WEBP',quality=88,method=6)
                    if not full:
                        im.thumbnail((1440,1000))
                        im.convert('RGB').save(OUT/f'{slug}-cover.webp','WEBP',quality=88,method=6)
            page.set_viewport_size({'width':390,'height':844})
            page.evaluate('window.scrollTo(0,0)')
            page.wait_for_timeout(1000)
            target=OUT/f'{slug}-mobile.png'
            page.screenshot(path=str(target),animations='disabled')
            with Image.open(target) as im:
                im.convert('RGB').save(target.with_suffix('.webp'),'WEBP',quality=88,method=6)
            print('SITE_EVIDENCE '+json.dumps(evidence,ensure_ascii=True),flush=True)
            for route in ({'nerj-metal':['/catalog','/contact'],'talsan-power':['/services','/contacts'],'ayva-tech':['/catalog','/contacts']}[slug]):
                try:
                    r=page.goto(url.rstrip('/')+route,wait_until='domcontentloaded',timeout=30000)
                    page.wait_for_timeout(700)
                    print('ROUTE_EVIDENCE '+json.dumps({'slug':slug,'status':r.status,**inspect(page)},ensure_ascii=True),flush=True)
                except Exception as ex:
                    print('ROUTE_ERROR '+slug+' '+route+' '+str(ex),flush=True)
        except Exception as ex:
            print('SITE_ERROR '+slug+' '+str(ex),flush=True)
        context.close()
    browser.close()
for path in sorted(OUT.glob('*')):
    with Image.open(path) as im:
        print('ASSET '+json.dumps({'path':str(path),'bytes':path.stat().st_size,'width':im.width,'height':im.height}),flush=True)
