"""File to define River class!"""


__author__ = "730471008"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River: 
    """It do be a river class!"""

    def __init__(self, num_fish: int, num_bears: int, day: int = 0): 
        """New River with num_fish Fish and num_bears Bears!"""
        self.day = day
        self.num_fish = num_fish
        self.num_bears = num_bears
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self): 
        """Check ages!"""
        new: int = len(self.fish) - 1
        while new >= 0:
            check: Fish = self.fish[new]
            if check.age > 3:
                self.fish.pop(new)
            new -= 1
        newer: int = len(self.bears) - 1
        while newer >= 0:
            checker: Bear = self.bears[newer]
            if checker.age > 5:
                self.bears.pop(newer)
            newer -= 1
        return None
    
    def remove_fish(self, amount: int): 
        """Remove fish!"""
        idk: list[Fish] = []
        idk += self.fish
        fish: int = 0
        while fish < amount:
            idk.pop(fish)
            amount -= 1
        self.fish = idk
        return None

    def bears_eating(self): 
        """Bears be hungry!"""
        bear: int = 0
        while bear < len(self.bears):
            if len(self.fish) >= 5:
                self.bears[bear].eat(3)
                self.remove_fish(3)
            bear += 1
        return None

    def check_hunger(self): 
        """Checking in!"""
        survive: list[Bear] = []
        survive += self.bears
        bear: int = 0
        while bear < len(self.bears): 
            if self.bears[bear].hunger_score < 0:
                survive.pop(bear)
            bear += 1
        self.bears = survive
        return None

    def repopulate_fish(self): 
        """4 new baby fish!"""
        baby: int = len(self.fish)
        baby_creator: int = (baby // 2) * 4
        while baby_creator > 0:
            self.fish.append(Fish)
            baby_creator -= 1
        return None

    def repopulate_bears(self): 
        """1 Baby Bear!"""
        baby: int = len(self.bears)
        baby_creator: int = (baby // 2)
        while baby_creator > 0:
            self.bears.append(Bear)
            baby_creator -= 1
        return None

    def view_river(self): 
        """Read the populations!"""
        print(f"~~~Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self): 
        """Simulate one day of life in the river!"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None
    
    def one_river_week(self): 
        """Life in a week!"""
        while self.day < 7:
            self.one_river_day()
        return None