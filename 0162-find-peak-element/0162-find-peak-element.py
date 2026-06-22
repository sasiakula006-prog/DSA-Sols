class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        l = 1
        h = len(nums)-2
        while l<=h:
            m = (l+h)//2
            if nums[m]>nums[m-1] and nums[m]>nums[m+1]:
                return m
            elif nums[m]>nums[m-1]:
                l = m+1
            else:
                h = m-1
        return -1
        