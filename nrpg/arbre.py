# Ce fichier est destiné à l'implémentation (la plus simple et efficace) d'un
# arbre binaire pour représenter l'histoire. La classe sera utilisée par le
# parser de script pour y mettre l'histoire.

from nrpg.parser import Parser
import json

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

        self._fils_gauche = None
        self._fils_droit = None

        self._arete_gauche = u""
        self._arete_droit = u""

    @property
    def fils_gauche(self):
        u"""
        Renvoie le fils gauche.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.fils_gauche : None ou un Arbre
        """
        return self._fils_gauche

    @property
    def fils_droit(self):
        u"""
        Renvoie le fils droit.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.fils_droit : None ou un Arbre
        """
        return self._fils_droit

    @property
    def arete_gauche(self):
        u"""
        Renvoie le texte de l'arête gauche.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.arete_gauche : str, texte de l'arête gauche
        """
        return self._arete_gauche

    @property
    def arete_droit(self):
        u"""
        Renvoie le texte de l'arête droite.
        Préconditions :
            Paramètres : Aucun
        Postconditions :
            Sortie :
                self.arete_droit : str, texte de l'arête droit
        """
        return self._arete_droit

    @fils_gauche.setter
    def fils_gauche(self, texte : str) -> None:
        u"""
        Permet de creer un fils gauche au Noeud.
        Préconditions:
            Paramètres:
                texte: str, correspond au script du noeud créé
        Postconditions:
            Creer un fils gauche, un arbre.
        """

        if texte is not None:
            assert isinstance(texte, str), u"L'arbre doit \
                contenir une chaîne de caractères ou être vide."

            self._fils_gauche = Arbre(texte)

    @arete_gauche.setter
    def arete_gauche(self, texte : str) -> None:
        u"""
        Change le texte de l'arête gauche.
        Préconditions:
            Paramètres:
                texte : str, sera le texte de l'arête
        Postconditions:
            Le texte de l'arête gauche devient le texte entré.
        """
        assert isinstance(texte, str), u"L'arête doit \
            contenir une chaîne de caractères."
        self._arete_gauche = texte

    @fils_droit.setter
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
        if texte is not None:
            assert isinstance(texte, str), u"L'arbre doit \
                contenir une chaîne de caractères ou être vide."
            self._fils_droit = Arbre(texte)

    @arete_droit.setter
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
        assert isinstance(texte, str), u"L'arête doit \
            contenir une chaîne de caractères"
        self._arete_droit = texte

    def construire(self, parser: Parser = None, position: dict = None) -> None:
        u"""
        Construit l'arbre pour accueillir le contenu complet d'un script. Agit
        de façon récursive pour construire l'arbre à travers les différentes
        possibilités de l'histoire. Il doit être appelé avec None comme premier
        paramètre dans la plupart des cas.
        Préconditions :
            Un parser de Visual Novel MarkDown, qui lira l'information depuis le
                script précisé
            Un script écrit en VNMD à préciser dans cette fonction
            Paramètres :
                position : dict, un dictionnaire contenant le fichier lu et la
                    position dans le fichier, avec le même modèle que les
                    sauvegardes
        Postconditions :
            Peuplement de la structure de l'arbre sur lequel est appelée cette
            méthode avec l'ensemble des contenus et des choix du scipt entré.
            L'arbre est alors prêt à être montré pour représenter l'ensemble de
            l'histoire, les choix et les différentes routes.
            Sortie : Aucune
        """

        if parser is None : # Création de parser au début
            parser = Parser(position["fichier"], position["position"])
        arbre = self # Suivi de la racine de cet arbre
        information = parser.continuer()
        while (information is None) or (((contenu := json.loads(information)) \
                ["type"] != "choix") and (contenu["type"] != "fin")) :
            if information :
                arbre.texte = information
                arbre.fils_gauche = ""
                arbre = arbre.fils_gauche
            # Conservation de la dernière position pour pouvoir revenir en
            # arrière, permettant d'accéder à l'autre choix et de recharger les
            # choix disponibles
            position = json.loads(parser.sauvegarder())
            information = parser.continuer()
        if contenu["type"] != "fin":
            aliases = parser._aliases
            # À l'arivée d'un choix
            arbre.arete_gauche = contenu["0"]["texte"]
            # Garde l'endroit de la bifurcation
            arbre.fils_gauche = ""
            # Récursion
            try : # Arrête si le tronçon d'histoire n'existe pas
                parser.choisir(0)
                arbre.fils_gauche.construire(parser)
            except :
                pass
            if contenu.get("1") :
                parser = Parser(position["fichier"], position["position"], \
                        aliases)
                arbre.arete_droit = contenu["1"]["texte"]
                arbre.fils_droit = ""
                try : # Idem
                    parser.continuer() # Charge le choix
                    parser.choisir(1)
                    arbre.fils_droit.construire(parser)
                except :
                    pass
        else :
            arbre.texte = information

    def afficher(self, route: str = "", suivant: bool = False) -> None:
        u"""
        Méthode d'impression, imprime l'arbre par parcours en profondeur infixe
        afin de pouvoir le visualiser, avec des marques. Le résultat peut être
        assez grand, veuillez le visualiser à l'aide de "more" ou "less" dans
        un shell.
        Préconditions :
            L'arbre est rempli convenablement et contient des informations
            Paramètres :
                route : str, la route de choix suivie pour arriver à ce
                    fragment. Par défaut vide.
                suivant : bool, si l'arbre descend en ligne droite plutôt que
                    droit, permettant de ne pas réafficher la route. Par défaut
                    Faux.
        Postconditions :
            Impression vers la sortie standard de l'arbre, de façon
             visualisable. Il s'agit néanmoins probablement d'une mauvaise idée
             sur un très grand arbre.
            Sortie : Aucune
        """
        if not(suivant):
            print(f"-- {route} --")
        if self.texte != "":
            print(json.loads(self.texte))
        if self.fils_droit is not None:
            print() # Retour à la ligne pour la lisibilité
            print(f"({self.arete_gauche})")
            self.fils_gauche.afficher(route + "0")
            print() # Retour à la ligne pour la lisibilité
            print(f"({self.arete_droit})")
            self.fils_droit.afficher(route + "1")
            print() # Retour à la ligne pour la lisibilité
        elif self.fils_gauche is not None:
            self.fils_gauche.afficher(route, True)
        # Sinon, l'arbre est fini et la récursion se finit
