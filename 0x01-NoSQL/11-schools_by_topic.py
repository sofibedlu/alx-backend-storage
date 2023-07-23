#!/usr/bin/env python3
"""
define schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns list of school having a specific topic
    """
    criteria = {"topics": {"$in": [topic]}}
    cursor = mongo_collection.find(criteria)
    return list(cursor)
