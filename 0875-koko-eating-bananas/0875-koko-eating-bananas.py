class Solution(object):
    def minEatingSpeed(self, piles, h):
        m = max(piles)
        n =len(piles)
        def check(k):
            t = 0
            i = 0
            for i in range(n):
                if piles[i]>k:
                    if piles[i]%k:
                        t+= (piles[i]//k)+1
                    else:
                        t+=(piles[i]//k)
                else:
                    t+=1
            if t<=h:
                return True
            return False
        l = 1
        hi = m
        ans = m
        while l<=hi:
            mid = (l+hi)//2
            if check(mid):
                ans = mid
                hi = mid-1
            else:
                l = mid+1
        return ans