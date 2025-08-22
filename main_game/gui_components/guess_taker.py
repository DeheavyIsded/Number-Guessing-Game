"""Takes the user's guess via an entrybox and checks it"""

import tkinter as tk
from tkinter import messagebox

class GuessTaker:
    """An entrybox to take user's guess"""

    def __init__(self, parent): # For root, game_vals and prp, you need self.parent.parent
        self.parent = parent

        self.guess_entrybox = tk.Entry(self.parent.parent.root)
        self.guess_entrybox.place(x= 400, y= 100)

        self.guess_entrybox.bind("<Return>", self.check_entry)

    def check_entry(self, _):
        """After pressed Enter, this method checks the answer"""
        try:
            self.entry = int(self.guess_entrybox.get())
            self.entry += 1 
            # Try a basic operation, if self.entry is not an int then this will throw an Error

        except TypeError:
            messagebox.showerror(title= "Invalid Entry",
                                 message= "You have to enter normal, integer numbers here.")

            self.guess_entrybox.delete(0, tk.END)

        self.entry -= 1 # Take that 1 back now, int-test has been passed

        if len(str(self.entry)) != 2:
            messagebox.showwarning(
                title= "Wrong type of number",
                message= "The number to guess is a 2 digit positive natural number"
            )
            return

        if str(self.entry) in self.parent.misguess.misguesses:
            messagebox.showwarning(
                title= "You already tried that",
                message= "You have tried that number before"
            )
            return
            

        # Update the number of trials left, can't be less than zero
        self.parent.parent.game_vals.attempts_left = max(
            0, (self.parent.parent.game_vals.attempts_left - 1)
            )

        # Now update the text that shows the number of trials left
        self.parent.attempts.attempt_screen.config(
            text= f"Tries: {self.parent.parent.game_vals.attempts_left}"
            )

        # If the guess is correct
        if self.entry == self.parent.parent.game_vals.number:

            self.parent.timers.stop_timer

            tries= self.parent.parent.game_vals.trials - self.parent.parent.game_vals.attempts_left
            messagebox.showinfo(
                title= "Success",
                message= f"You have guessed correctly, it only took {tries} tries!"
            )

            self.guess_entrybox.config(state="readonly")
            self.parent.parent.root.configure(background= "#00ff00")

            tk.Label(master= self.parent.parent.root,
                     text= (f"{self.parent.parent.game_vals.number}!"),
                     font= ("TF2 Build", 25),
                     bg= self.parent.parent.bg,
                     fg= "#00ffff",
            ).place(x= 400, y= 50)
            return

        # If the guess is incorrect
        self.guess_entrybox.delete(0, tk.END)
        messagebox.showwarning(title= "Incorrect",
                               message= "Your guess is incorrect")
        self.parent.misguess.add_guess(new_misguess=self.entry)
        self.display_hints()

        # If player is out of tries
        if self.parent.parent.game_vals.attempts_left == 0:
            messagebox.showwarning(message= "You are out of your tries")
            self.guess_entrybox.config(state="readonly")
            self.parent.parent.root.configure(background= "#ff0000")
            

    def display_hints(self):
        """Show hints to help the player"""
        proper_hints: dict= {
            0: self.parent.hints.no_hints,
            1: self.parent.hints.greater_or_lesser,
            2: self.parent.hints.temperature,
            3: self.parent.hints.freemium_info,
            4: self.parent.hints.premium_info
            }

        proper_hints[self.parent.parent.prp.hints_chosen_level](self.entry)
