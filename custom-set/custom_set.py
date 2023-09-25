from __future__ import annotations

from typing import Any, Optional


class CustomSet:
    def __init__(self, elements: Optional[list[Any]] = None) -> None:
        self.elements = elements or []

    def __repr__(self) -> str:
        return f"CustomSet({self.elements})"

    def __len__(self) -> int:
        return len(self.elements)

    def isempty(self) -> bool:
        return len(self.elements) == 0

    def __contains__(self, element: Any) -> bool:
        return element in self.elements

    def issubset(self, other: CustomSet) -> bool:
        return all(e in other.elements for e in self.elements)

    def isdisjoint(self, other: CustomSet) -> bool:
        return all(e not in other.elements for e in self.elements)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CustomSet) and len(self) == len(other) and self.issubset(other)

    def add(self, element: Any) -> None:
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other: CustomSet) -> CustomSet:
        return CustomSet([e for e in self.elements if e in other])

    def __sub__(self, other: CustomSet) -> CustomSet:
        return CustomSet([e for e in self.elements if e not in other])

    def __add__(self, other: CustomSet) -> CustomSet:
        return CustomSet(self.elements + [e for e in other.elements if e not in self.elements])
