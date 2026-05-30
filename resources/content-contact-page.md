# Website Content — Contact Page

*The page where the worker decides whether to contact the firm. The job is to make it easy, signal availability, and remove anxiety.*
*Suggested URL slug: /contact*

---

## Page Headline (H1)

**Contact Fingerhut Law**

## Sub-headline

A free, confidential consultation about your employment law matter.

---

## Page Body — Above the Form

### Three Ways to Reach the Firm

**Call** — *(212) 680-4040*
Monday through Friday, 9:00 am – 6:00 pm ET. After-hours consultations available by appointment.

**Email** — sfingerhut@fingerhutlawgroup.com

**Send a message through the form below.** Steven will respond within one business day.

> *Note: Information sent through this form or by email is not protected by the attorney-client privilege until a representation has been confirmed in writing. Please do not share sensitive details about your matter until we have spoken. See the [Disclaimer](/disclaimer).*

---

## Contact Form Specification

The form should have these fields and no more. Per the competitive research (`competitive-research.md` §4), shorter forms convert better and a NY plaintiff-side employment firm does not need a 12-field intake on the website — the phone call or first meeting is the real intake.

| Field | Type | Required | Notes |
|---|---|---|---|
| Full name | Text | Yes | |
| Email address | Email | Yes | Validated |
| Phone number | Tel | No | Recommended; explain why below |
| Best way to reach you | Dropdown (Phone / Email / Either) | Yes | Helps Steven respect the worker's preference |
| Brief description of your situation | Textarea | Yes | "A sentence or two is plenty — we will talk through the rest by phone." |
| Honeypot | Hidden | — | Anti-spam, invisible to humans |

**Do not include** a captcha — they read paranoid for a small firm and depress conversion. A honeypot field plus Squarespace's built-in spam filtering is sufficient.

**Submission button label:** *Send Message* (not "Submit" — friendlier)

**After submission, show this success message** instead of redirecting:

> Thank you. Your message has been received. Steven will respond personally within one business day.
> If your matter is time-sensitive, please call **(212) 680-4040**.

---

## Page Body — Below the Form

### What to Expect After You Submit

1. **Within one business day**, Steven will email or call you back — whichever you indicated as your preference on the form.
2. He will ask a few questions to understand the basics of your situation.
3. If the matter falls within the firm's practice and there is no conflict of interest, he will schedule a longer, free consultation by phone or video.
4. If the firm cannot help — because the matter is outside the practice, because there is a conflict, or because of timing — Steven will tell you and, where possible, point you toward an attorney who can.

There is no obligation to retain the firm and no fee for the initial consultation.

### Privacy and Confidentiality

The firm treats every inquiry with discretion. As noted above, information you share before signing a written engagement agreement is not protected by the attorney-client privilege — but it is treated with care and is not shared outside the firm. See the [Privacy Policy](/privacy) for detail on how the firm handles personal information.

### Deadlines Matter

Employment claims in New York have short deadlines — sometimes as short as 180 days to file with the EEOC, and three years for many claims under New York State and New York City law. If you have a claim, the longer you wait, the more options narrow. If you are unsure whether your situation involves a deadline that is approaching, that is a good reason to call rather than email.

---

## Footer (page-level — separate from the site-wide footer)

**Fingerhut Law Group, PLLC**
469 7th Avenue, 12th Floor
New York, NY 10018
Telephone: (212) 680-4040
Email: sfingerhut@fingerhutlawgroup.com
Office hours: Monday through Friday, 9:00 am – 6:00 pm ET. After-hours consultations by appointment.

---

## Editorial / Design Notes

- **Layout:** Left column holds the three contact channels + page-level footer info; right column holds the form. On mobile, the three channels stack first, then the form.
- **No address until the office lease is signed.** Per `gbp_timing.md`, the firm cannot list a virtual or coworking address as "the office" on Google Business Profile without GBP suspension risk. Whether to list a similar virtual address publicly *here* before the lease is signed is a closer call — addresses on the website are not the same kind of policy violation as GBP — but Steven should think about whether the visible address matches the address he will eventually use for GBP. If they will differ, leave the address off the site or replace it with "New York, NY · By appointment" until the lease is in place.
- **Phone tap-to-call.** Every phone number on this page should be a `tel:(212)xxxxxxx` link so it's tappable on mobile.
- **Form spam protection:** honeypot only. Avoid Squarespace's optional CAPTCHA — adds friction without much value at this volume.
- **Form storage:** Squarespace stores form submissions on Squarespace's servers and emails Steven a copy. The Squarespace storage is reflected in the Privacy Policy ("Hosting and form processing: Squarespace"). If Steven later moves to a CRM-based intake (Clio Grow, Lawmatics), this page and the Privacy Policy both need updating.
- **No live chat widget.** Per `competitive-research.md`, live-chat reads cheap on a boutique site, especially because the worker is often funneled to a non-attorney intake person. Phone or form is more honest.
- **Confidentiality language.** Repeated intentionally — once near the top, once near the bottom, once in the footer. Reduces the chance that someone treats the form as a privileged communication.

---

## What's not yet drafted on this page

- [x] ~~**Phone number**~~ — (212) 680-4040 (RingCentral). Locked 2026-05-30.
- [x] ~~**Office hours**~~ — Monday through Friday, 9:00 am – 6:00 pm ET. After-hours consultations by appointment. Locked 2026-05-30.
- [x] ~~**Office address**~~ — 469 7th Avenue, 12th Floor, New York, NY 10018. Locked 2026-05-30. (Virtual office at Executive Offices of New York; address remains stable when Steven upgrades to leased space in same building.)
