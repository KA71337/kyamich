"""Independent production QA. No runtime dependencies; artifacts stay in TEMP."""
import json, os, time
from pathlib import Path
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright
OUT = Path(os.environ['TEMP']) / 'kyamich-final-qa'
OUT.mkdir(exist_ok=True)
BASE = 'http://127.0.0.1:3000'
report = {'viewports': [], 'external': [], 'seo': [], 'errors': [], 'warnings': []}
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    for width, height in [(320,812),(375,812),(768,1024),(1440,900),(1920,1080)]:
        page = browser.new_page(viewport={'width':width,'height':height}, device_scale_factor=1)
        page.on('pageerror', lambda e: report['errors'].append(str(e)))
        page.on('console', lambda m: report['errors'].append(m.text) if m.type=='error' else report['warnings'].append(m.text) if m.type=='warning' else None)
        page.on('response', lambda r: report['errors'].append(f'HTTP {r.status}: {r.url}') if r.status>=400 else None)
        page.add_init_script("""window.qaPerf={lcp:0,cls:0};new PerformanceObserver(l=>{for(const e of l.getEntries())window.qaPerf.lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});new PerformanceObserver(l=>{for(const e of l.getEntries())if(!e.hadRecentInput)window.qaPerf.cls+=e.value}).observe({type:'layout-shift',buffered:true});""")
        response = page.goto(BASE,wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        page.wait_for_timeout(750)
        perf = page.evaluate("""() => ({...window.qaPerf, navigation:performance.getEntriesByType('navigation').map(n=>({ttfb:n.responseStart,domContentLoaded:n.domContentLoadedEventEnd,load:n.loadEventEnd})), resources:performance.getEntriesByType('resource').map(r=>({url:r.name,type:r.initiatorType,transfer:r.transferSize,encoded:r.encodedBodySize,duration:r.duration}))})""")
        page.screenshot(path=str(OUT/f'hero-{width}.png'),animations='disabled')
        # Actually visit the whole page; allow lazy images and reveals to settle.
        page.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,100));}scrollTo({top:0,behavior:'instant'});}")
        page.wait_for_timeout(700)
        result = page.evaluate("""() => ({width:innerWidth, scrollWidth:document.documentElement.scrollWidth, h1:document.querySelectorAll('h1').length,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),images:[...document.images].map(i=>({src:i.currentSrc,width:i.naturalWidth,loading:i.loading})), missingAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.querySelector(a.getAttribute('href'))).map(a=>a.href), lang:document.documentElement.lang, canonical:document.querySelector('link[rel=canonical]').href, description:document.querySelector('meta[name=description]').content, ogLocale:document.querySelector('meta[property="og:locale"]').content, schema:JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent), temporary:/lorem ipsum|TODO|coming soon|paylaşılacaq/i.test(document.body.innerText),smallTargets:[...document.querySelectorAll('a,button')].filter(e=>{let r=e.getBoundingClientRect();return r.width&&r.height&&r.height<24}).map(e=>({text:e.textContent.trim(),height:e.getBoundingClientRect().height}))})""")
        assert response.status==200 and result['scrollWidth']==width and result['h1']==1 and not result['brokenImages'] and not result['missingAnchors'] and not result['temporary'],result
        assert result['lang']=='az' and result['canonical']=='https://kyamich.dev/' and result['ogLocale']=='az_AZ',result
        page.screenshot(path=str(OUT/f'full-{width}.png'),full_page=True,animations='disabled')
        # Keyboard starts with visible skip link and lands in main content.
        page.evaluate('document.activeElement.blur();scrollTo({top:0,behavior:"instant"})')
        page.keyboard.press('Tab')
        assert page.locator('.skip-link').evaluate('e=>e===document.activeElement'), 'skip link not first'
        assert page.locator('.skip-link').evaluate('e=>e.getBoundingClientRect().top>=0'), 'skip link invisible'
        page.keyboard.press('Enter')
        page.keyboard.press('Tab')
        assert page.locator('.hero-actions a').first.evaluate('e=>e===document.activeElement'), 'skip link does not skip header'
        focus = page.locator('.hero-actions a').first.evaluate('e=>({style:getComputedStyle(e).outlineStyle,color:getComputedStyle(e).outlineColor})')
        assert focus['style']!='none',focus
        result['focus']=focus
        page.locator('.pricing a').focus()
        page.keyboard.press('Tab')
        page.keyboard.press('Shift+Tab')
        pricing_focus=page.locator('.pricing a').evaluate('e=>({style:getComputedStyle(e).outlineStyle,color:getComputedStyle(e).outlineColor})')
        assert pricing_focus['style']!='none' and pricing_focus['color']=='rgb(20, 22, 21)',pricing_focus
        result['pricingFocus']=pricing_focus
        # Both main CTAs must actually reach their target.
        for selector, anchor in [('.hero-actions a:first-child','#elaqe'),('.hero-actions a:last-child','#isler')]:
            page.locator(selector).click()
            page.wait_for_timeout(1000)
            assert page.url.endswith(anchor),page.url
            top=page.locator(anchor).evaluate('e=>e.getBoundingClientRect().top')
            assert 60<=top<height,(anchor,top)
        page.evaluate('scrollTo({top:0,behavior:"instant"})')
        if width<800:
            button=page.locator('.menu-toggle')
            button.click()
            nav=page.get_by_role('navigation',name='Mobil naviqasiya')
            assert nav.is_visible()
            assert nav.locator('a').first.evaluate('e=>e===document.activeElement')
            assert page.evaluate('document.body.style.overflow')=='hidden'
            page.keyboard.press('Shift+Tab')
            assert button.evaluate('e=>e===document.activeElement')
            page.keyboard.press('Shift+Tab')
            assert nav.locator('a').last.evaluate('e=>e===document.activeElement')
            page.keyboard.press('Tab')
            assert button.evaluate('e=>e===document.activeElement')
            page.keyboard.press('Escape')
            assert button.get_attribute('aria-expanded')=='false' and button.evaluate('e=>e===document.activeElement')
            assert page.evaluate('document.body.style.overflow')!='hidden'
            button.click()
            nav.get_by_role('link',name='Xidmətlər').click()
            assert button.get_attribute('aria-expanded')=='false'
            button.click()
            page.screenshot(path=str(OUT/f'menu-{width}.png'))
            page.set_viewport_size({'width':1024,'height':height})
            assert button.get_attribute('aria-expanded')=='false'
            assert page.evaluate('document.body.style.overflow')!='hidden'
            page.set_viewport_size({'width':width,'height':height})
        # Run genuine axe-core, with WCAG 2 A/AA and 2.1 A/AA rules.
        try:
            axe=page.request.get('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js',timeout=30000)
            assert axe.status==200
            page.add_script_tag(content=axe.text())
            a=page.evaluate("async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}})")
            result['axe']={'version':a['testEngine']['version'],'violations':a['violations'],'incomplete':a['incomplete'],'passes':len(a['passes'])}
        except Exception as e:
            result['axe_unavailable']=str(e)
        result['performance']=perf
        report['viewports'].append(result)
        print('VIEWPORT',width,'PASS','axe violations',len(result.get('axe',{}).get('violations',[])),flush=True)
        page.close()
    page=browser.new_page(viewport={'width':375,'height':812},reduced_motion='reduce')
    page.goto(BASE,wait_until='networkidle')
    assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
    assert page.locator('.hero-main-window').evaluate('e=>getComputedStyle(e).transform')=='none'
    assert page.evaluate('document.getAnimations().length')==0
    report['reducedMotion']='PASS'
    for route in ['/robots.txt','/sitemap.xml','/opengraph-image','/icon.svg']:
        r=page.request.get(BASE+route)
        assert r.status==200
        report['seo'].append({'route':route,'status':r.status,'type':r.headers.get('content-type'),'bytes':len(r.body()),'text':r.text() if route.endswith(('.txt','.xml')) else None})
    for url in ['https://nerjmetal.com/','https://talsanpower.com/','https://www.ayvatech.az/','https://github.com/KA71337']:
        external=browser.new_page()
        try:
            r=external.goto(url,wait_until='domcontentloaded',timeout=45000)
            external.wait_for_timeout(2000)
            external.screenshot(path=str(OUT/('external-'+url.split('/')[2]+'.png')))
            report['external'].append({'requested':url,'final':external.url,'status':r.status,'title':external.title()})
        except Exception as e: report['external'].append({'requested':url,'error':str(e)})
        external.close()
    nojs=browser.new_page(java_script_enabled=False,viewport={'width':375,'height':812})
    nojs.goto(BASE,wait_until='networkidle')
    report['noJS']={'mainVisible':nojs.locator('main').is_visible(),'projects':nojs.locator('.project-visual').count(),'contactVisible':nojs.locator('#elaqe').is_visible()}
    browser.close()
# Save actual measurements without inventing lab scores.
(OUT/'results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for kind in ['hero','full']:
    thumbs=[]
    for w in [320,375,768,1440,1920]:
        im=Image.open(OUT/f'{kind}-{w}.png').convert('RGB')
        target=400 if kind=='hero' else 340
        im=im.resize((target,round(im.height*target/im.width)))
        canvas=Image.new('RGB',(target,im.height+35),'#303530');ImageDraw.Draw(canvas).text((10,10),f'{kind.upper()} {w}px',fill='white');canvas.paste(im,(0,35));thumbs.append(canvas)
    sheet=Image.new('RGB',(sum(i.width for i in thumbs),max(i.height for i in thumbs)),'#303530')
    x=0
    for im in thumbs:sheet.paste(im,(x,0));x+=im.width
    sheet.save(OUT/f'{kind}-review.jpg',quality=92)
# Readable complete section contact sheets for each width.
for w in [320,375,768,1440,1920]:
    im=Image.open(OUT/f'full-{w}.png').convert('RGB')
    tilew=600
    im=im.resize((tilew,round(im.height*tilew/im.width)))
    slices=[im.crop((0,y,tilew,min(y+900,im.height))) for y in range(0,im.height,900)]
    sheet=Image.new('RGB',(tilew*len(slices),935),'#303530')
    d=ImageDraw.Draw(sheet)
    for i,tile in enumerate(slices):d.text((i*tilew+8,10),f'{w}px / section slice {i+1}',fill='white');sheet.paste(tile,(i*tilew,35))
    sheet.save(OUT/f'sections-{w}.jpg',quality=94)
print('RESULTS',OUT,flush=True)
print('ERRORS',report['errors'],flush=True)
