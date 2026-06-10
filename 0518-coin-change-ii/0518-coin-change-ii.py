class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        '''def f(i,a):
            if i == n-1:
                if not a%(coins[i]):
                    return 1
                else:
                    return 0
            if dp[i][a] !=-1:
                return dp[i][a]
            p1 = f(i+1,a)
            p2 = 0
            if a>= coins[i]:
                p2 = f(i,a-coins[i])
                dp[i][a] = p1+p2
            return p1+p2
        return f(0,amount)'''
        for a in range(amount+1):
            if a%coins[0]:
                dp[0][a] = 0
            else:
                dp[0][a] = 1
        for i in range(1,n):
            for a in range(amount+1):
                p1 = dp[i-1][a]
                p2 = 0
                if a>=coins[i]:
                    p2 = dp[i][a-coins[i]]
                dp[i][a]=p1+p2
        return dp[n-1][amount]
        