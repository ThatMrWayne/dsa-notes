from typing import List
# 122
# TC :
# SC :
"""
The point is buying at relative low price and selling at relative high price.
That' it...
"""


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    buy_p = None
    for i in range(len(prices)-1):
        curr_price = prices[i]
        next_price = prices[i+1]
        if buy_p is None and next_price > curr_price:
            buy_p = curr_price
        elif buy_p is not None and next_price < curr_price:
            max_profit += (curr_price - buy_p)
            buy_p = None
    if buy_p is not None and prices[-1] > buy_p:
        max_profit += (prices[-1] - buy_p)
    return max_profit
