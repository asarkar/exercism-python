# To avoid repeated multiplications, we maintain a running product.
# Whenever we exceed the length of a span, we divide the product
# by the outgoing number, provided the outgoing number is not zero.
# We restart the product when we get past a zero.
def largest_product(txt: str, span: int) -> int:
    if span > len(txt):
        raise ValueError("span must be smaller than string length")
    if span < 0:
        raise ValueError("span must not be negative")

    pdt = 1
    cnt = max_pdt = 0

    for end, ch in enumerate(txt):
        if not ch.isdigit():
            raise ValueError("digits input must only contain digits")

        k = int(ch)
        pdt *= k
        cnt += 1

        if k == 0:
            pdt = 1
            cnt = 0
        elif cnt >= span:
            if end >= span and (prev := txt[end - span]) != "0":
                pdt //= int(prev)
            max_pdt = max(pdt, max_pdt)

    return max_pdt
