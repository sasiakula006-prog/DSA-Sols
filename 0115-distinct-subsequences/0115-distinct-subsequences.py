class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[-1]*(n) for _ in range(m)]
        def f(i,j):
            if j == n:
                return 1
            if i==m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            p1,p2 = 0,0
            if s[i]==t[j]:
                p1 = f(i+1,j+1)
            p2 = f(i+1,j)
            dp[i][j] = p1+p2
            return p1+p2
        return f(0,0)