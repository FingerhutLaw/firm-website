# Migration Setup Guide — Fingerhut Law Group
**Moving to: Squarespace (website) + Google Workspace (email)**
**Domain stays at: Hostinger (you keep full control)**

---

## Overview

You are setting up three things independently:
1. **Google Workspace** — powers all @fingerhutlawgroup.com email
2. **Squarespace** — hosts your website
3. **Hostinger DNS** — the control panel that points your domain at both

Do these in order. The whole process takes about 1–2 hours of your time spread over a day or two (some DNS changes take up to 48 hours to propagate, though usually much faster).

---

## PHASE 1 — Sign Up for Google Workspace (Do This First)

Email is more critical than the website. Set this up first so your inbox is never down.

### Step 1: Go to workspace.google.com
- Click **Get Started**
- Enter your business name: **Fingerhut Law Group**
- Number of employees: **Just you** (you can add users later)
- Your current email (for account recovery): stevenfingerhut@gmail.com

### Step 2: Choose your domain
- When asked "Does your business have a domain?", select **Yes, I have one I can use**
- Enter: `fingerhutlawgroup.com`

### Step 3: Create your Google Workspace account
- Create your primary email address: `sfingerhut@fingerhutlawgroup.com`
- Set a strong password

### Step 4: Choose a plan
- Select **Business Starter** — $7/user/month (billed monthly) or $6/user/month (billed annually)
- You only need 1 user to start. You can add more addresses later.

### Step 5: Verify your domain (in Hostinger)
Google needs to confirm you own fingerhutlawgroup.com. They will give you a **TXT record** to add in Hostinger.

1. Copy the TXT record Google gives you (looks like: `google-site-verification=xxxxxxxx`)
2. Log in to **Hostinger** → go to **hPanel** → **DNS / Zone Editor** for fingerhutlawgroup.com
3. Add a new **TXT record**:
   - Host/Name: `@`
   - Value: paste the code Google gave you
   - TTL: 3600 (or default)
4. Save it, go back to Google, click **Verify**

> Verification usually completes within a few minutes, sometimes up to an hour.

### Step 6: Set up MX records (this switches your email to Google)

After verification, Google will show you the **MX record** to add. As of 2024, Google uses a single simplified MX record:

| Priority | Mail Server |
|---|---|
| 1 | SMTP.GOOGLE.COM |

In Hostinger DNS, **delete any existing MX records** for fingerhutlawgroup.com first (they point to Hostinger's mail servers), then add the one above. Google may also ask you to add a TXT record (SPF: `v=spf1 include:_spf.google.com ~all`) to prevent outgoing mail from being marked as spam — add whatever Google shows you on the screen.

> Once it propagates (usually 1–4 hours), all email to @fingerhutlawgroup.com routes through Gmail/Google.
> Note: the older 5-record setup (ASPMX.L.GOOGLE.COM + 4 ALT records) still works if you already have it, but new accounts use the single SMTP.GOOGLE.COM record.

### Step 7: Test your email
- Go to **mail.google.com** and sign in with sfingerhut@fingerhutlawgroup.com
- Send a test email to yourself (from your Gmail personal account)
- Confirm it arrives in the Google Workspace inbox

### Step 8: Add additional email addresses (optional, do anytime)
In Google Workspace Admin (admin.google.com):
- Go to **Directory → Users → Add new user**
- Suggested addresses to create:
  - `info@fingerhutlawgroup.com` (general inquiries)
  - `intake@fingerhutlawgroup.com` (new client intake)
- Each additional user costs $7/month. Alternatively, you can create **email aliases** (free) that forward to your main sfingerhut@ inbox — good option if it's just you for now.

---

## PHASE 2 — Set Up Squarespace

### Step 1: Go to squarespace.com and create an account
- Click **Get Started**
- Choose a template — for a law firm, look at templates in the **Professional Services** or **Business** categories. Clean, minimal, dark navy or charcoal themes read as authoritative.

### Step 2: Choose a plan
- Select **Business** — ~$23/month (billed annually at ~$276/year)
- This includes unlimited pages, professional email marketing, and no transaction fees

### Step 3: Build your site
Start with these pages (you already have the content drafted in this resources folder):
- **Home** — short headline, your value proposition, call-to-action button
- **About / Steven Fingerhut** — use `content-bio-page.md`
- **Practice Areas** — list your areas (sexual harassment, discrimination, retaliation, etc.)
- **Results** — pull the notable verdicts and settlements from your bio
- **In the News / Media** — use `content-media-page.md`
- **Contact** — form + phone number + note about free consultations

### Step 4: Connect your domain (do NOT transfer — just connect)

In Squarespace:
1. Go to **Settings → Domains → Use a Domain I Own**
2. Enter `fingerhutlawgroup.com`
3. Squarespace will show you DNS records to add

In Hostinger DNS, add the records Squarespace gives you. They will typically be:
- **A record**: `@` → points to Squarespace's IP address
- **CNAME record**: `www` → `ext-cgi.squarespace.com` (or as shown)

> ⚠️ Do NOT change your nameservers to Squarespace's nameservers — that would give Squarespace control over your entire DNS. Only add the specific A and CNAME records they list.

### Step 5: Wait for DNS propagation
- Usually 1–4 hours, sometimes up to 48 hours
- Once live, visiting fingerhutlawgroup.com will show your Squarespace site

---

## PHASE 3 — Clean Up Hostinger

Once both are confirmed working:

1. **Cancel Hostinger email** — you no longer need it (Google Workspace handles email now)
2. **Keep your domain registration at Hostinger** — do NOT cancel this. Your domain renewal is separate from hosting. Just make sure auto-renew is on so you don't accidentally lose the domain.
3. **Cancel Hostinger hosting/website plan** — if you had one, cancel it. Keep only the domain registration.

---

## Summary Checklist

- [ ] Sign up for Google Workspace ($7/mo)
- [ ] Verify domain ownership via TXT record in Hostinger DNS
- [ ] Add Google MX records in Hostinger DNS
- [ ] Test sfingerhut@fingerhutlawgroup.com in Gmail
- [ ] Add info@ and intake@ as aliases or users
- [ ] Sign up for Squarespace Business (~$23/mo)
- [ ] Build site using content files in this resources folder
- [ ] Connect fingerhutlawgroup.com to Squarespace via DNS (A + CNAME records only)
- [ ] Confirm website is live at fingerhutlawgroup.com
- [ ] Cancel Hostinger email and website hosting
- [ ] Keep Hostinger domain registration active with auto-renew ON

---

## Monthly Cost After Migration

| Service | Cost |
|---|---|
| Squarespace Business | ~$23/mo |
| Google Workspace (1 user) | $7/mo |
| Hostinger (domain registration only) | ~$1–2/mo |
| **Total** | **~$31–32/mo** |

*Add $7/mo per additional Google Workspace user as you hire staff.*

---

## If You Get Stuck

- **Google Workspace setup help:** workspace.google.com/support or call 1-877-355-5787
- **Squarespace DNS help:** squarespace.com/help → search "connect a domain"
- **Hostinger DNS help:** support.hostinger.com → search "DNS zone editor"
- **Or just come back here** — paste any error message or screenshot and I'll walk you through it.
