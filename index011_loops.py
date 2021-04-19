"""
Cours : APPRENDRE LE PYTHON #5 ? LES BOUCLES
Lien : https://www.youtube.com/watch?v=BrknhzrHm8w&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=5

Éditeur : Laurent REYNAUD
"""

print("Email envoyé à : lrcompta@ao.fr")
print("Email envoyé à : lrcompta@free.fr")
print("Email envoyé à : lrcompta@sfr.fr")
print("Email envoyé à : lrcompta@gmail.com")
print("Email envoyé à : lrcompta@xxx.fr")

print()
print("Recours à la boucle for each")
print()

# Stockage des données dans une liste
emails = ["lrcompta@ao.fr", "lrcompta@free.fr", "lrcompta@sfr.fr", "lrcompta@gmail.com", "lrcompta@xxx.fr"]

# Boucle for each
for elements in emails:
    print("Email envoyé à :", elements)
