class Solution(object):
    def countSquares(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        def check(i,j):
            dic = [(-1,0),(0,-1),(-1,-1)]
            mini = 1e9
            for di,dj in dic:
                ni,nj = i+di,j+dj
                mini = min(mini,dp[ni][nj])
            return mini
        t = 0
        for j in range(n):
            dp[0][j] = matrix[0][j]
            t += matrix[0][j]

        for i in range(1,m):
            dp[i][0] = matrix[i][0]
            t+=matrix[i][0]

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]:
                    dp[i][j] = check(i,j)+1
                    t += dp[i][j]
        return t