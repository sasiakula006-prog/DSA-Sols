class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        dp[-1] = 0
        for i in range(n-1,-1,-1):
            p1,p2 = dp[i+1],nums[i]
            if i<=n-2:
                p2 += dp[i+2]
            dp[i] = max(p1,p2)

        return dp[0]