"""Main Settings -> Timer Menu"""

import tkinter as tk
from .timer_type import TimerType
from ..properties import Properties

class Timer:
    """Main class for the menu"""
    def __init__(self, master, _, permit):

        # >>> Timer choice menu
        self.root = master
        self.permit = permit
        self.prp = Properties()

        # Title for the main menu
        timer_title = tk.Label(self.root,
                               text= "Timer",
                               font= ("TF2 Build", 25, "underline"),
                               bg= "gray20",
                               fg= "white")
        timer_title.place(x= 10, y= 275)
        TimerType(self)
