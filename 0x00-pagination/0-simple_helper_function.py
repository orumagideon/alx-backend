#!/usr/bin/env python3
"""
Defines the index_range helper function to calculate pagination indexes.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes for pagination.
    
    Args:
        page (int): The page number to return (pages are 1-indexed).
        page_size (int): The number of items per page.
        
    Returns:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
