class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num = 0
        visited = set()
        def bfs(grid, visited, start) : 
            q = [start]
            visited.add(start)
            while q : 
                i, j = q.pop(0)
                for di, dj in directions : 
                    ni = i + di 
                    nj = j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited: 
                        if grid[ni][nj] == "1" :
                            q.append((ni, nj))
                            visited.add((ni, nj))
        
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == "1" and (i, j) not in visited : 
                    bfs(grid, visited, (i, j))
                    num += 1
        return num
