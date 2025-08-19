"""Generate the random number for the game"""

from numpy import random

class RandomNumber:
    """Random number generation module"""
    
    def __init__(self, parent):
        self.parent = parent

        self.trial_levels: dict[str, int]= {
            "Easy": 10,
            "Medium": 7,
            "Hard": 5
            }

        self._trials: int= self.trial_levels[self.parent.prp.difficulty]
        self._attempts_left: int= self._trials
        self._number: int= random.randint(low= 10, high= 100) # Generate a random 2 digit number

        @property
        def trials(self) -> int:
            """How many trials will the user have in the beginning"""
            return self._trials

        @property
        def attempts_left(self) -> int:
            """How many attempts left"""
            return self._attempts_left

        @attempts_left.setter
        def attempts_left(self, new_amount):
            self._attempts_left = new_amount

        @property
        def number(self) -> int:
            """The number to guess"""
            return self._number
