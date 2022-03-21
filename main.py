# Importation du moteur qui fait tourner le jeu
from nrpg.moteur import *
# Importation du module os.path, essentiel pour proprement indiquer l'emplacement d'un fichier
import os.path

# Création d'objets contenant l'emplacement du son et de l'image d'introduction
image = os.path.join(os.path.dirname(__file__), 'media', 'images', 'imagemenu.jpg')
son = os.path.join(os.path.dirname(__file__), 'media', 'sfx', 'Duckpoxode_Syrup.mp3')

# Création de l'objet tkinter
root = Tk()

# Création du moteur
moteur = MoteurGUI("Bonjour !\n")

# Lancement de l'interface
moteur.lancer_interface(root, image, son)

# Boucle principale de l'objet root pour afficher l'interface graphique
root.mainloop()
