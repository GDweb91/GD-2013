"""Shared helper for the seo-technical scripts: locate the site root and
build the "live page" inventory every other script in this folder uses.

Reuses the redirect-stub/legacy-file list already maintained in
scripts/fix_navs.py (the SKIP set) instead of duplicating it — but that file
has no `if __name__ == '__main__':` guard around its nav-rewriting loop, so a
plain `import fix_navs` would rewrite every page's nav as a side effect of
just loading this helper. Its source is parsed with `ast` instead, purely to
pull out the SKIP literal, without ever executing the file.
"""
import ast
import os
import re

SITE = None
_path = os.path.dirname(os.path.abspath(__file__))
while True:
    if os.path.isfile(os.path.join(_path, "sitemap.xml")):
        SITE = _path
        break
    _parent = os.path.dirname(_path)
    if _parent == _path:
        raise RuntimeError("Could not locate site root (no sitemap.xml found above this file)")
    _path = _parent

DOMAIN = "https://gdprowebdesigns.com"


def _load_fix_navs_skip():
    fix_navs_path = os.path.join(SITE, "scripts", "fix_navs.py")
    with open(fix_navs_path, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=fix_navs_path)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "SKIP" for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise RuntimeError("Could not find SKIP assignment in scripts/fix_navs.py")


# fix_navs.py skips 'index.html' only because it's the copy-FROM source for
# nav edits, not because it isn't live — don't inherit that exclusion here.
LIVE_SKIP = _load_fix_navs_skip() - {"index.html"}

# A handful of live pages that live in subfolders, not the site root.
SUBDIR_PAGES = [
    "blog/custom-website-or-DIY.html",
    "blog/how-to-create-your-own-website-with-wordpress.html",
    "shopify/shopify-developer-boston-ma-ecommerce.html",
]


def is_off_page(filename):
    """Deactivated pages are named *-off.html by convention (see CLAUDE.md)."""
    return filename.endswith("-off.html")


def live_pages():
    """Sorted list of paths (relative to SITE) for every live HTML page.

    LIVE_SKIP (from fix_navs.py) is known to be incomplete — it missed
    internet-marketing-local-marketing-everett-malden-medford-revere-saugus-ma.html,
    a real .htaccess redirect-stub file left on disk (found 2026-08-20 while
    regenerating sitemap.xml). Rather than special-case that one filename,
    any candidate whose path itself matches a known .htaccess redirect
    source is excluded here — self-correcting against this whole class of
    gap instead of just the one instance found so far.
    """
    pages = []
    for name in sorted(os.listdir(SITE)):
        if not name.endswith(".html"):
            continue
        if name in LIVE_SKIP or is_off_page(name):
            continue
        if redirect_target(name):
            continue
        pages.append(name)
    for rel in SUBDIR_PAGES:
        if os.path.isfile(os.path.join(SITE, rel)):
            pages.append(rel)
    return pages


def url_for(rel_path):
    return f"{DOMAIN}/{rel_path}"


def path_for_url(url):
    """Strip domain from a sitemap/live URL, return the relative site path
    (e.g. 'https://gdprowebdesigns.com/foo.html' -> 'foo.html', '/' -> '')."""
    for prefix in (DOMAIN + "/", DOMAIN):
        if url.startswith(prefix):
            return url[len(prefix):]
    return url


_REWRITE_RE = re.compile(
    r"^RewriteRule\s+\^(?P<pattern>.+?)\$\s+(?P<dest>\S+)\s+\[R=301", re.MULTILINE
)
_htaccess_redirects_cache = None


def htaccess_redirects():
    """(compiled_source_regex, destination_url) pairs from the '# 301
    REDIRECTS' section of .htaccess, in file order. Cached after first call."""
    global _htaccess_redirects_cache
    if _htaccess_redirects_cache is not None:
        return _htaccess_redirects_cache
    with open(os.path.join(SITE, ".htaccess"), encoding="utf-8") as f:
        text = f.read()
    # Scope to the marked redirects section (skips the WordPress block, which
    # has its own unrelated RewriteRule lines with no [R=301] flag anyway).
    # Note: "# BEGIN WordPress" also appears quoted inside the section's own
    # explanatory comment, so match it as a line start (preceded by \n) to
    # find the real marker further down, not that in-comment mention.
    start = text.find("# 301 REDIRECTS")
    end = text.find("\n# BEGIN WordPress")
    section = text[start:end] if start != -1 else text
    redirects = []
    for m in _REWRITE_RE.finditer(section):
        try:
            rx = re.compile("^" + m.group("pattern") + "$")
        except re.error:
            continue
        redirects.append((rx, m.group("dest")))
    _htaccess_redirects_cache = redirects
    return redirects


def redirect_target(rel_path):
    """Destination URL if rel_path matches a known .htaccess redirect source,
    else None. rel_path should have no leading slash (e.g. 'foo.html')."""
    for rx, dest in htaccess_redirects():
        if rx.match(rel_path):
            return dest
    return None
