import accesmodule

"""
Ce test permet de récupérer le script du jeu, de l'ajouter dans un arbre, puis
d'afficher l'arbre. Il permet de vérifier l'utilisation du parser et du système
de construction d'arbre.
"""

import os
import sys
from nrpg.arbre import Arbre

position_script = os.path.join(os.path.dirname(__file__), '..', 
        '..', 'script', 'depart.md')

arbre = Arbre("JOLIE PETITE HISTOIRE")

arbre.construire(None, position_script)
arbre.afficher()

"""
Ce test a permis de régler les bugs suivants :
    - Erreur de syntaxe
    - Manque de passage d'un titre à l'arbre
    - Ne marche pas avec les lignes vides
    - Mauvais contenu envoyé dans les arêtes
    - Appel erroné à l'arbre à la place du parser
    - Fautes d'orthographe
    - Mauvais modèle de récursion dans la construction de l'arbre
    - Problème du parser dans la recherche d'identifiant
    - Mauvaise gestion de la fin de fichier du parser
"""
