import os

def create_illustrations():
    os.makedirs('assets/illustrations', exist_ok=True)

    # -------------------------------------------------------------
    # Shared SVG Components & Styles
    # -------------------------------------------------------------
    svg_defs = '''
    <defs>
      <!-- Base Gradients -->
      <radialGradient id="cave-bg" cx="50%" cy="45%" r="75%">
        <stop offset="0%" stop-color="#241B15"/>
        <stop offset="60%" stop-color="#18130F"/>
        <stop offset="100%" stop-color="#0E0B08"/>
      </radialGradient>
      <radialGradient id="palace-bg" cx="50%" cy="40%" r="70%">
        <stop offset="0%" stop-color="#362217"/>
        <stop offset="60%" stop-color="#22160F"/>
        <stop offset="100%" stop-color="#120C08"/>
      </radialGradient>
      <radialGradient id="dawn-bg" cx="50%" cy="40%" r="75%">
        <stop offset="0%" stop-color="#4A311D"/>
        <stop offset="45%" stop-color="#2D1C12"/>
        <stop offset="100%" stop-color="#140E0A"/>
      </radialGradient>

      <!-- White Elephant Bodhisattva Gradient -->
      <linearGradient id="white-elephant-body" x1="0.2" y1="0" x2="0.8" y2="1">
        <stop offset="0%" stop-color="#FAF5EC"/>
        <stop offset="40%" stop-color="#ECE0CD"/>
        <stop offset="75%" stop-color="#D0BC9E"/>
        <stop offset="100%" stop-color="#9C8065"/>
      </linearGradient>

      <linearGradient id="white-elephant-highlight" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
        <stop offset="100%" stop-color="#E2D0B6" stop-opacity="0.2"/>
      </linearGradient>

      <!-- Blind Parents Gray/Umber Gradient -->
      <linearGradient id="parent-elephant-grad" x1="0.2" y1="0" x2="0.8" y2="1">
        <stop offset="0%" stop-color="#7A685B"/>
        <stop offset="50%" stop-color="#58483D"/>
        <stop offset="100%" stop-color="#382C23"/>
      </linearGradient>

      <!-- Ancient Bent Sal Tree Trunk Gradient -->
      <linearGradient id="tree-bark" x1="0" y1="0" x2="1" y2="0.2">
        <stop offset="0%" stop-color="#271911"/>
        <stop offset="35%" stop-color="#432F23"/>
        <stop offset="70%" stop-color="#563E30"/>
        <stop offset="100%" stop-color="#1E130D"/>
      </linearGradient>

      <!-- Mineral Pigment Shading -->
      <linearGradient id="ochre-gold" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#E5B456"/>
        <stop offset="100%" stop-color="#9E6E20"/>
      </linearGradient>
      <linearGradient id="terracotta-red" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#C25A39"/>
        <stop offset="100%" stop-color="#6F2815"/>
      </linearGradient>

      <!-- Plaster Stipple Texture Pattern -->
      <pattern id="plaster-grain" width="100" height="100" patternUnits="userSpaceOnUse">
        <circle cx="15" cy="15" r="1" fill="#C99A43" opacity="0.12"/>
        <circle cx="65" cy="35" r="1.5" fill="#E6D2AD" opacity="0.08"/>
        <circle cx="40" cy="75" r="1" fill="#A84F32" opacity="0.1"/>
        <circle cx="85" cy="85" r="1.2" fill="#C99A43" opacity="0.12"/>
      </pattern>
    </defs>
    '''

    # =============================================================
    # SCENE 01: FOREST CAREGIVING
    # Adult white elephant offering foliage to two blind parents
    # =============================================================
    scene_01 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
      {svg_defs}
      <!-- Background -->
      <rect width="1200" height="800" fill="url(#cave-bg)"/>
      <rect width="1200" height="800" fill="url(#plaster-grain)"/>

      <!-- Distant Ajanta Cliff Rocks -->
      <path d="M0,520 Q240,430 480,480 T960,450 Q1100,470 1200,440 L1200,800 L0,800 Z" fill="#1C1510" opacity="0.9"/>
      <path d="M0,570 Q200,510 400,540 T880,520 L1200,500 L1200,800 L0,800 Z" fill="#251B14" opacity="0.95"/>

      <!-- The Recurring Ancient Bent Sal Tree (Left Anchor) -->
      <!-- Massive Gnarled Trunk with distinct arch curving inward -->
      <path d="M60,800 C75,660 55,530 110,410 C145,330 210,280 290,230 C380,180 500,200 610,170 C600,195 540,225 450,245 C370,265 295,315 250,385 C205,470 215,630 220,800 Z" fill="url(#tree-bark)"/>
      <path d="M210,340 C270,305 365,295 425,260 C410,278 355,320 300,342 Z" fill="#38261C"/>
      <path d="M125,430 C70,390 10,380 -30,390 C-20,375 40,370 100,405 Z" fill="#38261C"/>

      <!-- Stylized Tiered Canopy (Ajanta Lotus-Leaf Clustered Foliage) -->
      <g fill="#455437" stroke="#25301D" stroke-width="2">
        <ellipse cx="320" cy="190" rx="95" ry="50"/>
        <ellipse cx="450" cy="165" rx="115" ry="60"/>
        <ellipse cx="570" cy="155" rx="85" ry="45"/>
        <ellipse cx="240" cy="235" rx="85" ry="48"/>
        <ellipse cx="370" cy="225" rx="100" ry="52"/>
      </g>
      <g fill="#617051" stroke="#37452A" stroke-width="1.5">
        <ellipse cx="340" cy="175" rx="75" ry="38"/>
        <ellipse cx="465" cy="150" rx="90" ry="42"/>
        <ellipse cx="550" cy="145" rx="65" ry="32"/>
        <ellipse cx="260" cy="220" rx="65" ry="34"/>
      </g>
      <!-- Hanging forest creepers and ochre berries -->
      <path d="M300,230 Q325,340 295,410" stroke="#68765A" stroke-width="3" fill="none"/>
      <path d="M430,210 Q455,330 435,395" stroke="#68765A" stroke-width="2.5" fill="none"/>
      <circle cx="295" cy="415" r="7" fill="#A96F66"/>
      <circle cx="435" cy="400" r="6" fill="#C99A43"/>

      <!-- Two Blind Elderly Parents (Resting close together in devotion, right side) -->
      <g id="scene1-parents" transform="translate(560, 370)">
        <!-- Mother (Behind) -->
        <path d="M150,260 C130,200 170,130 230,105 C300,75 380,85 430,125 C480,165 490,240 480,300 L430,300 C420,230 370,175 310,175 C250,175 190,215 170,280 Z" fill="url(#parent-elephant-grad)"/>
        <!-- Mother's head and gentle closed eye -->
        <circle cx="360" cy="135" r="45" fill="#4B3A30"/>
        <path d="M345,138 Q360,132 375,140" stroke="#2B1F17" stroke-width="3.5" stroke-linecap="round" fill="none"/>
        <path d="M380,140 Q415,175 425,220" stroke="#362921" stroke-width="12" stroke-linecap="round" fill="none"/>

        <!-- Father (Foreground resting) -->
        <path d="M70,320 C50,250 80,180 140,140 C220,95 330,100 390,150 C430,195 450,270 440,335 C350,345 200,345 70,320 Z" fill="url(#parent-elephant-grad)"/>
        <ellipse cx="170" cy="335" rx="90" ry="35" fill="#392C23"/>
        <ellipse cx="320" cy="340" rx="80" ry="30" fill="#2E221A"/>

        <!-- Father's Head with Venerable Wrinkles -->
        <circle cx="130" cy="180" r="65" fill="#584639"/>
        <path d="M95,150 Q130,140 165,155" stroke="#362920" stroke-width="2.5" fill="none"/>
        <path d="M90,165 Q125,155 160,170" stroke="#362920" stroke-width="2" fill="none"/>
        <!-- Peaceful curved closed blind eye -->
        <path d="M115,185 Q135,177 155,188" stroke="#201610" stroke-width="4.5" stroke-linecap="round" fill="none"/>
        <!-- Soft drooping ear -->
        <path d="M165,150 C205,160 225,220 205,260 C185,290 155,280 145,250 Z" fill="#48382E" stroke="#30231B" stroke-width="2"/>
        <!-- Curled trunk reaching warmly toward offering -->
        <path d="M90,200 C60,240 35,270 15,258 C0,246 12,218 35,208" stroke="#48382E" stroke-width="18" stroke-linecap="round" fill="none"/>
      </g>

      <!-- The Bodhisattva White Elephant (Active, Majestic, Offering Foliage) -->
      <g id="scene1-white-elephant" transform="translate(190, 245)">
        <!-- Robust, Luminous Ivory Body -->
        <path d="M180,260 C160,180 220,115 310,105 C410,95 480,135 510,215 C530,275 510,375 470,425 L390,425 C400,345 390,305 330,295 C270,285 210,325 190,425 L120,425 C110,355 130,295 180,260 Z" fill="url(#white-elephant-body)"/>

        <!-- Sturdy Classical Legs -->
        <path d="M300,310 L320,475 L380,475 L370,310 Z" fill="#C2AC90" stroke="#7A6046" stroke-width="2"/>
        <path d="M220,320 L230,475 L290,475 L280,320 Z" fill="#DCBDA1" stroke="#7A6046" stroke-width="2"/>
        <path d="M430,320 L440,475 L490,475 L480,320 Z" fill="#B29C80" stroke="#7A6046" stroke-width="2"/>

        <!-- Classical Ajanta Forehead Dome (Kumbha) -->
        <path d="M160,190 C140,125 185,65 255,65 C305,65 335,105 325,165 C305,205 255,235 205,225 Z" fill="url(#white-elephant-body)" stroke="#8C6A4B" stroke-width="2.5"/>

        <!-- Graceful Flared Royal Ear with Terracotta Accent -->
        <path d="M255,105 C305,115 340,175 320,240 C300,285 255,280 240,235 Z" fill="#D5C2A9" stroke="#8C6A4B" stroke-width="2.5"/>
        <path d="M265,130 C295,145 310,185 295,225" stroke="#A96F66" stroke-width="5" stroke-linecap="round" fill="none" opacity="0.45"/>

        <!-- Lotus Petal Eye (Gentle, Radiant, Aware) -->
        <ellipse cx=\"208\" cy=\"145\" rx=\"14\" ry=\"8\" fill=\"#FFF9F0\" stroke=\"#4A3528\" stroke-width=\"2\"/>
        <circle cx=\"210\" cy=\"145\" r=\"5\" fill=\"#241B14\"/>
        <circle cx=\"212\" cy=\"143\" r=\"1.5\" fill=\"#FFFFFF\"/>
        <path d=\"M192,136 Q208,128 228,137\" stroke=\"#A84F32\" stroke-width=\"2.5\" fill=\"none\"/>

        <!-- Polished Curved Ivory Tusk -->
        <path d=\"M160,205 C130,235 90,245 70,230 C65,225 75,210 115,195 C140,185 160,190 160,205 Z\" fill=\"#FFFDF5\" stroke=\"#BAAA90\" stroke-width=\"2\"/>

        <!-- Reaching Tender Trunk with Forest Shoots -->
        <path d=\"M170,205 C150,265 170,335 250,365 C320,390 390,375 425,335\" stroke=\"url(#white-elephant-body)\" stroke-width=\"32\" stroke-linecap=\"round\" fill=\"none\"/>
        <path d=\"M170,205 C150,265 170,335 250,365 C320,390 390,375 425,335\" stroke=\"#7A6046\" stroke-width=\"2\" fill=\"none\"/>

        <!-- Forest Greens, Lotus Stalks and Wild Fig in Trunk -->
        <g transform=\"translate(415, 310)\">
          <path d=\"M0,10 C10,-15 35,-15 45,10 C25,25 15,20 0,10 Z\" fill=\"#A96F66\" stroke=\"#69352E\" stroke-width=\"1.5\"/>
          <path d=\"M10,8 C20,-8 30,-8 35,8 Z\" fill=\"#C99A43\"/>
          <path d=\"M-10,25 C-5,-5 20,0 25,20 Z\" fill=\"#68765A\" stroke=\"#3D4933\" stroke-width=\"1.5\"/>
          <path d=\"M20,20 C35,5 55,15 45,35 Z\" fill=\"#4C5B3E\" stroke=\"#26311D\" stroke-width=\"1.5\"/>
        </g>
      </g>

      <!-- Forest Floor & Still Mountain Water Pool -->
      <path d=\"M0,720 Q300,680 600,710 T1200,690 L1200,800 L0,800 Z\" fill=\"#17120D\"/>
      <ellipse cx=\"520\" cy=\"755\" rx=\"180\" ry=\"35\" fill=\"#111610\" stroke=\"#2A3826\" stroke-width=\"1.5\"/>
      <ellipse cx=\"470\" cy=\"750\" rx=\"35\" ry=\"10\" fill=\"#3D5034\"/>
      <ellipse cx=\"560\" cy=\"760\" rx=\"45\" ry=\"12\" fill=\"#32422B\"/>
      <circle cx=\"520\" cy=\"745\" r=\"7\" fill=\"#A96F66\"/>

      <!-- Refined Mineral Framing Borders -->
      <rect x=\"16\" y=\"16\" width=\"1168\" height=\"768\" rx=\"4\" fill=\"none\" stroke=\"#C99A43\" stroke-width=\"1.5\" stroke-opacity=\"0.4\"/>
      <rect x=\"24\" y=\"24\" width=\"1152\" height=\"752\" rx=\"2\" fill=\"none\" stroke=\"#A84F32\" stroke-width=\"0.75\" stroke-opacity=\"0.3\"/>
    </svg>'''

    # =============================================================
    # SCENE 02: THE LOST TRAVELLER
    # Compassion on the winding forest mountain path
    # =============================================================
    scene_02 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
      {svg_defs}
      <!-- Background Base -->
      <rect width="1200" height="800" fill="url(#cave-bg)"/>
      <rect width="1200" height="800" fill="url(#plaster-grain)"/>

      <!-- Distant Sunlit Clearing Breakout -->
      <path d="M750,150 Q920,100 1150,160 L1200,480 L700,450 Z" fill="#4A341E" opacity="0.35"/>
      <circle cx="950" cy="220" r="140" fill="#C99A43" opacity="0.12"/>

      <!-- Rugged Forest Mountains and Crags -->
      <path d="M0,450 Q280,360 560,420 T1200,380 L1200,800 L0,800 Z" fill="#1E1611"/>
      <path d="M0,520 Q320,460 640,510 T1200,470 L1200,800 L0,800 Z" fill="#291E16"/>

      <!-- Winding Rocky Forest Path -->
      <path d="M120,800 C180,680 280,620 440,590 C620,560 760,490 920,420 C1040,360 1120,320 1200,300 L1200,420 C1100,450 980,510 820,580 C680,640 540,680 420,800 Z" fill="#3D2C1E" stroke="#5B4330" stroke-width="1.5"/>

      <!-- Dense Forest Plant Clusters & Trees -->
      <g fill="#37452B" stroke="#222B1B" stroke-width="1.5">
        <ellipse cx="140" cy="380" rx="100" ry="60"/>
        <ellipse cx="250" cy="350" rx="90" ry="50"/>
        <ellipse cx="80" cy="440" rx="85" ry="45"/>
        <ellipse cx="780" cy="340" rx="90" ry="45"/>
        <ellipse cx="900" cy="310" rx="110" ry="55"/>
      </g>
      <g fill="#576847" stroke="#37452B" stroke-width="1.5">
        <ellipse cx="160" cy="365" rx="75" ry="40"/>
        <ellipse cx="265" cy="335" rx="70" ry="38"/>
        <ellipse cx="800" cy="325" rx="70" ry="35"/>
      </g>

      <!-- The Bodhisattva White Elephant Guiding the Way (Left Center) -->
      <g id="scene2-elephant" transform="translate(140, 210)">
        <!-- Majestic Ivory Body Oriented Forward Right -->
        <path d="M160,260 C140,180 200,115 290,105 C390,95 460,135 490,215 C510,275 490,375 450,425 L370,425 C380,345 370,305 310,295 C250,285 190,325 170,425 L100,425 C90,355 110,295 160,260 Z" fill="url(#white-elephant-body)"/>

        <!-- Legs Standing Forward on Path -->
        <path d="M280,310 L300,475 L360,475 L350,310 Z" fill="#C2AC90" stroke="#7A6046" stroke-width="2"/>
        <path d="M200,320 L210,475 L270,475 L260,320 Z" fill="#DCBDA1" stroke="#7A6046" stroke-width="2"/>
        <path d="M410,320 L420,475 L470,475 L460,320 Z" fill="#B29C80" stroke="#7A6046" stroke-width="2"/>

        <!-- Noble Head & Arched Ear -->
        <path d="M280,180 C260,115 305,55 375,55 C425,55 455,95 445,155 C425,195 375,225 325,215 Z" fill="url(#white-elephant-body)" stroke="#8C6A4B" stroke-width="2.5"/>
        <path d="M320,105 C370,115 405,175 385,240 C365,285 320,280 305,235 Z" fill="#D5C2A9" stroke="#8C6A4B" stroke-width="2.5"/>

        <!-- Kind Almond Eye looking gently at Traveller -->
        <ellipse cx="370" cy="135" rx="13" ry="7.5" fill="#FFF9F0" stroke="#4A3528" stroke-width="2"/>
        <circle cx="372" cy="135" r="4.5" fill="#241B14"/>
        <circle cx="374" cy="133" r="1.5" fill="#FFFFFF"/>
        <path d="M355,126 Q370,118 390,127" stroke="#A84F32" stroke-width="2.5" fill="none"/>

        <!-- Tusk pointing forward -->
        <path d="M400,195 C430,225 470,230 490,215 C495,210 485,195 445,180 Z" fill="#FFFDF5" stroke="#BAAA90" stroke-width="2"/>

        <!-- Extended Trunk Gracefully Indicating the Way to the Traveller -->
        <path d="M380,195 C430,240 500,270 590,275 C640,278 690,265 720,245" stroke="url(#white-elephant-body)" stroke-width="28" stroke-linecap="round" fill="none"/>
        <path d="M380,195 C430,240 500,270 590,275 C640,278 690,265 720,245" stroke="#7A6046" stroke-width="2" fill="none"/>
      </g>

      <!-- The Lost Traveller (Ajanta Human Figure Proportions: graceful, grateful) -->
      <g id="scene2-traveller" transform="translate(860, 360)">
        <!-- Exhausted but Relieved Posture, Hands Clasped in Anjali Mudra -->
        <!-- Slender legs draped in ochre dhoti -->
        <path d="M40,230 L30,360 L55,360 L65,230 Z" fill="#755026"/>
        <path d="M70,230 L80,360 L105,360 L95,230 Z" fill="#916430"/>
        <!-- Terracotta / Ochre pleated dhoti wrap -->
        <path d="M25,140 C15,190 20,240 45,260 C65,270 95,270 115,245 C125,200 115,150 100,140 Z" fill="#C99A43" stroke="#855B18" stroke-width="2"/>
        <path d="M50,150 Q70,210 65,260" stroke="#855B18" stroke-width="2" fill="none"/>
        <path d="M80,150 Q90,205 95,255" stroke="#855B18" stroke-width="2" fill="none"/>

        <!-- Warm Golden-Umber Skin Tone Torso (Ajanta Classical Figure) -->
        <path d="M35,60 C25,95 20,130 30,155 C50,165 95,165 110,150 C115,125 105,90 95,60 Z" fill="#B37C50" stroke="#684223" stroke-width="2"/>
        <!-- Slender Chest Contouring and Sacred Cord (Upavita) -->
        <path d="M45,65 Q75,110 50,155" stroke="#E6D2AD" stroke-width="2" stroke-dasharray="4,4" fill="none"/>

        <!-- Clasped Hands in Reverent Gratitude -->
        <path d="M15,100 C-5,115 -10,130 5,140 C20,145 35,135 45,110 Z" fill="#A47047" stroke="#684223" stroke-width="1.5"/>
        <path d="M20,95 L-5,110 L-10,125 L10,120 Z" fill="#94633B"/>

        <!-- Head, Classic Ajanta Profile, Hair Tied in Topknot (Chignon) -->
        <circle cx="65" cy="25" r="26" fill="#B37C50" stroke="#684223" stroke-width="2"/>
        <path d="M45,20 C40,-5 65,-15 80,-5 C90,5 90,20 85,25 Z" fill="#1C140E"/>
        <circle cx="82" cy="-2" r="10" fill="#1C140E"/>
        <!-- Soft facial features: bowed head in thankfulness -->
        <ellipse cx="56" cy="22" rx="4" ry="2.5" fill="#20150E"/>
        <path d="M50,16 Q57,12 65,16" stroke="#523218" stroke-width="1.5" fill="none"/>
        <path d="M52,32 Q62,35 68,30" stroke="#7A2D1F" stroke-width="2" fill="none"/>
      </g>

      <!-- Foreground Floral Details & Framing -->
      <path d="M0,740 Q400,700 800,730 T1200,710 L1200,800 L0,800 Z" fill="#16110D"/>
      <rect x="16" y="16" width="1168" height="768" rx="4" fill="none" stroke="#C99A43" stroke-width="1.5" stroke-opacity="0.4"/>
      <rect x="24" y="24" width="1152" height="752" rx="2" fill="none" stroke="#A84F32" stroke-width="0.75" stroke-opacity="0.3"/>
    </svg>'''

    # =============================================================
    # SCENE 03: TRUST BETRAYED
    # Tense umber palette, royal attendants with ropes, sorrowful glance back
    # =============================================================
    scene_03 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
      {svg_defs}
      <!-- Moody, Stormy Umber Background -->
      <radialGradient id="betrayal-bg" cx="45%" cy="45%" r="75%">
        <stop offset="0%" stop-color="#2D1A12"/>
        <stop offset="50%" stop-color="#1F120D"/>
        <stop offset="100%" stop-color="#0E0805"/>
      </radialGradient>
      <rect width="1200" height="800" fill="url(#betrayal-bg)"/>
      <rect width="1200" height="800" fill="url(#plaster-grain)"/>

      <!-- Darkened Cliffs and Tangled Creepers -->
      <path d="M0,480 Q240,400 480,450 T960,420 Q1100,440 1200,410 L1200,800 L0,800 Z" fill="#180F0A"/>
      <path d="M0,540 Q300,480 600,530 T1200,490 L1200,800 L0,800 Z" fill="#20140D"/>

      <!-- Treacherous Traveller in Left Midground Pointing Out The Elephant -->
      <g id="scene3-betrayer" transform="translate(180, 370)">
        <!-- Draped in darker terracotta/soiled ochre -->
        <path d="M30,220 L20,350 L45,350 L55,220 Z" fill="#583B1B"/>
        <path d="M60,220 L70,350 L95,350 L85,220 Z" fill="#704A23"/>
        <path d="M15,130 C5,180 10,230 35,250 C55,260 85,260 105,235 C115,190 105,140 90,130 Z" fill="#A84F32" stroke="#5E2716" stroke-width="2"/>

        <!-- Tense Torso leaning forward toward royal party -->
        <path d="M25,50 C15,85 10,120 20,145 C40,155 85,155 100,140 C105,115 95,80 85,50 Z" fill="#A36B42" stroke="#59341B" stroke-width="2"/>

        <!-- Betraying Arm Pointing Directly at the White Elephant -->
        <path d="M85,70 L190,45 L190,65 L85,90 Z" fill="#A36B42" stroke="#59341B" stroke-width="1.5"/>
        <circle cx="195" cy="55" r="7" fill="#8E5A35"/>
        <path d="M195,55 L225,50" stroke="#59341B" stroke-width="3" stroke-linecap="round"/>

        <!-- Face turned with guilt/greed (sharp eye, crooked brow) -->
        <circle cx="55" cy="20" r="24" fill="#A36B42" stroke="#59341B" stroke-width="2"/>
        <path d="M35,15 C30,-8 55,-18 70,-8 C80,2 80,18 75,22 Z" fill="#140E0A"/>
        <ellipse cx="62" cy="18" rx="4" ry="2" fill="#1C140E"/>
        <path d="M56,12 Q64,15 72,11" stroke="#482713" stroke-width="2" fill="none"/>
      </g>

      <!-- Royal Hunters / Attendants with Turbans and Catching Cords -->
      <g id="scene3-royal-retinue" transform="translate(360, 330)">
        <!-- Royal Attendant 1 (Leading the Cords) -->
        <path d="M40,240 L35,390 L60,390 L65,240 Z" fill="#2E2016"/>
        <path d="M70,240 L75,390 L100,390 L95,240 Z" fill="#442E20"/>
        <!-- Draped ochre royal livery -->
        <path d="M25,140 C15,190 20,240 45,260 C65,270 95,270 115,245 C125,200 115,150 100,140 Z" fill="#C99A43" stroke="#855B18" stroke-width="2"/>
        <path d="M35,60 C25,95 20,130 30,155 C50,165 95,165 110,150 C115,125 105,90 95,60 Z" fill="#99663E" stroke="#58351B" stroke-width="2"/>
        <!-- Elaborate Ajanta Turban (Ushnisha wrap) with crest ornament -->
        <circle cx="65" cy="25" r="26" fill="#99663E"/>
        <ellipse cx="65" cy="10" rx="30" ry="18" fill="#A84F32" stroke="#5C2515" stroke-width="2"/>
        <circle cx="65" cy="-2" r="7" fill="#E5B456"/>

        <!-- Attendant holding ceremonial golden-ochre capture ropes -->
        <path d="M85,100 L140,120" stroke="#99663E" stroke-width="8" stroke-linecap="round"/>
        <path d="M140,120 C220,140 320,180 420,240" stroke="#C99A43" stroke-width="5" stroke-dasharray="6,4" fill="none"/>
      </g>

      <!-- The Captive Bodhisattva White Elephant (Facing Right, Head Turned Back in Deep Sorrow) -->
      <g id="scene3-captive-elephant" transform="translate(620, 220)">
        <!-- Massive ivory body caught in royal harness cords -->
        <path d="M180,260 C160,180 220,115 310,105 C410,95 480,135 510,215 C530,275 510,375 470,425 L390,425 C400,345 390,305 330,295 C270,285 210,325 190,425 L120,425 C110,355 130,295 180,260 Z" fill="url(#white-elephant-body)"/>

        <!-- Legs with restrained step -->
        <path d="M300,310 L320,475 L380,475 L370,310 Z" fill="#C2AC90" stroke="#7A6046" stroke-width="2"/>
        <path d="M220,320 L230,475 L290,475 L280,320 Z" fill="#DCBDA1" stroke="#7A6046" stroke-width="2"/>
        <path d="M430,320 L440,475 L490,475 L480,320 Z" fill="#B29C80" stroke="#7A6046" stroke-width="2"/>

        <!-- Royal Golden-Ochre Capture Cords Draped Across Body -->
        <path d="M150,230 C240,260 380,270 490,260" stroke="#C99A43" stroke-width="4.5" fill="none"/>
        <path d="M200,160 C260,250 310,350 330,430" stroke="#C99A43" stroke-width="4" fill="none"/>

        <!-- Head Turned Back Towards the Forest (Looking Back Left) -->
        <path d="M170,180 C150,115 195,55 265,55 C315,55 345,95 335,155 C315,195 265,225 215,215 Z" fill="url(#white-elephant-body)" stroke="#8C6A4B" stroke-width="2.5"/>
        <path d="M245,105 C295,115 330,175 310,240 C290,285 245,280 230,235 Z" fill="#D5C2A9" stroke="#8C6A4B" stroke-width="2.5"/>

        <!-- Heartbroken, Grieving Almond Eye (Tears of Sorrow for Blind Parents) -->
        <ellipse cx="205" cy="138" rx="14" ry="8" fill="#FFF9F0" stroke="#4A3528" stroke-width="2"/>
        <circle cx="204" cy="138" r="5" fill="#241B14"/>
        <circle cx="202" cy="136" r="1.5" fill="#FFFFFF"/>
        <!-- Curved downcast eyelid -->
        <path d="M190,132 Q205,124 225,134" stroke="#A84F32" stroke-width="2.5" fill="none"/>
        <!-- Glistening tear line -->
        <path d="M204,146 Q200,165 198,180" stroke="#E6D2AD" stroke-width="1.5" stroke-linecap="round" fill="none"/>

        <!-- Downcast Trunk Drooping in Grief -->
        <path d="M180,200 C150,260 145,340 160,410 C165,430 180,440 195,435" stroke="url(#white-elephant-body)" stroke-width="30" stroke-linecap="round" fill="none"/>
        <path d="M180,200 C150,260 145,340 160,410 C165,430 180,440 195,435" stroke="#7A6046" stroke-width="2" fill="none"/>
      </g>

      <!-- Framing Borders -->
      <rect x="16" y="16" width="1168" height="768" rx="4" fill="none" stroke="#C99A43" stroke-width="1.5" stroke-opacity="0.4"/>
      <rect x="24" y="24" width="1152" height="752" rx="2" fill="none" stroke="#A84F32" stroke-width="0.75" stroke-opacity="0.3"/>
    </svg>'''

    # =============================================================
    # SCENE 04: THE ROYAL COURTYARD
    # Palace pavilion, untouched food foreground, silent elephant, listening king
    # =============================================================
    scene_04 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
      {svg_defs}
      <!-- Background Palace Hall -->
      <rect width="1200" height="800" fill="url(#palace-bg)"/>
      <rect width="1200" height="800" fill="url(#plaster-grain)"/>

      <!-- 5th-Century Gupta-Vakataka Architectural Pillars & Capital Brackets -->
      <!-- Left Pavilion Pillar -->
      <g fill="#42291C" stroke="#684530" stroke-width="2">
        <!-- Capital Bracket with Carved Makara / Foliated Curve -->
        <path d="M80,100 L240,100 L220,150 L180,170 L140,170 L100,150 Z"/>
        <circle cx="160" cy="135" r="14" fill="#C99A43"/>
        <!-- Fluted Shaft -->
        <rect x="135" y="170" width="50" height="550" fill="#382216"/>
        <line x1="150" y1="170" x2="150" y2="720" stroke="#503322" stroke-width="2"/>
        <line x1="170" y1="170" x2="170" y2="720" stroke="#503322" stroke-width="2"/>
        <!-- Base Plinth -->
        <rect x="110" y="720" width="100" height="40" fill="#2A180E"/>
      </g>

      <!-- Right Pavilion Pillar Behind King -->
      <g fill="#42291C" stroke="#684530" stroke-width="2">
        <path d="M960,100 L1120,100 L1100,150 L1060,170 L1020,170 L980,150 Z"/>
        <circle cx="1040" cy="135" r="14" fill="#C99A43"/>
        <rect x="1015" y="170" width="50" height="550" fill="#382216"/>
        <rect x="990" y="720" width="100" height="40" fill="#2A180E"/>
      </g>

      <!-- Ornate Architrave & Draped Royal Textile Canopy -->
      <rect x="0" y="60" width="1200" height="40" fill="#2E1C12" stroke="#C99A43" stroke-width="2"/>
      <g fill="#A84F32">
        <path d="M200,100 Q260,140 320,100 Z"/>
        <path d="M320,100 Q380,140 440,100 Z"/>
        <path d="M440,100 Q500,140 560,100 Z"/>
        <path d="M560,100 Q620,140 680,100 Z"/>
        <path d="M680,100 Q740,140 800,100 Z"/>
        <path d="M800,100 Q860,140 920,100 Z"/>
        <path d="M920,100 Q980,140 1040,100 Z"/>
      </g>

      <!-- The Thoughtful King Seated on Lion Throne (Right) -->
      <g id="scene4-king" transform="translate(820, 240)">
        <!-- Carved Lion Throne (Simhasana) in Gold and Teak -->
        <rect x="30" y="240" width="220" height="240" fill="#4B3120" stroke="#C99A43" stroke-width="3"/>
        <circle cx="45" cy="240" r="18" fill="#C99A43"/>
        <circle cx="235" cy="240" r="18" fill="#C99A43"/>
        <!-- Ornate Silk Cushion in Terracotta -->
        <ellipse cx="140" cy="245" rx="90" ry="22" fill="#A84F32" stroke="#682918" stroke-width="2"/>

        <!-- Regal Seated Posture (Lalitasana - one leg resting, one gracefully pendent) -->
        <path d="M70,250 C50,290 60,380 90,420 L120,420 C100,380 95,300 120,260 Z" fill="#B37C50"/>
        <path d="M120,250 C140,290 190,320 220,320 L240,290 C200,280 160,250 140,250 Z" fill="#B37C50"/>

        <!-- Pleated Fine Silk Royal Uttariya (Drapery) with Gold Borders -->
        <path d="M70,180 C50,230 70,300 110,320 C140,300 170,310 200,280 C210,230 190,190 170,180 Z" fill="#FAF5EC" stroke="#C99A43" stroke-width="2"/>
        <path d="M85,190 Q110,260 135,315" stroke="#C99A43" stroke-width="1.5" fill="none"/>

        <!-- Graceful Slender Torso Adorned with Pearl Necklaces (Hara) -->
        <path d="M80,85 C70,120 70,160 85,185 C115,195 155,195 175,180 C185,150 180,115 165,85 Z" fill="#B37C50" stroke="#684223" stroke-width="2"/>
        <!-- Ajanta Pearl Collar & Sacred Cord -->
        <path d="M100,95 Q125,130 150,95" stroke="#FFFDF8" stroke-width="3" stroke-dasharray="3,3" fill="none"/>
        <path d="M95,115 Q125,165 155,115" stroke="#C99A43" stroke-width="2" stroke-dasharray="4,4" fill="none"/>

        <!-- Hand supporting chin in profound, empathetic contemplation -->
        <path d="M150,140 L180,95 L165,80 L135,130 Z" fill="#A47047" stroke="#684223" stroke-width="1.5"/>
        <circle cx="170" cy="80" r="10" fill="#A47047"/>

        <!-- Noble Head, High Ajanta Crown (Kiritamukuta) -->
        <circle cx="125" cy="45" r="28" fill="#B37C50" stroke="#684223" stroke-width="2"/>
        <!-- Towering Jeweled Gold Crown -->
        <path d="M100,30 L105,-40 L125,-60 L145,-40 L150,30 Z" fill="#E5B456" stroke="#8A6318" stroke-width="2.5"/>
        <circle cx="125" cy="-20" r="8" fill="#A84F32"/>
        <circle cx="125" cy="5" r="6" fill="#68765A"/>

        <!-- Contemplative, Perceptive Eyes Listening Deeply -->
        <ellipse cx="112" cy="42" rx="6" ry="3.5" fill="#FFF9F0" stroke="#4A3528" stroke-width="1.5"/>
        <circle cx="110" cy="42" r="2.5" fill="#241B14"/>
        <path d="M104,36 Q112,32 122,37" stroke="#684223" stroke-width="2" fill="none"/>
      </g>

      <!-- The Silent, Mourning White Elephant (Center Left) -->
      <g id="scene4-silent-elephant" transform="translate(240, 240)">
        <path d="M180,260 C160,180 220,115 310,105 C410,95 480,135 510,215 C530,275 510,375 470,425 L390,425 C400,345 390,305 330,295 C270,285 210,325 190,425 L120,425 C110,355 130,295 180,260 Z" fill="url(#white-elephant-body)"/>

        <!-- Legs Standing Still in Fasting Vigil -->
        <path d="M300,310 L315,475 L375,475 L365,310 Z" fill="#C2AC90" stroke="#7A6046" stroke-width="2"/>
        <path d="M220,320 L230,475 L290,475 L280,320 Z" fill="#DCBDA1" stroke="#7A6046" stroke-width="2"/>

        <!-- Bowed Head in Complete Fasting Grief -->
        <path d="M220,210 C180,165 210,95 280,95 C330,95 360,135 345,195 C325,235 275,265 235,255 Z" fill="url(#white-elephant-body)" stroke="#8C6A4B" stroke-width="2.5"/>
        <path d="M280,135 C330,145 365,205 345,270 C325,315 280,310 265,265 Z" fill="#D5C2A9" stroke="#8C6A4B" stroke-width="2.5"/>

        <!-- Downcast, Starving Eye Fixed on Memory of Parents -->
        <ellipse cx="235" cy="170" rx="13" ry="7" fill="#FFF9F0" stroke="#4A3528" stroke-width="2"/>
        <circle cx="233" cy="170" r="4.5" fill="#241B14"/>
        <path d="M220,162 Q235,155 252,165" stroke="#A84F32" stroke-width="2.5" fill="none"/>

        <!-- Motionless Trunk Refusing Sustenance -->
        <path d="M220,230 C190,290 190,370 210,430 C215,445 230,450 240,440" stroke="url(#white-elephant-body)" stroke-width="28" stroke-linecap="round" fill="none"/>
        <path d="M220,230 C190,290 190,370 210,430 C215,445 230,450 240,440" stroke="#7A6046" stroke-width="2" fill="none"/>
      </g>

      <!-- Foreground: The Untouched Royal Feasts (Heaped Platters of Sugarcane, Sweet Rice & Lotus Stalks) -->
      <g id="scene4-untouched-feast" transform="translate(380, 640)">
        <!-- Massive Golden Feast Platter (Thali) -->
        <ellipse cx="140" cy="80" rx="140" ry="32" fill="#C99A43" stroke="#8A6318" stroke-width="3"/>
        <ellipse cx="140" cy="76" rx="125" ry="26" fill="#E5B456"/>

        <!-- Untouched Bundles of Tender Sugarcane Stalks -->
        <rect x="50" y="30" width="18" height="50" rx="3" fill="#68765A" stroke="#3D4933" stroke-width="1.5" transform="rotate(-15 50 30)"/>
        <rect x="75" y="25" width="18" height="55" rx="3" fill="#7E9169" stroke="#3D4933" stroke-width="1.5" transform="rotate(-5 75 25)"/>
        <rect x="100" y="25" width="18" height="55" rx="3" fill="#68765A" stroke="#3D4933" stroke-width="1.5" transform="rotate(10 100 25)"/>

        <!-- Heaped Wild Fruits & Honey Cakes -->
        <circle cx="140" cy="55" r="14" fill="#A84F32"/>
        <circle cx="165" cy="60" r="12" fill="#C99A43"/>
        <circle cx="120" cy="65" r="11" fill="#A96F66"/>
        <circle cx="185" cy="65" r="10" fill="#68765A"/>

        <!-- Water Pitcher (Kamandalu / Kalasha) in Burnished Brass -->
        <ellipse cx="260" cy="60" rx="28" ry="12" fill="#C99A43" stroke="#855B18" stroke-width="2"/>
        <path d="M240,60 C235,30 250,10 260,10 C270,10 285,30 280,60 Z" fill="#E5B456" stroke="#855B18" stroke-width="2"/>
        <circle cx="260" cy="5" r="6" fill="#C99A43"/>
      </g>

      <!-- Framing Borders -->
      <rect x="16" y="16" width="1168" height="768" rx="4" fill="none" stroke="#C99A43" stroke-width="1.5" stroke-opacity="0.4"/>
      <rect x="24" y="24" width="1152" height="752" rx="2" fill="none" stroke="#A84F32" stroke-width="0.75" stroke-opacity="0.3"/>
    </svg>'''

    # =============================================================
    # SCENE 05: THE WAY HOME / REUNION
    # Same bent Sal tree motif as scene 1, warm dawn, joyful embrace
    # =============================================================
    scene_05 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
      {svg_defs}
      <!-- Warm Radiant Dawn Sunrise Background -->
      <rect width="1200" height="800" fill="url(#dawn-bg)"/>
      <rect width="1200" height="800" fill="url(#plaster-grain)"/>

      <!-- Golden Warm Dawn Light Breaking Over Mountain Glade -->
      <circle cx="580" cy="280" r="260" fill="#E5B456" opacity="0.12"/>
      <path d="M0,480 Q240,380 500,430 T1000,400 L1200,430 L1200,800 L0,800 Z" fill="#25170F"/>
      <path d="M0,540 Q280,480 580,510 T1200,480 L1200,800 L0,800 Z" fill="#321E14"/>

      <!-- The Very Same Ancient Bent Sal Tree as Scene 1 (Visual Continuity Anchor) -->
      <path d="M60,800 C75,660 55,530 110,410 C145,330 210,280 290,230 C380,180 500,200 610,170 C600,195 540,225 450,245 C370,265 295,315 250,385 C205,470 215,630 220,800 Z" fill="url(#tree-bark)"/>
      <path d="M210,340 C270,305 365,295 425,260 C410,278 355,320 300,342 Z" fill="#38261C"/>

      <!-- Luminous Blossoming Foliage Canopy (Restored Life & Warmth) -->
      <g fill="#536642" stroke="#2D3823" stroke-width="2">
        <ellipse cx="320" cy="190" rx="95" ry="50"/>
        <ellipse cx="450" cy="165" rx="115" ry="60"/>
        <ellipse cx="570" cy="155" rx="85" ry="45"/>
        <ellipse cx="240" cy="235" rx="85" ry="48"/>
      </g>
      <g fill="#7A8F65" stroke="#485938" stroke-width="1.5">
        <ellipse cx="340" cy="175" rx="75" ry="38"/>
        <ellipse cx="465" cy="150" rx="90" ry="42"/>
        <ellipse cx="550" cy="145" rx="65" ry="32"/>
      </g>

      <!-- Cascading Pink Madder & Lotus Blossoms Celebrating Return -->
      <g fill="#A96F66" stroke="#68342C" stroke-width="1.5">
        <circle cx="280" cy="280" r="10"/>
        <circle cx="360" cy="260" r="12"/>
        <circle cx="440" cy="230" r="11"/>
        <circle cx="510" cy="210" r="9"/>
        <circle cx="390" cy="310" r="8"/>
        <circle cx="480" cy="290" r="10"/>
      </g>

      <!-- The Venerable Parents Lifted in Joyous Recognition (Right) -->
      <g id="scene5-parents" transform="translate(680, 340)">
        <!-- Mother with Trunk Lifted in Delight -->
        <path d="M120,240 C100,180 140,110 200,85 C270,55 350,65 400,105 C450,145 460,220 450,280 L400,280 C390,210 340,155 280,155 C220,155 160,195 140,260 Z" fill="url(#parent-elephant-grad)"/>
        <circle cx="330" cy="115" r="45" fill="#4B3A30"/>
        <!-- Joyful lifted ear -->
        <path d="M350,80 C390,90 415,145 395,190 C375,225 345,215 335,185 Z" fill="#584639" stroke="#362920" stroke-width="2"/>
        <!-- Tender lifted trunk twining with returning son -->
        <path d="M290,120 C240,100 160,130 90,180 C40,220 -20,230 -80,210" stroke="#48382E" stroke-width="16" stroke-linecap="round" fill="none"/>

        <!-- Father Radiant with Raised Trunk in Embrace -->
        <path d="M50,300 C30,230 60,160 120,120 C200,75 310,80 370,130 C410,175 430,250 420,315 C330,325 180,325 50,300 Z" fill="url(#parent-elephant-grad)"/>
        <circle cx="100" cy="160" r="65" fill="#584639"/>
        <!-- Soft peaceful blind eyes weeping tears of happiness -->
        <path d="M85,165 Q105,157 125,168" stroke="#201610" stroke-width="4.5" stroke-linecap="round" fill="none"/>
        <path d="M98,175 Q95,195 93,210" stroke="#E6D2AD" stroke-width="1.5" stroke-linecap="round" fill="none"/>

        <!-- Father's Trunk entwined with son's trunk in filial reunion -->
        <path d="M60,180 C10,190 -60,190 -120,170 C-160,155 -190,170 -210,200" stroke="#584639" stroke-width="22" stroke-linecap="round" fill="none"/>
      </g>

      <!-- The Bodhisattva White Elephant Bounding Joyfully Home (Center Left) -->
      <g id="scene5-returning-elephant" transform="translate(190, 240)">
        <!-- Resplendent Ivory Body with Dynamic Energetic Cadence -->
        <path d="M180,250 C160,170 220,105 310,95 C410,85 480,125 510,205 C530,265 510,365 470,415 L390,415 C400,335 390,295 330,285 C270,275 210,315 190,415 L120,415 C110,345 130,285 180,250 Z" fill="url(#white-elephant-body)"/>

        <!-- Eager forward bounding legs -->
        <path d="M310,300 L340,465 L400,465 L380,300 Z" fill="#C2AC90" stroke="#7A6046" stroke-width="2"/>
        <path d="M220,310 L210,465 L270,465 L280,310 Z" fill="#DCBDA1" stroke="#7A6046" stroke-width="2"/>
        <path d="M430,310 L460,465 L510,465 L490,310 Z" fill="#B29C80" stroke="#7A6046" stroke-width="2"/>

        <!-- High Elevated Head in Radiant Joy -->
        <path d="M280,160 C260,95 305,35 375,35 C425,35 455,75 445,135 C425,175 375,205 325,195 Z" fill="url(#white-elephant-body)" stroke="#8C6A4B" stroke-width="2.5"/>
        <path d="M330,85 C380,95 415,155 395,220 C375,265 330,260 315,215 Z" fill="#D5C2A9" stroke="#8C6A4B" stroke-width="2.5"/>

        <!-- Radiant, Shining Lotus Eye Filled with Bliss -->
        <ellipse cx="370" cy="115" rx="14" ry="8" fill="#FFFDF8" stroke="#4A3528" stroke-width="2"/>
        <circle cx="372" cy="115" r="5" fill="#241B14"/>
        <circle cx="374" cy="113" r="2" fill="#FFFFFF"/>
        <path d="M355,106 Q370,98 390,107" stroke="#A84F32" stroke-width="2.5" fill="none"/>

        <!-- Gleaming White Tusk Reaching Towards Parents -->
        <path d="M395,175 C430,205 470,210 495,195 C500,190 490,175 445,160 Z" fill="#FFFDF5" stroke="#BAAA90" stroke-width="2"/>

        <!-- Trunk passionately embracing parents' trunks -->
        <path d="M380,175 C440,220 520,240 600,210 C650,190 700,210 740,240" stroke="url(#white-elephant-body)" stroke-width="32" stroke-linecap="round" fill="none"/>
        <path d="M380,175 C440,220 520,240 600,210 C650,190 700,210 740,240" stroke="#7A6046" stroke-width="2.5" fill="none"/>
      </g>

      <!-- Forest Floor with Blooming Water Lilies -->
      <path d="M0,720 Q300,680 600,710 T1200,690 L1200,800 L0,800 Z" fill="#1C140D"/>
      <ellipse cx="560" cy="755" rx="200" ry="35" fill="#1A2016" stroke="#3D5034" stroke-width="2"/>
      <ellipse cx="510" cy="750" rx="40" ry="12" fill="#4B613F"/>
      <ellipse cx="610" cy="760" rx="45" ry="14" fill="#3D5034"/>
      <circle cx="560" cy="745" r="8" fill="#A96F66"/>
      <circle cx="630" cy="752" r="7" fill="#C99A43"/>

      <!-- Framing Borders -->
      <rect x="16" y="16" width="1168" height="768" rx="4" fill="none" stroke="#C99A43" stroke-width="1.5" stroke-opacity="0.4"/>
      <rect x="24" y="24" width="1152" height="752" rx="2" fill="none" stroke="#A84F32" stroke-width="0.75" stroke-opacity="0.3"/>
    </svg>'''

    files = [
        ('assets/illustrations/scene-01-forest.svg', scene_01),
        ('assets/illustrations/scene-02-stranger.svg', scene_02),
        ('assets/illustrations/scene-03-betrayal.svg', scene_03),
        ('assets/illustrations/scene-04-palace.svg', scene_04),
        ('assets/illustrations/scene-05-return.svg', scene_05),
    ]

    for path, content in files:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print(f'Wrote {path} ({len(content)} bytes)')

if __name__ == '__main__':
    create_illustrations()
