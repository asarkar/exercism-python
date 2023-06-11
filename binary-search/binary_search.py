def find(search_list: list[int], value: int) -> int:
    return __find(search_list, value, 0, len(search_list) - 1)


def __find(nums: list[int], value: int, lo: int, hi: int) -> int:
    mid = lo + (hi - lo + 1) // 2
    if hi < lo:
        raise ValueError('value not in array')
    if nums[mid] == value:
        return mid
    if nums[mid] > value:
        return __find(nums, value, lo, mid - 1)
    return __find(nums, value, mid + 1, hi)
