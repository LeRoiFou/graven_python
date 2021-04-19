"""
Cours : APPRENDRE LE PYTHON #4 ? LES LISTES
Lien : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4

Éditeur : Laurent REYNAUD
"""

# Import du package statistics pour recourir aux outils tels que la moyenne, la médiane...
import statistics

# Import du module random pour recourir entre autres au mélange des données
import random

# Liste des notes d'un élève
notes = [8, 12, 10, 9, 4, 20]
print(notes)

# Instruction pour obtenir la moyenne avec la fonction statistics.mean()
result = statistics.mean(notes)
print("La moyenne de  l'élève est de " + str(result) + "/20")

# Instruction pour obtenir les notes dans le désordre avec la fonction random.shuffle
# R : [10, 4, 8, 9, 20, 12]
auhasard = random.shuffle(notes)
print(notes)
