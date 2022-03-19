u"""
Ce fichier contient le parser de script. Il peut être dynamique (prendre des
appels et construire au fur et à mesure) ou statique (bouffer le texte une
fois et renvoyer un arbre).
Son but est de recevoir:
    - Le script, formaté de façon pratique pour tous
    - La classe arbre
Et ainsi de renvoyer un arbre, comprenant toutes les informations récupérées
dans le script pour le bon fonctionnement du jeu.
Ces informations peuvent être statiques (contruire l'arbre et fourrer le texte)
ou dynamique (et retient uniquement les numéros de ligne pour aller chercher
dans le scipt le texte).
Le système peut se faire sous la forme d'une classe ou d'une collection de
fonctions.
"""

# Un dictionnaire retiendra les points et leur position, un dictionnaire de
# dictionnaires dans le cas de plusieurs fichiers.

# Ce parser doit s'en tenir au moins possible d'entrées de la part du moteur, et
# d'actionner un nombre limité d'appels au moteur (une spécification du moteur
# polyvalente et réduite)

import json, sys, os.path

# Erreur en fin de fichier
class FinError(Exception):
    pass

class Parser:
    def __init__(self, script: str, position: int = None) -> None:
        u"""
        Initialisation d'un parser à utiliser pour lire le script et le
        transformer en appels au moteur de jeu.
        Préconditions :
            Un moteur quelconque suivant la spécification (à trouver dans
                portofolio/moteur), qui recevra l'information en appelant le
                parser.
            Un script écrit en Visual Novel MarkDown (.vnmd), suivant la
                spécification à trouver dans portofolio/vnmd.
            Paramètres :
                script : str, le chemin vers le fichier de script VNMD qui est lu
                position : int, la position dans le fichier lu (par défaut, 0)
        Postconditions :
            Création d'un objet parser, auquel est envoyé la méthode continuer,
            qui exécute la prochaine partie du script, la méthode sauvegarder
            ou bien la méthode choisir avec un paramètre dans le cas des choix.
            Ces commandes entraînent un renvoi, défini sleon la spécification,
            reçu par le moteur.
            Sortie : Aucune
        """
        self._script_nom = script # Enregistre le nom du script actuel
        self._script_actuel = open(script,"r") # Une amélioration peut
        # éventuellement se faire sur le buffering des fichiers. Néanmoins, ce
        # changement n'est pas trivial, complexe et rarement très utile.
        if position :
            u"""
            Ne se déclenche que si une position particulière est
            précisée : par défaut, la valeur étant None, rien ne se passe et
            le pointeur sur le fichier reste bien à la position par défaut.
            """
            self._script_actuel.seek(position) # Placement du pointeur
        self._table = {self._script_nom : {}}
        u"""
        Dictionnaire de dictionnaires : il contient les
        identificateurs retenus et leur position, rangés par fichier
        Le hachage automatique des dictionnaires en python permet une
        meilleure performance de ce type de fonctions.
        La position retenue est le premier caractère des paramètres de la ligne,
        que le parser analysera alors et enverra alors.
        """
        self._aliases = {} # Aliases à remplacer
        self._choix = [] # Options entre lesquelles choisir

    def _fin(func):
        """
        Décorateur permettant de prendre en charge l'erreur en arrivant en fin de
        fichier.
        Préconditions :
            Décorer une fonction qui fait appel à self._lire(), directemet ou
                indirectement, et renvoie une valeur vers l'extérieur.
            Paramètres :
                func : func, la fonction décorée
        Postconditions :
            Si tout s'est bien passé, ne modifie pas la sortie de la fonction
                précédente. Si une erreur de fin de fichier est levée, renvoie
                une fin vide.
        Sortie :
            sortie : str, soit la sortie de la fonction, soit une fin vide
        """
        def inner(self):
            try :
                sortie = func(self)
            except(FinError):
                sortie = json.dumps({
                'type': 'fin',
                'parametres': '',
                'texte': ''
                })
            except (Exception) as e:
                # Dans le cas d'une autre erreur, la laisse passer normalement
                raise
            finally:
                return sortie
        return inner

    @_fin
    def continuer(self) -> None:
        u"""
        Lit la ligne suivante et analyse le texte.
        Fonction principale du parser, elle est appelée par le moteur de jeu
        pour passer au suivant.
        Préconditions :
            Existence d'un scipt valide depuis lequel lire dans
                self._script_actuel
            Paramètres : Aucun
        Postconditions :
            Avancée du pointeur du fichier jusqu'à la prochaine ligne en
            attente, et renvois au moteur de jeu en fonction de ce qui a été lu.
            En fonction des lectures peuvent être faits :
                - Des ajouts à la _table
                - Un envoi de choix
                - Un affichage de texte
                - Une modification de paramètres
                - L'arivée à une fin
            Et toutes les autres possibilités de contrôle précisées pour le
            VNMD.
            Sortie :
                json.dumps(sortie): json, sortie standardisée pour le moteur de jeu
        """
        # Lecture du premier caractère de la ligne
        caractere = self._lire()

        if caractere == "\n":
            contenu = {
                    "type": "texte",
                    "remplacer": 1,
                    "contenu": ""
                    }
            return json.dumps(contenu)

        elif caractere == "$":
            identifiant = self._identifiant()
            sortie = {
                    "type": "parametres"
                    }
            if identifiant != "":
                self._table[self._script_nom][str(identifiant)] \
                        = self._script_actuel.tell()
                # Le type d'identifiant doit être forcé pour éviter
                # l'auto-changement. Python stuff.
            caractere = self._lire()
            parametre = ""
            while True:
                if caractere == "\n":
                    break
                elif caractere == "=":
                    if parametre != "":
                        sortie[self._remplacement(parametre)] \
                                = self._identifiant()
                        parametre = ""
                else:
                    parametre += caractere
                caractere = self._lire()
            return json.dumps(sortie)

        elif caractere == "/":
            self._contenu()

        elif caractere == "-":
            sortie = {
                    "type": "choix"
                    }
            compteur = -1 # Pour partir de 0
            while True:
                if caractere == "-":
                    compteur += 1
                    self._choix.append("")
                    sortie[compteur]={
                            "parametres": self._identifiant(),
                            "texte": self._contenu()
                            }
                elif caractere == "=":
                    self._choix[compteur] = self._identifiant()
                    self._contenu() # Ignorer la fin de la ligne
                elif caractere == "\n":
                    break
                else:
                    self._contenu()
                caractere = self._lire()
            return json.dumps(sortie)

        elif caractere == "#":
            ordre = 0
            while caractere == "#":
                ordre += 1 # Description de l'ordre du titre
                caractere = self._lire()
            parametres = self._identifiant()
            contenu = self._contenu()
            sortie = {
                    "type": "titre",
                    "parametres": parametres,
                    "ordre": ordre,
                    "contenu": contenu
                    }
            return json.dumps(sortie)

        elif caractere == "*":
            self._table[self._identifiant()] = self._contenu()

        elif caractere == "=":
            identifiant = self._identifiant()
            if identifiant != "":
                self._rechercher(identifiant)
            else:
                self._contenu()

        elif caractere == ">":
            sortie = {
                    "type": "texte",
                    "remplacer": 0,
                    "contenu": ""
                    }
            return json.dumps(sortie)

        elif caractere == "|":
            parametres = self._identifiant()
            contenu = self._contenu()
            sortie = {
                    "type": "fin",
                    "parametres": parametres,
                    "texte": contenu
                    }
            return json.dumps(sortie)

        else: # Dans le cas de texte normal
            contenu = caractere + self._contenu(True)
            sortie = {
                    "type": "texte",
                    "remplacer": 0,
                    "contenu": contenu
                    }
            return json.dumps(sortie)

    def choisir(self, choix: int = None) -> None:
        u"""
        Permet de selectionner l'un des choix disponibles. Les identifiants vers
        lequels les choix menent sont enregistres dans self._choix.
        Préconditions :
            Disponibilité d'un fichier ouvert dans self._script_actuel
            Disponibilité des identifiants vers lesquels les choix menent dans
                self._choix.
            Paramètres :
                choix : int, le numero du choix vers lequel est redirige le
                    script
        Postconditons :
            Deplacement de la position dans le fichier vers le bon emplacement.
            Reinitialisation de self._choix pour un prochain choix
            Sortie : Aucune
        """
        destination = self._choix[choix]
        if destination != "": # Par defaut, laisse au paragraphe suivant
            self._rechercher(destination)
        self._choix = []

    @_fin
    def sauvegarder(self) -> None:
        u"""
        Donne la position actuelle du parser afin de pouvoir réutiliser cette
        position. Le processus de sauvegarde et de gestion des autres
        informations est laissée au moteur de jeu.
        Préconditions :
            Disponibilité d'un fichier ouvert dans self._script_actuel
            Paramètres : Aucun
        Postconditons :
            Sortie :
                _ : json, appel standardisé contenant le nom du fichier et la
                position dans celui-ci.
        """
        sortie = {
                "type" : "sauvegarde",
                "fichier" : self._script_nom,
                "position" : self._script_actuel.tell()
                }
        return json.dumps(sortie)

    # Fonctions servant au fonctionnement des appels principaux

    def _identifiant(self) -> str:
        u"""
        Lit l'identifiant à la suite d'un symbole, et le renvoie. Prend en
        compte les alias à remplacer.
        Préconditions :
            Existence d'un script ouvert sous forme d'un objet file
                self._script_actuel
            Le pointeursur le fichier devrait êtreau premier caractère à la
                suite d'un caractère qui précède un identifiant.
            Paramètres : Aucun
        Postconditions :
            Déplacement du pointeur dans le fichier après l'identifiant.
            Sortie :
                identifiant : str, identifiant lu
        """
        identifiant = ""
        caractere = self._lire()
        while True:
            if caractere == "\\": # Caractère d'échappement
                caractere = self._script_actuel.read(1)
                # Ne passe pas par les autres vérifications
            elif caractere == " ":
                break
            elif caractere == "\n":
                self._script_actuel.seek(self._script_actuel.tell()-1,0) # Retour en arrière
                break
            identifiant += caractere
            caractere = self._lire()
        return self._remplacement(identifiant)

    def _contenu(self, stop=False) -> str:
        u"""
        Lit le contenu jusqu'à la fin de la ligne, et le renvoie. Permet aussi
        évetuellement de prendre en compte les pauses dans le texte. Prend en
        compte les lignes étendues à l'aide de l'espace en début de ligne
        suivante et de remplacer les aliases.
        Préconditions :
            Existence d'un script ouvert sous forme d'un objet file dans
                self._script_actuel.
            Le positionnement doit être sur une ligne de contenu, après que les
                autres informations aient été lues.
            Paramètres :
                stop : bool, note s'il faut s'arêter en rencontrant un symbole
                de pause. Par défaut, la valeur est "False".
        Postconditions :
            Positionnement du pointeur dans le fichier au début d'une nouvelle
            ligne.
            Sortie :
                contenu : str, texte lu jusqu'à la fin de la ligne.
        """
        # Trouver un moyen de bien s'occuper de la fin du fichier !
        contenu = ""
        while True:
            caractere = self._lire()
            if caractere == "\\": # Caractère d'échappement
                caractere = self._script_actuel.read(1)
                # Ne passe pas par les autres vérifications
            elif caractere == "\n":
                if self._lire() == " ":
                    contenu += " " # Laisse un espace
                    continue # Si la ligne est étendue
                else :
                    self._script_actuel.seek(self._script_actuel.tell()-1,0) # Retour en arrière
                    break
            elif stop and caractere == ">":
                break
            contenu += caractere
        return self._remplacement(contenu)

    def _lire(self) -> str:
        u"""
        Lit le caractere suivant de self._script_actuel, et le renvoie. Fait le
        nécessaire si le script atteint sa fin. Prend en compte les caracteres
        d'échappement.
        Préconditions:
            Existence s'un script ouvert sous forme d'un objet file dans
                self._script_actuel
            Paramètres : Aucun
        Postconditions:
            Avancement d'une position du pointeur dans le fichier
            Renvoie une erreur de fin de fichier si on ne lit plus rien
            Sortie :
                _ : str, le caractere lu.
        """
        caractere = self._script_actuel.read(1)
        if caractere == "":
            raise FinError
        return caractere

    def _rechercher(self, identifiant: str) -> None:
        u"""
        Place le pointeur dans le fichier à la ligne correspondant à
        l'identifiant, soit en le retrouvant dans la _table, soit en lisant le
        script, en indexant tous les autres identifiants trouvés sur le chemin.
        Préconditions :
            Existence d'un script dans lequel rechercher
            Existence d'une _table dans laquelle indexer les positions
                d'identifiants
            Paramètres :
                identifiant : str, le nom de l'identifiant recherché
        Postconditions :
            Placement du pointeur sur le fichier à l'identifiant demandé
            Indexage des identifiants rencontrés
            Sortie : Aucune
        """
        # Passe sur l'identifiant pour y trouver un lien
        if identifiant[0] == '[':
            compteur = 1
            lien = ""
            while (lettre := identifiant[compteur]) != ']': # Passage dans les
                                                            # crochets
                lien += lettre
                compteur += 1
            self._passage_fichier(lien)
            identifiant = identifiant[compteur+1:] # Recoupage de l'identifiant
        if identifiant != "": # Dans le cas où on change de fichier sans aller
            # vers un nouvel identifiant, mais juste le début du fichier
            position = self._table.get(identifiant) # None si la clé n'est pas
            # présente
            if position is not None:
                self._script_actuel.seek(position)
            else:
                while True:
                    caractere = self._lire()
                    while caractere != "\n": # Recherche d'une fin de ligne
                        caractere = self._lire()
                    while caractere == "\n": # En cas de plusieurs retours à la ligne
                        caractere = self._lire()
                    if caractere == "$": # Et que celle-ci commence par un $
                        nom = self._identifiant()
                        if nom != "": # N'enregistre pas dans le cas d'une ligne
                            # de paramètre anonyme
                            self._table[nom] = self._script_actuel.tell()
                        if nom == identifiant : # Si il s'agit de ce que l'on
                            # cherchait
                            break # Fin de la fonction

    def _passage_fichier(self, fichier: str) -> None:
        u"""
        Change le fichier dans lequel travaille actuellement le parser.
        Préconditions :
            Paramètres :
                fichier : str, le nom du fichier vers lequel on passe
        Postconditions:
            Changement du fichier dans lequel le parser est placé et de son nom
            Sortie : Aucune
        """
        dossier = os.path.dirname(self._script_nom)
        # Enregistre le nom du script actuel en donnant sa route
        self._script_nom = os.path.join(dossier, fichier)
        self._script_actuel.close()
        self._script_actuel = open(self._script_nom,"r")
        self._table[self._script_nom] = {}

    def _remplacement(self,contenu: str) -> str:
        u"""
        Remplace dans un texte les aliases, et renvoie la version interprétée.
        Préconditions :
            Avoir une table d'aliases disponibles
            Paramètres :
                contenu : str, un texte à traiter
        Postconditions :
            Sortie :
                sortie : str, le texte traité
        """
        sortie = [""]
        actuel = 0 # Boucle actuelle
        for i in contenu:
            if i == "{":
                sortie.append("")
                actuel += 1
            elif i == "}" and actuel != 0:
                remplacement = self._table.get(sortie[actuel])
                if remplacement:
                    sortie[actuel-1] += remplacement
                else:
                    sortie[actuel-1] += sortie[actuel]
                actuel -= 1
                sortie.pop()
            else:
                sortie[actuel] += i
        return sortie[0]
