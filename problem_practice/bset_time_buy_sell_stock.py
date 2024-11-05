from typing import List

# 121
# TC : O(n)
# SC : O(n)
"""
Use bottom-up dynamic programmin
"""


def maxProfit(prices: List[int]) -> int:
    record = dict()
    record[1] = 0
    max_profit = 0
    min_price = prices[0]
    for i in range(2, len(prices)+1):
        idx = i - 1
        record[i] = prices[idx] - min_price
        min_price = prices[idx] if prices[idx] < min_price else min_price
        max_profit = record[i] if record[i] > max_profit else max_profit
    return max_profit
