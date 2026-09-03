"""
Site-wide phone-scraping protection + sticky Call Now bar.

What it does to every active .html page:
1. Rewrites every <a href="tel:6177710645" ...>...</a> so the raw digits never
   appear in the page source: href becomes "#" + data-tel="<reversed digits>",
   and the visible number is replaced with an empty <span class="phone-num">
   that js/phone-protect.js fills in on DOMContentLoaded. Any surrounding label
   text in the same anchor ("Just call:", "Llamenos al", "Tel:", etc.) is left
   untouched.
2. Adds <link rel="stylesheet" href="css/phone-protect.css"> before </head>.
3. Adds <script src="js/phone-protect.js" defer></script> plus the sticky
   #stickyCallBar markup before </body>.

Idempotent — safe to re-run after adding new pages. JSON-LD "telephone" and
<meta> description mentions of the phone number are intentionally left alone
(needed for local SEO / Google Business Profile matching and search snippet
CTR — those aren't the vector that harvests tel: links at scale).

Run from the site root: python3 scripts/fix_phone_protection.py
"""
import glob
import os
import re

DIGITS = '6177710645'
ENCODED = DIGITS[::-1]

SKIP_DIRS = ('node_modules', 'archive', 'seo', 'index-css')
SKIP_FILES = {
    'google07be07f249ecb0f1.html',
    'googleae58b8e4a5c2267d.html',
}

ANCHOR_RE = re.compile(
    r'<a href="tel:6177710645"((?:\s+[\w-]+="[^"]*")*)\s*>(.*?)</a>',
    re.DOTALL,
)
NUM_RE = re.compile(r'\(?617\)?[\s-]?771[\s-]?0645')

STICKY_BAR_TMPL = (
    '<div class="sticky-call-bar" id="stickyCallBar">\n'
    '  <a href="#" data-tel="{encoded}" class="sticky-call-btn" '
    'aria-label="Call GD Pro Web Designs now">\n'
    '    <i class="fas fa-phone-alt"></i> Call Now\n'
    '  </a>\n'
    '</div>\n'
)


def rewrite_anchor(match):
    attrs, inner = match.group(1), match.group(2)
    new_inner, n = NUM_RE.subn('<span class="phone-num"></span>', inner)
    if n == 0:
        new_inner = '<span class="phone-num"></span>'
    return '<a href="#" data-tel="{}"{} aria-label="Call GD Pro Web Designs">{}</a>'.format(
        ENCODED, attrs, new_inner
    )


def process(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    original = content

    # One-off repair: a premature </body> in this file puts the footer and
    # analytics scripts outside <body>. Collapse to the final </body>.
    if path.endswith('Jamaica-Plain-wordpress-developer.html'):
        first = content.find('</body>')
        last = content.rfind('</body>')
        if first != last:
            content = content[:first] + content[first + len('</body>'):]

    content, anchor_subs = ANCHOR_RE.subn(rewrite_anchor, content)

    depth = path.count(os.sep)
    prefix = '../' * depth

    if 'phone-protect.css' not in content and '</head>' in content:
        content = content.replace(
            '</head>',
            '<link rel="stylesheet" href="{}css/phone-protect.css">\n</head>'.format(prefix),
            1,
        )

    if 'stickyCallBar' not in content and '</body>' in content:
        injection = (
            '<script src="{}js/phone-protect.js" defer></script>\n'.format(prefix)
            + STICKY_BAR_TMPL.format(encoded=ENCODED)
        )
        content = content.replace('</body>', injection + '</body>', 1)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return anchor_subs
    return None


def main():
    changed = []
    for path in glob.glob('**/*.html', recursive=True):
        if any(part in SKIP_DIRS for part in path.split(os.sep)):
            continue
        if os.path.basename(path) in SKIP_FILES:
            continue
        result = process(path)
        if result is not None:
            changed.append((path, result))

    for path, anchor_subs in changed:
        print('{}: {} anchor(s) rewritten'.format(path, anchor_subs))
    print('Total files touched: {}'.format(len(changed)))


if __name__ == '__main__':
    main()
