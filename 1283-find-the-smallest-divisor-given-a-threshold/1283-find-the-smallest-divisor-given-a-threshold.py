class Solution(object):
    def smallestDivisor(self, nums, threshold):
        n = len(nums)
        def check(v):
            s = 0
            for i in range(n):
                if nums[i]%v:
                    s += (nums[i]//v)+1
                else:
                    s+= nums[i]//v
            if s<=threshold:
                return True
            return False
        
        l = 1
        h = max(nums)
        ans = h
        while l<=h:
            m = (l+h)//2
            if check(m):
                ans = m
                h = m-1
            else:
                l = m+1
        return ans