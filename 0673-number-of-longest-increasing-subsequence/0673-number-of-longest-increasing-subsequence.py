class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        maxi= 0
        dp = [1]*n
        c1 = [1]*n
        c0 = 0
        for i in range(n):
            for p in range(i):
                if nums[i]>nums[p]:
                    if dp[i]<1+dp[p]:
                        dp[i] = 1+dp[p]
                        c1[i] = c1[p]
                    elif dp[i]==1+dp[p]:
                        c1[i] += c1[p]
            if dp[i]>maxi:
                maxi = dp[i]
                c0 = c1[i]
            elif dp[i]==maxi:
                c0 += c1[i]
        return c0