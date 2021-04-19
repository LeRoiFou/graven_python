"""
Cours : APPRENDRE LE PYTHON #9 ? INTERFACE GRAPHIQUE (avec Tkinter)
Lien : https://www.youtube.com/watch?v=N4M4W7JPOL4&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=9

Générateur de mot de passe avec tkinter

Éditeur : Laurent REYNAUD
Date : 21-10-2020
"""

import tkinter
import random
import string


def generate_password():
    """Configuration du mot de passe qui se génère automatiquement avec 6 caractères minimum et 12 caractères maximum
    et comprenant des lettres, des chiffres et des ponctuations."""
    password_min = 6  # nombre de caractères minimum du mdp
    password_max = 12  # nombre de caractères maximum du mdp
    all_chars = string.ascii_letters + string.punctuation + string.digits  # caractères autorisés
    password = ''.join(random.choice(all_chars) for x in range(random.randint(password_min, password_max)))
    password_entry.delete(0, 'end')  # réinitialisation du mpd
    password_entry.insert(0, password)  # régénération du mpd


# Configuration de la fenêtre
window = tkinter.Tk()
window.title('Générateur de mot de passe')
window.geometry('720x480')
window.config(background='#4065A4')

# Widget cadre principal où se trouve tous les widgets ci-après
frame = tkinter.Frame(window, bg='#4065A4')
frame.pack(expand='yes')

# Widget image
width = 300
height = 300
image = tkinter.PhotoImage(file='images/padlock.png').zoom(17).subsample(30)  # dimension de l'image téléchargée
canvas = tkinter.Canvas(frame, width=width, height=height, bg='#4065A4', bd=0,
                        highlightthickness=0)  # dimension de la fenêtre image + suppression de la bordure blanche
canvas.create_image(width / 2, height / 2, image=image)  # adaptation de l'image dans la fenêtre
canvas.grid(row=0, column=0, sticky='w')  # image à gauche de l'étiquette détaillée ci-dessous

# Widget sous-cadre où se trouve le titre 'Mot de passe', le champs de saisie du mot de passe et le bouton 'générer'
right_frame = tkinter.Frame(frame, bg='#4065A4', )
right_frame.grid(row=0, column=1, sticky='w')  # sous-cadre à droite du cadre principal

# Widget étiquette titre 'Mot de passe'
label = tkinter.Label(right_frame, text='Mot de passe', font=('Arial', 20), bg='#4065A4', fg='white')
label.pack()

# Widget champs de saisie du mot de passe
password_entry = tkinter.Entry(right_frame, font=('Arial', 20), bg='#4065A4', fg='white')
password_entry.pack()

# Widget bouton permettant de générer un mot de passe
button = tkinter.Button(right_frame, text='Générer', font=('Arial', 15), bg='#4065A4', fg='white',
                        command=generate_password)  # widget en corréraltion aved la fonction generate-password()
button.pack(fill='x')  # largeur du bouton = largeur champs de saisie

# Widget barre de menu
mainmenu = tkinter.Menu(window)
file_menu = tkinter.Menu(mainmenu, tearoff=0)
file_menu.add_command(label='Nouveau', command=generate_password)
file_menu.add_command(label='Quitter', command=window.quit)
mainmenu.add_cascade(label='Fichier', menu=file_menu)

window.config(menu=mainmenu)
window.mainloop()
