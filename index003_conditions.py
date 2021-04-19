"""
Cours : APPRENDRE LE PYTHON #3 ? LES CONDITIONS

Éditeur : Laurent REYNAUD
"""

# Places de cinéma
# Age de la personne : "quel est votre âge ?"
# Si la personne est mineure : 7 €
# Si la personne est majeure : 12 €
# Souhaitez-vous du popcorn ?
# Si oui : +5 €
# Affichage du prix total à payer

print("Bienvenue au cinéma !")
age = input("Quel est votre âge ? ")
if age < "18":
    print("Tarif d'entrée : 7 €")
    tarifentree = 7
else:
    print("Tarif d'entrée : 12 €")
    tarifentree = 12
pop = input("Souhaitez-vous du pop-corn ? ")
if pop == "oui":
    print("Prix du pop-corn : 5 €")
    tarifentree += 5
else:
    print("Radin !")
print("Prix total : " + str(tarifentree) + " €")
