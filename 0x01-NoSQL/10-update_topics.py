#!/usr/bin/env python3
"""
define update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    craiteria = {"name": name}
    value = {"$set": {"topics": topics}}

    mongo_collection.update_one(craiteria, value)
