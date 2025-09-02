"""GUI of the Number Guessing Game"""

from .guess_taker import GuessTaker
from .show_attempts import AttemptsLeft
from .show_hints import ShowHints
from .show_misguesses import Misguess
from .show_timers import TimerManager
from .show_mainmenu import MainMenuButton

class NGGui: # Root: self.parent.root
    """GUI of the game"""
    def __init__(self, parent):

        self.parent = parent

        self.misguess = Misguess(self)
        self.hints = ShowHints(self)
        self.attempts = AttemptsLeft(self)
        self.timers = TimerManager(self)
        self.main_menu = MainMenuButton(self)
        self.guesstaker = GuessTaker(self)
