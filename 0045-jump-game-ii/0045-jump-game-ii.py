class Solution(object):
    def jump(self, nums):
        n = len(nums)
        farthest = 0
        target_node = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            if i==target_node:
                jumps +=1
                target_node = farthest
        return jumps
        