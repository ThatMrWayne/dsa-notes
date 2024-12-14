# 6


def convert(s: str, numRows: int) -> str:
    memo = []
    for _ in range(numRows):
        memo.append([])
    idx_list = []
    for i in range(numRows):
        idx_list.append(i)
    for j in range(numRows-2, 0, -1):
        idx_list.append(j)
    length = len(idx_list)
    for idx in range(len(s)):
        position = idx%length
        memo[idx_list[position]].append(s[idx])
    r = []
    for i in memo:
        r+=i
    return ''.join(r)
