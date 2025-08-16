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
    def __init__(self, master, parent):

        self.root = master
        self.parent = parent
        self.settings = GameSettings()
        try:
            with open("peynir.yeah", "r", encoding= "utf-8") as file:
                code = file.readline()
                if code == "Mentlegen.":
                    self.settings_set_ = True
            self.settings_set: bool = False

        except FileNotFoundError:
            self.settings_set: bool = True

        self.hover_texts = [" Gumber Nuessing Name ",
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
                              "            The           "]
        # The I.O.U text
        self.settings_i_owe_you = Label(self.root,
                                     text= "  I.O.U  ",
                                     font= ("Comic Sans MS", 20, "bold"),
                                     background= "#a76311",
                                     foreground= "black")
        Gui(self.root, self)

    def start(self):
        """Start the game"""
        self.root.destroy()
        settings_menu: GameSettings = GameSettings()
        settings_menu.set_up_gui()

    def stats(self):
        """Show player's statistics"""
        messagebox.showerror(title= "Stats?",
        message= 'You have not played the game yet,\n'
        'what "stats" are you expecting me to bring up?')

    def check_settings(self, child):
        """The "Settings" option"""
        with open("peynir.yeah", "r", encoding= "utf-8") as file:
            if file.read() == "Mentlegen.":
                self.settings.set_up_gui()
            else:
                messagebox.showwarning(title= "Psyche!",
                                       message= "I got you, the are no settings :)")
                child.settings_button.place_forget()
                Path("peynir.yeah").unlink()
                child.settings_i_owe_you.place(x=260, y=275, width= 280, height= 50)
