"""File to define Bear class!"""


class Bear:
    """Best kind of bear?"""

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Init!"""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """One day!"""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bears be hungry!"""
        self.hunger_score += num_fish
        return None