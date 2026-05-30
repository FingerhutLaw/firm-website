# DKIM + DMARC Follow-up — Fingerhut Law Group

**Status as of 2026-05-26:** Email migration to Google Workspace is complete. SPF, MX, and a basic DMARC record are in place. **DKIM still needs to be added**, and DMARC should be tightened later once you've been monitoring it.

---

## What's already done

| Record | Status | Value |
|---|---|---|
| MX | Done | `smtp.google.com` priority 1 |
| SPF (TXT @) | Done | `v=spf1 include:_spf.google.com ~all` |
| DMARC (TXT _dmarc) | Done — monitor only | `v=DMARC1; p=none` |
| Google domain verification (TXT @) | Done | `google-site-verification=A5Mu85yviyMZB-aVdVAzg_ISsEyGOK5ULHBnj7Jyw7Y` |
| DKIM | **NOT DONE** | — |

---

## Step 1 — Add DKIM (15 min, do once site is live)

DKIM cryptographically signs your outgoing mail so recipients can verify it really came from your domain. Without it, a portion of your emails to corporate recipients (especially Microsoft 365) may land in spam.

### Generate the key in Google

1. Go to **admin.google.com**
2. Navigate to: **Apps → Google Workspace → Gmail → Authenticate email**
3. Make sure `fingerhutlawgroup.com` is selected in the dropdown
4. Click **Generate new record**
5. Choose **2048-bit** key length
6. Click **Generate**
7. Google will show you a TXT record with:
   - **DNS Host name:** `google._domainkey`
   - **TXT record value:** a long string starting with `v=DKIM1; k=rsa; p=...`
8. Copy both — leave this browser tab open

### Add the record in Hostinger DNS

1. Log in to **hpanel.hostinger.com**
2. **Domains** → fingerhutlawgroup.com → **Manage** → **DNS / Nameservers**
3. Click **Add Record**:
   - **Type:** TXT
   - **Name:** `google._domainkey`
   - **Content:** paste the long `v=DKIM1; k=rsa; p=...` value
   - **TTL:** default (3600)
4. Save

### Activate in Google

1. Wait about 1 hour (some sources say up to 48 hours, but usually within an hour)
2. Go back to the Gmail Authenticate email page in Google Admin
3. Click **Start authentication**
4. Status should change to "Authenticating email with DKIM"

### Verify it's working

Send a test email from `sfingerhut@fingerhutlawgroup.com` to your personal `stevenfingerhut@gmail.com`. Open the message in Gmail, click the three-dot menu → **Show original**. Look for:
- `SPF: PASS`
- `DKIM: 'PASS' with domain fingerhutlawgroup.com`  ← this is what you want to see
- `DMARC: 'PASS'`

---

## Step 2 — Tighten DMARC (do ~4–8 weeks after DKIM is live)

Your current DMARC is `p=none` which means "monitor only, don't block bad mail." That's the safe starting policy. Once DKIM has been live for a month and you haven't seen any deliverability issues, tighten it.

### Edit the existing DMARC record in Hostinger

Find the TXT record with **Name** `_dmarc` and change the **Content** to:

```
v=DMARC1; p=quarantine; rua=mailto:sfingerhut@fingerhutlawgroup.com; pct=100; adkim=s; aspf=s
```

What this does:
- `p=quarantine` — mail that fails SPF+DKIM goes to recipient's spam folder (rather than being delivered or rejected)
- `rua=mailto:...` — DMARC aggregate reports get emailed to you weekly so you can see who's trying to send mail as your domain
- `adkim=s` and `aspf=s` — strict alignment (the domains in the From: header must exactly match the SPF/DKIM signing domain)

### After another 4–8 weeks at quarantine

If everything's still fine and the DMARC reports look clean, upgrade to **`p=reject`** — this tells recipients to outright refuse mail that fails authentication. This is the gold-standard for stopping spoofing of your domain.

```
v=DMARC1; p=reject; rua=mailto:sfingerhut@fingerhutlawgroup.com; pct=100; adkim=s; aspf=s
```

---

## Why bother with all this?

For a law firm, this matters more than for a typical small business:
- **Deliverability** — opposing counsel, courts on Microsoft 365, and HR departments at Fortune 500s increasingly require DKIM and respect DMARC. Without these, your emails about deadlines may quietly miss the inbox.
- **Anti-spoofing** — `p=reject` prevents anyone from sending mail that *looks like* it came from `@fingerhutlawgroup.com`. That's a real concern for a plaintiff-side employment firm where adversaries are sometimes motivated to impersonate.

---

## Quick reference — final desired DNS state

After all of this is done, your Hostinger DNS should contain (for email purposes):

| Type | Name | Content |
|---|---|---|
| MX | @ | `smtp.google.com` (priority 1) |
| TXT | @ | `v=spf1 include:_spf.google.com ~all` |
| TXT | @ | `google-site-verification=A5Mu85yviyMZB-aVdVAzg_ISsEyGOK5ULHBnj7Jyw7Y` |
| TXT | `google._domainkey` | `v=DKIM1; k=rsa; p=...` (very long, from Google) |
| TXT | `_dmarc` | eventually `v=DMARC1; p=reject; rua=mailto:sfingerhut@fingerhutlawgroup.com; pct=100; adkim=s; aspf=s` |
