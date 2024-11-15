from collections import deque

# 200
# TC : O(r*c)
# SC : O(r*c)
"""
Using BFS from a point to scan four dirction until it can't go on anymore
"""


def numIslands(grid):
    island_cnt = 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    q = deque()

    def bfs(r, c):
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0 ,1], [0, -1]]
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                island_cnt += 1
                bfs(r, c)

    return island_cnt
