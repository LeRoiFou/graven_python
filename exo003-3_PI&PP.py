"""
Exercice : Jour 12/30 - Exo Python 4 - Gestion d'un parking
Lien : https://www.youtube.com/watch?v=m96VEV7MeZQ&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=12

Contexte du jeu :
Vous êtes le gérant d'un parking commercial comportant actuellement 27 emplacements pour accueillir les véhicules
clients du centre commercial

Cette fois-ci il y a pour chaque étages 2 emplacements prioritaires à mobilité réduite('H')
Dans ce programme on a recours à de la programmation impérative et à de la programmation procédurale

Mais également aux expresssions rationnelles pour saisir un code sous format HP-2222-XX pour réserver une 
place prioritaire à mobilité réduite
Documentation sur l'outil regex (module re) : https://www.w3schools.com/python/python_regex.asp
Autre site : https://ihateregex.io/

Éditeur : Laurent REYNAUD
Date : 03-05-21
"""

import random
import string # module pour récupérer des caractères de la table ASCII
import re # expressions rationnelles

def generer_code_debloquage():
	# fonction permettant de générer cette chaîne (code secret) sour le format du code de déblocage : AAAA-2222-XX

	"""
	lien : https://www.askpython.com/python/examples/generate-random-strings-in-python
	récupéré pour effectuer les deux instructions ci-après
	"""
	lettres = string.ascii_letters.upper()  # récupération des lettres en majuscules de la table ASCII
	mot = ''.join(random.choice(lettres) for x in range(4))
	numero = ''.join(str(random.randint(1, 9)) for x in range(4))
	chars = ''.join(random.choice(lettres) for x in range(2))
	code = mot + '-'+ numero + '-' + chars
	print(f"Votre code de débloquage est : {code}")
	return code

def afficher_parking():
	 # fonction permettant d'afficher le statut de chaque emplacmeent (D = Disponible / V = Véhicule à l'emplacement)
	
	for num_etage, etage in enumerate(parking, 1):
		for num_place, place in enumerate(etage, 1):
			resultat = ("Non disponible", "Disponible")[place == 'D']
			resultat = (resultat, "Place réservée")[place == 'H']
			print(f"Etage n° {num_etage} - place n° {num_place} : {resultat}")

# afficher une message de bienvenue
print("Bienvenue au niveau -1, que souhaitez-vous faire ?")

# création d'une compréhension de liste de 27 places disponibles dans le parking de 3 étages (D)
nb_places = 27
nb_etages = 3
parking = [['D' for x in range(nb_places)] for x in range(nb_etages)]

# créer une liste de code à débloquer
code_debloquage = [['.' for x in range(nb_places)] for x in range(nb_etages)]

# générer deux emplacements prioritaires pour chaque étage
for num_etage, etage in enumerate(parking):
	emplacement1_hasard = random.randint(1, len(parking[num_etage]) - 1)
	emplacement2_hasard = random.randint(1, len(parking[num_etage]) - 2)
	parking[num_etage][emplacement1_hasard] = 'H'
	parking[num_etage][emplacement2_hasard] = 'H'

# garer une voiture à l'étage 1 (indice n° 0) au 1er emplacement (indice n° 0) = 'V' (place prise)
parking[0][0] = 'V'

afficher_parking()

# boucle à l'infinie en recourant à l'instruction True
while True:

	# proposer à notre client de choisir un étage
	choix_etage = int(input("Choisissez votre étage : ")) - 1

	# vérifier si l'étage choisi existe
	if 0 <= choix_etage <= len(parking) :
		print(f"Vous avez choisi l'étage n° {choix_etage + 1}")

		# proposer à notre client de faire une action
		print("1: Garer une voiture\n2: Récupérer une voiture")
		choix = int(input())

		# vérifier le choix
		if choix == 1:
			print("Vous avez choisi de garer une voiture, à quel emplacement souhaitez-vous la mettre ?")
			choix_emplacement = int(input()) - 1

			# vérifier si la place choisie se trouve dans le nombre de composants de la liste
			if 0 <= choix_emplacement <= len(parking[choix_etage]):

				# vérifier si l'emplacement est 'H'
				if parking[choix_etage][choix_emplacement] == 'H':
					# demander son code sous le format suivant : HP-1111-XX
					choix_code_h = input("Votre code prioritaire svp : ")
					
					# vérification du code en recourant aux expressions rationnelles
					code = r"^HP-[1-9]{4}-[a-zA-Z]{2}"
					verif = re.search(code, choix_code_h)
					if verif is None:
						print("Vous n'avez pas le bon code")
					else:
						print("C'est ok !")
						print(f"Vous avez pris la place n° {choix_emplacement + 1} à l'étage n° {choix_etage + 1}")
						# la place n'est plus disponible
						parking[choix_etage][choix_emplacement] = 'V'
						# générer le code secret
						code_secret = generer_code_debloquage()
						# affecter le code secret à l'étage / place choisie
						code_debloquage[choix_etage][choix_emplacement] = code_secret

				# vérifier si la place est disponible
				elif parking[choix_etage][choix_emplacement] == 'D':
					print(f"Vous avez pris la place n° {choix_emplacement + 1} à l'étage n° {choix_etage + 1}")
					# la place n'est plus disponible
					parking[choix_etage][choix_emplacement] = 'V'
					# générer le code secret
					code_secret = generer_code_debloquage()
					# affecter le code secret à l'étage / place choisie
					code_debloquage[choix_etage][choix_emplacement] = code_secret
				
				else:
					print("Emplacement non disponible")

		elif choix == 2:
			print("Récupérer une voiture")
			choix_emplacement = int(input("N° d'emplacement svp : ")) - 1

			# vérifier si la place choisie se trouve dans le nombre de composants de la liste
			if 0 <= choix_emplacement <= len(parking[choix_etage]):

				# vérifier si la place est occupée
				if parking[choix_etage][choix_emplacement] == 'V':
					# demander le code secret de la place prise
					choix_code_secret = input("Veuillez saisir votre code secret : ")
					# vérifier si le code secret est bon
					code_secret_atrouver = code_debloquage[choix_etage][choix_emplacement]
					# comparer
					if choix_code_secret == code_secret_atrouver :
						print("Véhicule récupéré")
						# la place redevient disponible
						parking[choix_etage][choix_emplacement] = 'D'
						print(f"L'emplacement n° {choix_emplacement + 1} est à nouveau disponible")
					else:
						print("Code incorrect !")
				else:
					print(f"Oh oh... il n'y a pas de véhicule à l'emplacement n° {choix_emplacement + 1} :(")

		else:
			print("Erreur, vous devez écrire 1 ou 2")

		# appel de la fonction
		afficher_parking()

	else:
		print("Cet étage n'existe pas à moins que vous vous appelez Harry Potter...")