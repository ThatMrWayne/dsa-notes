from typing import List

# 219
# TC: O(n)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = dict()
        for i in range(len(nums)):
            if nums[i] not in memo:
                memo[nums[i]] = i
            else:
                if i-memo[nums[i]] <= k:
                    return True
                else:
                    memo[nums[i]] = i
        return False
