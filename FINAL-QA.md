# Independent final production QA

Reviewed the complete 403-line user brief and the existing application, configuration, project data, navigation, animation code and research assets. Tested the real production server, not a mocked page: http://127.0.0.1:3000/.

## Bugs fixed in existing files

- `src/app/page.tsx`: removed the visible future-tense contact placeholder. Now explicitly describes the verified GitHub profile and the lack of a direct contact channel; no phone/email invented. Added `role="group"` to the named hero showcase (axe had marked the unnamed generic role's aria-label for review).
- `src/app/layout.tsx`, `src/app/globals.css`: replaced unpreloaded font CSS imports with Next local-font preloading and metric-adjusted fallback; retained genuine installed Manrope/Space Grotesk latin and latin-ext variable subsets for Azerbaijani glyphs. Initial measured mobile layout shift was 0.158–0.171; final measured CLS is 0 at all five widths.
- `src/app/globals.css`: footer navigation links now have 44px-high touch areas (previously 16.5px). Pricing CTA now has a dark keyboard focus outline on the lime panel instead of an invisible lime-on-lime outline.

## Executed regression checks

`npm run build && npm run typecheck && npm run lint`: PASS after the last application change, no lint warnings. Log: `%TEMP%\postman-shell-term_1792916062924_tpya8zafv.log`.

Independent repeatable script: `tools/final-qa.py` (isolated Python Playwright/Pillow tools, no application dependency additions):

```bat
set "PYTHONPATH=%TEMP%\kyamich-research-tools" && python tools\final-qa.py
```

Final run log: `%TEMP%\postman-shell-term_1792916106554_8kg20a274.log`.

PASS: 320×812, 375×812, 768×1024, 1440×900, 1920×1080. No horizontal overflow, broken images, missing anchors or temporary copy. One H1; AZ language; real cover images loaded. Full-page scroll exercised lazy images/reveals. Hero and full-page screenshots generated for every width and visually reviewed using the browser, including readable mobile and desktop section sheets. Graphite/lime identity, asymmetric project windows and gallery, services, pricing, process, typographic About, final CTA and footer remain consistent. The 320px secondary CTA intentionally wraps to a second row; no clipped text.

Keyboard: first Tab shows skip link; Enter skips header; next Tab reaches hero CTA. Visible focus outlines; main CTAs reach actual contact/projects sections below sticky header. Mobile menu: first-link focus, Shift+Tab/Tab containment, Escape/focus return, scroll lock cleanup, close on link, close on desktop resize. Reduced motion: instant scrolling, no card transform, no running animations. No-JS main, all three projects and contact content remain visible (interactive menu is a JS enhancement).

Genuine axe-core **4.10.3** executed on all five widths with WCAG 2 A/AA and 2.1 A/AA rules: **0 violations** each. Gradient/transformed text still produces `color-contrast` incomplete/manual-review cases, not an exhaustive WCAG certification. Actual palette luminance checks: muted/body 7.63:1; muted/surface 6.83:1; muted heading/body 6.18:1; window bar text 7.95:1; window label 9.97:1; muted on brightest final-CTA gradient 5.04:1; pricing secondary text 8.10:1; dark/lime focus and CTA 15.74:1. Decorative SVG and monogram are hidden from accessibility tree.

External pages freshly opened in real Playwright browser: NERJ METAL, TALSAN POWER, AYVA TECH and GitHub KA71337 all returned **200** with the expected page titles. No submitted forms or third-party business functionality tested.

SEO: canonical https://kyamich.dev/, lang az, OG locale az_AZ, description and truthful Person JSON-LD verified. `/robots.txt`, `/sitemap.xml`, `/opengraph-image`, `/icon.svg` all **200** with correct types. Sitemap/robots point at real domain; social image 1200×630 PNG, 49,368 bytes. No invented biographical facts, ratings or contact details in content/config/schema.

Browser/page/console errors, HTTP failures and warnings: **none** in final local run. Production server log also shows no server errors.

## Measured performance (local, unthrottled Chromium/Edge; not Lighthouse)

| Width | Observed initial LCP | Initial CLS | Resource transfer before scrolling |
|---|---:|---:|---:|
|320|384 ms|0|279,070 B|
|375|108 ms|0|279,070 B|
|768|104 ms|0|280,231 B|
|1440|100 ms|0|318,167 B|
|1920|100 ms|0|331,061 B|

Compressed JS body total: 135,795 B per viewport. These are PerformanceObserver/Navigation/Resource Timing samples taken before QA scrolling and interaction, not field Core Web Vitals or a mobile network score. No Lighthouse run, INP certification or WebKit/Firefox/physical-device testing claimed.

Source screenshot archive in public totals 47,246,693 B, including a 27.4MB full PNG. These existing originals were deliberately preserved and are **not requested by the portfolio page**; runtime uses three optimized WebP covers (71,912 / 62,274 / 98,158 B) via responsive Next Image. No iframe/live-site embedding or heavy background media. Moving archival originals outside public could reduce a future deployment's asset footprint, but was not necessary for runtime loading and no originals were deleted.

## Artifacts and remaining limitations

Complete raw results (axe details, resource timings, external results): `%TEMP%\kyamich-final-qa\results.json`.
Screenshots: same directory, `hero-<width>.png`, `full-<width>.png`, `menu-<width>.png`, `hero-review.jpg`, `full-review.jpg`, `sections-<width>.jpg`, and external page captures.

The final production server is left running at http://127.0.0.1:3000/, PID 30156. Log: `%TEMP%\postman-shell-term_1792916100737_r6xtwicwy.log`.

No commit, push, DNS change or Vercel deployment attempt in this QA session. Branch main and original `6233bac` Initial commit remain unchanged. Project is build-ready, not published.

A genuine direct business contact remains the only business-content dependency: email/phone are null in `src/config/site.ts`. Discuss CTAs scroll to an honest GitHub fallback; GitHub is not a direct messaging/contact submission channel. Do not claim customer lead delivery is operational until a verified contact is supplied. Lighthouse/field performance, exhaustive assistive-technology testing, physical-device and cross-engine coverage remain unperformed.
