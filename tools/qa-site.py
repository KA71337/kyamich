"""Local production QA; uses the isolated research Playwright install, not runtime dependencies."""
import json, os
from pathlib import Path
from playwright.sync_api import sync_playwright
OUT = Path(os.environ['TEMP']) / 'kyamich-qa'
OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    errors = []
    for width in [320, 375, 390, 768, 1024, 1440, 1920]:
        page = browser.new_page(viewport={'width': width, 'height': 1000})
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
        response = page.goto('http://127.0.0.1:3000', wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        page.evaluate("async () => { for(let y=0;y<document.body.scrollHeight;y+=700){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,70));} window.scrollTo(0,0); }")
        page.wait_for_timeout(500)
        result = page.evaluate("""() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.querySelector(a.getAttribute('href'))).map(a=>a.href),projects:[...document.querySelectorAll('.project-visual')].map(a=>a.href),fonts:document.fonts.check('400 16px "Manrope Variable"')})""")
        assert response.status == 200, response.status
        assert result['scrollWidth'] == width, result
        assert result['h1'] == 1 and not result['brokenImages'] and not result['missingAnchors'], result
        if width < 800:
            button = page.get_by_role('button', name='Menyunu aç')
            button.click()
            assert page.get_by_role('navigation', name='Mobil naviqasiya').is_visible()
            page.keyboard.press('Escape')
            assert button.get_attribute('aria-expanded') == 'false'
            assert button.evaluate('(el)=>el===document.activeElement')
            button.click()
            page.get_by_role('navigation', name='Mobil naviqasiya').get_by_role('link', name='Xidmətlər').click()
            assert button.get_attribute('aria-expanded') == 'false'
            page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
        page.screenshot(path=str(OUT/f'desktop-{width}.png'), full_page=True, animations='disabled')
        print('VIEWPORT', json.dumps(result))
        page.close()
    page = browser.new_page(viewport={'width':375,'height':812}, reduced_motion='reduce')
    page.goto('http://127.0.0.1:3000',wait_until='networkidle')
    assert page.evaluate("getComputedStyle(document.documentElement).scrollBehavior") == 'auto'
    assert page.locator('.hero-main-window').evaluate("el=>getComputedStyle(el).transform") == 'none'
    print('REDUCED_MOTION PASS')
    for route in ['/robots.txt','/sitemap.xml','/opengraph-image','/icon.svg']:
        response = page.request.get('http://127.0.0.1:3000'+route)
        assert response.status == 200, (route,response.status)
        print('SEO',route,response.status,response.headers.get('content-type'))
    assert not errors, errors
    print('CONSOLE_ERRORS',json.dumps(errors))
    print('QA_SCREENSHOTS',str(OUT))
    browser.close()
