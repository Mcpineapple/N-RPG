# Ce court script est essentiel au bon fonctionnement des tests
# Il est appelé par tous les tests, et permet simplement d'importer les modules
# testés, puisqu'ils ne sont pas présents dans le même dossier.

# Ce script permet d'importer le paquet présent à la racine de ce projet, peu
# importe d'où il est exécuté, tant que ce script en particulier est présent
# sous le chemin "/portofolio/tests/" du projet.

import os
import sys
position = os.path.dirname(__file__)
dossier_module = os.path.join(position, '..', '..')
sys.path.append(dossier_module)

# Il suffit d'importer ce script : les instructions s'exécuteront
