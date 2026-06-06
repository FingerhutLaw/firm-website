# Squarespace Setup — Session Notes

**Last updated:** 2026-06-02 (start of seventh session — CSS Section 11 surgically removed)
**Status:** Section 11 (dark-section overrides) deleted from local CSS file — was the source of the invisible CTA button bug. Dark sections now handled via Site Styles → Colors palette instead. About page still one big Dark 1 section; needs split into 5 sections + CTA button rebuild. Three pages pasted total (Disclaimer, Privacy, About).

---

## Where we are now (2026-06-02, start of seventh session)

### What just got done
- ✅ **CSS Section 11 removed** from `resources/squarespace-custom.css` — the block that forced dark/bold themes to Oxford Blue + white text + inverted buttons. It was fighting Squarespace's native theme engine via universal `*` selectors and CSS-variable overrides; almost certainly the cause of the invisible CTA button on the About page Dark 1 section.
- The replacement strategy: dark sections (footer, CTA bands) are now configured natively via **Site Styles → Colors → palette swatches**, not via Custom CSS. Brand tokens, fonts, buttons (on light sections), footer styling, and the warmth pass (Section 14) are all preserved.

### Immediate next steps (do these in Squarespace)

**1. Update Custom CSS panel in Squarespace** (do FIRST)
- Open Squarespace → Website → Website Tools → Custom CSS
- Delete everything currently there
- Open `resources/squarespace-custom.css` in this repo, copy the entire file, paste it into the Squarespace Custom CSS panel
- Save
- ALSO: delete the red H2 test rule (`h2 { color: red !important; }`) if it's still pasted in there

**2. Configure dark sections via Site Styles (replaces what Section 11 was trying to do)**
- Squarespace → Website → Site Styles → Colors → Edit palette
- For each color theme that needs to be Oxford Blue + white (typically "Dark 1" or whichever one footer/CTA uses):
  - Background: `#0A1F44` (Oxford Blue)
  - Heading text: `#FFFFFF`
  - Body text: `#FFFFFF`
  - Primary button background: `#FFFFFF`
  - Primary button text: `#0A1F44` (Oxford Blue)
  - Links: `#FFFFFF` (with underline)
- Save
- This is what Section 11 was *trying* to do, but the native palette editor does it without fighting the runtime

**3. THEN tackle the About page section split** (per recipe below — unchanged from sixth session)

---

## Where we left off (2026-06-01, end of sixth session)

### What got done this session
- ✅ **Headshot processed**: `IMG_0586.JPG` → background blurred via Python (rembg + PIL Gaussian) → saved as `IMG_0586_portrait.JPG` in `resources/Headshots/6-1-2026/Favorites/`. Steven cropped it to `IMG_0586_portrait, edited.JPG`. Uploaded to About page Section 1.
- ✅ **CSS warmth pass written**: Section 14 appended to `squarespace-custom.css`. Adds: small Oxford diamond ◆ above H2s, soft drop shadow on image blocks, zebra section tint (#FAFBFC on even Light sections), thin gradient hairline between sections, hero overlay for sections with bg images. Plus two opt-in utility classes: `fl-drop-cap` and `fl-pull-quote`.
- ✅ **CSS confirmed loading**: Red H2 test rule (`h2 { color: red !important; }`) was applied successfully — visible in editor view. Section 14 effects are subtle by design; whether they're rendering on Steven's specific Fluid Engine sections is TBD next session.
- ✅ **Stock photo curation strategy**: 6 Unsplash search URLs + per-placement selection criteria documented in chat (NYC skyline, empty office, courthouse, newspaper macro, morning light office). Selection deferred to a later session.

### Outstanding from this session

**1. Remove the red H2 test rule from Custom CSS panel** (top priority — easy)
- Squarespace → Website → Website Tools → Custom CSS
- Scroll to very bottom → delete the line `h2 { color: red !important; }`
- Save

**2. CTA button still invisible on About page** (parked — fresh attempt next session)
- Steven hit a wall trying to fix Dark 1 Primary Button colors in Site Styles
- Three workable paths next session:
  - **Easiest**: change CTA section from Dark 1 to Lightest 1 (loses dark band but button works immediately)
  - **Cleanest**: delete button block, reset Dark 1 button colors fresh, add new Primary button
  - **Sidestep**: keep dark band, ditch button block, use a styled text link instead
- Decide path when fresh. Don't try to white-knuckle the Site Styles button colors again — that's where the night ended.

**3. About page is still ONE big Dark 1 section** (from end of fifth session)
- Original plan: split into 5 sections (Header / Bio+Trial+Settlements / Practice+Commentary+Speaking+Photo / Credentials+Badge / CTA). Sections 1–4 = Lightest, Section 5 (CTA) = Dark.
- Did NOT happen this session — Steven went straight to the button fix and got blocked.
- Recipe from fifth-session notes (below) still applies. Do this BEFORE the button fix.

**4. Verify warmth pass effects are visible**
- Section 14 selectors target `.sqs-block-html h2` etc. — may not match Fluid Engine's actual class structure.
- Look on About page for: small ◆ above headings, drop shadow under headshot, faint hairline between sections, off-white tint on alternating sections.
- If not visible, swap to broader selectors (just `h2`, just `img`) — that mismatch was already identified.

---

## Strategic items Steven wants to discuss next session

### A. Future domain change as firm adds partners
- Steven anticipates adding partners (currently solo). Firm name would shift from "Fingerhut Law" (DBA) → something like "Fingerhut & [Partner] LLP" or similar.
- Wants to know whether/when he can change the domain without losing the SEO equity and Google Business Profile he's building now.
- Things to think through before next session:
  - **SEO impact**: 301 redirects from old domain → new domain preserve most ranking equity if done properly. Not zero loss, but manageable. Bigger risk is if multiple migrations happen in quick succession.
  - **Google Business Profile**: per [[gbp_timing]] memory, GBP hasn't been filed yet (waiting on office lease). So GBP impact on a domain change is moot for now — but if he files GBP and then changes the firm name, that triggers verification and is messy. **Recommendation: don't file GBP until firm name/domain is stable, even if office lease comes first.**
  - **Email migration**: Google Workspace can be moved to a new primary domain without losing inbox history (domain alias → primary swap). Doable but multi-step.
  - **Brand assets**: site copy, footer, disclaimer, retainer agreements — all reference "Fingerhut Law" / "Fingerhut Law Group, PLLC." A name change is a non-trivial copy update across files in this repo.
- **Decision deferred** — but worth aligning on timing: don't lock GBP, don't print stationery/business cards, don't deeply invest in SEO content until partner picture stabilizes.

### B. Email address feels too long
- Current: `sfingerhut@fingerhutlawgroup.com` (29 characters before the @ + domain)
- Steven wants to explore shortening. Options:
  1. **Shorter local part**: `steve@fingerhutlawgroup.com` (5 chars) or `sf@fingerhutlawgroup.com` (2 chars) — easiest, no DNS change, just create a new Google Workspace user/alias
  2. **Shorter domain**: register `fingerhutlaw.com` if available — would shorten to `sfingerhut@fingerhutlaw.com` or `steve@fingerhutlaw.com` (much shorter)
  3. **Both**: e.g., `steve@fingerhutlaw.com` (22 chars total)
- Things to check next session:
  - Is `fingerhutlaw.com` available at Hostinger / other registrars? Other variants too: `fingerhutlawnyc.com`, `flglaw.com`, `fingerhutlawfirm.com`
  - If a new domain is registered, decide: parallel (forward to primary) vs migrate primary
  - This also intersects with item A — if a partner-driven name change is coming, don't double-migrate
- **Cheap quick win**: regardless of any domain decision, create a `steve@fingerhutlawgroup.com` alias in Google Workspace tonight/tomorrow. Free, no DNS change, gives a shorter address immediately while the domain question stays open.

---

## Older outstanding issue from fifth session

### About page section split (still not done)

**Confirmed by Steven 2026-05-31:** All About-page content was added as **multiple blocks inside one big section**. Page needs to be split into 5 sections so the page has proper visual band structure (Sections 1–4 Light, Section 5 CTA Dark).

**Fix recipe (still applies):**
1. Open About page in editor mode. Confirm it's one big section.
2. **Split into 5 sections** by adding four new Blank sections below the existing one and drag-and-dropping content blocks into them in order: Header / Bio+Trial+Settlements / Practice+Commentary+Speaking+Photo / Credentials+Badge / CTA
3. Set per-section themes: Sections 1–4 = **Lightest**, Section 5 (CTA) = **Dark**
4. Then tackle the CTA button (see path options above)

### Next pages to paste (in order, unchanged)
1. **Practice Areas** (`content-practice-areas.md`) — 12 areas, longest content page; decide single-overview vs. overview + 12 sub-pages
2. **Results** (`content-results-page.md`)
3. **Media** (`content-media-page.md`) — reconcile with About (Law360, NPS panel, NJSBA panel now on About)
4. **Contact** (`content-contact-page.md`)
5. **Homepage** (`content-homepage.md`) — most design-heavy, save for last
6. **Footer build** — dark Oxford Blue band, three columns, compressed disclaimer + legal entity

---

## OLDER NOTES — Where we left off (end of fifth session, 2026-05-31)

### What's done this session
- ✅ **Disclaimer page** — pasted, formatted, slug `/disclaimer`, SEO set
- ✅ **Privacy Policy page** — pasted, formatted, slug `/privacy`, SEO set
- ✅ **About / Bio page** — content fully pasted (5 sections, Credentials with MMDAF badge, NJSBA panel photo embedded)
- ✅ **P&A contract IP risk addressed**: Read Steven's signed partnership agreement (`resources/Fingerhut Partnership Agreement, Signed.pdf`), confirmed Paragraph 4 grants post-departure license to reference/link/share authored articles, reference participation in CLEs/podcasts/media, and reference third-party publications where he was featured or quoted. Bio narrative paragraphs were rewritten in fresh language; Law360 quotes paraphrased rather than verbatim; panel descriptions rewritten in his voice rather than echoing conference agendas. See [[phillips-ip-constraint]] memory (updated 2026-05-31 with actual contract text).
- ✅ **Memory captured**: Steven prefers comprehensive linear instructions over iterative micro-corrections — see [[feedback-instruction-style]].

### Outstanding issue on About page — fix at start of next session

**Confirmed by Steven before logging off 2026-05-31:** All About-page content was added as **multiple blocks inside one big section**, not as five separate sections. The page therefore has one shared color theme (set to Dark / Oxford Blue), which is why most of the page came out Oxford Blue with white text and the Contact Us button came out white instead of blue.

**Steven wants to do this "the right way" tomorrow — i.e., break the single section up into five separate sections so the page has proper visual band structure (with Section 5 / CTA on its own Dark band against Light Sections 1–4).**

**Fix recipe (do this first thing next session):**
1. Open the About page in editor mode. Confirm it's one big section (single section settings gear at top, no horizontal Insert-Section dividers between content blocks).
2. **Split into 5 sections** by inserting section breaks at the right boundaries. Easiest method:
   - Add four new Blank sections below the existing one (`+ Add Section` at the bottom of the page → Blank → repeat 4 times)
   - Drag-and-drop content blocks from the existing big section down into the new empty sections, in the order Section 1 → 2 → 3 → 4 → 5 per the original paste plan (Header / Bio+Trial+Settlements / Practice Areas+Commentary+Speaking+Photo / Credentials+Badge / CTA)
   - Alternative if drag-and-drop is finicky: leave content in place and use the "Insert Section Above/Below" option from the section editor menu to split the existing section into pieces — but Squarespace doesn't always support this cleanly, so drag-into-new-section is the reliable path
3. Set per-section themes: Sections 1–4 = **Lightest** (pure white bg), Section 5 (CTA) = **Dark** (Oxford Blue band)
4. Verify the Contact Us button auto-flipped to Oxford Blue on a Light section. If it stays white, check Site Styles → Buttons.
5. Once colors are right, do a top-to-bottom pass for spacing/heading-size issues that may still remain
6. Then set slug `/about` and SEO if not already done

### Next pages to paste (in order)
1. **Practice Areas** (`content-practice-areas.md`)
2. **Results** (`content-results-page.md`)
3. **Media** (`content-media-page.md`) — needs to also be updated with the Law360 article, NPS panel, and NJSBA panel since those are now on the About page
4. **Contact** (`content-contact-page.md`)
5. **Homepage** (`content-homepage.md`) — most design-heavy, save for last
6. **Footer build** — dark Oxford Blue band, three columns, compressed disclaimer + legal entity

---

## OLDER NOTES — Where we left off (end of fourth session, 2026-05-31)

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
