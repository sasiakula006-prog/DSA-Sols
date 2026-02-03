class Solution(object):
    def sortColors(self, nums):
        j = len(nums)-1
        while j>=0:
            if nums[j] ==1:
                nums.remove(1)
                nums.append(1)
            j -=1
        j = len(nums) -1
        while j>=0:
            if nums[j] ==2:
                nums.remove(2)
                nums.append(2)
            j -=1

        

        