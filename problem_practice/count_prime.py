# 204
"""
I have no idea how is this has anything to do with daily programming...
厄拉托西尼篩法
"""


def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    cnt = 0
    memo = [True]*n
    for i in range(2, n):
        if not memo[i]:
            continue
        cnt += 1
        for j in range(i*i, n, i):
            memo[j] = False

    return cnt
