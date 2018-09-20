#Created by Lukas Pabijonavicius

from tkinter import Tk, Entry, Button


class App:

	def __init__(self,master):
		self.master = master
		self.entry_fields = []
		self.buttons = []
		self.grid_fields = []

		self.draw_gui()

	def draw_gui(self):
		self.master.title("Matrix Calculator")






root = Tk()
my_gui = App(root)
root.mainloop()