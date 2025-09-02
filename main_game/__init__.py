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

        # This could've given me really hard time
        self.prp= prp

        # Set the window
        self.root = tk.Tk()
        self.root.geometry("600x475")
        self.root.title("Number Guessing Game")
        self.root.iconphoto(
            False,
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"icon.png"))
        )

        # Manage the background colors from here
        self.bg= "gray20"
        self.root.configure(background= self.bg)

        # To shut the W0201
        self.game_vals: object

        # Start the game
        self.start_game()

        #XXX self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def start_game(self):
        """Start the game"""
        self.game_vals = RandomNumber(self)
        NGGui(self)

    def on_exit(self):
        """Where do you think you're going?"""
        leave = messagebox.askyesno(
            title= "Leaving Game",
            message= "Do you actually want to leave the game?"
        )

        if not leave:
            return

        self.root.destroy()
