class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[[-1]*2 for _ in range(n)]  for _ in range(m)]
        dic = [(0,1),(1,0)]
        mod = 10**9+7
        def f(i,j,d):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j][d] !=-1:
                return dp[i][j][d]
            if grid[i][j] == 1:
                if i+(1-d)<m and j+d <n and dp[i+(1-d)][j+d][1-d] == -1:
                    dp[i][j][d] = f(i+(1-d),j+d,1-d)
                else:
                   dp[i][j][d] =  0
            else:
                v = 0
                for di,dj in dic:
                    v += f(i+di,j+dj,di)
                dp[i][j][d] = v
            return dp[i][j][d]
        return (f(0,0,0))%mod