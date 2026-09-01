# -*- coding: utf-8 -*-
"""
Amarimmo — builds index.html (Algérie), espagne.html, turquie.html and chine.html.

Four pages that share a header, a footer and a stylesheet, so the shell is written once here
rather than copy-pasted into each file and left to drift apart.

Content rules I held to, same as every other build for this client:
  - nothing invented about the COMPANY. No years in business, no unit counts delivered, no
    "leader du marché", no team, no awards, no address, no phone, no licence number.
  - the PROJECT cards are explicitly labelled as examples and the page carries a demo banner.
  - what IS stated as fact is the buying process and the taxes, which are public and
    checkable, each with the caveat that rates move and are region-dependent.
  - Spain's Golden Visa ended on 3 April 2025. Half the sites selling Spanish property to
    North African buyers still advertise it. Saying so is worth more than a slogan.
"""
import os, html
from turquie_contenu import VILLES, ETAPES, BAREME, FAQ as TR_FAQ
from chine_contenu import (VILLES as CN_VILLES, ETAPES as CN_ETAPES,
                           BAREME as CN_BAREME, FAQ as CN_FAQ)

HERE = os.path.dirname(os.path.abspath(__file__))

MARK = ('<svg class="mk" viewBox="0 0 32 32" fill="none" aria-hidden="true">'
        '<path d="M3 29V13.6L16 3l13 10.6V29" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/>'
        '<path d="M12 29v-9.2h8V29" fill="#A9814B"/>'
        '<path d="M16 3 29 13.6" stroke="#A9814B" stroke-width="2.1" stroke-linecap="round"/>'
        '</svg>')

ARROW = '<svg class="ar" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def icon(d):
    return (f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


ICONS = {
    "pin":   '<path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
    "doc":   '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    "hard":  '<path d="M4 17h16"/><path d="M6 17V12a6 6 0 0 1 12 0v5"/><path d="M10 6.6V4.4A1.4 1.4 0 0 1 11.4 3h1.2A1.4 1.4 0 0 1 14 4.4v2.2"/>',
    "key":   '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15.5 12v2"/>',
    "shield":'<path d="M12 3 20 6v6c0 4.6-3.3 7.9-8 9-4.7-1.1-8-4.4-8-9V6Z"/><path d="m9 12 2 2 4-4"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "sun":   '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "scale": '<path d="M12 3v18M7 21h10"/><path d="m5 8 3-4 3 4M13 8l3-4 3 4"/><path d="M2 8h8a4 4 0 0 1-8 0ZM14 8h8a4 4 0 0 1-8 0Z"/>',
    "plan":  '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 10h7V3M14 21v-7h7"/>',
    "hand":  '<path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V12"/><path d="M11 11.5V4.5a1.5 1.5 0 0 1 3 0V12"/><path d="M14 11V6.5a1.5 1.5 0 0 1 3 0V14"/><path d="M17 12.5a1.5 1.5 0 0 1 3 0V16a6 6 0 0 1-6 6h-2a6 6 0 0 1-6-6v-3l-1.6-2.1a1.5 1.5 0 0 1 2.4-1.8L8 13"/>',
}


def nav(page):
    items = [("#residences", "Nos résidences"), ("#processus", "Le processus"),
             ("#garanties", "Garanties"), ("#faq", "Questions"), ("#contact", "Contact")]
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in items)
    dz = ' aria-current="page"' if page == "dz" else ""
    es = ' aria-current="page"' if page == "es" else ""
    tr = ' aria-current="page"' if page == "tr" else ""
    cn = ' aria-current="page"' if page == "cn" else ""
    accueil = {"dz": "index.html", "es": "espagne.html",
               "tr": "turquie.html", "cn": "chine.html"}[page]
    return f'''<header class="hdr">
  <div class="wrap">
    <a class="brand" href="{accueil}">
      {MARK}<span class="nm">Amar<em>immo</em></span>
    </a>
    <nav class="nav" id="nav">{links}</nav>
    <div class="mkt">
      <a href="index.html"{dz}>Algérie</a>
      <a href="espagne.html"{es}>Espagne</a>
      <a href="turquie.html"{tr}>Turquie</a>
      <a href="chine.html"{cn}>Chine</a>
    </div>
    <button class="burger" aria-label="Menu" aria-expanded="false" id="burger"><span></span><span></span><span></span></button>
  </div>
</header>'''


DEMO = '''<div class="demo" id="demo">
  <span><b>Maquette de démonstration.</b> Les visuels sont des illustrations, pas des rendus de projets réels, et les fiches de résidences sont des exemples. Coordonnées et projets à remplacer.</span>
  <button onclick="document.getElementById('demo').remove()">Masquer</button>
</div>'''


FOOT = '''<footer class="ft-main">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="brand">''' + MARK + '''<span class="nm" style="color:#fff">Amar<em style="color:#A9814B;font-style:normal">immo</em></span></div>
        <p class="bl">Promotion et commercialisation de résidences en Algérie et en Espagne, accompagnement à l'acquisition en Turquie et en Chine.</p>
        <ul style="margin-top:20px">
          <li class="muted" style="color:#8C8377">Coordonnées à compléter</li>
          <li><a href="#contact">Formulaire de contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Algérie</h4>
        <ul>
          <li><a href="index.html#residences">Nos résidences</a></li>
          <li><a href="index.html#processus">Acheter sur plan</a></li>
          <li><a href="index.html#garanties">Garanties</a></li>
          <li><a href="index.html#faq">Questions fréquentes</a></li>
        </ul>
      </div>
      <div>
        <h4>Espagne</h4>
        <ul>
          <li><a href="espagne.html#residences">Nos programmes</a></li>
          <li><a href="espagne.html#processus">Acheter en Espagne</a></li>
          <li><a href="espagne.html#couts">Frais et fiscalité</a></li>
          <li><a href="espagne.html#faq">Questions fréquentes</a></li>
        </ul>
      </div>
      <div>
        <h4>Turquie</h4>
        <ul>
          <li><a href="turquie.html#villes">Les douze marchés</a></li>
          <li><a href="turquie.html#processus">Acheter en Turquie</a></li>
          <li><a href="turquie.html#couts">Frais, taxes et seuils</a></li>
          <li><a href="turquie.html#faq">Questions fréquentes</a></li>
        </ul>
      </div>
      <div>
        <h4>Chine</h4>
        <ul>
          <li><a href="chine.html#villes">Les douze marchés</a></li>
          <li><a href="chine.html#processus">Acheter en Chine</a></li>
          <li><a href="chine.html#sol">Le droit d'usage du sol</a></li>
          <li><a href="chine.html#faq">Questions fréquentes</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="ft-bot">
      <span>© 2026 Amarimmo. Tous droits réservés.</span>
      <span>Mentions légales · Politique de confidentialité — à rédiger</span>
    </div>
  </div>
</footer>
<script>
(function(){
  var b=document.getElementById('burger'), n=document.getElementById('nav');
  if(b&&n) b.addEventListener('click',function(){
    var open=n.classList.toggle('open');
    b.setAttribute('aria-expanded', open?'true':'false');
  });
  // the form is a front-end demo: there is no endpoint yet, so intercept rather than
  // let a submit reload the page and look broken
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var n=f.querySelector('[data-note]');
      if(n) n.textContent="Formulaire de démonstration — non connecté. Indiquez l'adresse de réception et je le branche.";
    });
  });
})();
</script>'''


import re

def typo_fr(h):
    """Espace insecable avant la ponctuation double, comme le veut le francais.

    Sans elle, le navigateur peut renvoyer le signe seul en debut de ligne :
    une capture de la page Chine montrait un « ; » orphelin ouvrant une ligne,
    ce qui se lit comme une faute de frappe. Vu sur une image, pas dans le code.

    Deux precautions, parce qu'une substitution globale sur du HTML est
    exactement le genre de chose qui casse en silence :
      - on ne touche QUE le texte, jamais l'interieur d'une balise. D'ou le
        decoupage sur (<[^>]*>) : les index pairs sont hors balise.
      - on saute le contenu de <script> et <style>, ou un « ; » colle a un
        insecable serait du code invalide.
    """
    morceaux = re.split(r'(<[^>]*>)', h)
    dans_code = False
    for i, m in enumerate(morceaux):
        if i % 2:                                  # une balise
            b = m.lower()
            if b.startswith(('<script', '<style')):
                dans_code = True
            elif b.startswith(('</script', '</style')):
                dans_code = False
            continue
        if dans_code or not m:
            continue
        m = re.sub(r' ([;!?»])', ' \\1', m)   # fine insecable
        m = re.sub(r' (:)', ' \\1', m)        # insecable pleine
        m = m.replace('« ', '« ')
        morceaux[i] = m
    return "".join(morceaux)


def page(title, desc, body, which):
    return typo_fr(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/site.css?v=3">
</head>
<body>
{DEMO}
{nav(which)}
{body}
{FOOT}
</body>
</html>''')


def project(img, tag, name, loc, chips, status, demo_tag=True):
    lis = "".join(f"<li>{c}</li>" for c in chips)
    t = (f'<span class="tag demo-tag">{tag}</span>' if demo_tag else f'<span class="tag">{tag}</span>')
    return f'''<article class="pc">
  <div class="im"><img src="assets/{img}.svg" alt="Illustration — {html.escape(name)}" loading="lazy">{t}</div>
  <div class="bd">
    <span class="loc">{loc}</span>
    <h3>{name}</h3>
    <ul>{lis}</ul>
    <div class="ft"><span>{status}</span><a href="#contact">Demander la fiche {ARROW}</a></div>
  </div>
</article>'''


def steps(items):
    li = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items)
    return f'<ol class="steps">{li}</ol>'


def features(items):
    return "".join(f'<div class="fc">{icon(ICONS[i])}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)


def faq(items):
    d = "".join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items)
    return f'<div class="faq">{d}</div>'


def contact(country, opts):
    o = "".join(f'<option>{x}</option>' for x in opts)
    return f'''<section id="contact">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Contact</div>
        <h2>Parlons de votre projet</h2>
        <p class="lede" style="margin-top:18px">Dites-nous ce que vous cherchez — la ville, le nombre de pièces, l'échéance. Nous revenons vers vous avec les fiches correspondantes et le détail des modalités.</p>
        <div class="grid g2" style="margin-top:34px">
          <div><h4 style="font-family:var(--sans);font-size:.79rem;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px">Marché</h4><p>{country}</p></div>
          <div><h4 style="font-family:var(--sans);font-size:.79rem;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px">Langues</h4><p>Français, arabe, anglais</p></div>
        </div>
      </div>
      <form class="form" data-demo>
        <div><label for="n">Nom</label><input id="n" name="nom" required></div>
        <div><label for="p">Téléphone</label><input id="p" name="tel" type="tel" required></div>
        <div class="full"><label for="e">E-mail</label><input id="e" name="email" type="email" required></div>
        <div><label for="v">Ville / secteur</label><select id="v" name="ville">{o}</select></div>
        <div><label for="t">Type de bien</label><select id="t" name="type"><option>F2</option><option>F3</option><option>F4</option><option>F5 et +</option><option>Duplex / penthouse</option><option>Villa</option><option>Local commercial</option></select></div>
        <div class="full"><label for="m">Votre projet</label><textarea id="m" name="message" placeholder="Budget approximatif, échéance, financement envisagé…"></textarea></div>
        <label class="consent full"><input type="checkbox" required> J'accepte d'être recontacté au sujet de ma demande.</label>
        <div class="full"><button class="btn btn-p" type="submit">Envoyer ma demande {ARROW}</button></div>
        <p class="formnote full" data-note></p>
      </form>
    </div>
  </div>
</section>'''


# ============================================================== ALGÉRIE =========
dz_projects = "".join([
    project("dz-oran-front", "Exemple de fiche", "Résidence Ryad", "Oran — Front de mer",
            ["F3 · F4 · F5", "Parking sous-sol", "Ascenseurs", "Vue mer"], "Vente sur plan"),
    project("dz-alger-hydra", "Exemple de fiche", "Résidence El Wiam", "Alger — Hydra",
            ["F2 · F3 · F4", "Espaces verts", "Gardiennage", "Local commercial"], "Vente sur plan"),
    project("dz-oran-parc", "Exemple de fiche", "Résidence Nour", "Oran — Bir El Djir",
            ["F3 · F4", "Aire de jeux", "Parking extérieur"], "Livraison à venir"),
    project("dz-alger-tour", "Exemple de fiche", "Tour Meridien", "Alger — Bab Ezzouar",
            ["F2 · F3", "Duplex derniers niveaux", "Vue panoramique"], "En construction"),
])

dz_body = f'''
<div class="hero">
  <img src="assets/hero-dz.svg" alt="Illustration de résidences modernes en Algérie">
  <div class="wrap">
    <div class="eyebrow">Promotion immobilière — Algérie</div>
    <h1>Des résidences modernes à Oran et à Alger.</h1>
    <p class="sub">Des programmes pensés pour la façon dont on vit réellement en Algérie aujourd'hui : des surfaces utiles, des finitions qui tiennent, du stationnement, et des documents en règle du premier jour au livret foncier.</p>
    <div class="cta">
      <a class="btn btn-p" href="#residences">Voir les résidences {ARROW}</a>
      <a class="btn btn-g" href="#contact">Être rappelé</a>
    </div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div><div class="k">Implantation</div><div class="v">Oran et Alger</div></div>
    <div><div class="k">Type de vente</div><div class="v">Vente sur plan (VSP)</div></div>
    <div><div class="k">Cadre</div><div class="v">Acte notarié, livret foncier</div></div>
    <div><div class="k">Accompagnement</div><div class="v">De la réservation aux clés</div></div>
  </div>
</div>

<section id="residences">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Nos résidences</div>
      <h2>Des programmes à taille humaine, dans des quartiers qui tiennent leur valeur.</h2>
      <p class="lede" style="margin-top:18px">L'emplacement décide de tout le reste. Nous ne lançons un programme que là où les accès, les écoles, les commerces et le réseau existent déjà — pas là où ils sont annoncés.</p>
    </div>
    <div class="grid g4">{dz_projects}</div>
    <p class="note">Les quatre fiches ci-dessus sont des exemples de mise en page. Vos programmes réels, avec leurs rendus, leurs plans et leurs surfaces, viendront s'y substituer.</p>
  </div>
</section>

<section class="sand" id="processus">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Le processus</div>
      <h2>Acheter sur plan, étape par étape.</h2>
      <p class="lede" style="margin-top:18px">La vente sur plan est encadrée par la loi. Voici ce qui se passe réellement, dans l'ordre, et ce que vous signez à chaque étape.</p>
    </div>
    {steps([
      ("Sélection et visite du site",
       "Vous choisissez le programme et le lot. Nous vous montrons le terrain, le plan de masse et le plan de votre appartement, avec les surfaces habitables et les annexes détaillées séparément."),
      ("Réservation",
       "Un contrat de réservation fixe le lot, la surface, le prix et l'échéancier. Il précise ce qui est compris dans le prix et ce qui ne l'est pas — c'est le document qu'il faut lire ligne par ligne, pas survoler."),
      ("Contrat de vente sur plan chez le notaire",
       "La VSP est établie par acte notarié. Le contrat fixe le délai de livraison, les pénalités de retard, le descriptif des travaux et les garanties. Sans notaire, il n'y a pas de vente sur plan — il y a une promesse."),
      ("Paiements échelonnés selon l'avancement",
       "Les versements suivent l'avancement du chantier selon l'échéancier du contrat. Vous savez à quoi correspond chaque appel de fonds, et vous pouvez le vérifier sur place."),
      ("Suivi de chantier",
       "Points d'avancement réguliers et accès au chantier aux étapes clés. Les modifications que vous demandez sont chiffrées et écrites avant d'être exécutées, jamais l'inverse."),
      ("Livraison, réception et livret foncier",
       "Réception contradictoire avec relevé des réserves, remise des clés, puis établissement de l'acte définitif et du livret foncier à votre nom."),
    ])}
  </div>
</section>

<section id="garanties">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Ce sur quoi vous pouvez nous juger</div>
      <h2>Un promoteur se juge sur ses documents, pas sur ses images.</h2>
    </div>
    <div class="grid g3">
      {features([
        ("doc", "Des documents complets",
         "Permis de construire, plan de masse, descriptif des travaux, échéancier, délai de livraison et pénalités : tout est communiqué avant la réservation, pas après."),
        ("plan", "Des surfaces annoncées telles quelles",
         "Surface habitable et surfaces annexes présentées séparément. Un balcon, une loggia et une cave ne se comptent pas comme un salon."),
        ("hard", "Un descriptif technique écrit",
         "Marques et références des matériaux, menuiseries, sanitaires et équipements figurent au contrat. Un descriptif qui reste vague est un descriptif qui va changer."),
        ("shield", "Des délais assortis de pénalités",
         "Un délai de livraison sans pénalité de retard n'est pas un engagement. Le nôtre est chiffré au contrat."),
        ("key", "Une réception contradictoire",
         "Vous réceptionnez avec nous, réserve par réserve, et les réserves sont levées avant le solde — pas promises pour plus tard."),
        ("scale", "Le titre au bout du chemin",
         "L'objectif n'est pas la remise des clés, c'est le livret foncier à votre nom. Nous vous accompagnons jusque-là."),
      ])}
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Vous achetez depuis l'étranger</div>
        <h2>Acheter en Algérie depuis la France, l'Espagne ou le Canada.</h2>
        <p class="lede" style="margin-top:18px">Une part importante des acquéreurs vit à l'étranger et ne peut pas passer six mois à faire des allers-retours. Le dossier peut avancer à distance, à condition que la procuration et les traductions soient faites correctement dès le départ.</p>
      </div>
      <div class="grid" style="gap:16px">
        <div class="box"><h3>Procuration</h3><p>Établie au consulat ou chez un notaire local puis légalisée, elle permet de signer sans être sur place. C'est l'étape que l'on prépare en premier, parce que c'est celle qui prend le plus de temps.</p></div>
        <div class="box"><h3>Transferts et devises</h3><p>Le mode de règlement se cale sur votre situation et sur la réglementation des changes en vigueur. Nous vous disons ce qui est possible avant que vous engagiez quoi que ce soit.</p></div>
        <div class="box"><h3>Suivi à distance</h3><p>Photos et points d'avancement à chaque étape clé, et un interlocuteur unique joignable sur votre fuseau horaire.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sand" id="faq">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Questions fréquentes</div><h2>Ce que les acheteurs demandent en premier.</h2></div>
    {faq([
      ("Qu'est-ce que la vente sur plan (VSP) exactement ?",
       "<p>C'est l'achat d'un logement qui n'est pas encore construit, ou pas encore terminé. En Algérie, la VSP est encadrée : elle passe obligatoirement par un acte notarié, et le contrat doit préciser le descriptif des travaux, le prix, l'échéancier des paiements, le délai de livraison et les pénalités en cas de retard.</p><p>Un accord signé sous seing privé, sans notaire, n'est pas une vente sur plan.</p>"),
      ("Quels documents dois-je exiger avant de réserver ?",
       "<p>Le permis de construire, l'acte de propriété du terrain, le plan de masse, le plan de votre lot avec les surfaces, le descriptif technique des travaux, l'échéancier de paiement et le délai de livraison avec les pénalités associées.</p><p>Si l'un de ces documents ne vous est pas montré avant la réservation, il y a une raison, et elle n'est jamais en votre faveur.</p>"),
      ("Je paie combien, et quand ?",
       "<p>Par tranches, suivant l'avancement du chantier, selon l'échéancier inscrit au contrat notarié. Chaque appel de fonds correspond à une étape que vous pouvez aller vérifier sur place.</p>"),
      ("Que se passe-t-il en cas de retard de livraison ?",
       "<p>Le contrat prévoit des pénalités de retard. C'est précisément pour cela qu'il faut vérifier qu'elles y figurent, et à quel montant, avant de signer — et pas seulement que le délai soit écrit quelque part.</p>"),
      ("Quand est-ce que je deviens réellement propriétaire ?",
       "<p>À l'établissement de l'acte de vente définitif, puis à l'inscription et à la délivrance du livret foncier à votre nom. La remise des clés et le titre de propriété sont deux choses différentes, et la seconde est la seule qui compte juridiquement.</p>"),
      ("Puis-je acheter si je réside à l'étranger ?",
       "<p>Oui. La signature peut se faire par procuration établie au consulat ou devant notaire puis légalisée. Le point à anticiper est le mode de paiement, qui dépend de votre situation et de la réglementation des changes applicable.</p>"),
      ("La surface annoncée, c'est quoi au juste ?",
       "<p>Nous présentons la surface habitable et les surfaces annexes séparément — balcon, loggia, cave, parking. Une annonce qui donne un seul chiffre global gonfle mécaniquement la surface perçue de 10 à 20 %.</p>"),
    ])}
  </div>
</section>

{contact("Algérie — Oran et Alger", ["Oran — centre", "Oran — Bir El Djir", "Oran — Front de mer",
                                     "Alger — Hydra", "Alger — Chéraga", "Alger — Bab Ezzouar",
                                     "Alger — autre", "Autre wilaya"])}
'''

# =============================================================== ESPAGNE ========
es_projects = "".join([
    project("es-costa", "Exemple de fiche", "Marina Estepona", "Costa del Sol — Estepona",
            ["2 · 3 chambres", "Piscine commune", "Parking", "Proche mer"], "En commercialisation"),
    project("es-alicante", "Exemple de fiche", "Residencial Altamar", "Costa Blanca — Alicante",
            ["2 · 3 chambres", "Terrasses", "Solarium"], "Sur plan"),
    project("es-andalousie", "Exemple de fiche", "Villas Mirador", "Andalousie — Málaga",
            ["Villas 3 · 4 chambres", "Jardin privatif", "Piscine"], "Livraison à venir"),
    project("es-barcelona", "Exemple de fiche", "Eixample 118", "Barcelone — Eixample",
            ["2 chambres", "Immeuble réhabilité", "Ascenseur"], "En commercialisation"),
])

es_body = f'''
<div class="hero">
  <img src="assets/hero-es.svg" alt="Illustration de résidences modernes en Espagne">
  <div class="wrap">
    <div class="eyebrow">Promotion et acquisition — Espagne</div>
    <h1>Acheter en Espagne, sans mauvaise surprise.</h1>
    <p class="sub">La Méditerranée espagnole reste l'un des marchés les plus accessibles d'Europe pour un acheteur étranger. Encore faut-il connaître les frais réels, les délais réels et ce qui a changé récemment dans la loi.</p>
    <div class="cta">
      <a class="btn btn-p" href="#residences">Voir les programmes {ARROW}</a>
      <a class="btn btn-g" href="#couts">Frais et fiscalité</a>
    </div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div><div class="k">Régions</div><div class="v">Costa del Sol, Costa Blanca, Barcelone</div></div>
    <div><div class="k">Formalité d'entrée</div><div class="v">NIE obligatoire</div></div>
    <div><div class="k">Acte</div><div class="v">Escritura devant notaire</div></div>
    <div><div class="k">Enregistrement</div><div class="v">Registro de la Propiedad</div></div>
  </div>
</div>

<section id="residences">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Nos programmes</div>
      <h2>Du neuf sur la côte, de l'ancien réhabilité en ville.</h2>
      <p class="lede" style="margin-top:18px">Deux logiques différentes : le neuf côtier pour l'usage et la location saisonnière, l'ancien urbain pour le rendement à l'année. Nous ne présentons pas le second comme le premier.</p>
    </div>
    <div class="grid g4">{es_projects}</div>
    <p class="note">Fiches d'exemple. Vos programmes réels, avec photos, plans et prix, viendront les remplacer.</p>
  </div>
</section>

<section class="sand" id="processus">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Le processus</div>
      <h2>Acheter en Espagne quand on n'y réside pas.</h2>
      <p class="lede" style="margin-top:18px">La procédure est balisée et rapide dès lors que le NIE est obtenu. C'est presque toujours lui qui décide du calendrier.</p>
    </div>
    {steps([
      ("Obtenir le NIE",
       "Le Número de Identidad de Extranjero est indispensable pour acheter, ouvrir un compte et payer les impôts. Il s'obtient au consulat d'Espagne ou en Espagne, et le délai de rendez-vous est le vrai goulot d'étranglement — on le lance en premier."),
      ("Ouvrir un compte bancaire espagnol",
       "Nécessaire en pratique pour régler le prix, les frais et ensuite les charges et les taxes locales."),
      ("Réservation et contrat d'arrhes",
       "Une réserva retire le bien du marché. Vient ensuite le contrato de arras, généralement avec 10 % du prix. Attention au type d'arras : selon la formule, se rétracter coûte le dépôt, le double, ou ouvre à des poursuites. Ce n'est pas un détail de rédaction."),
      ("Vérifications juridiques avant signature",
       "Nota simple du Registro de la Propiedad (propriétaire réel, hypothèques, servitudes), certificat d'urbanisme, charges de copropriété impayées, certificat énergétique, licence de première occupation pour le neuf."),
      ("Signature de l'escritura chez le notaire",
       "L'acte est signé devant notaire, le solde est versé, les clés sont remises. Vous pouvez signer par procuration si vous ne pouvez pas être présent."),
      ("Inscription au Registro de la Propiedad",
       "Le notaire notifie le registre, puis l'inscription définitive est effectuée. C'est elle qui rend votre propriété opposable aux tiers — et elle intervient après la signature, pas le jour même."),
    ])}
  </div>
</section>

<section id="couts">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Frais et fiscalité</div>
      <h2>Ce que coûte réellement une acquisition, au-delà du prix affiché.</h2>
      <p class="lede" style="margin-top:18px">Les frais d'acquisition en Espagne représentent en pratique environ 10 à 14 % du prix. Un budget calculé sur le seul prix de vente est faux d'entrée.</p>
    </div>
    <div class="split" style="align-items:start">
      <div class="tbl-wrap"><table class="tbl">
        <tr><th>Poste</th><th>Ordre de grandeur</th><th>Sur quoi</th></tr>
        <tr><td>IVA (TVA)</td><td>10 %</td><td>Logement neuf, achat au promoteur</td></tr>
        <tr><td>AJD (droit d'acte)</td><td>≈ 0,5 – 1,5 %</td><td>Neuf, taux fixé par la communauté autonome</td></tr>
        <tr><td>ITP (droit de mutation)</td><td>≈ 6 – 10 %</td><td>Ancien, taux fixé par la communauté autonome</td></tr>
        <tr><td>Notaire</td><td>≈ 0,3 – 0,6 %</td><td>Tarif réglementé, dégressif</td></tr>
        <tr><td>Registre de la propriété</td><td>≈ 0,2 – 0,4 %</td><td>Inscription de l'acte</td></tr>
        <tr><td>Avocat</td><td>≈ 1 %</td><td>Facultatif, fortement recommandé pour un non-résident</td></tr>
        <tr><td>Gestoría / frais de dossier</td><td>Variable</td><td>Démarches administratives</td></tr>
      </table></div>
      <div>
        <div class="fc" style="margin-bottom:18px">
          {icon(ICONS["scale"])}
          <h3>Neuf ou ancien : ce n'est pas la même fiscalité</h3>
          <p>Le neuf acheté au promoteur supporte l'IVA plus l'AJD. L'ancien supporte l'ITP, dont le taux dépend de la communauté autonome et parfois du profil de l'acheteur. Comparer deux biens sans intégrer cela fausse l'écart de plusieurs milliers d'euros.</p>
        </div>
        <div class="fc">
          {icon(ICONS["shield"])}
          <h3>Le Golden Visa espagnol n'existe plus</h3>
          <p>Le visa de résidence par investissement immobilier a été supprimé et a cessé de s'appliquer le 3 avril 2025. Beaucoup de sites continuent de le mettre en avant pour attirer les acheteurs étrangers. Un achat immobilier en Espagne aujourd'hui ne donne aucun droit de séjour : il faut passer par une autre voie de résidence, ou par le régime de séjour de courte durée.</p>
        </div>
      </div>
    </div>
    <p class="note">Ordres de grandeur donnés à titre indicatif. Les taux d'ITP et d'AJD sont fixés par chaque communauté autonome et évoluent — le chiffrage exact de votre opération est établi avant toute signature, région par région.</p>
  </div>
</section>

<section class="dark" id="garanties">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Notre méthode</div><h2>Les vérifications qui évitent les litiges.</h2></div>
    <div class="grid g3">
      <div class="box"><h3>Nota simple systématique</h3><p>Extrait du registre foncier obtenu avant toute réserve : propriétaire réel, hypothèques inscrites, servitudes, saisies. Cinq euros et vingt minutes qui évitent la plupart des mauvaises histoires.</p></div>
      <div class="box"><h3>Charges de copropriété</h3><p>En Espagne, les impayés de la communauté de propriétaires suivent en partie le bien, pas le vendeur. On les vérifie avant la signature, pas après.</p></div>
      <div class="box"><h3>Licence de première occupation</h3><p>Pour le neuf, sans licencia de primera ocupación, pas de raccordement définitif ni de location légale. On ne signe pas sans.</p></div>
      <div class="box"><h3>Type d'arras négocié</h3><p>Arras penitenciales, confirmatorias ou penales : la formule retenue décide de ce qui se passe si l'une des parties se retire. Elle se négocie, elle ne se subit pas.</p></div>
      <div class="box"><h3>Fiscalité du non-résident</h3><p>Après l'achat viennent l'IBI, la taxe des ordures, et l'impôt du non-résident, y compris sans mise en location. Le budget annuel vous est donné avant l'acquisition.</p></div>
      <div class="box"><h3>Location saisonnière</h3><p>Les licences touristiques sont limitées et parfois gelées selon la commune. Si l'objectif est locatif, on vérifie la faisabilité avant l'achat, pas après.</p></div>
    </div>
  </div>
</section>

<section class="sand" id="faq">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Questions fréquentes</div><h2>Espagne — les questions qui reviennent.</h2></div>
    {faq([
      ("Un étranger non résident peut-il acheter en Espagne ?",
       "<p>Oui, sans restriction de nationalité pour l'immobilier résidentiel. Il faut un NIE et, en pratique, un compte bancaire espagnol.</p>"),
      ("Combien de temps prend une acquisition ?",
       "<p>Une fois le NIE en main, comptez généralement de six à dix semaines entre la réservation et la signature de l'escritura pour un bien existant. L'obtention du NIE est ce qui varie le plus, selon les délais de rendez-vous consulaires.</p>"),
      ("L'achat d'un bien donne-t-il droit à un titre de séjour ?",
       "<p>Non. Le Golden Visa par investissement immobilier a été supprimé et ne s'applique plus depuis le 3 avril 2025. Toute page qui l'annonce encore n'est pas à jour.</p>"),
      ("Puis-je obtenir un crédit immobilier espagnol en tant que non-résident ?",
       "<p>C'est possible, mais l'apport demandé est plus élevé que pour un résident : les banques espagnoles financent couramment jusqu'à 60 à 70 % de la valeur pour un non-résident. Le reste, plus les frais d'acquisition, doit être disponible.</p>"),
      ("Ai-je besoin d'un avocat ?",
       "<p>Ce n'est pas obligatoire, et c'est fortement conseillé pour un non-résident. Le notaire espagnol authentifie l'acte, il ne défend pas vos intérêts ni ne mène les vérifications à votre place. Comptez environ 1 % du prix.</p>"),
      ("Que dois-je payer chaque année une fois propriétaire ?",
       "<p>L'IBI (taxe foncière locale), la taxe d'enlèvement des ordures, les charges de copropriété, et l'impôt sur le revenu des non-résidents — qui est dû même si le bien n'est pas loué, sur une base forfaitaire.</p>"),
      ("Puis-je le mettre en location saisonnière ?",
       "<p>Cela dépend entièrement de la commune et de la communauté autonome. Plusieurs zones très demandées ont gelé la délivrance de nouvelles licences touristiques. La question se tranche avant l'achat.</p>"),
    ])}
  </div>
</section>

{contact("Espagne — Costa del Sol, Costa Blanca, Barcelone",
         ["Costa del Sol — Marbella / Estepona", "Costa del Sol — Málaga", "Costa Blanca — Alicante",
          "Costa Blanca — Torrevieja", "Barcelone", "Madrid", "Autre région"])}
'''


# =============================================================== TURQUIE ========
# Le contenu factuel est dans turquie_contenu.py, avec l'explication de ce qui
# y est laisse vide et pourquoi. Ce fichier-ci ne fait que le mettre en page.

tr_projects = "".join([
    project("tr-istanbul", "Exemple de fiche", "Résidence Bosphore", "Istanbul — rive européenne",
            ["2+1 · 3+1", "Ascenseurs", "Parking", "Vue détroit"], "En commercialisation"),
    project("tr-antalya", "Exemple de fiche", "Résidence Lara", "Antalya — Lara",
            ["1+1 · 2+1", "Piscine commune", "Proche mer"], "Sur plan"),
    project("tr-bodrum", "Exemple de fiche", "Villas Yalıkavak", "Bodrum — Yalikavak",
            ["Villas 3+1 · 4+1", "Jardin privatif", "Piscine"], "Livraison à venir"),
    project("tr-izmir", "Exemple de fiche", "Résidence Alsancak", "Izmir — Alsancak",
            ["2+1 · 3+1", "Immeuble urbain", "Commerces au pied"], "En commercialisation"),
])

tr_villes = "".join(
    f'<div class="box"><h3>{html.escape(n)}</h3>'
    f'<p class="muted" style="font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px">{html.escape(r)}</p>'
    f'<p>{html.escape(d)}</p></div>'
    for n, r, d in VILLES)

tr_bareme = "".join(
    f'<tr><td>{html.escape(l)}</td>'
    # LA VALEUR EST VIDE, ET ELLE SE VOIT. Voir l'entete de turquie_contenu.py :
    # un seuil perime sur un site qui vend a des investisseurs etrangers est
    # un chiffre sur lequel quelqu'un engage des centaines de milliers de
    # dollars. Une case vide se remarque, un chiffre faux non.
    f'<td><span class="tbd">à vérifier</span></td>'
    f'<td>{html.escape(q)}<br><span class="muted">Source : {html.escape(src)}</span></td></tr>'
    for l, q, src in BAREME)

tr_body = f'''
<div class="hero">
  <img src="assets/hero-tr.svg" alt="Illustration de résidences modernes en Turquie">
  <div class="wrap">
    <div class="eyebrow">Acquisition et investissement — Turquie</div>
    <h1>Acheter en Turquie, en sachant ce qui se vérifie avant de réserver.</h1>
    <p class="sub">Le marché turc est l'un des plus ouverts de la région aux acheteurs étrangers. Il a aussi ses règles propres : des zones où un étranger ne peut pas acheter, un rapport d'expertise obligatoire, une assurance séisme sans laquelle rien n'avance, et des seuils d'investissement qui ont changé récemment.</p>
    <div class="cta">
      <a class="btn btn-p" href="#villes">Les douze marchés {ARROW}</a>
      <a class="btn btn-g" href="#processus">Le processus d'achat</a>
    </div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div><div class="k">Titre de propriété</div><div class="v">Tapu</div></div>
    <div><div class="k">Transfert</div><div class="v">Direction du cadastre</div></div>
    <div><div class="k">Vente à un étranger</div><div class="v">Rapport d'expertise obligatoire</div></div>
    <div><div class="k">Assurance</div><div class="v">Séisme obligatoire (DASK)</div></div>
  </div>
</div>

<section id="sejour">
  <div class="wrap">
    <div class="fc" style="border-left:4px solid var(--gold)">
      {icon(ICONS["scale"])}
      <h3>Acheter un bien ne donne pas automatiquement un visa, un titre de séjour ni la citoyenneté</h3>
      <p>Ce sont trois procédures juridiques distinctes, avec chacune ses conditions. Des seuils d'investissement existent pour le séjour et pour la citoyenneté ; ils ont été modifiés récemment, et certains quartiers sont fermés à l'enregistrement de nouveaux résidents étrangers.</p>
      <p>Cette page ne publie aucun de ces montants tant qu'il n'a pas été vérifié à une date précise auprès de l'autorité qui le fixe. C'est une règle que tu as toi-même écrite dans ton cahier des charges, section 4 — et c'est la bonne.</p>
    </div>
  </div>
</section>

<section id="villes">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Les marchés</div>
      <h2>Douze villes, et elles ne se ressemblent pas.</h2>
      <p class="lede" style="margin-top:18px">Ce sont les douze destinations de ton document, dans ton ordre. Elles ne relèvent pas de la même logique : une côte saisonnière ne se finance pas et ne se loue pas comme une métropole à l'année, et les présenter sur la même grille de rendement serait trompeur.</p>
    </div>
    <div class="grid g3">{tr_villes}</div>
    <p class="note">Bodrum, Fethiye et Alanya sont des districts côtiers, pas des villes-provinces. Je les garde parce que ce sont des marchés en soi — mais un investisseur qui cherche « la ville de Bodrum » dans un registre officiel ne la trouvera pas sous ce nom, et autant le savoir avant.</p>
  </div>
</section>

<section class="sand" id="residences">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Nos programmes</div>
      <h2>Du neuf côtier, de l'urbain à l'année.</h2>
      <p class="lede" style="margin-top:18px">Deux logiques, comme en Espagne : le côtier pour l'usage et la location saisonnière, l'urbain pour le rendement à l'année. Nous ne présentons pas le second comme le premier.</p>
    </div>
    <div class="grid g4">{tr_projects}</div>
    <p class="note">Fiches d'exemple. Tes programmes réels, avec photos, plans et prix, viendront les remplacer.</p>
  </div>
</section>

<section id="processus">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Le processus</div>
      <h2>Acheter en Turquie quand on n'y réside pas.</h2>
      <p class="lede" style="margin-top:18px">L'ordre compte. Deux étapes doivent être faites AVANT toute réservation : la vérification du titre au cadastre, et celle des zones interdites. Les deux se rattrapent mal, et la seconde pas du tout.</p>
    </div>
    {steps(ETAPES)}
  </div>
</section>

<section class="sand" id="couts">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Frais, taxes et seuils</div>
      <h2>Les montants ne sont pas écrits ici, et c'est volontaire.</h2>
      <p class="lede" style="margin-top:18px">Ce tableau nomme chaque poste et l'autorité qui en publie la valeur. Il ne donne pas les chiffres.</p>
    </div>
    <div class="split" style="align-items:start">
      <div class="tbl-wrap"><table class="tbl">
        <tr><th>Poste</th><th>Valeur</th><th>Ce que c'est, et qui la publie</th></tr>
        {tr_bareme}
      </table></div>
      <div>
        <div class="fc" style="margin-bottom:18px">
          {icon(ICONS["shield"])}
          <h3>Pourquoi une case vide plutôt qu'un chiffre</h3>
          <p>Un mécanisme est stable : le tapu s'appellera encore le tapu dans trois ans. Un seuil, non. Celui de la citoyenneté par investissement a changé en 2022, celui du permis de séjour ensuite.</p>
          <p>Un chiffre périmé sur un site immobilier ne se signale pas tout seul. Il reste affiché, il a l'air juste, et quelqu'un engage plusieurs centaines de milliers de dollars dessus. Une case vide, elle, se remarque immédiatement.</p>
        </div>
        <div class="fc">
          {icon(ICONS["doc"])}
          <h3>Comment on remplit ce tableau</h3>
          <p>Chaque ligne est vérifiée auprès de l'autorité nommée en face, et la page porte la date de vérification. Quand la date vieillit, elle se voit aussi.</p>
        </div>
      </div>
    </div>
    <p class="note">Vérifié le <span class="tbd">à renseigner</span> — tant que cette date est vide, aucun montant n'est publié sur cette page.</p>
  </div>
</section>

<section class="dark" id="garanties">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Notre méthode</div><h2>Les vérifications qui évitent les litiges.</h2></div>
    <div class="grid g3">
      <div class="box"><h3>Extrait du cadastre avant toute réserve</h3><p>Propriétaire réel, hypothèques inscrites, servitudes, saisies. C'est l'équivalent turc de la nota simple espagnole, et il évite les mêmes histoires.</p></div>
      <div class="box"><h3>Zone militaire vérifiée en amont</h3><p>Un étranger ne peut pas acheter en zone militaire ou de sécurité. Ce n'est pas négociable et ça ne se découvre pas après la réservation.</p></div>
      <div class="box"><h3>Rapport d'expertise lu, pas seulement fourni</h3><p>Il est obligatoire pour une vente à un étranger. Il rend visible un prix très au-dessus du marché — à condition de le lire.</p></div>
      <div class="box"><h3>Permis d'habiter pour le neuf</h3><p>Sans iskân, les raccordements définitifs et la revente se compliquent. On vérifie avant de signer.</p></div>
      <div class="box"><h3>Assurance séisme dès le départ</h3><p>Elle est obligatoire et elle conditionne la suite des démarches. Ce n'est pas une option commerciale.</p></div>
      <div class="box"><h3>Montage bancaire préparé à l'avance</h3><p>La réglementation des changes impose des formalités spécifiques quand des fonds étrangers entrent dans l'opération. C'est ce qui retarde le plus souvent une acquisition, devant le juridique.</p></div>
    </div>
  </div>
</section>

<section class="sand" id="faq">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Questions fréquentes</div><h2>Turquie — les questions qui reviennent.</h2></div>
    {faq(TR_FAQ)}
  </div>
</section>

{contact("Turquie — douze marchés", [n for n, _, _ in VILLES] + ["Autre ville"])}
'''


# ================================================================= CHINE ========
# Le contenu factuel est dans chine_contenu.py, avec l'explication de ce qui y
# est laisse vide et pourquoi cette page ne peut pas etre la page Turquie avec
# d'autres noms de villes. Ce fichier-ci ne fait que la mise en page.

cn_projects = "".join([
    project("cn-shanghai", "Exemple de fiche", "Résidence Huangpu", "Shanghai — rive ouest",
            ["2 et 3 chambres", "Immeuble récent", "Métro à pied"], "En commercialisation"),
    project("cn-pekin", "Exemple de fiche", "Résidence Chaoyang", "Pékin — Chaoyang",
            ["2 et 3 chambres", "Résidence fermée", "Écoles"], "Ancien rénové"),
    project("cn-shenzhen", "Exemple de fiche", "Résidence Nanshan", "Shenzhen — Nanshan",
            ["1 et 2 chambres", "Tour résidentielle", "Proche pôle tech"], "Sur plan"),
    project("cn-chengdu", "Exemple de fiche", "Résidence Jinjiang", "Chengdu — Jinjiang",
            ["2 et 3 chambres", "Parc au pied", "Marché à l'année"], "En commercialisation"),
])

cn_villes = "".join(
    f'<div class="box"><h3>{html.escape(n)}</h3>'
    f'<p class="muted" style="font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px">{html.escape(r)}</p>'
    f'<p>{html.escape(d)}</p></div>'
    for n, r, d in CN_VILLES)

# Deux natures de case vide, et elles ne disent pas la meme chose.
# « a verifier » : la valeur existe, l'autorite est nommee, personne ne l'a
#                  encore verifiee a une date precise.
# « non fixe »   : la valeur N'EXISTE PAS. Ecrire « a verifier » la-dessus
#                  ferait croire qu'il suffit de chercher — c'est le cas du
#                  cout de renouvellement du droit d'usage du sol, que les
#                  textes d'application n'ont jamais chiffre.
cn_bareme = "".join(
    f'<tr><td>{html.escape(l)}</td>'
    f'<td><span class="tbd{"" if k == "verif" else " tbd-x"}">'
    f'{"à vérifier" if k == "verif" else "non fixé"}</span></td>'
    f'<td>{html.escape(q)}<br><span class="muted">Source : {html.escape(src)}</span></td></tr>'
    for l, k, q, src in CN_BAREME)

cn_body = f'''
<div class="hero">
  <img src="assets/hero-cn.svg" alt="Illustration de résidences modernes en Chine">
  <div class="wrap">
    <div class="eyebrow">Acquisition — Chine continentale</div>
    <h1>Acheter en Chine, en sachant d'abord ce que l'on achète.</h1>
    <p class="sub">Ce marché ne se lit pas comme les trois autres. Personne n'y achète le sol — pas même un acheteur chinois : on acquiert le bâti et un droit d'usage du sol pour une durée déterminée. Et l'achat par un étranger repose sur un principe d'usage propre, sous conditions fixées ville par ville. Cette page dit ce qui est possible, pour qui, et à quelles conditions.</p>
    <div class="cta">
      <a class="btn btn-p" href="#sol">Ce que l'on achète réellement {ARROW}</a>
      <a class="btn btn-g" href="#villes">Les douze marchés</a>
    </div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div><div class="k">Ce qui s'acquiert</div><div class="v">Le bâti + un droit d'usage du sol</div></div>
    <div><div class="k">Titre</div><div class="v">Certificat de propriété immobilière</div></div>
    <div><div class="k">Achat par un étranger</div><div class="v">Usage propre, sous conditions</div></div>
    <div><div class="k">Séjour ou nationalité</div><div class="v">Aucun lien avec l'achat</div></div>
  </div>
</div>

<section id="sol">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">La différence de fond</div>
      <h2>Deux choses à comprendre avant de regarder un seul bien.</h2>
      <p class="lede" style="margin-top:18px">Elles ne sont pas des réserves de bas de page. Elles décident si l'opération est possible, et ce qu'elle vaut.</p>
    </div>
    <div class="grid g2">
      <div class="fc" style="border-left:4px solid var(--gold)">
        {icon(ICONS["plan"])}
        <h3>Le sol appartient à l'État — pour tout le monde</h3>
        <p>Le sol urbain chinois n'est la propriété de personne d'autre que l'État. Un acquéreur, chinois ou étranger, obtient la propriété du bâti et un droit d'usage du sol accordé pour une durée déterminée, la durée résidentielle étant la plus longue des trois catégories.</p>
        <p>Conséquence pratique, souvent ignorée : dans l'ancien, la durée qui <b>reste</b> compte autant que l'état du bien. Deux appartements identiques ne valent pas la même chose si l'un a vingt ans de droit d'usage de moins. Cette durée résiduelle figure au registre et se vérifie avant toute offre.</p>
        <p>À l'échéance, le renouvellement du résidentiel est automatique — le propriétaire ne perd pas son logement. Mais <b>son coût n'est pas fixé</b> : les textes d'application n'ont pas été publiés. Nous l'écrivons tel quel, parce qu'aucun chiffre honnête n'existe.</p>
      </div>
      <div class="fc" style="border-left:4px solid var(--gold)">
        {icon(ICONS["scale"])}
        <h3>Acheter n'ouvre aucun droit de séjour, ni la nationalité</h3>
        <p>Il n'existe pas en Chine de titre de séjour ni de nationalité par investissement immobilier, à aucun montant. La résidence permanente existe, mais ses critères n'ont rien à voir avec l'achat d'un logement.</p>
        <p>Nous l'écrivons explicitement parce que ce site présente plusieurs marchés côte à côte : ce qui vaut sur une autre page ne vaut pas ici, et un lecteur transpose sans y penser.</p>
        <p>L'achat lui-même est encadré par un principe d'usage propre : un logement pour l'habiter. S'y ajoutent une ancienneté de travail ou d'études en Chine et les conditions propres à chaque municipalité — elles diffèrent d'une ville à l'autre et elles ont déjà été durcies puis assouplies.</p>
      </div>
    </div>
  </div>
</section>

<section class="sand" id="villes">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Les marchés</div>
      <h2>Douze villes, et rien d'un marché unique.</h2>
      <p class="lede" style="margin-top:18px">Quatre métropoles de premier rang, sept grandes métropoles régionales et un marché littoral. Ce sont des marchés distincts, avec leurs propres règles locales d'achat : la même question posée à Pékin et à Chengdu n'appelle pas la même réponse.</p>
    </div>
    <div class="grid g3">{cn_villes}</div>
    <p class="note">Tu as écrit « Add China » sans liste de villes — contrairement à la Turquie, où les douze venaient de ton document. Cette sélection est donc la mienne, et je le dis plutôt que de la présenter comme un choix évident. Envoie ta liste et je remplace, dans ton ordre.</p>
  </div>
</section>

<section id="residences">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Nos programmes</div>
      <h2>De l'urbain à l'année, neuf et ancien.</h2>
      <p class="lede" style="margin-top:18px">Pas de logique balnéaire ici, à l'exception de Hainan : ce sont des marchés résidentiels de métropole, occupés à l'année. Les présenter comme une côte espagnole serait faux sur toute la ligne.</p>
    </div>
    <div class="grid g4">{cn_projects}</div>
    <p class="note">Fiches d'exemple. Tes programmes réels, avec photos, plans et prix, viendront les remplacer.</p>
  </div>
</section>

<section class="sand" id="processus">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Le processus</div>
      <h2>Acheter en Chine quand on n'y réside pas.</h2>
      <p class="lede" style="margin-top:18px">La première étape n'est pas une formalité : c'est une condition. Si l'éligibilité n'est pas acquise dans la ville visée, il n'y a pas d'opération, et les sept étapes suivantes n'ont pas lieu d'être. La quatrième, elle, se fait des années avant de servir.</p>
    </div>
    {steps(CN_ETAPES)}
  </div>
</section>

<section id="devises">
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <div class="eyebrow">Le point que l'on découvre trop tard</div>
        <h2>Entrer l'argent est une démarche. Le faire ressortir est un dossier.</h2>
        <p class="lede" style="margin-top:18px">Rapatrier le produit d'une vente suppose de démontrer l'origine des fonds entrés, la régularité de l'acquisition et le paiement des impôts dus. Ces preuves ne se fabriquent pas au moment de vendre : ce sont les justificatifs constitués à <b>l'achat</b> qui rendront la <b>sortie</b> possible dix ans plus tard.</p>
        <p class="lede" style="margin-top:14px">C'est le conseil le plus utile de cette page, et c'est pour ça qu'il est écrit ici en grand plutôt que rangé dans la FAQ. Un dossier d'entrée bâclé se paie à la revente, quand il est trop tard pour le reconstituer.</p>
      </div>
      <div>
        <div class="fc" style="margin-bottom:18px">
          {icon(ICONS["doc"])}
          <h3>Ce qui se conserve dès le premier virement</h3>
          <p>Justificatifs bancaires d'entrée des fonds et leur enregistrement, contrat enregistré auprès de l'autorité du logement, certificat de propriété, et l'ensemble des quittances d'impôts et de taxes liées à l'acquisition.</p>
        </div>
        <div class="fc">
          {icon(ICONS["shield"])}
          <h3>Le quota de conversion</h3>
          <p>La conversion de devises par personne physique est plafonnée par année civile. Ce montant est publié par l'administration des changes ; il n'est pas écrit ici tant qu'il n'a pas été vérifié à une date précise.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sand" id="couts">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Frais, taxes et conditions</div>
      <h2>Les montants ne sont pas écrits ici, et c'est volontaire.</h2>
      <p class="lede" style="margin-top:18px">Ce tableau nomme chaque poste et l'autorité qui en publie la valeur. Deux mentions différentes y figurent, et elles ne veulent pas dire la même chose.</p>
    </div>
    <div class="split" style="align-items:start">
      <div class="tbl-wrap"><table class="tbl">
        <tr><th>Poste</th><th>Valeur</th><th>Ce que c'est, et qui la publie</th></tr>
        {cn_bareme}
      </table></div>
      <div>
        <div class="fc" style="margin-bottom:18px">
          {icon(ICONS["shield"])}
          <h3>« À vérifier » et « non fixé » ne sont pas la même absence</h3>
          <p><span class="tbd">à vérifier</span> — la valeur existe, l'autorité qui la publie est nommée en face, et personne ne l'a encore vérifiée à une date précise.</p>
          <p><span class="tbd tbd-x">non fixé</span> — la valeur <b>n'existe pas</b> à ce jour. Écrire « à vérifier » là-dessus laisserait croire qu'il suffit de chercher. C'est le cas du coût de renouvellement du droit d'usage du sol : le renouvellement est prévu, son prix ne l'est pas.</p>
        </div>
        <div class="fc">
          {icon(ICONS["chart"])}
          <h3>Un point à suivre dans le temps</h3>
          <p>Une taxe foncière annuelle sur le résidentiel est annoncée et expérimentée localement depuis des années, sans généralisation à ce jour. Elle ne change rien à un achat aujourd'hui ; elle change tout au calcul de quelqu'un qui garde le bien vingt ans.</p>
        </div>
      </div>
    </div>
    <p class="note">Vérifié le <span class="tbd">à renseigner</span> — tant que cette date est vide, aucun montant n'est publié sur cette page.</p>
  </div>
</section>

<section class="dark" id="garanties">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Notre méthode</div><h2>Les vérifications qui évitent les mauvaises surprises.</h2></div>
    <div class="grid g3">
      <div class="box"><h3>Éligibilité confirmée par écrit, ville par ville</h3><p>Avant de visiter quoi que ce soit. Les conditions posées à un acheteur étranger ne sont pas les mêmes à Pékin, à Shanghai et à Chengdu, et elles ont déjà changé.</p></div>
      <div class="box"><h3>Durée résiduelle du droit d'usage lue au registre</h3><p>Dans l'ancien, c'est un élément de valeur au même titre que la surface. Elle ne se devine pas depuis l'annonce.</p></div>
      <div class="box"><h3>Permis de prévente exigé dans le neuf</h3><p>Un promoteur ne peut commercialiser sur plan sans lui. On le demande, on le lit, et on vérifie que le compte de supervision des fonds est bien celui qui reçoit les versements.</p></div>
      <div class="box"><h3>Charges inscrites vérifiées</h3><p>Titulaire réel, hypothèques, saisies, litiges en cours. Même exigence qu'en Espagne et en Turquie, sur un registre différent.</p></div>
      <div class="box"><h3>Dossier de change constitué dès l'entrée des fonds</h3><p>Parce que c'est lui qui autorisera la sortie du produit de la vente, des années plus tard.</p></div>
      <div class="box"><h3>Contrat lu en chinois</h3><p>C'est la version chinoise qui fait foi. Une traduction sert à comprendre, pas à se défendre : toute clause qui compte est vérifiée sur l'original, par quelqu'un qui le lit.</p></div>
    </div>
  </div>
</section>

<section class="sand" id="faq">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Questions fréquentes</div><h2>Chine — les questions qui reviennent.</h2></div>
    {faq(CN_FAQ)}
    <p class="note">Cette page couvre la Chine continentale. Hong Kong, Macao et Taïwan sont des systèmes juridiques distincts : droit de la propriété, fiscalité et règles pour les non-résidents y sont différents, et rien de ce qui précède ne s'y applique.</p>
  </div>
</section>

{contact("Chine — douze marchés", [n for n, _, _ in CN_VILLES] + ["Autre ville"])}
'''

if __name__ == "__main__":
    out = {
        "index.html": page(
            "Amarimmo — Promotion immobilière à Oran et Alger | Résidences modernes en Algérie",
            "Promoteur immobilier en Algérie. Résidences modernes à Oran et Alger, vente sur plan encadrée par acte notarié, suivi de chantier et accompagnement jusqu'au livret foncier.",
            dz_body, "dz"),
        "espagne.html": page(
            "Amarimmo Espagne — Acheter un bien sur la Costa del Sol, la Costa Blanca et à Barcelone",
            "Acquisition immobilière en Espagne pour non-résidents : NIE, contrat d'arras, escritura, frais réels et fiscalité. Programmes neufs sur la côte et ancien réhabilité en ville.",
            es_body, "es"),
        "turquie.html": page(
            "Amarimmo Turquie — Acheter un bien à Istanbul, Antalya, Izmir, Bodrum et neuf autres marchés",
            "Acquisition immobilière en Turquie pour acheteurs étrangers : tapu, rapport d'expertise "
            "obligatoire, zones interdites, assurance séisme, et douze marchés expliqués. Aucun seuil "
            "d'investissement publié sans date de vérification.",
            tr_body, "tr"),
        "chine.html": page(
            "Amarimmo Chine — Acheter un logement à Shanghai, Pékin, Shenzhen et neuf autres marchés",
            "Acquisition immobilière en Chine continentale pour acheteurs étrangers : droit d'usage "
            "du sol, conditions d'éligibilité ville par ville, contrôle des changes à l'entrée comme "
            "à la sortie. Aucun taux ni seuil publié sans date de vérification.",
            cn_body, "cn"),
    }
    for name, content in out.items():
        p = os.path.join(HERE, name)
        open(p, "w", encoding="utf-8").write(content)
        print(f"  {name}  {len(content)//1024} KB")
    print(f"built {len(out)} pages")
