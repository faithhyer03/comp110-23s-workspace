"""EX04: Artistry on a computer."""

__author__= "730471008"


def all(x: list[int], y: int) -> bool:
    """Yeah no, it all has to match"""
    i: int = 0
    j: int = 0
    if len(x) == 0:
        return False
    while len(x) > i: 
        if x[i] == y:
            j = j + 1
        else:
            return False
        i = i + 1
    if j != len(x):
        return False
    else:
        return True


def max(z: list[int]) -> int:
    """I want the big one"""
    if len(z) == 0:
        raise ValueError("max() arg is an empty List")
    h: int = 0
    j: int = 0
    max_value: int = z[h]
    while len(z) >= h:
        while len(z) > j:
            if z[h] > z[j] and max_value:
                max_value = z[h]
            if z[j] > max_value:
                max_value = z[j]
            j = j + 1
        h = h + 1
    return max_value


def is_equal(a: list[int], b: list[int]) -> bool:
    """True or False: The lists match"""
    if a == b:
        return True
    else:
        return False