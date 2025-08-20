"""GUI of the Number Guessing Game"""

import tkinter as tk
from .guess_taker import GuessTaker
from .show_attempts import AttemptsLeft

class NGGui:
    """GUI of the game"""
    def __init__(self, parent):

        self.parent = parent

        self.test_title = tk.Label(self.parent.root, text= "  GAME.  ", font= ("TF2 Build", 20))
        self.test_title.place(x= 450, y= 20)

        self.attempts = AttemptsLeft(self)
        GuessTaker(self)
