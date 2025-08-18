"""Game of the Number Guessing Game"""

import os
import tkinter as tk
from tkinter import messagebox
from ..game_settings.properties import Properties
from .gui_ngg import NGGui

class NumberGuessing:
    """Number Guessing Game"""
    
    def __init__(self):

        self.prp = Properties

        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Number Guessing Game")
        self.root.iconphoto(False,
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
