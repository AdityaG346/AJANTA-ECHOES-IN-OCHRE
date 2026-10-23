/**
 * AJANTA: ECHOES IN OCHRE — NAVIGATION MODULE
 * Accessible navigation, mobile drawer, scroll states & active links
 */

export function initNavigation() {
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const primaryNav = document.getElementById('primary-nav');
  const navLinks = document.querySelectorAll('.nav-link');
  const backToTopBtn = document.getElementById('back-to-top');

  // Sticky header background state on scroll
  const handleScroll = () => {
    if (window.scrollY > 40) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // Mobile menu drawer open/close
  const toggleMenu = (open) => {
    const isCurrentlyOpen = menuToggle?.getAttribute('aria-expanded') === 'true';
    const shouldOpen = open !== undefined ? open : !isCurrentlyOpen;

    menuToggle?.setAttribute('aria-expanded', String(shouldOpen));
    primaryNav?.classList.toggle('is-open', shouldOpen);

    if (shouldOpen) {
      // Focus first link in drawer
      const firstLink = primaryNav?.querySelector('a');
      firstLink?.focus();
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
      menuToggle?.focus();
    }
  };

  menuToggle?.addEventListener('click', () => toggleMenu());

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && primaryNav?.classList.contains('is-open')) {
      toggleMenu(false);
    }
  });

  // Close on link click
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (primaryNav?.classList.contains('is-open')) {
        toggleMenu(false);
      }
    });
  });

  // Smooth scroll for Back to Top
  backToTopBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
    });
  });

  // Highlight active section link on scroll
  const sections = document.querySelectorAll('section[id]');
  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -60% 0px',
    threshold: 0
  };

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach((link) => {
          const href = link.getAttribute('href');
          if (href === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach((sec) => navObserver.observe(sec));
}
