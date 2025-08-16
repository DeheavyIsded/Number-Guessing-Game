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
        self.main_menu_text = tk.Label(self.root,
                                       text= "Number Guessing Game",
                                       font= self.parent.parent.main_menu_font,
                                       background= self.parent.parent.root_background,
                                       foreground= "#0000bb")
        self.add_hover(self.main_menu_text,
                       background= ("#224466", self.parent.parent.root_background),
                       foreground= ("#aaaaff", "#0000bb"),
                       text= (self.parent.hover_texts, "Number Guessing Game"))
        self.main_menu_text.place(x=100, y= 50, height= 100)

        # The start button
        self.parent.start_button = tk.Button(self.root,
                                      text= "  PLAY  ",
                                      font= ("Arial", 20, "bold"),
                                      command= self.parent.start,
                                      background= "#ddeeff",
                                      foreground= "black",
                                      activebackground= "#5d7185",
                                      activeforeground= "white")
        self.add_hover(self.parent.start_button,
                              background= ("#bbccdd", "#ddeeff"))
        self.parent.start_button.place(x=250, y=200,
                                       width= 300, height= 50)
        # The settings button
        self.settings_button = tk.Button(self.root,
                                         text= "  SETTINGS  ",
                                         font= ("Arial", 20, "bold"),
                                         background= "#ddeeff",
                                         foreground= "black",
                                         activebackground= "#5d7185",
                                         activeforeground= "white",
                                         command= lambda: self.parent.check_settings(self))
        self.add_hover(self.settings_button,
                              background= ("#bbccdd", "#ddeeff"))

        # Set the related widget
        if not self.parent.settings_set:
            self.settings_button.place(x=260, y=275, width= 280, height= 50)
        else:
            self.parent.settings_i_owe_you.place(x= 260, y= 275, width= 280, height= 50)

        # The exit button
        self.exit_button = tk.Button(self.root,
                                      text= "  EXIT  ",
                                      font= ("Arial", 20, "bold"),
                                      command= self.on_exit,
                                      background= "#ddeeff",
                                      foreground= "black",
                                      activebackground= "#5d7185",
                                      activeforeground= "white")
        self.add_hover(self.exit_button,
                              background= ("#bbccdd", "#ddeeff"))
        self.exit_button.place(x=280, y=350, width= 240, height= 50)

        # The about button
        self.about_button = tk.Button(self.root,
                                      text= "  ABOUT  ",
                                      font= ("Arial", 10, "bold"),
                                command= lambda: webbrowser.open("https://github.com/DeheavyIsded"),
                                      background= "#88ff88",
                                      foreground= "black",
                                      activebackground= "#2f4d2f",
                                      activeforeground= "white")
        self.add_hover(self.about_button,
                              background= ("#336633", "#88ff88"),
                              foreground= ("white", "black"))
        self.about_button.place(x=650, y=435, width= 100, height= 30)

        # The statistics button
        self.statistics_button = tk.Button(self.root,
                                      text= "  STATISTICS  ",
                                      font= ("Arial", 10, "bold"),
                                      command= self.parent.stats,
                                      background= "#dddd88",
                                      foreground= "black",
                                      activebackground= "#4a4a1e",
                                      activeforeground= "white")
        self.add_hover(self.statistics_button,
                              background= ("#888844", "#dddd88"),
                              foreground= ("white", "black"))
        self.statistics_button.place(x=50, y=435, width= 100, height= 30)

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def add_hover(self,
                  widget,
                  background: tuple[str, str]= (None, None),
                  foreground: tuple[str, str]= (None, None),
                        text: tuple[str, str]= (None, None)) -> None:
        """Add mouse-over effects to the widgets"""

        hover_bg, normal_bg = background
        hover_fg, normal_fg = foreground
        hover_text, normal_text = text

        def on_enter(_):
            new_text = np.random.choice(self.parent.hover_texts) if isinstance(hover_text,
                                                               list) else (
                                                                   hover_text or widget["text"])
            widget.config(background= hover_bg or widget["background"],
                          foreground= hover_fg or widget["foreground"],
                         text= new_text)

        def on_leave(_):
            widget.config(background= normal_bg or widget["background"],
                          foreground= normal_fg or widget["foreground"],
                          text= normal_text or widget["text"])

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def on_exit(self):
        """Run this function during an exit"""
        odds = np.array([0,0,1,0,0])
        if not np.random.choice(odds):
            close: bool = messagebox.askyesno(title= "Exit",
                          message= "You are leaving the game, are you sure?")
            if close:
                self.root.destroy()
            return

        not_close: bool = messagebox.askyesno(title= "Exit",
                      message= "You are leaving the game, are you not sure?")
        if not not_close:
            self.root.destroy()
        else:
            messagebox.showinfo(title= "Understood",
                                message= "You have agreed that you are not sure.")
