"""The Timer type choice menu for the Settings -> Timer menu"""

import tkinter as tk
from .timer_timer_time import TimerTimerTime

class TimerType:
    """Timer choice menu, Timer | Chronometer"""
    def __init__(self, parent):

        self.parent = parent
        self.time: TimerTimerTime= TimerTimerTime(self)

        # Checkbox for the timer
        timer_checkbox = tk.Checkbutton(self.parent.root,
                                        text= "Timer",
                                        font= ("Arial", 10, "bold"),
                                        bg= "gray20",
                                        selectcolor= "black",
                                        fg= "white",
                                        activebackground= "gray20",
                                        activeforeground= "white",
                                        variable= self.parent.parent.prp.timer_enabled_raw,
                                        onvalue= True,
                                        offvalue= False,
                                        command= self.check_timer_type_menu)

        timer_checkbox.place(x= 10, y= 325)

        # Title for the timer type selection menu
        self.timer_type_title = tk.Label(self.parent.root,
                               text= "Timer Type",
                               font= ("TF2 Build", 15),
                               bg= "gray20",
                               fg= "cyan")

        self.timer_type_chronometer = tk.Radiobutton(self.parent.root,
                                             text="Chronometer",
                                             font=("Arial", 10, "bold"),
                                             bg="gray20",
                                             fg="white",
                                             selectcolor="black",
                                             activebackground="gray20",
                                             activeforeground="white",
                                             variable= self.parent.parent.prp.timer_style_raw,
                                             value="chronometer",
                                             command= self.time.check_appearance_status)

        self.timer_type_timer = tk.Radiobutton(self.parent.root,
                                               text="Timer",
                                               font=("Arial", 10, "bold"),
                                               bg="gray20",
                                               fg="white",
                                               selectcolor="black",
                                               activebackground="gray20",
                                               activeforeground="white",
                                               variable= self.parent.parent.prp.timer_style_raw,
                                               value="timer",
                                               command= self.time.check_appearance_status)

    def check_timer_type_menu(self) -> None:
        """Checks the appearance status of the timer-type menu"""
        self.parent.parent.upd.update_timer_style()
        self.parent.parent.upd.update_chosen_time()

        menu_items: list[tk.Widget] = [self.timer_type_title,
                                       self.timer_type_chronometer,
                                       self.timer_type_timer]

        item_coords: dict[tk.Widget: tuple[int, int]] = {
            self.timer_type_title: (10, 350),
            self.timer_type_chronometer: (30, 375),
            self.timer_type_timer: (30, 400)}

        # Is the Timer box checked?
        if not self.parent.parent.prp.timer_enabled:

            # For no:
            for menu_item in menu_items:
                menu_item.place_forget()

            self.time.timer_checked(False)
            return

        # For yes:
        for menu_item in menu_items:
            item_x, item_y = item_coords[menu_item]
            menu_item.place(x= item_x, y= item_y)
            self.parent.parent.upd.update_timer_style()
            self.parent.parent.upd.update_chosen_time()

        self.parent.parent.prp.timer_style = "chronometer"
