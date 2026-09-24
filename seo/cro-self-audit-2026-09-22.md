# CRO Self-Audit — gdprowebdesigns.com — 2026-09-22

**Purpose:** first real-world run of `seo/cro-audit-methodology.md`, against GD's own site — both a genuine conversion-health check and a dry run before offering this as a paid client service. Data sources: GA4 property `362005686` (last 90 days via `gsc-ga4` MCP), Google Search Console (`https://gdprowebdesigns.com/`, last 90 days), live-site walkthrough via browser.

**Not yet done:** Microsoft Clarity heatmaps/recordings weren't pulled in this pass (no MCP/API access to Clarity from this session — needs manual login). Recommended as the immediate next step, see §6.

---

## 1. Executive Summary — ranked by impact

| # | Issue | Impact | Effort to fix |
|---|---|---|---|
| 1 | **Lead/phone conversion tracking appears to have stopped working since 08-07, and a bogus "contact-form_submit" event is firing on pages with no contact form in its place** | Critical — GA4 currently shows zero trustworthy lead data of any kind | Low (GTM config fix) |
| 2 | **Homepage bounce rate 83%, avg. session 22s, over last 90 days** | High — the highest-traffic page on the site is losing the large majority of visitors almost immediately | Medium (needs traffic-quality triage first, see #1) |
| 3 | **"Direct / (none)" traffic is 93% of all sessions (426 of 458) and has by far the worst engagement (15%) of any channel** | High — this looks like non-human traffic, which is inflating session counts and hiding real visitor behavior | Low (GA4 traffic filtering) |
| 4 | Homepage ranks position ~45.5 in Google for the query set driving 13,056 impressions, at 0.21% CTR | Medium — SEO/CTR issue, not a page-CRO issue, but suppressing the organic traffic this CRO work would otherwise convert | Longer-term (ranking work, out of CRO scope) |
| 5 | Hero section message clarity | Low — reviewed live, this is actually fine (see §3) | N/A |

---

## 2. Evidence Per Issue

### Issue 1 — Contact-form_submit event over-firing (CRITICAL)

GA4 event counts, last 90 days, by page:

| Page | page_view | contact-form_submit | Ratio |
|---|---|---|---|
| `/` (homepage) | 384 | 207 | 54% |
| `/PPC-adwords-advertising-boston.html` | 8 | 8 | 100% |
| `/web-design-company-boston-ma.html` | 13 | 10 | 77% |
| `/about-gd-freelance-web-designer-boston.html` | 12 | 9 | 75% |
| `/portfolio-graphics-design-boston-everett-ma.html` | 7 | 6 | 86% |

**Total: 288 `contact-form_submit` events in 90 days, across the whole site.** None of these pages contain an actual HTML `<form>` element — confirmed by grepping the static repo (`grep -n "<form" index.html footer.php header.php` returns nothing) and by the fact that this event fires on pages like the PPC service page and portfolio page, which have never had a contact form on them. The static site's contact form was retired in favor of `/gd-blog/contact-us` (a WordPress page) per `CLAUDE.md`; the legacy jQuery `.contact-form` handler in `js/custom.js` (~line 1083) is dead code with no matching element on any current page.

**Cross-referenced against `ga4_event_tracking_status` memory (documented 2026-07-14 through 08-07):** the *correct*, currently-intended lead-tracking setup is a Page View trigger scoped to `/gd-blog/thank-you/`, feeding a GA4 event named `fill_out_email_form` — driven by a dataLayer/trigger event named `contact_form_submit` (underscore). That memory also documents that the **original** approach (before the 07-17 redesign) was a Custom HTML tag called `CH-CF & Form Submit Listener` that attached a `wpcf7mailsent` listener to the page, and that this old tag was described as "no longer needed" once the Page-View approach replaced it — but nothing in that memory confirms it was actually deleted or paused in GTM.

The event this audit found live in GA4 is named **`contact-form_submit`** (hyphen, not underscore) — matching neither the documented trigger name (`contact_form_submit`) nor the final GA4 event name (`fill_out_email_form`). Combined with the fact that it fires on pages with zero forms, at high fixed ratios regardless of page content, the most likely explanation is that **the old `CH-CF & Form Submit Listener` Custom HTML tag (or something similarly leftover) was never actually removed from GTM**, and either fires unconditionally on a broad trigger (e.g. "All Pages") or has a scoping bug that pushes its dataLayer event outside the intended listener callback. This is a hypothesis to verify in the GTM UI, not a confirmed root cause — but it gives the user a specific, named tag to go look for first instead of searching blind.

Cross-check: despite 288 firings, **GA4's own `conversions` metric returns 0 for every single dimension pulled** (page, device, channel, event) — meaning this event either isn't marked as a Key Event right now, or was un-marked (plausibly during the GA4 property deletion/relink incident resolved 2026-08-20 — see `ga4_property_deletion_gsc_relink` memory).

**More important: the full 90-day event list (9 distinct event names total, not truncated) contains no `fill_out_email_form` and no `click_to_call` at all** — the two GA4 event names that `ga4_event_tracking_status` memory documents as "DONE, confirmed firing in production, both marked as GA4 Key Events" as of 2026-08-07. Only the raw trigger-side name `phone_click` appears, exactly once, in 90 days. This means the **documented, previously-working lead/phone tracking appears to have stopped sending data to GA4 at some point since 08-07** — plausibly during or after the 08-20 property-deletion/relink incident. Right now, GD Pro Web Designs has zero visibility into real lead volume through GA4: the intended events aren't showing up, and the one event that IS firing at volume (`contact-form_submit`) is fabricated and disconnected from real forms.

**This needs to be checked in GTM directly** (only the account owner has that access) — open the `GTM-N4P95M5` container, find the tag firing on the `contact-form_submit` event/trigger, and check what it's actually bound to. This is a 5-10 minute fix once found, but it can't be diagnosed further from outside GTM's admin UI.

### Issue 2 — Homepage bounce rate / engagement

| Metric | Homepage, 90d |
|---|---|
| Sessions | 355 |
| Bounce rate | 80% (83% desktop-only) |
| Engagement rate | 20% |
| Avg. session duration | 22 seconds |

For comparison, Organic Search traffic sitewide (19 sessions) has a 63% engagement rate — 3x better than the site average, which is dragged down by the Direct-channel volume in Issue 3. This suggests the real, human-driven engagement on this site is reasonably healthy; the aggregate numbers are being diluted by something else.

### Issue 3 — Direct/(none) traffic dominance and quality

| Source / Medium | Sessions (90d) | Bounce rate | Avg. duration |
|---|---|---|---|
| (direct) / (none) | 426 | 85% | 19s |
| google / organic | 18 | 33% | 109s |
| chatgpt.com / ai-assistant | 3 | 33% | 19s |
| bing / organic | 1 | 100% | 5s |

426 of 458 total sessions (93%) are unattributed "Direct" traffic with an 85% bounce rate and 19-second average duration — a profile more consistent with bot/crawler traffic or referrer spam than real visitors typing the URL or using a bookmark. Real Direct traffic to a business site this size (no major ad campaigns, no brand recognition at national scale) at this volume would be unusual on its own; combined with the bounce/duration profile and the fact that the fabricated `contact-form_submit` events are concentrated on exactly these low-engagement sessions, non-human traffic is the more likely explanation than a sudden surge of real repeat visitors.

**Not confirmed as bot traffic — flagged as the most likely explanation given the evidence, not a certainty.** Worth checking GA4's "Traffic Acquisition" report filtered to Direct, cross-referenced with server access logs, for user-agent patterns.

### Issue 4 — Homepage SERP position/CTR

GSC (90 days): homepage has 13,056 impressions, 28 clicks, 0.21% CTR, average position 45.5. At position 45 (page 4-5 of Google), a sub-1% CTR is expected and not itself a CRO defect — it's a ranking problem, which is squarely the local-SEO initiative's territory (`organic_lead_growth_plan` memory), not this audit. Flagged here only because it caps how much organic traffic ever reaches the page this audit is evaluating.

### Issue 5 — Manual walkthrough of the hero (homepage, live, 2026-09-22)

Reviewed live via browser. The hero: clear H1 ("Web Designer & WordPress Developer Near Boston, MA"), specific subhead, one visually distinct gold primary CTA ("Free Consultation") plus a secondary outlined CTA ("See Our Services"), visible phone number, and 5 trust badges (WordPress Expert, SEO Certified, Since 2005, Hablamos Español, Affordable Pricing) all above the fold. This passes the "5-second clarity" and "single distinct CTA" checklist items cleanly — **no fix needed here.** A mobile-viewport screenshot comparison was attempted but the browser tool's window resize didn't change the rendered viewport in this session, so mobile-specific layout wasn't independently verified this pass; the GA4 mobile numbers (19 sessions, 47% engagement) are too small a sample (90 days, single-digit traffic) to draw a layout conclusion from either way.

---

## 3. Fixes — Specific and Actionable

1. **Open GTM container `GTM-N4P95M5` → search for `CH-CF & Form Submit Listener`** (the old, supposedly-retired Custom HTML tag per `ga4_event_tracking_status` memory) **and any tag/trigger referencing `contact-form_submit`.** Check what trigger it's actually bound to; pause or delete it if it's the leftover pre-07-17 tag. This is the highest-priority item; nothing else in this audit (or any future CRO work on this site) is measurable until it's fixed.
2. **Separately confirm the *intended* tracking is still healthy**: `fill_out_email_form` (real lead event, Page View trigger on `/gd-blog/thank-you/`) and `click_to_call` (phone clicks) should still be firing and marked as Key Events — re-verify both weren't affected by the 08-20 property-deletion/relink incident, since this audit's `conversions` pull came back 0 across the board, which is inconsistent with either event working correctly.
3. **Filter or exclude bot/spam traffic in GA4** (Data Filters, or a Direct-traffic user-agent check) once #1 is fixed, so future engagement/bounce numbers reflect real visitors.
4. Re-run this audit's Section 2a/2b data pull 30 days after #1-#3 are fixed, to get a clean baseline.

---

## 4. Priority Tiers

- **Quick win (this week):** #1 (GTM fix) and #2 (Key Event re-mark) — both configuration-only, no code/content changes.
- **Medium (next check-in):** #3 (traffic filtering), plus pulling Microsoft Clarity heatmaps/recordings once real traffic is confirmed (Clarity was not checked this pass).
- **Structural / longer-term:** #4 (homepage ranking/CTR) — belongs to the local-SEO initiative, not this CRO track.

---

## 5. Before/After Measurement Plan

Once #1-#3 are fixed, track for 30 days and compare against this baseline:
- **Real contact-form submissions** (once tracking is trustworthy) — target: any number > 0 that can be trusted, since the current 288 is known-fake
- **Direct-channel session count and bounce rate** — expect both to drop sharply once bot traffic is filtered
- **Homepage engagement rate** — expect it to rise once diluting bot sessions are removed, isolating real visitor behavior

---

## 6. What's Still Needed (not done in this pass)

- **Microsoft Clarity heatmaps/session recordings** — confirmed installed sitewide (per `national_remote_clients_plan` memory) but not pulled this session; no Clarity API/MCP access available. Recommend a manual login pass once the GTM issue is fixed, so recordings reflect real traffic.
- **Core Web Vitals (PageSpeed Insights)** — the public PSI API returned HTTP 429 (rate-limited without an API key) this session. Recommend running `https://pagespeed.web.dev/analysis?url=https://gdprowebdesigns.com/` manually, or re-running with an API key.
- **Manual mobile-viewport walkthrough** — the browser automation tool's resize didn't change the rendered page this session; worth a manual phone check.
