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

# Ce parser doit s'en tenr au moins possible d'entrées de la part du moteur, et
# d'actionner un nombre limité de méthodes du moteur (une spécification du
# moteur polyvalente et réduite)

class Parser:
    def __init__(self, moteur, script: str, position: int = None) -> None:
        """
        Initialisation d'un parser à utiliser pour lire le script et le
        transformer en appels au moteur de jeu.
        Préconditions :
            Un moteur quelconque suivant la spécification (à trouver dans
                portofolio/moteur).
            Un script écrit en Visual Novel MarkDown (.vnmd), suivant la
                spécification à trouver dans portofolio/vnmd.
            Paramètres :
                moteur : [moteur], un moteur quelconque suivant la spécification
                script : str, le chemin vers le fichier de script VNMD qui est lu
                position : int, la position dans le fichier lu (par défaut, 0)
        Postconditions :
            Création d'un objet parser, auquel est envoyé la méthode suivant,
            qui exécute la prochaine partie du script, ou bien la méthode choix
            avec un paramètre dans le cas des choix. Cette commande entraîne le
            parser à exécuter des méthodes du moteur de jeu.
        """
        self.moteur = moteur # Enregistre la référence du moteur pour agir avec
        self.script_actuel = open(script,r,0) # Une amélioration peut
        # éventuellement se faire sur le buffering des fichiers. Néanmoins, ce
        # changement n'est pas trivial, complexe et rarement très utile.
        if position :
            """
            Ne se déclenche que si une position particulière est
            précisée : par défaut, la valeur étant None, rien ne se passe et
            le pointeur sur le fichier reste bien à à, position par défaut.
            """
            self.script_actuel.seek(position) # Placement du pointeur
        self.table = {script : {}}
        """
        Dictionnaire de dictionnaires : il contient les
        identificateurs retenus et leur position, rangés par fichier
        Le hachage automatique des dictionnaires en python permet une
        meilleure performance de ce type de fonctions
        """
        self.choix = [] # Liste changeable, contient la position des choix d'une
        # action sur l'autre pour être lue

    def suivant(self) -> None:
        """
        Lit la ligne suivante et analyse le texte.
        Fonction principale du parser, elle est appelée par le moteur de jeu
        pour passer au suivant.
        Préconditions :
            Existence d'un scipt valide depuis lequel lire dans
                self.script_actuel
            Existence d'un moteur vers lequel faire les appels dans self.moteur
            Paramètres : Aucun
        Postconditions :
            Avancée du pointeur du fichier jusqu'à la prochaine ligne en
            attente, et appels au moteur de jeu en fonction de ce qui a été lu.
            En fonction des lectures peuvent être faits :
                - Des ajouts à la table
                - Un envoi de choix
                - Un affichage de texte
                - Une modification de paramètres
                - L'arivée à une fin
            Et toutes les autres possibilités de contrôle précisées pour le
            VNMD.
        """
        # caractère = self.script_actuel.read(1)
        pass

    def choix(self, choix: int = None) -> None:
        pass
