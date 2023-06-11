from functools import reduce


def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    def go(acc: dict[str, int], item: tuple[int, list[str]]) -> dict[str, int]:
        for x in item[1]:
            acc[x.lower()] = item[0]
        return acc

    return reduce(go, legacy_data.items(), {})
