class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        s = sum(nums)
        l = 2*s+1
        dp = [[-1]*(l) for _ in range(n)]
        def f(i,t):
            if i==n:
                if t==target:
                    return 1
                else:
                    return 0
            if dp[i][t] !=-1:
                return dp[i][t]
            p1 = f(i+1,t+nums[i])
            p2 = f(i+1,t-nums[i])
            dp[i][t]=p1+p2
            return p1+p2
        return f(0,0)