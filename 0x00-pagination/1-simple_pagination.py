#!/usr/bin/env python3
"""
Defines the Server class responsible for paginating a database of popular baby names.
"""
import csv
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the requested page from the dataset.

        Args:
            page (int): The page number to retrieve. Must be a positive integer.
            page_size (int): The number of records per page. Must be a positive integer.

        Returns:
            List[List]: A list of lists containing the required data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
