import os, re

SITE = '/Users/gdwebpros/Sites/GD-2013'
SKIP = {
    'boston-web-design-development-company.html', 'contact-gd-website-design-estimates.html',
    'contact-thanks.html', 'contacts.html', 'everett-ma-local-seo-services.html',
    'google07be07f249ecb0f1.html', 'googleae58b8e4a5c2267d.html',
    'local-marketing-boston-everett-malden-medford-revere-saugus-ma.html',
    'responsive-web-design-development-boston-ma.html', 'web-design-Boston-MA.html',
    'web-designer-developer-for-small-business-boston-ma.html',
    'web-dsigner-developer-for-small-business-boston-ma.html',
}

def add_class_to_tag(content, style_str, new_class):
    """
    For every tag containing style="style_str":
    - If tag has class="...", append new_class to it and remove the style attr.
    - If tag has no class, replace style="..." with class="new_class".
    Operates line-by-line to avoid crossing tag boundaries.
    """
    style_attr = f'style="{style_str}"'
    lines = content.split('\n')
    out = []
    for line in lines:
        if style_attr not in line:
            out.append(line)
            continue
        # Has existing class attribute on same line
        m = re.search(r'class="([^"]*)"', line)
        if m:
            existing = m.group(1)
            merged = (existing + ' ' + new_class).strip()
            line = line.replace(f'class="{existing}"', f'class="{merged}"', 1)
            line = line.replace(f' {style_attr}', '').replace(style_attr, '')
        else:
            line = line.replace(style_attr, f'class="{new_class}"')
        out.append(line)
    return '\n'.join(out)

REPLACEMENTS = [
    # btn-gold with sm size — exact class append
    ('class="btn-gold" style="font-size:.82rem;padding:.55rem 1.3rem;"',
     'class="btn-gold btn-gold-sm"'),

    # Green checkmark spans
    ('style="color: #28a745; margin-right: 0.5rem;"',   'class="check-green"'),
    ('style="color: #28a745; margin-right: 0.5rem"',    'class="check-green"'),

    # White links (both spacing variants)
    ('style="color: var(--white); text-decoration: none;"',  'class="link-white"'),
    ('style="color:var(--white);text-decoration:none;"',     'class="link-white"'),
    ('style="color: var(--white); text-decoration: none"',   'class="link-white"'),

    # Long pill-teal style
    ('style="display:inline-flex;align-items:center;gap:.45rem;background:rgba(4,65,67,.07);border:1px solid rgba(4,65,67,.18);color:var(--primary-light);font-size:.78rem;font-weight:600;padding:.3rem .85rem;border-radius:50px;"',
     'class="pill-teal"'),
    ('style="display:inline-flex;align-items:center;gap:.45rem;background:rgba(255,186,0,.08);border:1px solid rgba(255,186,0,.22);color:var(--accent-dark);font-size:.78rem;font-weight:600;padding:.3rem .85rem;border-radius:50px;"',
     'class="pill-teal pill-teal--gold"'),

    # list-style: circle
    ('style="list-style: circle;"',      'class="list-circle"'),
    ('style="text-align: left; list-style: circle;"', 'class="list-circle text-start"'),
]

# Styles to handle via add_class_to_tag (need class merging)
CLASS_MERGE = [
    ('color:var(--accent-dark)',          'text-accent-dark'),
    ('background-color:#024a4d',          'bg-dark-teal'),
]

total_files = 0

for fname in sorted(os.listdir(SITE)):
    if not fname.endswith('.html') or fname in SKIP:
        continue
    fpath = os.path.join(SITE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original

    # Exact string replacements
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    # Class-merge replacements
    for style_val, cls in CLASS_MERGE:
        content = add_class_to_tag(content, style_val, cls)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✓ {fname}')
        total_files += 1

print(f'\nDone — {total_files} files updated.')
