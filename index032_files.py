"""
Cours : APPRENDRE LE PYTHON #10 ? LES FICHIERS
Lien : https://www.youtube.com/watch?v=jOHpZg8k668&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&ind

Les fichiers : copier/coller un fichier

Éditeur : Laurent REYNAUD
Date : 03-09-2020
"""

import os  # module de gestion des systèmes d'exploitation dont les fichiers
import shutil  # module qui permet de voir entre autres un copier/coller d'un fichier

source = "Meals.txt"  # fichier source
target = "pieces/FichierADeplacer.txt"  # répertoire et fichier cibles

shutil.copy(source, target)  # copie du fichier source dans le répertoire cible
os.remove(source)  # suppression de l'emplacement initial du fichier source
