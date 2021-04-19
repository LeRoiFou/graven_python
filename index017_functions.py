"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Variable sur l'année en cours
year = 2020

# Fonction sur l'année : pour recourir à cette variable ci-dessus
# dans la fonction ci-après, il faut recourir à l'instruction 'global'


def next_year():
    global year
    print("C'est la fin de l'année actuelle", year)
    year += 1
    print("Début de l'année", year)


# Appel de la fonction
next_year()
