# -*- coding: utf-8 -*-
"""
Amarimmo — Égypte. Contenu de la cinquième page de marché.

POURQUOI CETTE PAGE N'EST PAS LA PAGE TURQUIE AVEC D'AUTRES VILLES.

Quatre marchés déjà en ligne : Algérie, Espagne, Turquie, Chine. Trois d'entre
eux ont une règle NATIONALE et un TITRE qui existe. L'Égypte diffère sur ces
deux points exactement, et ce sont les deux blocs de haut de page.

  1. UN CONTRAT N'EST PAS UN TITRE.
     En Espagne il y a l'escritura, en Turquie le tapu, en Chine le certificat
     de propriété. En Égypte, une part très importante des transactions se fait
     sur un contrat de vente NON ENREGISTRÉ. Le contrat crée une créance contre
     le vendeur ; il ne crée pas un droit opposable à tout le monde. Tant que
     l'acte n'est pas inscrit au service de la publicité foncière, l'acheteur
     a payé et détient un papier, pas la propriété.
     Le contournement usuel — l'action en « validité et opposabilité » qui fait
     constater la vente par un juge — n'est PAS un enregistrement. C'est mieux
     que rien et ce n'est pas un titre. Écrire l'un pour l'autre serait la
     faute la plus coûteuse que cette page puisse commettre.

  2. LA RÈGLE N'EST PAS LA MÊME PARTOUT DANS LE PAYS.
     Sur les quatre autres marchés, le régime d'acquisition est national : ce
     qui vaut à Alicante vaut à Barcelone. En Égypte non. Le Sinaï relève d'un
     régime distinct où un étranger n'accède pas à la pleine propriété — l'usage
     y passe par un droit d'usage à durée déterminée. Et ce n'est pas un détail
     de géographie : Charm el-Cheikh et Dahab, qui sont parmi les premières
     destinations que cherche un acheteur étranger, sont dans le Sinaï.
     D'où un choix de conception : le régime est affiché SUR CHAQUE VILLE, dans
     la grille, et pas renvoyé à une note. Une liste de douze villes sans cette
     mention laisserait croire à un marché homogène qui n'existe pas.

CE QUI CHANGE AUSSI PAR RAPPORT À LA CHINE — et il faut le dire, parce que la
page Chine est juste à côté dans le menu : ici, une voie de séjour et une voie
de nationalité liées à un investissement immobilier EXISTENT. La page Chine dit
« aucune, à aucun montant ». Un lecteur qui enchaîne les deux pages doit voir
la différence tout de suite, sinon il transpose. Les MONTANTS, eux, restent
vides comme partout ailleurs sur ce site.

L'ARGENT : ici le point sensible est l'ENTRÉE, pas la sortie.
En Chine, la difficulté est de faire ressortir le produit de la vente. En
Égypte, la difficulté est de prouver que l'argent est entré par le canal
bancaire, en devises, depuis l'étranger. C'est ce justificatif qui conditionne
à la fois les voies de séjour et de nationalité, et la possibilité de
rapatrier plus tard. Un achat payé hors du système bancaire n'est pas
« moins bien documenté » : il ferme des portes définitivement.

RÈGLE DES CHIFFRES, inchangée depuis la page Turquie : un mécanisme est stable,
un taux ou un seuil bouge. Les mécanismes sont écrits. Les montants restent
visiblement vides, avec le nom de l'autorité qui les publie, et un champ
« vérifié le » qui reste vide tant que personne n'a vérifié. Deux natures
d'absence, comme sur la page Chine : « à vérifier » et « non fixé ».
"""

# Le client a écrit « And egypt », sans liste de villes — comme pour la Chine,
# et contrairement à la Turquie où les douze venaient de son document. Cette
# sélection est donc la mienne et la page le dit.
#
# Quatrième élément du tuple : le RÉGIME. C'est la différence de structure avec
# les quatre autres pages, où une seule règle vaut pour tout le pays.
#   "pp"    -> pleine propriété accessible à un étranger, sous les conditions
#              de la loi (nombre de biens, surface, délai de revente).
#   "sinai" -> Sinaï : pas de pleine propriété pour un étranger. Droit d'usage
#              à durée déterminée, et procédure d'autorisation distincte.
VILLES = [
    ("Le Caire", "Gouvernorat du Caire", "pp",
     "Capitale et premier marché du pays. Marché résidentiel à l'année, très segmenté d'un "
     "quartier à l'autre, avec un ancien souvent mal enregistré — c'est ici que la question du "
     "titre se pose le plus souvent."),
    ("Nouvelle Capitale administrative", "Gouvernorat du Caire — est", "pp",
     "Ville nouvelle édifiée à l'est du Caire, où l'offre est presque entièrement neuve et vendue "
     "sur plan par des promoteurs, avec des échéanciers longs. Marché de livraison future : ce "
     "qu'on achète est un engagement de livrer."),
    ("Nouveau Caire", "Gouvernorat du Caire — est", "pp",
     "Ensemble de quartiers récents à l'est de la capitale, résidences fermées et services. "
     "Marché occupé à l'année, très demandé par les familles et par la diaspora."),
    ("Cheikh Zayed et 6-Octobre", "Gouvernorat de Gizeh", "pp",
     "Pendant occidental du Nouveau Caire, de l'autre côté du Nil. Même logique de résidences "
     "récentes, marché à l'année, offre neuve et ancien récent."),
    ("Gizeh", "Gouvernorat de Gizeh", "pp",
     "Marché urbain dense en continuité du Caire. Beaucoup d'ancien, donc beaucoup de biens dont "
     "l'historique de propriété demande à être reconstitué avant toute offre."),
    ("Alexandrie", "Gouvernorat d'Alexandrie", "pp",
     "Deuxième ville du pays, sur la Méditerranée. Marché mixte : résidentiel à l'année en ville, "
     "saisonnier sur la côte ouest. Nombreux immeubles anciens en indivision familiale."),
    ("El-Alamein", "Gouvernorat de Marsa-Matrouh", "pp",
     "Côte méditerranéenne à l'ouest d'Alexandrie, où une ville nouvelle balnéaire sort de terre. "
     "Marché saisonnier et très majoritairement sur plan."),
    ("Aïn Sokhna", "Gouvernorat de Suez", "pp",
     "Littoral de la mer Rouge le plus proche du Caire, à quelques heures de route. Marché de "
     "résidence secondaire pour la clientèle cairote, forte saisonnalité."),
    ("Hurghada", "Gouvernorat de la mer Rouge", "pp",
     "Principal marché balnéaire ouvert aux acheteurs étrangers, sur la côte occidentale de la mer "
     "Rouge — donc hors Sinaï, et la pleine propriété y est accessible. Offre abondante, écarts "
     "de qualité importants d'un programme à l'autre."),
    ("El Gouna", "Gouvernorat de la mer Rouge", "pp",
     "Station intégrée au nord de Hurghada, développée par un promoteur unique. Marché à part, "
     "avec ses propres règles de copropriété et de gestion locative."),
    ("Charm el-Cheikh", "Sinaï Sud", "sinai",
     "Première destination balnéaire du pays et l'une des plus recherchées par les acheteurs "
     "étrangers — et elle est dans le Sinaï. La pleine propriété n'y est pas accessible à un "
     "étranger : l'accès se fait par un droit d'usage à durée déterminée, avec une procédure "
     "d'autorisation propre. Rien de ce qui vaut à Hurghada ne s'y applique tel quel."),
    ("Dahab", "Sinaï Sud", "sinai",
     "Petite station de la côte est du Sinaï, marché confidentiel et très recherché. Même régime "
     "que Charm el-Cheikh : pas de pleine propriété pour un étranger."),
]

# L'ordre compte. L'étape 1 est une CONDITION de lieu : selon l'endroit, ce
# n'est pas la même opération juridique. L'étape 2 est une condition de forme
# du paiement, et elle se prépare AVANT de réserver — pas au moment de payer.
ETAPES = [
    ("Regarder d'abord OÙ se trouve le bien",
     "Ce n'est pas une formalité de dossier, c'est ce qui détermine la nature de l'opération. Sur "
     "la plus grande partie du pays, un étranger peut devenir pleinement propriétaire, dans les "
     "limites fixées par la loi. Dans le Sinaï, non : l'accès passe par un droit d'usage à durée "
     "déterminée et par une procédure d'autorisation distincte. S'y ajoutent des zones frontalières "
     "et stratégiques soumises à approbation, dont le périmètre est fixé par décret. La question se "
     "pose pour la parcelle précise, avant tout le reste."),
    ("Faire entrer les fonds par le canal bancaire, en devises, et garder la preuve",
     "Le virement se fait depuis l'étranger vers une banque égyptienne, en devises, au nom de "
     "l'acquéreur. La banque délivre une attestation de transfert. Ce document est le pivot de tout "
     "le dossier : c'est lui qui ouvre les voies de séjour et de nationalité liées à "
     "l'investissement, et c'est lui qui permettra de justifier l'origine des fonds à la revente. "
     "Payer en espèces ou par un circuit parallèle ne rend pas le dossier « moins complet » : cela "
     "ferme ces portes, et on ne les rouvre pas après coup."),
    ("Vérifier sous quelle forme le titre du vendeur existe",
     "La bonne question n'est pas « le vendeur a-t-il un contrat ? » — il en aura un. C'est : "
     "l'acte est-il INSCRIT au service de la publicité foncière, ou bien s'agit-il d'une chaîne de "
     "contrats successifs jamais enregistrée ? On demande le numéro d'inscription et on le fait "
     "vérifier. On remonte aussi la chaîne des propriétaires précédents, et on vérifie l'absence "
     "d'indivision non réglée — une succession partagée entre héritiers dont un seul signe est le "
     "litige le plus courant du marché."),
    ("Faire rédiger le contrat en arabe, et savoir ce qui fait foi",
     "C'est la version arabe qui est lue par un tribunal égyptien. Une traduction française ou "
     "anglaise sert à comprendre, pas à se défendre. Le contrat décrit le bien, le prix, "
     "l'échéancier, la date de livraison dans le neuf, les pénalités de retard de part et d'autre, "
     "et l'engagement précis du vendeur quant à l'enregistrement : qui fait la démarche, à quel "
     "moment, et à la charge de qui."),
    ("Dans le neuf : savoir qui l'on finance, et sur quelle durée",
     "Le neuf égyptien se vend très majoritairement sur plan, avec un acompte modeste et un "
     "échéancier étalé sur plusieurs années. Ce n'est pas un crédit bancaire : c'est le promoteur "
     "qui est financé, et le risque porté est celui de sa livraison. On regarde donc ses "
     "réalisations effectivement livrées, ses autorisations de construire, et surtout ce que le "
     "contrat prévoit si la livraison prend deux ans de retard."),
    ("Enregistrer l'acte — et savoir quoi faire quand ça bloque",
     "L'inscription au service de la publicité foncière est ce qui transfère la propriété de façon "
     "opposable. Elle suppose que la chaîne amont soit elle-même en règle, ce qui n'est pas toujours "
     "le cas et bloque le dossier. Le recours usuel est l'action en validité et opposabilité, qui "
     "fait constater la vente par un juge. Il faut savoir ce qu'elle est et ce qu'elle n'est pas : "
     "elle sécurise nettement la position de l'acheteur, elle ne remplace pas l'inscription."),
    ("Ouvrir la situation fiscale du bien et raccorder les compteurs",
     "Déclaration du bien auprès de l'administration fiscale au titre de la taxe foncière, "
     "raccordement de l'électricité, de l'eau et du gaz au nom de l'acquéreur, et pour les "
     "résidences fermées et stations intégrées, le règlement de copropriété et les charges "
     "annuelles. Ces charges se chiffrent avant l'achat, pas après."),
    ("Préparer la revente et la sortie des fonds dès maintenant",
     "Le dossier constitué à l'achat — attestation de transfert bancaire, acte inscrit ou jugement, "
     "quittances d'impôts — est ce qui rendra la revente et le rapatriement possibles des années "
     "plus tard. Il se conserve, en original. Un acheteur qui néglige ce point le paie au moment de "
     "vendre, quand il n'est plus possible de le reconstituer."),
]

# LES MONTANTS SONT VIDES. Voir l'en-tête du fichier.
# Deux natures d'absence, comme sur la page Chine :
#   « à vérifier » = la valeur existe, publiée par l'autorité nommée en face,
#                    et personne ne l'a encore vérifiée à une date précise.
#   « non fixé »   = la valeur N'EXISTE PAS. Ici ce ne sont pas des chiffres
#                    qu'on n'a pas trouvés : ce sont deux postes que la
#                    réglementation ne fixe pas du tout, et qui se jouent
#                    entièrement dans le contrat. Les marquer « à vérifier »
#                    enverrait quelqu'un chercher un barème inexistant au lieu
#                    de relire sa clause.
BAREME = [
    ("Frais d'inscription de l'acte au registre", "verif",
     "montant ou plafond dû pour l'inscription qui rend la propriété opposable",
     "Service de la publicité foncière — ministère de la Justice"),
    ("Taxe sur la cession de biens immobiliers", "verif",
     "taux, assiette et partie qui en est redevable",
     "Autorité fiscale égyptienne"),
    ("Taxe foncière annuelle sur le bâti", "verif",
     "taux, base de calcul et seuil d'exonération",
     "Autorité fiscale égyptienne — loi sur la taxe foncière"),
    ("Nombre maximal de biens détenus par un étranger", "verif",
     "nombre de biens autorisé par personne, et l'usage auquel ils doivent être destinés",
     "Loi relative à l'acquisition de biens immobiliers par des non-Égyptiens"),
    ("Superficie maximale par bien", "verif",
     "surface plafond, par bien acquis",
     "Loi relative à l'acquisition de biens immobiliers par des non-Égyptiens"),
    ("Délai avant revente libre", "verif",
     "durée pendant laquelle la revente est restreinte après l'acquisition, et les dispenses",
     "Loi relative à l'acquisition de biens immobiliers par des non-Égyptiens"),
    ("Montant d'acquisition ouvrant droit à un titre de séjour", "verif",
     "montant, durée du titre délivré, et obligation de transfert des fonds depuis l'étranger",
     "Ministère de l'Intérieur — administration des étrangers"),
    ("Montant ouvrant droit à la nationalité par investissement", "verif",
     "montant, forme de l'investissement et délai avant décision",
     "Loi sur la nationalité et son règlement d'application"),
    ("Commission de l'agent immobilier", "nonfixe",
     "aucune autorité ne publie de barème : le taux se négocie et figure au contrat. "
     "Chercher un pourcentage officiel, c'est chercher quelque chose qui n'existe pas",
     "Aucune — usage de marché, librement négocié"),
    ("Revalorisation des échéances dans le neuf", "nonfixe",
     "aucun texte n'encadre la révision d'un échéancier de promoteur en cours de paiement. "
     "Ce qui s'applique est la clause du contrat, et elle seule — c'est donc elle qu'il faut "
     "lire avant de signer, pas un barème",
     "Aucune — matière purement contractuelle"),
]

FAQ = [
    ("Un étranger peut-il acheter un bien en Égypte ?",
     "<p>Oui sur la plus grande partie du pays, et il en devient pleinement propriétaire. La loi "
     "pose toutefois des limites : un nombre maximal de biens par personne, une surface plafond par "
     "bien, une destination d'habitation, et un délai pendant lequel la revente est restreinte. Ces "
     "valeurs figurent au tableau des frais, sans chiffre, avec l'autorité qui les publie.</p>"
     "<p>Deux réserves qui ne sont pas des détails : le Sinaï relève d'un régime distinct, et "
     "certaines zones frontalières ou stratégiques sont soumises à autorisation. La question se "
     "vérifie pour la parcelle précise.</p>"),

    ("Pourquoi Charm el-Cheikh est-il traité à part ?",
     "<p>Parce que la règle égyptienne n'est pas la même partout, contrairement aux autres marchés "
     "présentés sur ce site. <b>Le Sinaï n'ouvre pas la pleine propriété à un acheteur étranger.</b> "
     "L'accès se fait par un droit d'usage à durée déterminée, avec une procédure d'autorisation "
     "propre.</p>"
     "<p>Cela concerne Charm el-Cheikh et Dahab, c'est-à-dire précisément deux des destinations que "
     "cherche en premier un acheteur étranger. Hurghada et El Gouna, sur la côte ouest de la mer "
     "Rouge, ne sont pas dans le Sinaï : la pleine propriété y est accessible. C'est pour ça que le "
     "régime est écrit sur chaque ville de la grille plutôt que renvoyé à une note.</p>"),

    ("Le vendeur me dit que son contrat suffit. Est-ce vrai ?",
     "<p>Non, et c'est le point le plus important de cette page.</p>"
     "<p>Un contrat de vente non enregistré vous donne une créance <b>contre le vendeur</b>. "
     "L'inscription au service de la publicité foncière vous donne un droit <b>opposable à tous</b>. "
     "Ce n'est pas une nuance de vocabulaire : si le même bien est vendu deux fois, si un créancier "
     "du vendeur se manifeste, ou si des héritiers apparaissent, seul l'acte inscrit vous protège.</p>"
     "<p>Une part importante des biens en circulation en Égypte n'est pas enregistrée. Ce n'est donc "
     "pas une anomalie qui signale un vendeur douteux — c'est la situation ordinaire, et elle se "
     "traite. Ce qui n'est pas acceptable, c'est de ne pas savoir dans quelle situation on est.</p>"),

    ("Qu'est-ce qu'un jugement de validité et opposabilité ?",
     "<p>C'est l'action par laquelle un juge constate que la vente a bien eu lieu et qu'elle est "
     "valable. C'est le recours usuel quand l'inscription est bloquée parce que la chaîne des "
     "propriétaires précédents n'est pas en règle.</p>"
     "<p>Elle renforce nettement la position de l'acheteur. <b>Elle ne remplace pas l'inscription "
     "au registre.</b> Nous l'écrivons parce que les deux sont souvent présentés comme équivalents "
     "dans les annonces, et un acheteur qui croit tenir un titre alors qu'il tient un jugement se "
     "trompe sur ce qu'il possède.</p>"),

    ("L'achat ouvre-t-il un droit de séjour ou la nationalité ?",
     "<p>Oui, des voies existent — et c'est une différence nette avec la page Chine de ce site, où "
     "la réponse est non à tout montant. Nous le disons explicitement parce que les deux pages se "
     "suivent dans le menu et qu'un lecteur transpose sans y penser.</p>"
     "<p>Deux conditions comptent autant que le montant. D'abord, les fonds doivent être transférés "
     "<b>depuis l'étranger, en devises</b>, par le canal bancaire, avec l'attestation qui le prouve. "
     "Ensuite, ces voies relèvent de textes qui ont déjà été modifiés et dont les seuils sont "
     "révisés. Les montants ne sont donc pas écrits ici tant qu'ils n'ont pas été vérifiés à une "
     "date précise — un seuil périmé sur ce sujet ferait prendre une décision à plusieurs centaines "
     "de milliers de dollars.</p>"),

    ("Puis-je payer en espèces, ou par un compte hors d'Égypte ?",
     "<p>Techniquement, des paiements se font ainsi. Mais l'attestation de transfert bancaire en "
     "devises est le document qui conditionne les voies de séjour et de nationalité, et qui "
     "justifiera l'origine des fonds au moment de revendre et de rapatrier.</p>"
     "<p>Un achat payé hors du circuit bancaire n'est pas seulement moins bien documenté : il ferme "
     "ces possibilités, et elles ne se rouvrent pas rétroactivement. C'est une décision à prendre "
     "avant le premier versement, pas après.</p>"),

    ("Les échéanciers sur sept ou huit ans, est-ce normal ?",
     "<p>Oui, c'est le mode de vente dominant dans le neuf : acompte réduit, solde étalé sur "
     "plusieurs années, souvent au-delà de la livraison. Il faut comprendre ce que cela change.</p>"
     "<p>Vous ne remboursez pas une banque, <b>vous financez le promoteur</b>. Le risque n'est donc "
     "pas un taux d'intérêt, c'est la livraison. On regarde ses programmes réellement livrés, ses "
     "autorisations, et ce que le contrat prévoit en cas de retard — de son côté comme du vôtre. On "
     "lit aussi la clause de révision des échéances : aucun texte ne l'encadre, elle seule fait "
     "loi.</p>"),

    ("Puis-je louer mon bien, y compris en courte durée ?",
     "<p>La location est possible, mais trois choses se vérifient avant d'acheter dans cette "
     "intention : les règles applicables à la location saisonnière dans la localité visée, le "
     "règlement de la résidence ou de la station — beaucoup de programmes intégrés imposent leur "
     "propre gestion locative — et le traitement fiscal des revenus perçus par un non-résident.</p>"
     "<p>Nous ne répondons pas oui ou non à la place de l'administration compétente : cela se "
     "demande pour le programme précis, par écrit, avant de signer.</p>"),

    ("Dans quelle langue le contrat fait-il foi ?",
     "<p>En arabe. Une traduction française ou anglaise sert à comprendre ; ce n'est pas elle qui "
     "sera lue en cas de litige. Toute clause qui compte — prix, échéancier, livraison, pénalités, "
     "engagement d'enregistrement — se vérifie sur la version arabe, par quelqu'un qui la lit.</p>"),
]
