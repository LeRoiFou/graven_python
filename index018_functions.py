"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Fonction avec retour de résultat de chiffres


def addition():
    result = 5 + 5
    return result


# Étant donné qu'on a mis un retour de résultat dans la fonction ci-avant
# on peut donc directement appeler la fonction dans l'instruction print qui
# n'affichera pas dans ce cas un résultat nul
print("Le résultat du calcul est", addition())


# Autre moyen d'obtenir un retour de résultat
def additionbis():
    return 5 + 5


print("Le résultat du calcul est", additionbis())


# Fonction avec retour de résultat d'une chaîne de caractères
def get_message():
    return"Le résultat du calcul est"


print(get_message(), additionbis())
