class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n==1:
            return nums[-1]
        # recursive sol didn't work tho
        '''ans = [0]
        def solve(i,s,ans):
            if i<n-2:
                for j in range(2,n-i):
                    solve(i+j,s+nums[i+j],ans)
            else:
                if s>ans[-1]:
                    ans.append(s)
        solve(0,nums[0],ans)
        solve(1,nums[1],ans)
        return ans[-1]'''
        dp = [nums[0],nums[1]]
        for i in range(2,n):
            dp.append(max(dp[:-1])+nums[i])
        return max(dp.pop(),dp.pop())