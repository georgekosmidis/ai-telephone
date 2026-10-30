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
        scan = enumerate(islice(items, start + 1, end), start)
        carried: _SupportsLessThan = items[start]
        first_swap = last_swap = -1
        while True:
            for position, current in scan:
                if current < carried:
                    items[position] = current
                    last_swap = position
                    break
                carried = current
            else:
                break
            if first_swap < 0:
                first_swap = last_swap
            for position, current in scan:
                if not current < carried:
                    items[position] = carried
                    carried = current
                    break
                items[position] = current
                last_swap = position
            else:
                items[end - 1] = carried
                break
        if last_swap < 0:
            break
        start = max(first_swap - 1, 0)
        end = last_swap + 1
    return items
