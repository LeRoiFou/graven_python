"""
Cours : APPRENDRE LE PYTHON #7 ? LES OBJETS
Lien : https://www.youtube.com/watch?v=dfUM_9xibf8&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=7

Éditeur : Laurent REYNAUD
"""


class Player:

    # Constructeur paramétré (avec 'def' pour méthode)
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/ Points de vie :", health, "/ Points d'attaque :", attack)

    # Getters sur tous les attributs
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    # Setter sur l'attribut health
    def set_health(self, health):
        self.health -= health
        print("Bim ! vous avez perdu", health, "points")

    # Méthode pour attaquer un autre joueur
    def attack_player(self, target_player):
        target_player.set_health(self.attack)

# Fin de la classe Player
