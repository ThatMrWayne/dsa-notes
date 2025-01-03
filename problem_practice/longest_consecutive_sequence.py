#128


class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        r,curr = 1, 1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                curr+=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr=1
            r = curr if curr > r else r
        return r
