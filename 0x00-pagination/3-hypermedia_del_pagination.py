#!/usr/bin/env python3
"""
Implements deletion-resilient hypermedia pagination for a database of popular baby names.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset from a CSV file.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Indexes the dataset by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of the dataset using deletion-resilient hypermedia pagination.

        Args:
            index (int): The index of the first item in the current page.
            page_size (int): The number of records per page.

        Returns:
            Dict: A dictionary containing pagination information and the dataset page.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        response['data'] = data
        response['page_size'] = len(data)
        response['next_index'] = index if dataset.get(index) else None
        return response
