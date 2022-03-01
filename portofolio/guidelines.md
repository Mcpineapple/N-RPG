# Conventions de développement
Ce projet s'efforce de suivre des bonnes pratiques, que ce soit de
programmation, d'écriture ou d'organisation. Quelques-unes d'entre elles sont
consignées ici.

## Conventions d'écriture
Ce projet s'efforce de suivre les règles conventionelles en python de nom des
variables et de formatage, formalisées par la PEP 8.
Il décide néanmoins de suivre une programmation en
français (noms de variables français, par exemple). Ainsi, les modifications
suivies sont :
- Toutes les docstrings sont précédées d'un u, permettant de préciser qu'elles
  sont en unicode, évitant tout problème de représentation des caractères
  spéciaux français.
- Les méthodes correspondant à un attribut d'objet, "Getters" et "Setters", sont
  nommées avec le préfixe "obtenir" et "changer" respectivement, bien que la
  méthode préférée soit les décorateurs de fonctions.

## Conventions de programmation
Les intéractions avec les attributs d'un objet se font par des méthodes
permettant son obtention et modification. Celles-ci sont définies de préférence
à l'aide la fonction property, via des décorateurs de fonctions, les fonctions
décorées portant le nom de l'attribut concerné.

## Conventions de documentation
Toute la documentation "externe" aux programmes se fait dans le dossier
principal "portofolio", le plus souvent sous le format MarkDown, permettant une
bonne lisibilité.
La documentation interne au programme s'organise de la façon suivante :
- Chaque classe ou fonction possède une documentation sous la forme de doctring.
  Celle-ci s'organise de la façon suivante :
  """
  	{Description}
	Préconditions :
		{Préconditions}
		Paramètres (éventuellement):
			{Description des paramètres envoyés à la fonction}
	Postconditions :
		{Postconditions}
		Sortie {éventuellement} :
			{Description des objets renvoyés par la fonction}
  """
  Elle suit autrement les conventions généralement admises en python,
  formalisées par la PEP 256.

## Conventions d'organisation
La documentation, le script exécuté et les modules de fonctionnement sont
séparés. Les modules se trouvent sous le dossier de module général "nrpg",
contenant les différents dossiers et fichiers de même nom correspondant aux
modules. Ceux-ci sont ainsi importables tous ensemble, ou module par module ou
commande par commande. Sont ainsi séparés :
- Le parser;
- Le moteur de jeu;
- L'arbre binaire nécessaire au fonctionnement du jeu
La structure des modules suit une approche rapide de la documentation officielle
python afin d'être utilisable facilement avec pip, sans néanmoins formaliser
complètement une structure standard pour être exportée.
