# Spécification de l'API du parser de VNMD

Ce document décrit l'API nécessaire au bon fonctionnement d'un moteur de jeu
avec le parser de Visual Novel Markdown, afin de proposer une norme commune
rendant indépendants moteur et parser.
Cette spécification décrira d'abord le fonctionnement de la communication entre
les deux modules, puis les fonctions communes que doivent posséder les moteurs
ainsi que leur description.

## Mode de communication

Dans le modèle de cet API, deux processus de longue durée sont lancés
parallèlement : l'interface de jeu (le moteur de jeu) et la lecture du script
(parser). Ces deux processus intéragissent sur un modèle inspiré du modèle
client-serveur : le moteur de jeu (client) envoie l'une des requêtes possibles
au parser (serveur), qui lui répond avec un message formaté selon une API
standardisée ici.
Le parser est ainsi seul élément conscient et maître du script, reçoit des
demandes d'avancer ou de faire un choix, et transmet via un paquet contenant la
commande à effectuer et le contenu de celle-ci les informations qu'attend le
moteur de jeu.


## Structure technique de la communication



## Côté client

Le client (moteur de jeu) peut envoyer trois appels différents au serveur :
continuer, choisir et sauvegarder. Il enverra la plupart du temps des appels
jusqu'à ce qu'un nouveau texte apparaisse.
Le premier permet de passer à la suite du jeu (et donc du script) en lisant la
ligne suivante pour recevoir les prochaines informations à traiter, et possède un
ajout possible : la précision d'un endroit dans le script où reprendre.
Le second permet d'acquérir la position actuelle dans le script afin de la
sauvegarder ou de conserver un historique des lignes lues précédemment, par exemple.
Le troisième appel est un appel spécialement réservé à la sélection d'un choix.
Il permet d'informer le parser du choix qui a été fait afin de continuer dans
l'histoire.

## Côté serveur

Le serveur peut renvoyer un grand nombre d'informations différentes au moteur de
jeu, représentant toutes les possibilités offertes au premier coup d'oeil par la
spécification du Visual Novel MarkDown. Néanmoins, de nombreuses options,
nottament les paramètres, seront pris en charge spécialement par le moteur de
jeu, et les informations envoyées au moteur de jeu seront de toute façon
interprétées comme ce dernier le souhaite.
Les identifiants qui peuvent être envoyés au moteur sont :
- texte
- choix
- parametres
- titre
- fin

L'identifiant texte permet d'envoyer un texte qui doit être affiché : il peut
recevoir un argument supplémentaire, permettant d'ajouter le texte au texte déjà
affiché plutôt que de remplacer le texte de la zone de texte.
L'identifiant choix permet de proposer les différents choix possibles,
éventuellement avec des paramètres. Cela permet au moteur d'afficher les choix
d'une façon bien distincte.
L'identifiant parametres est l'un des plus importants pour tous les aspects
avancés d'un moteur de jeu : il permet d'envoyer les paramètres après un "$",
que ce soit pour des éléments graphiques, de personnages, etc... Ceux-ci seront
interprétés par le client.
L'identifiant titre correspond aux tires à afficher spécialement à
l'écran. Ceux-ci se comportant assez différemment des textes et des paramètres,
ils sont envoyés séparéments.
L'identifiant fin, dernièrement, permet de caractériser l'une des fins du
programme et doit amener à un arrêt.

## Recommendations pour le nom des paramètres

Afin de permettre la meilleure portabilité possible entre les moteurs, la plus
grande lisibilité et proposer des fonctions de bases, cette liste de
recommandations est proposée pour nommer les paramètres trouvés après "$" dans
les scripts.

Nom(s) | Effets
-------|-------
char/character | Change le personnage
bg/background | Change l'image de fond d'écran
music/track | Change de piste musicale
effect/vfx | Applique un effet visuel
sound/sfx | Joue un effet sonore

## Récapitulatif des appels de l'API
### Côté client
Nom | Effets
----|-------
continuer | Passe à la ligne suivante du script, la prochaine modification à faire
sauvegarder | Obtient la position actuelle dans le script
choisir | Permet de préciser quel choix a été effectué

### Côté serveur
Nom de l'identifiant | Contenu | Effets
---------------------|---------|-------
texte | texte et "ajoute" | Permet d'afficher du texte, en nettoyant la zone de texte ou non
choix | liste des choix et leurs paramètres | Permet d'afficher différents choix
parametres | liste de parametres | Envoie diverses informations, nottament média ou personnages
titre | paramètre, texte et taille du titre | Permet d'afficher un titre
fin | paramètre et texte | Affiche une fin
