# 290


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        m1, m2 = dict(), dict()
        for i in range(len(pattern)):
            if pattern[i] in m1:
                if m1[pattern[i]] != s[i]:
                    return False
            if s[i] in m2:
                if m2[s[i]] != pattern[i]:
                    return False
            m1[pattern[i]] = s[i]
            m2[s[i]] = pattern[i]
        return True
