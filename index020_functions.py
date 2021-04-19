"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Création d'une fonction max, qui va renvoyer le résultat le plus haut parmis les deux valeurs


def maximum(valeur1, valeur2):
    if valeur1 > valeur2:
        return valeur1
    else:
        return valeur2


v1 = int(input("Entrer la 1ère valeur : "))
v2 = int(input("Entrer la 2ème valeur : "))

print("La valeur maximum est", maximum(v1, v2))
