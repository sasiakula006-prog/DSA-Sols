class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        def f(i):
            if i>=n:
                return 0
            if dp[i] !=-1:
                return dp[i]
            p1,p2 = f(i+1),nums[i]+f(i+2)
            dp[i] = max(p1,p2)
            return max(p1,p2)
        return f(0)