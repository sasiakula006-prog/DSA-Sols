class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        if p == ["*"]*n:
            return True
        dp = [[-1]*n for _ in range(m)]
        def f(i,j,s,p,dp):
            if i<0 and j<0:
                return True
            if j<0 and i>=0:
                return False
            if i<0 and j>=0:
                for k in range(j+1):
                    if p[k] != "*":
                        return False
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i]==p[j] or p[j]=="?":
                dp[i][j] = f(i-1,j-1,s,p,dp)
                return dp[i][j]
            else:
                if p[j]== "*":
                    dp[i][j] = f(i-1,j,s,p,dp) or f(i,j-1,s,p,dp)
                    return dp[i][j]
                dp[i][j] == False
                return False
        return f(m-1,n-1,s,p,dp)