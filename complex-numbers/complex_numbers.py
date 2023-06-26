from __future__ import annotations

import math


class ComplexNumber:
    def __init__(self, real, imaginary: float = 0.0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: ComplexNumber) -> bool:
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imaginary})"

    def __add__(self, other) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        return self + ComplexNumber(other)

    def __radd__(self, other) -> ComplexNumber:
        return self + ComplexNumber(other)

    def __mul__(self, other) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            r = self.real * other.real - self.imaginary * other.imaginary
            i = self.imaginary * other.real + self.real * other.imaginary
            return ComplexNumber(r, i)
        return self * ComplexNumber(other)

    def __rmul__(self, other) -> ComplexNumber:
        return self * ComplexNumber(other)

    def __sub__(self, other) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        return self - ComplexNumber(other)

    def __rsub__(self, other) -> ComplexNumber:
        return ComplexNumber(other) - self

    def __truediv__(self, other) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            x = other.real * other.real + other.imaginary * other.imaginary
            r = (self.real * other.real + self.imaginary * other.imaginary) / x
            i = (self.imaginary * other.real - self.real * other.imaginary) / x
            return ComplexNumber(r, i)
        return self / ComplexNumber(other)

    def __rtruediv__(self, other) -> ComplexNumber:
        return ComplexNumber(other) / self

    def __abs__(self) -> float:
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def conjugate(self) -> ComplexNumber:
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> ComplexNumber:
        x = math.exp(self.real)
        return ComplexNumber(x * math.cos(self.imaginary), x * math.sin(self.imaginary))
