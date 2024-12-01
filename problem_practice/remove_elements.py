# 27
# TC : O(n)
# SC : O(n)


def removeElement(nums, val: int) -> int:
    if len(nums) == 0:
        return 0
    k = 0
    m = []
    for i in range(len(nums)):
        if nums[i] != val:
            k += 1
        else:
            m.append(i)

    for i in m[-1::-1]:
        del nums[i]

    return k
