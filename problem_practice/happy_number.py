# 202
"""
no comment, period.
(who the hell come up with this kind of problem...)
"""


def isHappy(n: int) -> bool:
    memo = set()
    is_happy = True
    while True:
        new_n = 0
        for i in str(n):
            new_n += int(i)**2
        if new_n  == 1:
            is_happy = True
            break
        if new_n in memo:
            is_happy = False
            break
        else:
            memo.add(new_n)
            n = new_n
    return is_happy
