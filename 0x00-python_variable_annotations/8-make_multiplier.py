#!/usr/bin/env python3
"""
The Module for task 8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    It Takes a float multiplier as argument
    and returns a function that multiplies
    a float by multiplier
    """
    def multiplier_fn(number: float) -> float:
        """Multiplies a float by multiplier"""
        return number * multiplier

    return multiplier_fn
