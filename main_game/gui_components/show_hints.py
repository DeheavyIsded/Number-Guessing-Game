"""Show hints to help the player"""

import numpy as np
import tkinter as tk

class ShowHints:
    """Special hints about the number"""

    def __init__(self, parent): # For root, game_vals and Properties, you need self.parent.parent
        self.parent = parent
        self.hints = tk.Label(master= self.parent.parent.root,
                              text= "",
                              bg= "black",
                              fg= "white")

    def no_hints(self, _) -> None:
        """No hints chosen"""
        self.set_hint("")

    def greater_or_lesser(self, guess: int) -> None:
        """The Greater or Lesser option"""
        hint_text: dict[bool, str]= {
            # True: guess > number, False: guess < number
            False: "The number is higher than your guess",
            True: "The number is lower than your guess"
            }

        self.set_hint(new_text= hint_text[(guess > self.parent.parent.game_vals.number)])

    def temperature(self, guess: int) -> None:
        """The Hot or Cold option"""
        hint_text: list[tuple[int, int, str, str]]= [
            # Low, High, Text, Foreground
        (1, 10, "Magma Hot!", "#aa0000"),
        (11, 20, "Real Hot!", "#ff1000"),
        (21, 30, "Warmer", "#ff3f00"),
        (31, 40, "Warm", "#ffcc00"),
        (41, 50, "Cool", "#297dff"),
        (51, 60, "Cold", "#3ba5ff"),
        (61, 70, "Really Cold!", "#22edff"),
        (71, 80, "Freezing!", "#53fff3"),
        (81, 87, "Oh my Cold!", "#62fff7"),
        (88, 88, "Impossibly Cold!", "#95fff9")
        ]
        
        difference: int= np.abs(self.parent.parent.game_vals.number - guess)
        for low, high, text, color in hint_text:
            if low <= difference <= high:
                self.set_hint(new_text= text, new_color= color)
                break

    def freemium_info(self, _) -> None:
        """Useful information"""

    def premium_info(self, _) -> None:
        """Less useful information"""
        hint_text: list[str]=[
            "This number might have two digits",
            "This number could be a positive number",
            "Your guess is incorrect",
            "This number is not equal to your guess",
            "You can actually write this number\nif you have a pen", # 5
            "You can see this number online if you Google it",
            "This number contains no letters",
            "",
            "",
            "", # 10
            "",
            "",
            "",
            "",
            "", # 15
            "",
            "",
            "",
            "",
            "", # 20
        ]

    def set_hint(self, new_text: str, new_color: str=None) -> None:
        """Set the new text for the hints display"""
        if not new_color:
            self.hints.config(text=new_text, fg="white")
            return

        self.hints.config(text=new_text, fg=new_color)
