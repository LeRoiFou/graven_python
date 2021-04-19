"""
Cours : APPRENDRE LE PYTHON #4 ? LES LISTES
Lien : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4

Éditeur : Laurent REYNAUD
"""

# Générateur de phrases
# Demander en console une chaîne de la forme : mot1/mot2/mot3/mot4
# Transformer cette chaîne en une liste
# La mélanger
# Si le nombre d'éléments de cette liste est < à 10 : afficher les 2 premiers mots
# Si le nombre d'éléments de cette liste est >= 10 : afficher les 3 derniers mots

import random

liste = input("Saisir une chaîne de la forme mot1/mot2/mot3/mot4/... : ").split("/")
melanger = random.shuffle(liste)
print(liste)
print(len(liste))
if len(liste) <= 2:
    print(liste)
elif 3 <= len(liste) <= 10:
    print(liste[0:2])
else:
    print(liste[len(liste) - 3], liste[len(liste) - 2], liste[len(liste) - 1])
