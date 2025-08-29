"""Game part of the Number Guessing Game"""

import os
import tkinter as tk
from tkinter import messagebox
try:
    from .main_game.gui_components import NGGui
    from .main_game.number_generator import RandomNumber
except ImportError:
    from main_game.gui_components import NGGui
    from main_game.number_generator import RandomNumber

class NumberGuessing:
    """Number Guessing Game"""

    def __init__(self, prp):

        self.prp= prp

        self.root = tk.Tk()
        self.root.geometry("600x475")
        self.root.title("Number Guessing Game")
        self.root.iconphoto(
            False,
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"icon.png"))
        )

        self.bg= "gray20"
        self.root.configure(background= self.bg)

        self.game_vals = RandomNumber(self)
        NGGui(self)

        #XXXself.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def on_exit(self):
        """Where do you think you're going?"""
        leave = messagebox.askyesno(title= "Leaving Game",
                                    message= "Do you actually want to leave the game?")

        if not leave:
            return

        self.root.destroy()
