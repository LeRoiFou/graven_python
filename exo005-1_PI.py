"""
Exercice : Jour 29/30 - Python n° 8 - Jeu du juste prix (avec tkinter)
Lien : https://www.youtube.com/watch?v=IQtAfooLsJA&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=29

Contexte du jeu :
Deviner un prix ;)

Recours ici aux instructions suivantes :
-> 'break' qui permet de casser une boucle

Éditeur : Laurent REYNAUD
Date : 08-05-21
"""

import random
import time

# afficher un message de bienvenue
print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense,\
 il se situe entre 1 et 100")

# assignation de variables
nombre_hasard = random.randint(1, 100)
proposition = 0
tentatives = 10
temps = time.time()
tic_tac = 60

# boucler tant que...
while proposition != nombre_hasard and tentatives > 0 :

	# proposer au joueur d'entrer une proposition
	proposition = int(input("Entrer votre proposition : "))

	# vérifier si le temps n'est pas dépassé
	temps_passe = time.time() - temps
	print(f"{round(temps_passe, 2)} secondes")

	if temps_passe >= tic_tac:
		print("Temps écoulé !")
		break
	
	# vérifier le nombre de la proposition <-> au nombre à trouver
	if proposition < nombre_hasard:
		print("C'est plus")
	elif proposition > nombre_hasard:
		print("C'est moins !")

	# incrémentation du nombre de tentatives
	tentatives -= 1
	print(tentatives)

if tentatives == 0 :
	print(f"C'est perdu ! Trop de tentatives, le nombre à trouver était le {nombre_hasard}")
elif temps_passe >= tic_tac:
	pass
else:
	print("Trouvé !")