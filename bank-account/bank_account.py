from threading import RLock


# Some community solutions using decorators:
# https://exercism.org/tracks/python/exercises/bank-account/solutions/paweltomkiel
# https://exercism.org/tracks/python/exercises/bank-account/solutions/FergusonTG
class BankAccount:
    def __init__(self):
        self._balance = None
        self._lock = RLock()

    # Don't need to synchronize here.
    def get_balance(self) -> int:
        self.__ensure_open()
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
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        with self._lock:
            if self.get_balance() < amount:
                raise ValueError("amount must be less than balance")
            self._balance -= amount

    def close(self):
        with self._lock:
            self.__ensure_open()
            self._balance = None

    def __ensure_open(self) -> None:
        if self._balance is None:
            raise ValueError("account not open")
