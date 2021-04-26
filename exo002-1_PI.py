"""
Exercice : JOUR 5/30 - Exo Python 2 - Séance de Cinéma
Lien : https://www.youtube.com/watch?v=lFBN75DEHBY&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=5

Dans ce programme un client vient réserver une place de cinéma selon 3 films proposés en mentionnant
en complément l'heure de la séance ainsi que le nombre de places disponible en recourant uniquement 
à la programmation impérative.
Les données sont affichées dans la console

Éditeur : Laurent REYNAUD
Date : 24-04-21
"""

print("Bienvenue au cinéma, voici les films à l'affiche :")

# liste des films dans des dictionnaires
films = [
{ # film n° 1
	"titre" : "Voyage au centre du HTML",
	"séance" : "18h05",
	"places" : 200
},
{ # film n° 2
	"titre" : "Les 9 jsons cachés",
	"séance" : "10h10",
	"places" : 80
},
{ # film n° 3
	"titre" : "Algobox - le film",
	"séance" : "22h15",
	"places" : 120
}
]

# affichage des films avec la méthode prédéfinie enumerate
for numero, film in enumerate(films, start=1): # départ à partir de 1 au lieu de 0
	titre = film['titre']
	seance = film['séance']
	places = film['places']
	print(f"Film n° {numero} : {titre}, séance de {seance} ({places} places dispo)")
print('')

# boucle infinie
while True:
	# demande à l'utilisateur d'entrer un film à voir et affichage du titre sélectionné
	choix = int(input("Inscrivez le numéro du film à voir (1, 2 ou 3) : "))
	selection = films[choix-1]
	print(f"Vous avez choisi le film : '{selection.get('titre')}'")

	nb_places = selection['places']

	# vérifier si le film n'est pas complet
	if nb_places > 0:
		print("Achat effectué")
		# retirer une place dans ce film
		selection['places'] -= 1
		print(f"Le film dispose désormais de {selection['places']} place(s)")
	else:
		print("Film complet !")
