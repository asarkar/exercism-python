import functools
from typing import TypeVar, Callable


U = TypeVar("U")
T = TypeVar("T")


def append(list1: list[T], list2: list[T]) -> list[T]:
    return list1 + list2


def concat(lists: list[list[T]]) -> list[T]:
    return [x for xs in lists for x in xs]


def filter(function: Callable[[T], bool], list: list[T]) -> list[T]:
    return [x for x in list if function(x)]


def length(list: list[T]) -> int:
    return len(list)


def map(function: Callable[[T], U], list: list[T]) -> list[U]:
    return [function(x) for x in list]


def foldl(function: Callable[[U, T], U], list: list[T], initial: U) -> U:
    return functools.reduce(function, list, initial)


def foldr(function: Callable[[U, T], U], list: list[T], initial: U) -> U:
    return foldl(function, reverse(list), initial)


def reverse(list: list[T]) -> list[T]:
    return list[::-1]
