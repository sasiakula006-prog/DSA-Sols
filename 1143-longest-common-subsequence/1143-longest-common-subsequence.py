class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[-1]*(n) for _ in range(m)]
        def f(i,j):
            if i==m or j==n:
                return 0
            if dp[i][j] !=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j] = 1+f(i+1,j+1)
                return dp[i][j] 
            else:
                p1,p2 = f(i+1,j),f(i,j+1)
                dp[i][j] = max(p1,p2)
                return max(p1,p2)
        return f(0,0)