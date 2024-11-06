# 387
# TC : O(n)
# SC : O(n)


def firstUniqChar(s: str) -> int:
    memo = {}
    for i in s:
        memo[i] = memo.get(i, 0) + 1

    for i in range(len(s)):
        if memo[s[i]] == 1:
            return i
    return -1
