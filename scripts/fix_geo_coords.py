#!/usr/bin/env python3
"""
Normalizes stale per-city GeoCoordinates blocks in LocalBusiness/ProfessionalService
JSON-LD to the real Everett, MA coordinates (42.40843, -71.053662).

fix_schema.py already corrected the fake per-city PostalAddress text (addressLocality)
to the real Everett address, but left the accompanying "geo" lat/long untouched, so
~22 pages still had an old block claiming to be physically located in the page's
target city (e.g. Dedham, Jamaica Plain, Lynn) while the address text says Everett.

Idempotent: only rewrites latitude/longitude pairs that don't already match the
canonical value, so re-running is always a no-op.
"""
import re
import pathlib

SITE_ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON_LAT = "42.40843"
CANON_LNG = "-71.053662"

SKIP_DIRS = {"archive", "node_modules", ".git", "seo", "index-css"}

GEO_RE = re.compile(
    r'("latitude"\s*:\s*)"?(-?[0-9]+\.[0-9]+)"?(\s*,\s*\n?\s*"longitude"\s*:\s*)"?(-?[0-9]+\.[0-9]+)"?'
)


def fix_file(path):
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(m):
        nonlocal changed
        lat, lng = m.group(2), m.group(4)
        if lat == CANON_LAT and lng == CANON_LNG:
            return m.group(0)
        changed = True
        return f"{m.group(1)}{CANON_LAT}{m.group(3)}{CANON_LNG}"

    new_text = GEO_RE.sub(repl, text)
    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main():
    changed_files = []
    for path in sorted(SITE_ROOT.rglob("*.html")):
        rel = path.relative_to(SITE_ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if fix_file(path):
            changed_files.append(str(rel))
    print(f"Fixed {len(changed_files)} file(s):")
    for f in changed_files:
        print(" -", f)


if __name__ == "__main__":
    main()
