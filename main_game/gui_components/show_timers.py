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

        # If the timer hits 00:00
        if self.chosen_time_dupe < 0:
            self.out_of_time()
            return

        # If the player finishes before the timer
        if self.sibling.stop_the_timer:
            self.sibling.parent.parent.root.after_cancel(self.ticktack)
            return

        # If the timer hasn't stopped to this point, count down and repeat
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

    def out_of_time(self) -> None:
        """But I'm outta my head when you're not around"""
        self.sibling.parent.parent.root.after(1000, self.stop)
        self.sibling.parent.guesstaker.end_game(message="You are out of time", color= "#ff0000")

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

        # Define important attributes
        self.parent = parent
        self.timer_on = bool()
        self.stop_the_timer = bool()
        self.picked: object

        # Assign the preffered time
        if self.parent.parent.prp.timer_custom_time:
            self.time_raw = self.parent.parent.prp.timer_custom_time

        else:
            self.time_raw = self.parent.parent.prp.timer_chosen_time

        # Enter a different text for each choice
        timer_items: dict[str, tuple(str, tuple[int, int])]= {
            "": ("No pressure", (200,250)),
            "timer": (self.convert_time(self.time_raw), (225,250)),
            "chronometer": ("00:00", (225,250))
        }

        items = timer_items[self.parent.parent.prp.timer_style]

        self.timer = tk.Label( # Widget vals
            master= self.parent.parent.root,
            text= items[0],
            font= ("Consolas", 15),
            bg= self.parent.parent.bg,
            fg= "red"
        )

        self.timer.place(x=items[1][0],y=items[1][1]) # Widget placement

    def stop_timer(self) -> None:
        """Give an order to stop the timer"""
        self.stop_the_timer = True

    def convert_time(self, raw) -> str:
        """Turn the seconds into minutes"""

        seconds = raw % 60
        minutes = raw // 60

        return f"{minutes:02}:{seconds:02}"

    def start(self) -> None:
        """Start the timers"""
        if not self.parent.parent.prp.timer_enabled or self.timer_on:
            return

        self.timer_on = True

        if self.parent.parent.prp.timer_style == "timer":

            # Initialize Timer timer
            self.timer.config(text= self.convert_time(self.time_raw))
            self.picked = TimerTimer(self)

        else:

            # Initialize Chronometer timer
            self.timer.config(text="00:00")
            self.picked = ChronometerTimer(self)

        self.picked.start() # Call the assigned class from above

    def stop(self) -> None:
        """Stop the timers"""
        try:
            self.picked.stop()
        except AttributeError:
            pass

        try:
            self.picked.chosen_time_dupe = self.time_raw
        except AttributeError:
            pass

        try:
            self.picked.total_time = 0
        except AttributeError:
            pass

        finally:
            self.timer_on = True
