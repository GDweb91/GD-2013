#!/usr/bin/env python3
"""Cross-reference sitemap.xml against the real site: malformed entries,
stale/dead URLs, entries that should point straight at a redirect's
destination, and live pages missing from the sitemap entirely.

Usage:
    python3 sitemap_check.py [--live]

    --live   Also HEAD-request every sitemap URL against the live site and
             report any non-200 response. Network access only; no credentials.
"""
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _site_root as sr

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
ISO_LASTMOD_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$")


def parse_sitemap(path):
    """Return list of dicts: {loc, lastmod, priority, commented}. Comments
    are handled separately since ElementTree silently drops them — a raw
    regex pass over the source finds any <url> block sitting inside an XML
    comment, which the tree parse alone can't see."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    # No defusedxml in this stdlib-only project; guard against XXE/billion-
    # laughs ourselves since this file has no legitimate reason to declare a
    # DOCTYPE or custom entities.
    if "<!DOCTYPE" in raw or "<!ENTITY" in raw:
        raise ValueError(f"{path} contains a DOCTYPE/ENTITY declaration — refusing to parse")

    tree = ET.parse(path)
    entries = []
    for url_el in tree.getroot().findall("sm:url", NS):
        loc_el = url_el.find("sm:loc", NS)
        lastmod_el = url_el.find("sm:lastmod", NS)
        entries.append({
            "loc": loc_el.text.strip() if loc_el is not None and loc_el.text else "",
            "lastmod": lastmod_el.text.strip() if lastmod_el is not None and lastmod_el.text else "",
            "commented": False,
        })

    for m in re.finditer(r"<!--(.*?)-->", raw, re.DOTALL):
        comment_body = m.group(1)
        for loc_m in re.finditer(r"<loc>(.*?)</loc>", comment_body):
            entries.append({"loc": loc_m.group(1).strip(), "lastmod": "", "commented": True})

    return entries


def check_live(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "gdprowebdesigns-seo-technical/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except urllib.error.URLError as e:
        return f"ERROR: {e.reason}"


def main():
    live_flag = "--live" in sys.argv
    sitemap_path = os.path.join(sr.SITE, "sitemap.xml")
    entries = parse_sitemap(sitemap_path)

    issues = []  # (severity, message)
    seen_paths = set()

    for e in entries:
        loc = e["loc"]
        label = f"{loc}"
        if e["commented"]:
            issues.append(("info", f"Commented-out <url> block still in file (dead weight): {label}"))
            continue

        if not loc:
            issues.append(("critical", "Empty <loc> entry"))
            continue

        rel = sr.path_for_url(loc)
        seen_paths.add(rel)

        if not e["lastmod"]:
            issues.append(("warning", f"Empty <lastmod>: {label}"))
        elif not ISO_LASTMOD_RE.match(e["lastmod"]):
            issues.append(("warning", f"Malformed <lastmod> '{e['lastmod']}': {label}"))

        decoded_rel = urllib.parse.unquote(rel)
        on_disk = rel == "" or os.path.isfile(os.path.join(sr.SITE, decoded_rel))
        redirect_dest = sr.redirect_target(decoded_rel)

        if redirect_dest:
            issues.append((
                "warning",
                f"Points at a URL that itself 301s: {label} -> {redirect_dest} "
                f"(sitemap should list the destination directly)",
            ))
        elif not on_disk:
            issues.append(("critical", f"No matching file on disk and no redirect covers it (likely 404): {label}"))
        elif rel != decoded_rel:
            issues.append(("warning", f"URL-encoded loc ('{rel}') resolves to a real file only after decoding — use the plain filename: {label}"))

        if rel == "index.html":
            issues.append(("info", f"Redundant entry: index.html duplicates '/' (and 301s to it per .htaccess): {label}"))

    live_paths = set(sr.live_pages())
    seen_locs = {e["loc"] for e in entries}
    # 'index.html' is the same page as '/' (and 301s to it per .htaccess) —
    # don't flag it missing just because only '/' is listed, not both.
    root_covered = "" in seen_paths or sr.DOMAIN + "/" in seen_locs
    missing = sorted(
        p for p in live_paths
        if p not in seen_paths
        and sr.url_for(p) not in seen_locs
        and not (p == "index.html" and root_covered)
    )
    for p in missing:
        issues.append(("warning", f"Live page missing from sitemap: {p}"))

    if live_flag:
        print("Checking live status for each sitemap URL (HEAD request)...\n")
        for e in entries:
            if e["commented"] or not e["loc"]:
                continue
            status = check_live(e["loc"])
            if status != 200:
                issues.append(("critical", f"Live status {status} (expected 200): {e['loc']}"))

    critical = [m for s, m in issues if s == "critical"]
    warning = [m for s, m in issues if s == "warning"]
    info = [m for s, m in issues if s == "info"]

    print(f"sitemap_check: {len(entries)} <url> entries parsed, {len(live_paths)} live pages on the site\n")
    print(f"CRITICAL ({len(critical)}):")
    for m in critical:
        print(f"  ✗ {m}")
    print(f"\nWARNING ({len(warning)}):")
    for m in warning:
        print(f"  ⚠ {m}")
    print(f"\nINFO ({len(info)}):")
    for m in info:
        print(f"  - {m}")


if __name__ == "__main__":
    main()
