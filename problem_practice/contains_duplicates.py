from typing import List

# 217
# TC : O(n)
# SC : O(n)


def containsDuplicate(nums: List[int]) -> bool:
    memo = set()
    for i in nums:
        if i in memo:
            return True
        memo.add(i)
    return False
