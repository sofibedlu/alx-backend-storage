#!/usr/bin/env python3
"""
define list_all function
"""


def list_all(mongo_collection):
    """
    return lists all documents in a collection
    """
    cursor = mongo_collection.find()
    return list(cursor)
