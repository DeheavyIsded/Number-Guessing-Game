"""The start button"""

import sys
import os
import tkinter as tk
from tkinter import messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from main_menu.gui_components import Gui
from main_game import NumberGuessing

class StartGame:
    """Class for the button that starts the game"""

    def __init__(self, parent):

        self.parent = parent

        # The button
        self.start_button = tk.Button(self.parent.root, text= "  START  ",
                                      bg= "#0099ff", fg= "#d0d0d0",
                                      activebackground= "#0066cc", activeforeground= "white",
                                      command= self.start_game)

        Gui.add_hover(widget= self.start_button,
                      background= ("#0078d8", "#0099ff"),
                      foreground= ("#e0e0e0", "#d0d0d0"),
                      text= ("  STRUT  ", "  START  "))

        self.start_button.place(x= 450, y= 450)

    def start_game(self):
        """Signal the start to the main game's package"""
        answer = messagebox.askyesno(title= "Confirm", message= "Are you sure about the settings?")

        if not answer:
            return

        self.parent.root.destroy()
        NumberGuessing()
