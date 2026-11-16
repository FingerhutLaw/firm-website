# Friedman & Fingerhut — firm website

## What this is

The public marketing website for **Friedman & Fingerhut, PLLC**, a plaintiff-side employment law firm in NYC. Lives at `https://friedmanfingerhut.com`. Built with [Astro](https://docs.astro.build) (static site generator), styled with Tailwind v4, deployed to Netlify.

## Repo layout

- `site/` — the Astro project. **All code changes happen here.**
- `resources/` — reference assets (brand files, source material) that aren't shipped to the live site.
- Root `README.md` is a stub.

## Running it locally

From `site/`:

```sh
npm install        # first time only
npm run dev        # local preview at http://localhost:4321
npm run build      # produces dist/ — what Netlify ships
```

**Node ≥ 22.12 required** (see `site/package.json`). If `npm install` fails with an engine/version error, you're probably on Node 20 (the common LTS). Fix with `nvm install 22` or install the latest from nodejs.org, then re-run `npm install`.

## How a change goes live

**Every push to `main` triggers a production Netlify build (~90 seconds), and the live site rebuilds automatically. There is no staging step.** Branch protection is currently off, so a direct push to `main` is production.

If anything goes wrong on live, roll back from the Netlify **Deploys** tab — one click, every past deploy is kept.

Two Netlify sites watch this same repo:
- `friedmanfingerhut` → serves `friedmanfingerhut.com` (primary — the one that matters).
- `fingerhutlaw` (orphan) → serves `fingerhutlawgroup.com` as 301 redirects via `site/public/_redirects`. Don't edit `_redirects` without a specific reason; its rules are hostname-scoped so they only fire on the old domain.

### Deploy previews

If you open a PR from a branch, Netlify auto-builds a preview at `deploy-preview-<N>--friedmanfingerhut.netlify.app` and posts the URL into the PR. Use this when you want Steven to see a change before it goes live.

## Where things live inside `site/src/`

- `pages/` — one file per route. `index.astro` is the homepage, `attorneys.astro` → `/attorneys`, etc. Subfolders (`pages/blog/`, `pages/practice-areas/`) hold per-item pages.
- `content/` — Astro content collections (blog posts, practice-area pages). Schema in `content.config.ts`.
- `layouts/Layout.astro` — the shared page shell (header, footer, meta tags).
- `styles/` — Tailwind globals.

## Firm voice + content rules

These are non-negotiable because this is a law-firm marketing site; the wrong line creates ethics or marketing problems.

- **Brand name is "Friedman & Fingerhut"** (or "Friedman & Fingerhut, PLLC"). Never "Fingerhut Law" (old name, retired as of the Oct 2026 rebrand) and never any variant mentioning "Phillips & Associates" (former affiliation — do not reference anywhere on the site).
- **No comparative case-value language in marketing copy.** No "we win $X million settlements," no fact-pattern → damages ranking, no "cases like yours are worth…" framing. The Results page lists verdicts/settlements as plain factual entries; nothing on marketing pages ranks or compares case values.
- **No AI-writing tells.** Avoid "not just X but Y" constructions, rhetorical Q-and-A ("Why does this matter? Because…"), and em-dash-heavy hedging. The site should read like a plaintiffs' employment lawyer wrote it — direct, concrete, grounded in the specific statute or facts.
- **No safety / outcome overclaims.** Avoid "guaranteed," "zero risk," "always win," or anything a bar committee would flag as a promise of result.
- **Contact details:** Phone is **(212) 680-4040**. Intake email is **intake@friedmanfingerhut.com**.

## Analytics

Plausible only. **No Google Analytics, no Google Tag Manager, no Meta Pixel, no Hotjar.** If a feature wants to add tracking, flag it and push back — this was a deliberate decision in July 2026.

## SEO notes

- `astro.config.mjs` sets `site: 'https://friedmanfingerhut.com'` and generates a sitemap at `/sitemap-index.xml` on every build. If you add new content types or routes you don't want indexed, add them to the `sitemap({ filter })` call there (see how `/contact/thanks` is excluded for the pattern).
- Title-tag strategy is hybrid by page type (keyword-first for practice-area pages, brand-first for about/attorneys/contact). Check with Steven before changing any `<title>` on existing pages.

## Common tasks — quick orientation

- **Add a blog post:** new file in `site/src/content/blog/` matching the schema in `content.config.ts`. Astro generates the route automatically.
- **Add a practice-area page:** new file in `site/src/content/practice-areas/` (same pattern).
- **Edit an existing page:** find it in `site/src/pages/`.
- **Change site-wide header/footer/nav:** `site/src/layouts/Layout.astro`.
- **Static assets (images, PDFs, favicons):** `site/public/` — served from the root of the site at the same path.
