# 56
# TC : O(n)
# SC : O(n)
"""
The key point is to sort the list first
"""


def merge(intervals):
    intervals.sort(key=lambda i:i[0])
    result = [intervals[0]]
    prev = result[-1]
    for idx in range(1, len(intervals)):
        curr = intervals[idx]
        if prev[0] <= curr[0] <= prev[1]:
            result[-1] = [prev[0], max(prev[1], curr[1])]
        else:
            result.append(curr)
        prev = result[-1]
    return result
