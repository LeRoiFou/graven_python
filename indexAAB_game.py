# https://youtu.be/SYtks243JR8?t=3214

from tkinter import *
from tkinter import Tk


class CrosswordGame:

	def __init__(self):

		# assignation d'une liste de str
		self.my_grid = [
		['O', 'P', 'H', 'P', 'R'],
		['E', 'R', 'T', 'I', 'E'],
		['X', 'I', 'M', 'H', 'G'],
		['E', 'T', 'L', 'M', 'E'],
		['R', 'T', 'O', 'D', 'X']
		]

		self.current_word = ""

	def insert_letter(self, row, col):

		# ajout des données de la grille
		self.current_word += self.my_grid[row][col]
		print(self.current_word)

	def get_current_word(self):
		return self.current_word


class GUI:

	def __init__(self, root):

		# instanciation de la classe CrosswordGame
		self.game = CrosswordGame()

		# configuration de la fenêtre
		self.root = root
		self.root.geometry("1080x720")
		self.root.title("Le Juste Mot : Mot croisé")
		self.root.resizable(False, False)

		self.selected_buttons = []

		# liste pour alimenter les composants des boutons (liste de compréhension)
		self.buttons = [[0 for x in range(5)] for x in range(5)]
		"""Le script ci-dessus équivaut à :
		self.buttons = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]"""
		
		# configuration des cadres
		self.left_frame = Frame(self.root)
		self.left_frame.grid(row=0, column=0, padx=20, pady=20)
		self.right_frame = Frame(self.root)
		self.right_frame.grid(row=0, column=1)

		self.current_word = StringVar()

		# appel des méthodes ci-dessous
		self.create_grid()
		self.create_right_part()

	def select_button(self, row, col):
		selected_button = self.buttons[row][col]
		selected_button.config(bg='yellow')
		self.current_word.set(self.game.get_current_word())
		self.game.insert_letter(row, col)
		self.selected_buttons.append(selected_button)

	def create_grid(self):
		# méthode permettant de configurer la grille à gauche de la fenêtre

		for row in range(5):
			for col in range(5):
				# instanciation de l'attribut my_grid de la classe CrosswordGame
				letter = self.game.my_grid[row][col]
				# configuration des lettres à afficher dans des boutons
				button = Button(
					self.left_frame, 
					text=letter, 
					width=6, 
					height=3, 
					font="Arial 20 normal",
					command= lambda r=row, c=col: self.select_button(r, c))
				button.grid(row=row, column=col)
				self.buttons[row][col] = button  # récupération des composants des boutons dans la liste

	def create_right_part(self):
		# méthode permettant de configurer les widgets à droite de la fenêtre

		display_text_selection = Label(self.right_frame, textvariable=self.current_word, font="Arial 20 normal")
		display_text_selection.pack(pady=40)
		confirm_button = Button(self.right_frame, text="Confirmer", font="Arial 20 normal")
		confirm_button.pack()
		reset_button = Button(self.right_frame, text="Effacer", font="Arial 20 normal")
		reset_button.pack()



root = Tk()
gui = GUI(root)
root.mainloop()