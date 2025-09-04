"""The Difficulty setting for the settings menu"""

import tkinter as tk

class Difficulty:
    """The Difficulty menu for the settings menu"""
    def __init__(self, _, parent):

        # >>> Difficulty choosing menu
        self.parent = parent

        # The "Difficulty" title
        difficulty_title = tk.Label(
            self.parent.root,
            text= "Difficulty",
            font= ("TF2 Build", 25, "underline"),
            bg= "gray20",
            fg= "white"
        )
        title_y = 75
        difficulty_title.place(x= 10, y= title_y)

        # The Difficulty options; easy, medium, hard
        difficulty_options: tuple[dict[str, str]]= (
            {"text":"Easy", "bg":"#33aa33", "fg":"white", "y_coord":title_y+60},
            {"text":"Medium", "bg":"#bfbf11", "fg":"white", "y_coord":title_y+100},
            {"text":"Hard", "bg":"#bf1111", "fg":"white", "y_coord":title_y+140}
        )

        for opt in difficulty_options:
            option_button = tk.Radiobutton(
                self.parent.root,
                text= opt["text"],
                variable= self.parent.prp.difficulty_raw,
                value= opt["text"],
                font=("TF2 Build", 16),
                bg= opt["bg"],
                fg= opt["fg"],
                activebackground= self.decrease_color_hue(opt["bg"], 50),
                selectcolor= self.decrease_color_hue(opt["bg"], 50),
                indicatoron= True,
                command= self.parent.upd.update_difficulty
            )
            option_button.place(x= 10, y= opt["y_coord"])

    def decrease_color_hue(self, color: str, amount: str) -> str:
        """Decrease the hue of the given Hexidecimal color"""
        color = color.lstrip("#")

        red: int = int(color[0:2], 16)
        green: int = int(color[2:4], 16)
        blue: int = int(color[4:6], 16)

        new_red: int = min(255, max(0, (red - amount)))
        new_green: int = min(255, max(0, (green - amount)))
        new_blue: int = min(255, max(0, (blue - amount)))

        return f"#{new_red:02x}{new_green:02x}{new_blue:02x}"

    def shut_up_code_analyzer(self) -> type:
        """Placeholder for Refactor R0903"""
        return int
