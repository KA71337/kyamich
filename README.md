# kyamich

Premium Azerbaijani-language portfolio for Kamil / KYAMICH. Next.js App Router, React, strict TypeScript, self-hosted variable fonts, Lucide icons and small native animation islands. No remote fonts, website iframes, fabricated contact forms or invented client results.

## Local development

Node.js 20.9+ (24 LTS recommended).

```sh
npm ci
npm run dev
```

Production preview:

```sh
npm run build
npm run typecheck
npm run lint
npm start -- --port 3000
```

Open http://127.0.0.1:3000. `npm start` serves the production build; `npm run dev` is the development server.

## Content and architecture

- `src/config/site.ts`: typed brand, domain, navigation, price and nullable contact configuration.
- `src/data/projects.ts`: verified project URLs, technologies, screenshot dimensions, descriptions, services and four process stages.
- `src/app/page.tsx`: hero, asymmetric selected works, services, pricing, process, About Kamil, final CTA, contacts and footer.
- `src/components/`: keyboard-accessible mobile navigation, project cards and reduced-motion-aware progressive reveal effects.
- `src/app/globals.css`: original graphite / acid-lime visual system, responsive layouts down to 320px.
- `src/app/layout.tsx`, `robots.ts`, `sitemap.ts`, `opengraph-image.tsx`, `icon.svg`: AZ metadata, canonical, structured data, social image and favicon.
- `public/projects/`: genuine research screenshots. UI uses only optimized local WebP covers; originals are preserved.
- `RESEARCH.md`, `tools/capture-projects.py`, `tools/verify-research.py`: original research preserved with private machine paths and unapproved author contact omitted from documentation. The research report describes the earlier research-only state, not the current application.
- `tools/qa-site.py`: production-browser responsive, links, images, menu, reduced-motion and SEO smoke tests. Uses the existing isolated Python Playwright installation with Microsoft Edge; not an app dependency.

### Contact truthfulness

Phone and business email remain `null`. The commit author email is not an approved business contact and is not rendered. Primary discussion CTAs lead to `#elaqe`. GitHub is explicitly labeled as an alternative **profile transition**, not a message channel; the page does not claim to send inquiries. To enable direct contact later, set approved values in `contacts` in `src/config/site.ts`. Client-company contact details must never be substituted.

### Deployment on Vercel

Ready for Vercel's Next.js preset: root directory `kyamich` when importing the parent workspace, or repository root when importing `KA71337/kyamich`; install `npm ci`, build `npm run build`, default Next.js output. No secrets or environment variables are required. Use a preview deployment first. The configured canonical domain is `https://kyamich.dev`; production deployment/account authorization and domain ownership must be available before publishing. No DNS changes are made by this application. Git delivery is separate from website deployment.

## Browser QA

Windows cmd, using the isolated research tooling:

```bat
set "PYTHONPATH=%TEMP%\kyamich-research-tools"
python tools\qa-site.py
```

Screenshots are saved outside the repository to `%TEMP%\kyamich-qa`. Actual verification results and current preview details are recorded in `IMPLEMENTATION.md`.
