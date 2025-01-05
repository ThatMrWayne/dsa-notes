from typing import List
#150


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in ('+','-','*','/'):
                s.append(int(i))
            else:
                f2 = s.pop()
                f1 = s.pop()
                if i == "+":
                    s.append(f1+f2)
                elif i == "-":
                    s.append(f1-f2)
                elif i == "*":
                    s.append(f1*f2)
                else:
                    s.append(int(f1/f2))
        return s.pop()
