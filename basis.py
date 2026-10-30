from typing import MutableSequence, TypeVar

T = TypeVar("T")

def bubble_sort(items: MutableSequence[T]) -> MutableSequence[T]:
    n = len(items)
    while n > 1:
        last_swap = 0
        for i in range(1, n):
            if items[i - 1] > items[i]:
                items[i - 1], items[i] = items[i], items[i - 1]
                last_swap = i
        n = last_swap
    return items