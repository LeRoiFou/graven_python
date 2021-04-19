"""
Cours : APPRENDRE LE PYTHON #5 ? LES BOUCLES
Lien : https://www.youtube.com/watch?v=BrknhzrHm8w&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=5

Éditeur : Laurent REYNAUD
"""

# Boucle while

salary = 1500

while salary < 2000:
    salary += 120
    print("Votre salaire actuel est de", salary, "€")
print()

# Autre cas avec un youtubeur ayant 2500 abonnés qui gagne 10 % d'abonnés par mois
# et on souhaite estimer, combien aura t'il d'abonnés après 2 ans (soit 24 mois)

suscribers_count = 2500
month = 0

while month <= 24:
    suscribers_count *= 1.10
    month += 1
    print("Vous avez actuellement", suscribers_count, "abonnés")
