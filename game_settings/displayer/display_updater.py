"""Update the display text to be up-to-date"""

class Updater:
    """Updaters for the displayer"""
    def __init__(self, master, _, prp):
        self.root = master
        self.prp = prp
    
    def update_difficulty(self=None, value: str="Medium") -> None:
        """Update the chosen difficulty to the chosen one"""
        
    
    def update_hint_level(self=None, value: str=0) -> None:
        """Update the chosen hint level to the chosen one"""
        pass
    
    def update_timer_style(self=None, value: str | None=None) -> None:
        """Update the timer style to the chosen one"""
        pass
    
    def update_chosen_time(self=None, value: int=40) -> None:
        """Update the chosen timer to the chosen one"""
        pass
    
    def update_general(self=None) -> None:
        """Run every updater"""
        self.update_difficulty()
        self.update_hint_level()
        self.update_timer_style()
        self.update_chosen_time()    
