"""
A fresh file to hold the properties

Held properties:
    
    *difficulty: Chosen difficulty level
    
    *timer_style: Chosen timer style
    
    *timer_chosen_time: Chosen seconds of time for timer
    
    *hints_chosen_level: Chosen level of given hints
"""

import tkinter

class Properties:
    """
    This class is responsible for holding the properties 
    given each one their own Getters and Setters
    
    Held properties:
    
        *difficulty
        
        *timer_style
        
        *timer_chosen_time
        
        *hints_chosen_level
    """
    def __init__(self) -> None:

        self.__difficulty: tkinter.StringVar
        self.__timer_style: tkinter.StringVar
        self.__timer_chosen_time: tkinter.IntVar
        self.__hints_chosen_level: tkinter

    # >>> Getters
    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def timer_style(self):
        return self.__timer_style

    @property
    def timer_chosen_time(self):
        return self.__timer_chosen_time

    @property
    def hints_chosen_level(self):
        return self.__hints_chosen_level

    # >>> Setters
    @difficulty.setter
    def difficulty(self, new_difficulty):
        self.__difficulty = new_difficulty

    @timer_style.setter
    def timer_style(self, new_timer_style):
        self.__timer_style = new_timer_style

    @timer_chosen_time.setter
    def timer_chosen_time(self, new_timer_chosen_time):
        self.__timer_chosen_time = new_timer_chosen_time

    @hints_chosen_level.setter
    def hints_chosen_level(self, new_level):
        self.__hints_chosen_level = new_level
