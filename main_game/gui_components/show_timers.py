"""Show the chosen timers"""

import tkinter as tk

class TimerTimer:
    """Class for Timer timer"""

    def __init__(self, sibling):
        self.sibling = sibling
        self.chosen_time_dupe = self.sibling.time_raw
        self.ticktack = None

    def tick(self):
        """Countdown"""
        if self.chosen_time_dupe < 0:
            return

        if self.sibling.stop_the_timer:
            self.sibling.parent.parent.root.after_cancel(self.ticktack)
            return

        time_text = self.sibling.convert_time(self.chosen_time_dupe)
        self.sibling.timer.config(text= time_text)
        self.chosen_time_dupe -= 1
        self.ticktack = self.sibling.parent.parent.root.after(1000, self.tick)

    def start(self):
        """Start the timer"""
        self.tick()

    def stop(self) -> None:
        """Stop the timer"""
        if self.ticktack:
            self.sibling.parent.parent.root.after_cancel(self.ticktack)
            self.ticktack = None

class ChronometerTimer:
    """Class for Chronometer timer"""

    def __init__(self, sibling):
        self.sibling = sibling
        self.total_time: int= 0
        self.ticktack = None

    def tick(self) -> None:
        """Chronometer starts doing its job"""
        if self.sibling.stop_the_timer:
            self.sibling.parent.parent.root.after_cancel(self.ticktack)
            return

        time_text = self.sibling.convert_time(self.total_time)
        self.sibling.timer.config(text= time_text)
        self.total_time += 1
        self.ticktack = self.sibling.parent.parent.root.after(1000, self.tick)

    def start(self) -> None:
        """Start the chronometer"""
        self.tick()

    def stop(self) -> None:
        """Stop the chronometer"""
        if self.ticktack:
            self.sibling.parent.parent.root.after_cancel(self.ticktack)
            self.ticktack = None

class TimerManager:
    """Start the related timer"""

    def __init__(self, parent):
        self.parent = parent
        self.timer_on: bool= False
        self.stop_the_timer: bool= False

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
        self.stop_the_timer = True # FIXME: Chronometer resets when stopped

    def convert_time(self, raw) -> str:
        """Turn the seconds into minutes"""

        seconds = raw % 60
        minutes = raw // 60

        return f"{minutes:02}:{seconds:02}"

    def start(self) -> None:
        """Start the timers"""
        if not self.parent.parent.prp.timer_enabled or self.timer_on:
            return

        self.timer.place(x= 650, y= 50)
        self.timer_on = True

        if self.parent.parent.prp.timer_style == "timer":
            # Initialize Timer timer
            self.timer.config(text= self.convert_time(self.time_raw))
            self.picked = TimerTimer(self)

        else: # Initialize Chronometer timer
            self.timer.config(text="00:00")
            self.picked = ChronometerTimer(self)

        self.picked.start() # Call the assigned class from above

    def stop(self) -> None:
        """Stop the timers"""
        self.picked.stop()
