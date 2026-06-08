class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n==1:
            return nums[-1]
        # recursive sol got runtime error tho
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
        prev1  = 0
        prev2 = 0
        for val in nums:
            cur = max(prev1,prev2+val)
            prev2 = prev1
            prev1 = cur
        return cur