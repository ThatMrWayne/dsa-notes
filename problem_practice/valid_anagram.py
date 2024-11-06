from collections import defaultdict
# 242
# TC : O(a + b)
# SC : O(n)


def isAnagram(s: str, t: str) -> bool:
    is_anagram = True
    memo = defaultdict(int)
    for i in s:
        memo[i] += 1
    for i in t:
        if i not in memo:
            is_anagram = False
            break
        memo[i] -= 1
    if not is_anagram:
        return False
    else:
        result = set(list(memo.values()))
        is_anagram = False if len(result - {0,}) > 0 else True
        return is_anagram
