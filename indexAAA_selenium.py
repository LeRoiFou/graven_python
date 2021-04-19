"""
Cours : Contrôler GOOGLE CHROME avec Python !
Lien : https://www.youtube.com/watch?v=pHFsGWC8LSU

Accès sur @ :
Site visité : https://selenium-python.readthedocs.io/
Installation du driver google chrome : https://sites.google.com/a/chromium.org/chromedriver/downloads
Récupérération du driver zippé de la version Chrome 88 ici, puis copie du fichier .exe dans le présent package

Documentation sur les éléments à récupérer du site :
https://selenium-python.readthedocs.io/navigating.html

Packages installés sur python :
. selenium

Dans ce programme on apprend à accéder à un site @ mais par rapport au module webbrowser, on peut fournir des commandes
à réaliser sur le site
À titre d'exemple, accéder au site INSEE puis avec la saisie sur tkinter du n° SIREN d'une société, on exige au sites
INSEE de ressortir les données de la société concernée

Éditeur : Laurent REYNAUD
Date : 28-02-2021
"""

from selenium import webdriver

"""Assignation d'un déclenchement du driver"""
driver = webdriver.Chrome(executable_path='chromedriver.exe')

"""Accès au site directement avec Chrome"""
driver.get('https://www.kubii.fr/')

"""Assignation de la récupération de la barre de recherche du site : on récupère dans le fichier html du site
l'identifiant 'id' de l'élément html lié à la barre de recherche et on pour cela on utilise la fonction:
driver..find_element_by_id()"""
search_bar = driver.find_element_by_id('search_query_top')
search_bar.send_keys('Raspberry')  # envoi d'instruction de saisir du texte dans la barre de recherche du site

"""Assignation de la récupération du bouton de recherche du site : cette fois-ci il n'y a pas d'identifiant 'id' mais
il y a un identifiant 'class' dans l'élément html lié à ce bouton de recherche et pour cela on utilise la fonction :
"""
search_btn = driver.find_element_by_class_name('button-search')
search_btn.click()  # envoi d'instruction de cliquer sur le bouton de recherche du site

"""Assignation de la récupération tous les noms de produits 'Raspberry' dans le site"""
all_titles = driver.find_elements_by_class_name("product-name")

"""Parcours de la liste des produits"""
for title in all_titles:
    print(title.text)  # valeur associée au composant 'title'
