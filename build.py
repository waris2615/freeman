import os

# --- SHARED COMPONENTS ---

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
"""

HEADER = """
    <!-- Top Bar -->
    <div class="bg-brand-navy text-gray-300 text-xs sm:text-sm py-2 px-4 sm:px-6 lg:px-8 flex justify-between items-center border-b border-gray-800">
        <div class="flex space-x-6">
            <span class="flex items-center"><i class="fas fa-phone-alt mr-2 gold-accent"></i> 1-800-555-0199</span>
            <span class="hidden sm:flex items-center"><i class="fas fa-envelope mr-2 gold-accent"></i> info@freedmanbroker.com</span>
        </div>
        <div class="flex space-x-5">
            <a href="#" class="hover:text-brand-gold transition-colors duration-300"><i class="fab fa-linkedin-in"></i></a>
            <a href="#" class="hover:text-brand-gold transition-colors duration-300"><i class="fab fa-twitter"></i></a>
        </div>
    </div>

    <!-- Main Navigation -->
    <header class="bg-white shadow-sm sticky top-0 z-50" x-data="{{ mobileMenuOpen: false }}">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-24">
                <!-- Logo -->
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center group">
                        <div class="w-10 h-10 bg-brand-navy flex items-center justify-center rounded-sm mr-3 group-hover:bg-brand-gold transition-colors duration-300">
                            <i class="fas fa-shield-alt text-white text-xl"></i>
                        </div>
                        <div>
                            <div class="text-2xl font-bold text-brand-navy tracking-tight heading-serif leading-none">Freedman Broker</div>
                            <div class="text-[0.65rem] uppercase tracking-[0.2em] text-gray-500 mt-1">Premium Insurance Services</div>
                        </div>
                    </a>
                </div>

                <!-- Desktop Menu -->
                <nav class="hidden md:flex space-x-8 h-full items-center">
                    <a href="index.html" class="text-gray-800 font-medium text-sm uppercase tracking-wide nav-link {active_home}">Home</a>
                    
                    <!-- Personal Dropdown -->
                    <div class="relative flex items-center h-full group" x-data="{{ open: false }}" @mouseenter="open = true" @mouseleave="open = false">
                        <a href="personal-insurance.html" class="text-gray-800 font-medium text-sm uppercase tracking-wide nav-link flex items-center {active_personal}">
                            Personal <i class="fas fa-chevron-down text-[0.6rem] ml-1.5 mt-0.5 text-gray-400 group-hover:text-brand-gold transition-colors"></i>
                        </a>
                        <div x-show="open" x-transition.opacity.duration.200ms class="absolute top-[80%] left-0 w-64 bg-white shadow-xl border border-gray-100 rounded-sm overflow-hidden py-2 z-50" style="display: none;">
                            <a href="personal-insurance.html#auto" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Automobile Insurance</a>
                            <a href="personal-insurance.html#home" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Home & Estate</a>
                            <a href="personal-insurance.html#life" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Life & Health</a>
                            <a href="personal-insurance.html#travel" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Travel Coverage</a>
                        </div>
                    </div>

                    <!-- Commercial Dropdown -->
                    <div class="relative flex items-center h-full group" x-data="{{ open: false }}" @mouseenter="open = true" @mouseleave="open = false">
                        <a href="commercial-insurance.html" class="text-gray-800 font-medium text-sm uppercase tracking-wide nav-link flex items-center {active_commercial}">
                            Commercial <i class="fas fa-chevron-down text-[0.6rem] ml-1.5 mt-0.5 text-gray-400 group-hover:text-brand-gold transition-colors"></i>
                        </a>
                        <div x-show="open" x-transition.opacity.duration.200ms class="absolute top-[80%] left-0 w-64 bg-white shadow-xl border border-gray-100 rounded-sm overflow-hidden py-2 z-50" style="display: none;">
                            <a href="commercial-insurance.html#liability" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">General Liability</a>
                            <a href="commercial-insurance.html#property" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Commercial Property</a>
                            <a href="commercial-insurance.html#contractors" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Contractors & Trades</a>
                            <a href="commercial-insurance.html#fleet" class="block px-6 py-3 text-sm text-gray-600 hover:bg-gray-50 hover:text-brand-navy hover:pl-8 transition-all duration-300">Fleet & Auto</a>
                        </div>
                    </div>

                    <a href="about-us.html" class="text-gray-800 font-medium text-sm uppercase tracking-wide nav-link {active_about}">Our Firm</a>
                    <a href="contact.html" class="text-gray-800 font-medium text-sm uppercase tracking-wide nav-link {active_contact}">Contact</a>
                </nav>

                <!-- CTA Button -->
                <div class="hidden md:flex items-center">
                    <a href="contact.html" class="bg-brand-navy hover:bg-brand-gold text-white px-7 py-2.5 rounded-sm font-medium text-sm tracking-wide transition-colors duration-300 shadow-md">
                        Request Quote
                    </a>
                </div>

                <!-- Mobile menu button -->
                <div class="flex items-center md:hidden">
                    <button @click="mobileMenuOpen = !mobileMenuOpen" type="button" class="text-brand-navy hover:text-brand-gold focus:outline-none transition-colors">
                        <i class="fas fa-bars text-2xl" x-show="!mobileMenuOpen"></i>
                        <i class="fas fa-times text-2xl" x-show="mobileMenuOpen" x-cloak></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div x-show="mobileMenuOpen" class="md:hidden bg-white border-t border-gray-100 shadow-inner absolute w-full z-50" x-transition style="display: none;">
            <div class="px-4 pt-4 pb-6 space-y-2">
                <a href="index.html" class="block px-3 py-3 text-sm uppercase tracking-wide font-medium text-gray-900 hover:bg-gray-50 border-l-2 border-transparent hover:border-brand-gold">Home</a>
                <a href="personal-insurance.html" class="block px-3 py-3 text-sm uppercase tracking-wide font-medium text-gray-900 hover:bg-gray-50 border-l-2 border-transparent hover:border-brand-gold">Personal Insurance</a>
                <a href="commercial-insurance.html" class="block px-3 py-3 text-sm uppercase tracking-wide font-medium text-gray-900 hover:bg-gray-50 border-l-2 border-transparent hover:border-brand-gold">Commercial Insurance</a>
                <a href="about-us.html" class="block px-3 py-3 text-sm uppercase tracking-wide font-medium text-gray-900 hover:bg-gray-50 border-l-2 border-transparent hover:border-brand-gold">Our Firm</a>
                <a href="contact.html" class="block px-3 py-3 text-sm uppercase tracking-wide font-medium text-gray-900 hover:bg-gray-50 border-l-2 border-transparent hover:border-brand-gold">Contact</a>
            </div>
        </div>
    </header>
"""

FOOTER = """
    <!-- Footer -->
    <footer class="bg-brand-navy text-white mt-auto pt-20 pb-10 border-t-4 border-gold-accent">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
                <!-- Brand Info -->
                <div class="md:col-span-4">
                    <a href="index.html" class="flex items-center mb-6">
                        <div class="w-8 h-8 bg-brand-gold flex items-center justify-center rounded-sm mr-3">
                            <i class="fas fa-shield-alt text-brand-navy text-sm"></i>
                        </div>
                        <div>
                            <div class="text-xl font-bold text-white tracking-tight heading-serif leading-none">Freedman Broker</div>
                        </div>
                    </a>
                    <p class="text-gray-400 text-sm leading-relaxed mb-6 max-w-sm">
                        An elite independent insurance brokerage dedicated to providing bespoke coverage solutions with uncompromising integrity and service.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-8 h-8 rounded-full bg-gray-800 flex items-center justify-center text-gray-400 hover:bg-brand-gold hover:text-white transition-colors"><i class="fab fa-linkedin-in text-sm"></i></a>
                        <a href="#" class="w-8 h-8 rounded-full bg-gray-800 flex items-center justify-center text-gray-400 hover:bg-brand-gold hover:text-white transition-colors"><i class="fab fa-twitter text-sm"></i></a>
                    </div>
                </div>
                
                <!-- Quick Links -->
                <div class="md:col-span-2 md:col-start-6">
                    <h4 class="text-white font-semibold mb-6 uppercase tracking-wider text-xs">Solutions</h4>
                    <ul class="space-y-3">
                        <li><a href="personal-insurance.html" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Personal Lines</a></li>
                        <li><a href="commercial-insurance.html" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Commercial Lines</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Request Quote</a></li>
                    </ul>
                </div>

                <!-- Firm -->
                <div class="md:col-span-2">
                    <h4 class="text-white font-semibold mb-6 uppercase tracking-wider text-xs">The Firm</h4>
                    <ul class="space-y-3">
                        <li><a href="about-us.html" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Our Story</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Careers</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-brand-gold text-sm transition-colors">Privacy Policy</a></li>
                    </ul>
                </div>

                <!-- Contact -->
                <div class="md:col-span-3">
                    <h4 class="text-white font-semibold mb-6 uppercase tracking-wider text-xs">Contact</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start text-gray-400 text-sm">
                            <i class="fas fa-map-marker-alt mt-1 mr-3 text-brand-gold w-4 text-center"></i>
                            <span>123 Financial District<br>Suite 4000<br>Toronto, ON M1M 1M1</span>
                        </li>
                        <li class="flex items-center text-gray-400 text-sm">
                            <i class="fas fa-phone-alt mr-3 text-brand-gold w-4 text-center"></i>
                            <a href="tel:18005550199" class="hover:text-white transition-colors">1-800-555-0199</a>
                        </li>
                        <li class="flex items-center text-gray-400 text-sm">
                            <i class="fas fa-envelope mr-3 text-brand-gold w-4 text-center"></i>
                            <a href="mailto:info@freedmanbroker.com" class="hover:text-white transition-colors">info@freedmanbroker.com</a>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-xs tracking-wide">
                <p>&copy; 2024 Freedman Broker Insurance. All rights reserved.</p>
                <p class="mt-2 md:mt-0">Licensed across Ontario, Canada.</p>
            </div>
        </div>
    </footer>
"""

# --- PAGE CONTENT ---

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
                <div class="group cursor-pointer">
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
                <div class="group cursor-pointer">
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

    <!-- Trust Banner -->
    <section class="py-16 bg-white border-y border-gray-100">
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

    </main>
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

    <!-- Content -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-20">
            
            <div id="liability" class="border-t border-gray-200 pt-8">
                <div class="w-12 h-12 bg-brand-navy text-brand-gold rounded-sm flex items-center justify-center text-xl mb-6 shadow-md"><i class="fas fa-balance-scale"></i></div>
                <h2 class="text-2xl font-bold text-brand-navy heading-serif mb-4">General Liability & D&O</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Protect your balance sheet from litigation. We craft robust liability shields including Directors & Officers, Errors & Omissions, and Cyber Liability.</p>
                <a href="contact.html" class="text-sm font-semibold uppercase tracking-wider text-brand-navy hover:text-brand-gold transition-colors">Inquire &rarr;</a>
            </div>

            <div id="property" class="border-t border-gray-200 pt-8">
                <div class="w-12 h-12 bg-brand-navy text-brand-gold rounded-sm flex items-center justify-center text-xl mb-6 shadow-md"><i class="fas fa-building"></i></div>
                <h2 class="text-2xl font-bold text-brand-navy heading-serif mb-4">Commercial Property</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Comprehensive coverage for real estate portfolios, manufacturing facilities, and corporate headquarters against physical loss and business interruption.</p>
                <a href="contact.html" class="text-sm font-semibold uppercase tracking-wider text-brand-navy hover:text-brand-gold transition-colors">Inquire &rarr;</a>
            </div>

            <div id="contractors" class="border-t border-gray-200 pt-8">
                <div class="w-12 h-12 bg-brand-navy text-brand-gold rounded-sm flex items-center justify-center text-xl mb-6 shadow-md"><i class="fas fa-hard-hat"></i></div>
                <h2 class="text-2xl font-bold text-brand-navy heading-serif mb-4">Contractors & Development</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Wrap-up liability, course of construction, and surety bonding for large-scale development projects and elite trade contractors.</p>
                <a href="contact.html" class="text-sm font-semibold uppercase tracking-wider text-brand-navy hover:text-brand-gold transition-colors">Inquire &rarr;</a>
            </div>

             <div id="fleet" class="border-t border-gray-200 pt-8">
                <div class="w-12 h-12 bg-brand-navy text-brand-gold rounded-sm flex items-center justify-center text-xl mb-6 shadow-md"><i class="fas fa-truck"></i></div>
                <h2 class="text-2xl font-bold text-brand-navy heading-serif mb-4">Commercial Fleet</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Optimized fleet insurance programs offering extensive liability limits and streamlined claims management to keep your business moving.</p>
                <a href="contact.html" class="text-sm font-semibold uppercase tracking-wider text-brand-navy hover:text-brand-gold transition-colors">Inquire &rarr;</a>
            </div>

        </div>
    </main>
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
        <div class="flex flex-col lg:flex-row gap-16 items-center">
            <div class="lg:w-1/2">
                <div class="relative p-6 bg-white shadow-2xl rounded-sm">
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
                
                <div class="border-l-4 border-brand-gold pl-6 py-2 mb-8">
                    <h3 class="text-xl font-bold text-brand-navy heading-serif mb-2">Unbiased Advocacy</h3>
                    <p class="text-gray-600 text-sm">As an independent firm, our allegiance is solely to our clients. In the event of a claim, our dedicated in-house counsel and adjusters negotiate fiercely on your behalf.</p>
                </div>
                
                <a href="contact.html" class="inline-flex items-center bg-brand-navy text-white px-8 py-3 rounded-sm font-medium text-sm uppercase tracking-wider hover:bg-brand-gold transition-colors duration-300">
                    Schedule a Review
                </a>
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
                            <p class="text-gray-800 font-medium">123 Financial District<br>Suite 4000<br>Toronto, ON M1M 1M1</p>
                        </div>
                        
                        <div>
                            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-2">Direct Lines</p>
                            <p class="text-gray-800 font-medium mb-1">T: 1-800-555-0199</p>
                            <p class="text-gray-800 font-medium">E: info@freedmanbroker.com</p>
                        </div>

                        <div>
                            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-2">Hours</p>
                            <p class="text-gray-800 font-medium">Mon-Fri: 8:30 AM - 5:30 PM</p>
                            <p class="text-brand-gold text-sm mt-2 italic font-serif">24/7 Concierge Claims Support available for active clients.</p>
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
                    
                    <div class="mb-6">
                        <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="email">Email Address</label>
                        <input type="email" id="email" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors" required>
                    </div>

                    <div class="mb-8">
                        <label class="block text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2" for="interest">Area of Interest</label>
                        <select id="interest" class="w-full border-b border-gray-300 bg-transparent py-2 focus:outline-none focus:border-brand-gold transition-colors text-gray-700">
                            <option>Personal Wealth & Estate</option>
                            <option>Commercial Enterprise</option>
                            <option>Executive Liability</option>
                        </select>
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
    
    # Calculate active states
    states = {
        "active_home": "", "active_personal": "", "active_commercial": "", "active_about": "", "active_contact": ""
    }
    states[f"active_{data['active']}"] = "active"

    rendered_header = HEADER.format(**states)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>{data['title']}</title>
    {HEAD_TAGS}
</head>
<body class="antialiased flex flex-col min-h-screen">
{rendered_header}
{data['content']}
{FOOTER}
</body>
</html>"""
    
    with open(filename, "w") as f:
        f.write(html)

print("Build complete.")
