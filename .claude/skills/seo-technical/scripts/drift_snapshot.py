#!/usr/bin/env python3
"""Snapshot and diff the LIVE, deployed site's key SEO signals — HTTP status,
redirect target, <title>, meta description, canonical, robots meta, and a
JSON-LD hash — to catch a production regression (bad deploy, a host-level
cache serving stale content, an accidental noindex) in days, not the ~9
months it took to notice the September 2025 ranking crash.

This is the only script in seo-technical/ that makes network requests: a
read-only GET to https://gdprowebdesigns.com per live page. No credentials,
no other hosts.

CAVEAT (found while building this): this host has served a 404 to Python's
urllib for a URL that curl/browsers get a 200 for on the same request path,
with no clean explanation found in HTTP version or Accept-Encoding — likely
some client-fingerprint-based filtering at the edge/WAF layer, in the same
family as the documented Bluehost edge-cache quirks in CLAUDE.md. Treat any
non-200 this script reports as "worth a manual `curl -I` before assuming
it's real," not as ground truth on its own.

Usage:
    python3 drift_snapshot.py baseline   # capture current live state
    python3 drift_snapshot.py compare    # diff live state vs. last snapshot,
                                          # then write a new snapshot either way
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _site_root as sr

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL | re.IGNORECASE)
LD_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)
_TAG_RE_CACHE = {}


def _tag_attr_values(html, tag, match_attr, match_value, want_attr):
    """Order-agnostic: find every <tag ...> where match_attr=match_value,
    return the want_attr value from each (attributes can appear in any order
    in real HTML, so a fixed-order regex would miss some)."""
    if tag not in _TAG_RE_CACHE:
        _TAG_RE_CACHE[tag] = re.compile(rf"<{tag}\b([^>]*)>", re.IGNORECASE)
    results = []
    for m in _TAG_RE_CACHE[tag].finditer(html):
        pairs = dict(re.findall(r'([\w-]+)\s*=\s*["\']([^"\']*)["\']', m.group(1)))
        pairs = {k.lower(): v for k, v in pairs.items()}
        if pairs.get(match_attr, "").lower() == match_value.lower() and want_attr in pairs:
            results.append(pairs[want_attr])
    return results


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "gdprowebdesigns-seo-technical/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {
                "status": resp.status,
                "final_url": resp.geturl(),
                "body": resp.read().decode("utf-8", errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return {"status": e.code, "final_url": e.geturl(), "body": body, "error": None}
    except urllib.error.URLError as e:
        return {"status": None, "final_url": url, "body": "", "error": str(e.reason)}


def snapshot_page(rel_path):
    url = sr.url_for(rel_path)
    result = fetch(url)
    if result["error"]:
        return {"url": url, "status": None, "error": result["error"]}

    html = result["body"]
    titles = TITLE_RE.findall(html)
    descs = _tag_attr_values(html, "meta", "name", "description", "content")
    canonicals = _tag_attr_values(html, "link", "rel", "canonical", "href")
    robots = _tag_attr_values(html, "meta", "name", "robots", "content")
    ld_blocks = LD_JSON_RE.findall(html)
    ld_hash = (
        hashlib.sha256("".join(sorted(b.strip() for b in ld_blocks)).encode("utf-8")).hexdigest()[:16]
        if ld_blocks else None
    )

    return {
        "url": url,
        "status": result["status"],
        "final_url": result["final_url"],
        "redirected": result["final_url"].rstrip("/") != url.rstrip("/"),
        "title": titles[0].strip() if titles else None,
        "meta_description": descs[0].strip() if descs else None,
        "canonical": canonicals[0].strip() if canonicals else None,
        "robots": robots,  # list — more than one entry means conflicting robots meta tags
        "jsonld_hash": ld_hash,
        "error": None,
    }


def fetch_all(pages, verbose=False):
    data = {}
    for i, rel in enumerate(pages, 1):
        data[rel] = snapshot_page(rel)
        status = data[rel].get("status")
        if verbose:
            flag = "  <- verify with curl -I, see CAVEAT in this script's docstring" if status != 200 else ""
            print(f"  [{i}/{len(pages)}] {rel} -> {status}{flag}")
        time.sleep(0.3)  # courteous pacing against our own host
    return data


def write_snapshot(data):
    seo_data = os.path.join(sr.SITE, "seo-data")
    os.makedirs(seo_data, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    out_path = os.path.join(seo_data, f"drift-{stamp}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"taken_at_utc": stamp, "pages": data}, f, indent=2, sort_keys=True)
    return out_path


def latest_snapshot_path():
    seo_data = os.path.join(sr.SITE, "seo-data")
    if not os.path.isdir(seo_data):
        return None
    candidates = sorted(f for f in os.listdir(seo_data) if f.startswith("drift-") and f.endswith(".json"))
    return os.path.join(seo_data, candidates[-1]) if candidates else None


def run_baseline():
    pages = sr.live_pages()
    print(f"Fetching {len(pages)} live pages from {sr.DOMAIN} ...")
    data = fetch_all(pages, verbose=True)
    out_path = write_snapshot(data)
    print(f"\nBaseline written to {out_path}")


def run_compare():
    prev_path = latest_snapshot_path()
    if not prev_path:
        print("No prior snapshot found in seo-data/ — run `baseline` first.")
        return
    with open(prev_path, encoding="utf-8") as f:
        prev = json.load(f)["pages"]

    pages = sr.live_pages()
    print(f"Comparing current live state against {os.path.basename(prev_path)} ...\n")
    current = fetch_all(pages)

    changes = []
    for rel, cur in current.items():
        before = prev.get(rel)
        if before is None:
            changes.append(f"{rel}: new page, not in prior snapshot")
            continue
        for field in ("status", "title", "meta_description", "canonical", "jsonld_hash"):
            if cur.get(field) != before.get(field):
                changes.append(f"{rel}: {field} changed: {before.get(field)!r} -> {cur.get(field)!r}")
        if cur.get("robots") != before.get("robots"):
            changes.append(f"{rel}: robots meta changed: {before.get('robots')!r} -> {cur.get('robots')!r}")
    for rel in prev:
        if rel not in current:
            changes.append(f"{rel}: no longer in the live-page inventory (removed or renamed locally)")

    if changes:
        print(f"CHANGED ({len(changes)}):")
        for c in changes:
            print(f"  ⚠ {c}")
    else:
        print("No drift detected — live site matches the last snapshot.")

    out_path = write_snapshot(current)
    print(f"\nNew snapshot written to {out_path}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("baseline", "compare"):
        print(__doc__)
        sys.exit(1)
    (run_baseline if sys.argv[1] == "baseline" else run_compare)()


if __name__ == "__main__":
    main()
