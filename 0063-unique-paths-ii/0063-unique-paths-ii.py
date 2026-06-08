class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i][j] =0
                else:
                    right = 0
                    down = 0
                    if j:
                        right += dp[i][j-1]
                    if i:
                        down += dp[i-1][j]
                    dp[i][j] += (right + down)
        return dp[m-1][n-1]