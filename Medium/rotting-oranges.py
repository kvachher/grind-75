class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []
        visited = set()
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(q, visited, minutes):
            if not q:
                return minutes
            new_q = []
            for curr_i, curr_j in q:
                for x, y in directions:
                    ni, nj = curr_i + x, curr_j + y
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in visited:
                        grid[ni][nj] = 2
                        visited.add((ni, nj))
                        new_q.append((ni, nj))
            if not new_q:
                return minutes
            return bfs(new_q, visited, minutes + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        if q:
            ans = bfs(q, visited, 0)
        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1
        return ans
