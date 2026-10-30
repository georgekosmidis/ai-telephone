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
                items[i] = largest
                last_swap = i
            else:
                largest = current
        end = last_swap
    return items