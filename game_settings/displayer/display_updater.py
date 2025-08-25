"""Update the display text to be up-to-date"""

class Updater:
    """Updaters for the displayer"""
    def __init__(self, prp=None, screen=None):
        self.screen = screen
        self.prp = prp

    def update_difficulty(self) -> None:
        """Update the chosen difficulty to the chosen one"""
        self.screen.difficulty_display.config(text= f"Difficulty: {self.prp.difficulty}")

    def update_hint_level(self, hints_checked: bool) -> None:
        """
        Update the chosen hint level to the chosen one

        Args:
            hints_checked: bool -> Is the "Allow Hints" button checked?
            True = Yes it is
            False = No it isn't
        """
        hint_level_translator: dict[int, str] = {
            0: "No hints",
            1: "Greater or Lesser",
            2: "Temperature (Cold & Hot)",
            3: "Freemium Information",
            4: "Premium Information"
            }

        hint_level = hint_level_translator[self.prp.hints_chosen_level] if \
                                     (self.prp.hints_chosen_level != 0) else "No Hints"

        if hints_checked:
            self.screen.hint_level_display.config(text= f"Hint Level: {hint_level}")

        else:
            self.screen.hint_level_display.config(text= "Hint Level: No Hints")

    def update_timer_style(self) -> None:
        """Update the timer style to the chosen one"""

        if not self.prp.timer_enabled:
            self.screen.timer_style_display.config(text= "Timer Style: Not Chosen")
            self.screen.chosen_time_display.place_forget()
            return

        style = self.prp.timer_style if self.prp.timer_style else "chronometer"

        self.screen.timer_style_display.config(text= f"Timer Style: {style.capitalize()}")

        if self.prp.timer_style == "chronometer":
            self.screen.chosen_time_display.place_forget()

        else:
            self.screen.chosen_time_display.place(x= 430, y= 410)

    def update_chosen_time(self, custom_time: int | None=None) -> None:
        """Update the chosen timer to the chosen one"""

        if not custom_time:
            if self.prp.timer_chosen_time == -1:
                self.screen.chosen_time_display.config(text= "Time: Custom")

            else:
                self.screen.chosen_time_display.config(
                    text= f"Time: {self.prp.timer_chosen_time} seconds"
                )

        elif custom_time:
            self.screen.chosen_time_display.config(text= f"Time: {custom_time} seconds")

        else:
            self.screen.chosen_time_display.config(text= "Time: Not chosen")

    def update_general(self) -> None:
        """Run every updater"""
        self.update_difficulty()
        self.update_hint_level(hints_checked= False)
        self.update_timer_style()
        self.update_chosen_time()
