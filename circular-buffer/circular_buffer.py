from collections import deque


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


# Just a queue, if full, overwrite removes the oldest element from the front.
class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.data: deque[str] = deque()
        self.capacity = capacity

    def read(self) -> str:
        if self._is_empty():
            raise BufferEmptyException("Circular buffer is empty")
        return self.data.popleft()

    def write(self, elem: str) -> None:
        if self._is_full():
            raise BufferFullException("Circular buffer is full")
        self.data.append(elem)

    def overwrite(self, elem: str) -> None:
        if self._is_full():
            self.data.popleft()
        self.data.append(elem)

    def clear(self) -> None:
        self.data.clear()

    def _is_empty(self) -> bool:
        return not self.data

    def _is_full(self) -> bool:
        return len(self.data) == self.capacity
