"""
Cours : APPRENDRE LE PYTHON #3 ? LES CONDITIONS

Éditeur : Laurent REYNAUD
"""

print("Saisie des opérations")
print()
date = input("Date : ")
libelle = input("Libellé : ")
montant = int(input("Montant : "))
print()
print("Affichage des données :")
print("Date de l'opération : " + date)
print("Libellé de l'opération : " + libelle)
if montant < 0:
    print("Montant au débit : " + str((-montant)) + " €")
else:
    print("Montant au crédit : " + str(montant) + " €")