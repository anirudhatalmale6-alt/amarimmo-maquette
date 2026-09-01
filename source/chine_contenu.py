# -*- coding: utf-8 -*-
"""
Amarimmo — Chine. Contenu de la quatrième page de marché.

POURQUOI CETTE PAGE NE RESSEMBLE PAS AUX TROIS AUTRES.

Algérie, Espagne, Turquie : trois marchés où un étranger peut acheter, sous
conditions, un bien dont il devient propriétaire. La page se construit alors
naturellement — voici les villes, voici le processus, voici les frais.

La Chine ne fonctionne pas comme ça, et écrire la même page en changeant les
noms de villes serait une page fausse. Deux différences de fond :

  1. PERSONNE n'achète le sol en Chine. Ni un étranger, ni un Chinois. Le sol
     urbain appartient à l'État. Ce qui s'achète est un DROIT D'USAGE du sol
     pour une durée déterminée, plus la propriété du bâti. C'est la première
     phrase de la page, pas une note de bas de page, parce qu'un acheteur qui
     croit acheter la pleine propriété achète autre chose que ce qu'il croit.

  2. L'achat par un étranger est encadré par un principe d'USAGE PROPRE, pas
     par un droit d'investir librement. Les conditions d'éligibilité sont
     fixées au niveau national ET par chaque municipalité, elles diffèrent
     d'une ville à l'autre, et elles ont bougé plusieurs fois. Un étranger
     peut se voir refuser l'achat sans que rien ne soit négociable.

Et une différence qui compte autant que les deux premières : acheter un bien
en Chine n'ouvre AUCUNE voie vers un titre de séjour ni vers la nationalité.
Il n'existe pas de programme d'investissement immobilier donnant un droit de
séjour, contrairement à ce qui existe ailleurs. Sur un site qui présente
quatre marchés côte à côte, ne pas l'écrire noir sur blanc laisserait le
lecteur transposer ce qu'il a lu sur la page précédente.

CE QUI EST ÉCRIT, CE QUI RESTE VIDE — même règle que la page Turquie :
un mécanisme est stable, un taux ou un seuil bouge. Les mécanismes sont
écrits. Les montants restent visiblement vides, avec le nom de l'autorité qui
les publie, et un champ « vérifié le » qui reste vide tant que personne n'a
vérifié.

UN POINT SUPPLÉMENTAIRE, PROPRE À CE MARCHÉ : la vraie difficulté n'est pas
d'entrer l'argent, c'est de le faire ressortir. Le contrôle des changes est
administré et documenté. Cette question se prépare à l'achat, pas à la
revente — c'est le conseil le plus utile de la page et il est écrit en clair
plutôt que dilué dans une FAQ.
"""

# Le client a écrit « Add China » sans liste de villes — contrairement à la
# Turquie, où les douze destinations venaient de son document. Ces douze-ci
# sont donc MON choix : les quatre métropoles de premier rang, sept grandes
# métropoles régionales, et un marché littoral. Elles sont dites comme telles
# sur la page. S'il envoie sa liste, je remplace dans son ordre.

VILLES = [
    ("Pékin", "Municipalité — Nord",
     "Capitale politique et administrative. Marché parmi les plus encadrés du pays : les "
     "conditions locales d'achat y sont historiquement les plus strictes, pour les acheteurs "
     "chinois comme étrangers."),
    ("Shanghai", "Municipalité — Delta du Yangtsé",
     "Première place financière du pays et marché le plus internationalisé. C'est aussi la ville "
     "où la population étrangère résidente est la plus nombreuse, donc celle où le cadre de "
     "l'achat par un étranger est le mieux rodé."),
    ("Shenzhen", "Guangdong — Delta de la rivière des Perles",
     "Pôle technologique adossé à Hong Kong. Marché jeune, cher, et très sensible aux mesures "
     "d'encadrement — les règles locales y bougent plus souvent qu'ailleurs."),
    ("Canton", "Guangdong — Delta de la rivière des Perles",
     "Grande métropole commerçante du sud, historiquement tournée vers l'export. Marché plus "
     "large et moins tendu que Shenzhen à quelques dizaines de kilomètres de là."),
    ("Chengdu", "Sichuan — Ouest",
     "Métropole de l'ouest, forte croissance démographique et pôle universitaire. Marché "
     "intérieur, très peu exposé à la demande étrangère."),
    ("Hangzhou", "Zhejiang — Delta du Yangtsé",
     "Pôle numérique à une heure de Shanghai. Marché résidentiel urbain adossé à un bassin "
     "d'emploi qualifié."),
    ("Chongqing", "Municipalité — Sud-Ouest",
     "L'une des plus vastes municipalités du pays, sur le Yangtsé. Marché intérieur, offre "
     "abondante, dynamique très différente du littoral."),
    ("Wuhan", "Hubei — Centre",
     "Carrefour ferroviaire et fluvial du centre du pays, très gros pôle universitaire. Marché "
     "local à l'année."),
    ("Xi'an", "Shaanxi — Nord-Ouest",
     "Capitale historique et pôle industriel du nord-ouest. Marché intérieur, saisonnalité "
     "touristique sans effet notable sur le résidentiel."),
    ("Nankin", "Jiangsu — Delta du Yangtsé",
     "Capitale provinciale du Jiangsu, deuxième pôle du delta après Shanghai. Marché urbain "
     "à l'année."),
    ("Tianjin", "Municipalité — Nord",
     "Port du nord, relié à Pékin par ligne à grande vitesse. Marché souvent lu comme un "
     "report de la demande pékinoise, ce qui est une simplification."),
    ("Sanya", "Hainan — Littoral tropical",
     "Station balnéaire de l'île de Hainan, seul marché franchement saisonnier de cette liste. "
     "Hainan relève d'un régime de port de libre-échange dont les règles propres évoluent, y "
     "compris en matière d'achat."),
]

# Ce que sont réellement les étapes, dans l'ordre où elles se posent.
# L'étape 1 est une CONDITION, pas une formalité : si elle n'est pas remplie,
# il n'y a pas d'opération, et aucune des suivantes n'a lieu d'être.
ETAPES = [
    ("Vérifier l'éligibilité — avant toute autre chose",
     "L'achat par un étranger repose sur un principe d'usage propre : on achète un logement "
     "pour l'habiter, pas un portefeuille. Des conditions s'y ajoutent — durée de travail ou "
     "d'études préalable en Chine, nombre de logements, conditions posées par la municipalité "
     "concernée. Elles diffèrent d'une ville à l'autre et elles ont été modifiées plusieurs "
     "fois. Cette vérification se fait auprès de l'autorité du logement de la ville visée, et "
     "elle se fait en premier : c'est un oui ou un non, pas une négociation."),
    ("Comprendre ce qui s'achète : le droit d'usage du sol, pas le sol",
     "Le sol urbain appartient à l'État. Un acquéreur, chinois ou étranger, obtient la propriété "
     "du bâti et un droit d'usage du sol accordé pour une durée déterminée — la durée résidentielle "
     "usuelle est la plus longue des trois catégories, devant le commercial et l'industriel. Le "
     "titre unique délivré depuis la réforme de l'enregistrement immobilier porte les deux."),
    ("Ouvrir un compte bancaire chinois et préparer l'entrée des fonds",
     "Les paiements se font depuis un compte chinois. L'entrée de fonds étrangers suit une "
     "procédure documentée auprès de l'administration des changes, via la banque. C'est une "
     "démarche de dossier, pas un virement : elle se prépare avant la réservation."),
    ("Préparer dès maintenant la sortie des fonds à la revente",
     "C'est le point que les acheteurs étrangers découvrent trop tard. Rapatrier le produit d'une "
     "vente suppose de pouvoir prouver l'origine des fonds entrés, la régularité de l'acquisition "
     "et le paiement des impôts dus. Les justificatifs de l'ACHAT sont ce qui rendra la SORTIE "
     "possible des années plus tard. On les constitue et on les conserve maintenant."),
    ("Vérifier le titre et ce qui est inscrit dessus",
     "Consultation du registre immobilier : titulaire réel, durée résiduelle du droit d'usage du "
     "sol, hypothèques, saisies, litiges. La durée résiduelle est propre à ce marché — deux biens "
     "identiques n'ont pas la même valeur si l'un a vingt ans de droit d'usage de moins que l'autre."),
    ("Dans le neuf : permis de prévente et compte de supervision",
     "Un promoteur ne peut commercialiser sur plan qu'avec un permis de prévente, et les fonds des "
     "acquéreurs transitent par un compte de supervision destiné à les affecter au chantier. Après "
     "les difficultés de plusieurs promoteurs, c'est la vérification la plus importante du neuf : "
     "on demande le permis et on vérifie que le compte de supervision est bien celui utilisé."),
    ("Contrat, enregistrement, délivrance du titre",
     "Le contrat de vente est enregistré auprès de l'autorité du logement, puis le transfert est "
     "inscrit au registre immobilier et le certificat est délivré au nom de l'acquéreur. Tant que "
     "cette inscription n'est pas faite, la propriété n'est pas transférée, quels que soient les "
     "documents signés et les sommes versées."),
    ("Après l'acquisition",
     "Charges de copropriété, fonds de maintenance des parties communes, abonnements, et les "
     "obligations déclaratives d'un non-résident. Ces montants s'établissent ville par ville et "
     "se chiffrent avant l'achat."),
]

# LES MONTANTS SONT VIDES. Voir l'en-tête du fichier.
# Deux natures d'absence, et elles ne se confondent pas :
#   « à vérifier »  = la valeur existe, publiée par l'autorité nommée en face,
#                     et personne ne l'a encore vérifiée à une date précise.
#   « non fixé »    = la valeur N'EXISTE PAS à ce jour. Écrire « à vérifier »
#                     là-dessus laisserait croire qu'il suffit de chercher.
BAREME = [
    ("Droit de mutation à l'acquisition", "verif",
     "taux selon la surface et le rang d'acquisition",
     "Administration fiscale de l'État"),
    ("TVA en cas de revente avant la durée de détention déclenchante", "verif",
     "taux, et durée de détention qui l'exonère",
     "Administration fiscale de l'État"),
    ("Impôt sur le revenu à la revente", "verif",
     "assiette et taux applicables à un non-résident",
     "Administration fiscale de l'État"),
    ("Fonds de maintenance des parties communes", "verif",
     "pourcentage du prix, fixé localement",
     "Autorité du logement de la municipalité"),
    ("Ancienneté de travail ou d'études exigée d'un acheteur étranger", "verif",
     "durée requise avant l'achat, variable selon la ville",
     "Règles nationales et autorité du logement de chaque ville"),
    ("Conditions locales d'achat", "verif",
     "nombre de logements autorisés et conditions de résidence",
     "Autorité du logement de chaque ville"),
    ("Quota annuel de conversion de devises par personne", "verif",
     "montant convertible par année civile",
     "Administration d'État des changes"),
    ("Durée du droit d'usage du sol — résidentiel", "verif",
     "durée maximale d'octroi, fixée par la loi",
     "Code civil et règlement d'octroi des droits d'usage du sol"),
    ("Coût du renouvellement à l'échéance du droit d'usage", "nonfixe",
     "le renouvellement du résidentiel est automatique ; son coût, sa réduction "
     "ou son exonération relèvent de textes d'application qui ne sont pas parus",
     "Code civil — textes d'application attendus"),
    ("Taxe foncière annuelle sur le résidentiel", "nonfixe",
     "annoncée et expérimentée localement, non généralisée à ce jour ; "
     "un investisseur qui garde le bien longtemps doit suivre ce point",
     "Législateur national — réforme en cours"),
]

FAQ = [
    ("Un étranger peut-il acheter un logement en Chine ?",
     "<p>Oui, mais pas librement, et pas partout dans les mêmes conditions. Le cadre repose sur "
     "l'usage propre : on achète un logement pour l'habiter. À cela s'ajoutent des conditions "
     "nationales — une ancienneté de travail ou d'études en Chine — et les conditions propres à "
     "chaque municipalité, qui limitent aussi le nombre de logements.</p>"
     "<p>Ces conditions ont été durcies puis assouplies à plusieurs reprises, et elles ne sont pas "
     "les mêmes à Pékin et à Chengdu. C'est la première chose à vérifier, avant même de regarder "
     "un bien : ce n'est pas une formalité qui se règle plus tard.</p>"),

    ("Achète-t-on vraiment le terrain ?",
     "<p><b>Non — et personne ne l'achète, y compris les acheteurs chinois.</b> Le sol urbain "
     "appartient à l'État. Ce qui s'acquiert, c'est la propriété du bâti et un droit d'usage du "
     "sol accordé pour une durée déterminée.</p>"
     "<p>Conséquence concrète, et elle est mal comprise : dans l'ancien, la durée qui RESTE compte "
     "autant que l'état du bien. Deux appartements identiques n'ont pas la même valeur si l'un a "
     "vingt ans de droit d'usage de moins que l'autre. Cette durée résiduelle figure au registre "
     "immobilier et se vérifie avant de faire une offre.</p>"),

    ("Que se passe-t-il à l'expiration du droit d'usage ?",
     "<p>Pour le résidentiel, le Code civil prévoit un renouvellement automatique à l'échéance : "
     "le propriétaire ne perd pas son logement.</p>"
     "<p>En revanche, <b>le coût de ce renouvellement n'est pas fixé.</b> Le texte renvoie à des "
     "règles d'application qui, à ce jour, n'ont pas été publiées. Nous l'écrivons tel quel, parce "
     "que c'est une question ouverte et non un détail : personne aujourd'hui ne peut dire "
     "honnêtement ce que coûtera le renouvellement, et un site qui avance un chiffre là-dessus "
     "invente.</p>"),

    ("Acheter un bien donne-t-il un droit de séjour ou la nationalité ?",
     "<p><b>Non. Aucun des deux, à aucun montant.</b> Il n'existe pas en Chine de programme de "
     "titre de séjour ou de nationalité par investissement immobilier. La résidence permanente "
     "existe mais répond à des critères qui n'ont rien à voir avec l'achat d'un logement, et la "
     "naturalisation est exceptionnelle.</p>"
     "<p>Nous l'écrivons explicitement parce que ce site présente plusieurs marchés côte à côte, et "
     "que ce qui vaut sur une autre page ne vaut pas ici.</p>"),

    ("Pourra-t-on faire ressortir l'argent après la revente ?",
     "<p>C'est la vraie question de ce marché, et elle se prépare à l'achat.</p>"
     "<p>Le rapatriement du produit d'une vente passe par une procédure documentée auprès de "
     "l'administration des changes, via la banque. Il faut pouvoir démontrer l'origine des fonds "
     "qui sont entrés, la régularité de l'acquisition et le paiement des impôts dus. Autrement dit, "
     "ce sont les justificatifs constitués au moment de l'ACHAT qui rendront la SORTIE possible dix "
     "ans plus tard. Un dossier d'entrée bâclé se paie à la revente, quand il est trop tard pour le "
     "reconstituer.</p>"),

    ("Peut-on acheter pour louer ?",
     "<p>Il faut être prudent avec cette question. L'autorisation d'acheter accordée à un étranger "
     "repose sur l'usage propre du logement. Une acquisition présentée d'emblée comme un "
     "placement locatif n'est donc pas la même opération, et les règles applicables à la mise en "
     "location varient d'une ville à l'autre.</p>"
     "<p>Nous ne répondons pas oui ou non ici à la place de l'autorité compétente. La réponse se "
     "demande pour la ville visée, avant l'achat, et par écrit.</p>"),

    ("Hong Kong, Macao et Taïwan, c'est pareil ?",
     "<p>Non. Ce sont des systèmes juridiques distincts, avec leur propre droit de la propriété, "
     "leur propre fiscalité et leurs propres règles pour les acheteurs non résidents. Rien de ce "
     "qui est écrit sur cette page ne s'y applique.</p>"
     "<p>Hong Kong en particulier est un marché à part entière, avec sa fiscalité de transaction "
     "propre — laquelle a été modifiée récemment. Il mérite sa page, pas un paragraphe.</p>"),

    ("Faut-il se déplacer pour signer ?",
     "<p>Une procuration est possible, mais son formalisme est strict et c'est là que les dossiers "
     "traînent. Depuis l'entrée en vigueur de la convention Apostille pour la Chine, le "
     "7 novembre 2023, un document public émis dans un autre État partie s'authentifie par apostille "
     "au lieu de la légalisation consulaire — nettement plus rapide. Cela ne dispense ni de la "
     "traduction en chinois ni des exigences propres à l'autorité qui reçoit le document.</p>"),

    ("Dans quelle langue le contrat fait-il foi ?",
     "<p>En chinois. Une traduction française ou anglaise sert à comprendre ; ce n'est pas elle qui "
     "sera lue en cas de litige. Toute clause qui compte doit donc être vérifiée sur la version "
     "chinoise, par quelqu'un qui la lit — et non sur la traduction de courtoisie fournie avec.</p>"),
]
