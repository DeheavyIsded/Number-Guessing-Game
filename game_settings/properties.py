"""
A fresh file to hold the properties

Held properties:
    
    *difficulty: Chosen difficulty level
    
    *timer_style: Chosen timer style
    
    *timer_chosen_time: Chosen seconds of time for timer
    
    *hints_chosen_level: Chosen level of given hints
    
    *timer_enabled
    
    *timer_custom_time
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
        
        *timer_enabled
        
        *timer_custom_time
    """
    def __init__(self) -> None:

        self.difficulty_raw: tkinter.StringVar = tkinter.StringVar(value= "Medium")
        self.timer_style_raw: tkinter.StringVar = tkinter.StringVar(value= None)
        self.timer_chosen_time_raw: tkinter.IntVar = tkinter.IntVar(value= 40)
        self.hints_chosen_level_raw: tkinter.IntVar = tkinter.IntVar(value= 0)
        self.timer_enabled_raw: tkinter.BooleanVar = tkinter.BooleanVar(value= False)
        self.timer_custom_time_raw: tkinter.IntVar = tkinter.IntVar(value= 0)

    # >>> Getters
    @property
    def difficulty(self) -> tkinter.StringVar:
        """Getter for Difficulty"""
        return self.difficulty_raw.get()

    @property
    def timer_style(self) -> tkinter.StringVar:
        """Getter for Timer Style"""
        return self.timer_style_raw.get()

    @property
    def timer_chosen_time(self) -> tkinter.IntVar:
        """Getter for Chosen Time"""
        return self.timer_chosen_time_raw.get()

    @property
    def hints_chosen_level(self) -> tkinter.IntVar:
        """Getter for Hint Level"""
        return self.hints_chosen_level_raw.get()

    @property
    def timer_enabled(self) -> tkinter.BooleanVar:
        """Getter for Timer Enabled"""
        return self.timer_enabled_raw.get()

    @property
    def timer_custom_time(self) -> tkinter.IntVar:
        """Getter for Custom Time"""
        return self.timer_custom_time_raw

    # >>> Setters
    @difficulty.setter
    def difficulty(self, new_difficulty):
        self.difficulty_raw.set(new_difficulty)

    @timer_style.setter
    def timer_style(self, new_timer_style):
        self.timer_style_raw.set(new_timer_style)

    @timer_chosen_time.setter
    def timer_chosen_time(self, new_timer_chosen_time):
        self.timer_chosen_time_raw.set(new_timer_chosen_time)

    @hints_chosen_level.setter
    def hints_chosen_level(self, new_level):
        self.hints_chosen_level_raw.set(new_level)

    @timer_enabled.setter
    def timer_enabled(self, new_status):
        self.timer_enabled_raw.set(new_status)

    @timer_custom_time.setter
    def timer_custom_time(self, new_time):
        self.timer_custom_time_raw.set(new_time)
