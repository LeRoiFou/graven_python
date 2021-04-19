"""
Cours : APPRENDRE LE PYTHON #4 ? LES LISTES
Lien : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4

Éditeur : Laurent REYNAUD
"""

date = input("Date : ")
libelle = input("Libellé : ")
montant = int(input("Montant : "))

liste = [date, libelle, montant]

print("Pour l'opération saisie, la date est le " + liste[0] + " pour le motif suivant : " + liste[
    1] + ", avec un montant de " + str(liste[2]) + " €")
