"""
Cache-bust css/custom.css on every active static page.

The static site sits behind Cloudflare (managed through Bluehost), which caches
css/custom.css at the edge for a day, and Bluehost's dashboard has no cache-purge
option for the static (non-WordPress) part of the site. So an uploaded CSS change
doesn't reach visitors until that cached copy expires.

This script rewrites every
    <link rel="stylesheet" href="css/custom.css">            (or ../css/custom.css)
    <link rel="stylesheet" href="css/custom.css?v=OLD">
to
    <link rel="stylesheet" href="css/custom.css?v=VERSION">

Cloudflare and browsers treat a new ?v= value as a brand-new file, so the fresh
CSS loads as soon as the updated pages are uploaded.

Usage (from the site root), after any change to css/custom.css:
    python3 scripts/fix_css_version.py              # VERSION = today, YYYYMMDD
    python3 scripts/fix_css_version.py 20261027b    # explicit version
Then upload css/custom.css plus every page the script lists as changed.

Idempotent — re-running with the same VERSION changes nothing. Skips archive/,
node_modules/, seo/, index-css/, deactivated *-off.html pages and redirect stubs
(none of those are deployed).
"""
import datetime
import glob
import os
import re
import sys

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = ('node_modules', 'archive', 'seo', 'index-css')
# Redirect stubs (301'd in .htaccess) — never served, so never uploaded.
SKIP_FILES = {
    'seo-services-everett-ma.html',
    'small-business-web-developer-web-designer-boston-ma.html',
}

LINK_RE = re.compile(r'href="((?:\.\./)*css/custom\.css)(?:\?v=[^"]*)?"')


def main():
    version = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().strftime('%Y%m%d')
    os.chdir(SITE_ROOT)
    changed = []
    for path in sorted(glob.glob('**/*.html', recursive=True)):
        if any(part in SKIP_DIRS for part in path.split(os.sep)):
            continue
        name = os.path.basename(path)
        if name in SKIP_FILES or name.endswith('-off.html'):
            continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        new_html = LINK_RE.sub(lambda m: 'href="{}?v={}"'.format(m.group(1), version), html)
        if new_html != html:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            changed.append(path)

    print('custom.css version: {}'.format(version))
    print('{} page(s) updated:'.format(len(changed)))
    for path in changed:
        print('  ' + path)


if __name__ == '__main__':
    main()
