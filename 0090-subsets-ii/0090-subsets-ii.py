class Solution(object):
    def subsetsWithDup(self, nums):
        L = []
        nums.sort()
        def rey(s,i):
            L.append(s)
            for j in range(i,len(nums)):
                if j >i and nums[j] == nums[j-1]:
                    continue
                rey(s+[nums[j]],j+1)
        rey([],0)
        return L