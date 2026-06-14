class Solution(object):
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        dp = [1]*n
        h = {}
        maxi = 0
        for i in range(n):
            h[i]=i
            for p in range(i):
                if not nums[i]%nums[p]:
                    if dp[i] < 1+dp[p]:
                        dp[i] = 1+dp[p]
                        h[i] = p
            if dp[i]>maxi:
                maxi = dp[i]
                last = i 
        ans = []
        ans.append(nums[last])
        while h[last] !=last:
            last = h[last]
            ans.append(nums[last])
        ans.reverse()
        return ans
        