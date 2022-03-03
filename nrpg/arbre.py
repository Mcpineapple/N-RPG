# Ce fichier est destiné à l'implémentation (la plus simple et efficace) d'un
# arbre binaire pour représenter l'histoire. La classe sera utilisée par le
# parser de script pour y mettre l'histoire.
class Arbre:

    def __init__(self, texte : str):

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.texte = texte

        self.fils_gauche = None
        self.fils_droit = None

        self.arete_gauche = u""
        self.arete_droit = u""

    @property
    def inserer_fils_gauche(self, texte : str):

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.fils_gauche = Arbre(texte)

    @property
    def inserer_arete_gauche(self, texte : str):

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.arete_gauche = texte

    @property
    def inserer_fils_droit(self, texte : str):

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."

        self.fils_droit = Arbre(texte)
    
    @property
    def inserer_arete_droit(self, texte : str):

        assert isinstance(texte, str), u"L'arbre doit contenir des chaînes de caractères."
        
        self.arete_droit = texte


    @property
    def recuperer_fils_gauche(self):
        
        return self.fils_gauche

    @property
    def recuperer_fils_droit(self):

        return self.fils_droit

    @property
    def lire_arete_gauche(self):

        return self.arete_gauche

    @property
    def lire_arete_droit(self):

        return self.arete_droit
