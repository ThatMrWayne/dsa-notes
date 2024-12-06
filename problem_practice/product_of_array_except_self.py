# 238
# TC: O(n)
# SC: O(n)



def productExceptSelf(nums):
    left_map, right_map = [], []
    for i in range(len(nums)):
        if i == 0:
            left_map.append(1)
        else:
            left_map.append(left_map[-1]*nums[i-1])
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            right_map.append(1)
        else:
            right_map.append(right_map[-1]*nums[i+1])
    right_map.reverse()
    result = []
    for i in range(len(nums)):
        result.append(left_map[i]*right_map[i])
    return result
