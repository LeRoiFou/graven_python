"""
Cours : APPRENDRE LE PYTHON #7 ? LES OBJETS
Lien : https://www.youtube.com/watch?v=dfUM_9xibf8&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=7

Éditeur : Laurent REYNAUD
"""

# Récupération des attributs et des méthodes de la classe player qui est dans un autre fichier
from alp7.player import Player  # du fichier player dans le package alp7 récupère la classe Player

# Instanciation des classes Player et Weapon
Player1 = Player("John", 20, 3)
Player2 = Player("Bob", 20, 5)

print("Joueur", Player1.get_pseudo(), "à vous de jouer")
Player1.set_health(10)
print(Player1.get_pseudo(), "il ne vous reste plus que", Player1.health, "points de vie")

Player1.attack_player(Player2)
print(Player1.get_pseudo(), "attaque", Player2.get_pseudo())
print(Player1.get_pseudo(), "/ Points de vie :", Player1.get_health(), "/ Points d'attaque :", Player1.get_attack())
print(Player2.get_pseudo(), "/ Points de vie :", Player2.get_health(), "/ Points d'attaque :", Player2.get_attack())
