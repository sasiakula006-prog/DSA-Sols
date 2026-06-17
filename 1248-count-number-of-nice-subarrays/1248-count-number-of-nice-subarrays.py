class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        def f(g):
            l = r =0
            cnt = 0
            t = 0
            while r<n:
                t += (nums[r]%2)
                while t>g:
                    t -= (nums[l]%2)
                    l +=1
                cnt += (r-l+1)
                r+=1
            return cnt
        return f(k)-f(k-1)