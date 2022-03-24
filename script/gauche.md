$couloir1 char= bg=couloirtournantdroit music=suspense
Vous avancez dans le couloir sombre. Devant vous se trouve un tournant vers la
 droite.
- Tourner
=

$couloir2 bg=couloirporte
Vous continuez à avancer.
Devant vous se trouve une porte en acier fermée.

- Pousser la porte
=

<caserne1 Vous arrivez dans une salle carbonisée, vous y voyez différents ensembles de ce qui semble avoir été une caserne. Vous voyez un cadavre de soldat au milieu de la pièce.

$caserne1 bg=caserne
{caserne1}
- Inspecter le corps
=corps
- Continuer
=caserne2

<corps Vous examinez le corps du militaire, il serre un paquet dans ses bras.

$corps bg=corps
{corps}
- Prendre le paquet
=explosifs
- Ne pas continuer
=caserne2

<explosifs Vous récupérez le paquet, il contient des explosifs. Cependant, vous ne savez pas comment ils pourraient vous être utiles.

$explosifs
{explosifs}
- Examiner l'insigne
=insigne

<insigne Vous examinez l'insigne du militaire, il ne vous dit absolument rien.

$insigne bg=insigne
{insigne}
- Continuer
=caserne2

<caserne2 La clé du mystère n'est pas ici, il faut continuer

$caserne2 bg=caserne
{caserne2}
- Prendre la porte à droit
=réacteur
- Prendre la porte droit devant
=derniercouloirgauche


<couloirréacteur1 Devant vous s'étend un couloir avec une porte à la fin

$couloirréacteur1 bg=couloirporte
{couloirréacteur1}
- Pousser la porte
=réacteur

<réacteur Vous arrivez dans une grande salle circulaire avec un gigantesque puits, un trou au plafond a laissé filtrer l'air et la pluie. Vous apercevez de la mousse aux abords du puits.
$réacteur bg=réacteur music=calm
{réacteur}
- Regarder au fond du réacteur
=Freefall
- Continuer
=couloirréacteur2

$Freefall bg=noir
En vous rapprochant du puits du réacteur pour contempler ce qu'il y a au fond,
 vous glissez sur la mousse environnant le puits.
 Vous mourrez après la meilleure expérience de chute libre de votre vie (et la plus courte).

| Freefall

<couloirréacteur2 Vous arrivez dans un couloir sombre avec une porte au bout.

$couloirréacteur2 bg=couloirporte music=suspense
{couloirréacteur2}
- Pousser la porte
=lab1

$lab1 bg=lab
Vous arrivez dans ce qui semble être un laboratoire désaffecté.
Sur le mur de droite se trouvent des cylindres brillants remplis d'un fluide vert dans
 lequel baignent d'étranges créatures.
- Continuer
=lab2
- Regarder une créature
=créature1

$créature1
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. Trouvée non loin du nid de la créature #3188
 forme non constante, aucun organe repéré. Composée d'une "espèce de plasma noir"
 selon le docteur Jeff O'Hale, responsable de la créature #3188 et affiliés"
- Arrêter de lire
=lab2
- Lire le suivant
=créature2

$créature2
Vous lisez l'entrée située en dessous du tube, Il est écrit:
"Spécimen de la créature #3188bis. On remarque chez ce spécimen une forme ovale
 particulière, rappelant la poire. Cette forme a été acquise suite à un morceau de
 nourriture qui a été posé au dessus d'elle. Cette expérience montre la flexibilité
 des créatures #3188."
- Arrêter de lire
=lab2
- Lire le suivant
=créature3

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
=lab2

<lab2 La réponse ne se trouve pas ici, il faut avancer. Il ne reste qu'une porte devant vous.

$lab2 bg=lab
{lab2}
- Passer la porte
=derniercouloirdroit

<derniercouloirdroit Vous arrivez dans un couloir avec un tournant à gauche au bout.
$derniercouloirdroit bg=couloirtournantgauche
{derniercouloirdroit}
- Prendre le tournant
=sas

<derniercouloirgauche Vous arrivez dans un couloir avec un tournant à gauche au bout.

$derniercouloirdroit bg=couloirtournantgauche
{derniercouloirgauche}
- Prendre le tournant
=sas

<sas Vous arrivez devant une grande porte en acier entrouverte avec un bouton à gauche.

$derniercouloirgauche1 bg=couloirtournantdroit
Vous arrivez dans un couloir avec un tournant à gauche
- Prendre le tournant
=sas

$sas bg=sas
{sas}
- Appuyer sur le bouton
=ouverture
- Se faufiler
=cellule

$ouverture
Vous appuyez sur le bouton, la porte s'ouvre doucement avec un grand fracas.
- Entrer
=cellulebout

<cellule Vous entrez dans la cellule, devant vous se trouve un cube en béton avec une étrange créature noire

$cellule bg=cellule char= music=
{cellule}
- L'observer
=créature
- S'enfuir
=fuite1

$cellulebout bg=cellule char= music=
{cellule}
- L'observer
=créature
- S'enfuir
=fuite1bout

$créature char=créature
...
>AUUUUUUUUGHHHHHH

$dévoré bg=noir
La créature va plus vite que vous et vous rattrape, vous sentez votre corps se faire
 dissoudre dans le plasma noir qui forme le corps de la créature.

| Dévoré

<fuite1 Vous commencez à courir alors que vous entendez la créature se lever et crier et commencer à vous poursuivre

$fuite1 bg=entrée music=fuite
{fuite1}
- Revenir sur vos pas
=fuite2droite

$fuite1bout bg=entrée music=fuite
{fuite1}
- Revenir sur vos pas
=fuite2droitebout

<fuite2 vous courez alors que la créature se lance à vos trousses

$fuite2droite bg=couloirtournantdroit
{fuite2}
- Prendre le tournant
=fuite3droite

$fuite2droitebout bg=couloirtournantdroit
{fuite2}
- Prendre le tournant
=fuite3droitebout

<fuite3 Vous continuez en direction de la porte devant vous

$fuite3droite bg=couloirporte
{fuite3}
- Pousser la porte
=lab1fuite

$fuite3droitebout bg=couloirporte
{fuite3}
- Pousser la porte
=lab1fuitebout

<lab1fuite Vous entrez dans le laboratoire.

$lab1fuite bg=lab
{lab1fuite}
- Continuer
=lab2fuite

$lab1fuitebout bg=lab
{lab1fuite}
- Continuer
=lab2fuitebout

<lab2fuite Vous continuez à courir à travers le laboratoire

$lab2fuite
{lab2fuite}
- Continuer tout droit
=dévoré
- aller à droite
=couloirréacteurfuite1


$labfuitebout
{lab2fuite}
- Continuer tout droit
=dévoré
- Aller à droite
=couloirfréacteuruite1bout

<couloirréacteurfuite1 Vous courez en direction du réacteur

$couloirréacteurfuite1 bg=couloirporte
{couloirréacteurfuite1}
- Vousser la porte
=réacteurfuite

$couloirréacteurfuite1bout bg=couloirporte
{couloirréacteurfuite1}
- Pousser la porte
=réacteurfuitebout

<réacteurfuite Vous arrivez devant le puits du réacteur, la créature se rapproche, vous n'êtes pas sûr d'avoir le temps de faire le tour du puits

$réacteurfuite bg=réacteur
{réacteurfuite}
- Faire le tour
=couloirréacteur2fuite
- Tenter de sauter au dessus du puits
=freefall2

$réacteurfuitebout bg=réacteur
{réacteurfuite}
- Faire le tour
=couloirréacteur2fuitebout
- Tenter de sauter au dessus du puits
=freefall2

$freefall2 bg=noir
Vous menez la créature au puit du réacteur et l'entrainez dedans,
 malheureusement vous tombez aussi. "Au moins j'ai sauvé la ville" est votre dernière pensée.
 Vous mourez après la meilleure expérience de chute libre de votre vie (très courte).
| Freefall 2

<couloirréacteur2fuite Vous arrivez juste à temps à traverser la salle. Vous arrivez maintenant dans le couloir menant au laboratoire

$couloirréacteur2fuite bg=couloirporte
{couloirréacteur2fuite}
- Pousser la porte
=caserne1fuite

$couloirréacteur2fuitebout bg=couloirporte
{couloirréacteur2fuite}
- Pousser la porte
=caserne1fuitebout

<caserne1fuite Vous entrez dans la caserne, alors que la créature continue à vous poursuivre.

$caserne1fuite bg=caserne1
{caserne1fuite}
- Continuer
=caserne2

$caserne1fuitebout bg=caserne1
{caserne1fuite}
- Continuer
=caserne2bout

<caserne2fuite vous continuez à courir à travers la caserne.

$caserne2fuite
{caserne2fuite}
- Prendre la porte à droite
=derniercouloirfuite1

$caserne2fuitebout
{caserne2fuite}
- Prendre la porte à droite
=derniercouloirfuite1

<derniercouloirfuite1 Vous continuez à courir dans le couloir, vous serez bientôt dehors.

$derniercouloirfuite1 bg=couloirtournantgauche
{derniercouloirfuite1}
- Tourner
=derniercouloirfuite2

$derniercouloirfuite1bout bg=couloirtournantgauche
{derniercouloirfuite1}
- Tourner
=derniercouloirfuite2bout

<derniercouloirfuite2 Vous arrivez proche de la dernière échelle. Vous y êtes presque.

$derniercouloirfuite2
{derniercouloirfuite2}
- Gravir l'échelle
=sortie

$derniercouloirfuite2bout
{derniercouloirfuite2}
- Gravir l'échelle
=proposition

$sortie bg=hill
Vous vous précipitez à l'extérieur, Bert est assis sur une souche non loin
- Le prévenir
=Bert1
- S'enfuir seul
=choixfuite

$Bert1 char=Bert
Qu'est ce qu'il y a patron? Oh mon Dieu... qu'est ce que c'est que ce truc?!

$ char=
Bert monte dans la voiture
- Le suivre
=fuite
- Fuir par la forêt
=siproche

$fuite music=calm bg=noir
Vous et Bert vous enfuyez en prévenant le central, la créature arrête de vous 
 poursuivre. Le lendemain, des militaires sont sur la zone.
| Fuite

$choixfuite
Vous courez à toute vitesse
- Prendre la voiture
=amiabandonné
- Fuir par la forêt
=siproche

$amiabandonné music= bg=noir
Vous fuyez en voiture sans demander votre reste et voyez Bert se faire dévorer
 vivant par la créature. Le lendemain, des militaires sont sur la zone.
| Ami Abandonné

$siproche music=fuite bg=noir
Vous décidez de vous enfuir à travers la forêt, vous trébuchez sur une racine 
 et la créature vous rattrape. Vous sentez votre corps se faire dissoudre dans
 le plasma noir qui forme le corps de la créature.
| Si Proche

$proposition bg=hill music=calm
Vous sortez du complexe, au moment où vous sortez, des militaires rentrent. 
Un homme s'approche de vous.

$ char=McTharney
Bonjour, je me nomme John McTharney, je suis agent de l'Agence Mondiale
d'Exploration et de Neutralisation de l'Occulte ou AMENO. Lorsque vous avez 
réactivé les mécanismes de cette base, nous avons été prévenus et nous sommes
rendus sur les lieux au plus vite.

$
Vous avez découvert ici un spécimen Top secret que l'on croyait disparu. Par
conséquent, Nous ne pouvons pas vous laisser gambader avec de telles informations.
Que diriez-vous donc, vous et votre adjoint de nous rejoindre?
- Refuser
=Elimination
- Accepter
=Recruté

$Elimination char=McTharney
Je vois, après tout, nous ne pouvons pas vous forcer.
>Au revoir, Shériff.

$ char= music= bg=noir
Bert se fait escorter vers un fourgon, McTharney sort un browning et fait feu.
| Eliminé

$Recruté char=McTharney bg=noir
Parfait, nous allons vous faire subir une formation intensive pendant les mois
 suivants. Vous partez tout de suite, désolé mais vous ne pourrez pas faire vos
 adieux.
| Recruté
