# 13
# TC : O(n)
# SC : O(n)


def romanToInt(s: str) -> int:
    r = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s = list(s)
    n = 0
    idx_skip = set()
    for i in range(len(s)):
        if i in idx_skip:
            continue
        if i != len(s)-1:
            if (s[i] == 'I' and s[i+1] in ("V", "X")) or \
                (s[i] == 'X' and s[i+1] in ("L", "C")) or \
                (s[i] == 'C' and s[i+1] in ("D", "M")):
                n = n + (r[s[i+1]]-r[s[i]])
                idx_skip.add(i+1)
            else:
                n += r[s[i]]
        else:
            n += r[s[i]]
    return n
