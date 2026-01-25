class Solution(object):
    def nextPermutation(self, nums):
        p =-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                p=i
                break
        if p==-1:
            return nums.sort()
        for i in range(len(nums)-1,p,-1):
            if nums[i] > nums[p]:
                nums[i],nums[p] = nums[p] ,nums[i]
                break
        nums[p+1:] = nums[p+1:][::-1]
        return nums