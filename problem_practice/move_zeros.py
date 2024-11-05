from typing import List

# 283
# TC : O(n)
# SC : O(n)


def moveZeroes(nums: List[int]) -> None:
    record = []
    for i in range(0, len(nums)):
        if nums[i] == 0:
            if i == len(nums)-1:
                pass
            else:
                record.append(i)
                nums.append(0)
    for j in range(len(record)-1, -1, -1):
        nums.pop(record[j])
