#!/usr/bin/env python3
"""Function"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Function"""
    return [(i, len(i)) for i in lst]
