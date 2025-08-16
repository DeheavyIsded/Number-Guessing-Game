"""Time selection menu for the Timer choice of the Timer menu"""

import tkinter as tk
from tkinter import messagebox
from .timer_timer_help import HelpMe
from ..properties import Properties

class TimerTimerTime:
    """This name is embarassing"""
    def __init__(self, master: tk.Widget, _) -> None:

        self.root = master
        Properties.timer_chosen_time: tk.IntVar= tk.IntVar(value= 40)
        self.help: HelpMe= HelpMe(self.root, self)

        # >>> The Timer-Timer—Sub-Menu
        # The "Timer's Time" title
        self.timer_timer_time_title= tk.Label(self.root,
                                         text= "Timer's Time",
                                         font= ("TF2 Build", 15),
                                         bg= "gray20",
                                         fg= "#00ff00")
        # The time options
        self.timer_time_40: tk.Radiobutton= self.create_radio_buttons("40 seconds", 40)
        self.timer_time_60: tk.Radiobutton= self.create_radio_buttons("60 seconds", 60)
        self.timer_time_100: tk.Radiobutton= self.create_radio_buttons("100 seconds", 100)

        self.timer_time_custom: tk.Radiobutton= tk.Radiobutton(self.root,
                                                               text= " Custom time",
                                                               font= ("Arial", 12),
                                                             variable= Properties.timer_chosen_time,
                                                               value= (-1),
                                                               command= self.summon_entrybox,
                                                               bg= "gray20",
                                                               fg= "white",
                                                               activebackground= "gray20",
                                                               activeforeground= "white",
                                                               selectcolor= "black")
        self.timer_custom_entrybox: tk.Entry= tk.Entry(self.root,
                                                    font= ("Consolas", 10),
                                                    bg= "#a0a0a0",
                                                    fg= "black",
                                                    selectbackground= "#909090",
                                                    selectforeground= "gray",
                                                    state= tk.NORMAL)
        self.timer_custom_entrybox.bind("<Return>", self.get_input)

    def get_input(self, _):
        """Validate the user's input"""
        user_input: str= self.timer_custom_entrybox.get()
        new_input: int
        try:
            new_input = abs(int(user_input))
            self.timer_custom_entrybox.config(state= "readonly")
            Properties.timer_chosen_time = new_input

        except ValueError:
            self.timer_custom_entrybox.delete(0, tk.END)
            messagebox.showerror(title= "Invalid Number",
                               message= "Try entering a normal-integer number.\n Please.")

    def create_radio_buttons(self, text: str, value: int) -> tk.Radiobutton:
        """Create the radio button"""
        return tk.Radiobutton(self.root,
                              text= text,
                              font= ("Arial", 12),
                              variable= Properties.timer_chosen_time,
                              value= value,
                              bg= "gray20",
                              fg= "white",
                              activebackground= "gray20",
                              activeforeground= "white",
                              selectcolor= "black",
                              command= self.refresh_custom)
    def timer_checked(self, checked: bool) -> None:
        """Dissapear if Timer checkbox is unchecked"""
        our_widgets: list[tk.Widget]= [self.timer_timer_time_title,
                                       self.timer_time_40,
                                       self.timer_time_60,
                                       self.timer_time_100,
                                       self.timer_time_custom,
                                       self.timer_custom_entrybox]
        if not checked:
            for widget in our_widgets:
                widget.place_forget()

    def refresh_custom(self):
        """Delete the text"""
        self.help.button_placement()
        self.timer_custom_entrybox.place_forget()
        self.timer_custom_entrybox.config(state= tk.NORMAL)
        self.timer_custom_entrybox.delete(0, tk.END)

    def check_appearance_status(self, timer_type: str) -> None:
        """Control the visiblity of the widget"""
        submenu_items: list[tk.Widget]= [self.timer_timer_time_title,
                                         self.timer_time_40,
                                         self.timer_time_60,
                                         self.timer_time_100,
                                         self.timer_time_custom]
        submenu_item_coords: dict[tk.Widget, tuple[int, int, int]]= {
            self.timer_timer_time_title:(50, 425),
            self.timer_time_40: (70, 450),
            self.timer_time_60: (70, 475),
            self.timer_time_100: (70, 500),
            self.timer_time_custom: (70, 525)}

        if timer_type != "timer":
            for submenu_item in submenu_items:
                submenu_item.place_forget()
            self.timer_custom_entrybox.place_forget()
            return
        for submenu_item in submenu_items:
            item_x, item_y = submenu_item_coords[submenu_item]
            submenu_item.place(x= item_x, y= item_y)
        Properties.timer_chosen_time = 40

    def summon_entrybox(self):
        """As the name suggests"""
        self.help.button_placement()
        if Properties.timer_chosen_time != -1:
            self.timer_custom_entrybox.place_forget()
            return
        self.timer_custom_entrybox.place(x= 200, y= 530, width= 50)
