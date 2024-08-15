#!/usr/bin/env python3

"""
takes a list mxd_lst of integers and floats and returns their sum
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats and returns their sum
    """
    return sum(mxd_lst)
