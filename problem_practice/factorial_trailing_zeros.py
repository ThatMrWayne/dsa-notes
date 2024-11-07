# 172
# TC : O(log5(n)) base 5
# SC : O(1)
"""
a pair of 2 and 5 will generate one trailing zero.
chances of appearance of 2 is larger than 5,
so simply calculate number of 5.
"""


# better
def trailingZeroes(n: int) -> int:
    cnt = 0
    curr = n
    while True:
        temp = curr // 5
        if temp == 0:
            break
        else:
            cnt += (temp)
            curr = temp
    return cnt


# worse, cause time limit exceed
def trailingZeroes(n: int) -> int:
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(i*memo[i-1])
    num = memo[n]
    cnt = 0
    if num != 0:
        while True:
            if num % 10 == 0:
                cnt += 1
                num = num // 10
            else:
                break
    return cnt
