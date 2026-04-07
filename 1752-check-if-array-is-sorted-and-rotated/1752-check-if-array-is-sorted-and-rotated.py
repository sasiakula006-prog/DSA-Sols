class Solution(object):
    def check(self, nums):
        l = nums[:]
        l.sort()
        for i in range(len(l)):
            nums = nums[1:]+[nums[0]]
            if nums==l:
                return True
        return False