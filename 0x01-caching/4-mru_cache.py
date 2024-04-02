#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache represents a caching system that follows the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initializes the class by calling the parent class's __init__ method and initializes an empty list to keep track of the usage order of keys.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Caches a key-value pair according to the MRU algorithm.
        
        Args:
            key: The key to be cached.
            item: The value associated with the key.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value linked to a given key, or None if the key doesn't exist in the cache.
        Updates the usage order of keys according to MRU algorithm.
        
        Args:
            key: The key to retrieve the associated value.

        Returns:
            The value associated with the key, or None if the key is None or doesn't exist in the cache.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
