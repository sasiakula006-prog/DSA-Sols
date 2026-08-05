class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(m) for _ in range(n)]
        def f(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            if i==n-1 and j==m-1:
                return 1
            if dp[i][j] !=-1:
                return dp[i][j]
            dp[i][j] = f(i+1,j)+f(i,j+1)
            return dp[i][j]
        return f(0,0)