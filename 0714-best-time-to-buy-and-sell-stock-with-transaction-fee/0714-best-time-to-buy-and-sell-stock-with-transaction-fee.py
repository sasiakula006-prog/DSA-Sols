class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        def f(i,b):
            if i == n:
                return 0
            if dp[i][b] != -1:
                return dp[i][b]
            if b:
                dp[i][1] = max(-prices[i]+f(i+1,0),f(i+1,1))
                return dp[i][1]
            else:
                dp[i][0] = max(prices[i]-fee+f(i+1,1),f(i+1,0))
                return dp[i][0]
        return f(0,1)