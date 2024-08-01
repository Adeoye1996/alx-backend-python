#!/usr/bin/env python3
"""
The Module for task  7-to_kv
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    It takes a string and a int or float
    and returns a tuple of the string
    and a float
    """
    return (k, v**2)
