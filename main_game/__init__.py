"""Game part of the Number Guessing Game"""

import os
import tkinter as tk
from tkinter import messagebox
try:
    from ..game_settings.properties import Properties
    from .main_game.gui_ngg import NGGui
except ImportError:
    from game_settings.properties import Properties
    from main_game.gui_ngg import NGGui

class NumberGuessing:
    """Number Guessing Game"""
    
    def __init__(self):

        self.prp = Properties

        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Number Guessing Game")
        self.root.iconphoto(False, # FIXME: "icon.png" is bad path!
                            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"icon.png")))
        NGGui(self)

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def on_exit(self):
        """Where do you think you're going?"""
        leave = messagebox.askyesno(title= "Leaving Game",
                                    message= "Do you actually want to leave the game?")

        if not leave:
            return

        self.root.destroy()
