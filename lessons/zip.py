"""Challenge question 04!"""
__author__ = "730471008"


def zip(x: list[str], y:list[int]) -> dict[str, int]:
    """Dictionaries vs Encyclopedias!"""
    dicts: dict[str, int] = {}
    if len(x) or len(y) == 0:
        return dicts
    if len(x) != len(y):
        return dicts
    for letter in x:
        dicts[letter] = x[letter]
    for number in y:
        dicts[number] = y[number]
    (f"x[letter] == y[number]")
    return dicts