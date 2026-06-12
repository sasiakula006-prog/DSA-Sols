class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(n+1):
            dp[0][i] = 0
        def f(s1,s2,m,n):
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            return dp[-1][-1]
        l = f(word1,word2,m,n)
        return m+n-2*l