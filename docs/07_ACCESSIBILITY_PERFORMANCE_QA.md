# ACCESSIBILITY, PERFORMANCE AND QA

## Accessibility
- Semantic HTML, single H1, logical heading levels.
- First focusable element is `Skip to content` linking to `#main`.
- Header links and CTA are real anchors; menu uses button with accessible label, `aria-expanded` and controlled panel ID.
- Visible focus ring, minimum comfortable touch targets, keyboard Escape-to-close mobile menu.
- Informative photos have factual alt text; decorative textures have `alt=""` or CSS backgrounds; decorative SVG `aria-hidden="true"`.
- Artwork captions and credit links are accessible as text, not embedded in the image.
- Text contrast verified; no text over detailed artwork without a safe contrast surface.
- `prefers-reduced-motion` respected; no autoplay audio; no animation-gated content.
- Test 200% browser zoom and screen reader landmarks where possible.

## Performance
- Prefer locally stored optimised WebP/JPEG photos; SVG for original vector assets.
- Hero image sized for viewport; `fetchpriority="high"` only if appropriate.
- Below-fold images `loading="lazy"`; set intrinsic width/height or `aspect-ratio` to prevent CLS.
- Limit external font weights and third-party dependencies.
- Avoid huge raster textures, full-screen video, continuous scroll listeners and heavy filters.
- Aim for fast perceived load on a typical student laptop and midrange phone; measure rather than claim scores.

## Test matrix
Viewport widths: 320, 375, 768, 1024, 1440px. Browsers: Chrome/Edge and Firefox. Modes: keyboard-only, reduced motion, JavaScript disabled, slower network, 200% zoom.

## Acceptance checklist
- [ ] Correct brand across browser title, header, hero, footer, README.
- [ ] Hero title fits and does not obscure meaningful artwork.
- [ ] Real Ajanta context images are genuine, sourced and licence-verified, or transparently replaced with placeholders.
- [ ] Five story scenes appear in correct order and use approved copy.
- [ ] No Chaddanta/Vessantara painting falsely attributed to Matri-Poshaka.
- [ ] No childish geometric/cartoon elephant.
- [ ] All image paths resolve; no remote broken thumbnails.
- [ ] Historical photos and modern interpretations clearly labelled.
- [ ] GSAP motion works without scroll trapping; fallback works without GSAP.
- [ ] Reduced motion and no-JS display readable content.
- [ ] Mobile menu and all navigation links function.
- [ ] No horizontal overflow; no illegible small text.
- [ ] Credits include source URL, licence and creator where known.
- [ ] No avoidable browser console errors.
- [ ] README explains running and deployment.

## Final evidence
Take desktop and mobile screenshots, list assets and licences, record actual test results and remaining limitations. Never claim all tests passed unless performed.
