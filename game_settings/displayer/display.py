"""Display the chosen settings"""

import tkinter as tk
from ..properties import Properties
from .display_updater import Updater

class Display:
    """Display the chosen settings"""

    def __init__(self, master):

        self.root = master
        self.prp = Properties()
        self.upd = Updater(self.root, self, self.prp, self)

        # GUI components
        gui_components: list[tk.Widget] = []
        gui_font: tuple[str, int]= ("TF2 Build", 9)

        # Difficulty display
        self.difficulty_display = tk.Label(self.root, font= gui_font)
        gui_components.append(self.difficulty_display)

        # Hint Level display
        self.hint_level_translator: dict[int, str] = {
            0: "No hints",
            1: "Greater or Lesser",
            2: "Temperature (Cold & Hot)",
            3: "Freemium Information",
            4: "Premium Information"
            }

        self.hint_level_display = tk.Label(self.root,
                                      font= gui_font)
        gui_components.append(self.hint_level_display)

        # Timer Style display
        self.timer_style_display = tk.Label(self.root,
                                       font= gui_font)
        gui_components.append(self.timer_style_display)

        # Chosen Time display
        self.chosen_time_display = tk.Label(self.root, # pylint: disable = unused-variable
                                       font= gui_font)

        component_coords: list[tuple[int, int]] = [
            (430, 320), # Coordinates of Difficulty display
            (430, 350), # Coordinates of Hint level display
            (430, 380)  # Coordinates of Timer Style display
            ]

        self.place_widgets(gui_components, component_coords)

    def place_widgets(self, components, coords):
        """Place the widgets"""
        for component, coordinate in zip(components, coords):
            comp_x, comp_y = coordinate
            component.place(x= comp_x, y= comp_y)

    def give_permit(self):
        """Give permission to use display_updater"""
        return self
