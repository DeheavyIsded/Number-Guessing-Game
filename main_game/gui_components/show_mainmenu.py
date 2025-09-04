"""The button to take you back to main menu"""

import tkinter as tk
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

class MainMenuButton:
    """The button to take you back to the main menu"""

    def __init__(self, parent):
        self.parent = parent

        self.main_menu_button = tk.Button(
            master=self.parent.parent.root,
            text="  GO BACK TO MAIN MENU  ",
            fg="black",
            bg="#00ffff",
            command=self.main_menu
        )

        self.replay_button = tk.Button(
            master=self.parent.parent.root,
            text="  REPLAY  ",
            fg="black",
            bg="#ffff00",
            command=self.replay
        )

    def show_buttons(self) -> None:
        """Show the buttons"""

        # Place the Replay button
        self.replay_button.place(x=400, y=250)

        # Place the Main Menu button
        self.main_menu_button.place(x=400, y=300)

    def hide_buttons(self) -> None:
        """Hide the buttons"""
        self.replay_button.place_forget()
        self.main_menu_button.place_forget()

    def main_menu(self) -> None:
        """Go back to main menu"""
        self.hide_buttons() #TODO: Find a way to connect the main menu to here
        self.parent.parent.root.destroy()
        from main_menu import Start
        Start()

    def replay(self) -> None:
        """Restart the game with the same settings"""

        # Restart the Game
        self.hide_buttons()
        self.parent.parent.start_game()

        # Change the windows background to normal
        self.parent.parent.root.config(background=self.parent.parent.bg)
        self.parent.misguess.misguess_list.config(bg=self.parent.parent.bg)
        self.parent.attempts.attempt_screen.config(bg=self.parent.parent.bg)
        self.parent.timers.timer.config(bg=self.parent.parent.bg)

        # Clean the list of incorrect guesses from the last gameplay
        self.parent.misguess.misguesses_raw = []
        self.parent.misguess.misguess_list.delete(0, tk.END)

        # Hide the enormous text that shows the number
        self.parent.guesstaker.number_label.place_forget()

        # Reset the timer
        self.parent.timers.start()
