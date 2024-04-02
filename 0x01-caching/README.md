# Caching Systems

This repository contains Python implementations of various caching systems as part of an exercise for the ALX School curriculum.

## Classes

1. **BasicCache** (`0-basic_cache.py`):
   - Inherits from `BaseCaching`
   - Simple caching system without any limit
   
2. **FIFOCache** (`1-fifo_cache.py`):
   - Inherits from `BaseCaching`
   - Implements FIFO (First-In, First-Out) caching algorithm
   
3. **LIFOCache** (`2-lifo_cache.py`):
   - Inherits from `BaseCaching`
   - Implements LIFO (Last-In, First-Out) caching algorithm
   
4. **LRUCache** (`3-lru_cache.py`):
   - Inherits from `BaseCaching`
   - Implements LRU (Least Recently Used) caching algorithm
   
5. **MRUCache** (`4-mru_cache.py`):
   - Inherits from `BaseCaching`
   - Implements MRU (Most Recently Used) caching algorithm
   
6. **LFUCache** (`100-lfu_cache.py`):
   - Inherits from `BaseCaching`
   - Implements LFU (Least Frequently Used) caching algorithm
   
## Usage

Each file contains a class definition along with its methods:
- `put(self, key, item)`: Adds an item to the cache
- `get(self, key)`: Retrieves an item from the cache

You can create an instance of any caching system and interact with it using these methods.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/orumagideon/alx-backend.git
