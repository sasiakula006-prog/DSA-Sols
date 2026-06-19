class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        li = n-1
        for i in range(n-2,0,-1):
            if i+nums[i]>=li:
                li = i
        if nums[0]>=li:
            return True
        return False