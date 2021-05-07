"""
Exercice : Jour Jour 18/30 - Python n°5 - Machine à laver
Lien : https://www.youtube.com/watch?v=HfS6XRfvd9Y&list=PLMS9Cy4Enq5Jnsgg_CqfxwyLHwf8X9AQI&index=18

Contexte du jeu :
Vous venez d'acheter une machine à laver dans votre magasin
Elle possède une capacité de 8 kg et possède une vitesse de 1 400 tours minutes et nécessite
35 minutes pour un lavage complet

Instructions vues dans ce programme :
-> Fonction prédéfinie ceil() du module math utilisé pour les arrondis
-> Fonction prédéfinie sleep() du module time pour générer un temps d'attente
-> Concernant les attributs d'une classe en POO :
- soit l'attribut est passé dans les paramètres du constructeur sans déclarer de valeurs, car c'est à
l'utilisateur de choisir la valeur affectée à l'attribut ;
- soit l'attribut est passée dans les paramètres du constructeur avec une valeur qui lui est affectée,
car c'est le concepteur qui propose cette valeur mais l'utilisateur peut très bien déclarer une valeur
différente à cet attribut et c'est cette dernière valeur qui sera appliquée ;
- soit l'attribut n'est pas dans les paramètres du constructeur, il est déclaré avec sa valeur à
l'intérieur du constructeur et dans ce cas là, on peut considérer l'attribut comme une constante pour
laquelle l'utilisateur ne peut en aucun cas rectifier la valeur déclarée et imposée par le concepteur

Éditeur : Laurent REYNAUD
Date : 06-05-21
"""
import math
import time

class LaveLinge:
	# classe qui va gérer la notion du lave-linge

	def __init__(self, tours_minutes=1_400, contenance_kg=8):
		# constructeur de la classe
		self.tours_minutes = tours_minutes
		self.contenance_kg = contenance_kg
		self.temperature_actuel = 60
		self.contenance_actuelle_kg = 0
		self.duree_machine_defaut = 35
		self.duree_machine = 5
		print("Nouvelle machine ajoutée à la laverie")
		print(f"Tours minutes : {self.tours_minutes} - Contenance : {self.contenance_kg} kg - Température : {self.temperature_actuel} °C")

	def inserer_linge(self, poids_kg):
		
		print(f"Vous ouvrez la machine et vous entrez du linge d'un poids total de {poids_kg} kg")

		# vérification
		if poids_kg <= self.contenance_kg:
			print("Ok ! Le linge est à l'intérieur")
			self.contenance_actuelle_kg = poids_kg
		else:
			print("Ah non ! La machine est trop petite !")

	def demarrage(self):
		# méthode pour démarrer la machine à laver

		# vérifier si la machine est vide
		if self.contenance_actuelle_kg != 0:

			# créer une variable pour stocker le nombre de tours de la machine
			compteur_tours = 0

			# boucle tant que la machine n'est pas arrivée à 0
			while self.duree_machine > 0 :
				print(f"Duree_machine : reste {self.duree_machine} min")
				# incrémentations
				self.duree_machine -= 1
				compteur_tours += 1_400
				# attendre 1 seconde avant de relancer le tour
				time.sleep(1)

			# afficher nombre de tours minutes
			print(f"Nombre de tours de la machine : {compteur_tours} tours")
		
		else:
			print("Démarrage impossible, vous n'avez pas mis de linge !")

	def stop(self):
		
		if self.duree_machine > 0 :
			print("Arrêt OK !")
			self.duree_machine = 0
		else:
			print("Arrêt impossible, lave-linge en cours d'utilisation")

	def fermer(self):
		pass

# afficher un message dans la console
print("Ouverture de la machine à laver")

# appel de la classe
machine = LaveLinge(2_000, 15)

# dictionnaire avec nos vêtements et leurs poids
vetements = {
"T-shirt vert fluo": 1,
"Manteau en fourrure de pastèques": 6,
"Chaussettes trouées": 4,
"Jean de Hulk": 20
}

# somme du poids de chaque vêtement
kg = sum(vetements.values())

print(f"Vous avez {kg} kg de vêtements")

# calculer combien de machines à utiliser (arrondi avec la fonction ceil du module math)
machines = math.ceil(kg / 8)
print(f"Nombre de machines à utiliser : {machines}")
	
# calculer la consommation d'eau
consommation_eau = machines * 60
print(f"La consommation d'eau pour {machines} machine(s) est de {consommation_eau} L")

# appeler la méthode inserer_linge de la classe LaveLinge
machine.inserer_linge(kg)

# appeler la méthode pour démarrer la machine à laver
machine.demarrage()

# appeler la méthode pour arrêter la machine à laver
machine.stop()