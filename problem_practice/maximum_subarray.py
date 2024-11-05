from typing import List

# 53
# TC : O(n)
# SC : O(n)
"""
Use bottom-up dynamic programming without recursion.
Slowly build up to get the answer.
"""


def maxSubArray(nums: List[int]) -> int:
    memo = {len(nums)-1: nums[-1]}
    max_val = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        memo[i] = max(nums[i], nums[i]+memo[i+1])
        if memo[i] > max_val:
            max_val = memo[i]
    return max_val
