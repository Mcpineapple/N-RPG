import accesmodule

"""
Ce test permet de faire marcher la méthode .afficher() de l'arbre binaire. Il
construit un arbre binaire et le fait s'afficher.
"""
from nrpg.arbre import Arbre

arbre = Arbre("1")
arbre.fils_gauche = "2"
arbre.arete_gauche = "A"
arbre.fils_droit = "3"
arbre.arete_droit = "B"
arbre.fils_gauche.fils_gauche  = "4"
arbre.fils_gauche.arete_gauche = "C"
arbre.fils_gauche.fils_droit = "5"
arbre.fils_gauche.arete_droit = "D"
arbre.fils_droit.fils_gauche = "6"
arbre.fils_droit.arete_gauche = "E"
arbre.fils_droit.fils_droit  = "7"
arbre.fils_droit.arete_droit = "F"

arbre.afficher()

"""
Ce test a permis de régler les bugs suivants :
"""
