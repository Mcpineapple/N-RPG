# Ce test vérifie le bon fonctionnement des fonctions basiques du moteur CLI

# Ajout des modules
import accesmodule

from nrpg.moteur import MoteurCLI

# Création d'un moteur
moteur = MoteurCLI()

# Texte du *Soulier de satin*, de Camille Claudel
moteur.personnage = ""
moteur.afficher("L’ANNONCIER , un papier à la main, tapant fortement le sol avec sa canne, annonce :")
moteur.afficher("...")
moteur.personnage = "L'annonciér"
moteur.afficher("Fixons, je vous prie, mes frères, les yeux sur ce point de l’Océan Atlantique qui est à quelques degrés au-dessous de la Ligne à égale distance de l’Ancien et du Nouveau Continent.")
