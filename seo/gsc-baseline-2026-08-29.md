# GSC Baseline — Phase 1 +0 Snapshot

**Purpose:** frozen pre-deployment baseline for measuring the organic-lead-growth
initiative. Phases 0–2 (static site) went live **2026-08-30** (commit `1b2a49f`);
the 2 static→WP town redirects (Cambridge, Quincy) + this snapshot are the
2026-09-03 session.

**Window:** `2026-06-01` → `2026-08-29` (90 days, ending the day before deploy).
**Property:** `https://gdprowebdesigns.com/` · **Source:** GSC Search Analytics API.
Compare against the same 90-day window length at **+14d, +28d, +60d**
(`gsc_search_analytics`, dimensions `["page"]` and `["page","query"]`).

Success = target clusters moving from pos 15–35 into 5–12, first non-zero clicks on
the 7k-impression pages, and homepage impressions **consolidating downward** (healthy —
cannibalization unwinding).

---

## Site-level page baseline (clicks / impressions / avg position)

| Page | Clicks | Impr | Pos | Role |
|---|---:|---:|---:|---|
| `/` (homepage) | 27 | 16,367 | 45.2 | cannibalization source — expect impr ↓ |
| `SEO-company-chelsea-ma.html` | 0 | 6,579 | 34.7 | P1 |
| `organic-search-engine-optimization-boston.html` | 1 | 6,534 | 52.8 | P1 |
| `wordpress-developer-boston-ma.html` | 1 | 6,006 | 35.0 | P1 |
| `newton-ma-web-designer-web-developer.html` | 0 | 3,425 | 37.2 | — |
| `PPC-adwords-advertising-boston.html` | 1 | 2,801 | 60.6 | P1 |
| `organic-SEO-everett-ma.html` | 0 | 2,588 | 33.9 | P1 |
| `web-design-company-boston-ma.html` | 2 | 2,163 | 57.9 | P1 |
| `wordpress-maintenance-boston-ma.html` | 1 | 1,811 | 38.4 | P1 |
| `portfolio-graphics-design-boston-everett-ma.html` | 2 | 1,407 | 49.6 | — |
| `gd-blog/service-area/` | 0 | 1,395 | 60.4 | WP hub |
| `portfolio-website-design-development-boston-ma.html` | 0 | 1,274 | 62.4 | — |
| `about-gd-freelance-web-designer-boston.html` | 2 | 1,094 | 30.7 | — |
| `sitemap.html` | 0 | 1,070 | 58.8 | — |
| `graphics-designer-logos-boston.html` | 1 | 879 | 43.6 | P1 (low pri) |
| `gd-blog/web-developer-ma/` | 0 | 870 | 68.3 | WP |
| `quincy-ma-web-design-and-development.html` | 0 | 825 | 31.5 | **301→WP 09-03** |
| `newton` / `malden` / `lynn` static town pages | 0 | 555 / 540 | 44.5 / 23.8 | — |
| `ai-search-visibility-audit-boston-ma.html` | 1 | 574 | 22.9 | P1 |
| `local-website-developer-near-me.html` | 0 | 387 | 59.3 | — |
| `somerville-ma-web-designer.html` | 0 | 340 | 33.6 | — |
| `chelsea-web-design-company-wordpress-developer.html` | 1 | 320 | 46.0 | — |
| `website-designer-near-cambridge-ma.html` | 0 | 192 | 43.6 | **301→WP 09-03** |
| `organic-seo-services-somerville.html` | 0 | 176 | 21.8 | — |
| `website-design-company-saugus-ma.html` | 0 | 157 | 24.7 | — |
| `saugus-web-designer-wordpress-developer-seo.html` | 0 | 115 | 15.6 | — |
| `seo-services-everett-ma.html` | 0 | 101 | 12.0 | 301 stub |

WP service-area town pages already outrank static equivalents:
`rowley-ma` pos 8.0 · `burlington-ma` 14.0 · `woburn-ma` 21.3 · `everett/` 32.1 ·
`ranfolph-ma` 27.4 · `somerville/` 23.2 — vs static towns mostly pos 33–47.

---

## Phase 1 target pages — cluster baseline (page × query)

### 1. `organic-SEO-everett-ma.html` — 2,588 impr · 0 clicks · pos 33.9
| Query | Impr | Pos |
|---|---:|---:|
| everett search engine optimization | 221 | 19.8 |
| everett seo company | 211 | 21.8 |
| everett seo agency | 82 | 19.0 |
| seo company everett | 82 | 36.1 |
| seo services everett | 76 | 30.6 |
| everett seo | 72 | 22.3 |
| seo agency everett | 68 | 21.4 |
| seo everett | 33 | 16.7 |
| everett ma seo agency | 18 | 10.0 |
| seo everett ma | 5 | 3.8 |

### 2. `organic-search-engine-optimization-boston.html` — 6,534 impr · 1 click · pos 52.8
| Query | Impr | Pos |
|---|---:|---:|
| affordable seo boston | 328 | 14.4 *(split w/ homepage)* |
| boston search engine optimization | 212 | 52.3 |
| boston local seo services | 173 | 48.9 |
| affordable search engine optimization company | 64 | 46.8 |
| affordable seo services boston | 67 | 18.1 |
| boston local seo company | 79 | 51.1 |
| boston local seo | 78 | 54.1 |

### 3. `web-design-company-boston-ma.html` — 2,163 impr · 2 clicks · pos 57.9
| Query | Impr | Pos |
|---|---:|---:|
| boston web designer | 441 | 42.9 |
| boston web design company | 327 | 53.0 |
| boston web design | 275 | 48.6 |
| boston web design services | 102 | 49.0 |
| boston web design pricing | 95 | 37.8 |
| affordable web design boston | 132 | 21.1 |
| affordable web design and development | 76 | 23.8 |
| affordable web design services in boston | 32 | 25.0 |

### 4. `wordpress-developer-boston-ma.html` — 6,006 impr · 1 click · pos 35.0
| Query | Impr | Pos |
|---|---:|---:|
| wordpress developer near me | 639 | 39.6 |
| wordpress developers near me | 291 | 24.6 |
| wordpress development boston | 232 | 24.4 |
| wordpress developer boston | 214 | 19.9 |
| wordpress site optimization western ma | 195 | 41.5 |
| professional wordpress developers custom sites near me | 174 | 20.9 |
| boston wordpress developers | 157 | 23.8 |
| wordpress design and development services | 154 | 56.6 |
| wordpress expert near me | 126 | 30.8 |
| wordpress web design boston | 112 | 59.8 |
| wordpress developers boston | 105 | 20.1 |
| professional wordpress design and development | 102 | 42.8 |
| wordpress developer for small business | 99 | 15.3 |
| freelance wordpress developer near me | 97 | 44.3 |
| wordpress designer boston | 93 | 37.2 |
| wordpress boston | 90 | 41.4 |

### 5. `PPC-adwords-advertising-boston.html` — 2,801 impr · 1 click · pos 60.6
| Query | Impr | Pos |
|---|---:|---:|
| ppc agency boston | 492 | 74.5 |
| google ads agency boston | 188 | 56.3 |
| ppc consultant boston | 186 | 58.2 |
| ppc in boston | 92 | 52.3 |
| boston ppc agency | 84 | 80.2 |
| boston ppc company | 82 | 65.5 |
| google ads management boston | 81 | 45.8 |
| adwords manager boston | 74 | 39.5 |
| adwords manager north shore | 57 | 30.5 |
| adwords management north shore | 55 | 37.5 |
| google ads boston | 52 | 42.4 |
| massachusetts ppc manager | 26 | 53.0 |
| *(long "google ads agency [town] ma" tail — ~90 towns, all pos 55–98)* | | |

### 6. `ai-search-visibility-audit-boston-ma.html` — 574 impr · 1 click · pos 22.9
| Query | Impr | Pos |
|---|---:|---:|
| ai search optimization massachusetts | 180 | 16.6 |
| ai search optimization boston | 55 | 17.1 |
| ai visibility boston | 49 | 10.4 |
| ai search optimization boston ma | 14 | 14.8 |

### 7. `SEO-company-chelsea-ma.html` — 6,579 impr · 0 clicks · pos 34.7
| Query | Impr | Pos |
|---|---:|---:|
| **seo company chelsea** | **2,122** | **8.1** |
| seo agency massachusetts | 104 | 34.5 |
| seo company truro *(Cape Cod noise)* | 88 | 31.1 |
| seo agency chelsea heights | 87 | 21.1 |
| search engine agency chelsea | 78 | 10.4 |
| search engine optimization company chelsea | 76 | 9.4 |
| seo chelsea | 52 | 9.9 |
| seo company for contractors chelsea | 50 | 24.3 |
| seo cape cod ma *(noise)* | 47 | 44.3 |
| seo company massachusetts | 39 | 32.2 |
| chelsea ma digital marketing | 37 | 13.6 |
| seo chelsea ma | 25 | 3.4 |
| contractor seo chelsea | 23 | 2.1 |
| seo company in chelsea | 21 | 3.7 |
| seo services chelsea | 19 | 3.8 |
| seo agency chelsea ma | 14 | 7.3 |

Kept static (NOT redirected to WP Chelsea) — distinct "seo company chelsea" cluster,
already rebuilt in Phase 1. Heavy Cape Cod / Truro / Camden / UK impressions =
title-intent bleed to watch.

### 8. `wordpress-maintenance-boston-ma.html` — 1,811 impr · 1 click · pos 38.4
Nearest queries (mostly attributed to the developer page pre-deploy):
`wordpress support boston` 72 @ 41.8 · `wordpress maintenance boston` 1 @ 41.0.
Page-level aggregate is the baseline to beat.

---

## Redirected pages (301 → WP, 2026-09-03) — expect static impr → 0, WP page inherits
| Old static URL | Impr | Pos | New target |
|---|---:|---:|---|
| `website-designer-near-cambridge-ma.html` | 192 | 43.6 | `/gd-blog/service-area/cambridge-ma/` |
| `quincy-ma-web-design-and-development.html` | 825 | 31.5 | `/gd-blog/service-area/quincy-ma/` |

Watch the two WP targets (`cambridge-ma` / `quincy-ma`, published 2026-09-03) pick up
the redirected impressions plus the "google ads agency [town]" / "[town] seo" tails.

---

## Cross-cluster notes
- **Homepage** eats "affordable seo boston" (328 @ 14.4), "boston web designer" (441),
  "boston web design company" (327) — same queries the P1 pages target. Expect the P1
  pages to take share and homepage impressions to fall. That is the intended outcome,
  not a regression.
- **"google ads agency [town] ma"** — ~90-town tail on the PPC page at pos 55–98.
  Phase 3 WP town pages + the PPC town matrix are meant to lift these.
- **North Shore PPC** ("adwords manager north shore" 57 @ 30.5, "adwords management
  north shore" 55 @ 37.5) — closest-to-page-1 PPC opportunity; the Phase 1 PPC rewrite
  added a North Shore section.
