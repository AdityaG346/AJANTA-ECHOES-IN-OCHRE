# MOTION SPECIFICATION — GSAP + SCROLLTRIGGER

## Philosophy
Animate revelation, not spectacle. Make paintings feel discovered. Preserve normal scrolling, never trap the reader in a pinned section. Respect reduced motion.

## Exact motion plan
- Hero: eyebrow, headline, subtitle, CTA appear sequentially with opacity 0→1 and translateY 20→0, total approximately 1.0–1.4s; no long delays.
- Hero artwork: separate low-amplitude transform/clip reveal; no overlap with title.
- Intro context: one fade/translate reveal; historical photograph remains stable for inspection.
- Each story scene: art fades/translateY 20px; copy follows ~0.1–0.2s later; no large zoom or dramatic rotation.
- Scene 3: optional restrained frame-darkening to signal betrayal, without hiding text.
- Scene 5: return of opening tree motif and warm palette, gentle reveal.
- Progress: textual `SCENE 01 / 05` plus thin ochre bar, updated by IntersectionObserver or ScrollTrigger onEnter/onEnterBack.
- Hover: artwork scale <= 1.02; no hover-only information.
- Links: smooth anchor scroll unless reduced motion.

## GSAP integration
Check for `window.gsap` and `window.ScrollTrigger` before registration. Use `gsap.registerPlugin(ScrollTrigger)` only when present. For `.story-scene`, create timelines with ScrollTrigger `start: 'top 80%'`, `once: true` for simple reveals. Prefer CSS class-based fallbacks if GSAP is missing. Do not combine conflicting CSS/GSAP transforms on the same node.

## Progressive enhancement
HTML is fully visible by default. Only add animation-ready classes after JS confirms its animation mechanism is available. If GSAP or ScrollTrigger fails, reveal content and keep navigation functional. No hard dependency on network-hosted animation code.

## Reduced motion
```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior:auto; }
  *,*::before,*::after {
    animation-duration:.01ms!important;
    animation-iteration-count:1!important;
    transition-duration:.01ms!important;
  }
}
```
JS must check `matchMedia('(prefers-reduced-motion: reduce)')` and skip non-essential GSAP timelines.

## Interaction acceptance
CTA scrolls to story; header links target correct sections; mobile menu works with keyboard and touch; story progress updates in both scroll directions; image credits open real source links; back-to-top works. Do not invent a lightbox unless actually implementing it.
