# National / Remote Clients Content Plan

**Status:** Prerequisite (entity `@id` unification) DONE 2026-09-11. Wave 1 DONE, published & verified live 2026-09-11 (both pages, cross-linked from local static flagship pages). Wave 2 DONE 2026-09-11 (3 pages, drafts — not yet published).
**Source:** `long-tail-keywords-for-web-design-dev.pdf` (Desktop/Gemini-chats), reviewed 2026-09-11.
**Related:** [[organic_lead_growth_plan]] (the local/Everett-MA initiative this is a companion to, not a replacement of) · `seo/keyword-intent-map.md` (P4 section) · `wp_rest_access_and_town_pages.md` (WP REST credentials/workflow)

---

## What this is

A second, separate content vertical: national/remote clients who find GD Pro Web Designs through platform-specific and migration/urgency intent (not local geography). This is **not** a pivot away from the local Everett/Greater-Boston brand — it's an addition, kept deliberately distinct so it doesn't dilute the local `LocalBusiness`/`ProfessionalService` entity work already done in Phases 0–3.

**Platform decision: WordPress (`gd-blog`), not static HTML.** Reasoning (full discussion 2026-09-11):
- This content is shaped like articles/service pages, not conversion-funnel landing pages — WP's authoring model fits better than hand-coded static HTML.
- User's stated future plan is to add social media posting — WordPress has a natural publishing pipeline (RSS, social plugins) that static `.html` files don't.
- Avoids the FTP/cPanel deploy friction that has repeatedly caused problems on the static site (silent FTP failures, Bluehost edge-cache staleness).
- No existing static cluster to anchor to (unlike the contractor-SEO pillar, which had to sit next to `SEO-company-chelsea-ma.html`) — this is a brand-new vertical, so the "new pages → WP" default (per [[architecture_static_vs_wp]]) applies cleanly.

**Prerequisite handled first, not after:** the WP side's `Organization` schema was using its own `@id` (`https://gdprowebdesigns.com/gd-blog/#organization`) instead of the static site's canonical one (`https://gdprowebdesigns.com/#organization`) — a business-identity fragmentation issue. Fixed 2026-09-11 across three files (`gd-seo-core.php`, `single-service_city.php`, `service-area.php`) plus a filter added to `gd-seo-core.php` suppressing AIOSEO's own competing Person/Organization Knowledge Graph output (`aioseo_schema_graphs` filter, strips `KgPerson`/`KgOrganization`). Verified live on `service-area/somerville/`; homepage and `service-area/` index pending a stale edge-cache to clear (code confirmed correct via cache-busted requests). Building the new national vertical on top of an already-unified entity, not a fragmented one.

---

## Keyword clusters → content (from the PDF)

| # | Cluster | Keywords | Content | Type |
|---|---|---|---|---|
| 1 | WordPress core offer | revamp/rebuild wordpress website, custom wordpress development services, freelance wordpress developer remote, wordpress speed optimization services | **Flagship pillar**: "Freelance WordPress Developer — Remote, Nationwide" | WP Page |
| 2 | Wix → WordPress | wix to wordpress migration service | "Wix to WordPress Migration Service" | WP Page |
| 3 | WordPress → Shopify | wordpress to shopify developer | "WordPress to Shopify Developer" | WP Page |
| 4 | Shopify setup | shopify design and setup expert | "Shopify Design & Setup Expert (Remote)" — distinct from the existing Boston-branded `shopify/shopify-developer-boston-ma-ecommerce.html` on the static site | WP Page |
| 5 | Wix Studio | hire freelance wix studio designer | "Hire a Freelance Wix Studio Designer" — first Wix-specific content on either site | WP Page |
| 6 | Bundled: SEO+design | seo friendly web design services, wordpress seo expert consultant | "SEO-Friendly WordPress Web Design" | WP Page |
| 7 | Bundled: CRO | conversion rate optimization cro services | "Conversion Rate Optimization (CRO) Services" | WP Page |
| 8 | Bundled: Shopify marketing | shopify store marketing strategy | "Shopify Store Marketing Strategy" | WP Page |
| 9 | Comparison | WordPress vs Shopify for small business e-commerce | Comparison article | WP Post |
| 10 | Fixer/urgent | hire freelancer to fix hacked wordpress site | "Fix a Hacked WordPress Site" | WP Post |
| 11 | Fixer/urgent | fix shopify checkout speed | "Fix Shopify Checkout Speed" | WP Post |

**Pages vs. Posts split:** evergreen commercial-intent service pages (1–8) are WP Pages; the comparison and urgent/fixer content (9–11) are WP Posts in a new category, "Remote & National Services" — those are the ones that benefit from the future social-posting pipeline.

## Waves

- **Wave 1** ✅ DONE, published & live 09-11: #1 `remote-wordpress-developer` (id 277), #2 `wix-to-wordpress-migration` (id 278). Full-width no-sidebar template (`page-full-width.php`) built and deployed as part of this wave, after the default WP page template was found to add an unwanted sidebar + duplicate hero. Cross-linked from `wordpress-developer-boston-ma.html` (new FAQ #9) and `web-design-company-boston-ma.html` (Website Redesigns card) — pending upload. Also cross-linked with the pre-existing blog post `custom-website-design-or-diy` (both directions).
- **Wave 2** ✅ DONE, published & verified live 09-11: #3 `wordpress-to-shopify-developer` (id 285), #4 `shopify-design-setup-expert` (id 286), #5 `hire-freelance-wix-studio-designer` (id 287). All use `page-full-width.php` from creation (no template-fix detour needed this time). AIOSEO title + meta description set and verified live on all three. Page 286 has a placeholder mention of Shopify store marketing (no link yet — target page doesn't exist until Wave 3).
- **Wave 3** ✅ DONE, published & verified live 09-11: #6 `seo-friendly-wordpress-web-design` (id 291), #7 `conversion-rate-optimization-services` (id 292), #8 `shopify-store-marketing-strategy` (id 293). All use `page-full-width.php`. AIOSEO title + meta description set and verified live on all three. The page-286 placeholder mention of Shopify store marketing (from Wave 2) is now a real link to id 293, verified live.
- **Wave 4** ✅ DONE 09-11, drafts not yet published: #9 `wordpress-vs-shopify-small-business-ecommerce` (id 298), #10 `fix-hacked-wordpress-site` (id 299), #11 `fix-shopify-checkout-speed` (id 300). Built as WP **Posts** (not Pages), category "Remote & National Services" (id 13, newly created). Use the site's existing article structure (`<section id="content" class="container py-5"><article class="mx-auto col-lg-10">`) matching the pre-existing `custom-website-design-or-diy` post — posts keep the default sidebar (Search/Recent Posts widgets), which is the established, correct pattern for blog content on this site, unlike Pages.
  - **Caught and fixed:** REST-created posts default `author` to the `claude-seo` API user (id 3), which shows publicly as "by JA-claude SEO" in the byline. Reassigned all 3 to author id 2 (the real account) before review. See [[wp_rest_access_and_town_pages]] — this applies to any future REST-created content.

**Wave 1 + 2 fully wrapped as of 2026-09-11:**
- AIOSEO Title + Meta Description set and verified live on all 5 pages
- All 5 Wave 1+2 pages published and verified live
- Cross-links from local static pages done both directions:
  - `wordpress-developer-boston-ma.html` — new FAQ #9 → `remote-wordpress-developer`
  - `web-design-company-boston-ma.html` — Website Redesigns card → `wix-to-wordpress-migration`; new FAQ (wdf9) → `hire-freelance-wix-studio-designer`
  - `shopify/shopify-developer-boston-ma-ecommerce.html` — existing "outside of Boston" FAQ (#6) → both `shopify-design-setup-expert` and `wordpress-to-shopify-developer`; also added that FAQ to its JSON-LD (was visible-only before, a pre-existing gap unrelated to this project, fixed while there)
  - Existing blog post `custom-website-design-or-diy` ↔ `wix-to-wordpress-migration` (both directions)
- These 5 static-file edits are committed to local files only — not yet uploaded/pushed, per usual review-before-deploy workflow

**Still open:**
- Once Wave 3 exists: add the Shopify-marketing link in page 286 that's currently a plain-text placeholder

## Structural rules

- **Schema:** `Service` type (not `LocalBusiness`), `areaServed: "United States"` (or "Remote/Nationwide"), `provider` referencing the unified `https://gdprowebdesigns.com/#organization` — modeled on `contractor-seo-services-boston-ma.html`'s pattern (the closest existing non-geo-tied pillar precedent), adapted for WP page content (JSON-LD embedded via a Custom HTML block).
- **No fabricated client roster.** The contractor page used real named local clients for credibility; there's no equivalent evidence of existing national/remote clients, so these pages are written on service/process/pricing/credentials, not invented testimonials. Revisit if real remote clients exist to reference.
- **Internal linking:** cross-link from the local flagship pages (`wordpress-developer-boston-ma.html`, the static Shopify page) — "Not in Massachusetts? We also work with clients remotely, nationwide →" — captures spillover without cannibalizing local queries.
- **Cannibalization guard:** tracked in `seo/keyword-intent-map.md` P4 section so national and local clusters don't compete for the same query.
- **Social-ready:** each page/post keeps a few extractable, quotable statements (same spirit as the `.quick-answer` pattern on the static site) so this content can be repurposed into social posts later without a rewrite — per the user's stated future plan, not being built yet.
- **AIOSEO:** leave per-post Title/Meta Description blank where a sane default template exists, matching the rule already established for the Cities content type — avoid recreating the `%%post_title%%`-style template bug.

## Deferred (explicitly out of scope right now)

- Social media posting/distribution — user wants this later, once there's a body of content to distribute.
- Paid Google Ads — organic only for now, per user's answer 2026-09-11.
