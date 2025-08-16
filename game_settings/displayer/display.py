"""Display the chosen settings"""

import tkinter as tk
from ..properties import Properties
from .display_updater import Updater

class Display:
    """Display the chosen settings"""

    def __init__(self, master):

        self.root = master
        self.prp = Properties()
        self.upd = Updater(self.root, self, self.prp)

        # GUI components
        gui_components: list[tk.Widget] = []

        # Difficulty display
        difficulty_display = tk.Label(self.root, text= f"Difficulty: {self.prp.difficulty}")
        gui_components.append(difficulty_display)

        # Hint Level display
        hint_level_translator: dict[int, str] = {
            0: "No hints",
            1: "Greater or Lesser",
            2: "Temperature (Cold & Hot)",
            3: "Freemium Information",
            4: "Premium Information"
            }

        hint_level_display = tk.Label(self.root, text= f"Hint Level: {hint_level_translator[self.prp.hints_chosen_level]}")
        gui_components.append(hint_level_display)

        # Timer Style display        
        timer_style_display = tk.Label(self.root, text= f"Timer Style: {self.prp.timer_style.capitalize()}")
        gui_components.append(timer_style_display)

        # Chosen Time display
        chosen_time_display = tk.Label(self.root, text= f"Difficulty: {self.prp.timer_chosen_time} seconds")

        component_coords: list[tuple[int, int]] = [
            (430, 300), # Coordinates of Difficulty display
            (430, 320), # Coordinates of Hint level display
            (430, 340) # Coordinates of Timer Style display
            ]

        for component, coordinate in zip(gui_components, component_coords):
            comp_x, comp_y = coordinate
            component.place(x= comp_x, y= comp_y)
