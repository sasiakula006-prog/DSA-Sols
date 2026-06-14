class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        cur = prev = [-1]*2
        prev[0] = 0
        prev[1] = -prices[0]
        for i in range(1,n):
            cur[0] = max(prices[i]-fee+prev[1],prev[0])
            cur[1] = max(-prices[i]+prev[0],prev[1])
            prev = cur
        return max(prev[0],prev[1])
