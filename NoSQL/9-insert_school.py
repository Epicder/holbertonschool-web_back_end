#!/usr/bin/env python3
"""this module insert a new document provided by kwargs"""
from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """inserts a new document in a collection based on kwargs"""
    add = mongo_collection.insert_one(kwargs)
    return add.inserted_id
