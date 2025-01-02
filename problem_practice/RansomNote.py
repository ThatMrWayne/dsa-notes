from collections import defaultdict
# 383


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memo = defaultdict(int)
        for s in magazine:
            memo[s]+=1
        for s in ransomNote:
            if s not in memo or memo[s] == 0:
                return False
            else:
                memo[s]-=1
        return True
