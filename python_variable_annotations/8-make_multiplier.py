#!/usr/bin/env python3

"""typed function that takes a float multiplier as argument and returns a function that multiplies a float by multiplier."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """typed function that takes a float number as argument and returns the product of number and multiplier."""
    def mult