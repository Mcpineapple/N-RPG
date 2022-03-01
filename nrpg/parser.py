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
