#!/usr/bin/env python3
"""Validate every <script type="application/ld+json"> block across the live
pages: JSON parse errors, missing @context/@type, leftover placeholder text,
and types Google no longer grants rich results for. Also reports pages that
carry no JSON-LD at all, so a real gap can be told apart from an intentional
one.

Usage: python3 schema_check.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _site_root as sr

LD_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)

PLACEHOLDER_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"\[business name\]", r"\[company name\]", r"\[your \w+\]",
        r"\{\{.*?\}\}", r"lorem ipsum", r"your company name",
        r"\bjohn doe\b", r"\bjane doe\b", r"123-456-7890",
        r"example\.com/(?!\.well-known)",
    ]
]

# Types where the markup is still valid Schema.org but Google no longer
# grants (or has restricted) a rich result for it, per Search Central
# announcements as of early 2026 — worth flagging even though it won't error.
GOOGLE_LIMITED_TYPES = {
    "HowTo": "Google dropped HowTo rich results (Sept 2023) — valid markup, no rich-result benefit.",
    "SpecialAnnouncement": "Google dropped SpecialAnnouncement rich results (2023, was COVID-era) — valid markup, no rich-result benefit.",
    "FAQPage": "Google limited FAQPage rich results to authoritative gov/health sites (Aug 2023) — a small-business FAQPage is unlikely to earn the rich result even though the markup is valid.",
}


def extract_blocks(html):
    return LD_JSON_RE.findall(html)


def check_page(rel_path):
    full_path = os.path.join(sr.SITE, rel_path)
    with open(full_path, encoding="utf-8", errors="replace") as f:
        html = f.read()

    blocks = extract_blocks(html)
    findings = []

    if not blocks:
        return findings, 0

    for i, raw in enumerate(blocks, start=1):
        where = f"{rel_path} (JSON-LD block {i}/{len(blocks)})"
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            findings.append(("critical", f"{where}: JSON parse error — {e.msg} at line {e.lineno} col {e.colno}"))
            continue

        # A "@graph" wrapper's single top-level @context covers every node
        # inside it by design (the standard way to bundle multiple JSON-LD
        # entities in one block) — only a bare object or bare array needs
        # @context checked per-node.
        if isinstance(data, dict) and "@graph" in data:
            if "@context" not in data:
                findings.append(("warning", f"{where}: missing @context on @graph wrapper"))
            graph = data["@graph"]
            nodes = graph if isinstance(graph, list) else [graph]
            check_context_per_node = False
        elif isinstance(data, list):
            nodes = data
            check_context_per_node = True
        else:
            nodes = [data]
            check_context_per_node = True

        for item in nodes:
            if not isinstance(item, dict):
                continue
            if check_context_per_node and "@context" not in item:
                findings.append(("warning", f"{where}: missing @context"))
            if "@type" not in item:
                findings.append(("warning", f"{where}: missing @type"))
                continue
            types = item["@type"] if isinstance(item["@type"], list) else [item["@type"]]
            for t in types:
                if t in GOOGLE_LIMITED_TYPES:
                    findings.append(("info", f"{where}: @type '{t}' — {GOOGLE_LIMITED_TYPES[t]}"))

        for pattern in PLACEHOLDER_PATTERNS:
            m = pattern.search(raw)
            if m:
                findings.append(("critical", f"{where}: placeholder text left in structured data — matched '{m.group(0)}'"))

    return findings, len(blocks)


def main():
    pages = sr.live_pages()
    all_findings = []
    no_schema = []

    for rel in pages:
        findings, block_count = check_page(rel)
        all_findings.extend(findings)
        if block_count == 0:
            no_schema.append(rel)

    critical = [m for s, m in all_findings if s == "critical"]
    warning = [m for s, m in all_findings if s == "warning"]
    info = [m for s, m in all_findings if s == "info"]

    print(f"schema_check: {len(pages)} live pages scanned\n")
    print(f"CRITICAL ({len(critical)}):")
    for m in critical:
        print(f"  ✗ {m}")
    print(f"\nWARNING ({len(warning)}):")
    for m in warning:
        print(f"  ⚠ {m}")
    print(f"\nINFO ({len(info)}):")
    for m in info:
        print(f"  - {m}")
    print(f"\nPAGES WITH NO JSON-LD ({len(no_schema)}/{len(pages)}):")
    for p in no_schema:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
