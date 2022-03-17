$couloir1 char= bg=couloirtournantgauche music=suspense
Vous avancez dans le couloir sombre. Devant vous se trouve un tournant vers la gauche.
- tourner
=

$couloir2 bg=couloirporte
Vous continuez à avancer.
Devant vous se trouve une porte en acier fermée.

- Pousser la porte
=

$lab1 bg=lab
Vous arrivez dans ce qui semble être un laboratoire désaffecté.
Sur le mur de droite se trouvent des cylindres brillants remplis d'un fluide vert dans
 lequel baignent d'étranges créatures.
- Continuer
=lab2
- Regarder une créature
=

$créature1
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. Trouvée non loin du nid de la créature #3188
 forme non constante, aucun organe repéré. Composée d'une "espèce de plasma noir"
 selon le docteur Jeff O'Hale, responsable de la créature #3188 et affiliés"

- Arrêter de lire
=lab2
- Lire le suivant
=

$créature2
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. On remarque chez ce spécimen une forme ovale
 particulière, rappelant la poire. Cette forme a été acquise suite à un morceau de
 nourriture qui a été posé au dessus d'elle. Cette expérience montre la flexibilité
 des créatures #3188."

- Arrêter de lire
=lab2

- Lire le suivant
=

$créature3
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. Le fluide dans lequel elle est conservée se
 trouve être un dérivé du formol, appelé héxacétyloformol, choisi pour ses
 capacités conservatrices. Fait surprenant, les créatures #3188bis semblent
 entrer dans une forme d'hibernation, montrant un organisme complexe, bien
 que difficile à examiner"

- Arrêter de lire
=lab2

- Lire le suivant
=

$créature4
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. Malgré une constitution quasiment
 indestructible, la créature #3188 dispose de 2 points faibles. Le premier est
 la chute, en effet quelques dizaines de mètres de chute sont suffisant pour
 tuer la créature #3188 et associés. Le deuxième est le feu et les explosifs,
 le plasma noir qui compose la créature est très inflammable et réagit
 violemment avec le feu."

- Arrêter de lire
=lab2logs

<lab2 La réponse ne se trouve pas ici, il faut avancer. Il y a deux portes devant vous, laquelle choissisez vous?

$lab2
{lab2}
- Celle de gauche
=couloirréacteur1
- Celle de droite
=derniercouloirgauche1

$lab2logs
{lab2}
- Celle de gauche
=couloirréacteur1logs
- Celle de droite
=derniercouloirdroit

<couloirréacteur1 Devant vous s'étend un couloir avec une porte à la fin

$couloirréacteur1 bg=couloirporte
{couloirréacteur1}
- Pousser la porte
=réacteur

$couloirréacteur1logs bg=couloirporte
{couloirréacteur1}
-pousser la porte
=réacteurlogs

<réacteur Vous arrivez dans une grande salle circulaire avec un gigantesque puits, un trou au plafond a laissé filtrer l'air et la pluie. Vous apercevez de la mousse aux abords du puits.
$réacteur bg=réacteur music=birds
/ Le birds est censé être des chants d'oiseaux au loin
{réacteur}
- Regarder au fond du réacteur
=Freefall
- Continuer
=couloirréacteur2

$réacteurlogs bg=réacteur music=birds
{réacteur}
- Regarder au fond du réacteur
=Freefall
- Continuer
=couloirréacteur2logs

$Freefall bg=puits
En vous rapprochant du puits du réacteur pour contempler ce qu'il y a au fond,
 vous glissez sur la mousse environnant le puits.
 Vous mourrez après la meilleure expérience de chute libre de votre vie (et la plus courte).

|-"Freefall" Freefall

<couloirréacteur2 Vous arrivez dans un couloir sombre avec une porte au bout.

$couloirréacteur2 bg=couloirporte music=suspense
{couloirréacteur2}
- Pousser la porte
=caserne1

$couloirréacteur2logs bg=couloirporte music=suspense
{couloirréacteur2}
- Pousser la porte
=caserne1logs

<caserne1 Vous arrivez dans une salle carbonisée, vous y voyez différents ensembles de ce qui semble avoir été une caserne. vous voyez un cadavre de soldat au milieu de la pièce.

$caserne1
{caserne1}
- Inspecter le corps
=corps
- Continuer
=caserne2

$caserne1logs
{caserne1}
- Inspecter le corps
=corpslogs
- Continuer
=caserne2

<corps vous examinez le corps du militaire, il serre un paquet dans ses bras.

$corps
{corps}

- prendre le paquet
=explosifs

- ne pas continuer
=caserne2

$corpslogs
{corps}

- prendre le paquet
=explosifslogs

- ne pas continuer
=caserne2

<explosifs vous récupérez le paquet, il contient des explosifs, vous apercevez un insigne étrange sur l'uniforme du militaire.

$explosifs
{explosifs}

- examiner l'insigne
=insigne

$explosifslogs
{explosifs}

- examiner l'insigne
=insignelogs

<insigne vous examinez l'insigne du militaire, il ne vous dit absolument rien.

$insigne bg=insigne
{insigne}

- continuer
=caserne2exp

$insignelogs bg=insigne
{insigne}

- continuer
=caserne2logs

<caserne2 La clé du mystère n'est pas ici, il faut continuer

$caserne2 bg=caserne
{caserne2}

- prendre la porte droit devant
=derniercouloirgauche

$caserne2exp bg=caserne
{caserne2}

- prendre la porte droit devant
=derniercouloirgaucheexp

$caserne2logs bg=caserne
{caserne2}

- prendre la porte droit devant
=derniercouloirgauchelogs

$derniercouloirdroit bg=couloirtournantgauche
Vous arrivez dans un couloir avec un tournant à gauche au bout.

- prendre le tournant
=sas

<derniercouloirgauche Vous arrivez dans un couloir avec un tournant à droite au bout.

$derniercouloirgauche bg=couloirtournantdroit
{derniercouloirgauche}

-prendre le tournant
=sas

$derniercouloirgaucheexp bg=couloirtournantdroit
{derniercouloirgauche}

-prendre le tournant
=sasexp

$derniercouloirgauchelogs bg=couloirtournantdroit
{derniercouloirgauche}

-prendre le tournant
=saslogs

<sas Vous arrivez devant une grande porte en acier entrouverte avec un bouton à gauche.

$sas bg=sas
{sas}

-appuyer sur le bouton
=ouverture

-se faufiler
=cellule