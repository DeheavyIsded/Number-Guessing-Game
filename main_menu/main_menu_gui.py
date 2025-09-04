# -*- coding: utf-8 -*-
"""
GUI of the main menu
"""

from tkinter import Label
from tkinter import messagebox
from pathlib import Path
from game_settings import GameSettings
from .gui_components import Gui

class MainMenu:
    """
    Class for the main game, I chose OOP because I don't want to deal with global values
    (A wise man told me to avoid them like the Black Plague)
    """
    def __init__(self, parent):

        self.parent = parent
        self.settings = GameSettings()
        self.hover_texts = [
            " Gumber Nuessing Name ",
            " Name Guessing Number ",
            "    Guess Naming Game ",
            "    Game Naming Guess ",
            "    Name Naming Name  ",
            "    Game Gaming Game  ",
            "  Guess Guessing Game ",
            " Guess Guessing Guess ",
            "    Name Gaming Game  ",
            "  That Game is a Spy! ",
            "   I forgot the name. ",
            "            The           "
        ]

        Gui(self.parent.root, self)

    def start(self):
        """Start the game"""
        self.root.destroy()
        settings_menu: GameSettings = GameSettings()
        settings_menu.set_up_gui()
