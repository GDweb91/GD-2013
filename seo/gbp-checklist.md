# Google Business Profile Checklist — GD Pro Web Designs

**Status (2026-09-24):** §8 Ownership confirmed. §3 NAP mismatch confirmed and the user
decided to file a DBA — exact City of Everett process/fee/requirements researched and
documented below, ready to act on. Everything else (§1, 2, 4–7, 9) not yet started. This
is the parallel, user-run track from the Organic Lead Growth Plan
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

## 1. Categories
- [ ] Primary category: **Website Designer**
- [ ] Secondary categories: **Marketing Agency**, **Internet Marketing Service**,
      **Software Company**
- [ ] Confirm no stale/incorrect category is still set (check current profile first)

## 2. Services
- [ ] Populate the Services list to mirror the site's actual offerings — don't invent
      new service names, reuse the site's own wording:
      - Custom Web Design (from ~$1,800)
      - WordPress Development / WooCommerce (from ~$2,500)
      - Search Engine Optimization — local & national (from ~$450/mo)
      - Google Ads / PPC Management
      - Local Internet Marketing / Digital Marketing
      - Social Media Integration
      - Graphic Design & Branding
      - WordPress Maintenance & Troubleshooting
      - Shopify Development (new, per the national/remote-clients vertical)
- [ ] Add a one-line description to each service (GBP allows this) — reuse the site's
      own service-page copy rather than writing new claims

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

## 4. Service area
- [ ] Set GBP's service-area list to match the current published WP town-page list —
      pull the live list from `/gd-blog/service-area/` rather than a static snapshot,
      since it's grown since `seo/town-facts.yml` was last touched (47 towns as of
      2026-09-11, plus whatever's been added since). Include Everett itself plus the
      North Shore tier (Peabody, Salem, Beverly, Marblehead, Swampscott, Danvers) if
      not already present.
- [ ] Do **not** set a fake/duplicate physical location per town — GBP service-area
      businesses declare one real address + a service-area list, same NAP-safety
      principle already applied to the WP town pages' schema (see the entity
      fragmentation fix in `wp_rest_access_and_town_pages` memory).

## 5. Posts (weekly cadence)
- [ ] Set a recurring reminder/process to post weekly — repurpose:
      - New blog posts (`/gd-blog/gd-news/`, and the new "Remote & National Services"
        category posts)
      - Completed project launches (portfolio additions)
      - Seasonal offers or service reminders
- [ ] Each post: photo/image, short copy, a CTA button (Call Now / Learn More →
      linking to the relevant page)

## 6. Reviews
- [ ] Set up a post-project email ask (template: short, direct link, sent within a few
      days of project completion/launch while satisfaction is fresh)
- [ ] Create a short redirect — `gdprowebdesigns.com/review` → the GBP review link —
      so it's easy to say/type on a call. This is a `.htaccess` 301, one line, low risk:
      add `Redirect 301 /review https://g.page/r/...../review` (get the real GBP review
      short-link from the dashboard first)
- [ ] Respond to every review (good and bad) — signals an active, monitored profile

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
