---
name: seo-technical
description: Run technical SEO health checks against the GD Pro Web Designs static site — sitemap accuracy vs. actual pages/redirects, JSON-LD schema validation, broken internal links/redirect chains/duplicate titles, and drift monitoring against the live site to catch ranking-affecting regressions early. Use when the user runs /seo-technical, asks to audit site health, check the sitemap, validate structured data, find broken links, or check what changed on the live site since the last check.
---

# Technical SEO Health Check

Run automated technical checks against this repo and the live site, then turn
the findings into a prioritized, do-this-next report — the sibling to
`/seo-analyze` (which covers ranking/opportunity analysis from GSC+GA4
exports). This skill covers site *health*: things that can silently tank
rankings regardless of content quality, and that went undetected for ~9
months before the September 2025 ranking crash was diagnosed.

All four scripts are stdlib-only Python (no third-party packages required,
none installed on this machine) and live in
`.claude/skills/seo-technical/scripts/`.

## Procedure

1. **Run the three local checks** via Bash (`python3`):
   - `python3 .claude/skills/seo-technical/scripts/sitemap_check.py` —
     cross-references `sitemap.xml` against the real page list and
     `.htaccess` redirects. Add `--live` to also HEAD-check every sitemap
     URL's actual status.
   - `python3 .claude/skills/seo-technical/scripts/schema_check.py` —
     validates every JSON-LD block site-wide.
   - `python3 .claude/skills/seo-technical/scripts/crawl_check.py` — broken
     internal links, links that route through a redirect instead of hitting
     the destination directly, duplicate title/meta, missing `alt` text.

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

## Guardrails

- `sitemap_check.py`, `schema_check.py`, and `crawl_check.py` are 100% local
  — they read repo files only, no network calls, no credentials.
- `drift_snapshot.py` is the *only* script that makes network requests: a
  read-only GET to `https://gdprowebdesigns.com` per live page. Nothing else.
- Never fabricate findings — every line in the report must trace back to
  actual script output.
- Read-only on the site; only modify HTML/`.htaccess`/`sitemap.xml` when the
  user approves step 5.
