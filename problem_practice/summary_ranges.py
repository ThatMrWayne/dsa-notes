from typing import List
#228


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        a = b = 0
        while b < len(nums):
            if nums[a] == nums[b]:
                b +=1
            elif nums[b]-nums[b-1] == 1:
                b += 1
            else:
                if nums[a] == nums[b-1]:
                    temp = f"{nums[a]}"
                else:
                    temp = f"{nums[a]}->{nums[b-1]}"
                result.append(temp)
                a = b
        if nums[b-1] == nums[a]:
            result.append(f"{nums[a]}")
        else:
            result.append(f"{nums[a]}->{nums[b-1]}")
        return result
