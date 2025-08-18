"""GUI of the Number Guessing Game"""

import tkinter as tk

class NGGui:
    """GUI of the game"""
    def __init__(self, parent):

        self.parent = parent

        self.test_title = tk.Label(text= "  GAME.  ")
