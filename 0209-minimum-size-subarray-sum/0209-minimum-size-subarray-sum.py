class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l =r =0
        mini = 1e9
        t = 0
        while r<n:
            t+=nums[r]
            if t>= target:
                while t>=target:
                    t -=nums[l]
                    l +=1
                if t+nums[l-1]>=target and mini>(r-l+2):
                    mini = r-l+2
            r +=1
        if mini ==1e9:
            return 0
        return mini
        