"""
Cours : APPRENDRE LE PYTHON #4 ? LES LISTES
Lien : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4

Éditeur : Laurent REYNAUD
"""

# Créer une liste qui va stocker des pseudos

# Déclaration
online_players = ["Gerald", "Ananas", "Test", "Bob"]

# R : ['Gerald', 'Ananas', 'Test']
print(online_players)

# R : Gerald
print(online_players[0])

# R : Test
print(online_players[2])

# R : Bob
print(online_players[len(online_players) - 1])

# Remplacement Gerald par John
online_players[0] = "John"
print(online_players[0])

# Ajout d'un nouvel élément dans la liste
# R : ['John', 'Ananas', 'Salut', 'Test', 'Bob']
online_players.insert(2, "Salut")
print(online_players)

# Affichage d'un certain nombre d'élément à partir d'une position
# R : ['Salut', 'Test']
print(online_players[2:4])

# Ajout d'un élément en fin de liste
# R : ['John', 'Ananas', 'Salut', 'Test', 'Bob', 'Toto']
online_players.append("Toto")
print(online_players)

# Ajout de plusieurs éléments en fin de liste
# R : ['John', 'Ananas', 'Salut', 'Test', 'Bob', 'Toto', 'titi', 22, 17]
online_players.extend(["titi", 22, 17])
print(online_players)

# Suppression d'un élément de la liste
# R : ['John', 'Ananas', 'Test', 'Bob', 'Toto', 'titi', 22, 17]
del online_players[2]
print(online_players)

# Autre possibilité de suppression d'un élément de la liste
# R : ['John', 'Ananas', 'Bob', 'Toto', 'titi', 22, 17]
online_players.remove("Test")
print(online_players)

# Suppression de tous les éléments de la liste
# R : []
online_players.clear()
print(online_players)
