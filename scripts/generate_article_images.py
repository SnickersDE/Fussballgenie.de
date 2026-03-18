from pathlib import Path


ROOT = Path("/Users/florian/fussballblog")
OUT = ROOT / "static" / "images" / "articles"
OUT.mkdir(parents=True, exist_ok=True)

SCENES = {
    "psg-schlaegt-chelsea-30-und-dominiert": {
        "title": "PSG BALANCE SHIFT",
        "sub": "PRESSING + RESTVERTEIDIGUNG",
        "colors": ("#111827", "#4c1d95", "#7e22ce"),
        "motif": """
  <g opacity=".9">
    <rect x="990" y="150" width="480" height="300" rx="20" fill="rgba(255,255,255,.1)"/>
    <path d="M1030 380 L1150 270 L1250 330 L1400 210" stroke="#f472b6" stroke-width="12" fill="none" stroke-linecap="round"/>
    <circle cx="1150" cy="270" r="16" fill="#f472b6"/>
    <circle cx="1250" cy="330" r="16" fill="#f472b6"/>
    <circle cx="1400" cy="210" r="16" fill="#f472b6"/>
    <rect x="1040" y="190" width="100" height="26" rx="6" fill="#f472b6"/>
  </g>""",
    },
    "bayern-atalanta-61-vorsprung-analyse": {
        "title": "BAYERN 6:1",
        "sub": "RISIKO + WUCHT IM STRAFRAUM",
        "colors": ("#1f2937", "#7f1d1d", "#dc2626"),
        "motif": """
  <g>
    <circle cx="1210" cy="300" r="220" fill="rgba(255,255,255,.07)"/>
    <text x="1080" y="350" fill="#fecaca" font-family="Barlow Condensed, Arial" font-size="170" font-weight="900">6:1</text>
    <path d="M1030 430 L1400 430" stroke="#fecaca" stroke-width="8"/>
    <circle cx="390" cy="290" r="70" fill="rgba(255,255,255,.12)"/>
    <path d="M390 230 L420 280 L395 340 L345 340 L320 280 Z" fill="#fff"/>
  </g>""",
    },
    "arsenal-leverkusen-20-analyse": {
        "title": "ARSENAL 2:0",
        "sub": "KONTROLLE IM HALBRAUM",
        "colors": ("#0f172a", "#7f1d1d", "#b91c1c"),
        "motif": """
  <g>
    <rect x="950" y="140" width="520" height="320" rx="26" fill="rgba(255,255,255,.08)"/>
    <text x="1050" y="335" fill="#fee2e2" font-family="Barlow Condensed, Arial" font-size="150" font-weight="900">2:0</text>
    <path d="M240 540 C440 380, 620 380, 830 520" stroke="#fca5a5" stroke-width="14" fill="none" stroke-linecap="round"/>
    <circle cx="830" cy="520" r="18" fill="#fca5a5"/>
  </g>""",
    },
    "hsv-koeln-11-analyse": {
        "title": "HSV 1:1 KÖLN",
        "sub": "PUNKT GEHOLT, KONTROLLE VERLOREN",
        "colors": ("#111827", "#1e3a8a", "#0ea5e9"),
        "motif": """
  <g>
    <rect x="1020" y="180" width="420" height="240" rx="18" fill="rgba(255,255,255,.09)"/>
    <text x="1090" y="338" fill="#dbeafe" font-family="Barlow Condensed, Arial" font-size="130" font-weight="900">1:1</text>
    <rect x="190" y="190" width="420" height="420" rx="28" fill="rgba(255,255,255,.08)"/>
    <path d="M250 520 L340 390 L430 470 L560 300" stroke="#7dd3fc" stroke-width="10" fill="none"/>
  </g>""",
    },
    "dresden-muenster-60-klartext": {
        "title": "DRESDEN 6:0",
        "sub": "VOLLTREFFER-SPIELTAG",
        "colors": ("#1f2937", "#7c2d12", "#ea580c"),
        "motif": """
  <g>
    <text x="980" y="380" fill="#ffedd5" font-family="Barlow Condensed, Arial" font-size="190" font-weight="900">6:0</text>
    <g transform="translate(300,190)">
      <circle cx="0" cy="0" r="58" fill="#fff" opacity=".95"/>
      <circle cx="0" cy="0" r="18" fill="#111"/>
      <path d="M-45 45 L-20 10 L20 10 L45 45 Z" fill="#111"/>
    </g>
    <path d="M200 640 C420 560, 640 560, 860 640" stroke="#fed7aa" stroke-width="14" fill="none"/>
  </g>""",
    },
    "schalke-hannover-22-analyse": {
        "title": "SCHALKE 2:2",
        "sub": "FÜHRUNG VERSPIELT",
        "colors": ("#0f172a", "#1e40af", "#0284c7"),
        "motif": """
  <g>
    <rect x="930" y="150" width="530" height="320" rx="20" fill="rgba(255,255,255,.08)"/>
    <text x="1030" y="340" fill="#dbeafe" font-family="Barlow Condensed, Arial" font-size="150" font-weight="900">2:2</text>
    <path d="M240 300 L600 300" stroke="#bfdbfe" stroke-width="10"/>
    <path d="M600 300 L560 260 M600 300 L560 340" stroke="#bfdbfe" stroke-width="10" fill="none"/>
    <path d="M600 420 L240 420" stroke="#bfdbfe" stroke-width="10"/>
    <path d="M240 420 L280 380 M240 420 L280 460" stroke="#bfdbfe" stroke-width="10" fill="none"/>
  </g>""",
    },
    "stuttgart-leipzig-10-undav": {
        "title": "VfB 1:0 LEIPZIG",
        "sub": "UNDAV ENTSCHEIDET",
        "colors": ("#111827", "#7f1d1d", "#ef4444"),
        "motif": """
  <g>
    <circle cx="1180" cy="290" r="190" fill="rgba(255,255,255,.09)"/>
    <text x="1100" y="330" fill="#fee2e2" font-family="Barlow Condensed, Arial" font-size="130" font-weight="900">1:0</text>
    <path d="M260 560 C390 470, 530 470, 660 560" stroke="#fecaca" stroke-width="12" fill="none"/>
    <circle cx="660" cy="560" r="16" fill="#fecaca"/>
    <rect x="220" y="220" width="180" height="260" rx="20" fill="rgba(255,255,255,.12)"/>
  </g>""",
    },
    "dortmund-augsburg-20-klartext": {
        "title": "BVB 2:0 FCA",
        "sub": "SIEG MIT BAUSTELLEN",
        "colors": ("#111827", "#ca8a04", "#facc15"),
        "motif": """
  <g>
    <rect x="980" y="170" width="460" height="270" rx="18" fill="rgba(0,0,0,.2)"/>
    <text x="1065" y="335" fill="#fef08a" font-family="Barlow Condensed, Arial" font-size="140" font-weight="900">2:0</text>
    <polygon points="280,620 390,430 500,620" fill="rgba(254,240,138,.22)"/>
    <polygon points="440,620 550,390 660,620" fill="rgba(254,240,138,.16)"/>
  </g>""",
    },
    "city-verliert-gegen-real-halbraeume-offen": {
        "title": "CITY VS REAL",
        "sub": "HALBRÄUME OFFEN",
        "colors": ("#082f49", "#1e3a8a", "#7c3aed"),
        "motif": """
  <g>
    <rect x="230" y="170" width="620" height="340" rx="24" fill="rgba(255,255,255,.08)"/>
    <line x1="540" y1="170" x2="540" y2="510" stroke="rgba(255,255,255,.35)" stroke-width="6"/>
    <rect x="260" y="210" width="240" height="260" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="5"/>
    <rect x="580" y="210" width="240" height="260" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="5"/>
    <path d="M1020 250 L1320 250 L1320 420 L1020 420 Z" fill="rgba(255,255,255,.08)"/>
    <text x="1085" y="360" fill="#ddd6fe" font-family="Barlow Condensed, Arial" font-size="110" font-weight="900">2:1</text>
  </g>""",
    },
    "real-madrid-schlaegt-mancity-21-rueckspiel": {
        "title": "REAL SCHLÄGT CITY",
        "sub": "K.O.-ABEND 2:1",
        "colors": ("#0f172a", "#1d4ed8", "#22d3ee"),
        "motif": """
  <g>
    <path d="M1180 130 L1230 220 L1330 220 L1250 285 L1280 380 L1180 325 L1080 380 L1110 285 L1030 220 L1130 220 Z" fill="rgba(255,255,255,.22)"/>
    <text x="1045" y="500" fill="#cffafe" font-family="Barlow Condensed, Arial" font-size="145" font-weight="900">2:1</text>
    <circle cx="300" cy="620" r="130" fill="rgba(255,255,255,.11)"/>
    <path d="M240 620 L360 620 M300 560 L300 680" stroke="#e0f2fe" stroke-width="10"/>
  </g>""",
    },
    "statistik-schock-scorer-rueckrunde-aktuell": {
        "title": "SCORER RADAR",
        "sub": "DATEN DER RÜCKRUNDE",
        "colors": ("#111827", "#0f766e", "#14b8a6"),
        "motif": """
  <g>
    <rect x="930" y="130" width="520" height="360" rx="24" fill="rgba(255,255,255,.08)"/>
    <line x1="980" y1="430" x2="1410" y2="430" stroke="rgba(255,255,255,.35)" stroke-width="5"/>
    <rect x="1000" y="300" width="70" height="130" fill="#99f6e4"/>
    <rect x="1100" y="250" width="70" height="180" fill="#5eead4"/>
    <rect x="1200" y="220" width="70" height="210" fill="#2dd4bf"/>
    <rect x="1300" y="270" width="70" height="160" fill="#14b8a6"/>
    <circle cx="360" cy="290" r="145" fill="rgba(255,255,255,.09)"/>
    <path d="M260 350 C320 250, 420 250, 470 350" stroke="#99f6e4" stroke-width="12" fill="none"/>
  </g>""",
    },
    "bayern-leverkusen-11-analyse": {
        "title": "BAYERN 1:1 LEVERKUSEN",
        "sub": "SPITZENSPIEL ANALYSE",
        "colors": ("#111827", "#7f1d1d", "#be123c"),
        "motif": """
  <g>
    <rect x="960" y="170" width="470" height="280" rx="22" fill="rgba(255,255,255,.08)"/>
    <text x="1035" y="340" fill="#fecdd3" font-family="Barlow Condensed, Arial" font-size="140" font-weight="900">1:1</text>
    <path d="M230 520 L420 320 L610 520" stroke="#fda4af" stroke-width="12" fill="none"/>
    <path d="M610 520 L780 340" stroke="#fda4af" stroke-width="12" fill="none"/>
    <circle cx="780" cy="340" r="18" fill="#fda4af"/>
  </g>""",
    },
}


def build_svg(slug: str, cfg: dict[str, str]) -> str:
    c1, c2, c3 = cfg["colors"]
    title = cfg["title"]
    sub = cfg["sub"]
    motif = cfg["motif"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="55%" stop-color="{c2}"/>
      <stop offset="100%" stop-color="{c3}"/>
    </linearGradient>
    <radialGradient id="glow" cx="72%" cy="18%" r="70%">
      <stop offset="0%" stop-color="rgba(255,255,255,.22)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </radialGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <rect width="1600" height="900" fill="url(#glow)"/>
  <g opacity=".35">
    <circle cx="140" cy="130" r="180" fill="rgba(255,255,255,.12)"/>
    <circle cx="1550" cy="860" r="260" fill="rgba(255,255,255,.08)"/>
  </g>
  {motif}
  <rect x="0" y="680" width="1600" height="220" fill="rgba(0,0,0,.35)"/>
  <text x="90" y="778" fill="rgba(255,255,255,.95)" font-family="Barlow Condensed, Arial, sans-serif" font-size="88" font-weight="900" letter-spacing="4">{title}</text>
  <text x="90" y="842" fill="rgba(255,255,255,.82)" font-family="Barlow, Arial, sans-serif" font-size="34" font-weight="700" letter-spacing="1.5">{sub}</text>
  <text x="90" y="886" fill="rgba(255,255,255,.65)" font-family="Barlow Condensed, Arial, sans-serif" font-size="24" font-weight="700" letter-spacing="2.5">FUSSBALLGENIE.DE · ORIGINAL ARTWORK</text>
</svg>"""


for slug, cfg in SCENES.items():
    (OUT / f"{slug}.svg").write_text(build_svg(slug, cfg), encoding="utf-8")

print(f"generated {len(SCENES)} diverse images in {OUT}")
