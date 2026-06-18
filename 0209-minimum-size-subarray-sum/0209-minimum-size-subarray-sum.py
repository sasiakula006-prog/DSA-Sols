class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l =0
        mini = 1e9
        t = 0
        for r in range(n):
            t+=nums[r]
            while t>=target:
                mini = min(mini,r-l+1)
                t -=nums[l]
                l +=1

        if mini ==1e9:
            return 0
        return mini
        