class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def f(s):
            if s==0:
                return 1
            if dp[s] !=-1:
                return dp[s]
            p1,p2 = 0,0
            if s>=1:
                p1 = f(s-1)
            if s>=2:
                p2 = f(s-2)
            dp[s] = p1+p2
            return p1+p2
        return f(n)
