class Solution(object):
    def majorityElement(self, nums):
        d =defaultdict()
        n = len(nums)//2
        for val in nums:
            if val in d:
                d[val]+=1
            else:
                d[val]=1
            if d[val] > n:
                return val
            
        