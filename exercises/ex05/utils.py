"""EX05 Building list utility funtions!"""
__author__ = "730471008"


def only_evens(x: list[int]) -> list[int]:
    """Only evens are valid ig!"""
    idx: int = 0
    even: list[int] = list()
    while idx < len(x):
        if (x[idx]) % 2 == 0:
            even.append(x[idx])
        idx += 1
    return even


def concat(y: list[int], z: list[int]) -> list[int]:
    """Getting close together!"""
    idx: int = 0
    idx2: int = 0
    combo_list: list[int] = list()
    while idx < len(y): 
        combo_list.append(y[idx])
        idx += 1
    while idx2 < len(z):
        combo_list.append(z[idx2])
        idx2 += 1
    return combo_list


def sub(w: list[int], start: int, end: int) -> list[int]:
    """Make a list that will be a subset of the provided list!"""
    subs: list[int] = list()
    if start < 0:
        start = 0
    if end > len(w):
        end = len(w)
    if len(w) == 0:
        return subs
    if start >= len(w):
        return subs
    if end <= 0:
        return subs
    for idx in range(start, end):
        subs.append(w[idx])
    return subs


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
    
    def one_river_week(self): 
        """Life in a week!"""
        while self.day < 7:
            self.one_river_day()
        return None