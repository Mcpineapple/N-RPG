
from nrpg.moteur import *
from nrpg.arbre import * 
import os.path

root = Tk()
moteur = MoteurGUI("Bienvenue !")
image1 = "media/images/imagemenu.jpg"
son = "media/sfx/Duckpoxode_Syrup.mp3"
moteur.lancer_interface(root, image1,son)
#moteur.arbre.afficher()
root.mainloop()
