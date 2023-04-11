"""Test for ex05!"""
__author__ = "730471008"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_empty() -> None:
    """Check if list is empty!"""
    assert only_evens([]) == 0


def test_mult() -> None:
    """Multiple types of int!"""
    test_list: list[int] = [1, -2, 5, 8, -9, 4]
    assert only_evens(test_list) == [-2, 8, 4]


def test_neg() -> None:
    """Negative values!"""
    test_list: list[int] = [-1, -2, -3, -4, -5]
    assert only_evens(test_list) == [-2, -4]


def test_concat_empty() -> None:
    """Make sure the lists are empty!"""
    test_list: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list, test_list2) == []


def test_concat_neg() -> None:
    """Negative Values!"""
    test_list: list[int] = [-2, -6, -8]
    test_list2: list[int] = [-1, -3, -5]
    assert concat(test_list, test_list2) == [-2, -6, -8, -1, -3, -5]


def test_concat_length() -> None:
    """It is what is inside that counts!"""
    test_list: list[int] = [5, 6, 7]
    test_list2: list[int] = [1]
    assert concat(test_list, test_list2) == [5, 6, 7, 1]


def test_sub_within() -> None:
    """A normal list!"""
    test_list: list[int] = [4, 5, 2, 6, 8, 9]
    assert sub(test_list, 1, 3) == [5, 2]


def test_sub_neg() -> None:
    """Start is always 0!"""
    test_list: list[int] = [1, 2, 4, 0, 7]
    assert sub(test_list, -5, 2) == [1, 2]


def test_sub_range() -> None:
    """Make sure it is within length!"""
    test_list: list[int] = [3, 8, 9, 1, 5]
    assert sub(test_list, 2, 55) == [9, 1, 5]