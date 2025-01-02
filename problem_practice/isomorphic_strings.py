# 205


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd, td = {}, {}
        for i in range(len(s)):
            if s[i] in sd:
                if sd[s[i]] != t[i]:
                    return False
            if t[i] in td:
                if td[t[i]] != s[i]:
                    return False
            sd[s[i]] = t[i]
            td[t[i]] = s[i]
        return True
