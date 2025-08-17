"""Update the display text to be up-to-date"""

class Updater:
    """Updaters for the displayer"""
    def __init__(self, _=None, __=None, prp=None, screen=None):
        self.screen = screen
        self.prp = prp
        self.data: dict= {
             "difficulty": prp.difficulty,
            "hints level": prp.hints_chosen_level,
            "timer style": prp.timer_style,
            "chosen time": prp.timer_chosen_time
            }

    def update_difficulty(self) -> None:
        """Update the chosen difficulty to the chosen one"""
        self.screen.difficulty_display.config(text= f"Difficulty: {self.prp.difficulty}")

    def update_hint_level(self, hints_checked: bool) -> None:
        """Update the chosen hint level to the chosen one"""
        
        hint_level = self.screen.hint_level_translator[self.prp.hints_chosen_level] if \
            (self.prp.hints_chosen_level != 0) else "No Hints"

        if hints_checked:
            self.screen.hint_level_display.config(text= f"Hint Level: {hint_level}")

        else:
            self.screen.hint_level_display.config(text= "Hint Level: No Hints")

    def update_timer_style(self, on: bool, style: bool | None=None) -> None:
        """Update the timer style to the chosen one"""

        if not on:
            self.screen.timer_style_display.config(text= "Timer Style: Not Chosen")
            return

        if not style:
            self.screen.timer_style_display.config(text= "Timer Style: Chronometer")

        else:
            self.screen.timer_style_display.config(text= "Timer Style: Timer")

    def update_chosen_time(self) -> None:
        """Update the chosen timer to the chosen one"""
        self.screen.chosen_time_display.config(text= f"Time: {self.prp.timer_chosen_time} seconds")

    def update_general(self=None) -> None:
        """Run every updater"""
        self.update_difficulty()
        self.update_hint_level(hints_checked= False)
        self.update_timer_style(on= False)
        self.update_chosen_time()
