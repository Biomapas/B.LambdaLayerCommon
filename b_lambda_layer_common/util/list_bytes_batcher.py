import json
import math
from itertools import islice
from typing import Any, Iterable, List


class ListBytesBatcher:
    def __init__(self, items: List[Any], batch_size: int) -> None:
        """
        Split the given list of any items into designated size batches.

        :param items: A list of any items that should be split into batches.
        :param batch_size: Size of batch in bytes. Positive non-zero value.

        return No return.
        """

        self.items = items
        self.batch_size = batch_size

    def iterate_batches(self) -> Iterable:
        """
        Split given list into batches not exceeding batch size.

        :return: Iterator of batches.
        """

        if self.batch_size <= 0:
            raise ValueError(f'Unexpected batch size value. Expected positive non-zero integer, got: {self.batch_size}')

        if not isinstance(self.items, list):
            raise TypeError(f'Unexpected data type of items. Expected: {type([])} got: {type(self.items)}.')

        slices = math.ceil(ListBytesBatcher.size(self.items)/self.batch_size)
        batch_size = math.ceil(len(self.items)/slices)
        iterable = iter(self.items)
        while batch := list(islice(iterable, batch_size)):
            yield batch

    @staticmethod
    def size(items: List[Any]) -> int:
        """
        Calculate a number of bytes of given list.

        :param items: A list of any items.

        :return: Number of bytes of given list in UTF-8 encoded form.
        """

        return len(json.dumps(items).encode('utf-8'))
