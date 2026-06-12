import os, re

SITE = '/Users/gdwebpros/Sites/GD-2013'

SKIP = {
    'index.html',  # canonical source — don't touch
    'boston-web-design-development-company.html',
    'contact-gd-website-design-estimates.html',
    'contact-thanks.html',
    'contacts.html',
    'everett-ma-local-seo-services.html',
    'google07be07f249ecb0f1.html',
    'googleae58b8e4a5c2267d.html',
    'local-marketing-boston-everett-malden-medford-revere-saugus-ma.html',
    'responsive-web-design-development-boston-ma.html',
    'web-design-Boston-MA.html',
    'web-designer-developer-for-small-business-boston-ma.html',
    'web-dsigner-developer-for-small-business-boston-ma.html',
    'seo-services-everett-ma.html',  # redirect stub → organic-SEO-everett-ma.html
}

# Which nav section gets active-page per page
ACTIVE = {
    # home
    'inicio.html': 'home',
    # services
    'web-design-company-boston-ma.html': 'services',
    'graphics-designer-logos-boston.html': 'services',
    'freelance-web-designer-developer-boston-ma.html': 'services',
    'freelance-web-developer-boston-ma.html': 'services',
    'freelance-wordpress-website-designer-ma.html': 'services',
    'web-design-for-restaurants-boston-ma.html': 'services',
    'boston-webdesign-for-non-profits.html': 'services',
    'fix-wordpress-issues-boston-ma.html': 'services',
    'wordpress-developer-boston-ma.html': 'services',
    'wordpress-maintenance-boston-ma.html': 'services',
    'web-design-FAQ.html': 'services',
    'web-site-designs-Boston-MA.html': 'services',
    'small-business-web-developer-web-designer-boston-ma.html': 'services',
    'local-website-developer-near-me.html': 'services',
    # location / service-area pages
    'somerville-ma-web-designer.html': 'services',
    'medford-website-design-company-wordpress-developer.html': 'services',
    'malden-web-designer-wordpress-developer.html': 'services',
    'chelsea-web-design-company-wordpress-developer.html': 'services',
    'newton-ma-web-designer-web-developer.html': 'services',
    'quincy-ma-web-design-and-development.html': 'services',
    'lynn-ma-web-designer-web-developer.html': 'services',
    'Dedham-ma-freelance-web-developer.html': 'services',
    'Jamaica-Plain-wordpress-developer.html': 'services',
    'Lawrence-MA-freelance-web-designer-wordpress-developer.html': 'services',
    'Waltham-MA-freelance-web-designer.html': 'services',
    'allston-freelance-web-designer-wordpress-developer.html': 'services',
    'web-designer-winchester-ma.html': 'services',
    'website-designer-near-cambridge-ma.html': 'services',
    'website-design-company-saugus-ma.html': 'services',
    'saugus-web-designer-wordpress-developer-seo.html': 'services',
    # spanish service pages
    'disenador-paginas-web-freelancer-boston.html': 'services',
    'chelsea-ma-disenador-web-wordpress.html': 'services',
    'lynn-ma-disenador-sitios-web-wordpress.html': 'services',
    'revere-ma-servicios-de-diseno-web-wordpress.html': 'services',
    # marketing
    'organic-search-engine-optimization-boston.html': 'marketing',
    'organic-SEO-everett-ma.html': 'marketing',
    'organic-seo-services-somerville.html': 'marketing',
    'local-seo-services-boston-ma.html': 'marketing',
    'affordable-seo-services-malden-ma.html': 'marketing',
    'SEO-company-chelsea-ma.html': 'marketing',
    'jamaica-plain-ma-local-seo-services.html': 'marketing',
    'PPC-adwords-advertising-boston.html': 'marketing',
    'social-media-advertising.html': 'marketing',
    'local-marketing-company-everett-malden-medford-revere-saugus-ma.html': 'marketing',
    'digital-marketing-company-everett-malden-medford-revere-saugus-ma.html': 'marketing',
    'internet-marketing-services.html': 'marketing',
    'internet-marketing-local-marketing-everett-malden-medford-revere-saugus-ma.html': 'marketing',
    # about
    'about-gd-freelance-web-designer-boston.html': 'about',
    'acerca-de-gd-pro-web-designs-boston.html': 'about',
    # portfolio
    'portfolio-website-design-development-boston-ma.html': 'portfolio',
    'portfolio-graphics-design-boston-everett-ma.html': 'portfolio',
}

def cls(section, target):
    base = 'nav-link'
    if target == 'dropdown':
        base += ' dropdown-toggle'
    if section == target or (target == 'services_dd' and section == 'services') \
       or (target == 'marketing_dd' and section == 'marketing') \
       or (target == 'about_dd' and section == 'about') \
       or (target == 'portfolio_dd' and section == 'portfolio'):
        base += ' active-page'
    return base

def nav_en(section):
    h  = ' active-page' if section == 'home'      else ''
    s  = ' active-page' if section == 'services'  else ''
    m  = ' active-page' if section == 'marketing' else ''
    ab = ' active-page' if section == 'about'     else ''
    p  = ' active-page' if section == 'portfolio' else ''
    return f'''\
<nav class="navbar navbar-expand-lg" id="mainNav" aria-label="Main navigation">
  <div class="container">
    <a class="navbar-brand" href="index.html">
      <img src="img/gd-pro-web-designs-logo.svg" alt="GD Pro Web Designs">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain" aria-controls="navMain" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navMain">
      <ul class="navbar-nav ms-auto align-items-lg-center">

        <li class="nav-item">
          <a class="nav-link{h}" href="/">Home</a>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle{s}" href="web-design-company-boston-ma.html" id="ddServices" role="button" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
          <ul class="dropdown-menu" aria-labelledby="ddServices">
            <li><a class="dropdown-item" href="web-design-company-boston-ma.html">Web Design</a></li>
            <li><a class="dropdown-item" href="/gd-blog/web-developer-ma/">Web Development</a></li>
            <li><a class="dropdown-item" href="graphics-designer-logos-boston.html">Graphic Design</a></li>
            <li><a class="dropdown-item" href="/gd-blog/digital-signage-solutions/">Digital Signage</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle{m}" href="#" id="ddMarketing" role="button" data-bs-toggle="dropdown" aria-expanded="false">Marketing</a>
          <ul class="dropdown-menu" aria-labelledby="ddMarketing">
            <li><a class="dropdown-item" href="organic-SEO-everett-ma.html">SEO Everett, MA</a></li>
            <li><a class="dropdown-item" href="organic-search-engine-optimization-boston.html">Search Engine Optimization</a></li>
            <li><a class="dropdown-item" href="PPC-adwords-advertising-boston.html">Google Ads Management</a></li>
            <li><a class="dropdown-item" href="local-marketing-company-everett-malden-medford-revere-saugus-ma.html">Local Internet Marketing</a></li>
            <li><a class="dropdown-item" href="social-media-advertising.html">Social Media Integration</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle{ab}" href="about-gd-freelance-web-designer-boston.html" id="ddAbout" role="button" data-bs-toggle="dropdown" aria-expanded="false">About</a>
          <ul class="dropdown-menu" aria-labelledby="ddAbout">
            <li><a class="dropdown-item" href="about-gd-freelance-web-designer-boston.html">About Us</a></li>
            <li><a class="dropdown-item" href="/gd-blog/service-area/">Service Area</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle{p}" href="portfolio-website-design-development-boston-ma.html" id="ddPortfolio" role="button" data-bs-toggle="dropdown" aria-expanded="false">Portfolio</a>
          <ul class="dropdown-menu" aria-labelledby="ddPortfolio">
            <li><a class="dropdown-item" href="portfolio-website-design-development-boston-ma.html">Design &amp; Development</a></li>
            <li><a class="dropdown-item" href="portfolio-graphics-design-boston-everett-ma.html">Graphic Designs</a></li>
          </ul>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="/gd-blog/contact-us">Contact</a>
        </li>

        <li class="nav-item">
          <a class="nav-link nav-cta" href="/gd-blog/contact-us">Free Consultation</a>
        </li>

        <li class="nav-item ms-lg-1">
          <a class="nav-link nav-lang" href="inicio.html" title="Versión en Español">ES</a>
        </li>

      </ul>
    </div>
  </div>
</nav>'''

def nav_es():
    return '''\
<nav class="navbar navbar-expand-lg" id="mainNav" aria-label="Main navigation">
  <div class="container">
    <a class="navbar-brand" href="inicio.html">
      <img src="img/gd-pro-web-designs-logo.svg" alt="GD Pro Web Designs">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain" aria-controls="navMain" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navMain">
      <ul class="navbar-nav ms-auto align-items-lg-center">

        <li class="nav-item">
          <a class="nav-link active-page" href="/inicio.html">Inicio</a>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="disenador-paginas-web-freelancer-boston.html" id="ddServices" role="button" data-bs-toggle="dropdown" aria-expanded="false">Servicios</a>
          <ul class="dropdown-menu" aria-labelledby="ddServices">
            <li><a class="dropdown-item" href="disenador-paginas-web-freelancer-boston.html">Diseño Web</a></li>
            <li><a class="dropdown-item" href="/gd-blog/web-developer-ma/">Desarrollo Web</a></li>
            <li><a class="dropdown-item" href="graphics-designer-logos-boston.html">Diseño Gráfico</a></li>
            <li><a class="dropdown-item" href="/gd-blog/digital-signage-solutions/">Señalización Digital</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="ddMarketing" role="button" data-bs-toggle="dropdown" aria-expanded="false">Marketing</a>
          <ul class="dropdown-menu" aria-labelledby="ddMarketing">
            <li><a class="dropdown-item" href="organic-SEO-everett-ma.html">SEO Everett, MA</a></li>
            <li><a class="dropdown-item" href="organic-search-engine-optimization-boston.html">Optimización SEO</a></li>
            <li><a class="dropdown-item" href="PPC-adwords-advertising-boston.html">Google Ads</a></li>
            <li><a class="dropdown-item" href="local-marketing-company-everett-malden-medford-revere-saugus-ma.html">Marketing Local</a></li>
            <li><a class="dropdown-item" href="social-media-advertising.html">Redes Sociales</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="acerca-de-gd-pro-web-designs-boston.html" id="ddAbout" role="button" data-bs-toggle="dropdown" aria-expanded="false">Nosotros</a>
          <ul class="dropdown-menu" aria-labelledby="ddAbout">
            <li><a class="dropdown-item" href="acerca-de-gd-pro-web-designs-boston.html">Acerca de Nosotros</a></li>
            <li><a class="dropdown-item" href="/gd-blog/service-area/">Área de Servicio</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="portfolio-website-design-development-boston-ma.html" id="ddPortfolio" role="button" data-bs-toggle="dropdown" aria-expanded="false">Portafolio</a>
          <ul class="dropdown-menu" aria-labelledby="ddPortfolio">
            <li><a class="dropdown-item" href="portfolio-website-design-development-boston-ma.html">Diseño &amp; Desarrollo</a></li>
            <li><a class="dropdown-item" href="portfolio-graphics-design-boston-everett-ma.html">Diseño Gráfico</a></li>
          </ul>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="/gd-blog/contact-us">Contacto</a>
        </li>

        <li class="nav-item">
          <a class="nav-link nav-cta" href="/gd-blog/contact-us">Consulta Gratis</a>
        </li>

        <li class="nav-item ms-lg-1">
          <a class="nav-link nav-lang" href="index.html" title="English Version">EN</a>
        </li>

      </ul>
    </div>
  </div>
</nav>'''

pat = re.compile(r'<nav\b[^>]*\bid="mainNav"[^>]*>.*?</nav>', re.DOTALL)

updated, unchanged, skipped, no_nav = [], [], [], []

for fname in sorted(os.listdir(SITE)):
    if not fname.endswith('.html'):
        continue
    if fname in SKIP:
        skipped.append(fname)
        continue

    fpath = os.path.join(SITE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="mainNav"' not in content:
        no_nav.append(fname)
        continue

    if fname == 'inicio.html':
        new_nav = nav_es()
    else:
        new_nav = nav_en(ACTIVE.get(fname))

    new_content = pat.sub(new_nav, content)

    if new_content == content:
        unchanged.append(fname)
    else:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(fname)

print(f"UPDATED ({len(updated)}):")
for f in updated: print(f"  ✓ {f}")
print(f"\nUNCHANGED ({len(unchanged)}):")
for f in unchanged: print(f"  - {f}")
print(f"\nSKIPPED stubs ({len(skipped)}): {', '.join(skipped)}")
print(f"NO mainNav ({len(no_nav)}): {', '.join(no_nav)}")
