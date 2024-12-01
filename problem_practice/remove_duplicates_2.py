# 80
# TC : O(N)
# SC : O(1)


def removeDuplicates(nums) -> int:
      l = len(nums)
      k = 1
      curr = nums[-1]
      for i in range(l-2,-1,-1):
          if nums[i] != curr:
              k = 1
              curr = nums[i]
              continue
          k += 1
          if k > 2:
              del nums[i]

      return len(nums)
