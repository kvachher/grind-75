class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        q = collections.deque()
        for i in range(m) : 
            for j in range(n) : 
                if mat[i][j] == 0 : 
                    q.append((i, j))
                else : 
                    mat[i][j] = float('inf')

        while q : 
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] : 
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[x][y] + 1 : 
                    q.append((nx, ny))
                    mat[nx][ny] = mat[x][y] + 1
        return mat
