"""
Cours : APPRENDRE LE PYTHON #5 ? LES BOUCLES
Lien : https://www.youtube.com/watch?v=BrknhzrHm8w&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=5

Éditeur : Laurent REYNAUD
"""

# Jeu du juste prix
# Demander à l'utilisateur d'entrer un prix entre 1 et 1000
# S'il trouve le juste prix "c'est gagné ! "
# Sinon on affiche "c'est moins" ou "c'est plus"

import random

print("Bienvenue au Juste Prix !")
print("musique...")

justeprix = random.randint(1, 1000)
joueurprix = int(input("Quel est votre prix ? "))
while joueurprix != justeprix:
    if joueurprix < justeprix:
        print("C'est plus !")
        joueurprix = int(input("Donner un autre prix : "))
    else:
        print("C'est moins !")
        joueurprix = int(input("Donner un autre prix : "))
print("C'est gagné !")
