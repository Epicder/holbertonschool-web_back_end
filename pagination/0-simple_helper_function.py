#!/usr/bin/env python3

"""this module take two int and return a tuple of size two
containing the start idx and the end idx"""


def index_range(page: int, page_size: int) -> tuple:
    """this function take two int and return a tuple of size two
    containing the start idx and the end idx"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
