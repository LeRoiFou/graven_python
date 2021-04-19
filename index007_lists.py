"""
Cours : APPRENDRE LE PYTHON #4 ? LES LISTES
Lien : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4

Éditeur : Laurent REYNAUD
"""

# En saisisant une chaîne de caractères séparé du caractère "-", une liste sera établie avec l''instruction ci-après
text = input("Entrer une chaîne de la forme (email-pseudo-mdp) : ").split("-")

# R : ['lrcompta', 'gerald', 'test22']
print(text)

# R : Salut, ton email est lrcompta, ton pseudo est gerald et ton mdp est test22
print("Salut, ton email est " + text[0] + ", ton pseudo est " + text[1] + " et ton mdp est " + text[2])
