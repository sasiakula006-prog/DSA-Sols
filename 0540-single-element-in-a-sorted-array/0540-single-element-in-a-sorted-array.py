class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 1
        h = len(nums)-2
        if len(nums)==1:
            return nums[-1]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        while l<=h:
            m = (l+h)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if m%2:
                if nums[m-1] != nums[m]:
                    h = m-1
                else:
                    l = m+1
            else:
                if nums[m+1] != nums[m]:
                    h = m-1
                else:
                    l = m+1
        return -1
