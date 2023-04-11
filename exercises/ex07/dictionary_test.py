"""Test for the dictionaries!"""

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest


with pytest.raises(KeyError):
    dictionary = {'black': 'white', "blue": 'white'}
    invert(dictionary)


def test_edge() -> None:
    """Edge!"""
    assert invert({'x': 'y', 'z': 'y', 'w': 'v'}) == {'y': 'z', 'v': 'w'}


def test_use() -> None:
    """Use!"""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f'}) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_use2() -> None:
    """Use!"""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}


def test_favorite_color_edge() -> None:
    """EDGE!"""
    assert favorite_color({'Grant': 'green', 'Chris': 'red', 'Liz': 'green'}) == 'green'


def test_favorite_color_use() -> None:
    """USE!"""
    assert favorite_color({'Grant': 'green', 'Chris': 'green', 'Liz': 'green', 'Pablo': 'green'}) == 'green'


def test_favorite_color_use2() -> None:
    """USE!"""
    assert favorite_color({'Grant': 'green', 'Chris': 'red', 'Liz': 'blue', 'Harper': 'red', 'Rachel': 'blue'}) == 'red', 'blue'


def test_count_edge() -> None:
    """EDGE!"""
    assert count([]) == {}


def test_count_use1() -> None:
    """COUNT!"""
    assert count(['pizza', 'burger', 'fries', 'pizza']) == {'pizza': 2, 'burger': 1, 'fries': 1}


def test_count_use2() -> None:
    """COUNT!"""
    assert count(['bird', 'fish', 'bird', 'cat', 'kangaroo']) == {'bird': 2, 'fish': 1, 'cat': 1, 'kangaroo': 1}