---
name: seo-analyze
description: Analyze Google Search Console + GA4 CSV exports against the GD Pro Web Designs static site to produce a prioritized, actionable plan for improving search rankings. Use when the user runs /seo-analyze, asks to review SEO performance, find ranking opportunities, fix low-CTR pages, or interpret their Search Console / Analytics data.
---

# SEO Analysis Skill

Turn raw Search Console + GA4 exports into a ranked, do-this-next SEO plan for
the GD Pro Web Designs static site. All analysis is local — no credentials, no
network calls, no data leaves the machine.

## Inputs

CSV files in `seo-data/` (gitignored). The user exports these from the Google
web UIs — see `seo-data/README.md`. Expected files (any subset is fine; adapt
to whatever is present):

- `gsc-queries.csv` — search queries with Clicks, Impressions, CTR, Position
- `gsc-pages.csv` — landing pages with the same four metrics
- `gsc-countries.csv`, `gsc-devices.csv` — optional segmentation
- `ga4-landing-pages.csv` — sessions/engagement by landing page
- `ga4-acquisition.csv` — traffic by channel/source

## Procedure

1. **Check the data exists.** List `seo-data/`. If there are no CSVs, tell the
   user exactly what to export (point them at `seo-data/README.md`) and stop —
   do not invent numbers.

2. **Load the CSVs.** Read them with a small pandas/csv script via Bash
   (`python3`). GSC exports are UTF-8 with a header row; CTR is a string like
   `2.3%` and Position is a float. Parse them to numbers. Note the date range
   if present in the file.

3. **Cross-reference against the real site.** The opportunities only matter if
   tied to a real page. For each high-value GSC page URL, map it to the local
   HTML file (strip the domain, match the slug). Read that file's
   `<title>`, `<meta name="description">`, `<h1>`, and canonical to judge
   whether the on-page targeting matches the queries it actually ranks for.
   Respect every rule in the project `CLAUDE.md` (nav is centralized, no inline
   styles, canonical/geo meta required, contact links go to `/gd-blog/contact-us`,
   etc.) when proposing edits.

4. **Run the opportunity analysis.** Surface, with the supporting numbers:

   - **Striking-distance keywords** — queries at avg position **8–20**. Small
     on-page tweaks can push these to page 1. Highest ROI; lead with these.
   - **High-impression / low-CTR pages** — lots of impressions but CTR well
     below the position's expected rate → rewrite `<title>` / meta description
     to be more compelling (add location, price hook, year, CTA).
   - **Keyword cannibalization** — one query where multiple pages compete →
     recommend which page should own it and how to differentiate the others.
   - **Content gaps** — queries with impressions but **no** strong matching
     page → candidate for a new service/location page or section.
   - **Position-1–3 wins to protect** — note what's already ranking well so the
     user doesn't accidentally weaken it.
   - **Geo/intent fit** — flag queries from outside MA / off-target intent.
   - **GA4 corroboration** — which landing pages convert engagement vs. bounce;
     pair GSC visibility with GA4 behavior.

5. **Produce the deliverable.** A prioritized table:

   | Priority | Page (local file) | Issue | Evidence (the numbers) | Specific fix |
   |----------|-------------------|-------|------------------------|--------------|

   Order by impact × ease. Make every fix concrete — give the actual rewritten
   `<title>` / meta description text, the exact internal-link anchor to add and
   from which page, or the new page slug + target query. Avoid generic advice
   ("write good content"); cite the query and number behind each recommendation.

6. **Offer to implement.** After presenting the plan, ask whether to apply the
   top fixes directly to the HTML files. When editing, follow `CLAUDE.md`
   conventions exactly and add a `.htaccess` 301 for any slug change.

## Guardrails

- Never fabricate metrics. If a file is missing or a number isn't in the export,
  say so rather than guessing.
- Read-only on the data; only modify site HTML when the user approves step 6.
- Keep recommendations within scope of a static HTML + WordPress-subdir site.
