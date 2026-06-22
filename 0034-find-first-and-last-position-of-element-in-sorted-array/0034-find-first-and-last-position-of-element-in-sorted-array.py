class Solution(object):
    def lower(self, nums, x):
        lo = 0
        hi = len(nums)-1
        ans = hi+1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid]>=x:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
    def searchRange(self, nums, target):
        u = self.lower(nums,target+1)-1
        l = self.lower(nums,target)
        if l<=u:
            return [l,u]
        return [-1,-1]