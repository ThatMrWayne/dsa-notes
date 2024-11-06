from math import log10

# 326
# TC : O(log3(n))
# SC : O(1)


# more naive way
def isPowerOfThree(n: int) -> bool:
    curr_value, is_valid = 1, True
    while True:
        if curr_value == n:
            is_valid = True
            break
        elif curr_value > n:
            is_valid = False
            break
        curr_value *= 3
    return is_valid


# in case your math is superior
def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    log = log10(n) / log10(3)
    return int(log) == log
