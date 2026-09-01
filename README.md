# Amarimmo — maquette statique, cinq marchés

Algérie · Espagne · Turquie · Chine continentale · Égypte.

Cinq pages HTML, une feuille de style, vingt-cinq illustrations SVG. Aucune
dépendance externe, aucun script tiers, rien à installer : on dépose le dossier
tel quel sur l'hébergement et ça marche.

## Contenu

```
index.html        Algérie   — promotion et vente sur plan
espagne.html      Espagne   — acquisition par un non-résident
turquie.html      Turquie   — douze marchés
chine.html        Chine     — douze marchés, Chine continentale uniquement
egypte.html       Égypte    — douze marchés, DEUX régimes d'acquisition
assets/           site.css + 25 illustrations SVG
source/           les scripts qui régénèrent le tout
```

## Régénérer

```
cd source
python3 gen_visuals.py     # écrit les 25 SVG dans ../assets — graines fixes,
                           # deux exécutions donnent des fichiers identiques
python3 build.py           # écrit les 5 pages HTML
```

Le gabarit (en-tête, pied de page, feuille de style) est écrit **une seule
fois** dans `build.py`. C'est ce qui évite que les cinq pages divergent à la
première correction.

Si une feuille de style change, le numéro de version dans `build.py`
(`site.css?v=5`) doit être incrémenté, sinon le navigateur ressert l'ancien
fichier et le test se répète pour rien.

## Une correction qui touche les cinq pages

Le sur-titre doré du bandeau d'accueil (« ACQUISITION — ÉGYPTE » et ses
équivalents) était posé directement sur le ciel de l'illustration. Mesuré en
échantillonnant les pixels derrière le libellé : **1,01:1 sur l'Égypte, 1,02
sur l'Espagne, 1,10 sur la Turquie, 1,13 sur l'Algérie** — c'est-à-dire
illisible sur quatre pages sur cinq, et depuis le début. Seule la page Chine,
au ciel de nuit, passait.

Il est désormais posé sur une pastille sombre : **9,75:1 dans le pire cas**. La
mesure est entrée dans la suite de vérification pour que ça ne revienne pas.

Une première tentative par ombre portée n'avait rien donné (1,15:1) : une ombre
n'assombrit qu'un halo autour des lettres, pas ce qu'il y a entre elles.

## Deux règles de contenu, tenues sur les cinq pages

**1. Rien d'inventé sur l'entreprise.** Pas d'années d'expérience, pas de
nombre de logements livrés, pas d'équipe, pas de récompense, pas d'adresse, pas
de numéro d'agrément. Les fiches de résidences sont marquées « exemple » et
chaque page porte un bandeau de démonstration.

**2. Aucun montant réglementaire n'est publié sans date de vérification.**
Un mécanisme est stable — le titre turc s'appellera encore le tapu dans trois
ans. Un taux ou un seuil, non. Un chiffre périmé sur un site immobilier ne se
signale pas tout seul : il reste affiché, il a l'air juste, et quelqu'un engage
plusieurs centaines de milliers de dollars dessus. Les pages Turquie, Chine et
Égypte affichent donc des cases **visiblement vides**, avec le nom de l'autorité
qui publie la valeur en face.

Sur les pages Chine et Égypte, deux mentions différentes, et elles ne disent pas
la même chose :

| mention | ce que ça veut dire |
|---|---|
| `à vérifier` (ambre) | la valeur existe, l'autorité est nommée, personne ne l'a encore vérifiée à une date précise |
| `non fixé` (gris) | la valeur **n'existe pas** — écrire « à vérifier » enverrait quelqu'un chercher un chiffre que personne n'a jamais écrit |

Le second cas n'est pas théorique. Chine : le coût de renouvellement du droit
d'usage du sol est prévu par le Code civil et n'a jamais été chiffré par un
texte d'application. Égypte : aucune autorité ne publie de barème de commission
d'agence, et aucun texte n'encadre la révision d'un échéancier de promoteur —
la réponse est dans la clause du contrat, nulle part ailleurs.

## Pourquoi la page Chine n'est pas la page Turquie avec d'autres villes

Deux différences de fond, écrites en haut de page et pas en note :

- **Personne n'achète le sol en Chine**, pas même un acheteur chinois. On
  acquiert le bâti et un droit d'usage du sol pour une durée déterminée. Dans
  l'ancien, la durée qui *reste* est un élément de valeur au même titre que la
  surface.
- **Acheter n'ouvre aucun droit de séjour ni la nationalité**, à aucun montant.
  Il n'existe pas de programme d'investissement immobilier de ce type.

La page couvre la **Chine continentale**. Hong Kong, Macao et Taïwan sont des
systèmes juridiques distincts et rien de ce qui y est écrit ne s'y applique.

## Pourquoi la page Égypte n'est pas la page Chine avec d'autres villes

Là encore deux différences de fond, en haut de page :

- **Un contrat n'est pas un titre.** Une part importante des transactions se
  fait sur un contrat de vente non enregistré. Ce contrat crée une créance
  *contre le vendeur* ; l'inscription au service de la publicité foncière crée
  un droit *opposable à tous*. Le contournement usuel — l'action en validité et
  opposabilité — renforce la position de l'acheteur mais **ne remplace pas
  l'inscription**, et les deux sont trop souvent présentés comme équivalents.
- **La règle n'est pas nationale.** C'est le seul des cinq marchés dans ce cas.
  Le Sinaï n'ouvre pas la pleine propriété à un acheteur étranger. Or Charm
  el-Cheikh et Dahab sont dans le Sinaï, et ce sont deux des premières
  destinations que cherche un acheteur étranger ; Hurghada et El Gouna, sur la
  côte ouest de la mer Rouge, n'y sont pas.

C'est pour ça que la grille des villes porte un **régime par ville**
(`.reg-pp` / `.reg-sn` dans la feuille de style) au lieu d'une note de bas de
page. Une liste de douze villes sans cette mention laisserait conclure à un
marché homogène qui n'existe pas.

Et une divergence à ne pas gommer entre les deux pages : la Chine dit *aucune
voie de séjour ni de nationalité, à aucun montant* ; l'Égypte dit *des voies
existent, sous conditions de montant et de provenance des fonds*. Les deux pages
se suivent dans le menu, donc chacune l'écrit explicitement.

## Ce qui reste à faire

- Les montants des tableaux Turquie, Chine et Égypte, chacun avec sa date de
  vérification. Les champs « Vérifié le ___ » sont déjà en place.
- Les coordonnées réelles (le pied de page dit « à compléter »).
- Les mentions légales et la politique de confidentialité.
- Le formulaire de contact n'a pas d'adresse de réception : il est intercepté
  en JavaScript pour ne pas recharger la page et avoir l'air cassé.
- Les fiches de résidences et les visuels, à remplacer par les programmes réels.
- Les listes de villes Chine et Égypte sont les miennes, faute de liste envoyée.
  Celle de la Turquie vient du document du client.
