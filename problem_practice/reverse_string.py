from typing import List

# 344
# TC : O(n)
# SC : O(1)


def reverseString(s: List[str]) -> None:
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
