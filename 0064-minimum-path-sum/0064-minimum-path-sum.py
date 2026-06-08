class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        infi = float('inf')
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j]+=grid[i][j]
                if i==0 and j==0:
                    continue
                left = up = infi
                if i:
                    left =dp[i-1][j]
                if j:
                    up = dp[i][j-1]
                dp[i][j] += min(left,up)
        return dp[m-1][n-1]
        