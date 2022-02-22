u"""
Ce fichier est le moteur de jeu.
Son but est de recevoir :
    - Le texte à afficher
    - Les information qu'il va chercher dans l'arbre (background, etc.)
À partir de ceci, il doit :
    - Afficher le texte
    - Charger et changer les images
    - Jouer tout autre média
    - S'occuper des boutons de choix
    - Éventuellement gérer n'importe quelle autre fonction de la fenêtre de jeu
Il s'agit soit d'un collection de fonctions, soit d'un objet unique avec des
méthodes attachées.
On peut de plus mettre dans le même fichier le moteur graphique et console, ou
les séparer.
"""

class MoteurCLI:
    u"""
    Moteur de jeu en ligne de commande simple. Il dispose d'une API standard
    permettant de recevoir des appels du jeu principal et de communiquer avec le
    script via le parser.
    Il se charge de l'affichage du texte et du traitement de l'entrée.
    """
    def __init__(self) -> None:
        u"""
        Constructeur de la classe MoteurCLI.
        Préconditions :
            Avoir à disposition une sortie standard quelconque vers laquelle
            écrire.
            Paramètres : Aucun
        Postconditions :
            Création d'un objet MoteurCLI qui pourra exécuter des actions par ses
            méthodes.
        """
        self._personnage = "" # Cette valeur correspond au personnage affiché
        # en haut de ligne : il peut être vide. Il s'agit d'une chaîne de
        # caractères

    def afficher(self, str: texte, ajouter=False) -> None:
        u"""
        Affiche le texte envoyé, à la place du précédent ou en l'ajoutant
        au précédent.
        Préconditions :
            Déclaration, nulle ou non d'un personnage
            Paramètres :
                texte : str, le texte entré
                ajouter: bool, si cette valeur est vraie, le texte sera ajouté
                en fin de ligne plutôt que de s'afficher sur une nouvelle ligne.
        Postconditions :
            Affiche dans la sortie standard le texte tel que demandé.
        """
        if ajouter:
            print("\n\t")
        print(texte, sep="")

    @property
    def personnage(self) -> str:
        u"""
        Renvoie la valeur du personnage actuel, prête à être ajoutée dans le
        texte.
        Préconditions :
            Déclaration, nulle ou non, d'un personnage
        Postconditions :
            Retour :
               _ : str, le nom du personnage, suivi d'un espace et de deux
               points
        """
        a = self._personnage
        return f"{self._personnage} : " if a else "" # Renvoie ce qui est
        # attendu si le personnage est non nul, et une chaîne vide sinon

    @personnage.setter
    def personnage(self, str: valeur) -> None:
        u""""
        Permet de modifier la valeur du personnage actuel, en analysant
        éventuellement tout ajout à modifier dans le nom. Le changement de
        personnage montre aussi le nom du nouveau personnage.
        Préconditions :
            Existence de la valeur _personnage dans l'objet.
            Paramètres :
                valeur : str, le nom qu'on souhaite attribuer au personnage
                actuel.
        Postconditions:
            Changement de valeur en valeur de _personnage, et affichage du nom
            du personnage dans la sortie standard.
        """
        self._personnage = valeur
        print(f"\n {self.personnage}")

    def __del__(self) -> None:
        pass
