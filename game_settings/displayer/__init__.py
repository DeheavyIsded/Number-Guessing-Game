"""Show all the chosen by the player"""

import tkinter as tk
from .display import Display

class Showcase: # pylint: disable= too-few-public-methods
    """Show the chosen settings"""
    def __init__(self, master, _):

        self.root = master

        title = tk.Label(self.root,
                         text= "Chosen Settings",
                         font= ("TF2 Build", 25, "underline"),
                         bg= "gray20", fg= "white")
        title.place(x= 400, y= 275)

        self.display = Display(self.root)

    def give_permit(self):
        return self.display.give_permit()
