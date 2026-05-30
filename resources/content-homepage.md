# Website Content — Homepage Assembly Plan

*The homepage stitches together pieces from the other content files (`content-mission-statement.md`, `content-firm-values.md`, `content-practice-areas.md`, `content-bio-page.md`, `content-media-page.md`) plus a few short connective sections drafted here.*

*Use as the master spec when building the Squarespace homepage.*

---

## 1. Strategic Frame

The homepage has 7–10 seconds to do three things for a worker who just typed "NYC employment lawyer" or who arrived from a press feature:

1. **Tell them they're in the right place** (NYC, employment, worker-side).
2. **Give them one immediate reason to trust this firm** (track record, press, judicial endorsement, or a recognizable settlement number).
3. **Make the next click obvious** (call, schedule, contact form).

Per `competitive-research.md`, the firms that do this best on this site's competitive scale are **Wang Hecker** (boutique restraint), **Outten & Golden** (worker-facing language + phone-first intake), and **Smith Mullin** (calm credibility, no combat tone). The wrong models are **Wigdor** (too combative for a solo) and **Phillips & Associates** (template SEO aesthetic). The homepage below follows the Wang Hecker / Smith Mullin register with O&G's intake patterns.

---

## 2. Wireframe (top to bottom)

```
+-----------------------------------------------------------+
| NAV: Fingerhut Law   About  Practice  Results  ...  |
|                                              (212) ...    |
+-----------------------------------------------------------+
|                                                           |
|   [1. HERO]                                               |
|   Headline (one sentence, NYC + employee-side)            |
|   Sub-headline (one line — trust anchor)                  |
|   [Schedule Consultation]    (212) 680-4040               |
|                                                           |
+-----------------------------------------------------------+
|   [2. PRESS / TRUST STRIP]                                |
|   Lawyer Monthly · Authority Mag · Beyond Exclamation     |
+-----------------------------------------------------------+
|                                                           |
|   [3. MISSION PULL-QUOTE]                                 |
|   "I believe victims. I stand with victims."              |
|                                                           |
+-----------------------------------------------------------+
|   [4. PRACTICE AREAS GRID — 6 tiles, 3x2]                 |
|   Sexual Harassment    Race Disc.        Retaliation      |
|   Pregnancy Disc.      Disability Disc.  Wrongful Term.   |
|                          [See all practice areas →]       |
+-----------------------------------------------------------+
|                                                           |
|   [5. RESULTS STRIP — 3-4 verdict/settlement callouts]    |
|   $2,000,000  |  $1,550,000  |  $30M+  |  Federal Verdict |
|                              [See more results →]         |
|                                                           |
+-----------------------------------------------------------+
|   [6. MEET STEVEN — bio teaser]                           |
|   [Portrait] | Short paragraph + credential bullets       |
|              [Read full bio →]                            |
+-----------------------------------------------------------+
|                                                           |
|   [7. VALUES — short list]                                |
|   What This Firm Stands For                               |
|   1. Belief.  2. Preparation.  3. Trial-readiness.        |
|   4. Plain talk.  5. Respect.                             |
|                                                           |
+-----------------------------------------------------------+
|   [8. IN THE NEWS — 2-3 press feature cards]              |
|   Lawyer Monthly cover (July 2019), Authority Mag, etc.   |
|                              [See all press →]            |
+-----------------------------------------------------------+
|                                                           |
|   [9. FINAL CTA]                                          |
|   "If your rights at work have been violated, ..."        |
|   [Schedule Consultation]    (212) 680-4040               |
|                                                           |
+-----------------------------------------------------------+
|   FOOTER                                                  |
|   Address · Phone · Email · Bar admissions · Disclaimer   |
+-----------------------------------------------------------+
```

---

## 3. Section-by-Section Spec

### Section 1 — Hero

**Purpose:** Identify the firm, the practice, and the audience in one screen. Drop one trust anchor. One primary CTA.

**Copy — recommended:**
> **Headline (H1):** A focused employment law practice in New York City.
>
> **Sub-headline:** Over $30 million recovered for workers in discrimination, harassment, retaliation, and wrongful termination cases.
>
> **Primary CTA button:** Schedule a Consultation
> **Secondary CTA (inline next to button):** or call (212) 680-4040

**Alternate hero (if Steven prefers more values-forward, Wang-Hecker-style):**
> **Headline:** Representing New York employees against discrimination, harassment, and retaliation.
>
> **Sub-headline:** Eleven years of trial and appellate experience. Over $30 million recovered. Free, confidential consultations.

**Alternate hero (most aggressive — only use if Steven wants the Wigdor register):**
> **Headline:** I believe victims. I stand with victims.
>
> **Sub-headline:** New York employment law. $30M+ recovered. Trial-tested.

*Recommendation:* Lead with the **first option** for the hero — it is the most boutique-credible register and matches the competitive analysis. Use *"I believe victims. I stand with victims."* later in the page as a pull-quote (section 3), not as the hero. The hero should be calm; the pull-quote can be fierce.

**Layout:**
- Full-width, ~600–700px tall on desktop
- Left-aligned text (not centered) — reads more editorial, less marketing
- Generous whitespace; nothing competing with the headline
- Optional background imagery: NYC architectural detail (skyline, courthouse exterior, Brooklyn Bridge from below) at low opacity, OR clean off-white background with no imagery (Wang Hecker style — the strongest signal)
- Avoid: stock gavels, scales of justice, leather books, "diverse team in a conference room"

**Source files:** `content-mission-statement.md` (headline options)

---

### Section 2 — Press / Trust Strip

**Purpose:** Visual proof, instantly. Logos do the talking.

**Copy:** None — visual only.

**Layout:**
- Horizontal strip of 3–5 logos, monochrome (grayscale at ~40% opacity)
- Equal heights, generous spacing
- Optional tiny label above: "As Featured In" (small caps, light weight)
- On mobile: scrolling carousel or 2x2 grid

**Logos to include (in order of authority):**
1. *Lawyer Monthly* (July 2019 cover — highest authority)
2. *Authority Magazine* (via Medium)
3. *Beyond Exclamation*
4. Super Lawyers (Rising Star 2018–2025)
5. NELA (National Employment Lawyers Association — member badge)

**Avoid:** Full-color badge soup (Lawyers of Distinction, Top 10 Lawyer, Avvo with star count). Per `competitive-research.md` these read pay-to-play.

**Source files:** `content-media-page.md`, `content-bio-page.md` (Recognition section)

---

### Section 3 — Mission Pull-Quote

**Purpose:** State the firm's defining belief. One sentence, large type.

**Copy:**
> **"I believe victims. I stand with victims."**
>
> — Steven Fingerhut

**Layout:**
- Full-width section, generous vertical padding (~120px top/bottom)
- Quote in display-size type (~48–60px desktop), centered or left-aligned
- Attribution in smaller type below
- Background: off-white or a subtle accent color (deep charcoal, burgundy, or muted gold per palette in section 11) — different from sections above and below to break the rhythm

**Source files:** `content-mission-statement.md`

---

### Section 4 — Practice Areas Grid

**Purpose:** Show breadth + let the worker self-identify their case. Each tile clicks through to the practice-area sub-page.

**Copy — heading:**
> **Practice Areas**
>
> *(Alternative: "Issues" — per `content-practice-areas.md`)*

**Tiles to include on homepage (6 of the 12 — the intake areas the firm wants to attract most). Grid order matters: the first row is the headline three.**

**Row 1 — top intake priorities:**

| Tile | Tagline | Links to |
|---|---|---|
| **Sexual Harassment** | When power is misused at work. | `/practice-areas/sexual-harassment` |
| **Race Discrimination** | Federal, state, and NYC HRL protections. | `/practice-areas/race-discrimination` |
| **Retaliation** | Punished for raising your hand? That's protected activity. | `/practice-areas/retaliation` |

**Row 2 — secondary tiles (still featured on home):**

| Tile | Tagline | Links to |
|---|---|---|
| **Pregnancy Discrimination** | Workers deserve more protection during pregnancy, not less. | `/practice-areas/pregnancy-discrimination` |
| **Disability Discrimination** | When a reasonable accommodation request became a termination. | `/practice-areas/disability-discrimination` |
| **Wrongful Termination** | Fired for the wrong reason — and the right framework matters. | `/practice-areas/wrongful-termination` |

**Below the grid:** *"See all practice areas →"* link to `/practice-areas` overview.

**Deliberately omitted from the homepage tiles** (still in the firm's full practice-area list, just not featured here):
- **Severance Negotiation** — the firm reviews severance agreements but is not actively marketing to high-volume severance shoppers. The full practice-area page exists for workers who arrive there from search or referral.
- **Paid Family Leave Violations** — PFL grievances are common but PFL-only matters are usually not financially attractive cases. The full practice-area page is framed as a gateway: a PFL grievance often signals an underlying pregnancy, disability, or FMLA claim that is the real recovery. Featuring PFL on the homepage would invite the wrong intake.

**Layout:**
- 3 columns x 2 rows on desktop
- 2 columns x 3 rows on tablet
- 1 column (stacked) on mobile
- Each tile: heading + 1-line tagline + hover state. No icons (per competitive research — icons read cheap).
- Type-only treatment; possibly with a subtle hairline border or background-on-hover

**Source files:** `content-practice-areas.md`

---

### Section 5 — Results Strip

**Purpose:** Concrete proof. Real numbers. Real cases.

**Copy — heading:**
> **Results**

**Callouts (3–4 horizontal cards):**

| Card | Detail |
|---|---|
| **$2,000,000** | Race discrimination settlement on behalf of eleven construction workers subjected to repeated racial slurs. |
| **$1,550,000** | Sexual harassment settlement for a content producer harassed by the CEO of a B2B marketing company. |
| **$425,000+** | Federal jury verdict (E.D.N.Y., January 2024) for a client subjected to race and sex discrimination, retaliation, and defamation. *Affirmed by the Second Circuit on all six grounds of appeal.* |
| **$30M+** | Total recovered for workers across eleven years of practice. |

**Below the strip:** *"See all results →"* link to `/results`.

**Layout:**
- Horizontal row, 4 cards (or 3 if Steven prefers — drop the rollup number)
- Large dollar figures in display type
- 1-line description under each
- On mobile: vertical stack
- Background: charcoal or near-black, white text — high contrast for the most important numbers on the page

**Source files:** `content-bio-page.md` (Trial Record + Notable Settlements), `Legal timeline 3.txt` transcript

---

### Section 6 — Meet Steven (Bio Teaser)

**Purpose:** Put a face on the firm. Establish E-E-A-T for Google and trust for the reader.

**Copy — 90-word teaser (new, written for this section):**

> **Steven Fingerhut**
> *Founder, Fingerhut Law*
>
> Steven Fingerhut is a New York employment law attorney with eleven years of experience representing workers in discrimination, harassment, retaliation, and wrongful termination cases. He is admitted in New York, New Jersey, all four New York federal districts, the District of New Jersey, and the Second Circuit Court of Appeals. He has tried employment cases to verdict in state and federal court and has defended those verdicts on appeal.
>
> [Read full bio →]

**Sidebar / credential pills (visual accent):**
- 11 years of practice
- $30M+ recovered
- Super Lawyers Rising Star, 2018–2025
- Lawyer Monthly cover feature, July 2019

**Layout:**
- Two-column on desktop: portrait on the left (40%), text on the right (60%)
- Single column on mobile, portrait stacked above text
- Portrait: professional headshot against a neutral background, ideally shot for this purpose. *Note:* the Lawyer Monthly July 2019 cover photo cannot be used as a fallback — that image is P&A-controlled per the partnership agreement (see `phillips-ip-constraint` memory). A new headshot needs to be commissioned. Until one exists, ship the bio section without a portrait rather than with a P&A-era image.
- Per `competitive-research.md`: clean, well-lit, neutral background. **No** courtroom-implied props, no "lawyer in suit standing in front of skyline."

**Source files:** `content-bio-page.md`

---

### Section 7 — What This Firm Stands For (Values)

**Purpose:** Differentiation. Why this firm rather than the firm down the street.

**Copy — heading + 5 short values:**

> **What This Firm Stands For**

| # | Value | One line |
|---|---|---|
| 1 | **I believe my clients.** | Belief is the starting position, not the reward. |
| 2 | **Preparation that anticipates everything.** | Over-preparation is the only kind of preparation. |
| 3 | **Willingness to try the case.** | Settlement only works when the defense knows trial is real. |
| 4 | **Plain talk.** | If you don't understand the strategy, that's on me. |
| 5 | **Real respect for the client.** | No client is judged at this firm. |

*(Use a 6th, "Boutique focus, real attention," if the layout needs even numbers.)*

**Layout:**
- Numbered list with strong type hierarchy
- Each item: number + bold one-phrase headline + 1-line elaboration
- Generous vertical spacing between items
- No icons
- Two-column layout on desktop (numbers 1–3 left, 4–6 right) OR single column with extra whitespace
- Soft background (warm off-white or barely-tinted accent) to distinguish from the section above and below

**Source files:** `content-firm-values.md` (this is the short homepage version; the full values page is the long form)

---

### Section 8 — In the News

**Purpose:** Authority through earned media. Different from section 2 (logos only) — this is a richer card view with headlines and links.

**Copy — heading:**
> **In the News**

**Cards (2–3, horizontal):**

| Card | Detail |
|---|---|
| **Lawyer Monthly** — Cover Feature, July 2019 | *LGBT+ Inclusivity in the Workplace.* Steven appeared on the cover discussing how the NYC Human Rights Law exceeds federal protections. |
| **Lawyer Monthly** — Expert Insight, March 2019 | *What Should You Do If You Are Fired After Filing a Sexual Harassment Complaint?* |
| **Beyond Exclamation** | *A Zealous Advocate for Employees Who Have Been Wronged.* |

**Below the cards:** *"See all press →"* link to `/media`.

**Layout:**
- 3 cards horizontal on desktop, 1 column on mobile
- Each card: publication name (small, in caps) + headline + 1-line excerpt + "Read article →" link
- **Do not use the Lawyer Monthly July 2019 cover photograph** as a card thumbnail — per `phillips-ip-constraint` memory, that image is controlled by Phillips & Associates and cannot appear on this site. Use the publication wordmark / logo instead, or a clean text-only card.

**Source files:** `content-media-page.md`

---

### Section 9 — Final CTA

**Purpose:** Close the funnel. If the worker has scrolled this far without clicking, give them one more clean conversion path.

**Copy:**

> **If your rights at work have been violated, don't wait.**
>
> Employment claims in New York have short deadlines — sometimes as short as 180 days. Contact Fingerhut Law for a free, confidential consultation.
>
> [Schedule a Consultation]    or call **(212) 680-4040**

**Layout:**
- Full-width band, dark background (charcoal or near-black) with light text
- Centered text on this section (in contrast to left-aligned hero)
- Generous vertical padding (~120px top/bottom)
- The button and phone number are the only interactive elements — no form embedded here. Form is at `/contact`.

**Source file:** *(new — drafted above)*

---

### Section 10 — Footer

**Purpose:** Trust signals, compliance, navigability.

**Required content:**

- **Brand line (top of footer, display type):** **Fingerhut Law** · New York employment law
- **Legal entity disclosure (smaller type below brand line):** *Fingerhut Law is the registered trade name of Fingerhut Law Group, PLLC, a New York professional limited liability company.*
- **Address:** 469 7th Avenue, 12th Floor, New York, NY 10018
- **Phone:** (212) 680-4040
- **Email:** sfingerhut@fingerhutlawgroup.com (or info@)
- **Office hours:** Monday through Friday, 9:00 am – 6:00 pm ET. After-hours consultations by appointment.
- **Quick links:** About · Practice Areas · Results · Press · Contact · Privacy · Disclaimer
- **Bar admissions row:** "Admitted: New York · New Jersey · S.D.N.Y. · E.D.N.Y. · N.D.N.Y. · W.D.N.Y. · D.N.J. · Second Circuit Court of Appeals"
- **Required disclaimer** (NY attorney advertising rule):
  > *Attorney Advertising. Prior results do not guarantee a similar outcome. The information on this website is for general informational purposes only and is not legal advice. Contacting the firm does not create an attorney-client relationship.*
- **Copyright:** © 2026 Fingerhut Law Group, PLLC. All rights reserved.

**Layout:**
- Dark background (matches CTA section above for visual continuity)
- 3–4 columns on desktop, stacked on mobile
- Small type throughout; disclaimer in the smallest readable size

---

## 4. Top Nav

Per `competitive-research.md` §4 (boutique restraint), keep nav to **6 items max**:

```
Fingerhut Law     About  |  Practice Areas  |  Results  |  Press  |  Contact     (212) 680-4040
```

- The firm name on the left is itself a link to `/`
- Phone number on the right is tap-to-call on mobile
- Sticky nav on scroll (Squarespace default)
- "Schedule Consultation" can replace the phone number as the right-side CTA if Steven prefers a button-style CTA over a phone-forward CTA. Recommendation: **phone number** — per the competitive research, phone-first intake reads more sophisticated and more available than form-first.

---

## 5. Mobile-Specific Notes

- The homepage will be visited on phone by ~60–75% of organic traffic. Test every section on phone before going live.
- Hero collapses to single column; CTA button and phone must be tappable side-by-side.
- Practice areas grid: 1 column stacked, not 2. Six tiles in a column is fine; readers expect to scroll.
- Press logo strip: scrolling marquee or 2x2 grid (not a single horizontal row that compresses to unreadable).
- Sticky phone-tap-to-call button at the bottom of the viewport is *optional* and *only* if it doesn't feel cheap. Tomkiel & Tomkiel does this well; many PI firms overdo it. Steven's call.

---

## 6. Palette & Typography (locked)

**Palette — locked 2026-05-30:**
- **Primary (foreground/text):** Near-black `#111111` — not pure black
- **Secondary (background base):** Warm off-white `#F7F4EE`
- **Accent:** **Aubergine `#2A1B2F`** — almost-black with a purple undertone. Reads as ink in low light, purple in good light. Used for: accent rules, the "Schedule a Consultation" button, accent words within headlines, and the full-bleed dark background on sections 3 (Mission Pull-Quote), 5 (Results), and 9 (Final CTA).
- **Inverted sections (3, 5, 9):** background `#2A1B2F`, text `#FFFFFF` with 70% opacity on labels and metadata
- *(Alternatives considered and rejected: Burgundy `#5C1E1B`, Deep Plum `#3A1F3F`, Midnight Indigo `#1F2147`. See `palette-preview-v2.html` for the side-by-side comparison.)*

**Typography — locked 2026-05-30:**
- **Headlines:** Inter Display (free, Google Fonts). Weights 600 for H1/H2, 500 for H3.
- **Body:** Source Serif Pro (free, Google Fonts). Weights 400 for body, 600 for emphasis.
- **UI / labels / metadata:** Inter (the text companion to Inter Display). Weights 400 and 500.
- **Reasoning:** Free, fast-loading, broadly available on Squarespace's font picker (Inter and Source Serif Pro both ship as standard Google Fonts options inside Squarespace's Typography panel). Modern editorial sans + contemporary serif body pair without licensing cost.
- **Avoid:** Lora, Playfair, Times New Roman, Cormorant. These read templated.

---

## 7. Conversion / Intake Detail

Per `competitive-research.md` §3, phone-first intake outperforms form-first for plaintiffs employment work. Implementation:

- Phone number visible in three places on the homepage: header, hero, footer (and in section 9 final CTA — that's four).
- The phone number should be a `tel:` link so it's tappable on mobile.
- Office hours stated in the footer ("Mon-Fri, 9am-6pm ET" or similar — be honest about real availability).
- "Free, confidential consultation" language used on all CTAs.
- Form lives at `/contact`, not embedded on the homepage. Fewer fields the better: Name, Email, Phone, Brief description of what happened, honeypot anti-spam. With confidentiality + attorney-advertising disclaimer below.

---

## 8. What's Not Yet Drafted (open items before paste-in)

- [x] ~~**Phone number string**~~ — **(212) 680-4040** (RingCentral). Locked across all five content files 2026-05-30.
- [x] ~~**Office address**~~ — **469 7th Avenue, 12th Floor, New York, NY 10018**. Locked across all five content files 2026-05-30. *Note: currently a virtual office within Executive Offices of New York. Steven plans to upgrade to a leased physical office at the same building/address within 1–2 months; the street address remains stable across the transition, which means no directory or letterhead updates needed when the lease is signed. GBP filing still waits for the lease per `gbp_timing.md` memory.*
- [x] ~~**Office hours**~~ — **Monday–Friday, 9:00 am – 6:00 pm ET. After-hours consultations by appointment.** Locked across all content files 2026-05-30.
- [ ] **Headshot photo** of Steven (professional, neutral background) — *must be newly commissioned. The Lawyer Monthly cover image is NOT available per the P&A partnership agreement.*
- [ ] **Press logos** — need clean PNG/SVG versions of the *Lawyer Monthly*, *Authority Magazine*, *Beyond Exclamation* publication wordmarks (the publications' own marks, not P&A material)
- [ ] **Bio review** for P&A-lifted language — `content-bio-page.md` needs Steven's line-by-line confirmation that each phrase is original to him and did not appear on his P&A attorney profile
- [x] ~~**Final palette decision**~~ — **Aubergine `#2A1B2F`** locked 2026-05-30
- [x] ~~**Typography**~~ — **Inter Display + Source Serif Pro** locked 2026-05-30
- [x] ~~**Hero option selection**~~ — **Option A (focused/boutique) as hero**, with Option C ("I believe victims. I stand with victims.") used as the Section 3 Mission Pull-Quote — locked 2026-05-30
- [x] ~~**Hero geography**~~ — **NYC-only** in hero; NJ admission named in bio, disclaimer, footer, admissions row — locked 2026-05-30
- [x] ~~**Phone service**~~ — **RingCentral**, with a number Steven purchased from a reseller and ported in. Locked 2026-05-30. Number: **(212) 680-4040**.
- [ ] **6 vs. 5 values** for section 7 (layout-dependent)
- [ ] **Settlement consent / anonymization review** — confirm each verdict/settlement called out in §5 is OK to publish in its current form

---

## 9. Build Order (recommended sequence in Squarespace)

1. Set palette + typography globally first
2. Build nav + footer (visible on every page)
3. Build the long-form pages first (About, each Practice Area sub-page, Results, Press, Contact) — *not* the homepage
4. Build the homepage *last*, pulling teasers + links from the long-form pages now that they exist
5. Pre-launch QA pass: phone tap-to-call, every internal link, mobile, page speed, schema markup
6. Connect domain (Setup Guide Phase 2 Step 4)
7. Submit sitemap to Google Search Console within 24 hours of going live

Reason for building homepage last: every homepage section links to a destination. Building destinations first means the homepage construction is just teaser-writing and linking, not parallel content authoring.
