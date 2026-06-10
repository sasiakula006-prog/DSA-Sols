class Solution(object):
    def coinChange(self, coins, amount):
        l = len(coins)
        dp = [[-1]*(amount+1) for _ in range(l)]
        def f(i,a):
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
        return ans