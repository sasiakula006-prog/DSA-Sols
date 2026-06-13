class Solution(object):
    def minDistance(self, word1, word2):
        if word1 == word2:
            return 0
        m = len(word1)
        n = len(word2)
        dp = [[-1]*(n) for _ in range(m)]
        def f(i,j):
            if i == m:
                return n-j
            if j==n:
                return m-i
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j] = f(i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j] = 1+min(f(i+1,j),f(i,j+1),f(i+1,j+1))
                return dp[i][j]
        return f(0,0)