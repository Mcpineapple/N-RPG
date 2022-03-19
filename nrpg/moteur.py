from tkinter import *
import os.path
from nrpg.arbre import *
from nrpg.parser import *
from PIL import Image, ImageTk
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from pydub.playback import _play_with_simpleaudio
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
            Paramètres :  Aucun
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

class MoteurGUI(Label):
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

    def __init__(self, text_intro) -> None :
        u"""
        Créer le moteur en récupérant l'arbre.
        Préconditions :
            Aucunes
        """
        self.text_intro = text_intro


    def lancer_interface(self, master, image_init : str, musique_init : str) -> None:
        u"""
        Initialise l'interface utilisateur.
        Préconditions :
            Le module standard python Tkinter doit être disponible
            Une fenêtre graphique doit pouvoir s'afficher via Tkinter
            Paramètres :
                master : recoit l'objet Tk()
                image_init : str, recoit l'emplacement de la première image affichée
                musique_init : str, recoit l'emplacement de la musique jouée
        Postconditions :
            Création d'une fenêtre de jeu active, éventuellement en affichant un
            menu de jeu. Cette fenêtre possède des options classiques
            d'interface de jeu.
            Sortie : Aucune.
        """

        Label.__init__(self, master)

        self.fenetre = master

        # Paramètres de la fenêtre master (root), l'objet Tk
        largeur,hauteur = 800, 800
        master.minsize(width=largeur, height=hauteur)
        master.maxsize(width=largeur, height=hauteur)
        master.title("N-RPG")

        # Musique du menu
        self.jouer_musique(musique_init)

        # Image menu.
        # L'image originale est récupérée et traité puis afficher dans le label
        image = Image.open(image_init)
        image = image.resize((800, 350), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)

        self.config(image = self.image)

        self.pack(side=TOP)

        # Créations d'objets Stringvar pour stocker le texte
        self.texte_afficher = StringVar()
        self.texte_bouton_droit = StringVar()
        self.texte_bouton_gauche = StringVar()

        # Valeur initiales des StringVar
        self.texte_bouton_gauche.set("Quitter")
        self.texte_bouton_droit.set("Commencer")
        self.texte_afficher.set(self.text_intro)

        self.affichage_texte = Label(master, font=("Firacode",15), textvariable = self.texte_afficher, anchor=N, height=15)
        self.affichage_texte.pack(side=TOP)

        self.bouton_gauche = Button(master, bg="grey", textvariable = self.texte_bouton_gauche, command=self.fonc_bouton_gauche, width = 45)
        self.bouton_gauche.pack(side=LEFT,expand=True)

        self.bouton_droit = Button(master, bg="grey", textvariable = self.texte_bouton_droit, command=self.fonc_bouton_droit, width=45)
        self.bouton_droit.pack(side=RIGHT,expand=True)

        self.commande_bouton_gauche = "delete"
        self.commande_bouton_droit = "start"


    def jouer_bruitage(self, emplacement : str) -> None:
        u"""
        Joue un bruitage.
        Préconditions:
            Paramètres:
                emplacement : str, endroit ou se trouve le fichier du bruitage jouer
        """
        # Block = False empêche l'écran de geler 
        #sinon le programme attend que la musique se termine pour continuer
        try :
            playsound(emplacement,block=False)
        except:
            print(f"Erreur lors du lancement du bruitage {emplacement}.")

    def jouer_musique(self, emplacement : str) -> None:
        u"""
        Joue une musique à partir d'un fichier.
        Préconditions :
            Paramètres :
                emplacement : str, l'endroit ou se trouve le fichier (devrait commencer par 'media/'')
        Postconditions :
            self.musique contient la musique qui joue.
        """
        try :
            musique = AudioSegment.from_mp3(emplacement)
            musique = musique * 5
            self.musique = _play_with_simpleaudio(musique)
        except :
            print(f"Erreur dans le lancement de la musique {emplacement}.")

    def arreter_musique(self) -> None:
        u"""
        Arrête la musique.
        Préconditions :
            Il faut que self.musique existe.
        Postconditions :
            La musique qui jouait dans l'objet self.musique s'arrête.
        """
        try :
            self.musique.stop()
        except:
            print("Erreur lors de l'arret de la musique.")


    def changer_image(self, emplacement : str) -> None:
        u"""
        Change l'image afficher.
        Préconditions:
            Paramètres:
                emplacement : str, contient l'emplacement de l'image qu'on souhaite afficher
        Postconditions:
            L'image affichée est remplacée.
        """
        try :
            image = Image.open(emplacement)
        except :
            print("Erreur lors de l'ouverture de l'image {emplacement}.")

        image = image.resize((800,350), Image.ANTIALIAS)

        self.image2 = ImageTk.PhotoImage(image)
        self.configure(image=self.image2)
        self.image=self.image2

    def changer_texte(self, text : str) -> None:
        u"""
        Change le texte afficher.
        Préconditions :
            Paramètres :
                text : str, le texte qui sera afficher
        Postcontions :
            self.afficher texte recoit la valeur entrée.
            La valeur entrée s'affiche sur le label au centre de l'écran.
        """
        try :
            self.texte_afficher.set(text)
        except :
            print("Erreur lors du changement du texte principal.")


    def changer_texte_bouton_gauche(self, text : str) -> None:
        u"""
        Change le texte sur le bouton gauche.
        Préconditions :
            Paramètres :
                text : str, le texte qui sera afficher
        Postcontions :
            self.texte_bouton_gauche texte recoit la valeur entrée.
            La valeur entrée s'affiche sur le bouton gauche.
        """
        try :
            self.texte_bouton_gauche.set(text)
        except :
            print("Erreur lors du changement de texte du bouton de gauche.")

    def changer_texte_bouton_droit(self, text : str) -> None:
        u"""
        Change le texte sur le bouton gauche.
        Préconditions :
            Paramètres :
                text : str, le texte qui sera afficher
        Postcontions :
            self.texte_bouton_droit texte recoit la valeur entrée.
            La valeur entrée s'affiche sur le bouton droit.
        """
        try :
            self.texte_bouton_droit.set(text)
        except:
            print("Erreur lors du changement du texte du bouton de droite.")

    def fonc_bouton_gauche(self) -> None:
        u"""
        Fonctions exécutées lorsque on appuie sur le bouton gauche.
        Préconditions :
            Aucune
        Postconditions :
            La commande associée au bouton gauche est executée.
        """
        self.jouer_bruitage("media/sfx/button-3.wav")
        if self.commande_bouton_gauche == "delete":
            self.fenetre.destroy()
        elif self.commande_bouton_gauche == "gauche":
            self.arbre = self.arbre.fils_gauche()
            self.changer_texte(self.arbre.texte)
            self.changer_texte_bouton_gauche(self.arbre.arete_gauche())
            self.changer_texte_bouton_droit(self.arbre.arete_droit())


    def fonc_bouton_droit(self):
        u"""
        Fonctions exécutées lorsque on appuie sur le bouton droit.
         Préconditions :
            Aucune
        Postconditions :
            La commande associée au bouton gauche est executée.       """
        self.jouer_bruitage("media/sfx/button-3.wav")
        if self.commande_bouton_droit ==  "start":
            self.commande_bouton_gauche = "gauche"
            self.commande_bouton_droit = "droite"

            position_script = os.path.join(os.path.dirname(__file__), 'media', 'script', 'depart.md')

            self.arbre = Arbre("JOLIE PETITE HISTOIRE")

            self.arbre.construire(None, {"fichier": position_script, "position": 0})

            self.changer_texte(self.arbre.texte)
            self.changer_texte_bouton_gauche(self.arbre.arete_gauche())
            self.changer_texte_bouton_droit(self.arbre.arete_droit())

        elif self.commande_bouton_droit == "droite":

            self.arbre = self.arbre.fils_droit()
            self.changer_texte(self.arbre.texte)
            self.changer_texte_bouton_gauche(self.arbre.arete_gauche())
            self.changer_texte_bouton_droit(self.arbre.arete_droit())



