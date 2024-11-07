# 20
# TC : O(n)
# SC : O(n)
"""
The description of this problem is not good enough :(
`[(])` => this is not allowed
"""


def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i in ("(", "[", "{"):
            stack.append(i)
        elif i == ")":
            if not stack or stack.pop() != "(":
                return False
        elif i == "]":
            if not stack or stack.pop() != "[":
                return False
        elif i == "}":
            if not stack or stack.pop() != "{":
                return False
    return False if stack else True
