class Solution(object):
    def splitArray(self, nums, k):
        n = len(nums)
        def check(a):
            nd = 1
            s = 0
            for val in nums:
                if val>a:
                    return False
                if s+val>a:
                    nd+=1
                    s = 0
                s+=val
            if nd>k:
                return False
            return True
        l = max(nums)
        h = sum(nums)
        ans = h
        while l<=h:
            mid = (l+h)//2
            if check(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans
        