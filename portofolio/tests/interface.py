#!/usr bin/env python
# -*- coding: utf-8 -*-

from nrpg.moteur import *
from nrpg.arbre import *
import os.path

root = Tk()
moteur = MoteurGUI("Bienvenue !")
image1 = os.path.join(os.path.dirname(__file__), '..', '..', 'media', 'images', 'lagiacrus.jpg')
son = os.path.join(os.path.dirname(__file__), '..', '..', 'media', 'sfx', 'Duckpoxode_Syrup.mp3') 
moteur.lancer_interface(root, image1,son)
#moteur.arbre.afficher()
root.mainloop()
