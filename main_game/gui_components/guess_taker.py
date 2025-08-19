"""Takes the user's guess via an entrybox and checks it"""

import tkinter as tk
from tkinter import messagebox

class GuessTaker:
    """An entrybox to take user's guess"""

    def __init__(self, parent):
        self.parent = parent

        self.guess_entrybox = tk.Entry(self.parent.parent.root)
        self.guess_entrybox.place(x= 400, y= 100)

        self.guess_entrybox.bind("<Return>", self.check_entry)

    def check_entry(self, _):
        """After pressed Enter, this method checks the answer"""
        try:
            entry = int(self.guess_entrybox.get())
            entry += 1

        except TypeError:
            messagebox.showerror(title= "Invalid Entry",
                                 message= "You have to enter normal, integer numbers here.")

            self.guess_entrybox.delete(0, tk.END)

        entry -= 1

        if self.parent.parent.game_vals.attemps_left == 0:
            messagebox.showwarning(message= "You are out of your tries")
        

        self.parent.parent.game_vals.attemps_left -= 1
        if entry == self.parent.parent.game_vals.number:
            messagebox.showinfo(title= "Success",
                                message= ("You have guessed correctly, it only took "
f"{self.parent.parent.game_vals.trials - self.parent.parent.game_vals.attempts_left} tries!"))
            return

        self.guess_entrybox.delete(0, tk.END)
        messagebox.showwarning(title= "Incorrect",
                               message= "Your guess is incorrect")
        
