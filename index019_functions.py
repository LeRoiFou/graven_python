"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Fonction paramétrée avec retour de résultat


def message():
    return"Le résultat du calcul est"


# Pour éviter de faire autant de fonctions suivantes :
def addition1():
    return 5 + 1


def addition2():
    return 5 + 2


def addition3():
    return 5 + 3


def addition4():
    return 5 + 4


def addition5():
    return 5 + 5


# Il suffit de paramétrer la fonction de résultat
def addition(n):
    return 5 + n


print(message(), addition(1))
print(message(), addition(2))
print(message(), addition(3))
print(message(), addition(4))
print(message(), addition(5))
