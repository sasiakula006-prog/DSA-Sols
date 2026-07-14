class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m,n = len(grid),len(grid[0])
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if dp[j]+1>dp[i]:
                    f = True
                    for r in range(m):
                        if abs(grid[r][i]-grid[r][j])>limit:
                            f = False
                            break
                    if f:
                        dp[i] = dp[j]+1
        return max(dp)