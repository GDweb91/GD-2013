#!/usr/bin/env python3
"""Thin-content and near-duplicate-content checks across every live page.

This exists because of the site's own history: the Sept 2025 ranking crash
was root-caused to Google's scaled/duplicate-content spam update hitting
this site's ~20 templated city pages. Thresholds are ported from the
third-party claude-seo repo's seo-programmatic skill (unique content % =
words unique to a page vs. the rest of the site, excluding shared
nav/footer boilerplate): <40% unique -> warning, <30% unique -> critical,
<300 words on a page -> thin-content warning.

Usage: python3 duplicate_content_check.py
"""
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _site_root as sr

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.DOTALL | re.IGNORECASE)
NAV_RE = re.compile(r'<nav\b[^>]*\bid=["\']mainNav["\'][^>]*>.*?</nav>', re.DOTALL | re.IGNORECASE)
FOOTER_RE = re.compile(r'<footer\s+id=["\']footer["\'].*?</footer>', re.DOTALL | re.IGNORECASE)
STICKY_BAR_RE = re.compile(
    r'<div\s+class=["\']sticky-call-bar["\'].*', re.DOTALL | re.IGNORECASE
)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")

THIN_WORD_COUNT = 300
CRITICAL_SIMILARITY = 0.70
WARNING_SIMILARITY = 0.60
QUICK_RATIO_PREFILTER = 0.50


def extract_body_text(rel_path):
    """Visible body text with shared boilerplate (nav/footer/sticky call
    bar/scripts/styles/comments) stripped, so similarity reflects actual
    page content rather than the markup every page shares."""
    with open(os.path.join(sr.SITE, rel_path), encoding="utf-8", errors="replace") as f:
        html = f.read()
    html = COMMENT_RE.sub("", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    html = NAV_RE.sub(" ", html)
    html = FOOTER_RE.sub(" ", html)
    html = STICKY_BAR_RE.sub(" ", html)
    text = TAG_RE.sub(" ", html)
    text = WS_RE.sub(" ", text).strip().lower()
    return text


def main():
    pages = sr.live_pages()
    # Compare word-token lists rather than raw character strings: faster
    # (hundreds of tokens vs. thousands of characters per page) and more
    # meaningful for "same template, city name swapped" detection.
    tokens = {p: extract_body_text(p).split() for p in pages}
    word_counts = {p: len(t) for p, t in tokens.items()}

    issues = []  # (severity, message)

    for p in sorted(pages):
        wc = word_counts[p]
        if wc < THIN_WORD_COUNT:
            issues.append(("warning", f"Thin content ({wc} words, boilerplate excluded): {p}"))

    matchers = {p: difflib.SequenceMatcher(a=t) for p, t in tokens.items()}
    best = {}  # page -> (score, other_page)
    reported_pairs = set()

    for i, p1 in enumerate(pages):
        for p2 in pages[i + 1:]:
            m = matchers[p1]
            m.set_seq2(tokens[p2])
            if m.quick_ratio() < QUICK_RATIO_PREFILTER:
                continue
            score = m.ratio()
            if score > best.get(p1, (0, None))[0]:
                best[p1] = (score, p2)
            if score > best.get(p2, (0, None))[0]:
                best[p2] = (score, p1)

    for p, (score, other) in sorted(best.items(), key=lambda kv: -kv[1][0]):
        pair_key = tuple(sorted((p, other)))
        if pair_key in reported_pairs:
            continue
        if score >= WARNING_SIMILARITY:
            reported_pairs.add(pair_key)
            severity = "critical" if score >= CRITICAL_SIMILARITY else "warning"
            issues.append((
                severity,
                f"{pair_key[0]!r} is {score:.0%} similar to {pair_key[1]!r} "
                f"after excluding nav/footer/sticky-bar "
                f"({word_counts[pair_key[0]]} vs {word_counts[pair_key[1]]} words)",
            ))

    critical = [m for s, m in issues if s == "critical"]
    warning = [m for s, m in issues if s == "warning"]

    print(f"duplicate_content_check: {len(pages)} live pages compared\n")
    print(f"CRITICAL ({len(critical)}) — likely scaled-content-abuse risk (≥70% similar):")
    for m in critical:
        print(f"  ✗ {m}")
    print(f"\nWARNING ({len(warning)}) — thin content or low differentiation:")
    for m in warning:
        print(f"  ⚠ {m}")


if __name__ == "__main__":
    main()
