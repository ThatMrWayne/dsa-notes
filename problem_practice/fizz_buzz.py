from typing import List

# 412
# TC : O(n)
# SC : O(n)


def fizzBuzz(n: int) -> List[str]:
    ans = []
    for i in range(n):
        fake_idx = i+1
        is_three = fake_idx%3 == 0
        is_five = fake_idx%5 == 0
        if is_three and is_five:
            ans.append("FizzBuzz")
        elif is_three:
            ans.append("Fizz")
        elif is_five:
            ans.append("Buzz")
        else:
            ans.append(str(fake_idx))
    return ans
