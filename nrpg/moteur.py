from time import sleep
from tkinter import * 
from PIL import Image, ImageTk
import pathlib
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

class MoteurGUI(Frame):
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
    def __init__(self, master=None, menu=None) -> None:
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

        Frame.__init__(self, master)
        largeur,hauteur = 650, 650
        master.minsize(width=largeur, height=hauteur)
        master.maxsize(width=largeur, height=hauteur)
        self.pack(side=BOTTOM)

        image = Image.open("media/lagiacrus.jpg")
        image = image.resize((600,600), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image) 

        self.label = Label(image=self.image)
        self.label.pack(side=TOP)

        self.bouton_gauche = Button(self, text="1", command=self.fonc_bouton_gauche)
        self.bouton_gauche.pack(side=LEFT)

        self.bouton_droit = Button(self, text = "2", command=self.fonc_bouton_droit)
        self.bouton_droit.pack(side=RIGHT)

        self.commande_bouton_gauche = "delete"
        self.commande_bouton_droit = "start"


    def changer_image(self, emplacement):
        image = Image.open(emplacement)
        image = image.resize((600,600), Image.ANTIALIAS)
       
        self.image2 = ImageTk.PhotoImage(image)
        self.label.configure(image=self.image2)
        self.label.image=self.image2


    def fonc_bouton_gauche(self):
        u"""
        Fonctions exécutées lorsque on appuie sur le bouton gauche.
        Préconditions :
            Aucune
        Postconditions :
            La commande associée au bouton gauche est executée.
        """
        global root
        if self.commande_bouton_gauche == "delete":
            root.destroy()
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


root = Tk()
test = MoteurGUI(master=root)
test.changer_image("media/fin.png")
test.mainloop()
