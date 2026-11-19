"""
fix_sri.py — add Subresource Integrity (SRI) to every CDN-hosted <script> and
stylesheet <link> on the live static pages.

SRI = integrity="sha384-..." + crossorigin="anonymous" on the tag. The browser
hashes the file it downloads from the CDN and refuses to run/apply it if the
hash doesn't match — so a compromised or tampered CDN file can't inject code
into our pages.

* IDEMPOTENT: re-running replaces any existing integrity/crossorigin on the
  known URLs, so updating a hash below and re-running is all a version bump needs.
* Only exact, version-pinned URLs are listed. A URL WITHOUT a pinned version
  (e.g. bootstrap@5 or @latest) can never use SRI — its content changes.
* NOT covered on purpose: Google Fonts CSS (fonts.googleapis.com returns
  different CSS per browser, so it has no fixed hash), and GTM / GA4 / Clarity
  (loaded by inline snippets and updated by Google/Microsoft continuously).

WHEN YOU CHANGE A CDN VERSION: get the new hash, e.g.
    curl -s URL | openssl dgst -sha384 -binary | openssl base64 -A
add/replace the entry in SRI below, run this script, upload the changed pages.
(Hashes below were verified 2026-11-18 against Bootstrap's docs, the cdnjs API
and the jsDelivr API.)

Run from anywhere:  python3 scripts/fix_sri.py        (add --check for a dry run)
"""
import glob
import os
import re
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRI = {
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css":
        "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js":
        "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css":
        "sha384-/o6I2CkkWC//PSjvWC/eYN7l3xM3tJm8ZzVkCOfp//W05QcE3mlGskpoHB6XqI+B",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css":
        "sha384-QuGBSgV5Im3DzL2z+8Ko9/hqNy/N0O7zwvXAtfd1MvPKWa/UbeLV65cfm4BV5Wgq",
}

TAG_RE = re.compile(r"<(script|link)\b[^>]*>", re.I)
URL_RE = re.compile(r"""\b(?:src|href)\s*=\s*["']([^"']+)["']""", re.I)
STRIP_RE = re.compile(r"""\s+(?:integrity|crossorigin)(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+))?""", re.I)


def fix_tag(m):
    tag = m.group(0)
    u = URL_RE.search(tag)
    if not u or u.group(1) not in SRI:
        return tag
    clean = STRIP_RE.sub("", tag)
    end = "/>" if clean.endswith("/>") else ">"
    body = clean[: -len(end)].rstrip()
    return f'{body} integrity="{SRI[u.group(1)]}" crossorigin="anonymous"{end}'


def main():
    check = "--check" in sys.argv
    changed = []
    for path in sorted(glob.glob(os.path.join(SITE, "*.html"))):
        name = os.path.basename(path)
        if name.endswith("-off.html"):
            continue  # deactivated pages never deploy
        with open(path, encoding="utf-8") as f:
            html = f.read()
        new = TAG_RE.sub(fix_tag, html)
        if new != html:
            changed.append(name)
            if not check:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)
    verb = "WOULD change" if check else "changed"
    print(f"fix_sri: {len(changed)} {verb}")
    for n in changed:
        print("  ~", n)


if __name__ == "__main__":
    main()
