#!/usr/bin/env python3
"""this module updates"""


def update_topics(mongo_collection, name, topics):
    """hanges all topics of a school document based on the name"""
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
