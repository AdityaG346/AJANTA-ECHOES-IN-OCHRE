# Ajanta: Echoes in Ochre
### The Living Murals of Ajanta

> **Ancient stories. Timeless lessons. Reimagined.**

A polished, responsive, accessible, single-page digital museum exhibition and five-scene graphic storyboard based on the **Matri-Poshaka Jataka**, inspired by the 5th-century Gupta-Vakataka murals of the UNESCO World Heritage Ajanta Caves in Maharashtra, India.

---

## 🏛️ Project Overview

This project was built from scratch as a college Cave Paintings Storyboard assignment. It combines:
1. **Verified Historical Photography Layer:** High-resolution photographs of authentic Ajanta cave architecture and surviving 5th-century Jataka murals from Cave 17, verified at the file level on Wikimedia Commons with documented open-access licenses (CC0, CC BY 4.0, CC BY 2.0).
2. **Cohesive Narrative Storyboard (Matri-Poshaka Jataka):** Five original, custom-crafted vector narrative panels created specifically for this exhibition according to classical Ajanta artistic traditions—incorporating mineral pigment palettes (red ochre, yellow ochre, raw umber, terra-verte sage, lime plaster), classical Gupta-Vakataka anatomical grace (tribhanga posture, almond lotus-petal eyes), an ancient recurring bent Sal tree motif, and culturally informed 5th-century architecture.
3. **Rigorous Art Provenance & Ethics:** Complete transparency distinguishing historical mural documentation from contemporary interpretations. Explicit clarification distinguishing the *Chaddanta Jataka* elephant iconography from the *Matri-Poshaka Jataka* narrative.
4. **Editorial Web Experience:** Rich, tactile aesthetic built with vanilla technologies (HTML5, CSS3, ES modules, GSAP 3 + ScrollTrigger), featuring alternating editorial layouts, real-time scroll progress tracking, accessible mobile navigation drawer, and full support for reduced-motion and no-JavaScript modes.

---

## 📁 Repository Structure

```
ajanta-echoes-in-ochre/
├── index.html                   # Semantic HTML5 single-page exhibition
├── README.md                    # Project documentation & execution guide
├── SOURCES_AND_CREDITS.md       # Complete asset provenance, licenses & citations
├── .gitignore                   # Standard repository ignores
├── css/
│   ├── style.css                # Design system, color tokens, typography & grid
│   ├── animations.css           # Purposeful motion, micro-interactions & reduced-motion
│   └── responsive.css           # Breakpoint adaptations (320px to 1440px+)
├── js/
│   ├── main.js                  # ES module entry point & diagnostics
│   ├── navigation.js            # Accessible mobile drawer, keyboard trap & active nav
│   ├── animations.js            # GSAP 3 + ScrollTrigger timelines & progressive enhancement
│   └── story-progress.js        # IntersectionObserver scene counter & progress bar
├── assets/
│   ├── images/                  # Verified historical photographs (WebP)
│   │   ├── ajanta-hero.webp
│   │   ├── ajanta-cave-context.webp
│   │   ├── ajanta-mural-reference.webp
│   │   └── ajanta-elephant-iconography.webp
│   ├── illustrations/           # Cohesive original vector narrative panels
│   │   ├── scene-01-forest.svg
│   │   ├── scene-02-stranger.svg
│   │   ├── scene-03-betrayal.svg
│   │   ├── scene-04-palace.svg
│   │   └── scene-05-return.svg
│   ├── textures/
│   │   └── cave-plaster.webp    # Subtle procedural lime-plaster patina
│   ├── icons/                   # Clean outline SVG icons
│   └── vendor/                  # Pinned offline GSAP 3.12.5 & ScrollTrigger
└── docs/                        # Complete project blueprint documentation (00 - 09)
```

---

## 🎨 Design System & Color Palette

The visual identity follows the natural mineral pigments discovered in the Ajanta Caves:

| Token | Hex / Value | Description |
|---|---|---|
| `--cave` | `#17130F` | Dark basalt cave ambient ground |
| `--cave-deep` | `#100D0A` | Deep shadowed rock base |
| `--umber` | `#34241C` | Warm burnt earth / shadow pigment |
| `--terracotta` | `#A84F32` | Indian red ochre (*geru*) accent & primary CTA |
| `--ochre` | `#C99A43` | Raw golden yellow ochre pigment & borders |
| `--sage` | `#68765A` | Terra-verte mineral green foliage |
| `--parchment` | `#E6D2AD` | Lime wash plaster tone for primary text |
| `--rose` | `#A96F66` | Indian madder mineral wash |
| `--muted` | `#B7A58B` | Weathered limestone supporting copy |
| `--line` | `rgba(201,154,67,0.28)` | Restrained 1px ochre framing rules |

### Typography
- **Display:** *Cormorant Garamond* (Google Fonts, SIL OFL 1.1) — elegant classical serif inspired by heritage carving.
- **Body & UI:** *Inter* (Google Fonts, SIL OFL 1.1) — highly legible modern grotesque sans-serif.

---

## 📖 The Five Narrative Scenes (Matri-Poshaka Jataka)

1. **Scene 01 — A quiet promise (`01 / THE FOREST`)**: In the secluded forest, the noble white elephant tends to his aged blind parents beneath an ancient bent Sal tree, measuring strength not by force, but by devotion.
2. **Scene 02 — A stranger on the path (`02 / AN ACT OF KINDNESS`)**: A disoriented traveller loses his way on a treacherous mountain path; the compassionate elephant guides him safely toward an opening glade.
3. **Scene 03 — Trust betrayed (`03 / THE TURNING POINT`)**: Led by greed, the traveller betrays the secret sanctuary to royal hunters; the white elephant is bound in cords and led away, casting a heartbroken backward glance toward his helpless parents.
4. **Scene 04 — A silent answer (`04 / THE REALISATION`)**: In the opulent royal pavilion, untouched golden platters of sugarcane and sweet fruits sit before the captive elephant, who fasts in grief; moved by his silent sorrow, the King inquires and awakens to the elephant's filial duty.
5. **Scene 05 — The way home (`05 / THE RETURN`)**: Freed by the moved monarch, the white elephant bounds back to the very same bent Sal tree at warm dawn; father, mother, and son embrace with entwined trunks in joyous reunion.

---

## ⚡ Technical Features & Architecture

- **Semantic HTML5:** Full landmark hierarchy (`header`, `nav`, `main`, `section#hero`, `section#ajanta`, `section#story`, `article#scene-1..5`, `section#reimagined`, `section#sources`, `footer`), single `h1`, structured headings and `figure`/`figcaption` pairings.
- **Accessibility (WCAG 2.1 AA Compliant):**
  - First focusable element is a dedicated `Skip to content` anchor.
  - Interactive elements have explicit labels, roles, and focus outlines.
  - Mobile menu includes `aria-expanded`, `aria-controls`, and keyboard `Escape` dismissal.
  - Informative images have factual, descriptive `alt` attributes; decorative graphics have `aria-hidden="true"`.
  - Contrast ratios meet or exceed AA standards on all surfaces.
  - Full `prefers-reduced-motion` overrides disabling animations and smooth scrolling.
- **Progressive Enhancement:**
  - Content is 100% visible and readable by default if JavaScript is disabled.
  - Animation classes are applied only after client-side capability detection.
  - GSAP 3 and ScrollTrigger are bundled locally in `assets/vendor/` for 100% offline functionality.
- **Dynamic Story Progress Tracker:** Real-time dual indicator (reading percentage bar and textual `SCENE 01 / 05`) driven by `IntersectionObserver`.

---

## 🚀 Running the Project Locally

Because the project uses ES Modules (`<script type="module">`), modern browsers require a local HTTP server rather than opening `file:///` directly.

### Method 1: Python (Recommended)
Open a terminal in the project directory:
```bash
# Navigate to the folder
cd "ajanta-echoes-in-ochre"

# Launch local HTTP server
python -m http.server 5500
```
Open your browser and navigate to:
```
http://localhost:5500
```

### Method 2: Node.js (npx)
```bash
cd "ajanta-echoes-in-ochre"
npx -y serve .
```

### Method 3: VS Code Live Server
Right-click on `index.html` inside VS Code / Antigravity and select **"Open with Live Server"**.

---

## 🌐 Static Deployment

The project has zero server dependencies and can be deployed directly to any static web host:
- **GitHub Pages:** Push the repository to GitHub, go to **Settings > Pages**, choose the branch and root folder, and save.
- **Netlify / Vercel:** Drag and drop the `ajanta-echoes-in-ochre` folder into the Netlify dashboard or link the Git repository.

---

## 📜 Provenance & Asset Verification

Full metadata records for all four historical photographs, vector illustrations, textures, typography, and libraries are recorded in [`SOURCES_AND_CREDITS.md`](SOURCES_AND_CREDITS.md).
