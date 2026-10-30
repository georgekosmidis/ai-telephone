from __future__ import annotations

from collections.abc import MutableSequence
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
        for i in range(1, end):
            current = items[i]
            if current < carried:
                items[i - 1] = current
                last_swap = i
                continue
            if last_swap == i - 1:
                items[i - 1] = carried
            carried = current
        if last_swap == end - 1:
            items[last_swap] = carried
        end = last_swap
    return items
