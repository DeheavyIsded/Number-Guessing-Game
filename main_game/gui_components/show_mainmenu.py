"""The button to take you back to main menu"""

import tkinter as tk
from tkinter import messagebox

class MainMenuButton:
    """The button to take you back to the main menu"""

    def __init__(self, parent):
        self.parent=parent

        self.main_menu = tk.Button(
            master=self.parent.parent.root,
            text="  GO BACK TO MAIN MENU  ",
            command=self.main_menu
        )

        self.replay = tk.Button(
            master=self.parent.parent.root,
            text="  REPLAY  ",
            command=self.replay
        )

    def main_menu(self):
        """Go back to main menu"""
        pass #TODO: Find a way to connect the main menu to here

    def replay(self):
        """Restart the game with the same settings"""
        self.parent.parent.start_game() #TODO: Test this feature
