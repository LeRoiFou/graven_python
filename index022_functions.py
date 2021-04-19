"""
Cours : APPRENDRE LE PYTHON #6 ? LES FONCTIONS
Lien : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6

Éditeur : Laurent REYNAUD
"""

# Une fonction pour calculer le nombre de voyelles et de consonnes dans une phrase
# définir une fonction get_lettres_numbers(mot)
# créer un compteur de voyelles, d'espaces et de consoles
# pour chaque lettre du mot vérifier s'il s'agit d'une voyelle, un espace ou une consonne
# si c'est le cas on ajoute +1 au compteur
# à la fin de la fonction, renvoyer le compteur

phrase = input("Veuillez saisir une phrase : ")


def get_lettres_numbers(p):
    nbre_voyelles = 0
    nbre_espaces = 0
    nbre_consonnes = 0
    for lettres in p:
        if lettres in "aeiouyAEIOUY":
            nbre_voyelles += 1
        elif lettres == " ":
            nbre_espaces += 1
        else:
            nbre_consonnes += 1
    return print("Il y a", nbre_voyelles, "voyelles", nbre_espaces, "espaces et",
                 nbre_consonnes, "consonnes dans cette phrase.")


get_lettres_numbers(phrase)
