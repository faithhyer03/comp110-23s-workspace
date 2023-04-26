"""File to define Fish class!"""


class Fish:
    """Slimey fishies!"""

    def __init__(self, age: int = 0):
        """Init!"""
        self.age = age
        return None
    
    def one_day(self):
        """One day!"""
        self.age += 1
        return None