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
        new_end = 0
        carried: _SupportsLessThan = items[0]
        displaced = False
        for position, current in enumerate(islice(items, 1, end)):
            if current < carried:
                items[position] = current
                displaced = True
                new_end = position + 1
            else:
                if displaced:
                    items[position] = carried
                    displaced = False
                carried = current
        if displaced:
            items[end - 1] = carried
        end = new_end
    return items
