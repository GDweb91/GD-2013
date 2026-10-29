"""
fix_gbp_name_note.py — add a footer line telling visitors that the Google Maps
listing "J.A. Armira (Freelance Web Designer)" is this same business.

Why: the Google Business Profile can't be named "GD Pro Web Designs" until the
DBA is filed (seo/gbp-checklist.md §3). Visitors arriving from Maps see a
different name than the site's, so the footer confirms they're the same
business and links back to the listing.

  * Inserted right after the footer's address row (f-contact-row with the
    map-marker icon), wrapped in marker comments.
  * IDEMPOTENT: re-running replaces the marked block.
  * Spanish pages (<html lang="es">) get a Spanish line.
  * --remove deletes the block from every page — run this once Google
    renames the listing back to "GD Pro Web Designs".

Run from anywhere:  python3 scripts/fix_gbp_name_note.py [--remove]
"""

import os
import re
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GBP_URL = "https://maps.google.com/?cid=14742453980006491533"
GBP_NAME = "J.A. Armira (Freelance Web Designer)"

MARK_OPEN = "<!-- gbp-name-note (scripts/fix_gbp_name_note.py) -->"
MARK_CLOSE = "<!-- /gbp-name-note -->"

TEXT = {
    "en": "On Google Maps as {link} &mdash; same business, same owner",
    "es": "En Google Maps como {link} &mdash; el mismo negocio",
}

ADDRESS_ROW = re.compile(
    r'(<div class="f-contact-row"><i class="fas fa-map-marker-alt"[^>]*></i>.*?</div>\n)')
EXISTING = re.compile(r'[ \t]*' + re.escape(MARK_OPEN) + r'.*?' + re.escape(MARK_CLOSE) + r'\n',
                      re.S)


def note_html(lang, indent):
    link = (f'<a href="{GBP_URL}" target="_blank" rel="noopener">{GBP_NAME}</a>')
    return (f'{indent}{MARK_OPEN}\n'
            f'{indent}<div class="f-contact-row"><i class="fab fa-google" aria-hidden="true"></i>'
            f'<span>{TEXT[lang].format(link=link)}</span></div>\n'
            f'{indent}{MARK_CLOSE}\n')


def main():
    remove = "--remove" in sys.argv
    changed, no_footer = [], []
    for name in sorted(os.listdir(SITE)):
        if not name.endswith(".html") or name.endswith("-off.html") or name.startswith("google"):
            continue
        path = os.path.join(SITE, name)
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        out = EXISTING.sub("", src)
        if not remove:
            m = ADDRESS_ROW.search(out)
            if not m:
                no_footer.append(name)
                continue
            line_start = out.rfind("\n", 0, m.start()) + 1
            indent = out[line_start:m.start()]
            lang = "es" if '<html lang="es"' in out else "en"
            out = out[:m.end()] + note_html(lang, indent) + out[m.end():]
        if out != src:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(out)
            changed.append(name)
    print(f"fix_gbp_name_note: {len(changed)} changed" + (" (removed)" if remove else ""))
    for n in changed:
        print("  ~", n)
    if no_footer:
        print(f"No footer address row (skipped, {len(no_footer)}): " + ", ".join(no_footer))


if __name__ == "__main__":
    main()
