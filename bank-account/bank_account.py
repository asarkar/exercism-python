from threading import RLock
from typing import Optional


# Some community solutions using decorators:
# https://exercism.org/tracks/python/exercises/bank-account/solutions/paweltomkiel
# https://exercism.org/tracks/python/exercises/bank-account/solutions/FergusonTG
class BankAccount:
    def __init__(self) -> None:
        self._balance: Optional[int] = None
        self._lock = RLock()

    # Don't need to synchronize here.
    def get_balance(self) -> int:
        self.__ensure_open()
        assert self._balance is not None
        return self._balance

    def open(self) -> None:
        with self._lock:
            if self._balance is not None:
                raise ValueError("account already open")
            self._balance = 0

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        with self._lock:
            self.__ensure_open()
            assert self._balance is not None
            self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        with self._lock:
            if self.get_balance() < amount:
                raise ValueError("amount must be less than balance")
            assert self._balance is not None
            self._balance -= amount

    def close(self) -> None:
        with self._lock:
            self.__ensure_open()
            self._balance = None

    def __ensure_open(self) -> None:
        if self._balance is None:
            raise ValueError("account not open")
