# -*- coding: utf-8 -*-
"""
Placeholder visuals for the Amarimmo demo.

Deliberately ILLUSTRATIONS - architectural-poster style, not photographs and not AI renders.
A buyer looking at a promoter's site reads a photo-real image as the building they will be
handed the keys to, and Amarimmo has not said yet which projects are real. A poster reads as
a poster. They are 3:2 and drop straight out when the real architect renders arrive.
"""
import os, math, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

W, H = 1500, 1000


class P:
    """One palette: sky stops, three building tones (far -> near), sun, sea, ground, ink."""
    def __init__(self, sky, tones, sun, sea, ground, ink):
        self.sky, self.tones, self.sun, self.sea, self.ground, self.ink = sky, tones, sun, sea, ground, ink


PALETTES = {
    "couchant":  P([("#F6C99A", 0.0), ("#E89B6C", .42), ("#C2637A", .74), ("#6E4A78", 1.0)],
                   ["#8C5F72", "#6E4A63", "#4E3550"], "#FFE3B8", "#5B3E64", "#3A2A42", "#241a2b"),
    "mediterranee": P([("#BFE3F2", 0.0), ("#DCEFF7", .45), ("#F6F1E7", 1.0)],
                      ["#C7D6DD", "#A9BEC9", "#7E97A6"], "#FFFFFF", "#7FB3CC", "#EDE6D8", "#33454f"),
    "sable":     P([("#F3E4CE", 0.0), ("#F8EFE0", .5), ("#FBF7F0", 1.0)],
                   ["#DCC9AE", "#C4A886", "#9C7E5C"], "#FFF6E4", "#D9C7AE", "#EFE6D5", "#4a3a28"),
    "nuit":      P([("#20304A", 0.0), ("#33465F", .5), ("#6C6379", 1.0)],
                   ["#3E4C63", "#2E3A4D", "#1F2938"], "#F2D9A8", "#26364B", "#1A2230", "#0f1620"),
    "olive":     P([("#DCE4D2", 0.0), ("#EDF0E4", .5), ("#F8F7EE", 1.0)],
                   ["#BDC7B0", "#9EAB90", "#79876C"], "#FFFFFF", "#9FB8AE", "#E7E7D8", "#38402e"),
}


def defs(pal, uid):
    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for c, o in pal.sky)
    return (f'<defs>'
            f'<linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1">{stops}</linearGradient>'
            f'<radialGradient id="glow{uid}" cx=".5" cy=".5" r=".5">'
            f'<stop offset="0" stop-color="{pal.sun}" stop-opacity=".85"/>'
            f'<stop offset="1" stop-color="{pal.sun}" stop-opacity="0"/></radialGradient>'
            f'<filter id="grain{uid}" x="0" y="0" width="100%" height="100%">'
            f'<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"/>'
            f'<feColorMatrix type="saturate" values="0"/>'
            f'<feComponentTransfer><feFuncA type="linear" slope=".055"/></feComponentTransfer></filter>'
            f'</defs>')


def tower(x, w, top, base, tone, ink, floors, rnd, rail=True):
    """A flat silhouette block with a balcony rhythm drawn as thin light lines."""
    h = base - top
    o = [f'<rect x="{x:.0f}" y="{top:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{tone}"/>']
    # crown setback, keeps the skyline from being a row of identical bricks
    if rnd.random() < .55:
        cw = w * rnd.uniform(.35, .7)
        ch = rnd.uniform(18, 46)
        o.append(f'<rect x="{x + (w-cw)/2:.0f}" y="{top-ch:.0f}" width="{cw:.0f}" height="{ch:.0f}" fill="{tone}"/>')
    fh = h / floors
    for f in range(1, floors):
        y = top + f * fh
        o.append(f'<line x1="{x:.0f}" y1="{y:.1f}" x2="{x+w:.0f}" y2="{y:.1f}" '
                 f'stroke="#FFFFFF" stroke-width="1.1" opacity=".16"/>')
        if rail and f % 2 == 0:
            inset = w * .1
            o.append(f'<line x1="{x+inset:.0f}" y1="{y-fh*.28:.1f}" x2="{x+w-inset:.0f}" y2="{y-fh*.28:.1f}" '
                     f'stroke="#FFFFFF" stroke-width="2" opacity=".26"/>')
    # a few lit windows for life
    for _ in range(int(floors * 1.4)):
        f = rnd.randrange(floors)
        bw = w * rnd.uniform(.11, .2)
        bx = x + rnd.uniform(w * .08, w * .92 - bw)
        by = top + f * fh + fh * .3
        o.append(f'<rect x="{bx:.0f}" y="{by:.1f}" width="{bw:.0f}" height="{fh*.34:.1f}" '
                 f'fill="#FFFFFF" opacity="{rnd.uniform(.1,.34):.2f}"/>')
    # vertical shadow edge
    o.append(f'<rect x="{x+w-w*0.16:.0f}" y="{top:.0f}" width="{w*0.16:.0f}" height="{h:.0f}" fill="{ink}" opacity=".10"/>')
    return "".join(o)


def palm_silhouette(cx, base, scale, colour, opacity=1.0):
    rnd = random.Random(int(cx))
    trunk_h = 250 * scale
    lean = rnd.uniform(-22, 22) * scale
    top_x, top_y = cx + lean, base - trunk_h
    o = [f'<path d="M{cx-9*scale:.0f},{base} Q{cx+lean*.3:.0f},{base-trunk_h*.55:.0f} {top_x:.0f},{top_y:.0f} '
         f'L{top_x+7*scale:.0f},{top_y:.0f} Q{cx+lean*.3+9*scale:.0f},{base-trunk_h*.55:.0f} {cx+9*scale:.0f},{base} Z" '
         f'fill="{colour}" opacity="{opacity}"/>']
    for i in range(9):
        a = math.pi * (0.06 + 0.88 * i / 8)
        L = 120 * scale * rnd.uniform(.75, 1.15)
        ex, ey = top_x - math.cos(a) * L, top_y - math.sin(a) * L * .62 + 26 * scale
        mx, my = (top_x + ex) / 2, (top_y + ey) / 2 - 46 * scale
        o.append(f'<path d="M{top_x:.0f},{top_y:.0f} Q{mx:.0f},{my:.0f} {ex:.0f},{ey:.0f} '
                 f'Q{mx:.0f},{my+15*scale:.0f} {top_x:.0f},{top_y+5*scale:.0f} Z" fill="{colour}" opacity="{opacity}"/>')
    return "".join(o)


def scene(name, pal_key, kind, seed, label):
    pal = PALETTES[pal_key]
    rnd = random.Random(seed)
    uid = seed
    horizon = H * (0.72 if kind == "sea" else 0.78)

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'preserveAspectRatio="xMidYMid slice" role="img" aria-label="{label}">',
         defs(pal, uid),
         f'<rect width="{W}" height="{H}" fill="url(#sky{uid})"/>']

    # sun
    sx, sy, sr = W * rnd.uniform(.58, .82), H * rnd.uniform(.20, .34), rnd.uniform(78, 122)
    s.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{sr*3.4:.0f}" fill="url(#glow{uid})"/>')
    s.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{sr:.0f}" fill="{pal.sun}" opacity=".92"/>')

    # far hills
    hy = horizon - rnd.uniform(60, 120)
    pts = " ".join(f"{x},{hy - 44*math.sin(x/W*math.pi*rnd.uniform(1.4,2.4)) - rnd.uniform(0,16):.0f}"
                   for x in range(0, W + 60, 60))
    s.append(f'<polygon points="0,{horizon} {pts} {W},{horizon}" fill="{pal.tones[0]}" opacity=".55"/>')

    # three depth planes of buildings
    # Three depth planes. Each one sits on its own base line - without that offset the
    # planes share a horizon and the whole thing flattens into a single row of blocks.
    plans = [(pal.tones[0], .60, (140, 250), (5, 9),  0.55, -78),
             (pal.tones[1], .82, (200, 360), (6, 12), 0.78, -34),
             (pal.tones[2], 1.0, (250, 460), (7, 14), 1.0,    6)]
    for tone, op, hrange, frange, scale, dy in plans:
        base = horizon + dy
        x = -rnd.uniform(0, 120)
        s.append(f'<g opacity="{op}">')
        while x < W + 60:
            w = rnd.uniform(90, 210) * (0.8 + scale * 0.4)
            h = rnd.uniform(*hrange)
            s.append(tower(x, w, base - h, base, tone, pal.ink,
                           rnd.randint(*frange), rnd, rail=scale > 0.7))
            x += w + rnd.uniform(-14, 34)
        s.append('</g>')

    # ground / sea
    if kind == "sea":
        s.append(f'<rect x="0" y="{horizon}" width="{W}" height="{H-horizon}" fill="{pal.sea}"/>')
        for i in range(26):
            y = horizon + 18 + i * ((H - horizon) / 26)
            lw = rnd.uniform(40, 300)
            lx = rnd.uniform(0, W - lw)
            s.append(f'<rect x="{lx:.0f}" y="{y:.0f}" width="{lw:.0f}" height="2.4" fill="#FFFFFF" '
                     f'opacity="{rnd.uniform(.06,.22):.2f}"/>')
        s.append(f'<rect x="{sx-70:.0f}" y="{horizon}" width="140" height="{H-horizon}" fill="{pal.sun}" opacity=".14"/>')
    else:
        s.append(f'<rect x="0" y="{horizon}" width="{W}" height="{H-horizon}" fill="{pal.ground}"/>')
        s.append(f'<ellipse cx="{W*0.5:.0f}" cy="{horizon+8:.0f}" rx="{W*0.62:.0f}" ry="26" fill="{pal.ink}" opacity=".10"/>')

    # Palms were here and they read as sticks at this scale - a clean skyline is
    # stronger than a badly drawn tree. Left out on purpose.

    s.append(f'<rect width="{W}" height="{H}" filter="url(#grain{uid})" opacity=".5"/>')
    s.append("</svg>")

    path = os.path.join(OUT, name + ".svg")
    open(path, "w", encoding="utf-8").write("".join(s))
    return path


SCENES = [
    ("hero-dz",         "couchant",     "land", 101, "Residences Amarimmo en Algerie"),
    ("hero-es",         "mediterranee", "sea",  202, "Residences Amarimmo en Espagne"),
    ("dz-oran-front",   "mediterranee", "sea",  303, "Residence front de mer a Oran"),
    ("dz-alger-hydra",  "sable",        "land", 404, "Residence haut standing a Alger"),
    ("dz-oran-parc",    "olive",        "land", 505, "Residence avec parc a Oran"),
    ("dz-alger-tour",   "nuit",         "land", 606, "Tour residentielle a Alger"),
    ("es-costa",        "mediterranee", "sea",  707, "Residence Costa del Sol"),
    ("es-andalousie",   "sable",        "land", 808, "Villas en Andalousie"),
    ("es-barcelona",    "olive",        "land", 909, "Immeuble a Barcelone"),
    ("es-alicante",     "couchant",     "sea",  111, "Residence a Alicante"),
    # Turquie. Memes palettes, memes graines fixes : deux executions du
    # generateur produisent des fichiers identiques, donc regenerer ne
    # bouscule pas les visuels deja valides.
    ("hero-tr",         "couchant",     "sea",  121, "Residences Amarimmo en Turquie"),
    ("tr-istanbul",     "nuit",         "sea",  131, "Immeuble residentiel a Istanbul"),
    ("tr-antalya",      "mediterranee", "sea",  141, "Residence sur la cote a Antalya"),
    ("tr-izmir",        "olive",        "land", 151, "Residence a Izmir"),
    ("tr-bodrum",       "sable",        "sea",  161, "Villas a Bodrum"),
    # Chine. Meme regle : graines fixes, donc regenerer ne bouscule rien.
    # La palette "nuit" pour le hero distingue la page au premier coup d'oeil
    # des trois autres marches, qui ouvrent tous sur un ciel clair.
    ("hero-cn",         "nuit",         "sea",  171, "Residences Amarimmo en Chine"),
    ("cn-shanghai",     "couchant",     "sea",  181, "Immeuble residentiel a Shanghai"),
    ("cn-pekin",        "sable",        "land", 191, "Residence a Pekin"),
    ("cn-shenzhen",     "mediterranee", "sea",  211, "Residence a Shenzhen"),
    ("cn-chengdu",      "olive",        "land", 221, "Residence a Chengdu"),
]

if __name__ == "__main__":
    for a in SCENES:
        p = scene(*a)
        print("  ", os.path.basename(p), f"{os.path.getsize(p)//1024} KB")
    print(f"{len(SCENES)} visuals -> {OUT}")
