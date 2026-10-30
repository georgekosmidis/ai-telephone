from __future__ import annotations

from collections.abc import MutableSequence
from itertools import islice
from typing import Any, Protocol, TypeVar

__all__ = ["bubble_sort"]


class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


_S = TypeVar("_S", bound=MutableSequence[Any])


def bubble_sort(items: _S) -> _S:
    end = len(items)
    while end > 1:
        last_swap = -1
        carried: _SupportsLessThan = items[0]
        position = 0
        for current in islice(items, 1, end):
            if current < carried:
                items[position] = current
                position += 1
                last_swap = position
                continue
            if last_swap == position:
                items[position] = carried
            carried = current
            position += 1
        if last_swap == position:
            items[position] = carried
        end = last_swap
    return items
