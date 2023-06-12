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


# We maintain a write and a read pointer into the buffer. Write
# is done at the location of the write ptr, and read is done from
# the location of the read ptr. The pointers are incremented after
# corresponding read/write operations, modulo to the capacity.
#
# The exception to the above is when the buffer is full and an
# overwrite is done, then we write at the location of the read
# ptr.
#
# Basically, the read ptr points to the oldest element, and the
# write ptr to the next free slot.

class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.data = [None] * capacity
        self.write_idx = self.read_idx = self.size = 0
        self.capacity = capacity

    def read(self) -> str:
        if self.__is_empty():
            raise BufferEmptyException('Circular buffer is empty')
        element = self.data[self.read_idx]
        self.read_idx = (self.read_idx + 1) % self.capacity
        self.size -= 1
        return element

    def write(self, element: str) -> None:
        if self.__is_full():
            raise BufferFullException('Circular buffer is full')

        self.data[self.write_idx] = element
        self.write_idx = (self.write_idx + 1) % self.capacity
        self.size += 1

    def overwrite(self, element: str) -> None:
        if self.__is_full():
            self.data[self.read_idx] = element
            self.read_idx = (self.read_idx + 1) % self.capacity
        else:
            self.write(element)

    def clear(self):
        self.data = [None] * self.capacity
        self.write_idx = self.read_idx = self.size = 0

    def __is_empty(self) -> bool:
        return self.size == 0

    def __is_full(self) -> bool:
        return self.size == self.capacity
