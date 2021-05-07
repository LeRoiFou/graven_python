"""
Exercice : Jour Jour 18/30 - Python n°5 - Machine à laver
Lien : https://www.youtube.com/watch?v=HfS6XRfvd9Y&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=18

Contexte du jeu :
Vous venez d'acheter une machine à laver dans votre magasin
Elle possède une capacité de 8 kg et possède une vitesse de 1 400 tours minutes et nécessite
35 minutes pour un lavage complet

Fonction prédéfinie ceil du module math utilisé pour les arrondis
Fonction prédéfinie sleep du module time pour générer un temps d'attente

Éditeur : Laurent REYNAUD
Date : 06-05-21
"""
import math
import time

def demarrer_machine(poids_kg):
	# fonction pour démarrer la machine à laver

	print(f"On essaye de démarrer la machine avec {poids_kg} kg")

	# créer une variable pour stocker le temps par défaut de la machine
	duree_machine = 5

	# créer une variable pour stocker le nombre de tours de la machine
	compteur_tours = 0

	# boucle tant que la machine n'est pas arrivée à 0
	while duree_machine > 0 :
		print(f"Duree_machine : reste {duree_machine} min")
		# incrémentations
		duree_machine -= 1
		compteur_tours += 1_400
		# attendre 1 seconde avant de relancer le tour
		time.sleep(1)

	# afficher nombre de tours minutes
	print(f"Nombre de tours de la machine : {compteur_tours} tours")


# afficher un message dans la console
print("Ouverture de la machine à laver")

# demander le poids en kg
try:
	kg = float(input("Quel est le poids total en kg de votre linge à laver ? "))
	print(f"Vous avez {kg} kg de vêtements")

	# calculer combien de machines à utiliser (arrondi avec la fonction ceil du module math)
	machines = math.ceil(kg / 8)
	print(f"Nombre de machines à utiliser : {machines}")
 	
	# calculer la consommation d'eau
	consommation_eau = machines * 60
	print(f"La consommation d'eau pour {machines} machine(s) est de {consommation_eau} L")

	# appel de la fonction
	demarrer_machine(kg)

except ValueError:
	# si la valeur saisie n'est pas un entier
	print("Vous devez entrer un nombre")