from __future__ import annotations

from collections.abc import MutableSequence
from itertools import islice
from typing import Any, Protocol, TypeVar

__all__ = ["bubble_sort"]


class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


_S = TypeVar("_S", bound=MutableSequence[Any])


def bubble_sort(items: _S) -> _S:
    start = 0
    end = len(items)
    while end - start > 1:
        pairs = enumerate(islice(items, start + 1, end), start)
        carried: _SupportsLessThan = items[start]
        for position, current in pairs:
            if current < carried:
                items[position] = current
                first_swap = position
                break
            carried = current
        else:
            break
        displaced = True
        last_swap = first_swap + 1
        for position, current in pairs:
            if current < carried:
                items[position] = current
                displaced = True
                last_swap = position + 1
            else:
                if displaced:
                    items[position] = carried
                    displaced = False
                carried = current
        if displaced:
            items[end - 1] = carried
        start = first_swap - 1 if first_swap > 0 else 0
        end = last_swap
    return items
