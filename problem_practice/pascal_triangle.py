from typing import List

# 118
# TC : O(n^2)
# SC : O(n^2)


def generate(numRows: int) -> List[List[int]]:
    result = [[1]]
    if numRows == 1:
        return result
    for i in range(1, numRows):
        curr = [1]
        pre = result[i-1]
        for j in range(len(pre)-1):
            curr.append(pre[j]+pre[j+1])
        curr.append(1)
        result.append(curr)
    return result
