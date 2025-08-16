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
from .displayer import Showcase

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

        # Custom font
        ctypes.windll.gdi32.AddFontResourceW("tf2build.ttf")
        self.title_font = tkFont.Font(
            family= "TF2 Build",
            size= 30,
            weight= "bold",
            underline= 1)

        # >>> >>> Window properties (widgets)
        # Settings title
        self.title = tk.Label(self.root,
                              text= "Settings!",
                              font= self.title_font,
                              fg= "#00ffff",
                              bg= "gray20")
        self.title.place(x= 200, y= 10)

        # "What settings?" button
        self.title_button = tk.Button(self.root,
                                      text="What Settings?",
                                      font= ("Arial", 20, "bold"),
                                      fg= "#b0b0b0",
                                      bg= "#997755",
                                      activebackground= "#553311",
                                      activeforeground= "#f0f0f0",
                                      command= self.settings_set)
        self.add_hover(self.title_button,
                       background= ("#775533","#997755"),
                       foreground= ("#d0d0d0","#b0b0b0"))

        try:
            with open("peynir.yeah", "r", encoding= "utf-8") as file:
                if file.readline() != "Mentlegen":
                    pass
        except FileNotFoundError:
            self.title_button.place(x= 450, y= 10)

        # Load the custom modules' objects
        self.load_modules([Difficulty, Hints, Timer, Showcase])

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def load_modules(self, modules: list):
        """Load each module one by one"""
        for module in modules:
            module(self.root, self)

    def add_hover(self,
                  widget,
                  background: tuple[str, str]= (None, None),
                  foreground: tuple[str, str]= (None, None),
                        text: tuple[str, str]= (None, None)):
        """Add mouse-over effects to the widgets"""          

        hover_bg, normal_bg = background
        hover_fg, normal_fg = foreground
        hover_text, normal_text = text

        def on_enter(_):
            """When pressed"""
            widget.config(bg=hover_bg or widget["bg"],
                          fg=hover_fg or widget["fg"],
                        text=hover_text or widget["text"])
        def on_leave(_):
            """When released"""
            widget.config(bg=normal_bg or widget["bg"],
                          fg=normal_fg or widget["fg"],
                        text=normal_text or widget["text"])

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def settings_set(self):
        """What do you mean they stole the settings button?"""
        messagebox.showinfo(message= 'What? "The Settings button got stolen"?'
                            "\nI'll have to buy a new one, it's not free!")
        with open("peynir.yeah", "x", encoding= "utf-8") as file:
            file.write("Mentlegen.")
            self.title_button.place_forget()

    def on_exit(self) -> None:
        """
        + Where to, Smoke?
        - Unity Station.
        """
        excit: bool = messagebox.askokcancel(title= "Where to?",
                      message= "You cannot run from this menu,"
                                   " complete the set-up now.")
        if not excit:
            messagebox.showinfo(message= "    ok :(")
            self.root.destroy()

if __name__ == "__main__":
    settings_menu: GameSettings = GameSettings()
    settings_menu.set_up_gui()
