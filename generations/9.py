from collections.abc import MutableSequence
from typing import Any, TypeVar

__all__ = ["bubble_sort"]

S = TypeVar("S", bound=MutableSequence[Any])


def bubble_sort(items: S) -> S:
    end = len(items)
    while end > 1:
        last_swap = 0
        largest = items[0]
        displaced = False
        for i in range(1, end):
            current = items[i]
            if current < largest:
                items[i - 1] = current
                last_swap = i
                displaced = True
                continue
            if displaced:
                items[i - 1] = largest
                displaced = False
            largest = current
        if displaced:
            items[last_swap] = largest
        end = last_swap
    return items
