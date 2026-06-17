class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        n =  len(nums)
        def f(g):
            if g<0:
                return 0
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
        return f(goal)-f(goal-1)