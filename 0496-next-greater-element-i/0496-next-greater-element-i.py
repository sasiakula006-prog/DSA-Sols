class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        d = {}
        l = []
        ans =[]
        for val in reversed(nums2):
            while l and l[-1] < val:
                l.pop()
            if l:
                d[val] = l[-1]
            else:
                d[val] =-1
            l.append(val)
        
        for val in nums1:
            ans.append(d[val])
        return ans
        