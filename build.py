import os

HEAD_TAGS = """
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            navy: '#0f172a',    // Very dark slate/navy
                            blue: '#1e3a8a',    // Deep classic blue
                            gold: '#bf953f',    // Elegant gold
                            light: '#fcfbf9',   // Off-white/cream
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['"Playfair Display"', 'serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #fcfbf9; }
        .heading-serif { font-family: 'Playfair Display', serif; }
        .gold-accent { color: #bf953f; }
        .bg-gold-accent { background-color: #bf953f; }
        .border-gold-accent { border-color: #bf953f; }
        .nav-link { position: relative; transition: color 0.3s ease; }
        .nav-link::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: #bf953f; transition: width 0.3s ease; }
        .nav-link:hover::after, .nav-link.active::after { width: 100%; }
        .nav-link:hover { color: #bf953f; }
    </style>
    <script src="scripts.js"></script>
"""

PAGES = {
    "index.html": {
        "title": "Freedman Broker | Premium Insurance Solutions",
        "active": "home",
        "content": """
    <!-- Hero Section -->
    <section class="relative bg-brand-navy min-h-[85vh] flex items-center">
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Corporate Architecture" class="w-full h-full object-cover opacity-20 mix-blend-luminosity">
            <div class="absolute inset-0 bg-gradient-to-r from-brand-navy via-brand-navy/90 to-transparent"></div>
        </div>
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-20">
            <div class="md:w-2/3 lg:w-1/2">
                <div class="flex items-center mb-6">
                    <div class="w-12 h-[1px] bg-brand-gold mr-4"></div>
                    <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs">Excellence in Protection</span>
                </div>
                <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold text-white leading-[1.1] mb-8 heading-serif">
                    Protecting What <br>
                    <span class="italic text-gray-300 font-light">Matters Most.</span>
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 font-light leading-relaxed max-w-lg">
                    Bespoke insurance portfolios crafted with precision for discerning individuals and established enterprises.
                </p>
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6">
                    <a href="contact.html" class="bg-brand-gold hover:bg-yellow-600 text-white px-8 py-4 rounded-sm font-medium text-sm uppercase tracking-wider transition-colors duration-300 text-center shadow-lg">
                        Consult an Advisor
                    </a>
                    <a href="about-us.html" class="bg-transparent border border-gray-500 text-white hover:border-white hover:bg-white/5 px-8 py-4 rounded-sm font-medium text-sm uppercase tracking-wider transition-all duration-300 text-center">
                        Our Philosophy
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Expertise Section -->
    <section class="py-24 bg-brand-light">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">Our Expertise</span>
                <h2 class="text-4xl font-bold text-brand-navy heading-serif mb-6">Comprehensive Portfolios</h2>
                <div class="w-16 h-0.5 bg-brand-gold mx-auto"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-10 lg:gap-16">
                <!-- Personal Card -->
                <div class="group cursor-pointer" onclick="window.location.href='personal-insurance.html'">
                    <div class="relative h-80 overflow-hidden rounded-sm mb-6 shadow-xl">
                        <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Luxury Home" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute inset-0 bg-brand-navy/20 group-hover:bg-transparent transition-colors duration-500"></div>
                    </div>
                    <div class="pr-8">
                        <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3 flex items-center">
                            Personal Lines <i class="fas fa-arrow-right ml-4 text-brand-gold text-sm opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300"></i>
                        </h3>
                        <p class="text-gray-600 leading-relaxed mb-4">Curated protection for high-value properties, luxury vehicles, and comprehensive family legacy planning.</p>
                        <a href="personal-insurance.html" class="text-sm font-semibold uppercase tracking-wider text-brand-gold hover:text-brand-navy transition-colors">Explore Personal</a>
                    </div>
                </div>

                <!-- Commercial Card -->
                <div class="group cursor-pointer" onclick="window.location.href='commercial-insurance.html'">
                    <div class="relative h-80 overflow-hidden rounded-sm mb-6 shadow-xl">
                        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Corporate Office" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute inset-0 bg-brand-navy/20 group-hover:bg-transparent transition-colors duration-500"></div>
                    </div>
                    <div class="pr-8">
                        <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3 flex items-center">
                            Commercial Lines <i class="fas fa-arrow-right ml-4 text-brand-gold text-sm opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300"></i>
                        </h3>
                        <p class="text-gray-600 leading-relaxed mb-4">Sophisticated risk mitigation strategies for enterprises, real estate portfolios, and executive liability.</p>
                        <a href="commercial-insurance.html" class="text-sm font-semibold uppercase tracking-wider text-brand-gold hover:text-brand-navy transition-colors">Explore Commercial</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Client Testimonials -->
    <section class="py-24 bg-white border-t border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">Client Relations</span>
                <h2 class="text-4xl font-bold text-brand-navy heading-serif mb-6">Enduring Partnerships</h2>
                <div class="w-16 h-0.5 bg-brand-gold mx-auto"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                <div class="p-8 border border-gray-100 shadow-sm relative">
                    <i class="fas fa-quote-left text-brand-gold/20 text-5xl absolute top-4 left-4"></i>
                    <p class="text-gray-600 relative z-10 mb-6 italic leading-relaxed">"Their handling of our corporate liability portfolio is nothing short of exceptional. The proactive risk management insights provided by Freedman Broker have been invaluable to our expansion."</p>
                    <div class="flex items-center">
                        <div class="w-10 h-10 bg-brand-navy rounded-full flex items-center justify-center text-white font-serif mr-4">J</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Jonathan H.</p>
                            <p class="text-xs text-gray-500 uppercase tracking-wide">CEO, Tech Innovations</p>
                        </div>
                    </div>
                </div>
                <div class="p-8 border border-gray-100 shadow-sm relative">
                    <i class="fas fa-quote-left text-brand-gold/20 text-5xl absolute top-4 left-4"></i>
                    <p class="text-gray-600 relative z-10 mb-6 italic leading-relaxed">"Securing our estate and private collection was handled with absolute discretion and unmatched expertise. They understand the nuances of high-value asset protection perfectly."</p>
                    <div class="flex items-center">
                        <div class="w-10 h-10 bg-brand-navy rounded-full flex items-center justify-center text-white font-serif mr-4">E</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Eleanor V.</p>
                            <p class="text-xs text-gray-500 uppercase tracking-wide">Private Client</p>
                        </div>
                    </div>
                </div>
                <div class="p-8 border border-gray-100 shadow-sm relative">
                    <i class="fas fa-quote-left text-brand-gold/20 text-5xl absolute top-4 left-4"></i>
                    <p class="text-gray-600 relative z-10 mb-6 italic leading-relaxed">"When a fire threatened our manufacturing facility, Freedman's claims advocacy team stepped in immediately. They managed the entire process, minimizing our downtime significantly."</p>
                    <div class="flex items-center">
                        <div class="w-10 h-10 bg-brand-navy rounded-full flex items-center justify-center text-white font-serif mr-4">M</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Marcus L.</p>
                            <p class="text-xs text-gray-500 uppercase tracking-wide">Director of Operations</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Market Insights (News) -->
    <section class="py-24 bg-brand-light">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-end mb-16 border-b border-gray-200 pb-6">
                <div>
                    <h2 class="text-4xl font-bold text-brand-navy heading-serif">Market Insights</h2>
                </div>
                <a href="#" class="text-sm font-semibold uppercase tracking-wider text-brand-gold hover:text-brand-navy transition-colors">View All Articles</a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div class="flex gap-6 group cursor-pointer">
                    <div class="w-1/3 h-32 overflow-hidden rounded-sm shadow-md">
                        <img src="https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Finance" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="w-2/3">
                        <p class="text-brand-gold text-xs font-semibold tracking-wider uppercase mb-2">Corporate Liability</p>
                        <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2 group-hover:text-brand-gold transition-colors">Navigating D&O Insurance in 2024</h3>
                        <p class="text-gray-600 text-sm line-clamp-2">An executive briefing on the shifting landscape of Directors and Officers liability...</p>
                    </div>
                </div>
                <div class="flex gap-6 group cursor-pointer">
                    <div class="w-1/3 h-32 overflow-hidden rounded-sm shadow-md">
                        <img src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Estate" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="w-2/3">
                        <p class="text-brand-gold text-xs font-semibold tracking-wider uppercase mb-2">Private Wealth</p>
                        <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2 group-hover:text-brand-gold transition-colors">Protecting Fine Art Collections</h3>
                        <p class="text-gray-600 text-sm line-clamp-2">Why standard homeowner policies fail to adequately protect significant art portfolios...</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Trust Banner -->
    <section class="py-16 bg-white border-t border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <p class="text-center text-xs font-semibold uppercase tracking-[0.2em] text-gray-400 mb-10">Underwritten by Premier Partners</p>
            <div class="flex flex-wrap justify-center items-center gap-12 lg:gap-24 opacity-40 grayscale hover:grayscale-0 transition-all duration-700">
                <span class="text-2xl font-bold heading-serif">INTACT</span>
                <span class="text-2xl font-bold heading-serif">AVIVA</span>
                <span class="text-2xl font-bold heading-serif">CHUBB</span>
                <span class="text-2xl font-bold heading-serif">WAWANESA</span>
            </div>
        </div>
    </section>
        """
    },
    "personal-insurance.html": {
        "title": "Personal Insurance | Freedman Broker",
        "active": "personal",
        "content": """
    <!-- Page Header -->
    <div class="bg-brand-navy py-24 relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-20 -mr-20 w-96 h-96 border border-brand-gold/20 rounded-full opacity-50"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">Individual & Family</span>
            <h1 class="text-5xl md:text-6xl font-bold text-white heading-serif mb-6">Personal Coverage</h1>
            <p class="text-xl text-gray-400 max-w-2xl font-light">Safeguarding your lifestyle, assets, and legacy with precision.</p>
        </div>
    </div>

    <!-- The Freedman Advantage -->
    <section class="py-16 bg-white border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                <div class="p-6">
                    <i class="fas fa-search-dollar text-brand-gold text-3xl mb-4"></i>
                    <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2">Market Analysis</h3>
                    <p class="text-gray-600 text-sm">We continually monitor the market to ensure your premiums reflect the best available value.</p>
                </div>
                <div class="p-6">
                    <i class="fas fa-file-contract text-brand-gold text-3xl mb-4"></i>
                    <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2">Policy Consolidation</h3>
                    <p class="text-gray-600 text-sm">Streamline your portfolio by bundling auto, home, and umbrella liability under one strategy.</p>
                </div>
                <div class="p-6">
                    <i class="fas fa-user-shield text-brand-gold text-3xl mb-4"></i>
                    <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2">Dedicated Advocate</h3>
                    <p class="text-gray-600 text-sm">A single point of contact for all your inquiries, policy updates, and claims assistance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Content -->
    <main class="flex-grow max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-24 space-y-24">
        
        <!-- Auto -->
        <div id="auto" class="flex flex-col md:flex-row gap-12 items-center">
            <div class="md:w-1/2">
                <div class="relative">
                    <div class="absolute -inset-4 border border-brand-gold/30 transform translate-x-2 translate-y-2 rounded-sm"></div>
                    <img src="https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Luxury Car" class="relative z-10 rounded-sm shadow-xl w-full h-80 object-cover">
                </div>
            </div>
            <div class="md:w-1/2 md:pl-8">
                <h2 class="text-3xl font-bold text-brand-navy heading-serif mb-4">Automobile & Collection</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">From daily drivers to exotic collections, we secure policies that offer total replacement value, genuine parts guarantees, and superior liability protection.</p>
                <ul class="space-y-3 mb-8 text-gray-700">
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Comprehensive Collision</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Classic & Exotic Valuations</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Worldwide Liability Extensions</li>
                </ul>
                <a href="contact.html" class="inline-block border-b-2 border-brand-navy text-brand-navy font-semibold uppercase tracking-wider text-sm pb-1 hover:text-brand-gold hover:border-brand-gold transition-colors">Request a Consultation</a>
            </div>
        </div>

        <!-- Home -->
        <div id="home" class="flex flex-col md:flex-row-reverse gap-12 items-center">
            <div class="md:w-1/2">
                <div class="relative">
                    <div class="absolute -inset-4 border border-brand-gold/30 transform -translate-x-2 translate-y-2 rounded-sm"></div>
                    <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Estate" class="relative z-10 rounded-sm shadow-xl w-full h-80 object-cover">
                </div>
            </div>
            <div class="md:w-1/2 md:pr-8">
                <h2 class="text-3xl font-bold text-brand-navy heading-serif mb-4">Home & Estate</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Protecting your most valuable asset requires more than a standard policy. We specialize in high-value properties, secondary homes, and fine art collections.</p>
                <ul class="space-y-3 mb-8 text-gray-700">
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Guaranteed Replacement Cost</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Fine Art & Jewelry Floaters</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Domestic Staff Liability</li>
                </ul>
                <a href="contact.html" class="inline-block border-b-2 border-brand-navy text-brand-navy font-semibold uppercase tracking-wider text-sm pb-1 hover:text-brand-gold hover:border-brand-gold transition-colors">Request a Consultation</a>
            </div>
        </div>
        
        <!-- Life -->
        <div id="life" class="flex flex-col md:flex-row gap-12 items-center">
            <div class="md:w-1/2">
                <div class="relative">
                    <div class="absolute -inset-4 border border-brand-gold/30 transform translate-x-2 translate-y-2 rounded-sm"></div>
                    <img src="https://images.unsplash.com/photo-1536640712-4d4c36ef0e47?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Family" class="relative z-10 rounded-sm shadow-xl w-full h-80 object-cover">
                </div>
            </div>
            <div class="md:w-1/2 md:pl-8">
                <h2 class="text-3xl font-bold text-brand-navy heading-serif mb-4">Life & Health Legacy</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Secure your family's future and preserve your wealth across generations. We offer bespoke life and health products designed for complex estates.</p>
                <ul class="space-y-3 mb-8 text-gray-700">
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Estate Preservation Plans</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Premium Term & Whole Life</li>
                    <li class="flex items-center"><i class="fas fa-check text-brand-gold mr-3 text-sm"></i> Critical Illness & Disability</li>
                </ul>
                <a href="contact.html" class="inline-block border-b-2 border-brand-navy text-brand-navy font-semibold uppercase tracking-wider text-sm pb-1 hover:text-brand-gold hover:border-brand-gold transition-colors">Request a Consultation</a>
            </div>
        </div>

    </main>
    
    <!-- FAQ Section -->
    <section class="py-20 bg-brand-navy">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-white heading-serif mb-4">Frequently Asked Questions</h2>
                <div class="w-16 h-0.5 bg-brand-gold mx-auto"></div>
            </div>
            <div class="space-y-6">
                <div class="bg-gray-800 p-6 rounded-sm border border-gray-700">
                    <h3 class="text-xl font-semibold text-white mb-3">How often should I review my personal insurance portfolio?</h3>
                    <p class="text-gray-400 text-sm leading-relaxed">We recommend a comprehensive review annually, or immediately following significant life events such as a marriage, birth of a child, major property acquisition, or significant changes to your asset valuation.</p>
                </div>
                <div class="bg-gray-800 p-6 rounded-sm border border-gray-700">
                    <h3 class="text-xl font-semibold text-white mb-3">Are my fine art and jewelry covered under my standard homeowner's policy?</h3>
                    <p class="text-gray-400 text-sm leading-relaxed">Standard policies often have strict sub-limits for high-value items. To guarantee full replacement value without depreciation, these items must be specifically scheduled on a valuable articles floater.</p>
                </div>
            </div>
        </div>
    </section>
        """
    },
    "commercial-insurance.html": {
        "title": "Commercial Insurance | Freedman Broker",
        "active": "commercial",
        "content": """
    <!-- Page Header -->
    <div class="bg-brand-navy py-24 relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-20 -mr-20 w-96 h-96 border border-brand-gold/20 rounded-full opacity-50"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">Enterprise & Business</span>
            <h1 class="text-5xl md:text-6xl font-bold text-white heading-serif mb-6">Commercial Lines</h1>
            <p class="text-xl text-gray-400 max-w-2xl font-light">Sophisticated risk mitigation strategies for modern enterprises.</p>
        </div>
    </div>

    <!-- Industry Expertise -->
    <section class="py-16 bg-brand-light border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h3 class="text-center text-sm font-semibold uppercase tracking-widest text-brand-navy mb-10">Specialized Industry Practices</h3>
            <div class="flex flex-wrap justify-center gap-4">
                <span class="px-6 py-2 border border-brand-gold/50 text-brand-navy rounded-full text-sm font-medium hover:bg-brand-gold hover:text-white transition-colors cursor-pointer">Real Estate & Construction</span>
                <span class="px-6 py-2 border border-brand-gold/50 text-brand-navy rounded-full text-sm font-medium hover:bg-brand-gold hover:text-white transition-colors cursor-pointer">Manufacturing</span>
                <span class="px-6 py-2 border border-brand-gold/50 text-brand-navy rounded-full text-sm font-medium hover:bg-brand-gold hover:text-white transition-colors cursor-pointer">Technology & Cyber</span>
                <span class="px-6 py-2 border border-brand-gold/50 text-brand-navy rounded-full text-sm font-medium hover:bg-brand-gold hover:text-white transition-colors cursor-pointer">Professional Services</span>
                <span class="px-6 py-2 border border-brand-gold/50 text-brand-navy rounded-full text-sm font-medium hover:bg-brand-gold hover:text-white transition-colors cursor-pointer">Transportation</span>
            </div>
        </div>
    </section>

    <!-- Content -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-16 mb-24">
            <div class="lg:col-span-1">
                <h2 class="text-4xl font-bold text-brand-navy heading-serif mb-6">Enterprise Risk Management</h2>
                <p class="text-gray-600 leading-relaxed mb-6">We do not simply sell policies; we engineer holistic risk architectures. Our commercial team conducts exhaustive audits of your operational exposures to design defenses that protect your balance sheet and satisfy board-level scrutiny.</p>
                <div class="p-6 bg-brand-navy text-white rounded-sm mt-8 relative overflow-hidden">
                    <div class="absolute -right-4 -bottom-4 opacity-10">
                        <i class="fas fa-chart-pie text-9xl text-brand-gold"></i>
                    </div>
                    <h4 class="text-brand-gold font-serif text-lg mb-2 relative z-10">Did You Know?</h4>
                    <p class="text-sm font-light text-gray-300 relative z-10">Over 60% of mid-market enterprises are underinsured in areas of Cyber Liability and Business Interruption. We close these gaps.</p>
                </div>
            </div>
            
            <div class="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-16">
                <div id="liability" class="border-t-2 border-brand-gold pt-6">
                    <div class="w-10 h-10 bg-brand-light text-brand-navy rounded flex items-center justify-center text-lg mb-4"><i class="fas fa-balance-scale"></i></div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3">General Liability & D&O</h3>
                    <p class="text-gray-600 mb-4 text-sm leading-relaxed">Protect your balance sheet from litigation. We craft robust liability shields including Directors & Officers, Errors & Omissions, and comprehensive Cyber Liability protection.</p>
                </div>

                <div id="property" class="border-t-2 border-brand-gold pt-6">
                    <div class="w-10 h-10 bg-brand-light text-brand-navy rounded flex items-center justify-center text-lg mb-4"><i class="fas fa-building"></i></div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3">Commercial Property</h3>
                    <p class="text-gray-600 mb-4 text-sm leading-relaxed">Comprehensive coverage for real estate portfolios, manufacturing facilities, and corporate headquarters against physical loss, equipment breakdown, and business interruption.</p>
                </div>

                <div id="contractors" class="border-t-2 border-brand-gold pt-6">
                    <div class="w-10 h-10 bg-brand-light text-brand-navy rounded flex items-center justify-center text-lg mb-4"><i class="fas fa-hard-hat"></i></div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3">Contractors & Development</h3>
                    <p class="text-gray-600 mb-4 text-sm leading-relaxed">Wrap-up liability, course of construction, and rigorous surety bonding solutions tailored for large-scale development projects and elite trade contractors.</p>
                </div>

                 <div id="fleet" class="border-t-2 border-brand-gold pt-6">
                    <div class="w-10 h-10 bg-brand-light text-brand-navy rounded flex items-center justify-center text-lg mb-4"><i class="fas fa-truck"></i></div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-3">Commercial Fleet</h3>
                    <p class="text-gray-600 mb-4 text-sm leading-relaxed">Optimized fleet insurance programs offering extensive liability limits, cargo protection, and streamlined claims management to keep your logistics network moving.</p>
                </div>
            </div>
        </div>

    </main>
    
    <!-- CTA Banner -->
    <section class="bg-gray-100 py-16 border-t border-gray-200">
        <div class="max-w-4xl mx-auto text-center px-4">
            <h2 class="text-3xl font-bold text-brand-navy heading-serif mb-6">Ready to secure your enterprise?</h2>
            <p class="text-gray-600 mb-8 text-lg">Request a confidential, comprehensive audit of your current commercial policies.</p>
            <a href="contact.html" class="inline-block bg-brand-navy text-white px-8 py-4 rounded-sm font-medium text-sm uppercase tracking-wider hover:bg-brand-gold transition-colors duration-300 shadow-lg">Schedule Commercial Audit</a>
        </div>
    </section>
        """
    },
    "about-us.html": {
        "title": "Our Firm | Freedman Broker",
        "active": "about",
        "content": """
    <!-- Page Header -->
    <div class="bg-brand-navy py-24 relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-20 -mr-20 w-96 h-96 border border-brand-gold/20 rounded-full opacity-50"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">The Firm</span>
            <h1 class="text-5xl md:text-6xl font-bold text-white heading-serif mb-6">Heritage & Excellence</h1>
            <p class="text-xl text-gray-400 max-w-2xl mx-auto font-light">Decades of uncompromising advocacy for our clients.</p>
        </div>
    </div>

    <main class="flex-grow max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div class="flex flex-col lg:flex-row gap-16 items-center mb-24">
            <div class="lg:w-1/2">
                <div class="relative p-6 bg-white shadow-2xl rounded-sm border border-gray-100">
                    <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Boardroom" class="rounded-sm w-full h-[500px] object-cover grayscale">
                    <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-brand-gold rounded-sm -z-10"></div>
                </div>
            </div>
            <div class="lg:w-1/2">
                <h2 class="text-4xl font-bold text-brand-navy heading-serif mb-8">Redefining the Brokerage Experience</h2>
                <p class="text-lg text-gray-600 mb-6 font-light leading-relaxed">
                    Freedman Broker Insurance was established on a singular premise: complex wealth and enterprise risk require more than an algorithm. They require a dedicated advocate.
                </p>
                <p class="text-lg text-gray-600 mb-10 font-light leading-relaxed">
                    We eschew the volume-driven models of modern insurance in favor of a boutique approach. Our advisors operate as an extension of your financial and legal teams, curating bespoke portfolios from the world's most elite underwriting syndicates.
                </p>
                
                <div class="border-l-4 border-brand-gold pl-6 py-4 mb-8 bg-gray-50 rounded-r-md">
                    <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2">Unbiased Advocacy</h3>
                    <p class="text-gray-600 text-sm">As an independent firm, our allegiance is solely to our clients. In the event of a claim, our dedicated in-house counsel and adjusters negotiate fiercely on your behalf.</p>
                </div>
            </div>
        </div>
        
        <!-- Leadership Section -->
        <div class="mb-24">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-brand-navy heading-serif mb-4">Leadership</h2>
                <div class="w-16 h-0.5 bg-brand-gold mx-auto"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto">
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-6 border-4 border-white shadow-xl">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="CEO" class="w-full h-full object-cover grayscale">
                    </div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif">Richard Freedman</h3>
                    <p class="text-brand-gold text-sm font-medium tracking-widest uppercase mb-4">Founder & CEO</p>
                    <p class="text-gray-600 text-sm">With over 30 years in corporate risk management, Richard guides the strategic vision of the firm.</p>
                </div>
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-6 border-4 border-white shadow-xl">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Partner" class="w-full h-full object-cover grayscale">
                    </div>
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif">Sarah Jenkins</h3>
                    <p class="text-brand-gold text-sm font-medium tracking-widest uppercase mb-4">Managing Partner</p>
                    <p class="text-gray-600 text-sm">Sarah oversees the Private Wealth division, specializing in ultra-high-net-worth portfolio design.</p>
                </div>
            </div>
        </div>

        <!-- Core Values Grid -->
        <div class="bg-brand-navy text-white rounded-sm p-12 md:p-16 shadow-2xl relative overflow-hidden">
            <div class="absolute -left-20 -top-20 opacity-5">
                <i class="fas fa-landmark text-[20rem]"></i>
            </div>
            <div class="relative z-10">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold heading-serif mb-4">Our Foundational Pillars</h2>
                    <div class="w-16 h-0.5 bg-brand-gold mx-auto"></div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
                    <div>
                        <div class="w-16 h-16 rounded-full border border-brand-gold flex items-center justify-center mx-auto mb-6 bg-brand-navy">
                            <i class="fas fa-gem text-brand-gold text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold heading-serif mb-3">Excellence</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">We demand perfection in policy architecture, leaving no exposure unaddressed and no detail overlooked.</p>
                    </div>
                    <div>
                        <div class="w-16 h-16 rounded-full border border-brand-gold flex items-center justify-center mx-auto mb-6 bg-brand-navy">
                            <i class="fas fa-handshake text-brand-gold text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold heading-serif mb-3">Integrity</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">Absolute transparency in pricing, coverage limitations, and carrier relationships. We serve only you.</p>
                    </div>
                    <div>
                        <div class="w-16 h-16 rounded-full border border-brand-gold flex items-center justify-center mx-auto mb-6 bg-brand-navy">
                            <i class="fas fa-shield-alt text-brand-gold text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold heading-serif mb-3">Tenacity</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">When claims arise, we act swiftly and aggressively to ensure maximum compensation and minimal disruption.</p>
                    </div>
                </div>
            </div>
        </div>
    </main>
        """
    },
    "contact.html": {
        "title": "Contact | Freedman Broker",
        "active": "contact",
        "content": """
    <!-- Page Header -->
    <div class="bg-brand-navy py-24 relative overflow-hidden">
        <div class="absolute top-0 right-0 -mt-20 -mr-20 w-96 h-96 border border-brand-gold/20 rounded-full opacity-50"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <span class="text-brand-gold font-medium tracking-[0.2em] uppercase text-xs block mb-4">Connect With Us</span>
            <h1 class="text-5xl md:text-6xl font-bold text-white heading-serif mb-6">Private Consultation</h1>
            <p class="text-xl text-gray-400 max-w-2xl mx-auto font-light">Discreet, professional, and entirely tailored to your requirements.</p>
        </div>
    </div>

    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div class="grid grid-cols-1 lg:grid-cols-5 gap-16">
            
            <!-- Contact Info -->
            <div class="lg:col-span-2">
                <div class="bg-white p-10 shadow-xl rounded-sm border border-gray-100 h-full">
                    <h3 class="text-2xl font-bold text-brand-navy heading-serif mb-8">Executive Office</h3>
                    
                    <div class="space-y-8">
                        <div>
                            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-2">Location</p>
                            <p class="text-gray-800 font-medium leading-relaxed">123 Financial District<br>Suite 4000<br>Toronto, ON M1M 1M1</p>
                        </div>
                        
                        <div>
                            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-2">Direct Lines</p>
                            <p class="text-gray-800 font-medium mb-1">T: <a href="tel:18005550199" class="hover:text-brand-gold transition-colors">1-800-555-0199</a></p>
                            <p class="text-gray-800 font-medium mb-1">F: 1-800-555-0198</p>
                            <p class="text-gray-800 font-medium">E: <a href="mailto:info@freedmanbroker.com" class="hover:text-brand-gold transition-colors">info@freedmanbroker.com</a></p>
                        </div>

                        <div>
                            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-2">Hours</p>
                            <p class="text-gray-800 font-medium">Mon-Fri: 8:30 AM - 5:30 PM</p>
                            
                            <div class="mt-6 p-4 bg-gray-50 border-l-2 border-brand-gold">
                                <p class="text-brand-navy font-semibold text-sm mb-1">24/7 Concierge Support</p>
                                <p class="text-gray-500 text-xs">Immediate claims assistance available exclusively for active clients.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Contact Form -->
            <div class="lg:col-span-3">
                <form class="bg-white p-10 shadow-xl rounded-sm border border-gray-100">
                    <h2 class="text-2xl font-bold text-brand-navy heading-serif mb-8">Request a Portfolio Review</h2>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="first-name">First Name</label>
                            <input type="text" id="first-name" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors" required>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="last-name">Last Name</label>
                            <input type="text" id="last-name" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors" required>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="email">Email Address</label>
                            <input type="email" id="email" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors" required>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="phone">Phone Number</label>
                            <input type="tel" id="phone" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors">
                        </div>
                    </div>

                    <div class="mb-8">
                        <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="interest">Area of Interest</label>
                        <select id="interest" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors text-gray-700">
                            <option>Personal Wealth & Estate</option>
                            <option>Commercial Enterprise</option>
                            <option>Executive Liability</option>
                            <option>General Inquiry</option>
                        </select>
                    </div>
                    
                    <div class="mb-8">
                        <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="message">Message (Optional)</label>
                        <textarea id="message" rows="3" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors resize-none"></textarea>
                    </div>

                    <button type="button" class="bg-brand-navy hover:bg-brand-gold text-white font-medium text-sm uppercase tracking-wider py-4 px-8 rounded-sm transition duration-300 w-full sm:w-auto shadow-md">
                        Submit Inquiry
                    </button>
                </form>
            </div>

        </div>
    </main>
        """
    }
}

for filename, data in PAGES.items():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>{data['title']}</title>
    {HEAD_TAGS}
</head>
<body class="antialiased flex flex-col min-h-screen" data-page="{data['active']}">
    <div id="global-header"></div>
    {data['content']}
    <div id="global-footer"></div>
</body>
</html>"""
    
    with open(filename, "w") as f:
        f.write(html)

print("Build complete.")
