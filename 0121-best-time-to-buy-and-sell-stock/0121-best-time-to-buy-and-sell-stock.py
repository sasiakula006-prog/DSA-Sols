class Solution(object):
    def maxProfit(self, prices):
        mini = prices[0]
        max_pro = 0
        l = len(prices)
        for i in range(l):
            max_pro = max(max_pro,prices[i] - mini)
            mini = min(mini,prices[i])
        return max_pro