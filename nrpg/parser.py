"""
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

import json

class Parser:
    def __init__(self, script: str, position: int = None) -> None:
        """
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
            Création d'un objet parser, auquel est envoyé la méthode suivant,
            qui exécute la prochaine partie du script, la méthode sauvegarde
            ou bien la méthode choix avec un paramètre dans le cas des choix.
            Ces commandes entraînent un renvoi, défini sleon la spécification,
            reçu par le moteur.
        """
        self.script_nom = script # Enregistre le nom du script actuel
        self.script_actuel = open(script,r,0) # Une amélioration peut
        # éventuellement se faire sur le buffering des fichiers. Néanmoins, ce
        # changement n'est pas trivial, complexe et rarement très utile.
        if position :
            """
            Ne se déclenche que si une position particulière est
            précisée : par défaut, la valeur étant None, rien ne se passe et
            le pointeur sur le fichier reste bien à la position par défaut.
            """
            self.script_actuel.seek(position) # Placement du pointeur
        self.table = {self.script_nom : {}}
        """
        Dictionnaire de dictionnaires : il contient les
        identificateurs retenus et leur position, rangés par fichier
        Le hachage automatique des dictionnaires en python permet une
        meilleure performance de ce type de fonctions.
        La position retenue est le premier caractère des paramètres de la ligne,
        que le parser analysera alors et enverra alors.
        """

    def suivant(self) -> None:
        """
        Lit la ligne suivante et analyse le texte.
        Fonction principale du parser, elle est appelée par le moteur de jeu
        pour passer au suivant.
        Préconditions :
            Existence d'un scipt valide depuis lequel lire dans
                self.script_actuel
            Paramètres : Aucun
        Postconditions :
            Avancée du pointeur du fichier jusqu'à la prochaine ligne en
            attente, et renvois au moteur de jeu en fonction de ce qui a été lu.
            En fonction des lectures peuvent être faits :
                - Des ajouts à la table
                - Un envoi de choix
                - Un affichage de texte
                - Une modification de paramètres
                - L'arivée à une fin
            Et toutes les autres possibilités de contrôle précisées pour le
            VNMD.
            Sortie :
                sortie : json, sortie standardisée pour le moteur de jeu
        """
        # Lecture du premier caractère de la ligne
        caractere = self._lire()
        if caractere == "$":
            # Ajout de l'identifiant
            # Ajout des paramètres
            # Retour de l'appel
            pass

        elif caractere == "/":
            while self._lire() != "\n":
                pass # Lit directement la nouvelle valeur jusqu'en fin de ligne

        elif caractere == "-":
            caractere = self._lire()
            parametre = ""
            while caractere != " ": # Paramètre
                parametre += caractere
                caractere = self._lire()
            contenu = ""
            caractere = self._lire()
            while True:
                if caractere == "\n":
                    if self._lire() != " ": # Si ligne étendue
                        self.script_actuel.seek(-1,1) # Retour en arrière
                        # Pour laisser place à la prochaine lecture
                        break
                    else:
                        caractere = self._lire()
                contenu += caractere

            # Doit gérer la séquence de choix complète !
            pass # Retour de l'information

        elif caractere == "#":
            ordre = 0
            while caractere == "#":
                ordre += 1 # Description de l'ordre du titre
                caractere = self._lire()
            if caractere == " ": # Passer le premier espace
                caractere = self._lire()
            contenu = ""
            while caractere != "\n":
                contenu += caractere
                caractere = self._lire()
            pass # Retour d'information

        elif caractere == "*":
            pass

        else: # Dans le cas de texte normal
            pass

    def choix(self, choix: int = None) -> None:
        pass

    def sauvegarde(self) -> None:
        """
        Donne la position actuelle du parser afin de pouvoir réutiliser cette
        position. Le processus de sauvegarde et de gestion des autres
        informations est laissée au moteur de jeu.
        Préconditions :
            Disponibilité d'un fichier ouvert dans self.script_actuel
            Paramètres : Aucun
        Postconditons :
            Sortie :
                _ : json, appel standardisé contenant le nom du fichier et la
                position dans celui-ci.
        """
        sortie = {
                "fichier" : self.script_nom,
                "position" : self.script_actuel.tell()
                }
        return json.dumps(sortie)

    # Fonctions servant au fonctionnement des appels principaux

    def _lire(self) -> str:
        """
        Lit le caractere suivant de self.script_actuel, et le renvoie. Fait le
        nécessaire si le script atteint sa fin.
        Préconditions:
            Existence s'un script ouvert sous forme d'un objet file dans
                self.script_actuel
            Paramètres : Aucun
        Postconditions:
            Avancement d'une position du pointeur dans le fichier
            Appel à _fin si la fin du fichier est atteinte.
            Sortie :
                _ : str, le caractere lu.
        """
        caractere = self.script_actuel.read(1)
        if caractere == "":
            self._fin()
        return caractere

    def _recherche(self, identifiant: str) -> None:
        """
        Place le pointeur dans le fichier à la ligne correspondant à
        l'identifiant, soit en le retrouvant dans la table, soit en lisant le
        script, en indexant tous les autres identifiants trouvés sur le chemin.
        Préconditions :
            Existence d'un script dans lequel rechecher
            Existence d'une table dans laquelle indexer les positions
                d'identifiants
            Paramètres :
                identifiant : str, le nom de l'identifiant recherché
        Postconditions :
            Placement du pointeur sur le fichier à l'identifiant demandé
            Indexage des identifiants rencontrés
            Sortie : Aucune
        """
        position = self.table.get(identifiant) # None si la clé n'est pas
        # présente
        if position is not None:
            self.script_actuel.seek(position)
        else:
            while True:
                caractere = self._lire()
                if caractere == "": # Arrivée en fin de fichier : ne lit plus
                    # aucun caractère
                    self._fin()
                elif caractere == "\n": # Si on revient à la ligne
                    caractere = self._lire()
                    if caractere == "$": # Et que celle-ci commence par un $
                        nom = "" # Création d'un nom pour cet identifiant
                        caractere = self._lire() # Vérifie le
                        # caractère suivant
                        while caractere != " ": # Cherche jusqu'à l'espace
                            nom += caractere # Enregistre le nom
                            caractere = self._lire()
                        if nom != "": # N'enregistre pas dans le cas d'une ligne
                            # de paramètre anonyme
                            self.table[nom : self.script_actuel.tell()]
                        if nom == identifiant : # Si il s'agit de ce que l'on
                            # cherchait
                            break # Fin de la fonction

    def _fin(self) -> None:
        # Action lorsque la fin du fichier est trouvée
        pass
