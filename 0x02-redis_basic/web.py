#!/usr/bin/env python3
"""
define get_page function
"""

import requests
import redis
import time

# Initialize the Redis client
redis_client = redis.Redis()


def get_page(url: str) -> str:
    # Check if the URL has been cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode()

    # If not cached, fetch the page content
    response = requests.get(url)

    # Increment the access count for the URL in Redis
    redis_client.incr(f"count:{url}")

    # Cache the page content with an expiration time of 10 seconds
    redis_client.setex(url, 10, response.text)

    return response.text


# Testing the get_page function
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    # Simulate slow response
    for _ in range(5):
        content = get_page(url)
        print(content)

    # Retrieve and print the access count for the URL
    access_count = redis_client.get(f"count:{url}")
    print(f"Access count for {url}: {int(access_count)}")
