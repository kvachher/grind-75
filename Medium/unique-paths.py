class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m) : 
            for j in range(n) : 
                if i == 0 and j == 0 : 
                    continue
                dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)

        print(dp)
        return dp[m-1][n-1]

# bc -> [0][0] = 1
# recursive step -> +1 unique path to the right and down
