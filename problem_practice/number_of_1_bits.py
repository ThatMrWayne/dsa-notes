# 191
# TC : O(1) with bits operation
# SC : O(1)


# more naive way
def hammingWeight(n: int) -> int:
    cnt = 0
    while True:
        remaining_part = n % 2
        if remaining_part == 1:
            cnt += 1
        int_part = n // 2
        if int_part == 0:
            break
        n = int_part
    return cnt


# with bits operation
def hammingWeight(n: int) -> int:
    cnt = 0
    for i in range(31):
        if (n>>i) & 1:
            cnt += 1
    return cnt
