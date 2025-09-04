"""The GUI components"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import numpy as np

class Gui:
    """The class of all main menu GUI components"""

    def __init__(self, master, parent):

        self.root = master
        self.parent = parent

        # Main menu text
        self.main_menu_text = tk.Label(
            master=self.root,
            text="Number Guessing Game",
            font=("TF2 Build", 25, "bold"),
            background=self.parent.parent.root_background,
            foreground="#0000bb"
        )

        self.add_hover(
            widget=self.main_menu_text,
            hover_bg="#224466",
            normal_bg=self.parent.parent.root_background,
            hover_fg="#aaaaff",
            normal_fg="#0000bb",
            hover_text=self.parent.hover_texts,
            normal_text="Number Guessing Game"
        )

        self.main_menu_text.place(x=75,y=50,height=50)

        # The start button
        self.parent.start_button = tk.Button(
            self.root,
            text="  PLAY  ",
            font=("Arial",20,"bold"),
            command=self.parent.start,
            background="#ddeeff",
            foreground="black",
            activebackground="#5d7185",
            activeforeground="white"
        )

        self.add_hover(
            widget=self.parent.start_button,
            hover_bg="#bbccdd",
            normal_bg="#ddeeff"
        )

        self.parent.start_button.place(x=100,y=250,width=100,height=25)

        # The exit button
        self.exit_button = tk.Button(
            self.root,
            text="  EXIT  ",
            font=("Arial",20,"bold"),
            command=self.on_exit,
            background="#ddeeff",
            foreground="black",
            activebackground="#5d7185",
            activeforeground="white"
        )

        self.add_hover(
            widget=self.exit_button,
            hover_bg="#bbccdd",
            normal_bg="#ddeeff"
        )

        self.exit_button.place(x=140,y=350,width=60,height=25)

        # The about button
        self.about_button = tk.Button(
            self.root,
            text="  ABOUT  ",
            font=("Arial",10,"bold"),
            command=lambda: webbrowser.open("https://github.com/DeheavyIsded"),
            background="#88ff88",
            foreground="black",
            activebackground="#2f4d2f",
            activeforeground="white"
        )

        self.add_hover(
            widget=self.about_button,
            hover_bg="#336633",
            normal_bg="#88ff88",
            hover_fg="white",
            normal_fg="black"
        )

        self.about_button.place(x=120,y=300,width=80,height=30)

        # Start the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def add_hover(self=None,**items) -> None:
        """
        Add mouse-over effects to the widgets
        
        Args:
            -widget: tkinter.Widget -> The target widget

            -background: tuple[str, str] -> background colors:
                background= ("hover_bg", "normal_bg")

            -foreground: tuple[str, str] -> foreground colors:
                foreground= ("hover_fg", "normal_fg")

            -text: tuple[str, str] -> texts:
                foreground= ("hover_text", "normal_text")
        """

        # Assign the variables
        widget = items.get("widget", None)
        hover_bg = items.get("hover_bg", None)
        normal_bg = items.get("normal_bg", None)
        hover_fg = items.get("hover_fg", None)
        normal_fg = items.get("normal_fg", None)
        hover_text = items.get("hover_text", None)
        normal_text = items.get("normal_text", None)

        def on_enter1(_):
            new_text: str= np.random.choice(
                self.parent.hover_texts) if isinstance(hover_text, list) else \
                                           (hover_text or widget["text"])

            widget.config(
                background= hover_bg or widget["background"],
                foreground= hover_fg or widget["foreground"],
                text= new_text
            )

        def on_enter2(_):
            widget.config(
                background= hover_bg or widget["background"],
                foreground= hover_fg or widget["foreground"],
                text= hover_text or widget["text"]
            )

        def on_leave(_):
            widget.config(
                background= normal_bg or widget["background"],
                foreground= normal_fg or widget["foreground"],
                text= normal_text or widget["text"]
            )

        on_enter = on_enter1 if self else on_enter2

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def on_exit(self):
        """Run this function during an exit"""
        odds = np.array([0,0,1,0,0])
        if not np.random.choice(odds):
            close: bool = messagebox.askyesno(
                title="Exit",
                message="You are leaving the game, are you sure?"
            )

            if close:
                self.root.destroy()

            return

        not_close: bool = messagebox.askyesno(
            title="Exit",
            message="You are leaving the game, are you not sure?"
        )

        if not not_close:
            self.root.destroy()

        else:
            messagebox.showinfo(
                title="Understood",
                message="You have agreed that you are not sure."
            )
