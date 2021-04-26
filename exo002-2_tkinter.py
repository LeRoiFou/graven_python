"""
Exercice : JOUR 5/30 - Exo Python 2 - Séance de Cinéma
Lien : https://www.youtube.com/watch?v=lFBN75DEHBY&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=5

Dans ce programme un client vient réserver une place de cinéma selon 3 films proposés en mentionnant
en complément l'heure de la séance ainsi que le nombre de places disponible
Cette fois-ci on a recours au module tkinter

Éditeur : Laurent REYNAUD
Date : 24-04-21
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title("Séance de cinéma - Logiciel de gestion")
		self.widgets()

	def click_btn(self, film_id, reserve):
		"""fonction qui va s'activer lors du clique sur le bouton réserver :
		cette fonction a des paramètres et pour cela on a recours à la fonction lambda
		dans l'instruction command du bouton"""

		# demande à l'utilisateur d'entrer un film à voir et affichage du titre sélectionné
		selection = self.films[film_id-1]

		nb_places = selection['places']

		# vérifier si le film n'est pas complet
		if nb_places > 1:
			# retirer une place dans ce film
			selection['places'] -= 1
			reserve.set(selection['places'])	
		else:
			reserve.set("Film complet !")

	def widgets(self):

		# liste des films dans des dictionnaires
		self.films = [
		{ # film n° 1
			"titre" : "Voyage au centre du HTML",
			"séance" : "18h05",
			"places" : 200
		},
		{ # film n° 2
			"titre" : "Les 9 jsons cachés",
			"séance" : "10h10",
			"places" : 10
		},
		{ # film n° 3
			"titre" : "Algobox - le film",
			"séance" : "22h15",
			"places" : 120
		}
		]

		# affichage des films avec la méthode prédéfinie enumerate
		for numero, self.film in enumerate(self.films, start=1): # départ à partir de 1 au lieu de 0
			
			self.titre = self.film['titre']
			self.seance = self.film['séance']
			self.places = self.film['places']

			# mise à jour du nombre de places restantes
			self.places_var = tkinter.StringVar()
			self.places_var.set(self.places)
			
			titreLabel = tkinter.Label(root, text=f"Titre du film : '{self.titre}'")
			titreLabel.grid(row=numero, padx=10, pady=5, column=0)
			
			seanceLabel = tkinter.Label(root, text=f"Heure de la séance : {self.seance}")
			seanceLabel.grid(row=numero, padx=10, pady=5, column=1)

			titreplacesLabel = tkinter.Label(root, text="Nombre de places disponibles :")
			titreplacesLabel.grid(row=numero, padx=10, pady=5, column=2)

			placesLabel = tkinter.Label(root, textvariable=self.places_var)
			placesLabel.grid(row=numero, pady=5, column=3)

			book_button = tkinter.Button(
				root, 
				text="Réserver", 
				width=10, 
				command= lambda num=numero, reserve=self.places_var:self.click_btn(num, reserve))
			book_button.grid(row=numero, padx=10, pady=5, column=4)

if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()