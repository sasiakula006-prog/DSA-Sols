class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        '''dp = [[-1]*(n) for _ in range(m)]
        def f(i,j):
            if j == n:
                return 1
            if i == m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            p1,p2 = 0,0
            if s[i]==t[j]:
                p1 = f(i+1,j+1)
            p2 = f(i+1,j)
            dp[i][j] = p1+p2
            return p1+p2
        return f(0,0)'''
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                p1,p2 = 0,0
                if s[i-1] == t[j-1]:
                    p1 = dp[i-1][j-1]
                p2 = dp[i-1][j]
                dp[i][j] = p1+p2
        return dp[m][n]