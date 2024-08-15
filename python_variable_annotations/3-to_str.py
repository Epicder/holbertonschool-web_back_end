#!/usr/bin/env python3

"""This module takes a float as an arg and return a str"""


def to_str(n: float) -> str:
    """Convert a float to a string, rounding to 2 decimal places."""    
    return "{:.2f}".format(n)
