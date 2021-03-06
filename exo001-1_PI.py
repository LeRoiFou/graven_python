"""
Exercice : JOUR 1/30 - Exo Python 1 - Les Jarres Magique
Lien : https://www.youtube.com/watch?v=CqJ13Op3_PE&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI

Dans ce programme on a recours uniquement à la programmation impérative
L'objet du jeu est de choisir au hasard 5 jarres et dans l'une d'elles il y a un serpent.
Lorsque joueur tombe sur une jarre où il n'y a pas de serpent, il gagne une clé.
Au bout de 3 clés gagnées, le joueur a terminé le jeu

Éditeur : Laurent REYNAUD
Date : 19-04-2021
"""

import random

print("Bienvenue dans le jeu !")

# compteur de clés magiques : le joueur n'a pas de clé
keys = 0

# répétition des manches de notre jeu
while keys != 3 :
	print("Vous disposez de 5 jarres devant vous.\nChoisis : 1, 2, 3, 4 ou 5")

	# choix aléatoire de la jarre qui fait perdre notre joueur
	snake_jar = random.randint(1, 5)

	# demande à notre joueur de mettre une valeur
	choix = int(input())
	print(f"Le joueur a mis la jarre n° {choix}")

	# vérification
	if choix != snake_jar :
		print("Gagné ! Tu obtiens une clé magique !")
		print(f"Le serpent était dans la jarre n° {snake_jar}")
		keys += 1
		print(f"Tu as actuellement {keys}/3 clés")
	else:
		print("Perdu ! Un serpent apparaît !")
		# si le joueur n'a pas de clé :
		if keys > 0 :
			keys -= 1
			print(f"Tu as actuellement {keys}/3 clés")

print("\nTu deviens le roi du temple !")