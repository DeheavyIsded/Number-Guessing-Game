"""The widget to show the incorrect guesses"""

import tkinter as tk

class Misguess:
    """The widget to show the incorrect guesses"""    
    def __init__(self, parent):
        self.parent = parent
        self.misguesses_raw: list[int]= []
        self.misguess_list = tk.Listbox(
            self.parent.parent.root,
            bg= self.parent.parent.bg,
            fg= "white",
            font= ("TF2 Build", 15),
            exportselection= False,
            selectmode= tk.NONE
        )
        self.misguess_list.place(x= 50, y= 50)

    @property
    def misguesses(self) -> list[int]:
        """The list of all incorrect guesses"""
        return self.misguesses_raw

    def add_guess(self, new_misguess: int) -> None:
        """Add new guess to the listbox"""
        self.misguesses_raw.append(new_misguess)
        self.misguess_list.insert(len(self.misguesses),new_misguess)
        self.misguess_list.config(height=self.misguess_list.size() + 1)
