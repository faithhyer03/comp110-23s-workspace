"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730471008"


class Simpy:
    """Wooo last one!"""

    values: list[float]

    def __init__(self, floater: list[float]) -> None:
        """Be simple!"""
        self.values = floater
        return None
    
    def __str__(self) -> str:
        """Make it a string!"""
        give_back: str = f"Simpy({self.values})"
        return give_back
    
    def fill(self, filling: float, values: int) -> None:
        """Filling values for a float!"""
        new: list[float] = list()
        while values > 0: 
            new.append(filling)
            values -= 1
        self.values = new
        return None
    
    def arrange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0
        new: list[float] = list()
        idx: int = 0
        new.append(start)
        while idx > new:
            new += 1
    # TODO: Your constructor and methods will go here.