#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class represents a basic caching system that stores key-value pairs.

    Methods:
        put(key, item): Stores a key-value pair in the cache.
        get(key): Retrieves the value associated with a given key.
    """

    def __init__(self):
        """
        Initializes the class by calling the parent class's __init__ method.
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Stores a key-value pair in the cache.

        Args:
            key: The key to be stored.
            item: The value associated with the key.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value linked to the provided key.

        Args:
            key: The key to retrieve the associated value.

        Returns:
            The value associated with the key, or None if the key is None or doesn't exist.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
