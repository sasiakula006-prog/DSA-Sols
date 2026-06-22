class Solution(object):
    def findMin(self, nums):
        mini = 5e4
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            mini = min(mini,nums[mid])
            if nums[mid]>nums[h]:
                l = mid+1
            else:
                h = mid-1
        return mini