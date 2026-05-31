# Squarespace Setup — Session Notes

**Last updated:** 2026-05-31 (end of fourth session — brand foundations done)
**Status:** Brand system installed via Custom CSS + Site Styles palette. Ready for content paste-in.

---

## Where we left off (2026-05-31)

- ✅ Signed up for Core plan, professional templates path, picked a template
- ✅ **Brand decisions locked**: Oxford Blue `#0A1F44` accent + pure white `#FFFFFF` background + Playfair Display headlines + Inter body (see Locked Decisions below)
- ✅ Wrote Custom CSS file (`resources/squarespace-custom.css`) — pasted into Squarespace Website Tools → Custom CSS
- ✅ Site Styles palette swatch 1 set to `#FFFFFF` so all Lightest-theme sections render pure white
- ✅ Verified working: header is white, "Schedule a Consultation" CTA is Oxford Blue, Playfair Display headlines render correctly
- ✅ Workaround documented: Squarespace 7.1 dark themes don't accept Custom CSS overrides reliably — switch sections to Light theme via the section editor, OR fix at Site Styles → Colors level for sections that must stay dark (footer/mission)

### What still has template placeholder content
- Homepage hero says "Business + Intellectual Property Attorneys"
- About page has "Advocating for creative communities and entrepreneurs since 2003"
- Areas of Practice has "Music" as a practice area with fake copy
- Contact section says "123 Demo Street" / "email@example.com"
- All other pages: still have template's fake content

---

## Next action when you return

### Pick up at: **Clear template placeholders and paste real content**

1. **Delete the template's placeholder pages first** (Pages panel left side → trash icon per page). Leaves you with a clean slate to scaffold the real pages.
2. **Scaffold real pages** with correct nav order:
   - Home / About / Practice Areas / Results / Media / Contact (in main nav)
   - Disclaimer / Privacy (footer-only, not in main nav)
3. **Paste content from `content-*.md` files**, starting with low-stakes pages:
   - Disclaimer → Privacy → Bio (About) → Practice Areas → Results → Media → Contact → **Homepage last** (most design-heavy)
4. **Edit nav menu**: remove "Our Team" (solo) and "Blog" (not planned); rename "Areas of Practice" → "Practice Areas"; add Results + Media if not already there
5. **Build the footer**: dark Oxford Blue band, three columns (firm address / practice areas / firm links), bottom legal line. Footer should use a Dark theme set via Site Styles → Colors (NOT via Custom CSS, since that didn't stick).

When you return, tell Claude "ready to paste content" and we'll start with Disclaimer.

### Then, in order

1. Content pasted on all pages
2. Connect `fingerhutlawgroup.com` via DNS in Hostinger (A + CNAME only — do NOT change nameservers)
3. Go live, add DKIM, cancel Hostinger hosting/email

---

## Bigger-picture roadmap (where Squarespace fits)

1. ~~Phase 1 — Google Workspace email~~ ✅ Done (DKIM still TODO — see `dkim-dmarc-followup.md`)
2. **Phase 2 — Squarespace** ← you are here
   - [x] Sign up, choose Core plan
   - [x] Skip AI builder, choose professional templates
   - [x] Pick template
   - [x] Configure colors, typography, header (via Custom CSS + Site Styles palette)
   - [ ] Delete template's placeholder pages
   - [ ] Scaffold real pages (Home, About, Practice Areas, Results, Media, Contact, Disclaimer, Privacy)
   - [ ] Paste in content from `content-*.md` files
   - [ ] Build footer (legal entity name: Fingerhut Law Group, PLLC)
   - [ ] Connect `fingerhutlawgroup.com` via DNS in Hostinger (A + CNAME only — do NOT change nameservers)
3. Phase 3 — Cleanup
   - [ ] Add DKIM in Hostinger DNS
   - [ ] Cancel Hostinger email + hosting
   - [ ] Keep Hostinger domain registration with auto-renew ON
4. Deferred (not now)
   - Google Business Profile — wait until physical office lease is signed (premature filing risks suspension + forced name change)

---

## Content files ready to paste in

All in `resources/`:
- `content-homepage.md`
- `content-bio-page.md`
- `content-practice-areas.md`
- `content-results-page.md`
- `content-media-page.md`
- `content-contact-page.md`
- `content-disclaimer-page.md`
- `content-privacy-policy.md`
- `content-firm-values.md`
- `content-mission-statement.md`

Reference (not pages, but informs design/copy):
- `competitive-research.md`
- `seo-content-plan.md`

---

## Locked decisions (don't re-litigate)

- Public brand: **Fingerhut Law** (DBA)
- Legal entity name (footer, disclaimer, privacy): **Fingerhut Law Group, PLLC**
- Solo attorney — no plural-attorney language anywhere
- PFL and severance are secondary positioning, not lead copy
- No copy or media from Phillips & Associates; no Lawyer Monthly cover image
- **Accent color:** Oxford Blue `#0A1F44` (was Aubergine, revised same day)
- **Background:** pure white `#FFFFFF` (was warm cream, revised after Oxford swap)
- **Body text:** near-black `#111111`
- **Headline font:** Playfair Display (serif)
- **Body font:** Inter (sans-serif)
- **Note on dark sections:** Squarespace's built-in dark themes don't accept Custom CSS overrides reliably; switch problem sections to Light theme via section editor instead.
