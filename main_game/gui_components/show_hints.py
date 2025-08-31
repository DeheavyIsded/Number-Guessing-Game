"""Show hints to help the player"""

import tkinter as tk
import numpy as np

class ShowHints:
    """Special hints about the number"""

    def __init__(self, parent): # For root, game_vals and Properties, you need self.parent.parent
        self.parent = parent

        print(self.parent.parent.game_vals.number)

        self.hints_label = tk.Label(
            master=self.parent.parent.root,
            text="",
            font=("TF2 Build", 13),
            fg="white",
            bg=self.parent.parent.bg
        )
        self.hints_label.place(x=75, y=200)

    def no_hints(self, _) -> None:
        """No hints chosen"""
        self.set_hint(new_text="", new_font="TF2 Build")

    def greater_or_lesser(self, guess: int) -> None: # TODO: Add the dynamic coordinate system!
        """The Greater or Lesser option"""
        hint_text: dict[bool, str]= {
            # True: guess > number, False: guess < number
            False: "The number is higher than your guess",
             True: "The number is lower than your guess"
            }

        self.set_hint(
            new_text=hint_text[(guess > self.parent.parent.game_vals.number)],
            new_font="Times New Roman"
        )

    def temperature(self, guess: int) -> None:
        """The Hot or Cold option"""
        hint_text: list[tuple[int, int, str, str, tuple[int, int]]]= [
         # Low, High, Text, Foreground
        ( 1,10,"Magma Hot!","#aa0000",(205,200)),
        (11,20,"Real Hot!","#ff1000",(215,200)),
        (21,30,"Warmer","#ff3f00",(225,200)),
        (31,40,"Warm","#ffcc00",(230,200)),
        (41,50,"Cool","#297dff",(230,200)),
        (51,60,"Cold","#3ba5ff",(230,200)),
        (61,70,"Really Cold!","#22edff",(205,200)),
        (71,80,"Freezing!","#53fff3",(220,200)),
        (81,87,"Oh my Cold!","#62fff7",(205,200))
        ]

        difference: int= np.abs(self.parent.parent.game_vals.number-guess)
        for low, high, text, color, coordinate in hint_text:
            if low <= difference <= high:
                self.set_hint(
                    new_text=text,
                    new_color=color,
                    new_font="TF2 Build",
                    new_coords=(coordinate[0], coordinate[1])
                )
                break

    def freemium_info(self, guess) -> None: # Add the dynamic coordinate system
        """Useful information"""
        number: int= self.parent.parent.game_vals.number

        situations: list[bool]= [
# All possible stats about the guess and the number
 (number % 2 == 1), # is odd
 (number % 2 == 0), # is even
 (str(guess)[0] == str(number)[0]), # Tens are equal
 (str(guess)[1] == str(number)[1]), # Ones are equal
 (isinstance(np.sqrt(number), int)), # is a perfect square
 (all(number % num != 0 for num in np.arange(2, number//2 + 1))), # is a prime number
 (number % 10 == 0), # divisible by ten
 (np.square(number) == guess), # is the square of your guess
 (np.square(guess) == number), # is the square root of your guess
 (np.sum(int(digit) for digit in str(number)) == np.sum(int(digit) for digit in str(guess))),
 (int(str(number)[0]) == int(str(number)[1]) + 1),
 (str(number)[0] == str(number)[1]), # Digits are equal
 (str(number) == str(number)[::-1]), # Palindrome
 number == 42 # The 42 joke
        ] # Sorry for the mess, tee-hee

        all_info: list[tuple[bool, str]]= [
            (situations [0], "This is an odd number"),
            (situations [1], "This is an even number"),
            (situations [2],f"The tens of this number and {guess} are equal"),
            (situations [3],f"The ones of this number and {guess} are equal"),
            (situations [4], "This number is a perfect square"),
            (situations [5], "This is a prime number"),
            (situations [6], "This number can divide by ten"),
            (situations [7],f"This number is the square root of {guess}"),
            (situations [8],f"This number is the square of {guess}"),
            (situations [9],f"The sum of this numbers digits equal to the sum of {guess}' digits"),
            (situations[10], "This number has consecutive digits"),
            (situations[11], "The digits of this number are the same"),
            (situations[12], "This number is a palindrome"),
            (situations[13], "This number is the meaning of universe, life and everything")
        ]

        chosen_info: list[str]= []
        for situation, text in all_info:
            if situation:
                chosen_info.append(text)

        self.set_hint(
            new_text=np.random.choice(chosen_info),
            new_font="DejaVu Sans Mono"
        )

    def premium_info(self, guess) -> None:
        """Less useful information"""
        hint_text: list[str]=[
            "This number might have two digits",
            "This number could be a positive number",
            "Your guess is incorrect",
            "This number is not equal to your guess",
            "You can actually write this number\nif you have a pen",
            "You can see this number online if you Google it",
            "This number contains no letters",
            "Name of the first digit of this number\nStarts with a number in the alphabet",
            "The decimal digit of this number is not zero",
            "Your guess is closer to this number than 1.000.000",
           f"Stuck? Try {self.parent.parent.game_vals.number}",
            "Try using the numpad at the right side of your keyboard",
           f"This number does not equal to {guess}",
           f"Here is a random number: ({self.parent.parent.game_vals.number-guess})",
           f"{guess} is a brilliant choice,\nit shows your excellence in guessing incorrectly",
            "Division of this number and 100 would never equal to 1",
            "You should try a different number",
            "There are 89 different possible options in total",
           f"With {guess} checked, {89-len(self.parent.misguess.misguesses_raw)} options left",
            "Did you try 10 and 99 yet?"
        ]

        hint_coords: dict[str, tuple[int, int]]={
            hint_text[0]:(125,200),
            hint_text[1]:(100,200),
            hint_text[2]:(165,200),
            hint_text[3]:(100,200),
            hint_text[4]:(125,200),
            hint_text[5]:(75,200),
            hint_text[6]:(125,200),
            hint_text[7]:(100,200),
            hint_text[8]:(75,200),
            hint_text[9]:(75,200),
            hint_text[10]:(205,200),
            hint_text[11]:(75,200),
            hint_text[12]:(125,200),
            hint_text[13]:(135,200),
            hint_text[14]:(75,200),
            hint_text[15]:(75,200),
            hint_text[16]:(125,200),
            hint_text[17]:(75,200),
            hint_text[18]:(125,200),
            hint_text[19]:(150,200)
        }

        chosen = np.random.choice(hint_text)

        self.set_hint(
            new_text=chosen,
            new_font="Lucida Sans Unicode",
            new_coords=hint_coords[chosen]
        )

    def set_hint(self, **kwargs) -> None:
        """
        Set the new text for the hints display

        KWARGS:
            new_text: str (The new text)
            new_color: str (Preferably a HEX code)
            new_font: str (Only the family name)
            new_coords: tuple[int, int] (Change the position with x, y)
        """

        defaults: dict={
        "new_text": "",
        "new_color": "#ffffff",
        "new_font": "TF2 Build",
        "new_coords": (100, 200)
        }

        defaults.update(kwargs)

        self.hints_label.config(
            text=defaults["new_text"],
            font= (defaults["new_font"], 13),
            bg=self.parent.parent.bg,
            fg=defaults["new_color"]
        )

        self.hints_label.place_configure(
            x= defaults["new_coords"][0],
            y= defaults["new_coords"][1]
        )
