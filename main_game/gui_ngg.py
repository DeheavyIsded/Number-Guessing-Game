"""GUI of the Number Guessing Game"""

import tkinter as tk

class NGGui:
    """GUI of the game"""
    def __init__(self, parent):

        self.parent = parent

        self.test_title = tk.Label(self.parent.root, text= "  GAME.  ")
        self.test_title.place(x= 100, y= 50)
