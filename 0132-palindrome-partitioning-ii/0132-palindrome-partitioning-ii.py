class Solution(object):
    def minCut(self, s):
        n = len(s)
        def ispal(i,j):
            if s[i:j+1] == s[i:j+1][::-1]:
                return True
            return False
        if ispal(0,n-1):
            return 0
        dp = [-1]*n 
        def f(i):
            if i==n:
                return 0
            if dp[i] != -1:
                return dp[i]
            mini = 1e9
            for j in range(i,n):
                if ispal(i,j):
                    c = 1+f(j+1)
                    mini = min(mini,c)
            dp[i] = mini
            return mini
        return f(0)-1
        