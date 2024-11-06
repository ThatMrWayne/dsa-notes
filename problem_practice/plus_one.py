from typing import List

# 66
# TC : O(n)
# SC : O(1)


def plusOne(self, digits: List[int]) -> List[int]:
    should_increase = False
    for i in range(len(digits)-1, -1, -1):
        if digits[i] + 1 < 10:
            digits[i] += 1
            break
        else:
            digits[i] = 0
            if i == 0:
                should_increase = True
    if should_increase:
        digits = [1,] + digits
    return digits
