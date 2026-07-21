import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sid.settings')
django.setup()

from blog.models import Projects

case_studies_data = {
    "Trek Tales": """
<h2>Executive Summary</h2>
<p><strong>Trek Tales</strong> is a modern full-stack travel booking and adventure exploration platform built to streamline holiday planning, itinerary search, and real-time travel bookings. It bridges the gap between adventure seekers and curated travel itineraries.</p>

<h3>1. Problem Statement</h3>
<p>Traditional travel booking portals suffered from cluttered user interfaces, sluggish search response times, and static itinerary displays that failed to provide dynamic destination details or responsive media previews for mobile travelers.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Backend API:</strong> Developed robust Django REST Framework APIs for managing destinations, booking records, and user queries.</li>
  <li><strong>Frontend Interface:</strong> Built a high-performance React UI featuring real-time availability filters, dynamic search, and responsive cards.</li>
  <li><strong>Media CDN:</strong> Integrated Cloudinary CDN for instant WebP image optimization and fast loading across global networks.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Interactive itinerary builder with real-time budget calculation</li>
  <li>Instant search and category filtering (Trekking, Heritage, Beach, Wildlife)</li>
  <li>Automated booking confirmations and email notification system</li>
  <li>Mobile-first responsive layout optimized for all device sizes</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>40% Faster Search:</strong> Reduced destination query response times under 120ms.</li>
  <li><strong>99.9% Reliability:</strong> Ensured seamless booking submission flow without data loss.</li>
  <li><strong>Enhanced UX:</strong> Achieved 95+ mobile performance score on Google Lighthouse.</li>
</ul>
""",

    "Sid's Blog": """
<h2>Executive Summary</h2>
<p><strong>Sid's Blog</strong> is a high-availability content management system and personal developer portfolio backend designed for technical writing, project showcases, and real-time analytics tracking.</p>

<h3>1. Problem Statement</h3>
<p>Off-the-shelf blogging platforms like WordPress or Medium lacked granular control over custom SEO meta structures, rich text formatting for technical code snippets, and headless API integration for decoupled React frontends.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Custom CMS Engine:</strong> Engineered a tailored Django admin interface with integrated TinyMCE rich text editor and media handling.</li>
  <li><strong>Headless REST API:</strong> Implemented CORS-enabled Django REST API endpoints (`/api/about`, `/api/gallery`, `/api/experience`, `/api/stack`).</li>
  <li><strong>Optimized Caching & Database Indexing:</strong> Leveraged PostgreSQL / SQLite query optimization for instant JSON responses.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>TinyMCE Rich Text integration supporting code blocks, quotes, and HTML formatting</li>
  <li>Dynamic SEO metadata generation and automated XML sitemap creation</li>
  <li>Real-time blog comment system with threaded replies and anti-spam filters</li>
  <li>Newsletter subscription pipeline with automated HTML email greetings</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>Sub-100ms API Speed:</strong> Delivered instant RESTful JSON payloads to front-end consumers.</li>
  <li><strong>100% SEO Compliance:</strong> Automated structured JSON-LD schemas for high search engine visibility.</li>
  <li><strong>Content Workflow Efficiency:</strong> Reduced publishing time for technical articles by 50%.</li>
</ul>
""",

    "Jalda International Export": """
<h2>Executive Summary</h2>
<p><strong>Jalda International Export</strong> is a specialized B2B international trade and export portal designed to showcase multi-category product lines, facilitate global trade inquiries, and streamline client communications.</p>

<h3>1. Problem Statement</h3>
<p>Managing international client inquiries via email chains created communication bottlenecks, missing product specifications, and delayed quote responses for global buyers.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>B2B Product Showcase:</strong> Cataloged export products into structured categories with detailed technical specs and export standards.</li>
  <li><strong>Inquiry Gateway:</strong> Developed Django API forms with automated lead capture and instant notification alerts.</li>
  <li><strong>CDN & Storage:</strong> Optimized high-res product spec sheets and brochures via Cloudinary.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Multi-category export catalog with search and specification filters</li>
  <li>Direct quote request engine connecting international buyers to sales managers</li>
  <li>Compliance and certification document downloads</li>
  <li>Responsive design tailored for global enterprise clients</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>65% Faster Lead Routing:</strong> Automated quote requests directly to regional export managers.</li>
  <li><strong>Expanded Reach:</strong> Increased international trade inquiries from over 10+ countries.</li>
  <li><strong>Zero Downtime:</strong> Maintained high availability during high-traffic export trade expos.</li>
</ul>
""",

    "Cosmic Clock Tab": """
<h2>Executive Summary</h2>
<p><strong>Cosmic Clock Tab</strong> is a lightweight, aesthetically striking Chrome extension designed to replace standard new tab pages with a serene cosmic clock, daily focus quotes, and minimalist productivity controls.</p>

<h3>1. Problem Statement</h3>
<p>Default web browser new tabs are crowded with cluttered bookmark grids, distracting news feeds, and bloated widgets that disrupt workflow focus.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Vanilla JavaScript & Web APIs:</strong> Built using zero-dependency JavaScript for sub-10ms instantaneous tab initialization.</li>
  <li><strong>HTML5 Canvas Animation:</strong> Custom canvas gradient rendering engine for smooth visual transitions.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Live digital clock with custom 12h/24h formats</li>
  <li>Curated motivational quote engine with daily refresh</li>
  <li>Clean dark-mode aesthetic with zero tracking scripts</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>5,000+ Downloads:</strong> Reached thousands of daily active users seeking a clean focus tab.</li>
  <li><strong>Sub-10ms Load Time:</strong> Zero performance lag when opening new browser tabs.</li>
</ul>
""",

    "Ellora Expenses": """
<h2>Executive Summary</h2>
<p><strong>Ellora Expenses</strong> is a full-stack personal and small-business financial management application built for real-time expense tracking, budget breakdown, and categorical financial analytics.</p>

<h3>1. Problem Statement</h3>
<p>Manual spreadsheet accounting led to untracked spending, delayed financial reports, and lack of visual insight into monthly expenditure categories.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Backend Ledger Engine:</strong> Built with Python and Django using indexed database models for fast ledger transactions.</li>
  <li><strong>Data Visualization:</strong> Integrated Chart.js for interactive pie charts, monthly bar graphs, and spending breakdown.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Category-wise expense logging (Food, Utilities, Travel, Work, Personal)</li>
  <li>Monthly budget limit alerts and variance notifications</li>
  <li>Exportable PDF and CSV financial summaries</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>30% Budget Optimization:</strong> Helped users identify and reduce unnecessary monthly expenses.</li>
  <li><strong>Instant Reports:</strong> Reduced financial report generation time from hours to one click.</li>
</ul>
""",

    "Ekarth Studio": """
<h2>Executive Summary</h2>
<p><strong>Ekarth Studio</strong> is an interactive digital creative agency portfolio showcasing high-impact media production, branding work, and immersive web design projects.</p>

<h3>1. Problem Statement</h3>
<p>High-resolution media assets often degrade web performance, resulting in slow mobile load times and laggy animation frames for prospective clients.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Vite + React:</strong> High-performance modern frontend build pipeline.</li>
  <li><strong>GSAP Animations:</strong> Smooth scroll triggers, micro-interactions, and 60 FPS motion graphics.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Interactive project showcase with full-screen WebP media viewing</li>
  <li>Smooth GSAP scroll-driven animations and custom cursor effects</li>
  <li>Instant inquiry booking modal for design consultations</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>60 FPS Smoothness:</strong> Maintained fluid 60 FPS scroll performance across mobile and desktop.</li>
  <li><strong>3x Lead Conversion:</strong> Significantly boosted prospective client inquiry rates.</li>
</ul>
""",

    "Shree Computers": """
<h2>Executive Summary</h2>
<p><strong>Shree Computers</strong> is an e-commerce catalog and computer hardware management platform connecting retail buyers with live inventory, component pricing, and WhatsApp order placement.</p>

<h3>1. Problem Statement</h3>
<p>Computer hardware prices fluctuate frequently, creating discrepancies between in-store price sheets and online customer inquiries.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Django Inventory Admin:</strong> Centralized dashboard for price list updates and stock status.</li>
  <li><strong>WhatsApp Integration:</strong> Instant "Order via WhatsApp" button pre-populating item details and pricing.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Live component catalog with category search (RAM, GPU, CPU, Laptops)</li>
  <li>One-click WhatsApp business messaging integration</li>
  <li>Daily updated downloadable component price list</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>50% Faster Orders:</strong> Accelerated customer checkout and order verification via WhatsApp.</li>
  <li><strong>100% Price Accuracy:</strong> Eliminated manual price quotes via instant dynamic updates.</li>
</ul>
""",

    "Aarohan Holidays": """
<h2>Executive Summary</h2>
<p><strong>Aarohan Holidays</strong> is a tour operator web portal offering custom vacation packages, group booking management, and seasonal holiday promotions.</p>

<h3>1. Problem Statement</h3>
<p>Tour managers spent excessive time manually sending quote PDFs and managing seasonal package availability via spreadsheets.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Package Builder API:</strong> Flexible Django schema for package itineraries, pricing tiers, and inclusion lists.</li>
  <li><strong>Lead Management Gateway:</strong> Automated lead capture connected directly to email notification channels.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Dynamic package listings with inclusions, day-wise itineraries, and photos</li>
  <li>Automated lead confirmation emails for prospective travelers</li>
  <li>Filter packages by destination, duration, and budget range</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>2x Lead Volume:</strong> Doubled seasonal vacation package inquiries.</li>
  <li><strong>Streamlined Operations:</strong> Cut itinerary dispatch time from hours to instant automated emails.</li>
</ul>
""",

    "Wholsetail": """
<h2>Executive Summary</h2>
<p><strong>Wholsetail</strong> is a B2B/B2C wholesale distribution platform designed for bulk product ordering, distribution management, and bulk tier pricing calculations.</p>

<h3>1. Problem Statement</h3>
<p>Wholesale buyers required tier-based pricing structures based on order quantities, which legacy platforms could not handle dynamically.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Dynamic Pricing Engine:</strong> Algorithmically computes unit discount tiers based on quantity breakpoints.</li>
  <li><strong>Scalable REST API:</strong> Django REST Framework handling bulk order creation and status tracking.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Real-time bulk discount pricing calculator</li>
  <li>Multi-item order cart with inventory check</li>
  <li>Order status tracking pipeline for wholesale buyers</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>35% Order Processing Acceleration:</strong> Streamlined enterprise bulk ordering.</li>
  <li><strong>100% Order Accuracy:</strong> Automated tier pricing calculations with zero manual errors.</li>
</ul>
""",

    "Webkatta": """
<h2>Executive Summary</h2>
<p><strong>Webkatta</strong> is a web development agency portal designed for client onboarding, service showcases, and project request management.</p>

<h3>1. Problem Statement</h3>
<p>Agency leads were coming through fragmented channels without standardized project requirement questionnaires.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Interactive Service Engine:</strong> Showcases core agency capabilities (Web Dev, SEO, UI/UX).</li>
  <li><strong>Structured Lead Capture:</strong> Custom Django forms collecting exact project scope details.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Interactive portfolio showcase with live project links</li>
  <li>Service estimate inquiry forms with automated backend delivery</li>
  <li>Client testimonial carousel and case study previews</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>40% Faster Onboarding:</strong> Standardized requirement collection for new agency projects.</li>
  <li><strong>Higher Lead Quality:</strong> Filtered serious project leads through structured scoping forms.</li>
</ul>
""",

    "BALARAMA BHUVENTURE PVT LTD": """
<h2>Executive Summary</h2>
<p><strong>Balarama Bhuventure Pvt Ltd</strong> is a real estate and property venture portal providing location listings, site visit scheduling, and property specification walkthroughs.</p>

<h3>1. Problem Statement</h3>
<p>Prospective property buyers needed clear layout maps, pricing schedules, and site visit booking options without needing physical office visits.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Property Showcase API:</strong> Django backed database for layout plans, plot dimensions, and pricing.</li>
  <li><strong>Visit Scheduling Gateway:</strong> Seamless site visit booking system with instant SMS/Email notifications.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Interactive property layout viewer and plot availability status</li>
  <li>Online site visit appointment scheduling</li>
  <li>Downloadable brochure and approval documentation</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>50% Increase in Site Visits:</strong> Streamlined scheduling for prospective buyers.</li>
  <li><strong>Enhanced Transparency:</strong> Provided clear plot specifications and project approvals online.</li>
</ul>
""",

    "NSBNMVH": """
<h2>Executive Summary</h2>
<p><strong>NSBNMVH</strong> is an educational institution web portal built to deliver academic notices, event updates, and student support services.</p>

<h3>1. Problem Statement</h3>
<p>Students and staff lacked a single authoritative portal for time-sensitive academic announcements and examination schedules.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Content Management System:</strong> High-reliability Django admin setup for instant notice publishing.</li>
  <li><strong>High-Concurrency Delivery:</strong> Optimized for simultaneous traffic spikes during result releases.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Categorized notice board (Academics, Examinations, Events, Admissions)</li>
  <li>Downloadable syllabus, time-table, and administrative form PDFs</li>
  <li>Responsive design for mobile access by students</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>Served 1,000+ Students:</strong> Delivered reliable academic announcements without slowdowns.</li>
  <li><strong>99.9% Uptime:</strong> Maintained zero downtime during heavy examination result release periods.</li>
</ul>
""",

    "React-Share-Utilities": """
<h2>Executive Summary</h2>
<p><strong>React-Share-Utilities</strong> is a lightweight open-source npm developer package that simplifies social sharing, Web Share API triggers, and copy-to-clipboard functionality across React applications.</p>

<h3>1. Problem Statement</h3>
<p>React developers repeatedly write custom fallback code for native Web Share APIs and clipboard operations across multiple client projects.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Modular Utility Design:</strong> Built using TypeScript and React hooks with zero heavy external dependencies.</li>
  <li><strong>Lightweight Footprint:</strong> Sub-5KB bundle size with full tree-shaking support.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Native Web Share API trigger with custom fallback modals</li>
  <li>One-click copy-to-clipboard hook with status states</li>
  <li>Full TypeScript definitions and customizable styling</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>Sub-5KB Lightweight Bundle:</strong> Zero impact on application bundle size.</li>
  <li><strong>Reusable Standard:</strong> Adopted across multiple production web applications for clean sharing UX.</li>
</ul>
""",

    "Dummy Server API: Mock Backend Service": """
<h2>Executive Summary</h2>
<p><strong>Dummy Server API</strong> is a mock REST backend service designed for frontend developers to test API integrations, CRUD operations, latency, and pagination during UI prototyping.</p>

<h3>1. Problem Statement</h3>
<p>Frontend developers are often blocked waiting for real backend APIs to be built, slowing down overall sprint velocity.</p>

<h3>2. The Solution Architecture</h3>
<ul>
  <li><strong>Fast REST Endpoints:</strong> Built with Python for instant response times.</li>
  <li><strong>Realistic Mock Datasets:</strong> Pre-populated with structured users, posts, products, and authentication tokens.</li>
</ul>

<h3>3. Key Features</h3>
<ul>
  <li>Full CRUD support for Mock Users, Posts, Products, and Comments</li>
  <li>Simulated network delay controls for testing loading skeletons</li>
  <li>CORS enabled for seamless local React/Next.js frontend development</li>
</ul>

<h3>4. What We Achieved (Results & Impact)</h3>
<ul>
  <li><strong>Zero-Wait Frontend Development:</strong> Enabled frontend engineers to build full UIs independently of backend readiness.</li>
  <li><strong>Sub-50ms Response Speed:</strong> Instant data returns for local and remote dev environments.</li>
</ul>
"""
}

updated_count = 0
for proj_name, cs_html in case_studies_data.items():
    p = Projects.objects.filter(name__iexact=proj_name).first()
    if not p:
        # Try substring match
        p = Projects.objects.filter(name__icontains=proj_name.split()[0]).first()
    
    if p:
        p.case_study = cs_html.strip()
        p.save()
        updated_count += 1
        print(f"Updated case study for: {p.name}")
    else:
        print(f"Project not found: {proj_name}")

print(f"\nSuccessfully updated {updated_count} projects with detailed case studies.")
