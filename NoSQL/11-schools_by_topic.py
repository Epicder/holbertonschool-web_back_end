#!/usr/bin/env python3
"""this module returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of schools having a specific topic"""
    schools = mongo_collection.find({'topics': topic})
    return list(schools)
