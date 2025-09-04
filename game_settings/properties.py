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
    def __init__(self, no_reset: int | None=None) -> None:
        """
        Parameters
        ----------
        no_reset : int | None, optional

        o------------------------------o
            If has a value, the values won't be assigned to the properties preventing a reset.

            Default is None. If no parameters are given, the properties will be assgined a value

        Returns None
        """
        if no_reset is None:
            self.difficulty_raw: tkinter.StringVar = tkinter.StringVar(value= "Medium")
            self.timer_style_raw: tkinter.StringVar = tkinter.StringVar(value= None)
            self.timer_chosen_time_raw: tkinter.IntVar = tkinter.IntVar(value= 40)
            self.hints_chosen_level_raw: tkinter.IntVar = tkinter.IntVar(value= 0)
            self.timer_enabled_raw: tkinter.BooleanVar = tkinter.BooleanVar(value= False)
            self.timer_custom_time_raw: tkinter.IntVar = tkinter.IntVar(value= 0)

    # >>> Getters
    @property
    def difficulty(self) -> str:
        """Getter for Difficulty"""
        return self.difficulty_raw.get()

    @property
    def timer_style(self) -> str:
        """Getter for Timer Style"""
        return self.timer_style_raw.get()

    @property
    def timer_chosen_time(self) -> int:
        """Getter for Chosen Time"""
        return self.timer_chosen_time_raw.get()

    @property
    def hints_chosen_level(self) -> int:
        """Getter for Hint Level"""
        return self.hints_chosen_level_raw.get()

    @property
    def timer_enabled(self) -> bool:
        """Getter for Timer Enabled"""
        return self.timer_enabled_raw.get()

    @property
    def timer_custom_time(self) -> int:
        """Getter for Custom Time"""
        return self.timer_custom_time_raw.get()

    # >>> Setters
    @difficulty.setter
    def difficulty(self, new_difficulty: str):
        self.difficulty_raw.set(new_difficulty)

    @timer_style.setter
    def timer_style(self, new_timer_style: str):
        self.timer_style_raw.set(new_timer_style)

    @timer_chosen_time.setter
    def timer_chosen_time(self, new_timer_chosen_time: int):
        self.timer_chosen_time_raw.set(new_timer_chosen_time)

    @hints_chosen_level.setter
    def hints_chosen_level(self, new_level: int):
        self.hints_chosen_level_raw.set(new_level)

    @timer_enabled.setter
    def timer_enabled(self, new_status: bool):
        self.timer_enabled_raw.set(new_status)

    @timer_custom_time.setter
    def timer_custom_time(self, new_time: int):
        self.timer_custom_time_raw.set(new_time)
