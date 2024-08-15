#!/usr/bin/env python3
"""Function"""
import typing


def element_length(lst: typing.List[str]) -> typing.List[typing.Tuple[str, int]]:
    """Function"""
    return [(i, len(i)) for i in lst]
