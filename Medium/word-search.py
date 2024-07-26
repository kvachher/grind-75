class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(board)
        n = len(board[0])
        found = False

        def dfs(board, window, i, j, word, visited) :
            if window == word :
                return True
            elif window == word[:len(window)] :
                visited.add((i, j))
                for d in directions : 
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if new_i < m and new_j < n and new_i >= 0 and new_j >= 0 and (new_i, new_j) not in visited : 
                        if dfs(board, window + board[new_i][new_j], new_i, new_j, word, visited) : 
                            return True
                visited.remove((i, j))
                return False

        for i in range(m) : 
            for j in range(n) : 
                if board[i][j] == word[0] and not found:
                    found = dfs(board, board[i][j], i, j, word, set())
        return found
