def maximum_value(maximum_weight: int, items: list[dict[str, int]]) -> int:
    # dp[i][j] is the maximum value obtainable by choosing the first i items not exceeding total weight j.
    dp: list[list[int]] = [[0] * (maximum_weight + 1) for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, maximum_weight + 1):
            #  Include the ith item if its weight is not more than the weight. In this case, we include
            #  its value plus whatever value we get from the remaining weight and from remaining items.
            if items[i - 1]['weight'] <= j:
                dp[i][j] = dp[i - 1][j - items[i - 1]['weight']] + items[i - 1]['value']
            # Exclude the ith item. In this case, we will take whatever value we get from the sub-array
            # excluding this item.
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    return dp[-1][-1]
