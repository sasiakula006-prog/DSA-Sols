class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def f(i,b):
            if i==n:
                return 0
            if dp[i][b] != -1:
                return dp[i][b]
            if b:
                dp[i][b] = max(-prices[i]+f(i+1,0),f(i+1,1))
                return dp[i][b]
            else:
                dp[i][b] = max(prices[i]+f(i+1,1),f(i+1,0))
                return dp[i][b]
        return f(0,1)