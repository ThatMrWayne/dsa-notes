#151
# TC: O(n)
# SC: O(n)


def reverseWords(s: str) -> str:
    result = []
    s = s.split()
    for idx in range(len(s)-1, -1, -1):
        result.append(s[idx])
    r = " ".join(result)
    return r
