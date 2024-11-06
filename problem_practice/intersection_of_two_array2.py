from typing import List

# 350
# TC : O(a) => a is the smaller length,
# but if the sorting algorithm is counted then O(alog(a)) + O(blog(b)) + O(a)
# SC : O(a) => a is the smaller length
"""
Sort input array first, then use 2-way merge method to get the answer
"""


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        elif nums1[i] == nums2[j]:
            result.append(nums1[i])
            i+=1
            j+=1
        else:
            j+=1
    return result
