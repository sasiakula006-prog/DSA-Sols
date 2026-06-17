class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def f(nums,g):
            if g<0:
                return 0
            n =  len(nums)
            l=r=0
            t = 0
            cnt = 0
            while r<n:
                t += nums[r]
                while t>g:
                    t -= nums[l]
                    l +=1
                cnt += (r-l+1)
                r+=1
            return cnt
        return f(nums,goal)-f(nums,goal-1)