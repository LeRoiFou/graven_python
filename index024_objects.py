"""
Cours : APPRENDRE LE PYTHON #7 ? LES OBJETS
Lien : https://www.youtube.com/watch?v=dfUM_9xibf8&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=7

Éditeur : Laurent REYNAUD
"""


# Classe Player
class Player:

    # Constructeur paramétré de la classe (avec 'def' pour fonction)
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/ Points de vie :", health, "/ Points d'attaque :", attack)


# Fin de la classe Player


# Instanciation de la classe Player en objet Player1 avec un constructeur paramétré
Player1 = Player("John", 20, 3)
Player2 = Player("Bob", 20, 5)
