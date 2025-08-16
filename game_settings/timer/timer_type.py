"""The Timer type choice menu for the Settings -> Timer menu"""

import tkinter as tk
from .timer_timer_time import TimerTimerTime
from ..properties import Properties
from ..displayer.display_updater import Updater

class TimerType:
    """Timer choice menu, Timer | Chronometer"""
    def __init__(self, master: tk.Widget, _, permit):

        self.root = master
        self.permit = permit
        self.timer_enabled: tk.BooleanVar= tk.BooleanVar(value= False)
        self.ttt: TimerTimerTime= TimerTimerTime(self.root, self, self.permit)

        # Checkbox for the timer
        timer_checkbox = tk.Checkbutton(self.root,
                                        text= "Timer",
                                        font= ("Arial", 10, "bold"),
                                        bg= "gray20",
                                        selectcolor= "black",
                                        fg= "white",
                                        activebackground= "gray20",
                                        activeforeground= "white",
                                        variable= self.timer_enabled,
                                        onvalue= True,
                                        offvalue= False,
                                        command= self.check_timer_type_menu)
        timer_checkbox.place(x= 10, y= 325)

        # Title for the timer type selection menu
        self.timer_type_title = tk.Label(self.root,
                               text= "Timer Type",
                               font= ("TF2 Build", 15),
                               bg= "gray20",
                               fg= "cyan")

        self.timer_type_chronometer = tk.Radiobutton(self.root,
                                             text="Chronometer",
                                             font=("Arial", 10, "bold"),
                                             bg="gray20",
                                             fg="white",
                                             selectcolor="black",
                                             activebackground="gray20",
                                             activeforeground="white",
                                             variable= Properties().timer_style_raw,
                                             value="chronometer",
                    command= lambda: self.ttt.check_appearance_status(Properties().timer_style))

        self.timer_type_timer = tk.Radiobutton(self.root,
                                               text="Timer",
                                               font=("Arial", 10, "bold"),
                                               bg="gray20",
                                               fg="white",
                                               selectcolor="black",
                                               activebackground="gray20",
                                               activeforeground="white",
                                               variable= Properties().timer_style_raw,
                                               value="timer",
                  command= lambda: self.ttt.check_appearance_status(Properties().timer_style))

    def check_timer_type_menu(self) -> None:
        """Checks the appearance status of the timer-type menu"""
        Updater(self.root, self, Properties, self.permit).update_timer_style()
        menu_items: list[tk.Widget] = [self.timer_type_title,
                                       self.timer_type_chronometer,
                                       self.timer_type_timer]

        item_coords: dict[tk.Widget: tuple[int, int]] = {
            self.timer_type_title: (10, 350),
            self.timer_type_chronometer: (30, 375),
            self.timer_type_timer: (30, 400)}

        if not self.timer_enabled.get():
            for menu_item in menu_items:
                menu_item.place_forget()
            self.ttt.timer_checked(False)
            return

        for menu_item in menu_items:
            item_x, item_y = item_coords[menu_item]
            menu_item.place(x= item_x, y= item_y)

        Properties().timer_style = "chronometer"
