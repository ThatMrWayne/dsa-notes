from typing import List

# 1
# TC : O(n)
# SC : O(n)


def twoSum(nums: List[int], target: int):
    map = {}
    for i in range(0, len(nums)):
        s = target - nums[i]
        if s in map:
            return [i, map[s]]
        else:
            map[nums[i]] = i
