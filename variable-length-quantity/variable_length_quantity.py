import functools
from collections import deque


def encode(numbers: [int]) -> [int]:
    def go(acc: [int], i: int) -> [int]:
        acc.extend(__encode(i))
        return acc

    return functools.reduce(go, numbers, [])


# 1. Represent the value in binary notation (e.g. 137 as 10001001).
# 2. Break it up in groups of 7 bits starting from the lowest
#    significant bit (e.g. 137 as 0000001 0001001).
# 3. Take the lowest 7 bits, and that gives the least significant
#    byte (0000 1001). This byte comes last.
# 4. For all the other groups of 7 bits (in the example, this is 000 0001),
#    set the MSb to 1 (which gives 1000 0001 in our example).
#
#    Thus. 137 becomes 1000 0001 0000 1001.
#    By definition, the very last byte of a variable-length integer will
#    have 0 as its MSb.
def __encode(num: int) -> deque[int]:
    result = deque()
    fst = True
    if num == 0:
        result.append(0)
    while num:
        # Mask (bitwise AND) with 0x7f = 127 = 0b1111111
        s = num & 0x7F
        if fst:
            # Clear the 8th bit from the right
            # 0x80 = 128 = 0b10000000, ~128 = 0b01111111
            s &= ~0x80
            fst = False
        else:
            # Set the 8th bit from the right
            s |= 0x80
        result.appendleft(s)
        # Right shift the remaining num dropping the 7 bits
        # processed above
        num >>= 7

    return result


def decode(bytes_):
    if bytes_ and not __is_last_byte(bytes_[-1]):
        raise ValueError("incomplete sequence")

    # Result is a list as there can be more sequences
    result = []
    # Initial decoded number for sequence
    num = 0
    # The following loop explained:
    # 1. Take a byte and mask it ('&' = bitwise AND) with
    #    0x7f (0b1111111), in other words - extract the last
    #    7 bits of the current byte.
    # 2. Left shift ('<<' = bitwise left shift) the current 'num'
    #    by 7, meaning it creates 7 zeroes on the right hand side
    #    of the binary number to make space for the 7 extracted
    #    bits from step 1.
    # 3. Using bitwise OR ('|') insert the extracted 7 bits form step 1
    #    into the previously shifted 'num' from step 2.
    # 4. Loop until a byte with MSb 0 is found.
    #
    #    Steps 1 through 3 are all happening within the line:
    #     ==>   num = (num << 7) | (b & 0x7f)   <==
    for b in bytes_:
        num = (num << 7) | (b & 0x7F)
        if __is_last_byte(b):
            result.append(num)
            num = 0

    return result


def __is_last_byte(i: int) -> bool:
    return not i & 0x80
