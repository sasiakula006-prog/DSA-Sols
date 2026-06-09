class Solution(object):
    def canPartition(self, nums):
        t0 = sum(nums)
        n = len(nums)
        if t0%2:
            return False
        dp = [[-1]*((t0/2)+1) for _ in range(n)]
        def f(i,t):
            if t == 0 and i:
                return True
            if t<0 or i>=n:
                return False
            if dp[i][t] != -1:
                return dp[i][t]
            if f(i+1,t-nums[i]):
                dp[i][t] = True
                return True
            if f(i+1,t):
                dp[i][t] = True
                return True
            dp[i][t] = False
            return False
        return f(0,t0/2)

        