"""Define the understanding of another part of Comp 110!"""
__author__ = "730471008"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Be different but not really!"""
    inverted: dict[str, str] = dict()
    for idx in dictionary:
        inverted_idx = dictionary[idx]
        inverted[inverted_idx] = idx
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Reeturn popular color!"""
    count = {}
    for idx in colors:
        if idx in colors:
            count[idx] += 1
        else:
            count[idx] = 1
    most = None
    for idx in colors:
        if most is None or count[idx] > count[most]:
            most = idx

    return most


def count(values: list[str]) -> dict[str, int]:
    """Easy as 1 2 3!"""
    count = {}
    for idx in values:
        if idx in count:
            count[idx] += 1
        else:
            count[idx] = 1
    return count