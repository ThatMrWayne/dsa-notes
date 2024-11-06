# 70
# TC : O(n)
# SC : O(n)
"""
Use bottom-up dynamic programming
"""

def climbStairs(n: int) -> int:
    records = [1,2]
    for i in range(2, n):
        records.append(records[i-1] + records[i-2])
    return records[n-1]
