from __future__ import annotations

import math
import typing


class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        sign = -1 if denom < 0 else int(denom > 0)
        g = math.gcd(abs(numer), abs(denom))

        self.numer = (numer * sign) // g
        self.denom = abs(denom) // g

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return False
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: Rational) -> Rational:
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other: Rational) -> Rational:
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other: Rational) -> Rational:
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other: Rational) -> Rational:
        if other.numer == 0:
            raise ZeroDivisionError("division not defined when divisor is zero")

        numer = self.numer * other.denom
        denom = other.numer * self.denom
        return Rational(numer, denom)

    def __abs__(self) -> Rational:
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power: int | float) -> Rational:
        if isinstance(power, int):
            if power < 0:
                return Rational(self.denom ** abs(power), self.numer ** abs(power))
            return Rational(self.numer ** abs(power), self.denom ** abs(power))

        # GCD of floats is not defined.
        raise ValueError("exponentiation to a floating-point number is not defined")

    def __rpow__(self, base: int | float) -> float:
        return typing.cast(float, pow(base, self.numer / self.denom))
