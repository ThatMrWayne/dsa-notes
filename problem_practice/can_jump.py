# 55
# TC : O(n)
# SC : O(1)
'''
The thought of this problem is that
we try to get as far as we can on each element
'''


def can_jump(nums):
    gas = 0
    for i in nums:
        if gas < 0:
            return False
        if i > gas:
            gas = i
        i -= 1
    return True
