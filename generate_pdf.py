import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Times-Roman", 9)
        self.setFillColor(colors.HexColor("#222222"))

        # Top running header
        self.setLineWidth(0.5)
        self.setStrokeColor(colors.HexColor("#777777"))
        self.line(54, 841.89 - 40, 595.27 - 54, 841.89 - 40)
        self.drawString(54, 841.89 - 34, "Ajanta: Echoes in Ochre — Academic Project Documentation")

        # Bottom running footer
        self.line(54, 46, 595.27 - 54, 46)
        self.drawString(54, 33, "Department of Computer Science & Engineering | Web Technologies Coursework")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(595.27 - 54, 33, page_str)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=50,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=16,
        leading=19,
        alignment=1, # Centered
        textColor=colors.black,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=11,
        leading=14,
        alignment=1, # Centered
        textColor=colors.HexColor("#2A2A2A"),
        spaceAfter=3
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=12,
        alignment=1, # Centered
        textColor=colors.HexColor("#555555"),
        spaceAfter=6
    )

    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.black,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.6,
        alignment=4, # Justified
        textColor=colors.black,
        spaceAfter=4.5
    )

    body_narrative = ParagraphStyle(
        'DocBodyNarrative',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=13.2,
        alignment=4, # Justified
        textColor=colors.black,
        spaceAfter=4
    )

    body_feature = ParagraphStyle(
        'DocBodyFeature',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=13.3,
        alignment=4, # Justified
        textColor=colors.black,
        spaceAfter=4.5
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.black
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=11.8,
        textColor=colors.black
    )

    story = []

    # ---------------------------------------------------------
    # PAGE 1 CONTENT
    # ---------------------------------------------------------

    # 1. Title Block
    story.append(Paragraph("Ajanta: Echoes in Ochre — The Living Murals of Ajanta", title_style))
    story.append(Paragraph("An Interactive Digital Storytelling Website Inspired by the Ajanta Cave Paintings", subtitle_style))
    story.append(Paragraph("Course Project: Interactive Media & Web Engineering | Live Website: <a href=\"https://ajanta-echoes-in-ochre.vercel.app/\" color=\"#003399\"><u>https://ajanta-echoes-in-ochre.vercel.app/</u></a>", meta_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#444444"), spaceBefore=0, spaceAfter=5))

    # 2. Project Overview
    story.append(Paragraph("1. Project Overview", h1_style))
    story.append(Paragraph(
        "<b>Ajanta: Echoes in Ochre</b> is a responsive, single-page digital museum and narrative storytelling website "
        "developed as an academic project to explore the artistic, cultural, and moral heritage of the UNESCO World Heritage "
        "Ajanta Caves in Maharashtra, India. Dating from approximately the 2nd century BCE to the 5th–6th century CE, the rock-cut "
        "monuments at Ajanta represent the pinnacle of ancient Indian painting and Buddhist rock architecture. However, due to "
        "geographical distance and environmental fragility, these masterworks remain largely inaccessible to modern students "
        "and general audiences in their original narrative context.",
        body_style
    ))
    story.append(Paragraph(
        "The primary objective of this project was to translate the ancient mural storytelling tradition into an engaging, "
        "interactive digital experience while preserving its historical dignity. Rather than constructing a detached image "
        "gallery or an oversimplified slideshow, the website integrates verified high-resolution photographs of surviving Cave 17 "
        "murals with an illustrated, five-scene adaptation of a traditional Buddhist moral tale. By utilizing thoughtful typography, "
        "an authentic natural mineral pigment palette, and scroll-driven animation, the website recreates the contemplative experience "
        "of walking through the dimly lit cave halls, highlighting the timeless craftsmanship of ancient Indian master artists.",
        body_style
    ))

    # 3. Story Presented in the Website
    story.append(Paragraph("2. Narrative Storyboard: The Matri-Poshaka Jataka", h1_style))
    story.append(Paragraph(
        "The centerpiece of the website is an illustrated retelling of the <b>Matri-Poshaka Jataka</b> (Jataka No. 455), an ancient "
        "Buddhist moral narrative centered on selfless filial devotion, empathy, and integrity. The tale follows the life of the "
        "Bodhisattva born as a noble, compassionate white elephant living in the Himalayan wilderness, whose sole devotion is the "
        "care and nourishment of his aged, blind parents. The website presents this enduring story across five sequential scenes:",
        body_narrative
    ))

    story.append(Paragraph(
        "<b>Scene 1 — A Quiet Promise:</b> Secluded in the deep forest away from worldly conflict, the white elephant devotes his physical "
        "strength to foraging wild fruits, fresh foliage, and tender lotus stalks for his two blind parents, who rest peacefully beneath an "
        "ancient bent Sal tree. His strength is defined not by dominance, but by the quiet patience and responsibility he demonstrates.",
        body_narrative
    ))
    story.append(Paragraph(
        "<b>Scene 2 — A Stranger on the Path:</b> While roaming the forest ridges, the elephant encounters an exhausted traveller who has "
        "lost his path amid dangerous ravines. Acting out of pure compassion and asking for nothing in return, the elephant allows the "
        "frightened wanderer to ride upon his back and guides him safely out of the wild forest to the populated highway.",
        body_narrative
    ))
    story.append(Paragraph(
        "<b>Scene 3 — Trust Betrayed:</b> The kindness freely given by the elephant is met with deceit. Arriving in the royal city of Varanasi, "
        "the traveller discovers that the King's state elephant has died and that royal scouts seek a worthy successor. Blinded by greed, "
        "the traveller leads royal foresters directly to the elephant's sanctuary. Captured in ceremonial ropes, the elephant offers no violent "
        "resistance, looking back with sorrow as he realizes his blind parents are left helpless and waiting.",
        body_narrative
    ))
    story.append(Paragraph(
        "<b>Scene 4 — A Silent Answer:</b> Brought to the royal palace courtyard, the captive elephant is offered lavish feasts of sugarcane, "
        "sweet rice, and fruits. In deep grief for his starving parents, the elephant fasts and refuses all food. Moved by the animal's silent "
        "dignity, the King inquires into the cause of his sorrow. Upon learning of the elephant's filial devotion, the King's conscience is deeply stirred.",
        body_narrative
    ))
    story.append(Paragraph(
        "<b>Scene 5 — The Way Home:</b> Recognizing that true nobility cannot be enslaved, the King grants the elephant unconditional freedom. "
        "Returning to the familiar bent Sal tree at dawn, the elephant joyously reunites with his weeping parents with entwined trunks.",
        body_narrative
    ))
    story.append(Paragraph(
        "<b>Core Moral Lessons:</b> The story highlights universal ethical virtues: filial responsibility (<i>matri-poshaka</i>), kindness "
        "extended without expectation of reward, the shamefulness of betrayal, and the necessity of empathetic listening in governance.",
        body_narrative
    ))

    # Force clean page break to maintain balanced 2-page academic layout
    story.append(PageBreak())

    # ---------------------------------------------------------
    # PAGE 2 CONTENT
    # ---------------------------------------------------------

    # 4. Website Design and Features
    story.append(Paragraph("3. Website Architecture, Design, and Key Features", h1_style))
    story.append(Paragraph(
        "The website was built following editorial heritage guidelines, emphasizing visual breathing room, restrained chrome, and legible "
        "storytelling. Key design and interactive features include:",
        body_style
    ))

    story.append(Paragraph(
        "• <b>Natural Mineral Pigment Palette:</b> The visual design faithfully mirrors the organic pigments found in the Ajanta Caves: "
        "Basalt Cave Black (#17130F), Raw Umber (#34241C), Indian Red Ochre / <i>Geru</i> (#A84F32), Golden Yellow Ochre (#C99A43), "
        "Terra-Verte Sage Green (#68765A), and Lime-Plaster Parchment (#E6D2AD), supplemented with a subtle procedural plaster grain overlay.",
        body_feature
    ))
    story.append(Paragraph(
        "• <b>Authentic Photographic Documentation:</b> Curated, high-resolution photographs of authentic Cave 17 murals and panoramic gorge views "
        "provide historical context. Every archival image includes holding collection citations (ASI) and verified open-access licenses (CC0, CC BY 4.0, CC BY 2.0).",
        body_feature
    ))
    story.append(Paragraph(
        "• <b>Five Custom Narrative Vector Illustrations:</b> To present the Matri-Poshaka narrative truthfully without misattributing ancient murals, "
        "five original vector panels were authored for this project. They preserve classical Gupta-Vakataka proportions, tribhanga body contours, "
        "lotus-petal eyes, character continuity (the white elephant, blind parents, and bent Sal tree), and period-accurate pavilion architecture.",
        body_feature
    ))
    story.append(Paragraph(
        "• <b>Interactive Story Progress Indicator:</b> A dynamic reading progress component in the story section continuously tracks the user's "
        "reading position across the five scenes using an <code>IntersectionObserver</code>, updating a percentage bar and textual indicator (<i>SCENE 01 / 05</i> to <i>05 / 05</i>).",
        body_feature
    ))
    story.append(Paragraph(
        "• <b>Scroll-Driven Animations & Performance:</b> Editorial reveals are orchestrated via GSAP 3 and ScrollTrigger. Animations are non-intrusive, "
        "preserving natural scrolling without scroll-trapping. Complete <code>prefers-reduced-motion</code> overrides and no-JS fallbacks are implemented.",
        body_feature
    ))
    story.append(Paragraph(
        "• <b>Responsive Layout & Accessible Navigation:</b> The interface adapts across devices (320px to 1440px+). Features include a sticky translucent "
        "header, an accessible keyboard-navigable mobile drawer, WCAG AA contrast compliance, and skip-to-content accessibility links.",
        body_feature
    ))

    # 5. Technologies Used
    story.append(Paragraph("4. Technologies Implemented", h1_style))

    tech_data = [
        [Paragraph("<b>Technology</b>", table_header_style), Paragraph("<b>Role and Functional Implementation</b>", table_header_style)],
        [Paragraph("<b>HTML5</b>", table_cell_style), Paragraph("Semantic page hierarchy (header, nav, main, article, figure, figcaption, footer), descriptive alt text, and ARIA roles.", table_cell_style)],
        [Paragraph("<b>CSS3</b>", table_cell_style), Paragraph("Custom design tokens, fluid clamp() typography, responsive grid and flexbox layouts, media queries, and plaster texture styling.", table_cell_style)],
        [Paragraph("<b>JavaScript (ES6+)</b>", table_cell_style), Paragraph("Modular ES architecture (main.js, navigation.js, story-progress.js, animations.js) managing navigation, drawer toggles, and observers.", table_cell_style)],
        [Paragraph("<b>GSAP 3 & ScrollTrigger</b>", table_cell_style), Paragraph("Scroll-triggered entrance reveals and element timelines, bundled locally in assets/vendor/ for 100% offline functionality.", table_cell_style)],
        [Paragraph("<b>Git & GitHub</b>", table_cell_style), Paragraph("Version control and repository management: <a href=\"https://github.com/AdityaG346/AJANTA-ECHOES-IN-OCHRE\" color=\"#003399\"><u>github.com/AdityaG346/AJANTA-ECHOES-IN-OCHRE</u></a>.", table_cell_style)],
        [Paragraph("<b>Vercel</b>", table_cell_style), Paragraph("Production deployment configuration with zero-configuration global CDN delivery.<br/><b>Live Website:</b> <a href=\"https://ajanta-echoes-in-ochre.vercel.app/\" color=\"#003399\"><u>https://ajanta-echoes-in-ochre.vercel.app/</u></a>", table_cell_style)]
    ]

    tech_table = Table(tech_data, colWidths=[120, 367])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#EFEFEF")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(tech_table)
    story.append(Spacer(1, 4))

    # 6. Conclusion
    story.append(Paragraph("5. Conclusion", h1_style))
    story.append(Paragraph(
        "The <b>Ajanta: Echoes in Ochre</b> project illustrates how modern front-end web development can serve as a compelling medium for "
        "cultural preservation and digital humanities. By synthesizing authentic historical research with modular web standards, custom vector "
        "art, and accessible storytelling, the project makes an ancient moral narrative vibrant and relevant for contemporary audiences. Developing "
        "this project reinforced core software engineering competencies, including semantic markup, performance budgeting, accessible interface design, "
        "and clean separation of concerns, demonstrating that thoughtful web engineering can honor ancient art traditions with fidelity and elegance.",
        body_style
    ))

    # Build the document using NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == '__main__':
    out_dir = 'documentation'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'AJANTA_ECHOES_IN_OCHRE_PROJECT_DOCUMENTATION.pdf')
    build_pdf(out_path)
    
    # Verify page count
    with open(out_path, 'rb') as f:
        data = f.read()
    pages = re.findall(rb'/Type\s*/Page\b', data)
    print(f"Generated PDF successfully. Exact page count: {len(pages)}")
