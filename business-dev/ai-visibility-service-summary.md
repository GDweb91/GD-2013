# AI Search Visibility Service — Session Summary

Recap of everything built in this session, for review before committing. 2026-07-17.

---

## 1. Where this came from

Started from a broader question: rankings have been declining, and how to use Fable (newest Claude model) to grow the business or find a fast, low-investment revenue line. Two directions were considered — using AI to fix the site's own chronic ranking problem (avg. position 30–60 for 2.5+ years, per [[ga4_event_tracking_status]]) vs. turning AI itself into a sellable service. Chose the latter: **AI Search Visibility** (industry terms: GEO/AEO — generative/answer engine optimization) — auditing and fixing whether ChatGPT, Gemini, Perplexity, and Google AI actually recommend a business by name.

Rationale: it reuses existing local-SEO expertise, requires near-zero new investment (Fable does the labor-intensive drafting), and there's a warm existing client base to pitch first.

---

## 2. Live proof-of-concept: GD Pro Web Designs' own AI visibility

Ran 5 real buyer queries through search to see how the business itself currently shows up:

| Query | Result |
|---|---|
| WordPress developer Everett MA | Won — #1 link + #1 in AI summary |
| Local SEO services Everett MA | Won — #1 link + #1 in AI summary |
| Freelance web designer near Boston small business | Won — #1 link + #1 in AI summary |
| **Best web designer Everett MA** | **Lost — absent from both links and AI summary; 6 competitors named instead** |
| GD Pro Web Designs Everett MA reviews | **Gap — listed on directories, zero reviews found anywhere** |

**Score: 3/5.** Root cause of the two misses: no review volume anywhere online — likely why the "best of" superlative query defaults to directories/competitors. Cheapest fix identified: start a review-request workflow with past/current clients. This case study is now baked into the audit template and referenced (softened, not spelled out) in the public service page copy.

---

## 3. What was built

| Deliverable | Location | Purpose |
|---|---|---|
| Audit template | `business-dev/ai-visibility-audit-template.md` | Repeatable process to run this same test for any client: query bank, trust/schema checklist, 5-point scorecard, fill-in client report section. ~30–45 min per audit once practiced. |
| Pitch email | `business-dev/pitch-email-ai-visibility.md` | 1-to-1 email template (not a blast) for existing clients, using GD Pro's own real gap as the credibility hook. Free snapshot offer, no pricing mentioned yet. Includes a follow-up nudge. |
| Service page | `ai-search-visibility-audit-boston-ma.html` | Public landing page, full modern template (Bootstrap 5.3, custom.css, LocalBusiness + FAQPage JSON-LD, phone protection, sticky call bar). No hard pricing published — funnels to free snapshot + custom quote since the service is unproven. |

---

## 4. Site-wide changes made

- **`index.html`** — added "AI Search Visibility" to the Marketing dropdown (canonical nav source)
- **`scripts/fix_navs.py`** — added the same item to `nav_en()`, added "Visibilidad en IA" to `nav_es()` (points at the same English-only page — matches the existing pattern where `organic-SEO-everett-ma.html` has no separate Spanish version), added the new page to the `ACTIVE` map under `marketing`
- Ran `fix_navs.py` → propagated the nav change to **53 live pages** (full list in git diff)
- **`sitemap.xml`** — added a `<url>` entry for the new page
- **`sitemap.html`** — added it to the SEO/Marketing services list
- Ran `fix_phone_protection.py` and `fix_inline_styles.py` on the new page — both completed with 0 changes needed, confirming it already matches site conventions

**Deliberately not done:** the new page isn't linked from any other page's *footer* (only nav + sitemap), and no pricing is published anywhere public yet.

---

## 5. Open items / decisions still pending

1. **Nothing is committed to git yet.** Everything above is unstaged working-tree changes only — nothing is live on the actual site.
2. **Security hook note:** the new page's CDN `<script>`/`<link>` tags (Bootstrap, Font Awesome, Google Fonts) have no Subresource Integrity (`integrity=`) hashes — but neither does any other page on the site, so this was left consistent rather than fixed on one page in isolation. Flagged as a possible separate site-wide hardening pass, not done here.
3. **Pitch email hasn't been sent to anyone yet.** Template is ready; sending is a manual, 1-to-1 per-client action.
4. **No client audits have been run yet** — the template is ready to use as soon as the first client replies "yes."
5. **Review-generation workflow** (the actual fix for the "best of" query gap found in Section 2) hasn't been built — natural next step once the pitch starts getting replies.
6. Whether to commit the nav/sitemap changes as one commit or review page-by-page first — was asked, not yet answered.
