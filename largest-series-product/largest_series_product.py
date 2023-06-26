# To avoid repeated multiplications, we maintain a running product.
# Whenever we exceed the length of a span, we divide the product
# by the outgoing number, provided the outgoing number is not zero.
# We also keep track of the index of the last zero, because as long
# as there is a zero in the span, the product is zero. We restart
# the product when we get past a zero.
def largest_product(txt: str, span: int) -> int:
    if span > len(txt):
        raise ValueError("span must be smaller than string length")
    if span < 0:
        raise ValueError("span must not be negative")

    pdt = 1
    max_pdt = start = 0
    last_index_of_zero = -1

    for i, ch in enumerate(txt):
        if not ch.isdigit():
            raise ValueError("digits input must only contain digits")
        k = int(ch)
        if k == 0:
            last_index_of_zero = i
        if i > 0 and last_index_of_zero == (i - 1):
            pdt = k
        else:
            pdt *= k

        if (i - start + 1) == span:
            if last_index_of_zero < start:
                max_pdt = max(max_pdt, pdt)
                if (x := int(txt[start])) != 0:
                    pdt //= x
            start += 1

    return max_pdt
