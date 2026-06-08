class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n==1:
            return nums[-1]
        def solve(nums):
            prev1 = 0
            prev2 = 0
            for val in nums:
                cur = max(prev1,prev2+val)
                prev2 = prev1
                prev1 = cur
            return cur
        return max(solve(nums[:-1]),solve(nums[1:]))
        