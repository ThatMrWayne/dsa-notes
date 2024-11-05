from typing import List

# 198
# TC : O(n)
# SC : O(n)
"""
Use bottom-up dynamic programming.
"""


def rob(nums: List[int]) -> int:
    best_sol = dict()
    best_sol[0] = 0
    best_sol[1] = nums[0]
    for i in range(2, len(nums)+1):
        nums_idx = i - 1
        position_best_sol = max(nums[nums_idx]+best_sol[i-2], best_sol[i-1])
        best_sol[i] = position_best_sol

    return best_sol[len(nums)]
