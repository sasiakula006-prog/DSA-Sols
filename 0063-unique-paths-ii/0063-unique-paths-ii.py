class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[-1][-1]:
            return 0
        dic = [(0,1),(1,0)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        def solve(i,j):
            if i == m-1 and j== n-1:
                return 1
            if dp[i][j] or obstacleGrid[i][j]:
                return dp[i][j]
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if ni <m and nj < n:
                    dp[i][j] += solve(ni,nj)
            return dp[i][j]
        return solve(0,0)
        