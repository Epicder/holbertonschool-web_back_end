#!/usr/bin/env python3
"""this module lists all documents in a collection"""
from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """list all documents in a collection"""
    documents = list(mongo_collection.find())
    return documents if documents else []
