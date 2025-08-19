"""Generate the random number for the game"""

from numpy import random

class RandomNumber:
    """Random number generation module"""
    
    def __init__(self, parent):
        self.parent = parent

        self.trials: list[str, int]= {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3
            }

        print(self.trials[self.parent.prp.difficulty])        
