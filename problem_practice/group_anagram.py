from typing import List
from collections import defaultdict

# 49


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        result = []
        t = []
        for i in range(len(strs)):
            t.append(''.join(sorted(strs[i])))
        for i in range(len(t)):
            memo[t[i]].extend([i,])
        for v in memo.values():
            temp = []
            for idx in v:
                temp.append(strs[idx])
            result.append(temp)
        return result
