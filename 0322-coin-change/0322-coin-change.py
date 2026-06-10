class Solution(object):
    def coinChange(self, coins, amount):
        l = len(coins)
        dp = [[-1]*(amount+1) for _ in range(l)]
        '''def f(i,a):
            if i ==l-1:
                if not a%coins[-1]:
                    return a/coins[-1]
                else:
                    return 1e9
            if dp[i][a] !=-1:
                return dp[i][a]
            p1 = f(i+1,a)
            p2 = 1e9
            if a>= coins[i]:
                p2 = 1 + f(i,a-coins[i])
            dp[i][a] = min(p1,p2)
            return min(p1,p2)
        ans = f(0,amount)
        if ans >= 1e9:
            return -1
        return ans'''

#tablation
        for t in range(amount+1):
            if not t%coins[0]:
                dp[0][t] = t/coins[0]
            else:
                dp[0][t] = 1e9

        for i in range(1,l):
            for a in range(amount+1):
                p1 = 0 + dp[i-1][a]
                p2 = 1e9
                if coins[i]<=a:
                    p2 = 1+dp[i][a-coins[i]]
                dp[i][a] = min(p1,p2)
        ans = dp[l-1][amount]
        if ans >= 1e9:
            return -1
        return ans