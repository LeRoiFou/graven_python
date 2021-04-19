"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Fonction avec récursivité


def add(valeur1):
    valeur1 += 1
    print(valeur1)
    if valeur1 < 10:  # Si on ne rajoute pas cette instruction, le programme continuera à rajouter 1 à chaque fois
        add(valeur1)


add(5)
