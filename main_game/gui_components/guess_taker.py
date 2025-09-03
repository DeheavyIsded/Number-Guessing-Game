"""Takes the user's guess via an entrybox and checks it"""

import tkinter as tk
from tkinter import messagebox

class GuessTaker:
    """An entrybox to take user's guess"""

    def __init__(self, parent): # For root, game_vals and prp, you need self.parent.parent

        # Define important attributes
        self.parent = parent
        self.entry: object

        # Place the entrybox for guesses
        self.guess_entrybox = tk.Entry(self.parent.parent.root)
        self.guess_entrybox.place(x= 200, y= 100)

        # This label will show the correct number at the end of each game
        self.number_label = tk.Label(
            master=self.parent.parent.root,
            font=("TF2 Build",100)
        )

        self.guess_entrybox.bind("<Return>", self.check_entry)

    def check_entry(self, _):
        """After pressed Enter, this method checks the answer"""
        try:
            # Try a basic operation, if self.entry is not an int then this will throw an Error
            self.entry = int(self.guess_entrybox.get())

        except ValueError:
            # Catch an error and this means the player entered an invalid number
            messagebox.showerror(
                title= "Invalid Entry",
                message= "You have to enter normal, integer numbers here."
            )

            self.guess_entrybox.delete(0, tk.END)
            return

        # If the user enters a non-2-digit number
        if self.entry < 10 or self.entry > 99:
            messagebox.showwarning(
                title= "Wrong type of number",
                message= "The number to guess is a 2-digit natural number"
            )
            return

        # If the player tries to enter the same number
        if self.entry in self.parent.misguess.misguesses:
            messagebox.showwarning(
                title= "You already tried that",
                message= "You have tried that number before"
            )
            return

        # Update the number of trials left, can't be less than zero
        self.parent.parent.game_vals.attempts_left = max(
            0, (self.parent.parent.game_vals.attempts_left-1)
        )

        # Now update the text that shows the number of trials left
        self.parent.attempts.attempt_screen.config(
            text= f"Tries: {self.parent.parent.game_vals.attempts_left}"
        )

        # If the guess is correct
        if self.entry == self.parent.parent.game_vals.number:

            # Stop the timer
            self.parent.timers.stop()

            # Show a messagebox to inform the player that the game ended
            tries= self.parent.parent.game_vals.trials-self.parent.parent.game_vals.attempts_left
            self.end_game(
                message=f"You have guessed correctly, it only took {tries} tries!",
                color="#00ff00"
            )
            return

        # If the guess is incorrect
        self.guess_entrybox.delete(0, tk.END)
        messagebox.showwarning(title="Incorrect",message="Your guess is incorrect")

        # If player is out of tries
        if self.parent.parent.game_vals.attempts_left == 0:
            self.end_game(
                message="You are out of your tries",
                color="#ff0000"
            )
            return

        # Add the new mistake to the list
        self.parent.misguess.add_guess(new_misguess=self.entry)

        # Show a hint
        self.display_hints()

        # Trigger the timer, won't work if it already started
        self.parent.timers.start()

    def end_game(self, message, color):
        """End the game"""
        # Stop the working functions
        self.parent.hints.lock = True
        self.parent.timers.stop()

        # Display the mssage
        messagebox.showwarning(message=message)

        # Lock the Entry-box
        self.guess_entrybox.config(state="readonly")

        # Change the GUI colors
        self.parent.parent.root.configure(background=color)
        self.parent.misguess.misguess_list.config(bg=color)
        self.parent.attempts.attempt_screen.config(bg=color)
        self.parent.timers.timer.config(bg=color)

        # Hide some of them
        self.parent.hints.hints_label.place_forget()

        background: dict[str, str]= {
            "#00ff00":"#ff0000",
            "#ff0000":"#00ff00"
        }

        # Show a label to display the correct number
        self.number_label.config(
            text=(f"{self.parent.parent.game_vals.number}!"),
            fg=background[color],
            bg=color
        )
        self.number_label.place(x=375,y=50)

        # Show the "Play Again" and "Go To Main Menu", buttons
        self.parent.main_menu.show_buttons()

    def display_hints(self):
        """Show hints to help the player"""
        # Assign the function to be called by the hint level
        proper_hints: dict= {
            0: self.parent.hints.no_hints,
            1: self.parent.hints.greater_or_lesser,
            2: self.parent.hints.temperature,
            3: self.parent.hints.freemium_info,
            4: self.parent.hints.premium_info
        }

        # function_from_somewhere(self.entry)
        proper_hints[self.parent.parent.prp.hints_chosen_level](self.entry)
