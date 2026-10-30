from __future__ import annotations

from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar

__all__ = ["bubble_sort"]


class _SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


_S = TypeVar("_S", bound=MutableSequence[Any])


def bubble_sort(items: _S) -> _S:
    fetch = items.__getitem__
    store = items.__setitem__
    start = 0
    end = len(items)
    while end - start > 1:
        last = end - 1
        scan = enumerate(map(fetch, range(start + 1, end)), start)
        carried: _SupportsLessThan = fetch(start)
        for first_swap, current in scan:
            if current < carried:
                store(first_swap, current)
                break
            carried = current
        else:
            break
        limit = last
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
                store(last, carried)
                limit = last
                break
            for position, current in scan:
                if current < carried:
                    store(position, current)
                    break
                carried = current
            else:
                break
        start = first_swap - 1 if first_swap else 0
        end = limit
    return items
