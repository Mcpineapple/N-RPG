# Ce fichier est destiné à l'implémentation (la plus simple et efficace) d'un
# arbre binaire pour représenter l'histoire. La classe sera utilisée par le
# parser de script pour y mettre l'histoire.

class Arbre:
    u"""
    Arbre binaire simple permettant de contenir le script et ses embranchements.
    Les noeuds contiendront du texte correspondant à l'histoire.
    Les arêtes de l'arbre contiennent du texte qui décriront les embranchements.
    """

    def __init__(self, texte : str):
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
    def arete_gauche(self, texte : str):
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
    def fils_droit(self, texte : str):
        u"""
        Permet de creer un fils droit au Noeud.
        Préconditions:
            Paramètres:
                texte: str, correspond au script du noeud créé
        Postconditions:
            Creer un fils droit, un arbre.
        """

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.fils_droit = Arbre(texte)

    @property.setter
    def arete_droit(self, texte : str):
        u"""
        Change le texte de l'arête droite.
        Préconditions:
            Paramètres:
                texte : str, sera le texte de l'arête
        Postconditions:
            Le texte de l'arête droite devient le texte entré.
        """

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.arete_droit = texte


    @property
    def fils_gauche(self):
        u"""
        Renvoie le fils gauche.
        Préconditions:
            Aucune
        Postconditions:
            self.fils_gauche : None ou un Arbre
        """

        return self.fils_gauche

    @property
    def fils_droit(self):
        u"""
        Renvoie le fils droit.
        Préconditions:
            Aucune
        Postconditions:
            self.fils_droit : None ou un Arbre
        """
        return self.fils_droit

    @property
    def arete_gauche(self):
        u"""
        Renvoie le texte de l'arête gauche.
        Préconditions:
            Aucune
        Postconditions:
            self.arete_gauche : str, texte de l'arête gauche
        """

        return self.arete_gauche

    @property
    def arete_droit(self):
        u"""
        Renvoie le texte de l'arête droite.
        Préconditions:
            Aucune
        Postconditions:
            self.arete_droit : str, texte de l'arête droit
        """

        return self.arete_droit
