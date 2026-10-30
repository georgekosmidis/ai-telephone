from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar

__all__ = ["bubble_sort"]


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=SupportsLessThan)
S = TypeVar("S", bound=MutableSequence[Any])


def bubble_sort(items: S) -> S:
    end = len(items)
    while end > 1:
        last_swap = 0
        largest = items[0]
        for i in range(1, end):
            current = items[i]
            if current < largest:
                items[i - 1] = current
                last_swap = i
            else:
                if last_swap == i - 1 and i > 1:
                    items[i - 1] = largest
                largest = current
        if last_swap == end - 1:
            items[end - 1] = largest
        end = last_swap
    return items