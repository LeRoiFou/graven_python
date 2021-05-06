"""
Exercice : Jour 12/30 - Exo Python 4 - Gestion d'un parking
Lien : https://www.youtube.com/watch?v=m96VEV7MeZQ&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=12

Contexte du jeu :
Vous êtes le gérant d'un parking commercial comportant actuellement 27 emplacements pour accueillir les véhicules
clients du centre commercial

Dans ce programme on a recours à de la programmation impérative et à de la programmation procédurale

Éditeur : Laurent REYNAUD
Date : 26-04-21
"""

def afficher_parking():
	 # fonction permettant d'afficher le statut de chaque emplacmeent (D = Disponible / V = Véhicule à l'emplacement)
	
	"""recours à une condition 'ternaire' qui va parcourir chaque emplacement pour afficher la disponibilité :
	Cette instruction est effectuée de la manière suivante :
	nom_variable = (condition_faux, condition_vrai)[condition à vérifier]"""
	for place_parking in parking:
		resultat = ("Non disponible", "Disponible")[place_parking == 'D']
		print(resultat)
	"""qui équivaut à la boucle suivante :
		if place_parking == 'D':
			print("Disponible")
		else:
			print("Non disponible")"""

# afficher une message de bienvenue
print("Bienvenue au niveau -1, que souhaitez-vous faire ?")

# création d'une compréhension de liste de 27 places disponibles dans le parking (D)
emplacements = 27
parking = ['D' for x in range(emplacements)]

# garer une voiture au 1er emplacement (indice n° 0) = 'V' (place prise)
parking[0] = 'V'

# appel de la fonction
afficher_parking()

# proposer à notre client de faire une action
print("1: Garer une voiture\n2: Récupérer une voiture")
choix = int(input())

# vérifier le choix
if choix == 1:
	print("Vous avez choisi de garer une voiture, à quel emplacement souhaitez-vous la mettre ?")
	choix_emplacement = int(input()) - 1

	# vérifier si la place choisie se trouve dans le nombre de composants de la liste
	if 0 <= choix_emplacement <= len(parking):

		# vérifier si la place est disponible
		if parking[choix_emplacement] == 'D':
			print(f"Vous avez pris la place n° {choix_emplacement + 1}")
			# la place n'est plus disponible
			parking[choix_emplacement] = 'V'
		else:
			print("Emplacement non disponible")

elif choix == 2:
	print("Récupérer une voiture")
	choix_emplacement = int(input("N° d'emplacement svp : ")) - 1

	# vérifier si la place choisie se trouve dans le nombre de composants de la liste
	if 0 <= choix_emplacement <= len(parking):

		# vérifier si la place est occupée
		if parking[choix_emplacement] == 'V':
			print("Véhicule récupéré")
			# la place redevient disponible
			parking[choix_emplacement] = 'D'
			print(f"L'emplacement n° {choix_emplacement + 1} est à nouveau disponible")
		else:
			print(f"Oh oh... il n'y a pas de véhicule à l'emplacement n° {choix_emplacement + 1} :(")

else:
	print("Erreur, vous devez écrire 1 ou 2")

# appel de la fonction
afficher_parking()