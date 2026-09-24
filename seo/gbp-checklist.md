# Google Business Profile Checklist — GD Pro Web Designs

**Status (2026-09-24):** §1 Categories and §2 Services both done (both pending Google
review). §8 Ownership confirmed. §3 NAP mismatch confirmed and the user decided to file a
DBA — exact City of Everett process/fee/requirements researched and documented below,
ready to act on. §4 Service area checked (state-level MA + RI already set, RI confirmed
intentional — layering in individual towns deferred to a future session). §6 Reviews
mostly done — replied to the one existing review, got the real review short-link, added
the `/review` redirect (committed, not yet uploaded live), drafted a post-project email
ask template. §5, 7, 9 not yet started. **Correction:** the "not yet started" status this
file originally carried for §2 (and assumed for §4, §6) was wrong — the live listing
already had substantial prior, undocumented work (extensive services list, state-level
service area). Always check the live listing before assuming a checklist item is
untouched. This is the parallel,
user-run track from the Organic Lead Growth Plan
(`~/.claude/plans/majestic-napping-whisper.md`) — it gates the "near me" query layer
(e.g. "freelance website designer near me" 306 impr @ pos 50.5) that the site alone can't
fully win. Nothing here touches the codebase; it's all done inside the Google Business
Profile dashboard (business.google.com) or, for §3, in person at Everett City Hall.

**Why now:** also the recommended fix path for the intermittent AI Mode mixup where
Google attaches Budō Creative's (Malden, MA) listing to GD Pro Web Designs mentions —
a stronger, more complete profile reduces the odds of being substituted by a nearby
competitor. See the `google_ai_mode_business_mixup` memory for the fuller diagnosis;
check with the user whether the two Google reports from 2026-08-20 were ever submitted
before assuming this is still open.

---

## 1. Categories — ✅ DONE 2026-09-24 (pending Google review, ~10 min)
- [x] Primary category: **Website designer** (already set)
- [x] Secondary categories added: **Marketing agency**, **Internet marketing service**,
      **Software company**
- [x] Confirmed via live listing — no stale/incorrect category was set

## 2. Services — ✅ DONE 2026-09-24 (2 gaps filled, pending Google review, up to 1 day)
- [x] **Existing list was already extensive**, not empty as originally assumed — includes
      SEO Services, PPC management service, Digital marketing, Wordpress development,
      Custom Wordpress plugin development, Website Maintenance & Support, Graphics
      Designer, Logo Design, Hosting services, and a long tail of niche vertical services
      (Web design for construction companies, Web design & SEO for tree services company,
      etc. — matching the contractor-SEO pillar work). Confirmed against the live listing
      before touching anything, rather than assuming this checklist's "not started" note
      was still accurate.
- [x] Two genuine gaps identified and added as custom services: **Shopify development**
      and **Social media marketing** (matching the listing's existing lowercase,
      plain-wording style).
- [ ] Per-service descriptions (GBP allows a one-line description per service) — not yet
      reviewed/added; low priority given how complete the list already is.

## 3. NAP consistency (byte-identical everywhere) — ⚠️ KNOWN MISMATCH, confirmed 2026-09-22
- [ ] **Business name mismatch, not yet resolved:** the live GBP listing currently shows
      as **"JA Armira (freelance web designer)"**, not "GD Pro Web Designs" — Google
      required proof of business registration in Everett, MA, and since "GD Pro Web
      Designs" was never filed as a legal/DBA name, the listing had to be renamed to the
      user's personal name to stay verified. Every other branded instance of the business
      (website `<title>`s, footer, JSON-LD `ProfessionalService`/`Organization` name,
      citations below) still says "GD Pro Web Designs." This is a real, current NAP
      inconsistency, not a hypothetical one — and a plausible contributing factor to the
      `google_ai_mode_business_mixup` memory (Google occasionally attaches Budō Creative's
      listing to GD Pro Web Designs mentions; a GBP name that doesn't match its own
      website is a weaker entity signal, more prone to being resolved to the wrong place).
- [ ] **Real fix — user decided 2026-09-24 to proceed with filing.** Confirmed with the
      actual City of Everett Business Certificate (DBA) application PDF
      (`cityofeverett.com/wp-content/uploads/2026/07/Application-Business-Certificate-DBA-002-1.pdf`,
      MGL Ch. 110 §5):
      - **In person only** — Everett's own instructions require in-person filing (state
        law technically allows mail in some towns, but Everett's sheet doesn't offer it).
      - **Where:** City Clerk's Office, Everett City Hall, 484 Broadway, Everett, MA 02149.
        Phone 617-394-2225. Hours: Mon &amp; Thu 8am&ndash;7:30pm, Tue&ndash;Wed 8am&ndash;5pm
        (closed Fri&ndash;Sun).
      - **Fee — discrepancy in the city's own paperwork, confirm by phone before going:**
        the info sheet says $95.00 (not incl. notarization); the certificate form itself
        prints $60.00 in its official-use box.
      - **Bring:** business name ("GD Pro Web Designs"), physical business address (no PO
        box &mdash; presumably the Lawrence St. address), owner's full name/home
        address/phone, a photo ID, and **SSN or Federal EIN** (mandatory on the bundled
        state REAP tax-compliance attestation &mdash; the certificate won't be issued
        without it).
      - **Signed under oath in front of the clerk** (they act as notary on the spot, no
        separate notary trip needed), along with the REAP attestation and a Workers' Comp
        Insurance Affidavit &mdash; as a sole proprietor with no employees, check box #2
        ("no workers' comp insurance required") on that form.
      - **Valid 4 years** from filing date, then needs renewal.
      - **Once filed:** submit the certificate as proof to Google to get the GBP listing
        renamed from "JA Armira (freelance web designer)" back to "GD Pro Web Designs."
- [ ] Until/unless that happens, decide deliberately whether to (a) keep pushing "GD Pro
      Web Designs" as the brand everywhere else and treat GBP as the one exception, or
      (b) start reflecting "JA Armira, freelance web designer" more consistently to match
      the now-legal name. Don't silently let this drift — it should be a conscious choice.
- [ ] Address: **Lawrence St., Everett, MA 02149**
- [ ] Phone: **(617) 771-0645**
- [ ] Cross-check address/phone against the homepage `ProfessionalService` JSON-LD and
      footer string — these are the canonical source (CLAUDE.md Business Info table). Any
      mismatch (abbreviation, suite number, formatting) is a NAP-consistency ranking risk.

## 4. Service area — checked 2026-09-24, mostly deferred
- [x] **Checked the live listing first** (correcting the original assumption this was
      empty): Service area is already set at the **state level** — `Massachusetts, USA`
      and `Rhode Island, USA`. Not a town-by-town list.
- [x] **Rhode Island confirmed intentional** by the user 2026-09-24 — a real target
      market, not an accident. Do not remove it in a future pass without asking again.
- [ ] **Deferred, not done:** layering in individual high-value towns on top of the state
      -level entries (GBP allows both broad + specific areas together, not
      mutually exclusive). Google generally caps service areas around 20 entries per
      listing, so "match all 41 real WP town pages" (the original plan below) isn't
      literally achievable — would need a prioritized subset instead, e.g. by GSC search
      demand: Everett, Chelsea, Somerville, Malden, Medford, Revere, Cambridge, Newton,
      Quincy, Lynn, Saugus, Waltham, plus the North Shore tier (Peabody, Salem, Beverly,
      Marblehead, Swampscott, Danvers) — per `organic_lead_growth_plan` memory town
      priority list. Picked up again whenever the user wants to continue.
- [ ] Live WP town-page count confirmed 2026-09-24 via `/gd-blog/service-area/`: **41
      actual town pages** (plus a separate `we-serve-the-entire-usa` nationwide page,
      not a town — exclude from any GBP town list). This supersedes the stale "47 towns
      as of 2026-09-11" figure from `seo/town-facts.yml` — always pull the live list, not
      the static snapshot.
- [x] No fake/duplicate physical location was set — confirmed the listing correctly uses
      the one real address (57 Lawrence St., Everett) + a service-area list, same
      NAP-safety principle already applied to the WP town pages' schema (see the entity
      fragmentation fix in `wp_rest_access_and_town_pages` memory).

**Also noticed while checking (§9-adjacent, not part of §4):** the live GBP hours don't
match CLAUDE.md's documented "Mon–Fri 9:00–18:00" — actual live hours show Saturday
9:00 AM–1:00 PM (not in CLAUDE.md at all) and Wednesday ending at 5:00 PM instead of 6:00
PM like the other weekdays. Worth reconciling in §9 (or updating CLAUDE.md) — not
touched yet, flagging so it's not lost.

## 5. Posts (weekly cadence)
- [ ] Set a recurring reminder/process to post weekly — repurpose:
      - New blog posts (`/gd-blog/gd-news/`, and the new "Remote & National Services"
        category posts)
      - Completed project launches (portfolio additions)
      - Seasonal offers or service reminders
- [ ] Each post: photo/image, short copy, a CTA button (Call Now / Learn More →
      linking to the relevant page)

## 6. Reviews — mostly DONE 2026-09-24
- [x] **Checked current state first:** only **1 review total** (5.0★, Cristian Ruiz, Jul
      20 2016 — over 9 years old) despite 21+ years in business. Never had an owner reply
      until now. This is the real starting point, not the "no reviews at all" the
      checklist originally implied.
- [x] **Replied to the existing review** (posted via Business Profile Manager, pending
      Google review ~10 min): "Thank you so much for the kind words, Cristian — really
      appreciate you taking the time to leave this. It means a lot, especially looking
      back on it after all these years! If you ever need any updates or additional work
      down the road, don't hesitate to reach out. — JA"
- [x] **Got the real GBP review short-link** from the dashboard's Share panel:
      `https://g.page/r/CY2l1DPJt5fMEAI/review` — verified live via `curl -I` (302
      redirect, real Google endpoint).
- [x] **Created the redirect** — `gdprowebdesigns.com/review` → that link, added to
      `.htaccess` (commit `f6ecb08`) as a `RewriteRule ... [R=301,L]` matching this repo's
      established pattern (not the plain `Redirect 301` directive originally guessed
      here). **Not yet uploaded to the live server** — needs the usual FTP/cPanel File
      Manager deploy + `curl -I` live verification per the standard `.htaccess` workflow
      (see CLAUDE.md's deployment gotchas).
- [x] **Post-project email ask template drafted and approved:**
      Subject: "A quick favor, if you have 60 seconds" — short body thanking the client,
      asking for a review, linking `gdprowebdesigns.com/review`, signed JA Armira / GD
      Pro Web Designs. Not yet wired into any actual send process (no CRM/automation) —
      it's a copy-paste template for now, living in this checklist's git history and the
      `gbp_checklist_progress` memory.
- [ ] **Not done:** actually using the template on a real completed project, and turning
      "respond to every review" into an ongoing habit rather than a one-time catch-up.

## 7. Citations (external NAP consistency)
- [ ] Audit/create listings with byte-identical NAP on:
      - Yelp
      - BBB
      - Clutch
      - LinkedIn Company Page (already exists per CLAUDE.md — verify NAP match)
      - Bing Places
      - Apple Business Connect
      - Local MA business directories (e.g. chamber of commerce, Everett/Boston local
        directories)
- [ ] Flag and fix any citation with an old address, old phone format, or a business
      name variant (e.g. "GDWebPros" vs "GD Pro Web Designs" — pick one and standardize,
      note both forms appear in CLAUDE.md's Business Info table)

## 8. Ownership / access — confirmed 2026-09-22
- [x] Confirmed: GBP **Primary Owner is `jorgelemus080@gmail.com`** — same account as
      Search Console. `ja@gdprowebdesigns.com` also has manager-level access. See
      `google_account_identity_history` memory for the full chain.
- [ ] `gddomain.77@gmail.com` (the account used day-to-day) is NOT yet confirmed as an
      Owner on the GBP listing — recommended: from `jorgelemus080@gmail.com`, add
      `gddomain.77@gmail.com` as an Owner (not just Manager) so future work doesn't require
      logging into the older account each time.
- [ ] This ownership chain is also the blocker for any Business Profile API automation —
      whoever does the one-time OAuth authorization has to be logged into the Primary
      Owner account (or an Owner-level account it delegates to).

## 9. Quarterly audit
- [ ] Search the business name + "Everett MA" / "web design" periodically and check for
      duplicate or rogue listings (a second, unclaimed, or merged profile). This is the
      same class of issue as the Budō Creative AI Mode mixup — Google has already shown
      it can misattribute this entity, so a recurring check catches it early rather than
      waiting for the user to notice a lost lead.
- [ ] Re-check photos are current (team/work samples, not stock)
- [ ] Confirm hours are still accurate (Mon–Fri 9:00–18:00 per CLAUDE.md)

---

## Sequencing note

This has no code dependency and can run in parallel with anything else — it was flagged
in the plan as "user, ongoing" effort with "high impact for the near-me layer." Per the
plan's phase table, it doesn't block or get blocked by the static-site/WP phases; do it
whenever there's a spare cycle, ideally starting now since the AI Mode mixup gives it
extra urgency beyond pure SEO.
