from typing import List

# 14


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    pref_len = len(prefix)
    for i in range(1, len(strs)):
        while prefix and prefix != strs[i][:pref_len]:
            prefix = prefix[:-1]
            pref_len = len(prefix)
        if not prefix:
            break
    return prefix
