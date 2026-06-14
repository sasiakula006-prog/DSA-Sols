class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]
        def f(i,b,t):
            if i == n:
                return 0
            if not t:
                return 0
            if dp[i][b][t] != -1:
                return dp[i][b][t]
            if b:
                dp[i][1][t] = max(-prices[i]+f(i+1,0,t),f(i+1,1,t))
                return dp[i][1][t]
            else:
                dp[i][0][t] = max(prices[i]+f(i+1,1,t-1),f(i+1,0,t))
                return dp[i][0][t]
        return f(0,1,2)        