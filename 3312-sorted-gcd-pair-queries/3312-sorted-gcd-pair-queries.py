class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        gcdPairs = []
        m = max(nums)
        a = [0]*(m+1)
        for num in nums:
            a[num]+=1

        cnt = [0]*(m+1)
        for g in range(m,0,-1):
            c = 0
            for d in range(g,m+1,g):
                c += a[d]
            cnt[g] = (c*(c-1))//2
            for mu in range(2*g,m+1,g):
                cnt[g] -= cnt[mu]

        for i in range(1,m+1):
            cnt[i] += cnt[i-1]
        
        def lowb(val):
            lo,hi = 1,m
            res = hi
            while lo<=hi:
                mid = (lo+hi)//2
                if cnt[mid]>val:
                    res = mid
                    hi = mid-1
                else:
                    lo = mid+1
            return res
        
        l = len(queries)
        ans = [0]*l
        for i in range(l):
            ans[i] = lowb(queries[i])
        return ans
                
            
        