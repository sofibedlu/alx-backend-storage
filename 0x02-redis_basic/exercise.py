#!/usr/bin/python3

"""
define a class Cache
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    represent cache instances
    """
    def __init__(self):
        """initialize Cache instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data using random key and
        return a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
