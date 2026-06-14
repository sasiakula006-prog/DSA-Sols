class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        '''def f(i,b):
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
        return f(0,1)'''
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(prices[i]+dp[i-1][1],dp[i-1][0])
            dp[i][1] = max(-prices[i]+dp[i-1][0],dp[i-1][1])
        return max(dp[n-1][0],dp[n-1][1])
