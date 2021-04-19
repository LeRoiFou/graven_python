"""
Cours : APPRENDRE LE PYTHON #9 ? INTERFACE GRAPHIQUE (avec Tkinter)
Lien : https://www.youtube.com/watch?v=N4M4W7JPOL4&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=9

Modules tkinter (interface graphique) et webbrowser (lien internet)

Pour changer l'icône situé à gauche du titre de la fenêtre (pour les icônes : https://www.flaticon.com/home):
    -> choisir une image .png pour remplacer l'icône
    -> ce fichier .png doit être converti en fichier .ico : tapper sur google 'png to ico' puis aller sur le 1er lien ->
    https://image.online-convert.com/convert/png-to-ico
    -> récupérer le fichier pour le convertir en .ico

Pour choisir une couleur de fond autre qu'une couleur classique telle que bleu, rouge ou jaune qui sont en surbrillance,
choisir une couleur en hexadécimal, pour cela tapper sur google 'couleur hexadécimale' pour obtenir le code hexadécimal
de la couleur souhaitée selon le formation suivant :
    -> WigdetParent.config(background='#CodeHexadecimal')

Les instructions pour configurer un widget :
    -> text="Titre du widget"
    -> font=(type d'écriture, taille de l'écriture)
    -> bg=(#code couleur hexadécimal ou NomCouleurPrimaire) : couleur de fond du widget (bg = background)
    -> fg=(#code couleur hexadécimal ou NomCouleurPrimaire) : couleur du texte
    -> bd=TailleDelaBordure (cadre)
    -> relief='TypeDeReliefDuFondDeLaBordure' (cadre)
    -> Widget.pack(fill='x') : le widget a la largeur du cadre

Éditeur : Laurent REYNAUD
Date : 20-10-2020
"""

import tkinter
import webbrowser


def open_channel():
    """Lien pour accéder à la documentation sur les interfaces graphiques"""
    webbrowser.open_new('http://tkinter.fdex.eu/index.html')


window = tkinter.Tk()

# Configuration de la fenêtre
window.minsize(200, 100)  # taille minimum
window.geometry('720x480')  # Dimension de la fenêtre
window.maxsize(800, 600)  # taille maximum
window.title('My application')  # Titre de la fenêtre
window.config(background='#3CAA9C')  # Couleur de fond de la fenêtre

# Widget cadre
frame = tkinter.Frame(window, bg='#3CAA9C', bd=1, relief='groove')  # Configuration
frame.pack(expand='yes')  # Affichage centré des widgets dans le cadre

# 1er widget étiquette
label = tkinter.Label(frame, text="Bienvenue sur l'application !", font=('Arial', 20),
                      bg='#3CAA9C', fg='white')  # Configuration
label.pack()  # Affichage dans le cadre

# 2ème widget étiquette
sub_label = tkinter.Label(frame, text="Hey salut à tous c'est John Gerald !", font=('Courrier', 15), bg='#3CAA9C',
                          fg='white')  # Configuration
sub_label.pack()  # Affichage dans le cadre

# 1er widget bouton qui permet d'accéder au lien sur les interfaces graphiques
button = tkinter.Button(frame, text='Documentation sur les interfaces graphiques', font=('Courrier', 15), bg='white',
                        fg='#3CAA9C', command=open_channel)
button.pack(fill='x')

window.mainloop()  # Arrêt du programme en fermant la fenêtre
