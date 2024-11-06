from typing import List

# 136
# TC : O(n)
# SC : O(1)
"""
User bit operation `XOR` to eleminate duplicate numbers,
the one left is the answer.
"""


def singleNumber(nums: List[int]) -> int:
    r = 0
    for i in nums:
        r = i ^ r
    return r
