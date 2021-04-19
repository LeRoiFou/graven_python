"""
Cours : APPRENDRE LE PYTHON #3 ? LES CONDITIONS
Lien : https://www.youtube.com/watch?v=_AgUOsvMt8s&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=3

Éditeur : Laurent REYNAUD
"""

# Attributs
wallet = 5000
computer_price = 900

# Résultat booléen
print(computer_price < 1000)

# Condition if else
if computer_price < 1000:
    print("Le prix de l'ordinateur est inférieur à 1 000 €")
else:
    print("Non le prix de l'ordinateur est supérieur à 1000 €")

# Autre condition avec l'instruction !=
if computer_price != 1000:
    print("Le prix de l'ordinateur est différent de 1 000 €")
else:
    print("Oui le prix de l'ordinateur est de 1 000 €")

# Autre condition avec l'instruction or
if computer_price <= wallet or computer_price < 1000:
    print("L'achat est possible")
    wallet -= computer_price
    print("Solde de votre porte-monnaie : {}".format(wallet) + " €")
    # Recours à l'instruction {}".format() au lieu et place de str()
else:
    print("Vous n'avez pas assez d'argent pour acheter l'ordinateur")

# Exemple d'une condition ternaire qui a 3 éléments :
# 1er élément : "L'achat est possible"
# 2ème élément : "L'achat est impossible"
# 3ème élément : [computer_price < 1000]
# Cette instruction est identique à la condition précédente mais présentée sous un autre format
text = ("L'achat est impossible", "L'achat est possible")[computer_price < 1000]
print(text)
