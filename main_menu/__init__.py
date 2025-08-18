"""Main Menu for the game"""

import os
import tkinter as tk
import tkinter.font as tkFont
import ctypes
from .main_menu_gui import MainMenu

class Start:
    """I couldnt find a better game"""

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Number Guessing Game")
        self.root.iconphoto(False,
                            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"icon.png")))

        self.root_background = "#aaccff"
        self.root.configure(background= self.root_background)

        # Main menu texts font
        ctypes.windll.gdi32.AddFontResourceW(
            os.path.join(os.path.dirname(__file__), "tf2build.ttf"))

        self.main_menu_font = tkFont.Font(
            family= "TF2 Build",
            size= 37,
            weight= "bold")

        MainMenu(self.root, self)

    def aaa(self) -> type:
        """Placeholder for Refactor code R0903"""
        return str
    def bbb(self) -> type:
        """Placeholder for Refactor code R0903"""
        return int
