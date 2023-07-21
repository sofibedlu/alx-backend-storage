#!/usr/bin/env python3

"""
define a class Cache
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method
        method_name = f"{self.__class__.__name__}.{method.__name__}"

        # Create input and output list keys
        input_key = f"{method_name}:inputs"
        output_key = f"{method_name}:outputs"

        # Convert the input arguments to a normalized string and store in Redis
        input_string = str(args)
        self._redis.rpush(input_key, input_string)

        # Call the original method to retrieve the output
        output = method(self, *args, **kwargs)

        # Store the output in Redis
        self._redis.rpush(output_key, str(output))

        # Return the output
        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
     count_calls decorator that takes a single method Callable
     argument and returns a Callable
     """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        # Get the qualified name of the method
        method_name = f"{self.__class__.__name__}.{method.__name__}"

        # Increment the count for the method in Redis
        self._redis.incr(method_name)

        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    represent cache instances
    """
    def __init__(self):
        """initialize Cache instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
