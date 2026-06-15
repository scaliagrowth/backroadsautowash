#!/usr/bin/env python3
"""Build static HTML pages for Back Roads Auto Wash."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, 'public')

def head(title, desc, path):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="https://backroadsautowash.com{path}" />
<meta name="theme-color" content="#0A0A0A" />
<meta name="author" content="Back Roads Auto Wash LLC" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Back Roads Auto Wash" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="https://backroadsautowash.com{path}" />
<meta property="og:image" content="https://backroadsautowash.com/images/hero-detail.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="https://backroadsautowash.com/images/hero-detail.jpg" />
<link rel="icon" type="image/png" href="/images/logo.png" />
<link rel="apple-touch-icon" href="/images/logo.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&family=Poppins:wght@300;500;600;700;800;900&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/css/site.css" />
'''

JSONLD_LOCAL = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"AutoDetailing","name":"Back Roads Auto Wash","image":"https://backroadsautowash.com/images/logo.png","url":"https://backroadsautowash.com/","telephone":"+1-208-317-9786","email":"backroadsautowash@gmail.com","priceRange":"$$","address":{"@type":"PostalAddress","addressLocality":"McCammon","addressRegion":"ID","addressCountry":"US"},"areaServed":[{"@type":"City","name":"McCammon, ID"},{"@type":"City","name":"Lava Hot Springs, ID"},{"@type":"City","name":"Arimo, ID"},{"@type":"City","name":"Downey, ID"},{"@type":"City","name":"Robin, ID"},{"@type":"City","name":"Inkom, ID"},{"@type":"City","name":"Pocatello, ID"}],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"19:00"}],"sameAs":["https://www.facebook.com/profile.php?id=61588172679083","https://www.instagram.com/backroadsautowash"]}
</script>'''

# Nav links — everything is a hash anchor on home except About
NAV_LINKS = [
    ('/#services', 'Services', 'services'),
    ('/#reviews', 'Reviews', 'reviews'),
    ('/about', 'About', 'about'),
    ('/#faq', 'FAQ', 'faq'),
    ('/#book', 'Contact', 'book'),
]

def nav(active):
    lis = ''.join(
        f'      <a href="{href}"{" class=\"active\"" if key==active else ""}>{label}</a>\n'
        for href, label, key in NAV_LINKS
    )
    return f'''<div class="announce" role="region" aria-label="Limited time offer">
  <span>🧼 LIMITED TIME: Book an Interior Deep Detail and get ALL Car Seat Cleaning 50% OFF — Offer ends June 17, 2026</span>
  <a href="/#book">Book Now →</a>
</div>
<header class="nav-wrap">
  <div class="container nav">
    <a href="/" aria-label="Back Roads Auto Wash home">
      <img src="/images/logo.png" alt="Back Roads Auto Wash logo" class="logo" width="220" height="54" />
    </a>
    <nav class="nav-links" id="navLinks" aria-label="Primary">
{lis}    </nav>
    <div class="nav-cta">
      <a href="/#book" class="btn btn-gold">Book Now</a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>
'''

FOOTER = '''<footer>
  <div class="container foot">
    <div>
      <a href="/"><img src="/images/logo.png" alt="Back Roads Auto Wash logo" width="200" height="46" /></a>
    </div>
    <div class="foot-links">
      <a href="/#services">Services</a>
      <a href="/#reviews">Reviews</a>
      <a href="/about">About</a>
      <a href="/#faq">FAQ</a>
      <a href="/#book">Contact</a>
    </div>
    <div class="foot-contact">
      <a href="tel:2083179786">📞 208-317-9786</a>
      <a href="mailto:backroadsautowash@gmail.com">✉️ backroadsautowash@gmail.com</a>
      <div class="socials">
        <a href="https://www.instagram.com/backroadsautowash" target="_blank" rel="noopener" aria-label="Instagram">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>
        </a>
        <a href="https://www.facebook.com/profile.php?id=61588172679083" target="_blank" rel="noopener" aria-label="Facebook">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M13 22v-8h3l1-4h-4V7.5c0-1.2.3-2 2-2h2V2.1C16.6 2 15.4 2 14.2 2 11.5 2 10 3.7 10 6.9V10H7v4h3v8h3z"/></svg>
        </a>
      </div>
    </div>
  </div>
  <div class="copy">© 2026 Back Roads Auto Wash LLC · McCammon, Idaho</div>
</footer>

<script src="/js/site.js" defer></script>
</body>
</html>'''

def page(title, desc, path, active, body, extra_head=''):
    return head(title, desc, path) + JSONLD_LOCAL + extra_head + '\n</head>\n<body>\n' + nav(active) + '<main>\n' + body + '\n</main>\n' + FOOTER

GICON = '''<svg class="gicon" viewBox="0 0 48 48" aria-hidden="true"><path fill="#4285F4" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.6 29.3 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3 0 5.8 1.1 7.9 3l5.7-5.7C34 6 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.2-.1-2.4-.4-3.5z"/><path fill="#34A853" d="M6.3 14.7l6.6 4.8C14.7 16 19 13 24 13c3 0 5.8 1.1 7.9 3l5.7-5.7C34 6 29.3 4 24 4 16.3 4 9.7 8.4 6.3 14.7z"/><path fill="#FBBC05" d="M24 44c5.2 0 9.8-2 13.3-5.2l-6.1-5c-2 1.4-4.5 2.2-7.2 2.2-5.3 0-9.7-3.4-11.3-8.1l-6.5 5C9.6 39.5 16.2 44 24 44z"/><path fill="#EA4335" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.3-2.3 4.3-4.2 5.7l6.1 5c4.3-4 6.8-9.8 6.8-16.7 0-1.2-.1-2.4-.4-3.5z"/></svg>'''

# ---------- HOME PAGE — full single-page experience ----------

HERO = '''<section class="hero" aria-label="Hero">
  <div class="hero-grad" aria-hidden="true"></div>
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="container hero-inner">
    <span class="hero-eyebrow reveal-up">Mobile Auto Detailing <span class="dot">·</span> Marsh Valley → Pocatello</span>
    <span class="hero-rule reveal-up" aria-hidden="true"></span>
    <h1 class="hero-title">
      <span class="line line-1 reveal-up">Showroom shine,</span>
      <span class="line line-2 reveal-up">delivered to your <span class="accent">driveway</span>.</span>
    </h1>
    <p class="sub reveal-up">Professional interior &amp; exterior detailing across Marsh Valley and Pocatello — we bring the wash to you, water and power included.</p>
    <div class="hero-ctas reveal-up">
      <a href="/#book" class="btn btn-gold">Book a Detail</a>
      <a href="tel:2083179786" class="btn btn-outline">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        (208) 317-9786
      </a>
    </div>
    <ul class="trust-strip reveal-up" aria-label="Trust signals">
      <li><span class="t-star">★</span> 4.9 Google</li>
      <li>100+ vehicles detailed</li>
      <li>Fully insured</li>
    </ul>
  </div>
</section>'''

SERVICES = f'''<section class="services" id="services">
  <div class="container">
    <div class="sec-head reveal">
      <span class="eyebrow">Services &amp; Pricing</span>
      <h2>Detailing That Comes To Your Driveway</h2>
      <p>Every package is tailored to your vehicle. We do a walk-through before every service.</p>
    </div>
    <div class="cat-label reveal">Interior Services</div>
    <div class="grid grid-2 reveal">
      <article class="card"><h3>Interior Refresh</h3><div class="price">Starting at $80</div><ul><li>Vacuum seats, carpets &amp; floor mats</li><li>Wipe down dash, console &amp; door panels</li><li>Clean inside windows &amp; mirrors</li><li>Spot clean upholstery as needed</li><li>Clean cup holders &amp; small compartments</li></ul><a href="/#book" class="btn btn-gold">Book This Service</a></article>
      <article class="card"><span class="badge">Most Popular</span><h3>Interior Deep Detail</h3><div class="price">Starting at $150</div><ul><li>Everything in Interior Refresh</li><li>Deep clean seats (cloth, vinyl, or leather)</li><li>Condition leather/vinyl surfaces</li><li>Odor neutralizer &amp; deodorizer</li><li>Interior trim detail</li></ul><a href="/#book" class="btn btn-gold">Book This Service</a></article>
    </div>
    <div class="cat-label reveal">Exterior Services</div>
    <div class="grid grid-3 reveal">
      <article class="card"><h3>Standard Exterior Wash</h3><div class="price">$25</div><ul><li>Rinse &amp; soap</li><li>Scrub &amp; pressure wash</li></ul><a href="/#book" class="btn btn-gold">Book This Service</a></article>
      <article class="card"><h3>Deluxe Exterior Wash</h3><div class="price">$50</div><ul><li>Everything in Standard</li><li>Wheels &amp; tires washed</li><li>Windows &amp; mirrors dried</li><li>Exterior wax protection (2–4 week shine)</li></ul><a href="/#book" class="btn btn-gold">Book This Service</a></article>
      <article class="card"><span class="badge green">Best Value</span><h3>Premium Exterior Wash</h3><div class="price">$100</div><ul><li>Everything in Deluxe</li><li>Wheels &amp; tires shined</li><li>Clay bar paint treatment</li><li>Exterior hand dried</li></ul><a href="/#book" class="btn btn-gold">Book This Service</a></article>
    </div>
    <div class="addons-wrap reveal">
      <span class="eyebrow">Customize Your Detail</span>
      <ul class="addons">
        <li><span>Upholstery Shampoo</span><span>$15/seat</span></li>
        <li><span>Pet Hair Removal</span><span>$40</span></li>
        <li><span>Leather Conditioning</span><span>$20/seat</span></li>
        <li><span>Deep Seat Stain Removal</span><span>$35</span></li>
        <li><span>Headliner Cleaning</span><span>$50</span></li>
        <li><span>Cargo Area Shampoo</span><span>$15–$30</span></li>
        <li><span>Car Seat Cleaning</span><span>Contact for pricing</span></li>
      </ul>
    </div>
    <div class="bundle reveal">
      <p><strong>Booking Interior + Exterior together?</strong> Call us for a bundled discount rate.</p>
      <a href="tel:2083179786" class="btn btn-gold">Call Us</a>
    </div>
  </div>
</section>'''

GALLERY = '''<section class="gallery">
  <div class="container">
    <div class="sec-head reveal">
      <span class="eyebrow">Before &amp; After</span>
      <h2>See the Difference</h2>
      <p>Real work. Real vehicles. Real results from right here in Southeast Idaho.</p>
    </div>
    <div class="ba-grid">
      <div class="ba reveal"><img src="/images/before-after-1.png" alt="Before and after auto detailing in McCammon Idaho by Back Roads Auto Wash" loading="lazy" /></div>
      <div class="ba reveal"><img src="/images/before-after-2.png" alt="Before and after interior detailing in Pocatello Idaho by Back Roads Auto Wash" loading="lazy" /></div>
      <div class="ba reveal"><img src="/images/before-after-3.png" alt="Before and after mobile car wash in Southeast Idaho by Back Roads Auto Wash" loading="lazy" /></div>
    </div>
  </div>
</section>'''

AREA = '''<section class="area" id="area">
  <div class="container">
    <div class="sec-head reveal">
      <span class="eyebrow">Service Area</span>
      <h2>We Come To You — Wherever You Are</h2>
      <p>Serving Southeast Idaho with mobile detailing you can count on.</p>
    </div>
    <div class="chips reveal" aria-label="Cities served">
      <span class="chip">McCammon</span><span class="chip">Lava Hot Springs</span><span class="chip">Arimo</span><span class="chip">Downey</span><span class="chip">Robin</span><span class="chip">Inkom</span><span class="chip">Pocatello</span>
    </div>
    <div class="reveal"><iframe class="map" title="Map of McCammon Idaho service area" src="https://www.google.com/maps?q=McCammon,Idaho&z=10&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    <p class="area-note reveal">Not sure if we serve your area? Call us at <a href="tel:2083179786">208-317-9786</a></p>
  </div>
</section>'''

REVIEWS = f'''<section class="reviews" id="reviews">
  <div class="container">
    <div class="sec-head reveal"><span class="eyebrow">5-Star Reviews</span><h2>What Our Customers Say</h2></div>
    <div class="review-grid">
      <article class="review reveal">{GICON}<div class="stars" aria-label="5 stars">★★★★★</div><p>"Highly recommend this company! He comes to you and does a fantastic job. Polite, friendly and thorough. My car looks brand new inside."</p><div class="who">Erika Gunter</div><div class="when">2 months ago</div></article>
      <article class="review reveal">{GICON}<div class="stars" aria-label="5 stars">★★★★★</div><p>"Came directly to my house and did an excellent job of washing and waxing my Roadtrek."</p><div class="who">Paula Rowe</div><div class="when">3 months ago</div></article>
      <article class="review reveal">{GICON}<div class="stars" aria-label="5 stars">★★★★★</div><p>"Back Roads Auto Wash was super friendly, professional, and did an amazing job on my car!!"</p><div class="who">Jeni Foster</div><div class="when">4 months ago</div></article>
    </div>
    <div class="reviews-cta reveal"><a href="https://share.google/ERh3UETePBt2pGKbb" target="_blank" rel="noopener" class="btn btn-outline">{GICON} View All Reviews on Google</a></div>
  </div>
</section>'''

FAQ = '''<section class="faq" id="faq">
  <div class="container">
    <div class="sec-head reveal"><span class="eyebrow">FAQ</span><h2>Frequently Asked Questions</h2><p>Everything you need to know before your appointment.</p></div>
    <div class="faq-list">
      <details class="reveal"><summary>Do I need to be home during the service?</summary><div class="a">Not necessarily — as long as we can access the vehicle and you've approved the service, we can handle the rest. We'll confirm details when booking.</div></details>
      <details class="reveal"><summary>How long does a typical service take?</summary><div class="a">It depends on the package and vehicle condition. An Interior Refresh typically takes 1–2 hours. A full Interior Deep Detail can take 2–4 hours. We'll give you an estimated time when we confirm your appointment.</div></details>
      <details class="reveal"><summary>What areas do you serve?</summary><div class="a">We serve McCammon, Lava Hot Springs, Arimo, Downey, Robin, Inkom, Pocatello, and surrounding Southeast Idaho communities. Not sure if you're in range? Just give us a call.</div></details>
      <details class="reveal"><summary>How do I pay?</summary><div class="a">We accept payment at time of service. Contact us when booking and we'll confirm accepted payment methods.</div></details>
      <details class="reveal"><summary>Can I book multiple vehicles?</summary><div class="a">Yes — and if you have more than one vehicle or a fleet, call us for a discounted multi-vehicle rate.</div></details>
      <details class="reveal"><summary>What's your cancellation policy?</summary><div class="a">Life happens. Just give us a heads up as soon as possible so we can reschedule for a time that works for you.</div></details>
    </div>
  </div>
</section>'''

BOOK = '''<section class="book" id="book">
  <div class="container">
    <div class="sec-head reveal"><span class="eyebrow">Contact &amp; Book</span><h2>Book Your Appointment</h2><p>We'll come to you — Monday through Saturday. Fill out the form below and we'll reach out to confirm.</p></div>
    <form class="form reveal" id="bookForm" novalidate>
      <div class="field"><label for="name">Full Name *</label><input id="name" name="name" required autocomplete="name" /></div>
      <div class="field"><label for="phone">Phone Number *</label><input id="phone" name="phone" type="tel" required autocomplete="tel" /></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" /></div>
      <div class="field"><label for="location">Location of Service *</label>
        <select id="location" name="location" required>
          <option value="">Select a city…</option>
          <option>McCammon</option><option>Lava Hot Springs</option><option>Arimo</option><option>Downey</option><option>Robin</option><option>Inkom</option><option>Pocatello</option><option>Other</option>
        </select>
      </div>
      <div class="field"><label>Service(s) Requested *</label>
        <div class="checks" id="svcChecks">
          <label><input type="checkbox" name="services" value="Interior Refresh" /> Interior Refresh</label>
          <label><input type="checkbox" name="services" value="Interior Deep Detail" /> Interior Deep Detail</label>
          <label><input type="checkbox" name="services" value="Standard Exterior Wash" /> Standard Exterior Wash</label>
          <label><input type="checkbox" name="services" value="Deluxe Exterior Wash" /> Deluxe Exterior Wash</label>
          <label><input type="checkbox" name="services" value="Premium Exterior Wash" /> Premium Exterior Wash</label>
          <label><input type="checkbox" name="services" value="Car Seat Cleaning" /> Car Seat Cleaning</label>
        </div>
      </div>
      <div class="field"><label for="vehicles">Number of Vehicles *</label>
        <select id="vehicles" name="vehicles" required>
          <option value="">Select…</option><option>1</option><option>2</option><option>3+</option><option>None — Car Seat Only</option>
        </select>
      </div>
      <div class="field"><label for="notes">Additional Notes</label><textarea id="notes" name="notes" placeholder="Vehicle type, condition, anything else we should know"></textarea></div>
      <button type="submit" class="btn btn-gold btn-block">Request My Appointment</button>
    </form>
    <div class="thankyou" id="thankyou" role="status" aria-live="polite">
      <strong>Thanks!</strong>
      We'll be in touch shortly to confirm your appointment.
    </div>
    <p style="text-align:center;margin-top:28px;color:#9ca3af">Prefer to call or text? <a href="tel:2083179786" style="color:var(--gold);font-weight:700">208-317-9786</a> · <a href="mailto:backroadsautowash@gmail.com" style="color:var(--gold);font-weight:700">backroadsautowash@gmail.com</a></p>
  </div>
</section>'''

HOME_BODY = HERO + SERVICES + GALLERY + AREA + REVIEWS + FAQ + BOOK

ABOUT_BODY = '''<section class="page-hero"><div class="container"><span class="eyebrow">About</span><h1>Meet the Back Roads Auto Wash Family</h1><p>Jake, Anna, Rosie &amp; Max — proudly serving Marsh Valley and Southeast Idaho.</p></div></section>
<section class="about">
  <div class="container about-grid">
    <div class="reveal">
      <img src="/images/about-family.jpg" alt="The Back Roads Auto Wash family — Jake, Anna, Rosie and Max — in Marsh Valley, Idaho" loading="lazy" width="900" height="1125" />
    </div>
    <div class="reveal about-body">
      <h2>Our Story</h2>
      <p>It was probably about time we introduced the people you're supporting when you book with us. 👋🏻</p>
      <p>Hi, we're Jake, Anna, Rosie, and Max!</p>
      <p>We moved to McCammon nearly 3 years ago and quickly fell in love with the community. While we're relatively new to town, Anna's mom, grandparents, and great-grandparents have deep roots in Marsh Valley and Eastern Idaho, so this area has felt like home for generations.</p>
      <p>Back Roads Auto Wash started when Jake noticed there weren't many options for people in Marsh Valley who wanted professional detailing services without having to wait for someone to come from Pocatello. He saw an opportunity to bring a convenient, reliable service directly to our community — and that's how Back Roads was born.</p>
      <p>When we're not cleaning vehicles, you'll usually find us swimming in Lava Hot Springs, exploring the mountains around Marsh Valley in our side-by-side, or spending time with family and friends.</p>
      <p>One of our favorite things about living here has been getting to know the incredible people who make this community so special. We're grateful for every customer who has trusted us with their vehicle and supported our family's small business.</p>
      <p>Thank you for helping us do what we love. We look forward to serving Marsh Valley and the surrounding communities for years to come! 🚗</p>
      <ul class="checklist">
        <li>Family owned &amp; operated</li>
        <li>Mobile — we come to you</li>
        <li>Available Monday through Saturday</li>
        <li>Serving McCammon, Pocatello &amp; surrounding Idaho communities</li>
      </ul>
    </div>
  </div>
</section>'''

FAQ_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Do I need to be home during the service?","acceptedAnswer":{"@type":"Answer","text":"Not necessarily — as long as we can access the vehicle and you have approved the service, we can handle the rest."}},{"@type":"Question","name":"How long does a typical service take?","acceptedAnswer":{"@type":"Answer","text":"An Interior Refresh typically takes 1–2 hours. A full Interior Deep Detail can take 2–4 hours."}},{"@type":"Question","name":"What areas do you serve?","acceptedAnswer":{"@type":"Answer","text":"McCammon, Lava Hot Springs, Arimo, Downey, Robin, Inkom, Pocatello, and surrounding Southeast Idaho communities."}},{"@type":"Question","name":"How do I pay?","acceptedAnswer":{"@type":"Answer","text":"We accept payment at time of service."}},{"@type":"Question","name":"Can I book multiple vehicles?","acceptedAnswer":{"@type":"Answer","text":"Yes — and if you have more than one vehicle or a fleet, call us for a discounted multi-vehicle rate."}},{"@type":"Question","name":"What is your cancellation policy?","acceptedAnswer":{"@type":"Answer","text":"Life happens. Just give us a heads up as soon as possible so we can reschedule."}}]}
</script>'''

pages = [
    ('index.html',
     'Back Roads Auto Wash | Mobile Car Detailing in McCammon, Pocatello & Southeast Idaho',
     'Mobile car washing and auto detailing brought right to your driveway. Serving McCammon, Pocatello, Lava Hot Springs & surrounding Idaho. Book online or call 208-317-9786.',
     '/', 'home', HOME_BODY, FAQ_LD),
    ('about/index.html',
     'About | Back Roads Auto Wash Family',
     'Meet the Back Roads Auto Wash family — Jake, Anna, Rosie and Max — proudly serving Marsh Valley and Southeast Idaho.',
     '/about', 'about', ABOUT_BODY, ''),
]

for fname, title, desc, path, active, body, extra in pages:
    out = os.path.join(PUB, fname)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(page(title, desc, path, active, body, extra))
    print('wrote', out)

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://backroadsautowash.com/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://backroadsautowash.com/about</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
</urlset>
'''
with open(os.path.join(PUB, 'sitemap.xml'), 'w') as f:
    f.write(sitemap)

with open(os.path.join(PUB, '_redirects'), 'w') as f:
    f.write('# Clean URLs (most static hosts auto-serve /folder/index.html as /folder)\n')

htaccess = '''Options -MultiViews
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME}/index.html -f
RewriteRule ^([^/]+)$ /$1/index.html [L]
'''
with open(os.path.join(PUB, '.htaccess'), 'w') as f:
    f.write(htaccess)

print('done')
