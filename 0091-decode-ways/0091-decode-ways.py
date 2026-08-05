class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for _ in range(n)]
        def f(i):
            if i==n:
                return 1
            if dp[i] !=-1:
                return dp[i]
            p1,p2=0,0
            if s[i] != '0':
                p1 = f(i+1)
                if i<=n-2 and 1<=int(s[i:i+2])<=26:
                    p2 = f(i+2)
            dp[i] = p1+p2
            return p1+p2
        return f(0)