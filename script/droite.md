$couloir1 char= bg=couloirtournantgauche music=suspense
Vous avancez dans le couloir sombre. Devant vous se trouve un tournant vers la gauche.
- Tourner
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

<explosifs vous récupérez le paquet, il contient des explosifs.
$explosifs
{explosifs} Cependant, vous ne savez pas comment ils pourraient vous être utiles
- continuer
=caserne2

$explosifslogs
{explosifs} Vous apercevez un insigne étrange sur l'uniforme du militaire.
- examiner l'insigne
=insigne

<insigne vous examinez l'insigne du militaire, il ne vous dit absolument rien.


$insigne bg=insigne
{insigne}
- continuer
=caserne2logs

<caserne2 La clé du mystère n'est pas ici, il faut continuer

$caserne2 bg=caserne
{caserne2}
- prendre la porte droit devant
=derniercouloirgauche

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
- prendre le tournant
=sas

$derniercouloirgauchelogs bg=couloirtournantdroit
{derniercouloirgauche}
- prendre le tournant
=saslogs

<sas Vous arrivez devant une grande porte en acier entrouverte avec un bouton à gauche.

$sas bg=sas
{sas}
- appuyer sur le bouton
=ouverture
- se faufiler
=cellule

$saslogs bg=sas
{sas}
- appuyer sur le bouton
=ouverturelogs
- se faufiler
=cellulelogs

<ouverture Vous appuyez sur le bouton, la porte s'ouvre doucement avec un grand fracas.

$ouverture
{ouverture}
- entrer
=cellulebout

$ouverturelogs
{ouverture}
- entrer
=cellulelogsbout

<cellule Vous entrz dans la cellule, devant vous se trouve un cube en béton avec une étrange créature noire

$cellule bg=cellule char= music=
{cellule}
- l'observer
=créature
- s'enfuir
=fuite1

$cellulelogs bg=cellule char= music=
{cellule}
- l'observer
=créature
- s'enfuir
=fuite1logs

$cellulebout bg=cellule char= music=
{cellule}
- l'observer
=créature
- s'enfuir
=fuite1bout

$cellulelogsbout bg=cellule char= music=
{cellule}
- l'observer
=créature
- s'enfuir
=fuite1logsbout

$créature char=créature
...
>AUUUUUUUUGHHHHHH

$dévoré
La créature va plus vite que vous et vous rattrape, vous sentez votre corps se faire
 dissoudre dans le plasma noir qui forme le corps de la créature.
|Fin échouée: Dévoré

<fuite1 Vous commencez à courir alors que vous entendez la créature se lever et crier et commencer à vous poursuivre

$fuite1 bg=entrée music=fuite
{fuite1}
- aller à droite
=fuite2droite
- aller à gauche
=fuite2gauche

$fuite1logs bg=entrée music=fuite
{fuite1}
- aller à droite
=fuite2droitelogs
- aller à gauche
=fuite2gauchelogs

$fuite1bout bg=entrée music=fuite
{fuite1}
- aller à droite
=fuite2droitebout
- aller à gauche
=fuite2gauchebout

$fuite1logsbout bg=entrée music=fuite
{fuite1}
- aller à droite
=fuite2droitelogsbout
- aller à gauche
=fuite2gauchelogsbout

<fuite2 vous courez alors que la créature se lance à vos trousses

$fuite2droite bg=couloirtournantgauche
{fuite2}
- prendre le tournant
=fuite3droite
$fuite2droitelogs bg=couloirtournantgauche
{fuite2}
- prendre le tournant
=fuite3droitelogs

$fuite2droitebout bg=couloirtournantgauche
{fuite2}
- prendre le tournant
=fuite3droitebout
$fuite2droitelogsbout bg=couloirtournantgauche
{fuite2}
- prendre le tournant
=fuite3droitelogsbout

<fuite3 Vous continuez en direction de la porte devant vous

$fuite3droite bg=couloirporte
{fuite3}
- pousser la porte
=casernefuite1

$fuite3droitelogs bg=couloirporte
{fuite3}
- pousser la porte
=casernefuite1logs

$fuite3droitebout bg=couloirporte
{fuite3}
- pousser la porte
=casernefuite1bout

$fuite3droitelogsbout bg=couloirporte
{fuite3}
- pousser la porte
=casernefuite1logsbout

<caserne1fuite Vous entrez dans la caserne, alors que la créature continue à vous poursuivre.
<opportunité Vous voyez une chance pour lancer les explosifs.

$caserne1fuite bg=caserne1
{caserne1fuite}
- continuer
=caserne2

$caserne1fuitebout bg=caserne1
{caserne1fuite}
- continuer
=caserne2bout

$caserne1fuitelogs bg=caserne1
{caserne1fuite}
>{opportunité}
- continuer
=caserne2fuitelogs
- lancer les explosifs
=mort

$caserne1fuitelogsbout bg=caserne1
{caserne1fuite}
>{opportunité}
- continuer
=caserne2fuitelogsbout
- lancer les explosifs
=mortbout

<caserne2fuite vous continuez à courir à travers la caserne.

$caserne2fuite
{caserne2fuite}
- prendre la porte droit devant
=dévoré
-prendre la porte de gauche
=couloirréacteurfuite1

$caserne2fuitelogs
{caserne2fuite}
- prendre la porte droit devant
=dévoré
-prendre la porte de gauche
=couloirréacteurfuite1logs

$caserne2fuitebout
{caserne2fuite}
- prendre la porte droit devant
=dévoré
-prendre la porte de gauche
=couloirréacteurfuite1bout

$caserne2fuitelogsbout
{caserne2fuite}
- prendre la porte droit devant
=dévoré
-prendre la porte de gauche
=couloirréacteurfuite1logsbout

<couloirréacteurfuite1
