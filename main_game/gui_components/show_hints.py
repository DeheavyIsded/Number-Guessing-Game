"""Show hints to help the player"""

import numpy as np
import tkinter as tk

class ShowHints:
    """Special hints about the number"""

    def __init__(self, parent): # For root, game_vals and Properties, you need self.parent.parent
        self.parent = parent
        self.hints_label = tk.Label(master= self.parent.parent.root,
                              text= "",
                              fg= "white")
        self.hints_label.place(x= 400, y= 200)

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

    def freemium_info(self, guess) -> None:
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
 (str(number) == str(number)[::-1]) # Palindrome
        ]

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
        ]

        chosen_info: list[str]= []
        for situation, text in all_info:
            if situation:
                chosen_info.append(text)

        self.set_hint(new_text= np.random.choice(chosen_info))

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
           f"With {guess} checked, {89-self.parent.parent.game_vals.attempts_left} options left",
            "Did you try 10 and 99 yet?"
        ]

        self.set_hint(new_text=np.random.choice(hint_text))

    def set_hint(self, new_text: str, new_color: str=None) -> None:
        """Set the new text for the hints display"""
        if not new_color:
            self.hints_label.config(text=new_text, bg=self.parent.parent.bg, fg="white")
            return

        self.hints_label.config(text=new_text, bg=self.parent.parent.bg, fg=new_color)
