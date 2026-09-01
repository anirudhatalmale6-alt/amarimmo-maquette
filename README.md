# Amarimmo — maquette statique, quatre marchés

Algérie · Espagne · Turquie · Chine continentale.

Quatre pages HTML, une feuille de style, vingt illustrations SVG. Aucune
dépendance externe, aucun script tiers, rien à installer : on dépose le dossier
tel quel sur l'hébergement et ça marche.

## Contenu

```
index.html        Algérie   — promotion et vente sur plan
espagne.html      Espagne   — acquisition par un non-résident
turquie.html      Turquie   — douze marchés
chine.html        Chine     — douze marchés, chine continentale uniquement
assets/           site.css + 20 illustrations SVG
source/           les scripts qui régénèrent le tout
```

## Régénérer

```
cd source
python3 gen_visuals.py     # écrit les 20 SVG dans ../assets — graines fixes,
                           # deux exécutions donnent des fichiers identiques
python3 build.py           # écrit les 4 pages HTML
```

Le gabarit (en-tête, pied de page, feuille de style) est écrit **une seule
fois** dans `build.py`. C'est ce qui évite que les quatre pages divergent à la
première correction.

## Deux règles de contenu, tenues sur les quatre pages

**1. Rien d'inventé sur l'entreprise.** Pas d'années d'expérience, pas de
nombre de logements livrés, pas d'équipe, pas de récompense, pas d'adresse, pas
de numéro d'agrément. Les fiches de résidences sont marquées « exemple » et
chaque page porte un bandeau de démonstration.

**2. Aucun montant réglementaire n'est publié sans date de vérification.**
Un mécanisme est stable — le titre turc s'appellera encore le tapu dans trois
ans. Un taux ou un seuil, non. Un chiffre périmé sur un site immobilier ne se
signale pas tout seul : il reste affiché, il a l'air juste, et quelqu'un engage
plusieurs centaines de milliers de dollars dessus. Les pages Turquie et Chine
affichent donc des cases **visiblement vides**, avec le nom de l'autorité qui
publie la valeur en face.

Sur la page Chine, deux mentions différentes, et elles ne disent pas la même
chose :

| mention | ce que ça veut dire |
|---|---|
| `à vérifier` (ambre) | la valeur existe, l'autorité est nommée, personne ne l'a encore vérifiée à une date précise |
| `non fixé` (gris) | la valeur **n'existe pas** à ce jour — écrire « à vérifier » ferait croire qu'il suffit de chercher |

Le second cas n'est pas théorique : le coût de renouvellement du droit d'usage
du sol est prévu par le Code civil chinois et n'a jamais été chiffré par un
texte d'application.

## Pourquoi la page Chine n'est pas la page Turquie avec d'autres villes

Deux différences de fond, écrites en haut de page et pas en note :

- **Personne n'achète le sol en Chine**, pas même un acheteur chinois. On
  acquiert le bâti et un droit d'usage du sol pour une durée déterminée. Dans
  l'ancien, la durée qui *reste* est un élément de valeur au même titre que la
  surface.
- **Acheter n'ouvre aucun droit de séjour ni la nationalité**, à aucun montant.
  Il n'existe pas de programme d'investissement immobilier de ce type. Sur un
  site qui présente quatre marchés côte à côte, ne pas l'écrire laisserait le
  lecteur transposer ce qu'il a lu sur la page précédente.

La page couvre la **Chine continentale**. Hong Kong, Macao et Taïwan sont des
systèmes juridiques distincts et rien de ce qui y est écrit ne s'y applique.

## Ce qui reste à faire

- Les montants des tableaux Turquie et Chine, chacun avec sa date de
  vérification. Les champs « Vérifié le ___ » sont déjà en place.
- Les coordonnées réelles (le pied de page dit « à compléter »).
- Les mentions légales et la politique de confidentialité.
- Le formulaire de contact n'a pas d'adresse de réception : il est intercepté
  en JavaScript pour ne pas recharger la page et avoir l'air cassé.
- Les fiches de résidences et les visuels, à remplacer par les programmes réels.
