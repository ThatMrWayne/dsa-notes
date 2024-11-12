# 28
# TC : O(n)
# SC : O(1)


def strStr(haystack: str, needle: str) -> int:
    length = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+length] == needle:
            return i
    return -1
