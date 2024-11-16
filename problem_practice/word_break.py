# 139
"""
This key point is using dynamic programming.
Start from intuitive solution and draw the diagram, then you could observe the pattern.
"""


def wordBreak(s, wordDict):
    def check_is_valid(start, end, s, wordDict, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        if s[start:end] == "":
            return True

        for i in range(start+1, end+1):
            if s[start: i] in wordDict:
                memo[(start, i)] = True
                memo[(i, end)] = check_is_valid(i, end, s, wordDict, memo)
                if memo[(i, end)]:
                    return True

        return False

    wordDict = set(wordDict)
    record = dict()
    start, end = 0, len(s)
    is_valid = check_is_valid(start, end, s, wordDict, record)
    return is_valid
