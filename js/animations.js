/**
 * AJANTA: ECHOES IN OCHRE — ANIMATION MODULE
 * Purposeful reveals using GSAP 3 + ScrollTrigger with robust progressive enhancement
 */

export function initAnimations() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // If reduced motion is requested by user, respect immediately and skip timelines
  if (prefersReducedMotion) {
    document.documentElement.classList.add('reduced-motion');
    return;
  }

  const hasGSAP = typeof window.gsap !== 'undefined';
  const hasScrollTrigger = typeof window.ScrollTrigger !== 'undefined';

  if (!hasGSAP) {
    console.info('GSAP not detected; content remains fully visible and accessible via semantic HTML & CSS.');
    return;
  }

  // Register ScrollTrigger if available
  if (hasScrollTrigger) {
    window.gsap.registerPlugin(window.ScrollTrigger);
  }

  // Signal to CSS that animation mechanism is active
  document.documentElement.classList.add('js-motion-ready');

  const { gsap } = window;

  // 1. Hero Reveal Timeline
  const heroTL = gsap.timeline({ defaults: { ease: 'power2.out' } });

  heroTL
    .fromTo(
      '.hero-eyebrow',
      { opacity: 0, y: 16 },
      { opacity: 1, y: 0, duration: 0.6, delay: 0.2 }
    )
    .fromTo(
      '.hero-title',
      { opacity: 0, y: 22 },
      { opacity: 1, y: 0, duration: 0.8 },
      '-=0.4'
    )
    .fromTo(
      '.hero-subtitle',
      { opacity: 0, y: 18 },
      { opacity: 1, y: 0, duration: 0.7 },
      '-=0.5'
    )
    .fromTo(
      '.hero-actions',
      { opacity: 0, y: 16 },
      { opacity: 1, y: 0, duration: 0.6 },
      '-=0.4'
    )
    .fromTo(
      '.hero-microcopy',
      { opacity: 0 },
      { opacity: 1, duration: 0.5 },
      '-=0.3'
    )
    .fromTo(
      '.hero-artwork',
      { opacity: 0, scale: 0.98, y: 15 },
      { opacity: 1, scale: 1, y: 0, duration: 0.9 },
      '-=0.7'
    );

  // 2. ScrollTrigger reveals for Narrative Scenes & Content Sections
  if (hasScrollTrigger) {
    // Reveal for About Ajanta section
    gsap.fromTo(
      '.ajanta-text-column',
      { opacity: 0, y: 24 },
      {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '#ajanta',
          start: 'top 80%',
          once: true
        }
      }
    );

    gsap.fromTo(
      '.ajanta-media-column .artwork-wrapper',
      { opacity: 0, y: 28 },
      {
        opacity: 1,
        y: 0,
        duration: 0.85,
        stagger: 0.2,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '.ajanta-media-column',
          start: 'top 82%',
          once: true
        }
      }
    );

    // Reveal each story scene cleanly without scroll trapping
    const sceneArticles = document.querySelectorAll('.story-scene');
    sceneArticles.forEach((scene) => {
      const media = scene.querySelector('.scene-media');
      const text = scene.querySelector('.scene-text-content');

      const sceneTL = gsap.timeline({
        scrollTrigger: {
          trigger: scene,
          start: 'top 80%',
          once: true
        }
      });

      sceneTL
        .fromTo(
          media,
          { opacity: 0, y: 24 },
          { opacity: 1, y: 0, duration: 0.75, ease: 'power2.out' }
        )
        .fromTo(
          text,
          { opacity: 0, y: 20 },
          { opacity: 1, y: 0, duration: 0.75, ease: 'power2.out' },
          '-=0.55'
        );
    });

    // Reveal values cards in reflection
    gsap.fromTo(
      '.value-card',
      { opacity: 0, y: 24 },
      {
        opacity: 1,
        y: 0,
        duration: 0.7,
        stagger: 0.15,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '.values-grid',
          start: 'top 85%',
          once: true
        }
      }
    );

    // Reveal sources catalog cards
    gsap.fromTo(
      '.source-card',
      { opacity: 0, y: 20 },
      {
        opacity: 1,
        y: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '.sources-catalog',
          start: 'top 88%',
          once: true
        }
      }
    );
  }
}
