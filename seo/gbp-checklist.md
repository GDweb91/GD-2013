# Google Business Profile Checklist — GD Pro Web Designs

**Status:** Not yet started. This is the parallel, user-run track from the Organic Lead
Growth Plan (`~/.claude/plans/majestic-napping-whisper.md`) — it gates the "near me"
query layer (e.g. "freelance website designer near me" 306 impr @ pos 50.5) that the
site alone can't fully win. Nothing here touches the codebase; it's all done inside the
Google Business Profile dashboard (business.google.com).

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

## 3. NAP consistency (byte-identical everywhere)
- [ ] Business name: **GD Pro Web Designs**
- [ ] Address: **Lawrence St., Everett, MA 02149**
- [ ] Phone: **(617) 771-0645**
- [ ] Cross-check against the homepage `ProfessionalService` JSON-LD and footer string —
      these are the canonical source (CLAUDE.md Business Info table). Any mismatch
      (abbreviation, suite number, formatting) is a NAP-consistency ranking risk.

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

## 8. Ownership / access
- [ ] Confirm the profile is verified and owned by an account the user actually
      controls day-to-day — given the tangled Google identity across `ja@gdprowebdesigns.com`
      / `jorgelemus080@gmail.com` / `gddomain.77@gmail.com` (see
      `google_account_identity_history` memory), check which account currently owns/manages
      the GBP listing before assuming access is fine. Don't assume an unfamiliar owner
      email is a compromise — it's likely the user's own tangled identity, but verify.

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
