class Solution(object):
    def subarraySum(self, nums, k):
        
        d = {0:1}
        c=0
        s=0
        for i in range(len(nums)):
            s += nums[i]
            if s-k in d:
                c+= d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return c
            