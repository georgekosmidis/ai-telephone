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
    first_swap: int
    position: int
    carried: _SupportsLessThan
    current: _SupportsLessThan
    while end - start > 1:
        scan = enumerate(map(fetch, range(start + 1, end)), start)
        carried = fetch(start)
        for first_swap, current in scan:
            if current < carried:
                store(first_swap, current)
                break
            carried = current
        else:
            break
        last = end - 1
        while True:
            for position, current in scan:
                if current < carried:
                    store(position, current)
                    continue
                store(position, carried)
                carried = current
                end = position
                break
            else:
                store(last, carried)
                end = last
                break
            for position, current in scan:
                if current < carried:
                    store(position, current)
                    break
                carried = current
            else:
                break
        start = first_swap - 1 if first_swap > 0 else 0
    return items
