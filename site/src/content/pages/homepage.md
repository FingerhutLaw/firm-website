---
# =============================================================
# HOMEPAGE COPY (v3 design, Nov 2026)
# Edit any value below — the site updates on the next build.
# Keep the field names (left of the colon) the same.
# Wrap text in "double quotes" if it contains special characters.
#
# Not in this file (set elsewhere):
#   - Google rating + review count: fetched automatically at build time
#     (site/src/lib/googleRating.ts). Fallback is 5.0 / 23.
#   - Consultation form endpoint: formAction in contact.md (shared with
#     the /contact page so both forms reach the same inbox).
# =============================================================

# --- HERO SECTION (top of homepage) ---
heroEyebrow: "For workers, never employers · NY & NJ"
# The H1 reads "<heroH1Lead> <heroH1Rest>". On phones, heroH1LeadShort
# is shown instead of heroH1Lead (screen readers always get the full one).
heroH1Lead: "New York & New Jersey"
heroH1LeadShort: "NY & NJ"
heroH1Rest: "Employment Lawyers"
heroDescription: "A focused practice for workers facing harassment, discrimination, retaliation, or a wrongful firing. The partners handle every case themselves."
heroCTAText: "Get a free consultation"
heroCTAHref: "#consult"
heroNote: "Free and confidential · No fee unless we win"
portraitImage: "/images/home/hero-partners.jpg"
portraitAlt: "Partners Steven Fingerhut and Joshua Friedman outside a Manhattan courthouse"
heroCaption: "Steven Fingerhut & Joshua Friedman, founding partners"

# --- PHONE NUMBER (used in hero + header + footer) ---
phone: "(212) 680-4040"
phoneHref: "tel:+12126804040"

# --- FEE NOTE (canonical — rendered site-wide on every closing CTA + footer) ---
# Edit this line and it updates everywhere. Honor the "where appropriate"
# framing — not every matter is contingency-eligible.
feeNote: "Free, confidential consultation — no obligation. No fee unless we obtain a recovery."

# --- PRESS STRIP ("As featured in", just below the stats) ---
# Plain name = text only. To link one, use:  - name: "Authority Magazine"
#                                              href: "https://..."
pressLabel: "As Featured In"
pressLogos:
  - "Lawyer Monthly"
  - "Authority Magazine"
  - "Beyond Exclamation"
  - "Super Lawyers"
  - "NELA"

# --- PRACTICE AREAS (6 cards + "Don't see your situation?" card) ---
practiceAreasHeading: "What we handle for New York and New Jersey employees."
practiceAreasCTA: "See all practice areas"
practiceAreasCTAHref: "/practice-areas"
practiceAreas:
  - name: "Sexual Harassment"
    tagline: "Harassed by a boss or coworker? Here is what to do first."
    href: "/practice-areas/sexual-harassment"
  - name: "Race Discrimination"
    tagline: "Federal, state, and NYC Human Rights Law protections."
    href: "/practice-areas/race-discrimination"
  - name: "Retaliation"
    tagline: "Fired after you complained? That can be its own claim."
    href: "/practice-areas/retaliation"
  - name: "Pregnancy Discrimination"
    tagline: "More protection during pregnancy, not less."
    href: "/practice-areas/pregnancy-discrimination"
  - name: "Disability Discrimination"
    tagline: "When an accommodation request became a firing."
    href: "/practice-areas/disability-discrimination"
  - name: "Wrongful Termination"
    tagline: "Not every firing is legal."
    href: "/practice-areas/wrongful-termination"
practiceAreasOtherHeading: "Don't see your situation?"
practiceAreasOtherBody: "Age, LGBTQ+, FMLA leave, whistleblowing, unpaid wages — tell us what happened."
practiceAreasOtherCTA: "Tell us what happened"

# --- RESULTS + REVIEWS (navy band, right after practice areas) ---
resultsLabel: "Results"
resultsHeading: "A track record of recoveries."
resultsCTA: "See more results"
resultsCTAHref: "/results"
results:
  - figure: "$2,000,000"
    description: "Race discrimination settlement for eleven construction workers."
  - figure: "$1,550,000"
    description: "Sexual harassment settlement for a content producer."
  - figure: "$1,300,000"
    description: "Whistleblower retaliation settlement for a head of data science."
  - figure: "$500,000+"
    description: "Federal jury verdict (E.D.N.Y., 2024), affirmed on appeal."
priorResultsNote: "Prior results do not guarantee a similar outcome."

# Client reviews — keep each quote exactly as the client wrote it on Google.
# A blank line inside a quote starts a new paragraph.
reviewsLabel: "What clients say"
reviews:
  - name: "Maggie J."
    quote: |
      Josh is genuinely the best lawyer you could ask for. He takes his time, explains every single detail and aspect in a way that is so easy to understand, and genuinely cares about his clients and the outcomes. I’ve been working with Josh for a bit now, and I’ve never once doubted his commitment to me as his client & to reaching an outcome that was in my best interest.

      I can’t recommend Josh & his firm enough.
  - name: "Joanna M."
    quote: |
      I cannot recommend Steve highly enough! He helped me navigate an incredibly difficult situation with a former employer… During an extremely stressful and uncertain time, he made me feel heard, supported, and confident that I had someone truly advocating for my best interests.

# --- HOW WE PRACTICE (homepage teaser; full text lives at /how-we-practice) ---
howWePracticeLabel: "How We Practice"
howWePracticeHeading: "We stand with workers. We believe survivors."
howWePracticeQuote: "The difference between a $200,000 case and a $2 million case is rarely the facts. It is almost always the strategy."
howWePracticeBody: "Between us, we have more than twenty-five years devoted exclusively to representing employees — never employers. We know how employers defend these cases, and we prepare every matter for trial. As the partners, we answer your questions, develop your strategy, take your depositions, and stand up in court for you."
howWePracticeCTA: "Read our full approach"
howWePracticeCTAHref: "/how-we-practice"
howWePracticeImage: "/images/home/courthouse-steps.jpg"
howWePracticeImageAlt: "Steven Fingerhut and Joshua Friedman on the courthouse steps"

# --- RECOGNITION (one line of honors; href makes it a link) ---
recognitionLabel: "Recognition"
recognition:
  - name: "Best Lawyers: Ones to Watch"
    href: "https://www.bestlawyers.com/lawyers/steven-fingerhut/261049"
  - name: "2026 Lawdragon 500 Leading Civil Rights & Plaintiff Employment Lawyers"
    href: "https://www.lawdragon.com/lawyers/friedman-fingerhut/joshua-m-friedman"
  - name: "Super Lawyers Rising Stars"
  - name: "Multi-Million Dollar Advocates Forum"
  - name: "AILC 10 Best"
  - name: "Lead Counsel Rated"
  - name: "Top 40 Under 40"

# --- IN THE NEWS (3 press cards) ---
# Leave href out (or set it to "#") to show a card without a "Read article" link.
newsHeading: "In the news."
newsCTA: "See all press"
newsCTAHref: "/press"
news:
  - publication: "Lawyer Monthly"
    tag: "Cover Feature"
    headline: "LGBT+ Inclusivity in the Workplace"
    href: "https://www.lawyer-monthly.com/2019/06/pride-yourself-at-work-lgbt-inclusivity-in-the-workplace/"
  - publication: "Lawyer Monthly"
    headline: "Fired after a sexual harassment complaint? What to do."
    href: "https://www.lawyer-monthly.com/2019/03/what-should-you-do-if-you-are-fired-after-filing-a-sexual-harassment-complaint/"
  - publication: "Beyond Exclamation"
    headline: "A Zealous Advocate for Employees Who Have Been Wronged"
    href: "https://beyondexclamation.com/steven-fingerhut-a-zealous-advocate-for-employees-who-have-been-wronged/"

# --- CONSULTATION (closes the page; every consultation button scrolls here) ---
finalCtaHeading: "If your rights at work have been violated, do not wait."
# Shown instead of finalCtaHeading on phones.
finalCtaHeadingShort: "Do not wait. Some deadlines are short."
finalCtaBody: "Employment claims have strict filing deadlines, and some run in months, not years. Tell us what happened and a partner will review it — free and confidential."
consultPoints:
  - "Free, confidential consultation"
  - "No fee unless we win"
  - "You speak with a partner, not an intake script"
consultFormHeading: "Request a free consultation"
consultSubmitLabel: "Request my free consultation"
consultDisclaimer: "Submitting this form does not create an attorney-client relationship. Please don't include confidential documents."
consultSuccess: "Thank you. A partner will review what you sent and contact you within one business day."
---

<!--
The homepage is all structured fields above, so this body is empty.
-->
