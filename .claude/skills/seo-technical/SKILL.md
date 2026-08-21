---
name: seo-technical
description: Run technical SEO health checks against the GD Pro Web Designs static site — sitemap accuracy vs. actual pages/redirects, JSON-LD schema validation, broken internal links/redirect chains/duplicate titles, thin and near-duplicate page content, and drift monitoring against the live site to catch ranking-affecting regressions early. Use when the user runs /seo-technical, asks to audit site health, check the sitemap, validate structured data, find broken links, check for thin or duplicate content, or check what changed on the live site since the last check.
---

# Technical SEO Health Check

Run automated technical checks against this repo and the live site, then turn
the findings into a prioritized, do-this-next report — the sibling to
`/seo-analyze` (which covers ranking/opportunity analysis from GSC+GA4
exports). This skill covers site *health*: things that can silently tank
rankings regardless of content quality, and that went undetected for ~9
months before the September 2025 ranking crash was diagnosed.

All five scripts are stdlib-only Python (no third-party packages required,
none installed on this machine) and live in
`.claude/skills/seo-technical/scripts/`.

## Procedure

1. **Run the four local checks** via Bash (`python3`):
   - `python3 .claude/skills/seo-technical/scripts/sitemap_check.py` —
     cross-references `sitemap.xml` against the real page list and
     `.htaccess` redirects. Add `--live` to also HEAD-check every sitemap
     URL's actual status.
   - `python3 .claude/skills/seo-technical/scripts/schema_check.py` —
     validates every JSON-LD block site-wide.
   - `python3 .claude/skills/seo-technical/scripts/crawl_check.py` — broken
     internal links, links that route through a redirect instead of hitting
     the destination directly, duplicate title/meta, missing `alt` text.
   - `python3 .claude/skills/seo-technical/scripts/duplicate_content_check.py`
     — thin-content pages (<300 words, boilerplate excluded) and pairs of
     pages that read as near-duplicates (≥60% similar after stripping
     nav/footer/sticky-bar; ≥70% is flagged critical). Exists because the
     Sept 2025 ranking crash root-caused to Google's scaled/duplicate-content
     spam update hitting this site's templated city pages — thresholds
     ported from the third-party `claude-seo` repo's `seo-programmatic`
     skill (unique-content-% methodology), scoped down to what's relevant
     at this site's size (67 pages, not thousands).

2. **Run the drift check** — this one talks to the live site
   (`https://gdprowebdesigns.com`), read-only, no credentials:
   - If `seo-data/drift-*.json` has no prior snapshot, run
     `python3 .claude/skills/seo-technical/scripts/drift_snapshot.py baseline`.
   - Otherwise run `... drift_snapshot.py compare` — diffs live state
     (status, title, meta description, canonical, robots meta, JSON-LD hash)
     against the most recent snapshot and writes a new one either way.
   - **Caveat**: this host has shown client-dependent behavior on at least
     one URL (Python's urllib got a 404 where curl got 200, no clean
     explanation found — see the CAVEAT in `drift_snapshot.py`'s docstring).
     Treat any non-200 this script reports as "verify with `curl -I` before
     treating as real," not as ground truth by itself.

3. **Cross-reference against the real site** the same way `/seo-analyze`
   does: for anything flagged, read the actual page's `<title>`,
   `<meta name="description">`, `<h1>`, and canonical before proposing a fix,
   and respect every rule in the project `CLAUDE.md` (nav is centralized in
   `scripts/fix_navs.py`, no inline styles, contact links go to
   `/gd-blog/contact-us/`, a slug change needs a `.htaccess` 301, etc.).

4. **Produce the deliverable** — same table format as `/seo-analyze`, for
   consistency:

   | Priority | Page (local file) | Issue | Evidence (script output) | Specific fix |
   |----------|-------------------|-------|---------------------------|--------------|

   Order critical (broken things, 404s, parse errors) before warning
   (redirect chains, duplicate meta, missing sitemap entries) before info
   (FAQPage rich-result eligibility notes, etc.).

5. **Offer to implement.** After presenting the plan, ask whether to apply
   the fixes directly — regenerating `sitemap.xml` entries, fixing broken
   `href`s, adding missing `alt` text, correcting JSON-LD. Follow `CLAUDE.md`
   conventions exactly; add a `.htaccess` 301 for any slug change.

## What this does NOT cover (by design)

Backlinks, SERP rank tracking, competitor analysis, Core Web Vitals/PageSpeed
(would need a Google API key), image SEO, hreflang, e-commerce — none of
these apply to this site today, or they need a paid third-party account
either way. Use `/seo-analyze` for ranking/opportunity analysis from GSC+GA4
data — this skill is purely site-health/technical.

`duplicate_content_check.py` only covers the static repo's pages. `gd-blog`'s
`service_city` custom post type (41 pages, WordPress-generated from a single
template) is the same architectural risk but isn't a local file — it lives
in the WP database, which this session found drifts from the live site
independently. A future version of this check would need to hit the live
`/gd-blog/wp-json/wp/v2/service_city` REST endpoint instead of reading local
files.

## Guardrails

- `sitemap_check.py`, `schema_check.py`, `crawl_check.py`, and
  `duplicate_content_check.py` are 100% local — they read repo files only,
  no network calls, no credentials.
- `drift_snapshot.py` is the *only* script that makes network requests: a
  read-only GET to `https://gdprowebdesigns.com` per live page. Nothing else.
- Never fabricate findings — every line in the report must trace back to
  actual script output.
- Read-only on the site; only modify HTML/`.htaccess`/`sitemap.xml` when the
  user approves step 5.
