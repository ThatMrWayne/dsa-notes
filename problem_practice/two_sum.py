# 1
# TC : O(n)
# SC : O(n)


def twoSum(nums, target: int):
    map = {}
    for i in range(0, len(nums)):
        s = target - nums[i]
        if s in map:
            return [i, map[s]]
        else:
            map[nums[i]] = i

