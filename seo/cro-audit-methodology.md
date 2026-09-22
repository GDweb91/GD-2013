# CRO Audit Methodology

**Purpose:** the repeatable process to actually deliver on the live [Conversion Rate Optimization (CRO) Services](https://gdprowebdesigns.com/gd-blog/conversion-rate-optimization-services/) page (id 292) when a client hires you for it. That page promises: *"a real audit of your current site's conversion path... analytics review... specific, prioritized fixes... before/after tracking."* This document is how that promise actually gets delivered, step by step.

**Related:** [[national_remote_clients_plan]] (where the CRO service page came from) · `seo/keyword-intent-map.md` P4 cluster #7

---

## 1. Client Onboarding — What to Request First

Before any audit work starts, request access to:

| Access needed | Why | If they don't have it |
|---|---|---|
| **Google Analytics 4** (Viewer or Analyst role) | Real traffic, behavior flow, and conversion-event data | Can't do a real audit without this — GA4 access is non-negotiable |
| **Google Search Console** | Confirms which queries/pages actually drive the traffic being evaluated | Helpful but not blocking |
| **Microsoft Clarity** (or existing heatmap tool: Hotjar, etc.) | Real click maps, scroll depth, session recordings, rage-click detection | If they don't have one, **install Clarity** (free, ~5 min setup via GTM or direct script tag) — this becomes step 0 of the engagement, and itself generates the visual evidence the audit report will use |
| **CMS/site admin** (or at least the ability to inspect page source) | Confirms actual form field counts, CTA markup, checkout steps — don't take screenshots at face value | Read-only front-end review still works, just slower |
| **E-commerce platform access** (Shopify/WooCommerce admin), if applicable | Real cart-abandonment rate, checkout funnel steps, payment options | Ask for the platform's own analytics dashboard export at minimum |

**If the client has no analytics or heatmap tool installed at all:** the engagement starts with a 1-2 week data-collection window after installing GA4 + Clarity, before the audit itself can be meaningful. Say this upfront — auditing a site with zero behavioral data is guessing, not CRO.

---

## 2. Data-Gathering Phase

### 2a. GA4 — pull via the `gsc-ga4` MCP tool (or GA4 UI if client access isn't MCP-connected)
- **Landing pages by sessions + conversion rate** — which pages get traffic, which of those actually convert
- **Device breakdown** (mobile vs. desktop conversion rate) — mobile often converts worse and gets ignored
- **Traffic source × conversion rate** — paid traffic converting worse than organic is a landing-page mismatch problem, not a CRO problem
- **Funnel/path exploration** (if GA4 Explore is set up) — where in a multi-step flow (e.g., product page → cart → checkout → purchase) people actually drop off
- **Engagement rate + average engagement time** on key pages — a proxy for whether the page is actually being read

### 2b. Microsoft Clarity — heatmaps + recordings
- **Click maps** on the top 3-5 landing pages — are people clicking things that aren't clickable (a sign of a confusing layout)? Are they NOT clicking the actual CTA?
- **Scroll depth** — if the real CTA is below the point where most visitors stop scrolling, that's a structural problem, not a copy problem
- **Rage clicks / dead clicks** (Clarity flags these automatically) — direct evidence of a broken or confusing element
- **5-10 session recordings** on the highest-traffic landing page — watch real visitors use the site; this surfaces friction no analytics number will show you

### 2c. Manual walkthrough — do this yourself, on both desktop and mobile
Actually go through the conversion path as a visitor would: land on the page, try to find the offer, try to fill out the form or complete checkout. Note every point of hesitation.

---

## 3. Audit Checklist — What to Actually Look At

### Message clarity (first 5 seconds)
- [ ] Can a first-time visitor tell what the business does within 5 seconds of landing, with no scrolling?
- [ ] Is the value proposition specific (not generic "quality service, great prices")?
- [ ] Is there a single clear next action, or does the page present 5 different competing CTAs?

### Forms
- [ ] Field count — every field beyond name/email/phone/message is a reason to abandon; is each one actually necessary?
- [ ] Is the form above the fold, or does a visitor have to scroll to find it?
- [ ] Are error states clear (not a vague "something went wrong")?
- [ ] Does the form work correctly on mobile (no zoomed-in tiny inputs, no keyboard covering the submit button)?

### Calls-to-action
- [ ] Is the primary CTA visually distinct (color, size, contrast) from every other button/link on the page?
- [ ] Does the CTA copy say what happens next ("Get a Free Quote" beats "Submit")?
- [ ] Is the CTA repeated at natural decision points on long pages, not just once at the top?

### Trust signals
- [ ] Reviews, testimonials, or ratings visible near the point of decision (not buried on a separate page)
- [ ] Real contact info (phone number, address) visible, not hidden behind a contact form only
- [ ] Security/payment trust badges near checkout, if e-commerce

### Page speed & mobile
- [ ] Core Web Vitals (LCP, CLS, INP) via PageSpeed Insights — slow pages lose conversions before a visitor ever reads the copy
- [ ] Mobile-specific layout issues (overlapping elements, text too small, tap targets too close together)

### E-commerce checkout specifically (if applicable)
- [ ] Number of steps from cart to completed purchase — every extra step is a drop-off point
- [ ] Guest checkout available, or is account creation forced?
- [ ] Shipping costs shown early, not as a surprise at the final step
- [ ] Payment method variety (does it match what the target customer actually expects to use?)

---

## 4. Deliverable — Report Structure

Match what the CRO service page promises: **prioritized, specific fixes**, not a generic audit template dump.

1. **Executive summary** — top 3-5 issues found, ranked by expected impact vs. effort to fix
2. **Evidence per issue** — the specific screenshot, heatmap, or analytics number that shows the problem (never a claim without evidence behind it)
3. **The fix** — specific and actionable ("move the CTA above the fold and change the copy from X to Y"), not vague ("improve the CTA")
4. **Priority tier**: Quick win (implement this week) / Medium (next sprint) / Structural (needs a bigger conversation, e.g. "your checkout needs 2 fewer steps")
5. **Before/after measurement plan** — which specific metric (form completion rate, add-to-cart rate, checkout completion rate) will confirm the fix worked, and over what time window

---

## 5. Pricing & Scoping (matches the live service page)

- Engagement starts with a **paid audit** scoped to the site and goals — not a free generic report
- Implementation of the fixes can be **one-time** (a project) or folded into the **$450/month** ongoing marketing retainer alongside SEO
- If the client has zero behavioral data (no GA4, no heatmap tool), the audit engagement includes a 1-2 week setup + data-collection window before findings are delivered — set this expectation during the sales conversation, not after the client is already impatient for a report

---

## 6. What NOT to Do

- **Don't recommend a fix without evidence.** "Best practices say X" is not the same as "your Clarity recordings show visitors abandoning at X."
- **Don't audit a page with near-zero traffic as if it were a priority.** Fix the highest-traffic, highest-intent pages first.
- **Don't promise a specific conversion lift number.** CRO findings are directional and testable, not guaranteed percentages — avoid the kind of overpromising that erodes trust when a fix underperforms.
