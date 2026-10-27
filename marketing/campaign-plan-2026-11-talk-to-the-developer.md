# Campaign Brief — "Talk to the Developer"

**Prepared:** 2026-10-27 · **Run:** Mon Nov 3 – Fri Dec 26, 2026 (8 weeks) · **Paid budget:** $300–500/mo
**Goal type:** Lead generation (calls + contact forms), non-SEO channels

---

## Baseline (GA4 property 362005686, Sep 25 – Oct 26, 2026)

| Signal | Last 30 days | Read |
|---|---|---|
| Completed contact forms (`Fill_out_email_form`, thank-you page) | **9** | User confirms most were real prospects |
| Phone clicks (`click_to_call`) | **1** | Calls dialed directly / from Google Business Profile aren't in GA4 |
| Form submit attempts (`form_submit`) | 45 | 45 vs 9 completions — check for blocked spam vs. real failures (Week 0) |
| Organic Search sessions | 23 | Search sends very few visitors |
| Direct sessions | 323 (22% engaged, ~all homepage) | Mostly bot-like; not real demand |

**Takeaway:** the site converts the real visitors it gets, but very few real visitors arrive. This campaign adds visitors and calls from channels outside organic search.

---

## 1. Campaign Overview

- **Name:** Talk to the Developer
- **Summary:** An 8-week push to get Greater Boston small business owners to call or message the person who will actually build their website, using Google Business Profile, past clients, a tight Google Ads test, and case-study posts.
- **Primary objective:** **50 leads in 8 weeks** (completed forms + phone clicks + GBP calls + ad calls), vs. ~19 at the current pace.
- **Secondary objectives:**
  - Google reviews **1 → 9** (+8)
  - **3 signed projects or care plans** attributed to the campaign
  - A Google Ads cost per lead you can decide on keeping (target ≤ $80)

## 2. Target Audience

**Primary: local service business owners.**
Owner of a 1–20 person service business (contractor, restaurant, cleaning, tree service, health practice, professional services) in Everett, Chelsea, Malden, Revere, Medford, Somerville or Boston. Their website is outdated, missing, or not bringing calls. They look for help on Google ("web designer near me"), on Google Maps, and through referrals from other owners. They care most about price certainty, speed, and someone who answers the phone.

**Secondary: Spanish-speaking business owners.**
Latino-owned businesses in Chelsea, East Boston, Everett, Revere and Lynn. Few designers serve them in Spanish, and the portfolio already includes restaurant sites for this market. They're reached through Facebook, local business groups, and word of mouth.

**Tertiary: "my WordPress site is broken" (urgent).**
Any owner whose site is hacked, down or erroring. They search with high intent and decide fast. This is the best fit for paid search.

| Pain point | Motivation | Buying stage |
|---|---|---|
| "Agencies are expensive and I never talk to the person doing the work" | Price certainty, one point of contact | Consideration |
| "My site looks old / doesn't bring calls" | More customers from Google | Consideration → decision |
| "My site is broken right now" | Fix it today | Decision |
| Language barrier with English-only vendors | Being understood | Consideration |

## 3. Key Messages

**Core message:** Work directly with a Boston-area web developer: agency-quality websites, flat-rate pricing, and a real person who answers the phone.

| Supporting message | Proof point |
|---|---|
| You talk to the developer, not an account manager | Freelance studio since 2005; agency-vs-freelance comparison on `wordpress-developer-boston-ma.html` |
| Flat-rate pricing, no surprises | Websites from $1,800; WordPress from $2,500; repair minimum $150 |
| Built to bring calls, not just look nice | Google SEO + Digital Marketing certificates; sites built with SEO, speed and call tracking |
| Local, and we speak Spanish | Based in Everett, 3 miles from Boston; restaurant sites for Chelsea, Everett, East Boston clients |

**Variations by channel:**
- **GBP and ads:** short, local, direct ("Everett web designer, flat-rate, call today").
- **LinkedIn:** a professional case-study voice.
- **Facebook:** friendly and neighborly, plus Spanish versions.
- **Past-client email:** personal, first person, from JA.

**Offer that runs through all channels:** a **free 15-minute website check**. Call or book, and get three specific fixes for your site, whether or not you hire. It gives a low-commitment reason to call now.

## 4. Channel Strategy

| Channel | Why it fits | Format | Effort | Budget |
|---|---|---|---|---|
| **Google Business Profile** | Map-pack results drive "near me" calls; currently only 1 review (2016) holds it back | 1 post/week (8), portfolio photos, review push, Q&A, fix hours mismatch | Low | $0 |
| **Past clients (<20)** | Warmest leads: reviews, referrals, repeat work and care plans | 3 personal emails + a follow-up call to each | Low | $0 |
| **Google Ads (Search)** | Captures people searching right now; tests whether paid leads are worth it | 2 ad groups (web design; WordPress fix/repair), ~10-mile radius around Everett, business hours, call assets | Medium | $400/mo (≈$13/day) |
| **LinkedIn + Facebook (organic)** | Credibility; owners see local work they recognize | 2 posts/week: case studies from the portfolio, before/after, tips; Spanish versions on Facebook | Medium | $0 |
| **Local communities** | Neighbor referrals; Spanish-speaking market | Join 2–3 Everett/Chelsea/Malden business Facebook groups; answer questions, no spam. Optional: Chamber of Commerce | Medium | $0 (Chamber optional; check price) |

**Google Ads setup essentials:**
- **Keywords:** phrase and exact match only. Examples: "web designer near me", "small business website design boston", "wordpress developer boston", "fix wordpress site", "wordpress site hacked help".
- **Negative keywords from day 1:** jobs, salary, course, free, template, DIY, Wix, Squarespace, internship.
- **Landing pages:** `web-design-company-boston-ma.html` for web design; `fix-wordpress-issues-boston-ma.html` for repair.
- **Tracking:** import the GA4 key events `click_to_call` and `Fill_out_email_form` as conversions, and turn on call reporting for call assets.

## 5. Content Calendar

| Week | Dates | Content piece | Channel | Notes / dependencies | Status |
|---|---|---|---|---|---|
| 0 | Oct 28 – Nov 2 | Upload the 49 pending static pages (CSS versioning + hours 9:00–6:30 structured data) | Website | **DONE 10-27**: all 49 verified on origin; last Cloudflare copies refresh by ~2:45 PM. `/review` redirect confirmed live | ☑ |
| 0 | | Stray duplicate found 10-27: `/shopify-developer-boston-ma-ecommerce.html` (root, Oct 10, not in repo) duplicates `shopify/…`. Delete from server or 301 to `shopify/` version | Website | Low priority, SEO hygiene | ☐ |
| 0 | | Set GBP hours to **Mon–Fri 9:00 AM – 6:30 PM, closed Sat/Sun** (remove Saturday 9–1, fix Wednesday). Site structured data already updated 10-27 | GBP | | ☐ |
| 0 | | Test the contact form end to end; check DebugView for `Fill_out_email_form`; look into 45 submits vs 9 completions | GA4 | Tracking has broken 3× before; check before spending | ☐ |
| 0 | | Create or verify Google Ads account, link GA4, import conversions | Ads | **Must finish before ads launch** | ☐ |
| 1 | Nov 3 | Past-client email #1: personal check-in + review ask (direct review link) | Email | Send to all; call anyone with no reply by Friday | ☐ |
| 1 | | GBP post #1: "Free 15-minute website check" offer + portfolio photo | GBP | | ☐ |
| 1 | | LinkedIn + FB: "Who builds your website?" agency vs. freelance post; case study #1 | Social | | ☐ |
| 2 | Nov 10 | **Google Ads launch** (both ad groups) | Ads | Needs Week 0 tracking done | ☐ |
| 2 | | GBP post #2: case study (restaurant site) | GBP | | ☐ |
| 2 | | FB (Spanish): "Diseño web para negocios latinos en Chelsea / Everett" + restaurant portfolio | Social | | ☐ |
| 3 | Nov 17 | Past-client email #2: referral ask ("know a business owner whose site needs help?") | Email | | ☐ |
| 3 | | GBP post #3: WordPress repair: "site down? call today" | GBP | | ☐ |
| 3 | | Ads review #1: search terms report, add negatives | Ads | 20 minutes | ☐ |
| 4 | Nov 24 | GBP post #4: Thanksgiving hours + Small Business Saturday (Nov 28) | GBP | Light week | ☐ |
| 4 | | LinkedIn: case study #2 (contractor site) | Social | | ☐ |
| 5 | Dec 1 | **Mid-campaign report** (leads by channel, ads CPL, reviews) | All | Shift ad budget toward the better ad group | ☐ |
| 5 | | Past-client email #3: care plan / "year-end website tune-up" offer | Email | | ☐ |
| 5 | | GBP post #5: new reviews spotlight (if any) | GBP | | ☐ |
| 6 | Dec 8 | "Plan your 2027 website now: book in December, launch in January" | GBP + Social + Ads copy | New-year planning angle | ☐ |
| 6 | | FB (Spanish) post #2 | Social | | ☐ |
| 7 | Dec 15 | GBP post #7 + LinkedIn case study #3 | GBP / Social | | ☐ |
| 7 | | Ads review #2: pause losers, keep winners | Ads | | ☐ |
| 8 | Dec 22 | GBP post #8: holiday hours / thank-you | GBP | | ☐ |
| 8 | Dec 26 | **Final report**: keep, change, or stop each channel for January | All | Run `marketing:performance-report` | ☐ |

About 20% of slots are left loose for reactive posts, such as a newly launched client site or a new review.

## 6. Content Pieces Needed

| Asset | Type | Contents | Priority | Create by |
|---|---|---|---|---|
| Past-client emails #1–3 | Email | Check-in + review ask; referral ask; care-plan / tune-up offer. Personal, from JA | Must | Oct 31 |
| Call script / "how did you hear about us?" log | Doc | One question on every call; simple tally by channel | Must | Oct 31 |
| GBP posts ×8 | GBP post | Offer, 3 case studies, repair, holiday, new-year, reviews | Must | Batch by Nov 1 |
| Google Ads copy | Search ads | 2 ad groups × 2 responsive search ads (15 headlines / 4 descriptions each), call asset, sitelinks | Must | Nov 7 |
| Ads keyword + negative list | Doc | Phrase/exact keywords, negatives | Must | Nov 7 |
| LinkedIn/Facebook posts ×12 | Social | Case studies from portfolio (sweepshimmercleaning, restaurants, contractor, tree service), agency-vs-freelance, tips | Must | Batch 4 at a time |
| Spanish Facebook posts ×3 | Social | Restaurant / local business focus | Must | Nov 7 |
| "Free 15-minute website check" landing page | Web page | Dedicated ad landing page with a short form | Nice-to-have (existing pages work for launch) | Week 4 if ads justify it |
| Review reply templates | Text | Thank-you reply for each new review | Nice | Nov 3 |

I can draft all of these with `marketing:draft-content` and `marketing:email-sequence`.

## 7. Success Metrics

| KPI | Target (8 wks) | Tracked in | Baseline |
|---|---|---|---|
| **Total leads** (primary) | **50** | GA4 `Fill_out_email_form` + `click_to_call`; GBP Performance → Calls; Google Ads call reporting; your call log | ~19 per 8 weeks |
| Google reviews | 1 → 9 | GBP | 1 |
| Google Ads cost per lead | ≤ $80 | Google Ads (GA4-imported conversions) | n/a |
| GBP calls + website clicks | +50% vs. Oct | GBP Performance | Pull Week 0 |
| Projects / care plans signed | 3 | Your records | n/a |

**Reporting cadence:**
- **Weekly (Fridays, 15 minutes):** lead count by channel.
- **Mid-campaign:** Dec 1.
- **Final:** Dec 26.
- **Attribution rule:** a direct phone call isn't tracked anywhere unless you ask "How did you find us?" Ask on every call.

## 8. Budget Allocation

| Item | Amount |
|---|---|
| Google Ads, Nov 10 – Dec 26 (~7 weeks at ~$13/day) | ~$650 |
| Contingency, held until mid-campaign review | ~$100 (≈13%) |
| Content production | $0 (Claude drafts; JA reviews and publishes) |
| Tools | $0 (GA4, GBP, Google Ads, free social) |
| Optional: local Chamber of Commerce membership | Check price (membership + networking events) |
| **Total cash** | **~$750 over 8 weeks** |

**Rule:** once the mid-campaign report is in, move budget to whichever ad group has the lower cost per lead. If ads produce 0 leads by Dec 1, pause them and put the time into referrals and GBP instead.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Ads spend on low-intent clicks (job seekers, DIY) | Phrase/exact match only, negative list from day 1, weekly search-terms review, business-hours schedule |
| Few past clients leave reviews | Personal ask with the one-click review link, follow-up phone call, ask right after a good interaction |
| Tracking silently breaks again (it has 3× before) | Week 0 DebugView test plus a manual call log; compare GA4 to the inbox weekly |
| Time: you're a solo operator | All posts and emails drafted up front in batches; about 1–2 hours a week to publish and respond |
| GBP still listed as "JA Armira" (DBA pending) | Reviews and posts still count; keep the DBA filing on the GBP checklist; ads use the GD Pro brand and domain |

## 10. Next Steps

1. **This week (Week 0):** upload the pending pages; confirm `/review` redirect live; decide true business hours and fix GBP; run the contact-form test.
2. **Decided 10-27:** offer = free 15-minute website check ✔; hours = Mon–Fri 9:00–18:30 ✔; Google Ads account already exists ✔ (verify billing + GA4 link in Week 0).
3. **Ads schedule:** Mon–Fri 9:00 AM – 6:30 PM so call ads only run while you can answer.
4. **Me:** draft the past-client emails, the first batch of GBP and social posts, and the ads copy plus keyword lists, ready for your review.
