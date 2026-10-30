from __future__ import annotations

from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar

__all__ = ["bubble_sort"]


class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


_S = TypeVar("_S", bound=MutableSequence[Any])


def bubble_sort(items: _S) -> _S:
    start = 0
    end = len(items)
    fetch = items.__getitem__
    store = items.__setitem__
    while start + 1 < end:
        scan = enumerate(map(fetch, range(start + 1, end)), start)
        carried: _SupportsLessThan = fetch(start)
        for first_swap, current in scan:
            if current < carried:
                store(first_swap, current)
                break
            carried = current
        else:
            break
        while True:
            for position, current in scan:
                if current < carried:
                    store(position, current)
                    continue
                store(position, carried)
                carried = current
                limit = position
                break
            else:
                limit = end - 1
                store(limit, carried)
                break
            for position, current in scan:
                if current < carried:
                    store(position, current)
                    break
                carried = current
            else:
                break
        start = max(first_swap - 1, 0)
        end = limit
    return items
