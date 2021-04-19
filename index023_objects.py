"""
Cours : APPRENDRE LE PYTHON #7 ? LES OBJETS
Lien : https://www.youtube.com/watch?v=dfUM_9xibf8&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=7

Éditeur : Laurent REYNAUD
"""

# Classe Player
class Player:
    # Attributs
    pseudo = "John"
    health = 20
    attack = 3


# Fin de la classe Player

# Instanciation de la classe Player en objet Player1 avec un constructeur par défaut par défaut
Player1 = Player()

print("Bievenue au joueur", Player1.pseudo)
