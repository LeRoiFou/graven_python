"""
Exercice : Jour 29/30 - Python n° 8 - Jeu du juste prix (avec tkinter)
Lien : https://www.youtube.com/watch?v=IQtAfooLsJA&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=29

Contexte du jeu :
Deviner un prix ;)

Recours dans ce programme :
- Aux interfaces graphiques avec tkinter
- POO
- instruction set() dans tkinter pour le widget Label pour une mise à jour du texte affiché
- instruction focus() dans tkinter pour sélectionné directement un widget
- instruction bind() pour valider l'action en appuyant sur Entrée sans cliquer sur le bouton 'Valider'
- méthode clock() vu dans le cours n° 79 dans codemy-tkinter

Éditeur : Laurent REYNAUD
Date : 08-05-21
"""

import random
import time
import tkinter

class GUI:

	def __init__(self, root):
		# constructeur de la classe

		# configuration de la fenêtre principale
		self.root = root
		root.geometry('600x300')
		root.resizable(False, False)
		root.title("Jeu du juste prix")
		root.config(bg="#08DD68")

		# assignation de variables
		self.nombre_hasard = random.randint(1, 100)
		self.tentatives = 10
		self.temps = time.time()
		self.tic_tac = 60

		# appel des méthodes
		self.widgets()

	def widgets(self):
		# méthode pour configurer les widgets

		# cadre pour centrer les widgets autres que le temps restant et le nbre de tentatives
		frame = tkinter.Frame(root, bg='#08DD68')
		frame.pack(expand='y')

		# ajouter une entrée pour écrire
		self.entree_proposition = tkinter.Entry(frame, justify='center')
		self.entree_proposition.focus() # le selecteur de la souris se positionne par défaut dans ce widget :)
		self.entree_proposition.bind('<Return>', self.essai) # permet de valider le bouton en appuyant sur Entrée
		self.entree_proposition.pack(pady=10)

		# ajouter le bouton
		bouton = tkinter.Button(frame, text="Valider", command=self.essai)
		bouton.pack(pady=10)

		# ajouter un intitulé pour afficher les informations
		self.infovar = tkinter.StringVar()  # variable de contrôle
		self.infovar.set("Bonne chance")  # affichage par défaut
		info = tkinter.Label(frame, textvariable=self.infovar, bg='#08DD68')
		info.pack(pady=10)

		# ajouter un nombre de tentatives
		self.tentativestxtvar = tkinter.StringVar() # variable de contrôle
		self.tentativestxtvar.set("10 tentatives") # valeur par défaut
		tentativestxt = tkinter.Label(root, textvariable=self.tentativestxtvar, bg='#08DD68')
		tentativestxt.place(x=450, y=20)

		# ajouter temps restant
		self.tempstxt = tkinter.Label(root, text="60 secondes restantes", bg='#08DD68')
		self.tempstxt.place(x=20, y=20)

	def essai(self, e):
		# méthode pour lancer la programmation du jeu

		# appel de la méthode du décompte du temps
		self.clock()

		# récolter la proposition qui est dans le champ de saisie Entry
		nombre_proposition = self.entree_proposition.get()

		# si la saisie faite est un chiffre
		if nombre_proposition.isdigit():

			# conversion de la str en int
			proposition = int(nombre_proposition)
			
			# vérifier le nombre de la proposition <-> au nombre à trouver
			if proposition < self.nombre_hasard:
				self.infovar.set("C'est plus")
			elif proposition > self.nombre_hasard:				
				self.infovar.set("C'est moins !")
			else:
				self.infovar.set("C'est gagné !")
				time.sleep(2)
				root.quit()

			# incrémentation dud nombre de self.tentatives
			self.tentatives -= 1
			if self.tentatives > 1 :
				self.tentativestxtvar.set(f"reste {self.tentatives} tentatives")			
			else:
				self.tentativestxtvar.set(f"reste {self.tentatives} tentative !")

		# si le nombre saisi n'est pas un chiffre
		else:
			self.infovar.set("Tu dois entrer un nombre...")

	def clock(self):
		# méthode pour le décompte du temps

		# vérifier si le temps n'est pas dépassé
		temps_passe = int(time.time() - self.temps)

		# modification du temps restant
		self.tempstxt.config(text=f"{60 - temps_passe} secondes restantes")
		self.tempstxt.after(10, self.clock) # mise à jour du temps avec en arguments : temps en millisecondes, fonction

if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()