from typing import List

# 189
# TC : O(n)
# SC : O(n)
"""
k = 3
[1,2,3,4,5,6,7] => [1,2,3,4,5,6,7,1,2,3,4] => [5,6,7,1,2,3,4]
"""


def rotate(nums: List[int], k: int) -> None:
    k = k%len(nums)
    length = len(nums)
    for i in range(length-k):
        nums.append(nums[i])
    del nums[:length-k]
