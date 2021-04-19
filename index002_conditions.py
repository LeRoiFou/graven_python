"""
Cours : APPRENDRE LE PYTHON #3 ? LES CONDITIONS
Lien : https://www.youtube.com/watch?v=_AgUOsvMt8s&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=3

Éditeur : Laurent REYNAUD
"""

# Système de vérification de mot de passe

password = input("Entrer votre mdp : ")
password_length = len(password)  # Compte le nombre de caractères
print(password_length)

# Vérifier si le mdp est <= à 8 caractères
if password_length <= 8 :
    print("Mdp trop court")
elif 8 < password_length < 12 :
    print("Mdp un peu bof...")
else:
    print("Mdp valide")
