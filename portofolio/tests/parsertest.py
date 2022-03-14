import accesmodule

"""
Importe le parser, et imprime les appels renvoyes a la lecture du protitype du
VNMD. Imprime aussi la position dans le script a la suite de l'appel, et le
numéro de la lecture (à peu près le numéro de ligne).
"""
import os
import sys

from nrpg.parser import Parser

position_script = os.path.join(os.path.dirname(__file__), '..', 'vnmd',
        'prototype.vnmd')
parser = Parser(position_script)

compteur = 0
a = ""
while a != "fin":
    a = parser.suivant()
    if a is not None :
        print(a)
    # print(parser.sauvegarde())
    # Alourdit l'affichage, à activer en cas de problème
    compteur += 1
    print(compteur)

"""
Ce test a permis de régler les bugs suivants :
    - dans la détection du contenu après "$", les identifiants composés de
      nombres étaient transformés en entiers, agissant sur le dictionnaire comme
      sur une liste, provoquant une erreur.
    - des erreurs de nom dans les variables.
    - manque du premier caractère à chaque ligne de texte.
    - manque du premier caractère à chaque titre.
    - _remplacement renvoyait une liste.
    - mauvais fonctionnement de la gestion des choix.
    - mauvais fonctionnement des caracteres d'éhappement.
    - mauvaise gestion des pauses.
"""
