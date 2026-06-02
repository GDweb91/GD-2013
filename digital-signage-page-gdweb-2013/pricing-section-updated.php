<?php 
/**
 * Template part: Pricing section
 */
 ?>
<!-- ══════════════════════════════════════════
   PRICING  (reuses #pricing / .price-card exactly)
══════════════════════════════════════════ -->
<section id="pricing">
  <div class="container">
    <div class="row mb-5 justify-content-center text-center">
      <div class="col-lg-7">
        <span class="section-badge">Transparent Pricing</span>
        <h2 class="section-title centered">Simple Packages. <span>No Hidden Fees.</span></h2>
        <div class="title-bar centered"></div>
        <p class="section-sub mx-auto">One-time setup covers hardware, design, and installation. Monthly plans cover content updates and support. All prices are starting rates — contact us for a custom quote.</p>
      </div>
    </div>
    <div class="row g-4 justify-content-center align-items-stretch">

      <!-- ── Starter ── -->
      <div class="col-md-6 col-lg-4">
        <div class="price-card h-100">
          <div class="price-icon"><i class="fa fa-tv"></i></div>
          <h4>Single Screen Starter</h4>
          <p>Perfect for cafés, food trucks, and small restaurants needing a clean, static menu display.</p>
          <div class="price-from">One-time setup fee</div>
          <div class="price-amount">$1,299</div>
          <ul class="price-list">
            <li><i class="fa fa-check"></i> Raspberry Pi 4 hardware included</li>
            <li><i class="fa fa-check"></i> 1 custom static menu board design</li>
            <li><i class="fa fa-check"></i> 1 promotions / specials slide</li>
            <li><i class="fa fa-check"></i> Subtle animations (e.g. slide transitions)</li>
            <li><i class="fa fa-check"></i> On-site software setup (Boston area)*</li>
            <li><i class="fa fa-check"></i> Content scheduling setup</li>
            <li><i class="fa fa-check"></i> 30-day support included</li>
          </ul>
          <a href="<?php echo home_url('/gd-blog/contact-us'); ?>" class="btn-outline-teal w-100 text-center">Get a Quote</a>
          <p class="price-note">+ Monthly management from $99/mo</p>
          <p class="price-note">* TV + physical installation charged separately</p>
        </div>
      </div>

      <!-- ── Restaurant Pro (Featured) ── -->
      <div class="col-md-6 col-lg-4">
        <div class="price-card featured h-100">
          <div class="price-icon"><i class="fa fa-star"></i></div>
          <h4>Restaurant Pro</h4>
          <p>Full animated signage system for full-service restaurants, bars, and multi-room venues.</p>
          <div class="price-from">One-time setup fee</div>
          <div class="price-amount">$2,199</div>
          <ul class="price-list">
            <li><i class="fa fa-check"></i> Raspberry Pi 4 hardware included</li>
            <li><i class="fa fa-check"></i> 3 custom menu board designs</li>
            <li><i class="fa fa-check"></i> Up to 3 animated promotional slides</li>
            <li><i class="fa fa-check"></i> Motion graphics &amp; subtle animations</li>
            <li><i class="fa fa-check"></i> Time-based scheduling (breakfast/lunch/dinner)</li>
            <li><i class="fa fa-check"></i> On-site software setup (Boston area)*</li>
            <li><i class="fa fa-check"></i> 3 months management included</li>
            <li><i class="fa fa-check"></i> Staff training walkthrough</li>
          </ul>
          <a href="<?php echo home_url('/gd-blog/contact-us'); ?>" class="btn-gold w-100 text-center">Get a Quote</a>
          <p class="price-note" style="color:rgba(255,255,255,.45);">+ Management from $149/mo after 3 months</p>
          <p class="price-note" style="color:rgba(255,255,255,.45);">* TV + physical installation charged separately</p>
        </div>
      </div>

       <!-- ── Monthly Management ── -->
      <div class="col-md-6 col-lg-4">
        <div class="price-card h-100">
          <div class="price-icon"><i class="fa fa-rotate"></i></div>
          <h4>Monthly Management</h4>
          <p>Already installed? Keep your content fresh with our ongoing update and support plan.</p>
          <div class="price-from">Monthly — no contract</div>
          <div class="price-amount">$199<span style="font-size:1rem;font-weight:400;color:var(--text-muted);">/mo</span></div>
          <ul class="price-list">
            <li><i class="fa fa-check"></i> Weekly content updates</li>
            <li><i class="fa fa-check"></i> New specials &amp; promos every week</li>
            <li><i class="fa fa-check"></i> Remote updates — no visit needed</li>
            <li><i class="fa fa-check"></i> Up to 3 seasonal menu redesigns/yr</li>
            <li><i class="fa fa-check"></i> Priority phone &amp; text support</li>
            <li><i class="fa fa-check"></i> Software / CMS platform fee included</li>
            <li><i class="fa fa-check"></i> Annual hardware check-up</li>
          </ul>
          <a href="<?php echo home_url('/gd-blog/contact-us'); ?>" class="btn-outline-teal w-100 text-center">Get a Quote</a>
          <p class="price-note">Cancel anytime — 30-day notice required</p>
          <p class="price-note">Equivalent to ~$50/hr — well below Boston agency rates of $75–$150/hr</p>
        </div>
      </div>

    </div>

    <!-- Add-ons row -->
    <div class="row justify-content-center mt-4">
      <div class="col-lg-10">
        <div class="ds-addons-bar">
          <span class="ds-addons-label">Available Add-ons:</span>
          <span class="ds-addon-chip"><i class="fa fa-film"></i> Full Cinematic Animation — from $1,500</span>
          <span class="ds-addon-chip"><i class="fa fa-plus"></i> Extra Screen Zone — from $300</span>
          <span class="ds-addon-chip"><i class="fa fa-screwdriver-wrench"></i> Physical TV Installation — quote on request</span>
          <span class="ds-addon-chip"><i class="fa fa-shield"></i> Annual Service Contract — $150–$300/yr</span>
        </div>
      </div>
    </div>

    <p class="text-center mt-3" style="font-size:.82rem;color:var(--text-muted);">
      * Prices are starting rates. Final pricing varies by screen count, animation complexity, restaurant size, and location. TV not included.
      <a href="<?php echo home_url('/gd-blog/contact-us'); ?>" style="color:var(--primary-light);font-weight:600;">Contact us for a custom quote.</a>
    </p>
  </div>
</section>
