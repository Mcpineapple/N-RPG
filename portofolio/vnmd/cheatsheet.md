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
