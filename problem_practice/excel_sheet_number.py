# 171
# TC : O(n)
# SC : O(1)
"""
use 26 as base like bit system
"""


def titleToNumber(columnTitle: str) -> int:
    result = 0
    n=len(columnTitle)-1
    for i in columnTitle:
        digit = ord(i)-64
        result += digit * (26**n)
        n-=1
    return result