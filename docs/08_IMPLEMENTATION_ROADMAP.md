# END-TO-END IMPLEMENTATION ROADMAP

## Phase 0 — Research gate
Verify Matri-Poshaka narrative from appropriate references. Verify all planned authentic photos at the file level and their licences. Decide image usage based on evidence, not convenience. Record findings in `SOURCES_AND_CREDITS.md`.

## Phase 1 — Asset production
Create/download properly credited historical images for hero and Ajanta context. Create five visually cohesive original story panels using the exact briefs in `01_CREATIVE_DIRECTION.md`. Optimise and store locally. If real-image acquisition is blocked, use labelled original-art fallback and report this explicitly.

## Phase 2 — Semantic skeleton
Create `index.html` with header, hero, Ajanta context, story intro, five article scenes, reflection, interpretation note, sources and footer. Add all exact copy before styling. Verify links and heading hierarchy.

## Phase 3 — Design system
Implement tokens, typography, grid, responsive editorial image layouts, frames, captions, buttons, focus styles and understated textures. Make hero image and text occupy safe zones. Avoid default split-screen sameness by mixing editorial compositions.

## Phase 4 — Interactions
Implement mobile nav and progress indicator. Add GSAP and ScrollTrigger only for purposeful reveals. Ensure fallback with missing library or disabled JS. Add reduced-motion branch.

## Phase 5 — QA and polish
Test 320/375/768/1024/1440 widths, keyboard, zoom, slow network, reduced motion, no JS, image credits and all links. Fix issues before declaring completion.

## Phase 6 — Delivery
Provide full working folder, README, source/credit inventory, preview screenshots if tools allow, and concise setup instructions. Host on GitHub Pages/Netlify if requested and access is available; otherwise explain how to deploy.

## Team of five suggested ownership
1. Research/provenance and source verification.
2. Art direction and cohesive illustrations.
3. HTML/content structure.
4. CSS/responsive/motion.
5. JavaScript/QA/integration.
Everyone jointly reviews final story accuracy and visual consistency.

## Agent operating rule
If a factual or legal question cannot be verified, do not guess. Use a transparent TODO with the exact missing information. Complete all other implementation work.
