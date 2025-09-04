"""Show all the chosen by the player"""

import tkinter as tk
from .display import Display
from .start_button import StartGame

class Showcase: # pylint: disable= too-few-public-methods
    """Show the chosen settings"""
    def __init__(self, parent):

        self.parent = parent

        title = tk.Label(
            master=self.parent.root,
            text="Chosen Settings",
            font=("TF2 Build", 25, "underline"),
            bg="gray20", fg="white"
        )

        title.place(x= 400, y= 275)

        self.display = Display(self.parent.root)
        StartGame(self)

    def give_permit(self):
        """Give display's self to other modules"""
        return self.display.give_permit()
