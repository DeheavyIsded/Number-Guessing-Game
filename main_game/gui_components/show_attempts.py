"""Shows how many attempts have left"""

import tkinter as tk

class AttemptsLeft:
    """A displayer to show how many attempts are left"""
    def __init__(self, parent): # For root, game_vals and prp, you need self.parent.parent
        self.parent = parent

        self.attempt_screen = tk.Label(master= self.parent.parent.root,
                                      text= f"Tries: {self.parent.parent.game_vals.attempts_left}",
                                      font= ("TF2 Build", 15),
                                      bg= self.parent.parent.bg,
                                      fg= "white")
        self.attempt_screen.place(x= 400, y= 160)
