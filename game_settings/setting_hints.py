"""Hints menu for the Settings window"""

import tkinter as tk
from itertools import cycle
from .properties import Properties
from .displayer.display_updater import Updater

class Hints:
    """Hints menu for the settings window"""
    def __init__(self, master, parent, permit):

        # >>> Hints Choice Menu
        self.root = master
        self.parent = parent
        self.permit = permit
        self.prp = Properties()

        # The "Hints" title
        hints_title = tk.Label(self.root,
                               text= "                Hints               ",
                               font= ("TF2 Build", 25, "underline"),
                               bg= "gray20",
                               fg= "white")
        hints_title.place(x= 275, y= 75)

        ### The "Hints" Options
        self.hints_yes = tk.BooleanVar(value= False)
        # The name shows the meaning of True value: yes

        self.levels: list[tk.Widget] = [
        self.create_radio_button("Greater of Lesser", 1),
        self.create_radio_button("Temperature", 2),
        self.create_radio_button("Freemium Information", 3),
        self.create_radio_button("Premium Information", 4)
        ]

        self.description: tk.Label = tk.Label(self.root,
                               text= "",
                               bg= "gray20",
                               fg= "yellow",
                               font= ("Arial", 12, "italic"))
        self.description.place(x= 440, y= 150)

        # The "Hints" checkbox
        hints_toggle = tk.Checkbutton(self.root,
                                      text= "Get Hints",
                                      font= ("Arial", 10, "bold"),
                                      bg= "gray20",
                                      selectcolor= "black",
                                      fg= "white",
                                      activebackground= "gray20",
                                      activeforeground= "white",
                                      variable= self.hints_yes,
                                      command= self.check_radio_buttons,
                                      onvalue= True,
                                      offvalue= False)
        hints_toggle.place(x= 275, y= 125)

    def create_radio_button(self, text: str, value: int) -> tk.Radiobutton:
        """Create the radio button, that's it"""

        if not self.hints_yes.get():
            self.parent.hints_chosen_level = "0"

        else:
            self.parent.hints_chosen_level = self.prp.hints_chosen_level

        return tk.Radiobutton(self.root,
                              text= text,
                              bg= "gray20",
                              fg= "white",
                              activebackground= "gray20",
                              activeforeground= "white",
                              selectcolor= "black",
                              variable= self.prp.hints_chosen_level_raw,
                              value= value,
                              command= lambda: self.show_descriptions(value))

    def show_descriptions(self, value: int | None = 0) -> None:
        """Show the descripton of the chosen option"""        

        Updater(self.root, self.parent, self.prp, self.permit).update_hint_level(
            hints_checked= self.hints_yes.get())

        hint_descriptions: dict[int, str]= {
            0: "",
            1: "Shows if your incorrect guess is bigger or smaller",
            2: "Shows the distance of your incorrect guess"
               "\n ... without numbers",
            3: "Gives helpful information about the number",
            4: "Gives less helpful information about the number",}

        if not self.hints_yes.get():
            self.description.config(text= hint_descriptions[0])
            return

        self.description.config(text= hint_descriptions[value])

    def check_radio_buttons(self) -> None:
        """Check the visiblity of Radio Buttons"""

        Updater(self.root, self.parent, self.prp, self.permit).update_hint_level(
            hints_checked= self.hints_yes.get())

        if not self.hints_yes.get():

            for level in self.levels:
                level.place_forget()

            self.show_descriptions()
            return

        coords = cycle((150, 175, 200, 225))

        for level in self.levels:
            level.place(x= 300, y= next(coords))

        self.show_descriptions(self.prp.hints_chosen_level)
