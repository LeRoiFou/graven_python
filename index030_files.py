"""
Cours : APPRENDRE LE PYTHON #10 ? LES FICHIERS
Lien : https://www.youtube.com/watch?v=jOHpZg8k668&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=10

Les fichiers : écriture dans un fichier Writer de LibreOffice à partir d'une liste de données

Éditeur : Laurent REYNAUD  
Date : 03-09-2020  
"""

students_list = ["John", "Marcel", "Fabien", "Laurent"]  # liste des étudiants

with open("pieces/Students.odt", "w+") as file:  # nom du fichier +
    # mode d'ouverture
    # (w+ = écrire, a+ = ajouter)
    for student in students_list:
        file.write(student + "\n")  # saisie de chaque étudie avec un retour chariot
    # fermeture du fichier non nécessaire avec l'instruction 'with open() as'
