class Solution(object):
    def productExceptSelf(self, nums):
        l =len(nums)
        ans = [1]*l
        left = 1
        for i in range(l):
            ans[i]*=left
            left *= nums[i]
        
        right = 1
        for i in range(l-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans

        