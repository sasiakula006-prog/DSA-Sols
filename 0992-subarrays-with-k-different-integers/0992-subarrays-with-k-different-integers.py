class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        n = len(nums)
        def f(c):
            l = 0
            cnt = 0
            d = defaultdict(int)
            for r in range(n):
                d[nums[r]] +=1
                while len(d)>c:
                    d[nums[l]] -=1
                    if d[nums[l]] ==0:
                        del d[nums[l]]
                    l +=1
                cnt+=r-l+1
            return cnt
        return f(k)-f(k-1)