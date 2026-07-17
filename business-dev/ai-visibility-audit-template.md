# AI Search Visibility Audit — Template

Internal working template for the "AI Visibility Snapshot" service. Copy this file per client (`ai-visibility-audit-[client-name].md`), fill it in, then use the "Client Report" section at the bottom as the basis for the deliverable you send them.

Target time per audit: **30–45 minutes** once you've run a few. Reference case study: GD Pro Web Designs itself (2026-07-17 snapshot) — see Appendix.

---

## 1. Pre-Audit Intake (5 min)

Fill in before running anything:

- **Client business name:**
- **City/town + nearest major metro:**
- **Core service(s) to test (2–4 max):**
- **2–3 known local competitors** (ask the client, or identify from a quick search):
- **Google Business Profile URL (if any):**

---

## 2. Query Bank (build 5–8 queries from these patterns)

Swap in the client's actual service + city. Always include at least one of each type — the query *type* is what determines whether you're testing brand strength vs. category visibility.

| # | Pattern | Example | Tests |
|---|---------|---------|-------|
| 1 | `[service] [city]` | "WordPress developer Everett MA" | Category + geo match — should be a near-guaranteed win if the client has a dedicated page |
| 2 | `[service] near [city]` or `[service] near me` framing | "local SEO services Everett MA" | Same as above, alternate phrasing |
| 3 | `best [service] [city]` | "best web designer Everett MA" | **Superlative/comparison query** — the hardest one, and the one most likely to expose a gap (directories/roundups tend to win this pattern over individual business sites unless trust signals are strong) |
| 4 | `[service] near Boston small business` (broader-region variant) | "freelance web designer near Boston small business" | Regional reach beyond the home city |
| 5 | `[business name] reviews` | "GD Pro Web Designs Everett MA reviews" | **Branded + trust check** — surfaces where the business is listed and whether reviews exist anywhere |
| 6 (optional) | `[business name] vs [competitor]` | — | Only if a specific competitor is named by the client as a rival |

---

## 3. Run & Record

For each query, record:

- [ ] Does the business appear in the **AI-synthesized answer/summary**, not just the raw links? (This is the actual AI-visibility signal — ranking in links ≠ being cited in the answer.)
- [ ] What **position** does it appear in (1st mentioned, buried, absent)?
- [ ] Is the info shown **accurate** (phone, founding year, description)?
- [ ] Which **competitors/directories** appear instead, if the business is absent?
- [ ] Note anything odd (wrong city, outdated info, wrong business entirely).

**Where to check reviews (query #5):** Yellow Pages, Yahoo Local, Alignable, Facebook, Google Business Profile, industry-specific directories. Record: does a review count/star rating exist anywhere, and is it visible/prominent?

---

## 4. Quick Trust & Structure Checks (10 min)

- [ ] **Schema/JSON-LD present?** View source on the client's homepage, search for `application/ld+json`. Does it include `LocalBusiness`/`ProfessionalService` type, address, phone, hours?
- [ ] **NAP consistency:** does the name/address/phone match exactly across the top 3 directory listings found in query #5? (Mismatches actively hurt AI/local trust signals.)
- [ ] **FAQ-shaped content:** does the site have any direct Q&A formatted content (not just marketing prose)? Y/N.
- [ ] **Review count:** total reviews found across all platforms (even if 0).

---

## 5. Score It

Simple 5-point scorecard — gives you something concrete and comparable to show the client, and to compare audits across clients over time.

| Category | Points |
|---|---|
| Wins category+geo queries (#1, #2) | 1 pt if yes |
| Wins the "best" superlative query (#3) | 1 pt if yes |
| Wins regional query (#4) | 1 pt if yes |
| Has visible reviews (query #5) | 1 pt if any found |
| Complete schema/JSON-LD | 1 pt if yes |

**AI Visibility Score: __ / 5**

---

## 6. Client Report (fill in, then send)

> Use plain language here — the client is not technical. Lead with the finding, not the method.

**What we tested:** [N] real questions a potential customer would type into ChatGPT, Google, or Gemini looking for a [service] in [city].

**Findings table:**

| Query a customer might ask | Do you show up? | Who shows up instead? |
|---|---|---|
| ... | ... | ... |

**The headline finding:** [1–2 sentences — usually the "best of" gap or the reviews gap. Be specific and concrete, e.g. "When someone asks for the *best* web designer in Everett, six other companies get named and you don't — including one based in Michigan."]

**Why this is happening:** [plain-language explanation — reviews, schema, or directory presence, whichever is the actual root cause found above]

**Recommended fixes, in order:**
1. [Fastest/cheapest fix — usually review generation]
2. [Second fix — usually schema/structured data]
3. [Third fix — usually FAQ/content additions]

**Next step / CTA:** [link to booking a fix engagement — see pricing tiers below]

---

## Pricing Reference (internal — don't include in client-facing copy verbatim)

- **Snapshot only** (this audit, delivered as the report above): $150–300 one-time
- **Snapshot + Fix** (implement schema, FAQ content, review-request workflow): $500–1,500 one-time
- **Ongoing**: add as a line item to existing SEO retainers

---

## Appendix — Reference Case Study (GD Pro Web Designs, run 2026-07-17)

| Query | Result |
|---|---|
| WordPress developer Everett MA | Won — #1 link + #1 in AI summary |
| Local SEO services Everett MA | Won — #1 link + #1 in AI summary |
| Freelance web designer near Boston small business | Won — #1 link + #1 in AI summary |
| Best web designer Everett MA | **Lost — absent from both links and AI summary** |
| GD Pro Web Designs Everett MA reviews | **Gap — listed on directories, zero reviews found anywhere** |

Score: 3/5. Root cause of the two misses: no review volume anywhere online, which is very likely why the "best of" superlative query defaults to directories/competitors instead. Cheapest fix: start a review-request workflow with recent/past clients.
