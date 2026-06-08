class Solution(object):
    def uniquePaths(self, m, n):
        dic = [(0,1),(1,0)]
        dp = [[0]*n for _ in range(m)]
        def solve(i,j):
            if i == m-1 and j== n-1:
                return 1
            if dp[i][j]:
                return dp[i][j]
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if ni <m and nj < n:
                    dp[i][j] += solve(ni,nj)
            return dp[i][j]
        return solve(0,0)