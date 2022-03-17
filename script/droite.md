$couloir1 char= bg=couloirtournantgauche music=suspense
Vous avancez dans le couloir sombre. Devant vous, se trouve un tournant vers la 
gauche

-tourner
=

$couloir2 bg=couloirporte
Vous continuez à avancer, devant vous se trouve une porte en acier fermée

-pousser la porte
=

$lab1 bg=lab
Vous arrivez dans ce qui semble être un laboratoire désaffecté, sur le mur de 
droite, se trouve des cylindres brillants remplis d'un fluide vert dans lequel 
baignent  d'étranges créatures noires sphériques.

-continuer
=lab2

-regarder la créature
=

$créature1
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis, trouvée non loin du nid de la créature #3188
forme non constante, aucun organe repéré. Composée d'une "espèce de plasma noir"
selon le docteur Jeff O'Hale, responsable de la créature #3188 et affiliés"

-arrêter de lire
=lab2

-lire le suivant
=

$créature2
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis, on remarque chez ce spécimen une forme ovale
particulière, rappelant la poire. Cette forme a été acquise suite à un morceau de
nourriture qui a été posé au dessus d'elle. Cette expérience montre la flexibilité
des créatures #3188."

-arrêter de lire
=lab2

-lire le suivant
=

$créature3
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis, le fluide dans lequel elle est conservée se
trouve être un dérivé du formol, appelé héxacétyloformol, choisi pour ses 
capacités conservatrices.Fait surprenant, les créatures #3188bis semblent
entrer dans une forme d'hibernation, montrant un organisme complexe, bien
que difficile à examiner"

-arrêter de lire
=lab2

-lire le suivant
=

$créature4
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis, malgré une constitution quasiment
indestructible, la créature #3188 dispose de 2 points faibles. Le premier est 
la chute, en effet quelques dizaines de mètres de chute sont suffisant pour
tuer la créature #3188 et associés. Le deuxième est le feu et les explosifs,
le plasma noir qui compose la créature est très inflammable et réagit 
violemment avec le feu."

-arrêter de lire
=lab2logs

<lab2 La réponse ne se trouve pas ici, il faut avancer. Il y a deux portes devant vous, laquelle choissisez vous?

$lab2
{lab2}

-gauche
=couloirréacteur1

-droite
=derniercouloirgauche1

$lab2logs
{lab2}

-gauche
=couloirréacteur1logs

-droite
=derniercouloirgauche1

<couloirréacteur1 Un couloir avec une porte à la fin

$couloirréacteur1 bg=couloirporte
{couloirréacteur1}

-pousser la porte

=réacteur

$couloirréacteur1logs bg=couloirporte
{couloirréacteur1}

-pousser la porte

=réacteurlogs

<réacteur Vous arrivez dans une grande salle circulaire avec un gigantesque puits, un trou au plafond a laissé filtrer l'air et la pluie. Vous apercevez de la mousse aux abords du puits.
$réacteur bg=réacteur music=birds
/le birds est censé être des chants d'oiseaux au loin
{réacteur}

-regarder au fond du réacteur
=Freefall

-continuer
=couloirréacteur2

$réacteurlogs bg=réacteur music=birds
{réacteur}

-regarder au fond du réacteur
=Freefall

-continuer
=couloirréacteur2logs

$Freefalln 
|-"Freefall": En vous rapprochant du puits du réacteur pour contempler ce qu'il y a au fond , vous glissez sur la mousse environnant le puits, vous mourez après la meilleure expérience de chute libre de votre vie (très courte).

<couloirréacteur2 Vous arrivez dans un couloir sombre avec une porte au bout

$couloirréacteur2 bg=couloirporte music=suspense
{couloirréacteur2}

-pousser la porte
=caserne1

$couloirréacteur2logs bg=couloirporte music=suspense
{couloirréacteur2}

-pousser la porte
=caserne1logs

<caserne1 Vous arrivez dans une salle carbonisée, vous y voyez différents ensembles de ce qui semble avoir été une caserne. vous voyez un cadavre de soldat au milieu de la pièce.

$caserne1
{caserne1}

-inspecter le corps
=corps

-continuer
=caserne2

$caserne1logs
{caserne1}

-inspecter le corps
=corpslogs

-continuer
=caserne2

corps=