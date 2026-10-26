---
# =============================================================
# CONTACT PAGE — /contact
# Edit any value below — the site updates instantly.
# =============================================================

title: "Contact Friedman & Fingerhut"
description: "Contact Friedman & Fingerhut for a free, confidential consultation about workplace discrimination, harassment, retaliation, or wrongful termination matters in New York and New Jersey."

# --- HERO ---
contactHeroLabel: "Contact"
contactHeroHeadline: "A free, confidential consultation."
contactHeroSubheadline: "If you believe your rights at work have been violated, a partner will personally review your inquiry and respond."

contactIntro: "Employment claims in New York have short deadlines — sometimes as short as 180 days to file with the EEOC. The fastest way to reach the firm is to call (212) 680-4040. If you prefer to write, submit the form below and a partner will respond within one business day."

# =============================================================
# FORM BACKEND
# Today: Formspree. Drop your Formspree form ID into formAction below
# (sign up at formspree.io, create a new form, copy the URL it gives you).
#
# To switch to a custom Astro endpoint later, change formAction to:
#   "/api/contact"
# (and build site/src/pages/api/contact.ts to handle the POST).
# Form field names (name, email, phone, message, _gotcha, _subject)
# stay the same — only this one URL changes.
# =============================================================

formAction: "https://formspree.io/f/xqeoeaey"
formSubject: "New consultation inquiry — Friedman & Fingerhut"
formSubmitLabel: "Send Inquiry"

# Full absolute URL. Formspree redirects here after a successful submission.
# Once the site is deployed at friedmanfingerhut.com, this routes users to
# the custom /contact/thanks page. In local dev, Formspree submissions still
# hit production — there is no dev-only redirect.
formSuccessRedirect: "https://friedmanfingerhut.com/contact/thanks"

# --- WHAT HAPPENS AFTER YOU SUBMIT ---
whatHappensHeading: "What happens after you submit"
whatHappens:
  - "A partner personally reviews every inquiry within one business day."
  - "A partner will reach out by phone or email to schedule a free, confidential consultation."
  - "All inquiries are kept confidential, whether or not the firm takes the matter."

# --- SIDEBAR (office info) ---
contactSidebarHeading: "Reach the firm"

# --- DISCLAIMER ---
contactDisclaimer: "Submitting this form does not create an attorney-client relationship. Do not include confidential information in your message. The firm will confirm any attorney-client relationship in a signed engagement letter before any privileged communication."
---

