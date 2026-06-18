class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l =0
        mini = 1e9
        t = 0
        for r in range(n):
            t+=nums[r]
            if t>= target:
                while t>=target:
                    t -=nums[l]
                    l +=1
                if t+nums[l-1]>=target and mini>(r-l+2):
                    mini = r-l+2
        if mini ==1e9:
            return 0
        return mini
        