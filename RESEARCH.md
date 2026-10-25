# KYAMICH portfolio — research only

## Scope and brief
Read the entire supplied 403-line local brief (not included in the repository).
The current request overrides its implementation/commit instructions: no application implementation, commit, push, DNS or production changes were performed.

## Repository and original state
Repository: `.`.
The parent workspace was not a Git repository. Cloned `https://github.com/KA71337/kyamich` into a new separate `kyamich` folder after checking that it did not exist. The `postman` and `.postman` folders were not modified.
Branch: `main`, tracking `origin/main`. Fetch/push origin: `https://github.com/KA71337/kyamich`.
HEAD: `6233bac769c551020057005fcd9fb230eba74767`, Initial commit.
Original working tree was clean; the only tracked file was `README.md` containing `# kyamich` (9 bytes). No application, components, package manifest, lockfile, styling configuration, tests or deployment configuration existed.
Only research files and screenshots have been added; tracked files remain unchanged.

## Contact evidence
There are no portfolio contact details in the README or existing source code (there is no application source). The initial Git commit author metadata contains an email address (intentionally omitted here), but this is provenance metadata, not confirmed permission to publish it as Kamil's business contact. The supplied GitHub URL is confirmed. No Kamil phone, WhatsApp, Telegram or Instagram was found. Confirm the preferred customer-contact channel before wiring the primary portfolio CTA. Never reuse client-company contacts as Kamil's contacts.

## Live sites: verified with browser and Playwright
All three homepages returned HTTP 200 at their own requested domains in independent Playwright contexts. In-app opening sometimes briefly reported the previously active page as a cross-domain redirect; direct navigation and independent browser results confirmed that this was not a real inter-project redirect.

### NERJ METAL
Category: industrial manufacturer / stainless-steel corporate catalog (`Paslanmaz polad istehsalı`).
Products: custom tanks, flagpoles, metal constructions, pool waterfalls, boiler/thermos/milk/fermentation/reactor tanks, spheres. Materials AISI 304 / 316. Construction, industry, food and chemical applications. Catalog, about, sectors, contact, product search, quote request and WhatsApp actions; TR/EN/RU language links observed (translation completeness not tested).
Visuals: black/graphite, lime highlights, manufacturing photography, very bold Archivo headings, Inter body, angular outlined CTAs and industrial editorial layout.
Confirmed public technology evidence: Next.js `_next/static` assets and `window.__next_f`, React through Next.js, Leaflet/OpenStreetMap map attribution, Vercel response header. Exact versions, TypeScript, Tailwind and animation libraries are not confirmed.
Contacts: `tel:+994708440664`, WhatsApp `https://wa.me/994708440664`; address shown as Bakü, Nerimanov rayonu, Ziya Bünyadov prospekti, 2075a. Mon–Sat 09:00–18:00, Sunday closed.
Checked `/catalog` and `/contact`: HTTP 200.

### TALSAN POWER
Category: power-equipment sales / technical service corporate catalog (`Enerji avadanlığı və texniki servis`).
Services: generator sales, stabilizer sales and repairs, regulator sales and repairs, technical consultation. Catalog has generator and stabilizer groupings; product/service inquiry forms and WhatsApp calls to action. No payment/checkout claim made.
Visuals: black masthead, light grey/white sections, yellow accents, Inter typography, numbered services and layered real equipment imagery.
Confirmed public technology evidence: Next.js `_next/static/immutable` assets, `window.__next_f`, React through Next.js, Turbopack-named asset, Vercel response header. Exact framework versions, TypeScript, Tailwind and animation libraries are not confirmed.
Contacts: `tel:+994506812125`, WhatsApp `https://wa.me/994506812125`; address shown as Lənkəran, Azərbaycan. The contact page displayed a dynamic closing-time statement (23:00), not a verified weekly schedule.
Checked `/services` and `/contacts`: HTTP 200.

### AYVA TECH
Category: electronics retail product catalog (`Elektronika məhsulları kataloqu`), not a confirmed checkout-enabled online shop.
Categories: tablets/e-readers, sport/leisure, smartwatches/bands, phones, home appliances, security systems, audio/video, games/controllers/software. Product cards display prices and detail links; category/search/sort catalog links, Tap.az shop link, contact/map and AZ/RU/EN language routes observed (translation completeness not tested).
Visuals: warm off-white, black, cyan/blue and yellow brand accents, Arial, spacious editorial hero and real product tiles. The first screen is intentionally restrained; an additional real selected-products gallery screenshot gives a stronger portfolio cover.
Confirmed evidence: rendered HTML/CSS and JavaScript assets `/style.css`, `/dropdown.js`, `/site.js`, Vercel response header. No React/Next.js/backend framework claim justified by observed assets.
Contacts: `tel:0108882313`, displayed `(010) 888-23-13`; address Bakı ş., Yasamal r., Azərbaycan pr., Həzi Aslanov küç., 7. Every day 09:00–21:00. No WhatsApp/email link observed.
Checked `/catalog` and `/contacts`: HTTP 200.

## Genuine local screenshots
Folder: `public/projects/`.
For each slug `nerj-metal`, `talsan-power`, `ayva-tech`:
- `<slug>-desktop.png` and `.webp`: 2880 × 2000, browser viewport 1440 × 1000 at DPR 2.
- `<slug>-cover.webp`: 1440 × 1000, quality 88.
- `<slug>-full.png` and `.webp`: full-page originals and optimized copies.
- `<slug>-mobile.png` and `.webp`: 780 × 1688, viewport 390 × 844 at DPR 2.
Additional: `ayva-tech-gallery.png`, `ayva-tech-gallery.webp`, `ayva-tech-gallery-cover.webp` (1440 × 1000 cover).
Recommended covers: `nerj-metal-cover.webp` (71,912 bytes), `talsan-power-cover.webp` (62,274 bytes), `ayva-tech-gallery-cover.webp` (98,158 bytes). AYVA hero alternative: `ayva-tech-cover.webp` (37,002 bytes).
Full-page WebP dimensions: NERJ 1861 × 16000; TALSAN 2880 × 9922; AYVA 2880 × 7496. NERJ full-page original exceeded WebP's 16383-pixel dimension limit; the capture script was repaired to downscale proportionally. This issue is resolved.
PNG originals are intentionally preserved for research; use optimized WebP covers rather than full PNG pages in the future UI.
Screenshot sheet was visually inspected in the browser, including the AYVA gallery. All homepage image elements loaded and no pageerror events occurred in the final independent captures. External ad/network console errors were observed in the in-app NERJ session; this is not a clean audit of all third-party network requests. Route snapshots were short inspections, not functional/form-submission testing.

## Research tooling
`tools/capture-projects.py`: repeatable live desktop/full/mobile capture and metadata inspection.
`tools/verify-research.py`: compact evidence verification and deterministic AYVA gallery capture.
Python Playwright was installed outside the repository into `%TEMP%\kyamich-research-tools`; used existing Microsoft Edge and existing Pillow. No application dependencies were installed.
Run with `PYTHONPATH` set to that isolated directory. Evidence logs are in `%TEMP%\kyamich-site-research-fixed.log` and `%TEMP%\kyamich-verification.log`.
A temporary loopback-only image inspection server was started on `127.0.0.1:8765`; no portfolio application was started.

## Implementation plan (not executed)
1. Initialize Next.js App Router + React + TypeScript, Tailwind CSS, selective Motion and Lucide; no existing stack needs preservation. Pin dependencies and add lockfile/build/typecheck/lint commands.
2. Create central `src/data/projects.ts` for verified project facts, URLs, technology labels and WebP dimensions; `src/config/site.ts` for domain and explicitly approved contacts. Initially AZ only; add RU/EN only if fully translated.
3. Build Navigation, Hero/ProjectPreview, SelectedWorks/ProjectCard, Services, Pricing, Process, About, FinalCTA and Footer. Graphite/ivory with restrained acid-lime highlights, oversized typography and asymmetric actual-project windows; mobile-specific layout rather than squeezed desktop.
4. Use verified covers, fixed image dimensions and responsive sizes; eagerly load only hero essentials. No site iframes, invented biographies, testimonials, guarantees or fake contact forms.
5. Price text exactly reflects 200–300 ₼ and scope-dependent final quotes. Primary contact CTA requires confirmed business contact; GitHub is not a substitute for an invented WhatsApp number.
6. Server-render mostly static content; minimal motion islands, reduced-motion support, keyboard navigation, visible focus and accessible mobile menu.
7. Configure kyamich.dev canonical/title/description/OG, AZ language, favicon/wordmark, robots and sitemap. Structured data only for established facts.
8. Run production build/typecheck/lint, desktop/mobile browser checks at 320/375/390/768/1440/1920 widths, overflow/image loading checks, all navigation/CTA/project links, reduced-motion and console inspection. Commit/push only in a subsequent expressly authorized implementation phase.

## Blockers
No blocker to research or screenshot delivery remains. Main implementation input gap: Kamil's explicitly approved business contact. No runnable application exists yet, so application build/lint tests cannot currently run. Client stacks beyond public evidence remain unverified; do not label them TypeScript/Tailwind/Motion without source evidence.
