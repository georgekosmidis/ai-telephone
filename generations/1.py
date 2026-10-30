from typing import Any, MutableSequence, Protocol, TypeVar


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=SupportsLessThan)


def bubble_sort(items: MutableSequence[T]) -> MutableSequence[T]:
    end = len(items)
    while end > 1:
        last_swap = 0
        for i in range(1, end):
            if items[i] < items[i - 1]:
                items[i - 1], items[i] = items[i], items[i - 1]
                last_swap = i
        end = last_swap
    return items