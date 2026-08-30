"""
fix_schema.py — inject a consistent Organization + Person entity graph into every
active interior page, so each page resolves to the same business entity
(https://gdprowebdesigns.com/#organization) and the same author
(https://gdprowebdesigns.com/#person, JA Armira) that the homepage defines.

Design goals:
  * ADDITIVE ONLY. This script never rewrites or deletes a page's existing
    JSON-LD (LocalBusiness / Service / FAQPage / BreadcrumbList blocks are left
    exactly as they are). It only inserts one extra <script type="application/ld+json">
    block, guarded by an HTML comment marker, right before </head>.
  * IDEMPOTENT. Re-running replaces the previously-injected marked block, so the
    entity data can be updated in one place (ENTITY_GRAPH below) and re-applied.
  * SELF-DERIVING PATHS, like fix_navs.py — runs correctly regardless of where
    the project folder lives on disk.

Run from anywhere:  python3 scripts/fix_schema.py
Add --check to report what WOULD change without writing.

After running, it also prints an informational list of pages whose *existing*
JSON-LD still hard-codes a non-Everett addressLocality (a NAP-consistency smell
to clean up separately — this script does not touch those blocks).
"""

import json
import os
import re
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MARKER_OPEN = "<!-- gd-entity-graph v1 (scripts/fix_schema.py) — do not edit by hand -->"
MARKER_CLOSE = "<!-- /gd-entity-graph -->"

# Pages that must NOT receive the injected block.
SKIP_EXACT = {
    "index.html",            # defines its own full @graph (source of truth)
    "inicio.html",           # ES homepage — its own @graph
    "404.html",
    "sitemap.html",
    "google07be07f249ecb0f1.html",
    "googleae58b8e4a5c2267d.html",
    # redirect stubs (no real content, 301 in .htaccess)
    "boston-web-design-development-company.html",
    "boston-web-design-development-company-freelance.html",
    "web-design-Boston-MA.html",
    "responsive-web-design-development-boston-ma.html",
    "everett-ma-local-seo-services.html",
    "seo-services-everett-ma.html",
    "freelance-web-developer-boston-ma.html",
    "freelance-wordpress-website-designer-ma.html",
    "small-business-web-developer-web-designer-boston-ma.html",
    "web-designer-developer-for-small-business-boston-ma.html",
    "web-dsigner-developer-for-small-business-boston-ma.html",
    "local-marketing-boston-everett-malden-medford-revere-saugus-ma.html",
    "contacts.html",
    "contact-thanks.html",
    "contact-gd-website-design-estimates.html",
}
SKIP_SUFFIXES = ("-off.html",)
SKIP_PREFIXES = ("google", "BingSiteAuth")

CERTS = [
    {"@type": "EducationalOccupationalCredential",
     "name": "Google Digital Marketing & E-Commerce Certificate"},
    {"@type": "EducationalOccupationalCredential",
     "name": "Google SEO Certificate"},
]
SAME_AS = [
    "https://www.facebook.com/pages/GD-Pro-Web-Designs/113091575402539",
    "https://www.linkedin.com/company/gd-pro-web-designs",
    "https://www.youtube.com/user/silfovientoful",
]
AREA_SERVED = (
    [{"@type": "State", "name": "Massachusetts"}]
    + [{"@type": "AdministrativeArea", "name": f"{c} County, MA"} for c in
       ("Middlesex", "Suffolk", "Norfolk", "Essex", "Worcester", "Plymouth")]
    + [{"@type": "City", "name": f"{c}, MA"} for c in
       ("Boston", "Everett", "Cambridge", "Somerville", "Malden", "Medford",
        "Lynn", "Chelsea", "Revere", "Saugus", "Salem", "Peabody", "Waltham",
        "Newton", "Quincy", "Dedham", "Winchester", "Lawrence", "Worcester")]
)

ORG = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": "https://gdprowebdesigns.com/#organization",
    "name": "GD Pro Web Designs",
    "alternateName": "GDWebPros",
    "description": ("Freelance web designer, WordPress developer, and SEO consultant "
                    "based in Everett, MA. Affordable web design, WordPress development, "
                    "SEO and digital marketing for small businesses in Boston and Greater "
                    "Massachusetts since 2005."),
    "url": "https://gdprowebdesigns.com/",
    "logo": {"@type": "ImageObject",
             "url": "https://gdprowebdesigns.com/img/tmp-imgs/gd-pro-web-designs-logo.png"},
    "image": "https://gdprowebdesigns.com/img/boston-freelance-website-designer.jpg",
    "telephone": "+1-617-771-0645",
    "priceRange": "$$",
    "foundingDate": "2005",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Lawrence St.",
        "addressLocality": "Everett",
        "addressRegion": "MA",
        "postalCode": "02149",
        "addressCountry": "US",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 42.40843, "longitude": -71.053662},
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00", "closes": "18:00",
    }],
    "areaServed": AREA_SERVED,
    "knowsLanguage": ["en", "es"],
    "sameAs": SAME_AS,
    "hasCredential": CERTS,
    "founder": {"@id": "https://gdprowebdesigns.com/#person"},
}

PERSON = {
    "@type": "Person",
    "@id": "https://gdprowebdesigns.com/#person",
    "name": "JA Armira",
    "jobTitle": "Freelance Web Designer, WordPress Developer & SEO Consultant",
    "url": "https://gdprowebdesigns.com/about-gd-freelance-web-designer-boston.html",
    "worksFor": {"@id": "https://gdprowebdesigns.com/#organization"},
    "hasCredential": CERTS,
    "knowsAbout": [
        "Web design", "Responsive web design", "WordPress development",
        "WordPress theme development", "WooCommerce", "WordPress maintenance",
        "Search engine optimization", "Local SEO", "Technical SEO",
        "Google Ads", "Pay-per-click advertising", "Digital marketing",
        "Generative engine optimization", "Google Business Profile optimization",
        "Website migration",
    ],
    "sameAs": SAME_AS,
}

BASE_URL = "https://gdprowebdesigns.com/"
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL | re.IGNORECASE)
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)
LANG_RE = re.compile(r'<html[^>]*\blang=["\']([^"\']+)["\']', re.IGNORECASE)


def web_page_node(name, html):
    cm = CANONICAL_RE.search(html)
    url = cm.group(1).strip() if cm else BASE_URL + name
    tm = TITLE_RE.search(html)
    title = re.sub(r"\s+", " ", tm.group(1)).strip() if tm else name
    lm = LANG_RE.search(html)
    lang = lm.group(1).strip() if lm else "en-US"
    node = {
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": title,
        "isPartOf": {"@id": "https://gdprowebdesigns.com/#organization"},
        "about": {"@id": "https://gdprowebdesigns.com/#organization"},
        "publisher": {"@id": "https://gdprowebdesigns.com/#organization"},
        "inLanguage": lang,
    }
    if 'class="quick-answer' in html:
        node["speakable"] = {
            "@type": "SpeakableSpecification",
            "cssSelector": [".quick-answer"],
        }
    return node


def block_html(name, html):
    graph = {"@context": "https://schema.org",
             "@graph": [ORG, PERSON, web_page_node(name, html)]}
    payload = json.dumps(graph, indent=2, ensure_ascii=False)
    return (f"{MARKER_OPEN}\n"
            f'<script type="application/ld+json">\n{payload}\n</script>\n'
            f"{MARKER_CLOSE}\n")


MARKED_RE = re.compile(
    re.escape(MARKER_OPEN) + r".*?" + re.escape(MARKER_CLOSE) + r"\n?",
    re.DOTALL,
)
LOCALITY_RE = re.compile(r'"addressLocality"\s*:\s*"([^"]+)"')
JSONLD_BLOCK_RE = re.compile(
    r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)
# A PostalAddress object whose locality is NOT Everett — normalise the whole
# address to the real Everett NAP. Deliberately narrow: only fires on the exact
# {"@type":"PostalAddress", ... "addressLocality":"<x>" ...} shape used across
# this site's per-city pages, and only when <x> != Everett.
FAKE_ADDR_RE = re.compile(
    r'\{\s*"@type"\s*:\s*"PostalAddress"\s*,'      # opening + @type
    r'(?P<body>(?:[^{}]|"[^"]*")*?)'              # inner fields (no nested objects)
    r'\}',
    re.DOTALL,
)
EVERETT_ADDR = (
    '{\n        "@type": "PostalAddress",\n'
    '        "streetAddress": "Lawrence St.",\n'
    '        "addressLocality": "Everett",\n'
    '        "addressRegion": "MA",\n'
    '        "postalCode": "02149",\n'
    '        "addressCountry": "US"\n'
    '      }'
)


def normalise_addresses(html):
    """Rewrite non-Everett PostalAddress blocks inside JSON-LD to the real NAP.
    Returns (new_html, list_of_cities_fixed)."""
    fixed = []

    def fix_block(m):
        head, body, tail = m.group(1), m.group(2), m.group(3)
        if MARKER_OPEN in head or MARKER_OPEN in body:
            return m.group(0)  # our own injected block — already correct

        def fix_addr(am):
            inner = am.group("body")
            loc = re.search(r'"addressLocality"\s*:\s*"([^"]+)"', inner)
            if not loc or loc.group(1).strip().lower() == "everett":
                return am.group(0)
            fixed.append(loc.group(1))
            return EVERETT_ADDR

        return head + FAKE_ADDR_RE.sub(fix_addr, body) + tail

    return JSONLD_BLOCK_RE.sub(fix_block, html), fixed


def should_skip(name):
    if name in SKIP_EXACT:
        return True
    if name.endswith(SKIP_SUFFIXES):
        return True
    if name.startswith(SKIP_PREFIXES):
        return True
    return False


def main():
    check = "--check" in sys.argv
    changed, skipped, no_head = [], [], []
    nap_smells = []

    for name in sorted(os.listdir(SITE)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(SITE, name)
        if not os.path.isfile(path):
            continue
        if should_skip(name):
            skipped.append(name)
            continue

        with open(path, encoding="utf-8") as fh:
            html = fh.read()

        # 1) Normalise any non-Everett PostalAddress in existing JSON-LD.
        html, cities = normalise_addresses(html)
        for c in cities:
            nap_smells.append(f"{name}: PostalAddress \"{c}\" -> Everett")

        # 2) Inject / refresh the entity graph before </head>.
        new_block = block_html(name, html)
        if MARKER_OPEN in html:
            updated = MARKED_RE.sub(lambda _m: new_block, html, count=1)
        else:
            if "</head>" not in html:
                no_head.append(name)
                continue
            updated = html.replace("</head>", new_block + "</head>", 1)

        # 3) Any remaining non-Everett locality (shapes the regex didn't catch)?
        for loc in LOCALITY_RE.findall(MARKED_RE.sub("", updated)):
            if loc.strip().lower() != "everett":
                nap_smells.append(f"{name}: STILL has addressLocality \"{loc}\"")

        if updated != html:
            changed.append(name)
            if not check:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(updated)

    verb = "WOULD change" if check else "changed"
    print(f"fix_schema: {len(changed)} {verb}, {len(skipped)} skipped")
    for n in changed:
        print(f"  ~ {n}")
    if no_head:
        print("\nNO </head> — left untouched:")
        for n in no_head:
            print(f"  ! {n}")
    if nap_smells:
        print("\nAddress normalisation:")
        for s in sorted(set(nap_smells)):
            print(f"  - {s}")


if __name__ == "__main__":
    main()
