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

    def afficher(self, texte: str, nouveau=True) -> None:
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
        if nouveau:
            print(f"\n\t", end="")
        print(f"{texte}", end="")

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
    def personnage(self, valeur: str) -> None:
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
        print(f"\n") # Imprime une ligne vide de séparation
        print(f"{self.personnage}", end="")

    def __del__(self) -> None:
        pass

class MoteurGUI:
    u"""
    Moteur de jeu graphique destiné à la représentation du jeu. Il possède des
    fonctions étendues, nottament l'affichage graphique de fonds et de dessins,
    le rendement de son, l'intéraction graphique avec le joueur par le biais de
    boutons. Il ouvre une fenêtre graphique par le biais du module standard
    python Tkinter.
    D'autres fonctions futures à ajouter à ce moteur sont :
        - La tenue d'un log de jeu
        - La gestion des sauvegardes
        - Adaptation selon la taille
    """
    def __init__(self, menu=None) -> None:
        u"""
        Crée un objet MoteurGUI, et initialise une interface utilisateur de
        base, extensible et personnalisable. Un menu permettant d'autres actions
        peut être passé.
        Préconditions :
            Le module standard python Tkinter doit être disponible
            Une fenêtre graphique doit pouvoir s'afficher via Tkinter
            Paramètres :
                menu : fonction, par défaut None. Cette fonction doit pouvoir
                    recevoir l'objet Tkinter, ce qui lui permet d'agir dessus.
                    Cette fonction peut aussi renvoyer des informations à
                    charger dans le parser (dans le cas par exemple de la
                    sélection de sauvegarde).
        Postconditions :
            Création d'une fenêtre de jeu active, éventuellement en affichant un
            menu de jeu. Cette fenêtre possède des options classiques
            d'interface de jeu.
            Sortie : Aucune.
        """
        from tkinter import Tk, Button, Label # Ne doit se faire que si le module n'est pas
        from PIL import ImageTk, Image
        import pathlib
        # encore importé

        self.fenetre = Tk()

        image_OG = Image.open(pathlib.Path("media/Sakurajima_Mai_Holding_The_HolyC_Programming_Language.jpg"))
        image_OG_tk = ImageTk.PhotoImage(image_OG)

        self.affichage = Label(self.fenetre, image=image_OG_tk)
        self.affichage.grid(column=0, row = 0, columnspan = 11, rowspan=10)

        self.bouton_gauche = Button(self.fenetre, text="1", command=self.fonc_bouton_gauche)
        self.bouton_gauche.grid(row=11, column=0, columnspan=3, sticky='w')

        self.bouton_droit = Button(self.fenetre, text = "2", command=self.fonc_bouton_droit)
        self.bouton_droit.grid(row=11, column=8, columnspan=3, sticky='e')

        self.commande_bouton_gauche = "delete"
        self.commande_bouton_droit = "start"

        self.fenetre.mainloop()


    def fonc_bouton_gauche(self):
        u"""
        Fonctions exécutées lorsque on appuie sur le bouton gauche.
        Préconditions :
            Aucune
        Postconditions :
            La commande associée au bouton gauche est executée.
        """
        if self.commande_bouton_gauche == "delete":
            self.fenetre.destroy()
        elif self.commande_bouton_gauche == "previous":
            pass

    def fonc_bouton_droit(self):
        u"""
        Fonctions exécutées lorsque on appuie sur le bouton droit.
         Préconditions :
            Aucune
        Postconditions :
            La commande associée au bouton gauche est executée.       """
        if self.commande_bouton_droit ==  "start":
            self.commande_bouton_gauche = "previous"
            self.commande_bouton_droit = "next"
        elif self.commande_bouton_droit == "next":
            pass

    def __del__(self) -> None:
        u"""
        Détruit un objet MoteurGUI en effectuant les maintenances nécessaires et
        en nettoyant les fenêtres grahiques affichées à l'écran.
        """
        pass

#test
test = MoteurGUI()
