"""
Cours : APPRENDRE LE PYTHON #5 ? LES BOUCLES
Lien : https://www.youtube.com/watch?v=BrknhzrHm8w&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=5

Éditeur : Laurent REYNAUD
"""

print("Vous êtes le client n° 1")
print("Vous êtes le client n° 2")
print("Vous êtes le client n° 3")
print("Vous êtes le client n° 4")
print("Vous êtes le client n° 5")

print()
print("Recours aux boucles ci-après")
print()

# Boucle for
for num_client in range(1, 6):  # la valeur d'arrivée est toujours exclue
    print("Vous êtes le client n°", num_client)
