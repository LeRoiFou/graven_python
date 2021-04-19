"""
Cours : APPRENDRE LE PYTHON #10 ? LES FICHIERS
Lien : https://www.youtube.com/watch?v=jOHpZg8k668&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&inde

Les fichiers : lecture d'un fichier

Éditeur : Laurent REYNAUD
Date : 03-09-2020
"""

import random

with open("pieces/Students.odt", "r+") as file:  # nom du fichier +
    # mode de lecture
    print(file.readlines())  # lecture du contenu du fichier
