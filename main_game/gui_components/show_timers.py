"""Show the chosen timers"""

import tkinter as tk

class TimerTimer:
    """Class for Timer timer"""

    def __init__(self, sibling):
        self.sibling = sibling
        self.chosen_time_dupe = self.sibling.time_raw

    def tick(self):
        """Countdown"""
        if self.sibling.stop_timer or self.chosen_time_dupe < 0:
            return

        time_text = self.sibling.convert_time(self.chosen_time_dupe)
        self.sibling.timer.config(text= time_text)
        self.chosen_time_dupe -= 1
        self.sibling.parent.parent.root.after(1000, self.tick)

    def start(self):
        """Start the timer"""
        self.tick()

class ChronometerTimer:
    """Class for Chronometer timer"""

    def __init__(self, sibling):
        self.sibling = sibling
        self.total_time: int= 0

    def tick(self):
        """Chronometer starts doing its job"""
        if self.sibling.stop_timer:
            return

        time_text = self.sibling.convert_time(self.total_time)
        self.sibling.timer.config(text= time_text)
        self.total_time += 1
        self.sibling.parent.parent.root.after(1000, self.tick)

    def start(self):
        """Start the chronometer"""
        self.tick()

class TimerManager:
    """Start the related timer"""

    def __init__(self, parent):
        self.parent = parent
        self.stop_timer: bool= False

        if self.parent.parent.prp.timer_custom_time:
            self.time_raw = self.parent.parent.prp.timer_custom_time

        else:
            self.time_raw = self.parent.parent.prp.timer_chosen_time

        self.timer = tk.Label(
            master= self.parent.parent.root,
            text= "",
            font= ("Consolas", 15),
            bg= self.parent.parent.bg,
            fg= "white"
        )

    def stop_timer(self):
        """Give an order to stop the timer"""
        self.stop_timer = True

    def convert_time(self, raw) -> str:
        """Turn the seconds into minutes"""

        seconds = raw % 60
        minutes = raw // 60

        return f"{minutes:02}:{seconds:02}"

    def start(self) -> None:
        """Start the timer"""
        if not self.parent.parent.prp.timer_enabled: # Don't do anything if timer is disabled
            return

        self.timer.place(x= 650, y= 50)

        if self.parent.parent.prp.timer_style == "timer":
            # Initialize Timer timer
            self.timer.config(text= self.convert_time(self.time_raw))
            picked = TimerTimer(self)

        else: # Initialize Chronometer timer
            self.timer.config(text="00:00")
            picked = ChronometerTimer(self)

        picked.start() # Call the assigned class from above
