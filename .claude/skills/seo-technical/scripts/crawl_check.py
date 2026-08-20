#!/usr/bin/env python3
"""Local structural checks across every live page: broken internal links,
links that route through a redirect instead of hitting the canonical page
directly, exact-duplicate <title>/meta description across pages, and <img>
tags with no alt attribute at all.

Usage: python3 crawl_check.py
"""
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _site_root as sr

HREF_RE = re.compile(r'<a\b[^>]*\bhref=["\']([^"\']*)["\']', re.IGNORECASE)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL | re.IGNORECASE)
META_DESC_RE = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', re.IGNORECASE
)
IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ALT_ATTR_RE = re.compile(r"\balt\s*=", re.IGNORECASE)

SAME_DOMAIN_HOSTS = {"gdprowebdesigns.com", "www.gdprowebdesigns.com"}

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_html_cache = {}


def read_html(rel_path):
    """Read a page once, with HTML comments stripped — commented-out old
    markup (a leftover <a href>, an <img> mentioned in a dev note, a dead
    <title>) would otherwise read as live content and produce false
    positives. Cached since every check function needs every page."""
    if rel_path not in _html_cache:
        with open(os.path.join(sr.SITE, rel_path), encoding="utf-8", errors="replace") as f:
            _html_cache[rel_path] = COMMENT_RE.sub("", f.read())
    return _html_cache[rel_path]


def classify_link(page_rel_path, href):
    href = href.strip()
    if not href:
        return "skip", href
    parsed = urllib.parse.urlparse(href)

    if parsed.scheme in ("mailto", "tel", "javascript"):
        return "skip", href
    if parsed.scheme in ("http", "https"):
        if parsed.netloc.lower() not in SAME_DOMAIN_HOSTS:
            return "external", href
        path = parsed.path
    else:
        path = parsed.path

    if not path or path == "/":
        return "local", ""
    # Site convention (see CLAUDE.md) writes these without a leading slash
    # (e.g. href="gd-blog/contact-us/"), so check the lstripped form.
    if path.lstrip("/").startswith("gd-blog"):
        return "wp", href

    if path.startswith("/"):
        rel_target = path.lstrip("/")
    else:
        page_dir = os.path.dirname(page_rel_path)
        rel_target = os.path.normpath(os.path.join(page_dir, path)).replace(os.sep, "/")
        if rel_target.startswith("../"):
            return "outside-repo", href

    return "local", rel_target


def check_links(pages):
    findings = []
    for rel in pages:
        html = read_html(rel)
        for href in HREF_RE.findall(html):
            kind, target = classify_link(rel, href)
            if kind in ("skip", "external", "wp", "outside-repo"):
                continue
            if target == "":
                continue  # homepage
            # Apache decodes %-escapes before matching .htaccess RewriteRule
            # patterns, so check existence/redirects against the decoded form
            # to match what a real request would actually resolve to.
            target = urllib.parse.unquote(target)
            full = os.path.join(sr.SITE, target)
            if os.path.isfile(full):
                continue
            redirect_dest = sr.redirect_target(target)
            if redirect_dest:
                findings.append((
                    "warning",
                    f"{rel}: links to '{href}', which itself 301s to {redirect_dest} — "
                    f"point the link at the destination directly",
                ))
            else:
                findings.append(("critical", f"{rel}: broken internal link — '{href}' has no matching file and no redirect"))
    return findings


def check_duplicates(pages):
    findings = []
    titles = {}
    descs = {}
    for rel in pages:
        html = read_html(rel)
        tm = TITLE_RE.search(html)
        if tm:
            titles.setdefault(tm.group(1).strip(), []).append(rel)
        dm = META_DESC_RE.search(html)
        if dm:
            descs.setdefault(dm.group(1).strip(), []).append(rel)

    for title, owners in titles.items():
        if len(owners) > 1:
            findings.append(("critical", f"Duplicate <title> \"{title}\" on: {', '.join(owners)}"))
    for desc, owners in descs.items():
        if len(owners) > 1:
            findings.append(("warning", f"Duplicate meta description on: {', '.join(owners)} — \"{desc[:80]}...\""))
    return findings


def check_alt_text(pages):
    findings = []
    for rel in pages:
        html = read_html(rel)
        missing = sum(1 for tag in IMG_RE.findall(html) if not ALT_ATTR_RE.search(tag))
        if missing:
            findings.append(("warning", f"{rel}: {missing} <img> tag(s) with no alt attribute"))
    return findings


def main():
    pages = sr.live_pages()
    all_findings = []
    all_findings += check_links(pages)
    all_findings += check_duplicates(pages)
    all_findings += check_alt_text(pages)

    critical = [m for s, m in all_findings if s == "critical"]
    warning = [m for s, m in all_findings if s == "warning"]

    print(f"crawl_check: {len(pages)} live pages scanned\n")
    print(f"CRITICAL ({len(critical)}):")
    for m in critical:
        print(f"  ✗ {m}")
    print(f"\nWARNING ({len(warning)}):")
    for m in warning:
        print(f"  ⚠ {m}")


if __name__ == "__main__":
    main()
