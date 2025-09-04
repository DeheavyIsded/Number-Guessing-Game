"""The settings menu for NGG"""

import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import ctypes

# Custom modules of mine
from .setting_difficulty import Difficulty
from .setting_hints import Hints
from .timer import Timer
from .properties import Properties
from .displayer import Showcase
from .displayer.display_updater import Updater

class GameSettings:
    """Set the basic values"""
    def __init__(self):
        pass

    def set_up_gui(self):
        """Set up the GUI for the settings menu"""
        self.root = tk.Tk()
        self.root.title("Settings Menu")
        self.root.geometry("800x600")
        self.root.configure(background= "gray20")
        self.root.iconphoto(False, tk.PhotoImage(
            file= os.path.join(os.path.dirname(__file__), "icon.png")))

        self.prp = Properties()
        self.swc = Showcase(self)
        self.upd = Updater(self.prp, self.swc.give_permit())

        # Custom font
        ctypes.windll.gdi32.AddFontResourceW("tf2build.ttf")
        self.title_font = tkFont.Font(
            family= "TF2 Build",
            size= 30,
            weight= "bold",
            underline= 1
        )

        # >>> >>> Window properties (widgets)
        # Settings title
        self.title = tk.Label(
            self.root,
            text= "Settings!",
            font= self.title_font,
            fg= "#00ffff",
            bg= "gray20"
        )

        self.title.place(x= 200, y= 10)

        # Load the custom modules' objects
        self.load_modules([Difficulty, Hints, Timer])

        self.upd.update_general()
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.update_idletasks()
        self.root.mainloop()

    def load_modules(self, modules: list):
        """Load each module one by one"""
        for module in modules:
            module(self.root, self)

    def add_hover(self, **items):
        """Add mouse-over effects to the widgets"""          

        # Assign the variables
        widget = items.get("widget", None)
        hover_bg = items.get("hover_bg", None)
        normal_bg = items.get("normal_bg", None)
        hover_fg = items.get("hover_fg", None)
        normal_fg = items.get("normal_fg", None)
        hover_text = items.get("hover_text", None)
        normal_text = items.get("normal_text", None)

        # With mouse-over:
        def on_enter(_):
            """When pressed"""
            widget.config(
                bg=hover_bg or widget["bg"],
                fg=hover_fg or widget["fg"],
                text=hover_text or widget["text"]
            )

        # Without mouse-over:
        def on_leave(_):
            """When released"""
            widget.config(
                bg=normal_bg or widget["bg"],
                fg=normal_fg or widget["fg"],
                text=normal_text or widget["text"]
            )

        # Bind the functions here
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def on_exit(self) -> None:
        """
        + Where to, Smoke?
        - Unity Station.
        """
        excit: bool = messagebox.askokcancel(
            title= "Where to?",
            message= "You cannot run from this menu,"
                     " complete the set-up now."
        )

        if not excit:
            messagebox.showinfo(message= "    ok :(")
            self.root.destroy()

if __name__ == "__main__":
    settings_menu: GameSettings = GameSettings()
    settings_menu.set_up_gui()
