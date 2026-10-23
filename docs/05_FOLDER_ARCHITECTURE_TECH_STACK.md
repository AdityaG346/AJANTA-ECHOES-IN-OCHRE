# FINAL TECH STACK, FOLDER STRUCTURE AND ARCHITECTURE

## Approved stack
- HTML5: semantic sections, captions, navigation and credits.
- CSS3: tokens, layout, textures, media queries and fallback transitions.
- Vanilla JS (ES modules): navigation, story progress, reduced-motion handling, interaction.
- GSAP 3 + ScrollTrigger: selected editorial scroll animations. Pin a tested version and load GSAP before registering ScrollTrigger; prefer local vendor files for stable offline use, subject to distribution terms.
- IntersectionObserver: lightweight scene visibility/progress fallback.
- SVG and WebP/JPEG: original scene artwork and real historical photographs.
- Figma/Krita/Inkscape: planning and illustration production.
- Git + GitHub: collaboration. GitHub Pages or Netlify: deployment.
- No React/Vite/backend/database/build system required.

## Folder tree
```
ajanta-echoes-in-ochre/
├── index.html
├── README.md
├── SOURCES_AND_CREDITS.md
├── .gitignore
├── css/
│   ├── style.css
│   ├── animations.css
│   └── responsive.css
├── js/
│   ├── main.js
│   ├── navigation.js
│   ├── animations.js
│   └── story-progress.js
├── assets/
│   ├── images/
│   │   ├── ajanta-cave-context.webp
│   │   ├── ajanta-mural-reference.webp
│   │   └── ajanta-hero.webp
│   ├── illustrations/
│   │   ├── scene-01-forest.svg
│   │   ├── scene-02-stranger.svg
│   │   ├── scene-03-betrayal.svg
│   │   ├── scene-04-palace.svg
│   │   └── scene-05-return.svg
│   ├── textures/
│   │   └── cave-plaster.webp
│   ├── icons/
│   └── vendor/              # optional pinned GSAP distribution files
└── docs/
    ├── 00_AGENT_START_HERE.md
    ├── 01_CREATIVE_DIRECTION.md
    ├── 02_DESIGN_TOKENS_TYPOGRAPHY_LAYOUT.md
    ├── 03_FINAL_COPY_AND_STORYBOARD.md
    ├── 04_HISTORICAL_RESEARCH_IMAGE_PIPELINE.md
    ├── 05_FOLDER_ARCHITECTURE_TECH_STACK.md
    ├── 06_MOTION_INTERACTIONS.md
    ├── 07_ACCESSIBILITY_PERFORMANCE_QA.md
    ├── 08_IMPLEMENTATION_ROADMAP.md
    └── 09_MASTER_AGENT_PROMPT.md
```
Names for downloaded image assets are *targets*, not proof files already exist. Never leave a broken reference if an asset is unavailable.

## HTML landmarks/IDs
`header` → `nav` → `main#main` → `section#hero` → `section#ajanta` → `section#story` containing `article#scene-1` ... `article#scene-5` → `section#reimagined` → `section#sources` → `footer`.

## JS responsibility boundaries
- `main.js`: initialise on DOM ready; register GSAP only if available; coordinate modules.
- `navigation.js`: mobile menu, `aria-expanded`, Escape-to-close, focus handling, active nav.
- `animations.js`: GSAP timeline definitions, ScrollTrigger refresh and reduced-motion fallback.
- `story-progress.js`: observer on five scenes, update `SCENE XX / 05`, optionally progress bar; do not overrun scroll handlers.

## Import strategy
Use `<script type="module" src="js/main.js"></script>` and ES imports for your own modules. Include pinned GSAP scripts before module startup or import locally with correct paths. Test using a local HTTP server (ES modules may not work correctly from `file://`).

## Development server
From root: `python -m http.server 5500`, then open `http://localhost:5500`. Alternatively VS Code Live Server. Deployment is static.
