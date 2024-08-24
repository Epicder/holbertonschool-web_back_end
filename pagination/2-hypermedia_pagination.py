#!/usr/bin/env python3

"""this module take two int and return a tuple of size two
containing the start idx and the end idx"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """this function take two int and return a tuple of size two
    containing the start idx and the end idx"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get a page of data from the dataset"""
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary with pagination."""
        data = self.get_page(page, page_size)
        next_page: int = page + 1 if page < total_pages else None
        prev_page: int = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.dataset) / page_size) # thanks chat gi pi ti

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }