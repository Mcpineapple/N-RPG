# Ce fichier est destiné à l'implémentation (la plus simple et efficace) d'un
# arbre binaire pour représenter l'histoire. La classe sera utilisée par le
# parser de script pour y mettre l'histoire.

from parser import Parser
from json

class Arbre:
    u"""
    Arbre binaire simple permettant de contenir le script et ses embranchements.
    Les noeuds contiendront du texte correspondant à l'histoire.
    Les arêtes de l'arbre contiennent du texte qui décriront les embranchements.
    """

    def __init__(self, texte : str) -> None :
        u"""
        Constructeur de la classe Arbre.
        Préconditions :
            Paramètres :
                texte : str, correspond au script de la racine
        Postconditions :
            Création d'une classe Arbre qui contiendra le script utilisable par le Moteur.
        """

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.texte = texte

        self.fils_gauche = None
        self.fils_droit = None

        self.arete_gauche = u""
        self.arete_droit = u""

    @property.setter
    def fils_gauche(self, texte : str) -> None:
        u"""
        Permet de creer un fils gauche au Noeud.
        Préconditions:
            Paramètres:
                texte: str, correspond au script du noeud créé
        Postconditions:
            Creer un fils gauche, un arbre.
        """

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.fils_gauche = Arbre(texte)

    @property.setter
    def arete_gauche(self, texte : str) -> None:
        u"""
        Change le texte de l'arête gauche.
        Préconditions:
            Paramètres:
                texte : str, sera le texte de l'arête
        Postconditions:
            Le texte de l'arête gauche devient le texte entré.
        """
        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."
        self.arete_gauche = texte

    @property.setter
    def fils_droit(self, texte : str) -> None :
        u"""
        Permet de creer un fils droit au Noeud.
        Préconditions:
            Paramètres:
                texte : str, correspond au script du noeud créé
        Postconditions:
            Creer un fils droit, un arbre.
            Sortie : Aucune
        """
        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."
        self.fils_droit = Arbre(texte)

    @property.setter
    def arete_droit(self, texte : str) -> None :
        u"""
        Change le texte de l'arête droite.
        Préconditions :
            Paramètres :
                texte : str, sera le texte de l'arête
        Postconditions :
            Le texte de l'arête droite devient le texte entré.
            Sortie : Aucune
        """

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.arete_droit = texte


    @property
    def fils_gauche(self) -> Arbre :
        u"""
        Renvoie le fils gauche.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.fils_gauche : None ou un Arbre
        """
        return self.fils_gauche

    @property
    def fils_droit(self) -> Arbre :
        u"""
        Renvoie le fils droit.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.fils_droit : None ou un Arbre
        """
        return self.fils_droit

    @property
    def arete_gauche(self) -> str :
        u"""
        Renvoie le texte de l'arête gauche.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.arete_gauche : str, texte de l'arête gauche
        """
        return self.arete_gauche

    @property
    def arete_droit(self) -> str :
        u"""
        Renvoie le texte de l'arête droite.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.arete_droit : str, texte de l'arête droit
        """
        return self.arete_droit
    
    def construire(self, script: str, position: int = None, choix : int = None) -> None:
        u"""
        Construit l'arbre pour accueillir le contenu complet d'un script. Agit
        de façon récursive pour construire l'arbre à travers les différentes
        possibilités de l'histoire.
        Préconditions :
            Un parser de Visual Novel MarkDown, qui lira l'information depuis le
                script précisé
            Un script écrit en VNMD à préciser dans cette fonction
            Paramètres :
                script : str, le chemin vers un script en VNMD
                position : int, endroit du cript auquel la lecture du parser
                    doit commencer
        Postconditions :
            Peuplement de la structure de l'arbre sur lequel est appelée cette
            méthode avec l'ensemble des contenus et des choix du scipt entré.
            L'arbre est alors prêt à être montré pour représenter l'ensemble de
            l'histoire, les choix et les différentes routes.
            Sortie : Aucune
        """
        parser = Parser(script, position)
        arbre = self # Suivi de la racine de cet arbre
        if choix :
            parser.choisir(choix)
        information = parser.continuer()
        while (contenu := json.loads(information))["type"] != "choix" :
            if information :
                arbre.texte = information
                arbre.fils_gauche = ""
                arbre = arbre.fils_gauche
            else : # À la fin du fichier
                exit(0)
            information = parser.continuer()
        # À l'arivée d'un choix
        arbre.arete_gauche = contenu["0"] 
        arbre.arete_droit = contenu["1"] 
        # Garde l'endroit de la bifurcation
        position = json.loads(self.sauvegarde())
        arbre.fils_gauche = ""
        arbre.fls_droit = ""
        # Récursion
        arbre.fils_gauche.construire(position["fichier"], \
                position["position"], 0)
        arbre.fils_droit.construire(position["fichier"], \
                position["position"], 1)

    def afficher(self, route: str = "") -> None:
        """
        Méthode d'impression, imprime l'arbre par parcours en profondeur infixe
        afin de pouvoir le visualiser, avec des marques. Le résultat peut être
        assez grand, veuillez le visualiser à l'aide de "more" ou "less" dans
        un shell.
        Préconditions :
            L'arbre est rempli convenablement et contient des informations
            Paramètres : Aucun
        Postconditions :
            Impression vers la sortie standard de l'arbre, de façon
            visualisable. Il s'agit néanmoins probablement d'une mauvaise idée
            sur un très grand arbre.
            Sortie : Aucune
        """
        print(f"-- {route} --")
        print(self.texte())
        while not(self.fils_droit):
            if self.fils_gauche:
                print(self.fils_gauche)
                self = self.fils_gauche # Changement de racine
            else : # Fin de l'arbre
                break
        print(f"({self.arete_gauche})")
        self.fils_gauche.afficher(route + "0")
        print(f"({self.arete_droit})")
        self.fils_droit.afficher(route + "1")
