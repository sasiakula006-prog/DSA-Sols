class Solution(object):
    def nextGreaterElements(self, nums):
        '''ans =[]
        for i in range(len(nums)):
            f = False
            for val in nums[i+1:] + nums:
                if val > nums[i]:
                    ans.append(val)
                    f = True
                    break
            if not f:
                ans.append(-1)
        return ans'''
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
        
