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

|Freefall 

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

|Dévoré

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

- revenir sur vos pas
=fuite2droitebout

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

- prendre la porte de gauche

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

- prendre la porte de gauche

=couloirréacteurfuite1bout

$caserne2fuitelogsbout
{caserne2fuite}
- prendre la porte droit devant
=dévoré

- prendre la porte de gauche

=couloirréacteurfuite1logsbout

<couloirréacteurfuite1 Vous courez en direction du réacteur

$couloirréacteurfuite1 bg=couloirporte
{couloirréacteurfuite1}

- pousser la porte
=réacteurfuite

$couloirréacteurfuite1logs bg=couloirporte
{couloirréacteurfuite1}

- pousser la porte
=réacteurfuitelogs

$couloirréacteurfuite1bout bg=couloirporte
{couloirréacteurfuite1}

- pousser la porte
=réacteurfuitebout

$couloirréacteurfuite1logsbout1 bg=couloirporte
{couloirréacteurfuite1}

- pousser la portelogsbout
=réacteurfuitelogsbout

<réacteurfuite Vous arrivez devant le puits du réacteur, la créature se rapproche, vous n'êtes pas sûr d'avoir le temps de faire le tour du puits

$réacteurfuite bg=réacteur
{réacteurfuite}

- faire le tour
=couloirréacteur2fuite

- tenter de sauter au dessus du puits
=freefall2

$réacteurfuitelogs bg=réacteur
{réacteurfuite}

- faire le tour
=couloirréacteur2fuitelogs

- tenter de sauter au dessus du puits
=freefall2

$réacteurfuitebout bg=réacteur
{réacteurfuite}

- faire le tour
=couloirréacteur2fuitebout

- tenter de sauter au dessus du puits
=freefall2

$réacteurfuitelogsbout bg=réacteur
{réacteurfuite}

- faire le tour
=couloirréacteur2fuitelogsbout

- tenter de sauter au dessus du puits
=freefall2

$freefall2
Vous menez la créature au puit du réacteur et l'entrainez dedans, 
 malheureusement vous tombez aussi, "Au moins j'ai sauvé la ville" est votre dernière pensée.
 Vous mourez après la meilleure expérience de chute libre de votre vie (très courte).
|Freefall 2

<couloirréacteur2fuite Vous arrivez juste à temps à traverser la salle. Vous arrivez maintenant dans le couloir menant au laboratoire

$couloirréacteur2fuite bg=couloirporte
{couloirréacteur2fuite}

- pousser la porte
=lab1fuite

$couloirréacteur2fuitelogs bg=couloirporte
{couloirréacteur2fuite}

- pousser la porte
=lab1fuitelogs

$couloirréacteur2fuitebout bg=couloirporte
{couloirréacteur2fuite}

- pousser la porte
=lab1fuitebout

$couloirréacteur2fuitelogsbout bg=couloirporte
{couloirréacteur2fuite}

- pousser la porte
=lab1fuitelogsbout

<lab1fuite Vous entrez dans le laboratoire.

$lab1fuite bg=lab
{lab1fuite}

- continuer
=lab2fuite

$lab1fuitebout bg=lab
{lab1fuite}

- continuer
=lab2fuitebout

$lab1logs bg=lab
{lab1fuite}
>{opportunité}

- lancer les explosifs
=mort

- continuer
=lab2fuite

$lab1logsbout
{lab1fuite}
>{opportunité}

- lancer les explosifs
=mortbout

- continuer
=lab2fuitebout

<mort La créature s'enflamme et se consume dans des râles d'agonie. Vous et la ville êtes saufs.
$mort
{mort}
- sortir
=purifiéparlefeu

$mortbout
{mort}
- sortir
=proposition

$purifiéparlefeu bg=hill
Vous sortez du complexe rempli de soulagement, vous choisissez
 de ne pas raconter l'histoire à Bert, il ne vous croirai pas.
 Cependant, les disparitions cessent, tout le monde va bien.
|Purifié par le feu

<lab2fuite Vous continuez à courir à travers le laboratoire

$lab2fuite
{lab2fuite}

- pousser la porte
=derniercouloirfuite1

$labfuitebout
{lab2fuite}
- pousser la porte
=derniercouloirfuite1bout

<derniercouloirfuite1 Vous continuez à courir dans le couloir, vous serez bientôt dehors.

$derniercouloirfuite1 bg=couloirtournantdroit
{derniercouloirfuite1}
- tourner
=derniercouloirfuite2

$derniercouloirfuite1bout bg=couloirtournantdroit
{derniercouloirfuite1}
- tourner
=derniercouloirfuite2bout

<derniercouloirfuite2 Vous arrivez proche de la dernière échelle. Vous y êtes presque.

$derniercouloirfuite2
{derniercouloirfuite2}
- gravir l'échelle
=sortie

$derniercouloirfuite2bout
{derniercouloirfuite2}
- gravir l'échelle
=proposition

$sortie bg=hill
Vous vous précipitez à l'extérieur, Bert est assis sur une souche non loin
- le prévenir
=Bert1
- s'enfuir seul
=choixfuite

$Bert1 char=Bert
Qu'est ce qu'il y a patron? Oh mon Dieu... qu'est ce que c'est que ce truc?!

$ char=
Bert monte dans la voiture
- le suivre
=fuite
-fuir par la forêt
=siproche

$fuite music=calm
Vous et Bert vous enfuyez en prévenant le central, la créature arrête de vous 
 poursuivre. Le lendemain, des militaires sont sur la zone.
|Fuite

$choixfuite
Vous courez à toute vitesse
- prendre la voiture
=amiabandonné
- fuir par la forêt
=siproche

$amiabandonné music=sad
Vous fuyez en voiture sans demander votre reste et voyez Bert se faire dévorer
 vivant par la créature. Le lendemain, des militaires sont sur la zone.
|Ami Abandonné

$siproche
Vous décidez de vous enfuir à travers la forêt, vous trébuchez sur une racine 
 et la créature vous rattrape. Vous sentez votre corps se faire dissoudre dans
 le plasma noir qui forme le corps de la créature.
|Si Proche

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

$ char= music=
Bert se fait escorter vers un fourgon, McTharney sort un browning et fait feu.
|Eliminé

$Recruté char=McTharney
Parfait, nous allons vous faire subir une formation intensive pendant les mois
 suivants. Vous partez tout de suite, désolé mais vous ne pourrez pas faire vos
 adieux.
|Recruté