# 69
# TC : O(logn)
# SC : O(logn)


def mySqrt(x):
    low, high = 0, x
    memo = set()
    if x == 1:
        return 1
    while True:
        curr = (low+high)//2
        square = curr**2
        if curr in memo:
            return curr
        if square == x:
            return curr
        elif square > x:
            high = curr
        else:
            low = curr
        memo.add(curr)
