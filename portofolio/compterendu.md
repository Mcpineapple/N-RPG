# Compte-rendu général du projet
Ce fichier a pour but de dresser un compte-rendu général du projet.
Il contient :
- Une introduction traitant des inspirations, buts, visions et défis du projet
- Une description succinte du contenu du jeu
- Une description du fonctionnement du jeu et des modules utilisés
- Un résumé des choix techniques et d'organisations faits
- Un compte-rendu des difficultés rencontrées
- Une conclusion sur ces éléments et le projet en général

## Introduction au projet
Ce mini-projet 3 a pour but de créer un jeu "Histoire dont vous êtes le héros".
Il a été réalisé avec grand enthousiasme dans le but de créer un jeu narratif
classique. La visée de ce projet était de réaliser, en respectant une
organisation la plus "professionelle" possible, et en suivant des modèles
d'organisation efficaces.
La consigne nous a semblé réminiscente des premiers Role-Playing Games textuels,
ou plus actuellement des Visual Novels populaires chez les producteurs
indépendants et amateurs japonais.
Un autre objectif était de ne pas télescoper les éléments de la production : le
moteur ne doit pas entrer en collision avec la partie de plus bas niveau, et
l'écriture ne doit pas entrer en collision avec la programmation. Il nous a donc
semblé avisé de rechercher un système simple, intuitif et pratique pour
l'écriture du "script" de l'histoire.
La réponse à cet objectif est la création et la spécification du Visual Novel
MarkDown (VNMD), utilisé pour écrire ce projet. Il permet de se reposer sur les
acquis de la méthode d'écriture en texte brut MarkDown, tout en s'adaptant à
l'écriture d'un tel jeu.
Enfin, nous avons souhaité donner un vrai sens aux choix donnés au joueur, en
permettant l'accès à de diverses fins qui s'entre-tissent. Nous avons donc
choisi de présenter un jeu à l'ambiance sombre et inquiétante, qui permet de
découvrir plus et d'accumuler des indices à chaque nouvelle partie.

## Contenu du jeu
Le jeu est une courte histoire d'un policier explorant un étrange laboratoire,
essayant de trouver la réponse aux mystères qui l'habitent. Il emmène à travers
différents tableaux, et propose des choix au joueur pour évoluer vers les
diverses fins du jeu et continuer l'histoire.

## Fonctionnement de jeu
Le jeu se compose de différents éléments :
- Le script et les médias :
	Le script (ou les différents fichiers composant le script), qui seront lus par
	le parser, composent la structure et le contenu du script, facilement
	compréhensibles par tout écrivain.
	De plus, on retrouve dans le dossier "media" l'ensemble des fichiers de
	contenu : musique, effets sonores, images et personnages. Ceux-ci sont
	référencés par le script et lus par le moteur.
- Le parser :
	Ce programme est destiné à lire un script en Visual Novel MarkDown, et à le
	traduire en appels simples en JSON pour le moteur. Ceux-ci sont les briques de
	base de ce que doit faire le jeu. Il prend ainsi en charge tous les
	déplacement, aliases, et autres éléments du script en interne pour servir un
	résultat facilement lisible pour le moteur.
- L'arbre binaire :
	Cette structure de données est spécialement équipée pour accueillir
	l'intégralité du script. En cas de choix, les arêtes de l'arbre sont
	étiquetées avec le texte des choix possibles. Il suit autrement un prograssion
	linéaire tant que l'histoire ne diverge. Il dispose d'une méthode spéciale
	utilisant le parser pour stocker toute l'information de l'histoire, afin
	d'être lu facilement pedant les tests ou par le moteur.
- Le moteur :
	Le moteur représente le jeu en lui-même : il s'agit de l'interface graphique
	entre l'utilisateur et les informations, qui prend en charge l'affichage du
	texte, l'affichage d'images ou de sons, et les choix envoyés par l'utilisateur
	en appuyant sur les boutons de choix. Il permet ainsi de représenter le jeu à
	partir de l'information contenue dans le script.

Le parser, l'arbre et le moteur sont importés comme des modules python. Pour
fonctionner, ce projet importe aussi des bibliothèques python classiques : 
- os et sys :
	Dans le cas de gestion de fichiers,de la route vers ces même fichiers, ou
	d'une sortie
- json :
	Pour prendre en charge l'encodage/décodage du contenu en json entre le parser,
	l'arbre et le moteur
- tkinter :
	Le moteur graphique utilisé par le moteur de jeu : il permet de créer des
	widgets visuels et est intégré dans la bibliothèque standard de python

## Choix techniques et d'organisation
Afin de promouvoir une bonne organisation, nous avons décidé d'héberger le code
source de notre projet via le logiciel libre de gestion de versions Git, par
Linus Torvalds, et en l'hébergeant sur la plateforme renommée GitHub. Nous avons
autrement utilisé Discord pour organiser notre discussion sur le projet et
rester en contact.
