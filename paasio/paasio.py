import io
from collections.abc import Iterator
from socket import socket
from types import TracebackType
from typing import Any, Self


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self._read_bytes = self._write_bytes = self._read_ops = self._write_ops = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        Exit the runtime context and return a Boolean flag indicating
        if any exception that occurred should be suppressed.

        The above is only true for context managers.  For IO, only None is allowed
        to be returned. See https://github.com/python/cpython/issues/103573
        """
        return super().__exit__(exc_type, exc_val, exc_tb)

    # BufferedRandom isn't an interator per se.
    # So we need to implement the iterator protocol ourselves.
    def __iter__(self) -> Iterator[bytes]:
        return self

    def __next__(self) -> bytes:
        b = super().readline()
        i = len(b)
        if i == 0:
            raise StopIteration
        self._read_bytes += i
        self._read_ops += 1
        return b

    def read(self, size: int | None = -1) -> bytes:
        """
        Read and return one line from the stream.
        """
        b = super().read(size)
        self._read_bytes += len(b)
        self._read_ops += 1
        return b

    @property
    def read_bytes(self) -> int:
        return self._read_bytes

    @property
    def read_ops(self) -> int:
        return self._read_ops

    # Starting with Python 3.12, b: collections.abc.Buffer.
    def write(self, b):  # type: ignore[no-untyped-def]
        i = super().write(b)
        self._write_bytes += i
        self._write_ops += 1
        return i

    @property
    def write_bytes(self) -> int:
        return self._write_bytes

    @property
    def write_ops(self) -> int:
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, s: socket):
        self._socket = s
        self._recv_bytes = self._send_bytes = self._recv_ops = self._send_ops = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        Exit the runtime context and return a Boolean flag indicating
        if any exception that occurred should be suppressed.

        The above is only true for context managers.  For IO, only None is allowed
        to be returned. See https://github.com/python/cpython/issues/103573
        """
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize: int, flags: int = 0) -> bytes:
        b = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(b)
        self._recv_ops += 1
        return b

    @property
    def recv_bytes(self) -> int:
        return self._recv_bytes

    @property
    def recv_ops(self) -> int:
        return self._recv_ops

    def send(self, data: Any, flags: int = 0) -> int:
        i = self._socket.send(data, flags)
        self._send_bytes += i
        self._send_ops += 1
        return i

    @property
    def send_bytes(self) -> int:
        return self._send_bytes

    @property
    def send_ops(self) -> int:
        return self._send_ops
