# Feuille récapitulative (cheatsheet) des symboles de VNMD
Cette feuille récapitule les différents symboles utilisés comme spéciaux par le
Visual Novel MarkDown, comme indiqués dans le prototype.

Effet|Doit prendre un espace avant le texte|Symbole
-----|-------------------------------------|-------

## Caractères d'échappement

Échappe le caractère suivant | X | \
Permet d'annuler l'effet d'un caractère spécial en se plaçant juste avant. Ce
caractère sera ainsi affiché sous la forme de texte normal. \ est lui-même un
caractère spécial, il doit donc être écrit "\\" dans le texte.

## Caractères modifiant leur ligne
Ces caractères modifient entièrement leur ligne : du texte normal ne peut pas
être inséré après eux.

Identifie l'endroit et ouvre les paramètres | O | $
Permet de donner un identificateur (un nom auquel se déplacer) à l'endroit où il
se place, peu importe où. Le nom de l'identificateur est collé au symbole.
À la suite d'un espace, des paramètres peuvent être envoyés, modifiant la scène,
sous la forme "paramètre=valeur" et séparés par des espaces

Ouvre un choix | O | -
Permet de placer à sa suite un choix qui emmene vers un certain paragraphe (voir
résolution). Le choix dure jusqu'au prochain choix, résolution, ou paragraphe.
Il peut être directement suivi d'un nom (jusqu'à un espace), qui peut être
interprété par le moteur pour personnaliser le choix.

Indique vers où mène un choix | O | =
Se place à la suite d'un choix pour indiquer où ce choix mène dans le texte.
N'admet pas de texte après un lui (il sera ignoré), seulement un identifiant qui
y est collé, et indique vers où ammène le choix. Par défaut (pas de nom), la
destination est le prochain paragraphe. Il peut dans ce cas même être omis (un
nouveau choix ou un double retour à la ligne finit le choix actuel, qui prend
alors comme destination le prochain paragraphe).

Indique un titre | O | #
Ce symbole indique un titre ou une subdivision du texte. Il peut être montré par
le moteur ou non. Il peut y avoir plusieurs # : plus ce nombre est grand, plus
la subdivision est petite.

Crée un alias | O | <
Ce symbole indique que le mot situé après lui en paramètre correspondra
lorsqu'il est remplacé (voir {}). Après l'espace se place le texte qui le
remplacera, qui peut être placé sur toute la ligne.

Ouvre un commentaire | X | /
Ce symbole perme, en début de lige, d'ouvrir une ligne de commentaires : toute
la ligne sera ignorée par le jeu, et ne sert qu'à l'utilisation de l'écrivain
et de ses collègues.

Étend la ligne précédente | X |   (espace)
En début de ligne, ce symbole permet d'indiquer que cette ligne est une
continuation de la précédente, permettant d'écrire proprement le script sans
affecter le résultat.

## Caractères à l'intérieur d'une ligne
Ces caractères spéciaux sont des symboles placés à même le texte. Un grand
nombre d'entre eux dépendent du moteur de jeu.

Lien vers un autre fichier | X | []
Ces symboles ne peuvent s'utiliser qu'à la suite d'une ligne avec =. Si vous
souhaitez séparer votre script entre plusieurs fichiers, vous pouvez mettre
dedans le nom d'un autre ficher, et le script continuera vers ce dernier.

Remplace un alias par son contenu | X | {}
Tout mot entre ces symboles sera interprété comme ce que le remplacement de
l'alias précise.

Marque une pause | X | >
Bien que ce symbole dépende de l'implémentation, il est conseillé d'ajouter ce
symbole à toutes les implémentations. Il permet de marquer une pause au milieu
de la ligne, et d'écrire ce qu'il y a après seulement après un clic.

D'autres symboles, issus du MarkDown classique, comprennent:
_x_
*x*
__x__
==x==
Tous ces symboles peuvent modifier l'interprétation ou le formatage du texte,
mais dépendent de l'implémentation.
