import functools
from collections.abc import Callable


def append[T](list1: list[T], list2: list[T]) -> list[T]:
    return list1 + list2


def concat[T](lists: list[list[T]]) -> list[T]:
    return [x for xs in lists for x in xs]


def filter[T](function: Callable[[T], bool], list: list[T]) -> list[T]:
    return [x for x in list if function(x)]


def length[T](list: list[T]) -> int:
    return len(list)


def map[U, T](function: Callable[[T], U], list: list[T]) -> list[U]:
    return [function(x) for x in list]


def foldl[U, T](function: Callable[[U, T], U], list: list[T], initial: U) -> U:
    return functools.reduce(function, list, initial)


def foldr[U, T](function: Callable[[U, T], U], list: list[T], initial: U) -> U:
    return foldl(function, reverse(list), initial)


def reverse[T](list: list[T]) -> list[T]:
    return list[::-1]
