# -*- coding: utf-8 -*-
"""
Amarimmo — Turquie. Contenu de la troisième page de marché.

CE QUI EST ÉCRIT ICI, ET CE QUI EST LAISSÉ VIDE.

Ce fichier décrit un MÉCANISME d'achat, pas un barème. La différence n'est
pas de la prudence de façade :

  - un mécanisme est stable. Le titre de propriété turc s'appelle le tapu,
    il se transfère devant la direction du cadastre, un rapport d'expertise
    est exigé pour une vente à un étranger, l'assurance séisme obligatoire
    conditionne les raccordements. Ces phrases seront encore vraies dans
    trois ans.

  - un SEUIL bouge. Le montant qui ouvre la citoyenneté par investissement
    a changé en 2022. Celui qui ouvre un permis de séjour a changé ensuite.
    Des quartiers entiers sont fermés à l'enregistrement de nouveaux
    résidents étrangers, et la liste évolue.

Écrire un seuil aujourd'hui, c'est mettre sur un site qui vend à des
investisseurs étrangers un chiffre qui sera faux un jour sans que personne
ne s'en aperçoive — et ce chiffre-là, un acheteur l'utilise pour décider
d'engager plusieurs centaines de milliers de dollars.

Donc : les montants restent VISIBLEMENT VIDES, avec le nom de l'autorité
qui les publie à côté, et un champ « vérifié le » qui reste vide tant que
personne n'a vérifié. Une case vide se remarque ; un chiffre périmé, non.

RÈGLE REPRISE DU CAHIER DES CHARGES DU CLIENT (section 4, mot pour mot) :
« The website must not imply that purchasing any property automatically
grants a visa, residence permit or citizenship. » Elle a son propre bloc
sur la page, en haut, et pas en petits caractères en bas.
"""

# Les douze villes viennent de la section 6 du document du client, dans son
# ordre. Je n'en ajoute ni n'en retire aucune.
#
# Note honnête portée sur la page : Bodrum, Fethiye et Alanya ne sont pas
# des villes-provinces mais des districts côtiers. Le client les a listées
# comme destinations, ce sont des marchés en soi, je les garde — mais je le
# dis, parce qu'un investisseur qui cherche « la ville de Bodrum » dans un
# registre ne la trouvera pas sous ce nom.

VILLES = [
    ("Istanbul", "Marmara",
     "La plus grande ville du pays, à cheval sur le Bosphore et donc sur deux continents. "
     "Marché le plus profond et le plus segmenté : rive européenne et rive asiatique n'obéissent "
     "pas aux mêmes logiques."),
    ("Ankara", "Anatolie centrale",
     "La capitale. Marché administratif et universitaire, moins exposé au tourisme, donc moins "
     "saisonnier."),
    ("Antalya", "Méditerranée",
     "Côte méditerranéenne, première destination touristique du pays. Forte présence d'acheteurs "
     "étrangers, ce qui rend certains quartiers sensibles aux restrictions d'enregistrement."),
    ("Izmir", "Égée",
     "Troisième ville du pays, sur la mer Égée. Port, industrie et front de mer urbain."),
    ("Bodrum", "Égée — district",
     "Péninsule de la mer Égée. Marché fortement saisonnier : la demande locative se concentre "
     "sur quelques mois."),
    ("Bursa", "Marmara",
     "Au sud d'Istanbul, adossée au massif de l'Uludağ. Ville industrielle et résidentielle, "
     "reliée à Istanbul."),
    ("Mersin", "Méditerranée",
     "Port méditerranéen à l'est d'Antalya. Marché plus local, moins tourné vers l'acheteur "
     "international."),
    ("Trabzon", "Mer Noire",
     "Côte de la mer Noire, climat et paysage très différents du sud. Saison touristique "
     "décalée par rapport à la Méditerranée."),
    ("Fethiye", "Égée — district",
     "District côtier entre Égée et Méditerranée. Comme Bodrum, marché saisonnier et très "
     "orienté vue mer."),
    ("Alanya", "Méditerranée — district",
     "District côtier de la province d'Antalya. L'un des marchés les plus fréquentés par les "
     "acheteurs étrangers du pays."),
    ("Gaziantep", "Anatolie du Sud-Est",
     "Grand pôle industriel et agroalimentaire du sud-est. Marché intérieur, non touristique."),
    ("Konya", "Anatolie centrale",
     "Ville de l'Anatolie centrale, industrielle et agricole. Marché local, peu exposé à la "
     "demande étrangère."),
]

# Chaque étape est un mécanisme, pas un délai chiffré. Les délais dépendent
# du dossier et de la direction du cadastre concernée.
ETAPES = [
    ("Numéro fiscal et compte bancaire",
     "Un numéro fiscal turc (vergi numarası) s'obtient auprès de l'administration fiscale et "
     "conditionne tout le reste : compte bancaire, paiement, raccordements. Le compte bancaire "
     "turc est nécessaire en pratique pour les transferts et pour la suite."),
    ("Vérification du titre au cadastre",
     "Le titre de propriété turc s'appelle le tapu. Avant toute réservation, on vérifie au "
     "registre foncier qui est réellement propriétaire, quelles hypothèques (ipotek) et quelles "
     "servitudes sont inscrites, et si le bien est grevé d'une saisie. C'est la même vérification "
     "qu'en Espagne avec la nota simple, et elle évite les mêmes histoires."),
    ("Zones interdites aux étrangers",
     "L'acquisition par un étranger est interdite dans les zones militaires et de sécurité. "
     "Cette vérification se fait auprès des autorités compétentes AVANT la réservation : elle ne "
     "se rattrape pas après, et c'est un refus sec, pas une formalité négociable."),
    ("Rapport d'expertise obligatoire",
     "Une vente à un acheteur étranger exige un rapport d'évaluation établi par un expert agréé. "
     "Ce rapport fixe une valeur de référence — et c'est aussi une protection pour l'acheteur, "
     "puisqu'il rend visible un prix manifestement hors marché."),
    ("Assurance séisme obligatoire (DASK)",
     "La Turquie impose une assurance séisme obligatoire sur les logements. Elle conditionne en "
     "pratique les raccordements et les démarches qui suivent. Ce n'est pas une option "
     "commerciale que l'on décline."),
    ("Transfert du tapu devant la direction du cadastre",
     "Le transfert de propriété se fait à la direction du cadastre (Tapu Müdürlüğü), en présence "
     "des deux parties ou de leurs mandataires. Si l'acheteur ne parle pas turc, la présence d'un "
     "interprète assermenté est requise — à prévoir, ce n'est pas une politesse."),
    ("Permis d'habiter pour le neuf",
     "Pour un logement neuf, le permis d'habiter (iskân) atteste que la construction est conforme "
     "au permis de construire. Sans lui, les raccordements définitifs et la revente se compliquent."),
    ("Après l'acquisition",
     "Taxe foncière annuelle, charges de copropriété, abonnements. Ces montants s'établissent "
     "commune par commune : ils sont chiffrés avant l'achat, pas découverts après."),
]

# LES MONTANTS SONT VIDES. Voir l'en-tête du fichier.
# Chaque ligne nomme l'autorité qui publie la valeur, pour que la
# vérification soit possible sans avoir à chercher où regarder.
BAREME = [
    ("Frais de transfert du titre (tapu harcı)",
     "pourcentage de la valeur déclarée",
     "Direction générale du cadastre et de l'enregistrement foncier"),
    ("TVA à l'achat",
     "taux selon le type et la surface du bien",
     "Administration fiscale turque"),
    ("Plafond de surface par acheteur étranger",
     "surface maximale détenue au niveau national",
     "Loi sur le cadastre"),
    ("Part maximale d'un district détenue par des étrangers",
     "pourcentage de la surface du district",
     "Loi sur le cadastre"),
    ("Seuil d'investissement — permis de séjour",
     "montant minimal de la valeur du bien",
     "Direction générale de la gestion des migrations"),
    ("Seuil d'investissement — citoyenneté",
     "montant minimal, avec engagement de non-revente",
     "Direction générale du cadastre et de l'enregistrement foncier"),
]

FAQ = [
    ("Un étranger peut-il acheter un bien en Turquie ?",
     "<p>Oui, dans le principe, et la Turquie est l'un des marchés les plus ouverts de la région "
     "aux acheteurs étrangers. Trois limites existent : les zones militaires et de sécurité sont "
     "interdites, une surface maximale est détenue par personne au niveau national, et une part "
     "maximale de la surface de chaque district peut être détenue par des étrangers. Certaines "
     "nationalités font en outre l'objet de restrictions particulières.</p>"
     "<p>Ces limites se vérifient avant la réservation, pas après.</p>"),

    ("L'achat d'un bien donne-t-il droit à un titre de séjour ou à la citoyenneté ?",
     "<p><b>Non, pas automatiquement.</b> Ce sont trois procédures juridiques distinctes : acheter "
     "un bien, obtenir un titre de séjour, obtenir la citoyenneté. Des seuils d'investissement et "
     "des conditions supplémentaires s'appliquent à chacune des deux dernières, ils ont changé "
     "récemment, et des quartiers entiers sont fermés à l'enregistrement de nouveaux résidents "
     "étrangers.</p>"
     "<p>Nous ne publions pas de montant sur cette page tant qu'il n'a pas été vérifié à une date "
     "précise auprès de l'autorité qui le fixe. Un seuil périmé sur un site immobilier, c'est une "
     "décision d'investissement prise sur un chiffre faux.</p>"),

    ("Qu'est-ce que le tapu exactement ?",
     "<p>C'est le titre de propriété turc, délivré et tenu par l'administration du cadastre. Le "
     "transfert se fait devant elle. Tant que le tapu n'est pas établi à votre nom, vous n'êtes "
     "pas propriétaire — quels que soient les documents signés par ailleurs et quelles que soient "
     "les clés remises.</p>"),

    ("Pourquoi un rapport d'expertise est-il exigé ?",
     "<p>Parce que la loi l'impose pour les ventes à des acheteurs étrangers. Il établit une "
     "valeur de référence par un expert agréé. C'est une contrainte administrative, et c'est aussi "
     "la meilleure protection gratuite dont dispose un acheteur qui ne connaît pas le marché "
     "local : un prix très au-dessus de l'expertise se voit.</p>"),

    ("Faut-il être présent en Turquie pour signer ?",
     "<p>Non, la signature peut se faire par un mandataire muni d'une procuration établie en bonne "
     "et due forme. En revanche, si l'acheteur signe lui-même sans parler turc, la présence d'un "
     "interprète assermenté est requise au cadastre.</p>"),

    ("Le paiement se fait dans quelle monnaie ?",
     "<p>La réglementation encadre les paiements en devises et impose des formalités bancaires "
     "spécifiques lorsque des fonds étrangers entrent dans l'opération. Le montage du paiement se "
     "prépare avec la banque avant la signature — c'est le point qui retarde le plus souvent une "
     "acquisition, devant les questions juridiques.</p>"),

    ("Que se passe-t-il si le bien est en zone militaire ?",
     "<p>La vente ne peut pas avoir lieu. La vérification se fait en amont auprès des autorités "
     "compétentes. Un vendeur qui presse pour réserver avant cette vérification donne une "
     "information sur lui-même.</p>"),

    ("Quels frais annuels une fois propriétaire ?",
     "<p>La taxe foncière annuelle, les charges de copropriété, l'assurance séisme obligatoire et "
     "les abonnements. Les montants dépendent de la commune et du bien ; ils sont chiffrés avant "
     "l'acquisition.</p>"),
]
