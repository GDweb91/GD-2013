# GD-2013 — GD Pro Web Designs Static Site

## What This Project Is

Static HTML business website for **GD Pro Web Designs**, a freelance web design, WordPress development, and SEO consultancy run by **JA Armira**, based in **Everett, MA** (3 miles from downtown Boston). The site has been live since 2005 at **https://gdprowebdesigns.com**.

This is NOT a WordPress theme — it is a standalone static HTML site. A separate WordPress installation lives at `/gd-blog/` and handles the blog, service area pages, and the contact form (`/gd-blog/contact-us`).

---

## Business Info

| Field            | Value |
|------------------|-------|
| Business name    | GD Pro Web Designs / GDWebPros |
| Owner            | JA Armira |
| Phone            | (617) 771-0645 |
| Address          | Lawrence St., Everett, MA 02149 |
| Geo coordinates  | 42.40843, -71.053662 |
| Domain           | https://gdprowebdesigns.com |
| Founded          | 2005 |
| Hours            | Mon–Fri 9:00–18:00 |
| Price range      | $$ |

### Services Offered
- Custom web design (starting ~$1800)
- WordPress development / WooCommerce (starting ~$2500)
- Search Engine Optimization (local & national, starting ~$450/mo)
- Google Ads / PPC management
- Local internet marketing & digital marketing
- Social media integration
- Graphic design & branding
- WordPress maintenance & issue fixing
- SEO-safe WordPress migrations

### Credentials
- Google Digital Marketing & E-Commerce Certificate
- Google SEO Certificate

### Social Profiles
- Facebook: https://www.facebook.com/pages/GD-Pro-Web-Designs/113091575402539
- LinkedIn: https://www.linkedin.com/company/gd-pro-web-designs
- YouTube: http://www.youtube.com/user/silfovientoful

---

## Technology Stack

| Layer        | Technology |
|--------------|------------|
| Site type    | Static HTML (no front-end CMS) |
| CSS framework | Bootstrap 5.3 (CDN) on redesigned pages; Bootstrap 5.0.1/4 on legacy pages |
| Custom CSS   | `css/custom.css` (modern) · `css/style.css` (legacy) |
| Fonts (modern) | Inter + Poppins via Google Fonts |
| Fonts (legacy) | Josefin Sans, Gruppo, Poiret One, Quicksand via Google Fonts |
| Icons        | Font Awesome 6.5 (CDN) on new pages · Font Awesome 5 (local `node_modules/`) on legacy |
| JS           | jQuery 1.7.1, Bootstrap JS, Popper.js, Isotope, jCarousel, Fancybox, Modernizr, TouchSwipe |
| PHP          | PHP 8.0 (cPanel `ea-php80`), used for contact forms only |
| Server       | Apache with mod_rewrite (cPanel hosted) |
| SSL          | Forced HTTPS via `.htaccess` |
| Analytics    | Google Tag Manager `GTM-N4P95M5` · Google Analytics 4 `G-DB973M2MJX` |
| Blog/CMS     | WordPress at `/gd-blog/` (separate WP install) |
---

## Brand & Design System

### Color Palette
| Token           | Hex      | Use |
|-----------------|----------|-----|
| `--primary`     | `#044143` | Dark teal — headers, buttons, borders |
| `--primary-light`| `#2a605d`| Hover states |
| `--accent`      | `#FFBA00` | Gold yellow — CTA buttons, highlights |
| `--accent-dark` | `#e6a800` | Hover on gold |
| `--text-dark`   | `#1a1a2e` | Body text |
| `--text-muted`  | `#6c757d` | Secondary text |
| `--bg-light`    | `#F4F6FB` | Light section backgrounds |

### Typography
- Headings: **Poppins** (700–800 weight)
- Body: **Inter** (300–600 weight)

### Logo Files
- SVG: `img/tmp-imgs/newlogo-gray-yellow-shadow2020.svg` (used in nav)
- PNG: `img/tmp-imgs/gd-pro-web-designs-logo.png` (used in structured data)
- Full logo on Boston page: `img/tmp-imgs/Boston-web-designer-logo.png`

### Hero Image & Video
- `img/boston-freelance-website-designer.jpg` (also `.webp` version) — used as the `poster` fallback on the homepage hero while the video loads, and as the full-width header background on all interior pages
- `video/hero-bg.mp4` — autoplay, muted, loop background video for the homepage `#hero` section

**HTML structure** (`index.html` ~line 1030):
```html
<section id="hero">
  <div class="hero-video-wrap">
    <video autoplay muted loop playsinline
           poster="img/boston-freelance-website-designer.jpg"
           aria-hidden="true">
      <source src="video/hero-bg.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-overlay"></div>
  <div class="container">...</div>
</section>
```

**CSS classes** (all defined in `css/custom.css`):
- `.hero-video-wrap` — `position:absolute; inset:0` wrapper that stretches the video to fill the section
- `.hero-video-wrap video` — `object-fit:cover` so the video crops to fill without distortion
- `.hero-overlay` — dark teal gradient overlay (`rgba(4,65,67,.92) → .72`) sits above the video (z-index 1) so text is readable
- `#hero .container` — z-index 2, above the overlay

**`index.html` `<style>` block:** reduced to a single homepage-only override — `#hero { min-height: 90vh; }` — because `custom.css` defaults to `70vh` for interior pages. All other homepage styles are now in `custom.css`. Original full inline styles are archived in `index-css/index-styles.css`.

**Known fix applied:** the `poster` attribute was incorrectly set to `"video/hero-bg.mp4"` — corrected to `"img/boston-freelance-website-designer.jpg"` so the fallback image shows while the video loads.

**To swap the video:** drop a new `.mp4` file into `video/` and update `<source src="video/your-file.mp4">` in `index.html`. Keep the poster attribute pointing to the JPG.
Free stock sources: mixkit.co or pexels.com (search "boston", "web design", "digital").

### CSS Architecture (Two Generations)
1. **Modern** (`css/custom.css`): Used on redesigned pages (`index.html`, newer service/location pages). Bootstrap 5.3, Inter/Poppins, CSS custom properties, card components, `.btn-gold`, `.section-badge`, `.area-badge`.
2. **Legacy** (`css/style.css` / `css/style.min.css`): Used on older pages. Bootstrap 4/5.0.1, Josefin Sans, custom-built grid, `.focus-bg` header style.

### Global Link Color

`css/custom.css` (near the top, ~line 38) sets:
```css
a {
    color: var(--primary);
}
```
This overrides Bootstrap's default blue/underlined link style — it works with **no `!important`** because `custom.css` loads after Bootstrap's CDN stylesheet in `<head>`, so it already wins on source order at equal specificity, while still correctly losing to any more-specific selector (`.nav-link`, `.dropdown-item`, `.area-pill.featured`, `.btn-gold`, `.arrow-link`, etc.).

**Do not add `!important` to this rule.** Several nav/badge components (e.g. `#mainNav .dropdown-item`, `.area-pill.featured`) intentionally set white text with no `!important`, relying on normal specificity to win over the plain `a` rule. Adding `!important` here forces those back to dark teal text on a dark teal background — invisible.

### Utility Classes (Extracted Inline Styles)

These classes live in the `/* EXTRACTED INLINE STYLES */` block near the bottom of `css/custom.css`. Use them instead of `style=""` attributes:

| Class | Replaces |
|-------|---------|
| `.nav-lang` | Gold accent color + small font on the ES/EN language toggle link. The language icon is injected via `.nav-lang::before` CSS pseudo-element — do **not** add a `<i class="fas fa-language">` tag in the HTML or the icon will appear twice. |
| `.link-white` | `style="color:var(--white);text-decoration:none;"` on white anchor links |
| `.btn-gold-sm` | `style="font-size:.82rem;padding:.55rem 1.3rem;"` appended to `.btn-gold` |
| `.check-green` | `style="color:#28a745;margin-right:0.5rem;"` on checkmark icons |
| `.text-accent` | `style="color:var(--accent)"` — gold text |
| `.text-accent-dark` | `style="color:var(--accent-dark)"` — darker gold text (e.g. on `<i>` icons) |
| `.pill-teal` | Long `display:inline-flex` pill badge with teal border/bg |
| `.bg-dark-teal` | `style="background-color:#024a4d"` — dark teal section bg |
| `.list-circle` | `style="list-style:circle"` on `<ul>` |

**Script:** `scripts/fix_inline_styles.py` — scans all active `.html` pages and replaces these inline style patterns automatically. Run `python3 scripts/fix_inline_styles.py` from the site root if new pages are added or if inline styles reappear.

---

## File Structure

```
GD-2013/
├── index.html                    # EN homepage (modern redesign)
├── inicio.html                   # ES homepage (Spanish)
├── header.php                    # Shared PHP header template (legacy pages)
├── footer.php                    # Shared PHP footer template (legacy pages)
│
├── css/
│   ├── custom.css                # Modern design system styles
│   ├── style.css                 # Legacy full stylesheet
│   ├── style.min.css             # Minified legacy styles
│   ├── bootstrap.min.css         # Local Bootstrap copy (legacy)
│   ├── feedback.css              # Feedback tab widget styles
│   └── phone-protect.css         # Sticky Call Now bar + phone-num placeholder styles (loaded on every page)
│
├── js/
│   ├── custom.js                 # Site-specific JavaScript
│   ├── custom-OLD.js             # Archived old JS
│   ├── feedback.js               # Feedback tab widget
│   ├── phone-protect.js          # Decodes obfuscated tel: links + sticky call bar (vanilla JS, loaded on every page)
│   ├── jquery-1.7.1.min.js       # jQuery
│   ├── bootstrap.bundle.min.js
│   ├── popper.js
│   ├── modernizr.custom.js
│   ├── jquery.isotope.js         # Portfolio grid filtering
│   ├── jquery.jcarousel.js       # Carousel
│   ├── jquery.fancybox.js        # Lightbox
│   ├── jquery.cycle.all.js       # Slideshow
│   ├── jquery.gmap.js            # Google Maps
│   └── jquery.touchSwipe.js      # Mobile swipe
│
├── img/
│   ├── boston-freelance-website-designer.jpg   # Hero image
│   ├── boston-freelance-website-designer.webp  # WebP version
│   ├── tmp-imgs/                 # Logo files, UI icons, misc images
│   ├── portfolio/large/          # Portfolio screenshots (large)
│   ├── portfolio/thum/           # Portfolio thumbnails
│   ├── graphic-design/           # Graphic design samples
│   ├── web-design/               # Web design samples
│   ├── seo-services/             # SEO section images
│   ├── slideshow/                # Slideshow images
│   ├── parallax/                 # Parallax section images
│   └── other-web-services/       # Misc service images
│
├── video/
│   └── hero-bg.mp4               # Hero section background video
│
├── fonts/                        # Self-hosted fonts
├── font-awesome/                 # Font Awesome 5 (local copy)
│
├── php/
│   ├── config.php                # PHP config
│   ├── contact-new.php           # Contact form handler
│   ├── contact-new-captcha.php   # reCAPTCHA version
│   ├── contact-send.php          # Email send handler
│   ├── flickr.php                # Flickr API helper
│   └── tweets.php                # Twitter feed helper
│
├── contact-gd-website-design-estimates.php   # Contact page (requires WP)
├── contact-gd-website-design-estimate2.php   # Alternate contact page
├── contact-gcaptcha.php                      # reCAPTCHA handler
│
├── blog/                         # Static blog HTML files
├── archive/                      # Archived/off pages (do not publish)
├── digital-signage-page-gdweb-2013/          # Digital signage subpage
├── shopify/                      # Shopify-related content
├── web-design/                   # Web design section subfolder
├── web-development/              # Web development subfolder
├── index-css/
│   └── index-styles.css          # Archive of the original index.html <style> block (moved to custom.css)
├── scripts/
│   ├── fix_navs.py               # Standardizes #mainNav across all 55 pages — run after any nav change
│   ├── fix_inline_styles.py      # Replaces inline style="" attributes with CSS utility classes — run after any new inline style discovery
│   └── fix_phone_protection.py   # Obfuscates tel: links + injects sticky Call Now bar — run after any new page or if a raw tel:6177710645 link reappears
├── node_modules/                 # npm packages (Font Awesome, etc.)
│
├── .htaccess                     # Apache: redirects, caching, HTTPS, security
├── robots.txt                    # Crawler directives
├── sitemap.xml                   # XML sitemap
├── sitemap.html                  # HTML sitemap page
├── package.json                  # npm (sass compiler only)
├── favicon.ico                   # Site favicon
├── favicon.gif                   # Legacy favicon
├── BingSiteAuth.xml              # Bing Webmaster verification
├── google07be07f249ecb0f1.html   # Google Search Console verification
└── googleae58b8e4a5c2267d.html   # Google Search Console verification (alt)
```

---

## Pages Inventory

### Core Pages
| File | Purpose |
|------|---------|
| `index.html` | EN homepage — hero, services, process, portfolio highlights, testimonials, FAQ, CTAs |
| `inicio.html` | ES homepage (Spanish-language version) |
| `about-gd-freelance-web-designer-boston.html` | About page (EN) |
| `acerca-de-gd-pro-web-designs-boston.html` | About page (ES) |
| `web-design-FAQ.html` | Frequently Asked Questions |
| `blog.html` | Blog listing page |
| `sitemap.html` | HTML sitemap |
| `404.html` | Custom 404 error page |

### Service Pages (EN)
| File | Service |
|------|---------|
| `web-design-company-boston-ma.html` | Web design |
| `web-site-designs-Boston-MA.html` | Web design variant |
| `organic-search-engine-optimization-boston.html` | SEO (main) |
| `organic-SEO-everett-ma.html` | Local SEO Everett (canonical SEO page) |
| `local-seo-services-boston-ma.html` | Local SEO Boston |
| `PPC-adwords-advertising-boston.html` | Google Ads/PPC |
| `local-marketing-company-everett-malden-medford-revere-saugus-ma.html` | Local internet marketing |
| `digital-marketing-company-everett-malden-medford-revere-saugus-ma.html` | Digital marketing |
| `internet-marketing-services.html` | Internet marketing |
| `internet-marketing-local-marketing-everett-malden-medford-revere-saugus-ma.html` | Local marketing variant |
| `social-media-advertising.html` | Social media |
| `graphics-designer-logos-boston.html` | Graphic design & logos |
| `wordpress-developer-boston-ma.html` | WordPress development |
| `wordpress-maintenance-boston-ma.html` | WordPress maintenance |
| `fix-wordpress-issues-boston-ma.html` | WordPress troubleshooting |
| `freelance-web-designer-developer-boston-ma.html` | Freelance designer |
| `freelance-web-developer-boston-ma.html` | Freelance developer |
| `freelance-wordpress-website-designer-ma.html` | WordPress designer |
| `small-business-web-developer-web-designer-boston-ma.html` | Small business |
| `local-website-developer-near-me.html` | Near me targeting |
| `web-design-for-restaurants-boston-ma.html` | Restaurant design |
| `portfolio-website-design-development-boston-ma.html` | Web portfolio |
| `portfolio-graphics-design-boston-everett-ma.html` | Graphic design portfolio |

### Location / Service Area Pages (EN)
| File | City |
|------|------|
| `somerville-ma-web-designer.html` | Somerville |
| `medford-website-design-company-wordpress-developer.html` | Medford |
| `malden-web-designer-wordpress-developer.html` | Malden |
| `chelsea-web-design-company-wordpress-developer.html` | Chelsea |
| `newton-ma-web-designer-web-developer.html` | Newton |
| `quincy-ma-web-design-and-development.html` | Quincy |
| `lynn-ma-web-designer-web-developer.html` | Lynn |
| `Dedham-ma-freelance-web-developer.html` | Dedham |
| `Jamaica-Plain-wordpress-developer.html` | Jamaica Plain |
| `Lawrence-MA-freelance-web-designer-wordpress-developer.html` | Lawrence |
| `Waltham-MA-freelance-web-designer.html` | Waltham |
| `allston-freelance-web-designer-wordpress-developer.html` | Allston |
| `web-designer-winchester-ma.html` | Winchester |
| `website-designer-near-cambridge-ma.html` | Cambridge |
| `website-design-company-saugus-ma.html` | Saugus |
| `saugus-web-designer-wordpress-developer-seo.html` | Saugus (SEO) |
| `affordable-seo-services-malden-ma.html` | Malden SEO |
| `jamaica-plain-ma-local-seo-services.html` | Jamaica Plain SEO |
| `organic-seo-services-somerville.html` | Somerville SEO |
| `SEO-company-chelsea-ma.html` | Chelsea SEO |

### Spanish Service/Location Pages
| File | Purpose |
|------|---------|
| `disenador-paginas-web-freelancer-boston.html` | ES web designer Boston |
| `chelsea-ma-disenador-web-wordpress.html` | ES Chelsea |
| `lynn-ma-disenador-sitios-web-wordpress.html` | ES Lynn |
| `revere-ma-servicios-de-diseno-web-wordpress.html` | ES Revere |

### Redirect Stub Pages (301 targets in .htaccess, kept for legacy links)
- `boston-web-design-development-company.html` → `web-design-company-boston-ma.html`
- `seo-services-everett-ma.html` → `organic-SEO-everett-ma.html`
- `everett-ma-local-seo-services.html` → `organic-SEO-everett-ma.html`
- `web-design-Boston-MA.html` → `web-design-company-boston-ma.html`
- `responsive-web-design-development-boston-ma.html` → `web-design-company-boston-ma.html`
- `local-marketing-boston-...ma.html` → `local-marketing-company-...ma.html`
- `web-designer-developer-for-small-business-boston-ma.html` → `/gd-blog/web-developer-ma/`
- `web-dsigner-developer-for-small-business-boston-ma.html` → `/gd-blog/web-developer-ma/` (typo URL)
- `contact-gd-website-design-estimates.html` → contact page stub
- `contacts.html` → contact page stub
- `contact-thanks.html` → contact thank-you stub

### Deactivated Pages (orphaned, no live links, kept as `-off.html`)
- `boston-webdesign-for-non-profits-off.html` — formerly `boston-webdesign-for-non-profits.html` (Non-profit web design). The live filename was deleted with no `.htaccess` 301 added yet, so the old URL currently 404s instead of redirecting — add a redirect rule (matching the `disenador-paginas-web-freelancer-boston-off.html` pattern) if the old URL still has inbound links/backlinks.

---

## Navigation Structure

All 55 active pages share the same canonical `#mainNav` navbar. **`index.html` is the single source of truth** — do not change nav items on individual pages; run the fix script instead (see below).

### English Nav (all pages except `inicio.html`)

```
Home                          → /
Services ▾
  ├── Web Design              → web-design-company-boston-ma.html
  ├── Web Development         → /gd-blog/web-developer-ma/ (WP)
  ├── Graphic Design          → graphics-designer-logos-boston.html
  └── Digital Signage         → /gd-blog/digital-signage-solutions/ (WP)
Marketing ▾
  ├── SEO Everett, MA         → seo-services-everett-ma.html
  ├── Search Engine Optimization → organic-search-engine-optimization-boston.html
  ├── Google Ads Management   → PPC-adwords-advertising-boston.html
  ├── Local Internet Marketing → local-marketing-company-everett-malden-medford-revere-saugus-ma.html
  └── Social Media Integration → social-media-advertising.html
About ▾
  ├── About Us                → about-gd-freelance-web-designer-boston.html
  └── Service Area            → /gd-blog/service-area/ (WP)
Portfolio ▾
  ├── Design & Development    → portfolio-website-design-development-boston-ma.html
  └── Graphic Designs         → portfolio-graphics-design-boston-everett-ma.html
Contact                       → /gd-blog/contact-us (WP)
Free Consultation             → /gd-blog/contact-us (WP)  [nav-cta gold button]
ES                            → inicio.html               [language toggle]
```

### Spanish Nav (`inicio.html` only)

```
Inicio                        → /inicio.html
Servicios ▾
  ├── Diseño Web              → disenador-paginas-web-freelancer-boston.html
  ├── Desarrollo Web          → /gd-blog/web-developer-ma/ (WP)
  ├── Diseño Gráfico          → graphics-designer-logos-boston.html
  └── Señalización Digital    → /gd-blog/digital-signage-solutions/ (WP)
Marketing ▾
  ├── SEO Everett, MA         → seo-services-everett-ma.html
  ├── Optimización SEO        → organic-search-engine-optimization-boston.html
  ├── Google Ads              → PPC-adwords-advertising-boston.html
  ├── Marketing Local         → local-marketing-company-everett-malden-medford-revere-saugus-ma.html
  └── Redes Sociales          → social-media-advertising.html
Nosotros ▾
  ├── Acerca de Nosotros      → acerca-de-gd-pro-web-designs-boston.html
  └── Área de Servicio        → /gd-blog/service-area/ (WP)
Portafolio ▾
  ├── Diseño & Desarrollo     → portfolio-website-design-development-boston-ma.html
  └── Diseño Gráfico          → portfolio-graphics-design-boston-everett-ma.html
Contacto                      → /gd-blog/contact-us (WP)
Consulta Gratis               → /gd-blog/contact-us (WP)  [nav-cta gold button]
EN                            → index.html                [language toggle]
```

### `active-page` Class Rules

The `active-page` class is added to the top-level `<a>` of the active dropdown (or the Home link) based on page category:

| active-page on | Pages |
|----------------|-------|
| **Home** | `inicio.html` |
| **Services** | All web design, WordPress, graphic design, location, and Spanish service pages |
| **Marketing** | All SEO, PPC, local marketing, social media, digital marketing pages |
| **About** | `about-gd-freelance-web-designer-boston.html`, `acerca-de-gd-pro-web-designs-boston.html` |
| **Portfolio** | `portfolio-website-design-development-boston-ma.html`, `portfolio-graphics-design-boston-everett-ma.html` |
| *(none)* | `404.html`, `sitemap.html`, `blog.html` |

### Updating the Nav Across All Pages

If you ever need to change a nav item (add a link, rename, reorder), **do not edit individual HTML files**. Instead:
1. Update `index.html` nav as the reference
2. Edit `nav_en()` / `nav_es()` functions and the `ACTIVE` mapping in `scripts/fix_navs.py`
3. Run `python3 scripts/fix_navs.py` from the site root — it replaces the `<nav id="mainNav">` block on all 55 pages in one pass

Both `fix_navs.py` and `fix_inline_styles.py` derive the site root from their own file location (`os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`) rather than a hardcoded path, so they run correctly regardless of where the project folder lives on disk (e.g. after the iCloud Drive move).

**Language toggle icon:** The ES/EN toggle renders its language icon via the `.nav-lang::before` CSS pseudo-element in `custom.css` (needed for WP nav menus where `<i>` tags can't be added). The HTML nav template uses plain text only — `ES` / `EN` — with no `<i>` tag. Adding an `<i class="fas fa-language">` tag alongside `.nav-lang` will cause the icon to appear twice.

**Pages intentionally skipped by the script** (redirect stubs with no real content):
`boston-web-design-development-company.html`, `contact-*.html`, `contacts.html`, `everett-ma-local-seo-services.html`, `google*.html`, `local-marketing-boston-...html`, `responsive-web-design-*.html`, `web-design-Boston-MA.html`, `web-d*signer-developer-for-small-business-*.html`, `seo-services-everett-ma.html`

---

## Phone Number Protection & Sticky Call Bar

The `tel:6177710645` link used to appear as raw, plain-text HTML on every page (hero section, footer "About" blurb, footer contact row). Because it's the exact same static string on ~70 public pages, it was trivial for phone-harvesting scrapers to crawl and add to robocall/spam-call lists — this is the #1 cause of the daily spam calls to (617) 771-0645.

**How it's fixed:** every live page now loads `css/phone-protect.css` and `js/phone-protect.js` (vanilla JS, no jQuery dependency, so it works on both modern and legacy pages). Instead of a plain `<a href="tel:6177710645">(617) 771-0645</a>`, the HTML source contains:

```html
<a href="#" data-tel="5460177716" aria-label="Call GD Pro Web Designs">
  <span class="phone-num"></span>
</a>
```

`data-tel` holds the digits **reversed** (`5460177716`), and the visible `<span class="phone-num">` is empty in the source. On `DOMContentLoaded`, `phone-protect.js` reverses the digits back, sets the real `href="tel:6177710645"`, and fills in the formatted number — so real visitors on any JS-enabled browser see and can tap/click the number exactly as before, but the raw digits never appear anywhere in the page's static HTML source. This defeats the simple regex/HTML-scraping bots that harvest `tel:` links at scale (the common source of robocall lists) without needing a CAPTCHA or hiding the number from real users.

Any label text in the same anchor (e.g. `Llámenos al `, `Tel: `) is preserved outside the `<span>` — only the digit run itself is replaced.

**GA4 click tracking:** `phone-protect.js` also attaches a `click` listener to every obfuscated phone anchor that pushes a `phone_click` event to `window.dataLayer` (`{ event: 'phone_click', phone_number, click_location: 'sticky_bar' | 'page_content', page_path }`). This feeds the `click_to_call` GA4 Key Event — see the GA4 event tracking status memory for current setup state.

**Left untouched on purpose:**
- The `"telephone"` field in the homepage's `ProfessionalService` JSON-LD — required for Local SEO / Google Business Profile NAP matching.
- Phone mentions inside `<meta name="description">` tags — these show up in the Google search snippet and are a legitimate, deliberate CTR driver, not a scraping vector at the same scale as a repeated visible `tel:` link.

**Trade-off:** the number is invisible to non-JS clients (very rare in practice; the site already depends on JS for GTM, nav, Bootstrap, etc.). There is intentionally no `<noscript>` fallback, because a `<noscript>` block still contains the raw digits in the static HTML source and would defeat the whole point.

**Sticky Call Bar:** a fixed-to-bottom bar (`#stickyCallBar`, gold `.sticky-call-btn` with a pulse animation) is injected before `</body>` on every page. It's hidden at the top of the page and fades in once the visitor scrolls down more than 400px (`phone-protect.js`), giving persistent access to a "Call Now" button — the nav bar itself has no phone number. It reuses the same `data-tel` obfuscation pattern.

**Script:** `scripts/fix_phone_protection.py` — rewrites every `<a href="tel:6177710645">` anchor site-wide into the obfuscated pattern above, and injects the `phone-protect.css`/`.js` includes plus the sticky bar markup before `</head>`/`</body>`. It's idempotent (safe to re-run) and skips `archive/`, `node_modules/`, and the Google Search Console verification stub pages. Run `python3 scripts/fix_phone_protection.py` from the site root whenever a new page is added or a raw `tel:6177710645` link reappears (e.g. pasted in from an old template).

---

## SEO Architecture

### Structured Data (JSON-LD) on Homepage
- `ProfessionalService` — business entity with address, geo, hours, services, credentials
- `WebSite` — site entity
- `WebPage` — page entity
- `Person` — JA Armira, freelance web designer
- `FAQPage` — 5 FAQ entries about services/pricing

### Geo Targeting
- Region: US-MA
- City: Everett, MA
- Coordinates: 42.40843, -71.053662
- Service area: All of Massachusetts, focus on Greater Boston metro

### Bilingual SEO
- English primary site at root (`/`)
- Spanish pages at root level with ES slugs (`inicio.html`, `disenador-*`, etc.)
- No hreflang tags — Spanish pages are standalone geo+language targeted pages

### Canonical URLs
- Every page has `<link rel="canonical" href="https://gdprowebdesigns.com/[page]">`
- Homepage canonical: `https://gdprowebdesigns.com/`
- All internal links use relative paths

### .htaccess Redirects (key 301s)
```
web-design-Boston-MA.html               → web-design-company-boston-ma.html
boston-web-design-development-company.html → web-design-company-boston-ma.html
seo-services-everett-ma.html            → organic-SEO-everett-ma.html
everett-ma-local-seo-services.html      → organic-SEO-everett-ma.html
web-designer-developer-for-small-business... → gd-blog/web-developer-ma/
web-dsigner-developer-for-small-...     → gd-blog/web-developer-ma/
disenador-paginas-web-freelancer-boston-off.html → disenador-paginas-web-freelancer-boston.html
```

### Sitemap
- XML: `sitemap.xml` (submit to Google Search Console and Bing)
- HTML: `sitemap.html`
- robots.txt: `sitemap: https://gdprowebdesigns.com/sitemap.xml`

---

## Analytics & Tracking

| Platform | ID |
|----------|----|
| Google Tag Manager | GTM-N4P95M5 |
| Google Analytics 4 | G-DB973M2MJX |
| Bing Webmaster | `BingSiteAuth.xml` |
| Google Search Console | `google07be07f249ecb0f1.html`, `googleae58b8e4a5c2267d.html` |
| Additional verif. | `9656e5e29fbd4b538dd418416d901095.txt`, `ddddf5f0a8af401294cab79969cb0aaf.txt` |

GTM and GA4 tag snippet appears in the `<head>` of every page. GTM noscript iframe is in `<body>` immediately after `<body>` opening tag.

---

## Contact Form

Contact routes through WordPress, NOT through the static PHP files:
- **Active contact URL**: `/gd-blog/contact-us` (WordPress page)
- `contact-gd-website-design-estimates.php` — legacy PHP contact page (includes WP via `require_once('./gd-blog/wp-blog-header.php')`, currently set to noindex/nofollow)
- `php/contact-send.php` — legacy standalone mailer (no longer primary)
- reCAPTCHA keys stored in `recaptcha-keys/` directory

---

## WordPress Integration (`gd-blog/`)

A separate WordPress installation lives at `/gd-blog/`. The static site links to several WP URLs:
- `/gd-blog/contact-us` — contact form
- `/gd-blog/gd-news/` — news/blog
- `/gd-blog/service-area/` — service area directory
- `/gd-blog/web-developer-ma/` — web developer page

The static HTML `.htaccess` includes the WordPress mod_rewrite block so WP can function at its subpath.

---

## Hosting & Server

- **Host**: cPanel shared hosting
- **PHP**: 8.0 (`ea-php80`)
- **Server**: Apache with mod_rewrite enabled
- **SSL**: Forced via `.htaccess` (`RewriteCond %{HTTPS} off → https://`)
- **Caching**: Browser caching set via `mod_expires` (images: 1 year, CSS/JS: 1 month)
- **Security**: `Options -Indexes` (no directory listing), Russian referrer spam blocked in `.htaccess`
- **Error pages**: Custom `404.html`

---

## Key Conventions When Editing Pages

1. **Every page must have**: `<meta charset>`, `<meta viewport>`, `<title>`, `<meta description>`, `<link rel="canonical">`, geo meta tags, GTM snippet, GA4 snippet.
2. **Structured data**: Use JSON-LD `<script type="application/ld+json">` in `<head>`. At minimum include `WebPage` type on interior pages.
3. **Navbar**: Never edit nav links on individual pages. `index.html` is the canonical source. To change any nav item, update `index.html` and re-run the fix script (see Navigation Structure section above).
4. **Contact links**: Always use `/gd-blog/contact-us` or `/gd-blog/contact-us/` — never link to the old `.php` or `.html` contact stubs.
5. **Blog/News links**: Always use `/gd-blog/gd-news/` — the `blog.html` file is a legacy page.
6. **CSS**: New/redesigned pages use `css/custom.css` + Bootstrap 5.3 CDN. Do not add `style.css` to redesigned pages.
7. **Fonts on new pages**: Load Inter + Poppins from Google Fonts. Do not add the legacy Josefin Sans stack.
8. **Bootstrap version**: New pages use Bootstrap 5.3.2 CDN. Legacy pages use 5.0.1 CDN. Do not mix versions on the same page.
9. **Archive folder**: Pages in `archive/` are NOT live. Do not link to them or republish them without review.
10. **Spanish pages**: `inicio.html` has its own fully Spanish nav (see Navigation Structure above). Other Spanish pages (disenador-*, chelsea-ma-disenador-*, etc.) use the standard English nav with the ES toggle.
11. **No inline styles**: Use the utility classes in `css/custom.css` instead of `style=""` attributes. If a new repeated style pattern is needed, add it as a class to `custom.css` and run `scripts/fix_inline_styles.py` to apply it site-wide.
12. **301 redirects**: Any URL change must be accompanied by a `.htaccess` 301 redirect entry from old slug to new slug.
13. **Phone number**: Never write a raw `<a href="tel:6177710645">(617) 771-0645</a>`. Use the obfuscated pattern from the Phone Number Protection section above, or just run `scripts/fix_phone_protection.py` after pasting in a new page — it will fix any raw tel: links automatically.

---

## Recreating the Site from Scratch

To fully recreate this site:

1. **Domain & hosting**: Register `gdprowebdesigns.com`, set up cPanel hosting with Apache + PHP 8.0, enable mod_rewrite.
2. **SSL**: Enable Let's Encrypt or cPanel SSL; the `.htaccess` handles forced redirect.
3. **Upload all files**: Copy the full directory. All assets are self-contained — no build step required for the static HTML pages.
4. **WordPress**: Install WordPress at `/gd-blog/`. Restore the WP database. Re-create the contact page at slug `contact-us`, news at `gd-news/`, service area at `service-area/`.
5. **Analytics**: Re-register GTM (`GTM-N4P95M5`) and GA4 (`G-DB973M2MJX`) — or create new accounts and update the IDs in every page `<head>`.
6. **Search Console**: Re-verify ownership using the verification HTML files already present in the repo.
7. **Bing Webmaster**: Re-verify via `BingSiteAuth.xml`.
8. **Contact form**: reCAPTCHA keys in `recaptcha-keys/` need to be registered for the new domain if domain changes.
9. **Sitemap**: Submit `https://gdprowebdesigns.com/sitemap.xml` to Google Search Console and Bing Webmaster after going live.
