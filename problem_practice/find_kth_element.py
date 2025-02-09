# 215
#TC: O(n)
#SC: O(1)
'''
use quick select algorithm
'''

class Solution:
    def find_kth(self, nums, left, right, target_idx):
        if left == right:
            return nums[left]

        pivot_idx = ((right-left)//2)+left
        pivot_val = nums[pivot_idx]
        i = left
        lt = left
        gt = right
        while i <= gt:
            if nums[i] < pivot_val:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt+=1
                i+=1
            elif nums[i] == pivot_val:
                i+=1
            elif nums[i] > pivot_val:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt-=1

        if lt <= target_idx <= gt:
            return nums[lt]
        elif target_idx < lt:
            right = lt-1
            return self.find_kth(nums, left, right, target_idx)
        elif target_idx > gt:
            left = gt+1
            return self.find_kth(nums, left, right, target_idx)

    def findKthLargest(self, nums, k) -> int:
        left, right = 0, len(nums)-1
        target_idx = len(nums)-k
        return self.find_kth(nums, left, right, target_idx)
