# DESIGN SYSTEM — EXACT SPECIFICATION

## Palette
```css
:root {
  --cave:#17130F; --cave-deep:#100D0A; --umber:#34241C;
  --terracotta:#A84F32; --ochre:#C99A43; --sage:#68765A;
  --parchment:#E6D2AD; --rose:#A96F66; --muted:#B7A58B;
  --line:rgba(201,154,67,.28);
  --content:1160px; --reading:64ch;
  --space-section:clamp(76px,10vw,140px);
}
```
Use dark base and sparing highlights; check contrast for every text/background combination. Accent colours are not automatically accessible for small text.

## Typography
- Display: **Cormorant Garamond** (fallback Georgia, serif), weight 500–600.
- Body/UI: **Inter** (fallback Arial, sans-serif), weight 400–600.
- Eyebrows: Inter 11–13px, uppercase, letter-spacing .16em, semibold.
- Hero H1: `clamp(3.5rem, 7.5vw, 7.5rem)` with tight line-height 0.98–1.05, never overlapping artwork.
- Section H2: `clamp(2.7rem, 5vw, 5rem)`, line-height ~1.08.
- Scene H3: `clamp(2.5rem, 4.5vw, 4.75rem)`.
- Body: `clamp(1rem, 1.1vw, 1.125rem)`; line-height 1.7; max 64ch.
- Captions: 12–14px, line-height 1.5.
- Avoid fully justified text and long centred paragraphs.

## Grid and spacing
- Container width: min(1160px, calc(100% - 40px)) on mobile, wider side margins desktop.
- Section spacing: `clamp(76px,10vw,140px)`.
- Hero: desktop 2-column 52/48 or an editorial image composition with text in a safe dark region; mobile stacks.
- Story: alternating image/text 55/45, gap 48–80px; mobile single column, image first.
- Historical photos may use a full-width feature frame; avoid five identical rectangles.
- Frames: 1px low-opacity ochre; corners 0–8px, not oversized rounding.
- Texture: very faint local plaster overlay, opacity roughly 0.04–0.09; never reduce legibility.

## Header and footer
Sticky translucent dark header with subtle border, left brand wordmark, right links Story / Ajanta / Reimagined / Sources, active scene text. Height approx 70–78px desktop. Mobile collapses to accessible menu. Footer shows project name, course/team placeholders, source link and back-to-top link.

## UI rules
One terracotta primary CTA. Text links underlined on hover/focus. Use consistent outline SVG icons (Lucide permitted), not emoji. Keyboard focus ring uses parchment/ochre contrast. Add skip-to-content. No dead links, auto-playing audio, or fake interactions.

## Responsive breakpoints
- 320–599: single column, compact header, 20px gutters.
- 600–899: stacked scenes or flexible two-column where legible.
- 900+: alternating editorial scene layouts.
- 1200+: max width enforced, no excessive text measure.
Test at 320, 375, 768, 1024 and 1440px plus 200% zoom.
