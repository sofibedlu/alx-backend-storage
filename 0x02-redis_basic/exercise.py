#!/usr/bin/env python3

"""
define a class Cache
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[bytes, str,
                                                          int, float]:
        """
        return the data from the redis with the desired format
        """
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> str:
        """
        make use of the get method and automatically parametrize it
        with the correct conversion function
        """
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """
        make use of the get method and automatically parametrize it
        with the correct conversion function
        """
        return self.get(key, fn=int)
