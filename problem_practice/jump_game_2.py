# 45
'''
Using BFS
'''


def jump(nums) -> int:
    if len(nums) == 1:
        return 0
    visited = set()
    memo = [[0]]
    step = 1
    while memo:
        next_level = []
        curr_level = memo.pop()
        for i in curr_level:
            curr_idx = i
            possible_steps = nums[curr_idx]
            if curr_idx+possible_steps >= len(nums)-1:
                return step
            for j in range(curr_idx+1, curr_idx+possible_steps+1):
                if j not in visited:
                    visited.add(j)
                    next_level.append(j)
        memo.append(next_level)
        step += 1
