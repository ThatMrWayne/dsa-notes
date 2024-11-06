from typing import List

# 169

# TC : O(n)
# SC : O(n)
def majorityElement(nums: List[int]) -> int:
    target_nums = len(nums)//2+1
    r = {}
    for i in nums:
        if i not in r:
            r[i] = 1
        else:
            r[i] += 1
        if r[i] >= target_nums:
            return i


# TC : O(n)
# SC : O(1)
def majorityElement(nums) -> int:
    result, majority = 0, 0
    for i in nums:
        if majority == 0:
            result = i
        if majority == i:
            majority += 1
        else:
            majority -= 1
    return result
