class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        if s==s[::-1]:
            return 0
        dp = [[-1]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[0][i]=0
            dp[i][0]=0
        def f(s1,s2,m,n):
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            return dp[-1][-1]
        l = f(s,s[::-1],n,n)
        return n-l