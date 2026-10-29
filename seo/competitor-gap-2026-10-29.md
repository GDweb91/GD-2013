# Competitor Keyword Gap — 2026-10-29

**Method (free version, no ranking database):** crawled competitor sitemaps + page titles/H1–H3, bucketed
by topic cluster, and compared against (a) GD's GSC queries for the trailing 12 months (2025-10-28 → 2026-10-26,
3,435 queries) and (b) GD's static + WP pages. Google autocomplete was used as a rough demand check.

**What this shows:** topics competitors *target* that GD doesn't. **What it can't show:** what they actually
*rank for*, or search volumes. GSC impressions stand in for demand. A cluster where GD gets impressions but has
no dedicated page is the strongest signal. To get real competitor rankings + volumes, export one Semrush Keyword Gap
CSV (7-day trial) or upgrade the connected Ahrefs plan to one with API access; the connected account currently returns "Insufficient plan".

Check every recommendation against `keyword-intent-map.md` before building so it doesn't cannibalize an existing page.

---

## Competitors examined

| Competitor | Base | Footprint | Threat to GD |
|---|---|---|---|
| **websitesusa.com** | Cambridge (national positioning) | ~355 URLs: **115 programmatic `/industry/*-web-design/` pages**, ~215 blog posts (WP error fixes, pricing/cost, comparisons, Boston listicles), one Boston page with a 3-tier pricing table | High on informational/long-tail; their industry pages are templated |
| **ebree.com** | Cambridge & Wakefield | ~40 URLs, almost all portfolio; homepage 77 words; niche = ExpressionEngine, accessibility, nonprofits/schools/arts | **Low.** Thin site; only the *accessibility* + *nonprofit* angles are worth noting |
| **cyberoptik.net** | Non-local agency with MA city pages | **15 MA city pages incl. `/web-design/everett-ma/`** (2,100 words), Medford, Somerville, Waltham, Quincy, Lawrence, Boston + far cities. 40 service pages incl. **16 "migrate X → WordPress" pages**, ADA/accessibility, hacked cleanup, speed, GBP management, Local Service Ads | **High.** Targets GD's home turf with a long, structured page |
| **creativemarketing.ai** | Malden/Revere city pages | 58 place pages (~480 words each, programmatic), 108 industry pages, 345 posts; "from $297/mo website + SEO" | Medium; thin pages, aggressive price anchor |
| LEX Marketing (Malden/Saugus) | Malden/Saugus | WP site has essentially 1 page; competes via BBB/GBP, not content | Low on content (GBP competitor only) |

Other names that surfaced for round 2: TheeDigital (Somerville service-area pages), Truly Good Design
(Somerville/Cambridge), Trellis (Malden, ecommerce), Roan Solutions (Everett, BBB), Digital Veer (Boston).

---

## Gap clusters, ranked

GSC numbers = 12-month impressions for GD, "p" = average position.

### Tier 1 — GD already gets impressions but has no dedicated page (act first)

| # | Cluster | GD evidence (GSC) | Competitor coverage | Recommended action |
|---|---|---|---|---|
| 1 | **Church / nonprofit web design** | church website design boston ma 94 @p29 · custom church website design boston ma 22 @p22 · non-profit web design MA · nonprofit WP maintenance (123 impr total, **no page**; the nonprofit page was deactivated → `boston-webdesign-for-non-profits-off.html`) | websitesusa `/industry/church-`, `/nonprofit-web-design/`; eBree's core niche; autocomplete: "church website design company / services" | **New WP page** "Church & Nonprofit Web Design — Boston" (revive the old content, redesign it). Also add the missing 301 for the old non-profit URL (open item in CLAUDE.md). |
| 2 | **Website redesign** | website redesign massachusetts 93 @p78 · website redesign near me 32 @p74 · website redesign services boston (137 impr, **no page**) | cyberoptik `/websites/website-redesign/`; websitesusa redesign-cost, redesign-checklist, signs-your-website-needs-a-redesign; autocomplete: full "website redesign cost" family | **New WP service page** "Website Redesign — Boston & MA", including a redesign-cost answer block. Supporting post: "Signs your site needs a redesign". |
| 3 | **Google Business Profile management** | gbp optimization services in boston 115 @p34 · google business profile optimization in boston 57 @p30 (187 impr) | cyberoptik `/marketing/google-business-profile-management/` + `/google-local-service-ads/` | **New WP service page** "Google Business Profile Optimization — Boston", or a strong H2 section on `local-marketing-company-…ma.html` if you'd rather not add a page. GD has done its own GBP work (see `gbp-checklist.md`), which gives the page firsthand material. |
| 4 | **Pricing / cost (supporting content)** | 216 cost/affordable queries, 9,316 impr; "boston web design pricing" already mapped to `web-design-company-boston-ma.html` | websitesusa "Web Design Prices in Boston" post + pricing table on its Boston page; "how much does SEO cost", "website maintenance cost", "ecommerce development cost" posts | **Don't build a competing pricing page.** Keep the money keyword on the flagship page (already in the intent map). Add 2–3 *informational* WP posts that link to it: "How much does a website cost in Boston (2026)", "How much does SEO cost for a small business in MA", "WordPress maintenance cost". Use GD's real prices ($1,800 / $2,500 / $450/mo / repairs from $150). |

### Tier 2 — zero GD impressions, competitors investing (new territory)

| # | Cluster | Competitor coverage | Recommended action |
|---|---|---|---|
| 5 | **WordPress error-specific fixes** | websitesusa posts: white screen of death, critical error, 500 error, database connection error, too many redirects, stuck in maintenance mode, robots.txt blocking pages, purge cache. Autocomplete confirms "wordpress critical error fix" / "…godaddy". | GD has `fix-wordpress-issues-boston-ma.html` (18 impr @**p9.9**, already close) + `/gd-blog/fix-hacked-wordpress-site/`. Write **one short WP post per error**, each ending in a CTA to the fix page ("Repairs from $150"). These are nationally searchable, so they fit the remote-clients vertical (`national-remote-clients-plan.md`). |
| 6 | **Migrate X → WordPress** | cyberoptik has 16 (Wix, Squarespace, Webflow, Shopify, Drupal, Joomla, HubSpot, Framer, Lovable/AI-site, HTML…); websitesusa has Wix, Shopify, Drupal | GD has only `/gd-blog/wix-to-wordpress-migration/`. Add **Squarespace → WP** and **"AI site builder / Lovable → WordPress"** next (newest, least contested), then GoDaddy Website Builder → WP. Each one ties to GD's "SEO-safe migrations" service. |
| 7 | **Industry verticals** | websitesusa: 115 templated industry pages; cyberoptik + creativemarketing.ai: 100+ each | **Don't copy the 100-page approach.** GD's two vertical pages already work: contractors (1,078 impr, e.g. "website design for contractor lynn" @p7) and restaurants (327 impr). Add **3 more verticals where GD has real portfolio clients**. GSC shows faint signals for law firm, dentist, and chiropractor SEO in Chelsea. Choose based on the portfolio, not the competitors' lists. |
| 8 | **Accessibility / ADA compliance** | cyberoptik `/websites/accessibility-ada/`; eBree positions on accessibility; websitesusa `wordpress-accessibility-compliance` | **New WP service page** "Website Accessibility (ADA/WCAG) — Boston" or an accessibility-audit add-on. Keep legal claims careful (no "guaranteed compliant"). |
| 9 | **Hiring/decision comparisons** | websitesusa: agency vs freelancer vs full-service; web designer vs web developer; questions to ask a web designer; comparing website design quotes; WordPress vs Wix vs Squarespace; Webflow vs WordPress | Strong fit for a solo freelancer and good GEO/AI-answer material. Start with **"Freelancer vs agency for a Boston small business"** (GD's honest angle) and **"Questions to ask before hiring a web designer"**. |

### Tier 3 — watch or skip

- **"Top N agencies in Boston" listicles** (websitesusa: SEO agencies, WordPress developers, maintenance companies, branding agencies, each ~4,600 words and listing themselves). These get cited by AI answers, but self-ranking listicles are a credibility risk for a one-person brand. **Optional.** If you do one, be transparent and include real competitors.
- **Far MA cities** (cyberoptik: Worcester, Springfield, Lowell, Brockton, Framingham, New Bedford, Taunton, Chicopee). Skip. These are outside GD's real service radius, and the Jamaica Plain/Saugus/Lynn/Dedham near-duplicate rewrite comes first.
- **Thin programmatic town pages** (creativemarketing.ai, ~480 words). Don't imitate them. GD's advantage is genuine local detail (`town-facts.yml`).
- **ExpressionEngine development** (eBree). Too niche. Skip.
- **Ecommerce/Shopify.** Not a gap: GD already ranks p11–12 for "shopify developer(s) boston". "woocommerce revere ma" 165 @p28 → add a WooCommerce H2 to the Revere page.

---

## Home-turf alert: CyberOptik's Everett page

`cyberoptik.net/web-design/everett-ma/` is 2,100 words with these sections: services, team, process, "Capturing the Spirit
of Everett", industries served, surrounding areas, FAQ. GD's Everett coverage is split between `organic-SEO-everett-ma.html`
(SEO) and `/gd-blog/service-area/everett/` (130 impr @p24.6). GD has no strong **"web design Everett MA"** page,
and Everett is where GD is actually located. **Recommended:** make `/gd-blog/service-area/everett/` the definitive
Everett web design page. Include a real address/map, Everett clients, and the GBP link. Being genuinely local is an advantage a non-local agency's template page can't match.

---

## Suggested build order

1. ✅ 2026-10-29 Everett web-design page — built as static `everett-ma-web-designer-wordpress-developer.html` (the WP service_city template only holds a short ACF intro, too thin for a definitive page). Open: decide whether `/gd-blog/service-area/everett/` 301s here or stays and links here
2. ✅ 2026-10-29 Church & nonprofit page — static `church-nonprofit-web-design-boston-ma.html` + 301 from the old non-profit URLs
   - Both pages uploaded and verified live on 2026-10-29 (commit `b8b9c14`). Also shipped: the GBP-name bridge (schema `alternateName`/`hasMap`, plus a footer note via `scripts/fix_gbp_name_note.py`). Next: Request Indexing for both pages in GSC.
3. Website redesign service page — WP
4. GBP optimization service page (or section) — WP
5. "How much does a website cost in Boston" post → links to flagship — WP
6. WordPress error posts (one batch of 3: critical error, white screen, database connection) — WP
7. Squarespace → WordPress and AI-builder → WordPress migration posts — WP
8. Accessibility service page — WP
9. "Freelancer vs agency" post — WP

## Open questions for the owner

- Which industries does the portfolio actually include? This decides #7.
- Do you want to offer accessibility audits as a paid service? This decides whether #8 is a page or a post.
- Round 2: which other competitors and cities should be added (e.g. TheeDigital and Truly Good Design for Somerville/Cambridge)?
