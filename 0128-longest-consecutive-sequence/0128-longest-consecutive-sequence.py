class Solution(object):
    def longestConsecutive(self, nums):
        l = set(nums)
        maxi = 0
        for val in l:
            c=0
            v = val
            if v-1 not in l:
                while v in l:
                    c+=1
                    v+=1
            if c>maxi:
                maxi = c
        return maxi 
        