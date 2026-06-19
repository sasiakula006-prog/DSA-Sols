class Solution(object):
    def checkValidString(self, s):
        n=len(s)
        dp = [[-1]*(n+1) for _ in range(n)]
        def f(i,c):
            if i==n:
                if c==0:
                    return True
                else:
                    return False
            if c<0:
                return False
            if dp[i][c] !=-1:
                return dp[i][c]
            if s[i] == '(':
                dp[i][c] = f(i+1,c+1)
                return dp[i][c]
            elif s[i] == ')':
                dp[i][c] = f(i+1,c-1)
                return dp[i][c]
            else:
                if f(i+1,c+1) or f(i+1,c) or f(i+1,c-1):
                    dp[i][c] = True
                    return True
                else:
                    dp[i][c] = False
                    return False
        return f(0,0)