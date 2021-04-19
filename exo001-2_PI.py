"""
Exercice : JOUR 1/30 - Exo Python 1 - Les Jarres Magique
Lien : https://www.youtube.com/watch?v=CqJ13Op3_PE&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI

Dans ce programme on a recours uniquement à la programmation impérative
L'objet du jeu est de choisir au hasard 5 jarres et dans l'une d'elles il y a un serpent.
Lorsque joueur tombe sur une jarre où il n'y a pas de serpent, il gagne une clé.
Au bout de 3 clés gagnées, le joueur a terminé le jeu

En complément avec l'autre exercice, cette fois-ci le joueur peut choisir son niveau de difficulté.
Niveau 1 : il n'y a qu'un serpent sur les 5 jarres
Niveau 2 : il y a deux serpents sur les 5 jarres
Niveau 3 : il y a trois serpents sur les 5 jarres

Dans ce programme, on a recours à une compréhension de liste ;)

Éditeur : Laurent REYNAUD
Date : 19-04-2021
"""

import random

print("Bienvenue dans le jeu !")

# choix du paramétrage/niveau de difficulté
level = int(input("Ecris 1: facile, 2: moyen, 3: difficile\n"))

# compteur de clés magiques : le joueur n'a pas de clé
keys = 0

# répétition des manches de notre jeu
while keys != 3 :
	print("\nVous disposez de 5 jarres devant vous.\nChoisis : 1, 2, 3, 4 ou 5")

	# niveau 1 donc une liste avec 1 composant (1 serpent), niveau 2 donc une liste avec 2 composants (2 serpents)...
	jars = ['S' for x in range(level)]
	# niveau 1 : différence = 5 - 1 = 4, niveau 2 : différence = 5 - 2 = 3
	difference = 5 - level
	# niveau 1 donc une liste de 4 composants (4 clés), niveau 2 donc une liste de 3 composants (3 clés)...
	trousseaux = ['K' for x in range(difference)]
	# rajout de la liste keys à la liste jars
	jars.extend(trousseaux)
	# mélange des jars
	random.shuffle(jars)

	# demande à notre joueur de mettre une valeur
	choix = int(input())
	print(f"\nLe joueur a mis la jarre n° {choix}")

	# vérification
	if jars[choix-1] == "K" :
		print("Gagné ! Tu obtiens une clé magique !")
		# print(f"Le serpent était dans la jarre n° {snake_jar}")
		keys += 1
		print(f"Tu as actuellement {keys}/3 clés\n")
	else:
		print("Perdu ! Un serpent apparaît !")
		# si le joueur n'a pas de clé :
		if keys > 0 :
			keys -= 1
			print(f"Tu as actuellement {keys}/3 clés\n")

print("Tu deviens le roi du temple !")