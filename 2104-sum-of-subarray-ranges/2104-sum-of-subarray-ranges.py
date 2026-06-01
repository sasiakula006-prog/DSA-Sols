class Solution(object):
    def subArrayRanges(self, nums):
        t =0
        max_sum = [0]*len(nums)
        min_sum = [0]*len(nums)
        max_stack = []
        min_stack = []
        for i in range(len(nums)):
            while max_stack and nums[max_stack[-1]]<nums[i]:
                max_stack.pop()
            if max_stack:
                j = max_stack[-1]
            else:
                j = -1
            max_sum[i] = max_sum[j]+(i-j)*nums[i]
            max_stack.append(i)
        maxi = sum(max_sum)

        for i in range(len(nums)):
            while min_stack and nums[min_stack[-1]]>nums[i]:
                min_stack.pop()
            if min_stack:
                j = min_stack[-1]
            else:
                j = -1
            min_sum[i] = min_sum[j]+(i-j)*nums[i]
            min_stack.append(i)
        mini = sum(min_sum)
        return maxi - mini
        