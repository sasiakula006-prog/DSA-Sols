class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        inf = float('inf')
        def f(i,a):
            if a==0:
                return 0
            if i==n:
                return inf
            if dp[i][a] !=-1:
                return dp[i][a]
            p1,p2 = f(i+1,a),inf
            if a>=coins[i]:
                p2 = 1+f(i,a-coins[i])
            dp[i][a] = min(p1,p2)
            return min(p1,p2)
        ans = f(0,amount)
        if ans >= inf:
            return -1
        return ans