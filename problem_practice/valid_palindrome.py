# 125
# TC : O(n)
# SC : O(n)


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = list(s)
    t = []
    for i in s:
        if (ord('a') <= ord(i) <= ord('z')) or \
            (ord('0') <= ord(i) <= ord('9')):
            t.append(i)
    return t[:] == t[len(t)-1::-1]
