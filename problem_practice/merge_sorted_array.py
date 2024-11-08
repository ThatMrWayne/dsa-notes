# 88
"""
The accept_range make sure the comparing element from nums1 is the one that
needs compared.
If it is out of accept_range, the comparing element from nums1 is 0 that should be ignored.
"""


def merge(nums1, m ,nums2, n):
    if n == 0:
        return nums1

    accept_range = m
    i, j = 0, 0
    while j < n:
        if i < accept_range:
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                i += 1
                j += 1
                accept_range += 1
            elif nums2[j] > nums1[i]:
                i += 1
        else:
            nums1.insert(i, nums2[j])
            nums1.pop()
            i += 1
            j += 1
            accept_range += 1
    return nums1
